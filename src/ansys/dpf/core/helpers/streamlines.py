"""Streamlines computation specific helpers.
"""

import numpy as np
import vtk
import warnings

from ansys.dpf.core.common import locations
from ansys.dpf.core.helpers.utils import _sort_supported_kwargs


class Streamlines:
    """Class to define the Streamline object
    scripting with `ansys-dpf-core`.

    """

    def __init__(self, pv_data_set):
        """Instantiate Streamline
        from pyvista.PolyData object.
        This construction is only
        intended to be used internally.

        Parameters
        ----------
        pv_data_set: pyvista.PolyData
        """
        # in the future, a FieldsContainer would
        # probably work to store the related data
        self._pv_data_set = pv_data_set

class StreamlinesSource:
    """Class to define the StreamlineSource
    object scripting with `ansys-dpf-core`.

    """

    def __init__(self, pv_data_set):
        """Instantiate Streamline
        from pyvista.PolyData object.
        This construction is only
        intended to be used internally.

        Parameters
        ----------
        pv_data_set: pyvista.PolyData
        """
        # in the future, a MeshedRegion would
        # probably work to store the related data
        self._pv_data_set = pv_data_set

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
        streamlines = Streamlines(streamlines)
        src = StreamlinesSource(src)
        return streamlines, src
    else:
        streamlines = grid.streamlines(
            vectors=f"{stream_name}",
            **kwargs_from_source,
        )
        streamlines = Streamlines(streamlines)
        return streamlines

