"""Streamlines computation specific helpers.
"""

import numpy as np
import warnings

from ansys.dpf import core as dpf
from ansys.dpf.core.common import (
    DefinitionLabels,
    locations,
    natures,
)
from ansys.dpf.core.elements import element_types
from ansys.dpf.core.helpers.utils import _sort_supported_kwargs


class _PvFieldsContainerBase:
    def __init__(self, data):
        """Instantiate Streamline
        from pyvista.PolyData object.
        This construction is only
        intended to be used internally.

        Parameters
        ----------
        pv_data_set: pyvista.PolyData
        """
        try:
            import pyvista as pv
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "To use streamlines capabilities, please install pyvista "
                "with :\n pip install pyvista>=0.24.0"
            )
        self._pv_data_set = None
        self._streamlines_fc = None
        if isinstance(data, pv.PolyData):
            self._pv_data_set = data
        elif isinstance(data, dpf.FieldsContainer):
            self._streamlines_fc = data
        else:
            raise AttributeError(
                "streamlines must be a pyvista.PolyData or a dpf.FieldsContainer instance."
            )

    def _pv_data_set_to_fc(self):
        """Convert pyvista.PolyData into FieldsContainer."""
        import vtk
        data_set = self._pv_data_set
        cell_points = []
        cell_types = []
        data_arrays = []
        array_names_base = data_set.array_names
        array_names = []
        for n in array_names_base:
            if not "streamlines" in n:
                continue
            array_names.append(n)
            data_arrays.append(data_set[n])
        for i in range(0, data_set.n_cells):
            cell_points.append(data_set.cell_point_ids(i))
            cell_types.append(data_set.cell_type(i))
        points_array = data_set.points

        # compute DPF objects
        cell_types_converted = []
        for c in cell_types:
            if c == vtk.VTK_LINE:
                cell_types_converted.append(element_types.Line2.value)
            elif c == vtk.VTK_POLY_LINE:
                cell_types_converted.append(element_types.EMagLine.value)
        nodes_scoping = dpf.Scoping(location=locations.nodal)
        nodes_scoping.ids = np.arange(1, data_set.n_points + 1)
        streamlines_field = dpf.Field(location=locations.nodal)
        fdef = streamlines_field.field_definition
        fdef.name = array_names[0]
        streamlines_field.scoping = nodes_scoping
        streamlines_field.data = data_arrays[0]
        mesh = dpf.MeshedRegion()
        coords_field = dpf.Field(location=locations.nodal)
        coords_field.scoping = nodes_scoping
        coords_field.data = points_array
        mesh.set_coordinates_field(coords_field)
        elems_scoping = dpf.Scoping(location=locations.elemental)
        elems_scoping.ids = np.arange(1, data_set.n_cells + 1)
        connectivity_field = dpf.PropertyField(location=locations.elemental)
        # connectivity size is different for each element,
        # data array can't be set in once
        for ind, dat in enumerate(cell_points):
            connectivity_field.append(dat, ind + 1)
        elems_types_field = dpf.PropertyField(location=locations.elemental)
        elems_types_field.scoping = elems_scoping
        elems_types_field.data = cell_types_converted
        mesh.nodes.coordinates_field = coords_field
        mesh.elements.connectivities_field = connectivity_field
        mesh.elements.element_types_field = elems_types_field
        streamlines_field.meshed_region = mesh
        fc_to_return = dpf.FieldsContainer()
        fc_to_return.add_label(DefinitionLabels.time)
        fc_to_return.add_field({DefinitionLabels.time: 1}, streamlines_field)

        return fc_to_return

    def _fc_to_pv_data_set(self):
        """Convert FieldsContainer into pyvista.PolyData."""
        fields = self._streamlines_fc

        from ansys.dpf.core.vtk_helper import PyVistaImportError
        try:
            import pyvista as pv
        except ModuleNotFoundError:
            raise PyVistaImportError
        import vtk

        streamlines_field = fields.get_field({DefinitionLabels.time: 1})
        mesh = streamlines_field.meshed_region
        cell_types = mesh.elements.element_types_field.data
        cell_points = []
        conn_field = mesh.elements.connectivities_field
        for i in range(len(cell_types)):
            cell_points.append(conn_field.get_entity_data(i))
        points = mesh.nodes.coordinates_field.data
        array_names = [ streamlines_field.field_definition.name ]
        data_arrays = [ streamlines_field.data ]

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
            this_cell_points = cell_points[i]
            cell_type_id = cell_types[i]
            if cell_type_id == element_types.Line2.value:
                vtk_cell = vtk.vtkLine()
            elif cell_type_id == element_types.EMagLine.value:
                vtk_cell = vtk.vtkPolyLine()
            vtk_cell_pid = vtk_cell.GetPointIds()
            vtk_cell_pid.SetNumberOfIds(len(this_cell_points))
            for ind, pid in enumerate(this_cell_points):
                vtk_cell_pid.SetId(ind, pid)
            vcells.InsertNextCell(vtk_cell)
        vpoly.SetLines(vcells)
        pv_poly = pv.wrap(vpoly)
        for ind, n in enumerate(array_names):
            pv_poly[n] = data_arrays[ind]
        return pv_poly

    def _as_pyvista_data_set(self):
        if self._pv_data_set is None:
            self._pv_data_set = self._fc_to_pv_data_set()
        return self._pv_data_set

    def _as_fields_container(self):
        """Returns a FieldsContainer representing the streamlines
        related objects.

        Returns
        -------
        streamlines_fields_container : FieldsContainer
            FieldsContainer containing the streamlines data array,
            and a MeshedRegion as support.

        """
        # once implemented, this method will become public
        if self._streamlines_fc is None:
            self._streamlines_fc = self._pv_data_set_to_fc()
        return self._streamlines_fc


