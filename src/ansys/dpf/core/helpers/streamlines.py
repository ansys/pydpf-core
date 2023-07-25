"""Streamlines computation specific helpers.
"""

import numpy as np
import vtk
import warnings

from ansys.dpf.core.common import locations
from ansys.dpf.core.helpers.utils import _sort_supported_kwargs

# class Streamline:
#     """Class to define the Streamline object
#     scripting with `ansys-dpf-core`.
#     """
#
#     def __init__(self, pv_data_set):
#         """Instantiate Streamline
#         from pyvista.PolyData object.
#         This construction is only
#         intended to be used internally.
#
#         Parameters
#         ----------
#         pv_data_set: pyvista.PolyData
#         """
#         _pv_data_set = pv_data_set

def _pvdataset_to_fields(data_set):
    to_return = {}
    cell_points = []
    cell_types = []
    data_arrays = []
    array_names = data_set.array_names
    for n in array_names:
        data_arrays.append(data_set[n])
    for i in range(0, data_set.n_cells):
        cell_points.append(data_set.cell_point_ids(i))
        cell_types.append(data_set.cell_type(i))
    to_return["cell_points"] = cell_points
    to_return["cell_types"] = cell_types
    to_return["points"] = data_set.points
    to_return["array_names"] = array_names
    to_return["data_arrays"] = data_arrays
    return to_return


def _fields_to_pvdataset(fields):
    from ansys.dpf.core.vtk_helper import PyVistaImportError
    try:
        import pyvista as pv
    except ModuleNotFoundError:
        raise PyVistaImportError

    cell_points = fields["cell_points"]
    cell_types = fields["cell_types"]
    points = fields["points"]
    array_names = fields["array_names"]
    data_arrays = fields["data_arrays"]
    ncells = len(cell_types)
    npoints = len(points)
    vpoly = vtk.vtkPolyData()
    vpoints = vtk.vtkPoints()
    vpoints.SetNumberOfPoints(npoints)
    vtk_array_points = pv.convert_array(arr=points)
    vpoints.SetData(vtk_array_points)
    vpoly.SetPoints(vpoints)
    vcells = vtk.vtkCellArray()
    for i in range(0, ncells):
        vcells.InsertNextCell(cell_types[i])
        for pid in cell_points[i]:
            vcells.InsertCellPoint(pid)
    # vtk_array_cell_points = pv.convert_array(arr=cell_points)
    # vcells.SetCells(ncells, vtk_array_cell_points)
    vpoly.SetPolys(vcells)
    pv_poly = pv.wrap(vpoly)
    for ind, n in enumerate(array_names):
        pv_poly[n] = data_arrays[ind]
    return pv_poly


def compute_streamlines(meshed_region, field, **kwargs):
    """Compute the streamlines for a given mesh and velocity
    field.

    Parameters
    ----------
    meshed_region: MeshedRegion
        MeshedRegion the streamline will be computed on.
    field: Field
        Field containing raw vector data the streamline is
        computed from. The data location must be nodal, velocity
        values must be defined at nodes.
    **kwargs : optional
        Additional keyword arguments for the streamline
        computation. More information is available at
        :func:`pyvista.DataSetFilters.streamlines`.

    Returns
    -------
    streamlines: FieldsContainer

    """
    from ansys.dpf.core.vtk_helper import PyVistaImportError
    try:
        import pyvista as pv
    except ModuleNotFoundError:
        raise PyVistaImportError

    # Check velocity field location
    if field.location is not locations.nodal:
        warnings.warn(
            "Velocity field must have a nodal location. Result must be carefully checked."
        )

    # handles input data
    f_name = field.name
    stream_name = "streamlines " + f_name + " (" + str(field.unit) + ")"
    grid = meshed_region.grid
    mesh_nodes = meshed_region.nodes

    ind, mask = mesh_nodes.map_scoping(field.scoping)
    overall_data = np.full((len(mesh_nodes), 3), np.nan)  # velocity has 3 components
    overall_data[ind] = field.data[mask]

    grid.set_active_scalars(None)
    grid[f"{stream_name}"] = overall_data

    # check src request
    return_source = kwargs.pop("return_source", None)

    # filter kwargs
    kwargs_base = _sort_supported_kwargs(bound_method=grid.streamlines, **kwargs)
    kwargs_from_source = _sort_supported_kwargs(
        bound_method=grid.streamlines_from_source, **kwargs
    )
    kwargs_from_source.update(kwargs_base)  # merge both dicts in kwargs_from_source

    if return_source:
        streamlines, src = grid.streamlines(
            vectors=f"{stream_name}",
            return_source=True,
            **kwargs_from_source,
        )
        streamlines = _pvdataset_to_fields(streamlines)
        src = _pvdataset_to_fields(src)
        return streamlines, src
    else:
        streamlines = grid.streamlines(
            vectors=f"{stream_name}",
            **kwargs_from_source,
        )
        streamlines = _pvdataset_to_fields(streamlines)
        return streamlines

