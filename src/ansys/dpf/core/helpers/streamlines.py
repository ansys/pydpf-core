# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Streamlines computation specific helpers."""

import warnings

import numpy as np

from ansys.dpf.core.common import locations
from ansys.dpf.core.fields_container import FieldsContainer
from ansys.dpf.core.helpers.utils import _sort_supported_kwargs


class _PvFieldsContainerBase:
    def __init__(self, data):
        """Instantiate Streamline from pyvista.PolyData object.

        This construction is only intended to be used internally.

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
        elif isinstance(FieldsContainer):
            self._streamlines_fc = data
        else:
            raise AttributeError(
                "streamlines must be a pyvista.PolyData or a dpf.FieldsContainer instance."
            )

    def _pv_data_set_to_fc(self):
        """Convert pyvista.PolyData into FieldsContainer."""
        raise Exception("Not implemented yet")

    def _fc_to_pv_data_set(self):
        """Convert FieldsContainer into pyvista.PolyData."""
        raise Exception("Not implemented yet")

    def _as_pyvista_data_set(self):
        if self._pv_data_set is None:
            self._pv_data_set = self._fc_to_pv_data_set()
        return self._pv_data_set

    def _as_fields_container(self):
        """Return a FieldsContainer representing the streamlines related objects.

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
    """Class to define the Streamlines object scripting with `ansys-dpf-core`."""

    def __init__(self, data):
        super().__init__(data=data)


class StreamlinesSource(_PvFieldsContainerBase):
    """Class to define the StreamlinesSource object scripting with `ansys-dpf-core`."""

    def __init__(self, data):
        super().__init__(data=data)


def compute_streamlines(meshed_region, field, **kwargs):
    """Compute the streamlines for a given mesh and velocity field.

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
    if field.location != locations.nodal:
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
