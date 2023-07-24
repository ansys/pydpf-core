"""Streamlines computation specific helpers.
"""

import numpy as np
import warnings

from ansys.dpf.core.common import locations
from ansys.dpf.core.helpers.utils import _sort_supported_kwargs


def _streamline_to_fields(streamline_data_set):
    return streamline_data_set


def _fields_to_streamline(streamline_fields):
    return streamline_fields


def _source_to_field(source_data_set):
    return source_data_set


def _field_to_source(source_field):
    return source_field


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
        streamlines = _streamline_to_fields(streamlines)
        src = _source_to_field(src)
        return streamlines, src
    else:
        streamlines = grid.streamlines(
            vectors=f"{stream_name}",
            **kwargs_from_source,
        )
        streamlines = _streamline_to_fields(streamlines)
        return streamlines