class Streamlines(_PvFieldsContainerBase):
    """Class to define the Streamlines object
    scripting with `ansys-dpf-core`.

    """

    def __init__(self, data):
        super().__init__(data=data)


class StreamlinesSource(_PvFieldsContainerBase):
    """Class to define the StreamlinesSource
    object scripting with `ansys-dpf-core`.

    """

    def __init__(self, data):
        super().__init__(data=data)


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
    streamlines: helpers.streamlines.Streamlines

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> from ansys.dpf.core.helpers.streamlines import compute_streamlines
    >>> # Get model and meshed region
    >>> files = examples.download_fluent_mixing_elbow_steady_state()
    >>> ds = dpf.DataSources()
    >>> ds.set_result_file_path(files["cas"][0], "cas")
    >>> ds.add_file_path(files["dat"][1], "dat")
    >>> model = dpf.Model(ds)
    >>> mesh = model.metadata.meshed_region
    >>> # Get velocity data
    >>> velocity_op = model.results.velocity()
    >>> fc = velocity_op.outputs.fields_container()
    >>> op = dpf.operators.averaging.to_nodal_fc(fields_container=fc)
    >>> field = op.outputs.fields_container()[0]
    >>> # compute streamline
    >>> streamline_obj = compute_streamlines(
    ...        meshed_region=mesh,
    ...        field=field,
    ...        source_center=(0.55, 0.55, 0.),
    ...        n_points=10,
    ...        source_radius=0.08,
    ...        max_time=10.0
    ...        )

    """
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
    kwargs_from_source = _sort_supported_kwargs(bound_method=grid.streamlines_from_source, **kwargs)
    kwargs_from_source.update(kwargs_base)  # merge both dicts in kwargs_from_source

    if return_source:
        streamlines, src = grid.streamlines(
            vectors=f"{stream_name}",
            return_source=True,
            **kwargs_from_source,
        )
        streamlines = Streamlines(data=streamlines)
        src = StreamlinesSource(data=src)
        return streamlines, src
    else:
        streamlines = grid.streamlines(
            vectors=f"{stream_name}",
            **kwargs_from_source,
        )
        streamlines = Streamlines(data=streamlines)
        return streamlines
