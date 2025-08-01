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

# -*- coding: utf-8 -*-
"""
MeshesContainer.

Contains classes associated with the DPF MeshesContainer.
"""

from __future__ import annotations

from ansys.dpf.core import errors as dpf_errors, meshed_region
from ansys.dpf.core.collection_base import CollectionBase
from ansys.dpf.core.plotter import DpfPlotter


class MeshesContainer(CollectionBase[meshed_region.MeshedRegion]):
    """Represents a meshes container, which contains meshes split on a given space.

    Parameters
    ----------
    meshes_container : ansys.grpc.dpf.collection_message_pb2.Collection or
                       ansys.dpf.core.MeshesContainer, optional
        Create a meshes container from a collection message or create a copy from an
        existing meshes container. The default is ``None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.
    """

    entries_type = meshed_region.MeshedRegion

    def __init__(self, meshes_container=None, server=None):
        super().__init__(collection=meshes_container, server=server)
        if self._internal_obj is None:
            if self._server.has_client():
                self._internal_obj = self._api.collection_of_mesh_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.collection_of_mesh_new()

    def create_subtype(self, obj_by_copy):
        """Create a meshed region sub type."""
        return meshed_region.MeshedRegion(mesh=obj_by_copy, server=self._server)

    def plot(self, fields_container=None, deform_by=None, scale_factor=1.0, **kwargs):
        """Plot the meshes container with a specific result if fields_container is specified.

        Parameters
        ----------
        fields_container : FieldsContainer, optional
            Data to plot. The default is ``None``.
        deform_by : Field, Result, Operator, optional
            Used to deform the plotted mesh. Must output a 3D vector field.
            Defaults to None.
        scale_factor : float, optional
            Scaling factor to apply when warping the mesh. Defaults to 1.0.
        **kwargs : optional
            Additional keyword arguments for the plotter. For additional keyword
            arguments, see ``help(pyvista.plot)``.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.find_multishells_rst())
        >>> mesh = model.metadata.meshed_region
        >>> split_mesh_op = dpf.operators.mesh.split_mesh(mesh=mesh, property="mat")
        >>> meshes_cont = split_mesh_op.eval()
        >>> disp_op = dpf.operators.result.displacement(
        ...     data_sources = dpf.DataSources(examples.find_multishells_rst()),
        ...     mesh = meshes_cont
        ... )
        >>> disp_fc = disp_op.outputs.fields_container()
        >>> meshes_cont.plot(disp_fc)
        (None, <pyvista.plotting.plotter.Plotter ...>)

        """
        # DPF defaults
        kwargs.setdefault("show_edges", True)
        # Initiate plotter
        pl = DpfPlotter(**kwargs)
        # If a fields' container is given
        if fields_container is not None:
            for i in range(len(fields_container)):
                label_space = fields_container.get_label_space(i)
                mesh_to_send = self.get_mesh(label_space)
                if mesh_to_send is None:
                    raise dpf_errors.DpfValueError(
                        "Meshes container and result fields "
                        "container do not have the same scope. "
                        "Plotting can not proceed. "
                    )
                field = fields_container[i]
                if deform_by:
                    from ansys.dpf.core.operators import scoping

                    mesh_scoping = scoping.from_mesh(mesh=mesh_to_send)
                    deform_by = deform_by.on_mesh_scoping(mesh_scoping)
                pl.add_field(
                    field,
                    mesh_to_send,
                    deform_by=deform_by,
                    show_axes=kwargs.pop("show_axes", True),
                    scale_factor=scale_factor,
                    **kwargs,
                )
        else:
            # If no field given, associate a random color to each mesh in the container
            from random import random

            random_color = "color" not in kwargs
            for mesh in self:
                if mesh.nodes.n_nodes == 0:
                    continue
                if random_color:
                    kwargs["color"] = [random(), random(), random()]
                pl.add_mesh(
                    mesh,
                    deform_by=deform_by,
                    scale_factor=scale_factor,
                    show_axes=kwargs.pop("show_axes", True),
                    **kwargs,
                )
        # Plot the figure
        kwargs.pop("notebook", None)
        return pl.show_figure(**kwargs)

    def get_meshes(self, label_space):
        """Retrieve the meshes at a label space.

        Parameters
        ----------
        label_space : dict[str,int]
            Meshes corresponding to a filter (label space) in the input. For example:
            ``{"elshape":1, "body":12}``

        Returns
        -------
        meshes : list[MeshedRegion]
            Meshes corresponding to the request.
        """
        return super()._get_entries(label_space)

    def get_mesh(self, label_space_or_index: int | dict[str, int]):
        """Retrieve the mesh at a requested index or label space.

        Raises an exception if the request returns more than one mesh.

        Parameters
        ----------
        label_space_or_index:
            Scoping of the requested mesh, such as ``{"time": 1, "complex": 0}``
            or the index of the mesh.

        Returns
        -------
        mesh : MeshedRegion
            Mesh corresponding to the request.
        """
        return super()._get_entry(label_space_or_index)

    def __getitem__(self, key):
        """Retrieve the mesh at a requested index.

        Parameters
        ----------
        key : int
            Index

        Returns
        -------
        mesh : MeshedRegion
            Mesh corresponding to the request.
        """
        return super().__getitem__(key)

    def add_mesh(self, label_space, mesh):
        """Add or update the mesh at a requested label space.

        Parameters
        ----------
        label_space : dict[str,int]
            Label space of the requested meshes. For example, {"elshape":1, "body":12}.

        mesh : MeshedRegion
            DPF mesh to add or update.
        """
        return super()._add_entry(label_space, mesh)
