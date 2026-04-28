# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

import os
from typing import TYPE_CHECKING, List, Optional, Union

import numpy as np

if TYPE_CHECKING:
    from ansys.dpf.core import FieldsContainer, Operator, TimeFreqSupport
    from ansys.dpf.core.results import Result

import ansys.dpf.core as dpf
from ansys.dpf.core import elements, errors as dpf_errors
from ansys.dpf.core.check_version import server_meet_version
from ansys.dpf.core.collection_base import CollectionBase
from ansys.dpf.core.meshed_region import MeshedRegion
from ansys.dpf.core.plotter import DpfPlotter


class MeshesContainer(CollectionBase[MeshedRegion]):
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

    entries_type = MeshedRegion

    def __init__(self, meshes_container=None, server=None):
        super().__init__(collection=meshes_container, server=server)
        if self._internal_obj is None:
            if self._server.has_client():
                self._internal_obj = self._api.collection_of_mesh_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.collection_of_mesh_new()

    def create_subtype(self, obj_by_copy):
        """Create a meshed region sub type."""
        return MeshedRegion(mesh=obj_by_copy, server=self._server)

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
        ([], <pyvista.plotting.plotter.Plotter ...>)

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
                    kwargs["color"] = [random(), random(), random()]  # nosec B311
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

    def animate(
        self,
        save_as: Union[str, os.PathLike] = None,
        deform_by: Union["FieldsContainer", "Result", "Operator", bool] = None,
        scale_factor: Union[float, List[float]] = 1.0,
        fields_container: Optional["FieldsContainer"] = None,
        time_freq_support: Optional["TimeFreqSupport"] = None,
        label: str = "time",
        **kwargs,
    ):
        """Create an animation based on the meshes contained in the MeshesContainer.

        Iterates over the entries indexed by *label*, rendering each :class:`MeshedRegion
        <ansys.dpf.core.MeshedRegion>` as a separate frame. Optionally colors each mesh
        using a matching :class:`FieldsContainer <ansys.dpf.core.FieldsContainer>` and/or
        deforms it.

        Parameters
        ----------
        save_as : str, os.PathLike, optional
            Path of the file to save the animation to. Defaults to ``None``. Supports any
            format accepted by :func:`pyvista.Plotter.write_frame` (.gif, .mp4, …).
        deform_by : FieldsContainer, Result, Operator, bool, optional
            Used to deform the mesh at each frame. Must evaluate to a
            :class:`FieldsContainer <ansys.dpf.core.FieldsContainer>` of 3D nodal vector
            fields with a matching label structure. Set to ``False`` to disable deformation.
            Defaults to ``None`` (no deformation).
        scale_factor : float, list[float], optional
            Scale factor applied to the deformation. Defaults to ``1.0``. Pass a list to
            vary the factor per frame.
        fields_container : FieldsContainer, optional
            If provided, each mesh frame is colored by the corresponding field. The
            :class:`FieldsContainer <ansys.dpf.core.FieldsContainer>` must share the same
            label and IDs as this :class:`MeshesContainer
            <ansys.dpf.core.MeshesContainer>`.
        time_freq_support : TimeFreqSupport, optional
            When the animated label is ``"time"``, provide this to display actual
            time/frequency values in the per-frame overlay text instead of label IDs.
            Defaults to ``None``.
        label : str, optional
            Name of the label to animate over. Defaults to ``"time"``.
            Must be a label present in the container.
        **kwargs
            Additional keyword arguments forwarded to the animator and plotter
            (e.g. ``off_screen``, ``cpos``, ``framerate``, ``quality``).

        Examples
        --------
        Animate a mesh split by material:

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.find_multishells_rst())
        >>> mesh = model.metadata.meshed_region
        >>> split_mesh_op = dpf.operators.mesh.split_mesh(mesh=mesh, property="mat")
        >>> meshes_cont = split_mesh_op.eval()
        >>> meshes_cont.animate(off_screen=True)  # doctest: +SKIP

        """
        from ansys.dpf.core.animator import Animator

        # ── validate the label ────────────────────────────────────────────────
        available_labels = self.labels
        if label not in available_labels:
            raise ValueError(
                f"Label '{label}' not found in this MeshesContainer. "
                f"Available labels: {available_labels}"
            )

        label_scoping = self.get_label_scoping(label=label)

        # ── build the server-side workflow ────────────────────────────────────
        # Multiple operator inputs can share the same workflow input name, so a
        # single workflow.connect("label_space", dict) fans out to every extract
        # operator registered under that name.
        wf = dpf.Workflow()

        # Mesh path: extract_sub_mc → merge_meshes → MeshedRegion
        extract_mc_op = dpf.operators.utility.extract_sub_mc(meshes=self)
        wf.set_input_name("label_space", extract_mc_op.inputs.label_space)
        merge_op = dpf.operators.utility.merge_meshes(
            meshes1=extract_mc_op.outputs.meshes_container
        )
        wf.set_output_name("mesh_to_render", merge_op.outputs.merges_mesh)
        wf.add_operators([extract_mc_op, merge_op])

        # Optional coloring path: extract_sub_fc → extract_field → Field
        # Expose the coloring field under the "field_to_render" convention used by animate_workflow.
        if fields_container is not None:
            extract_fc_op = dpf.operators.utility.extract_sub_fc(
                fields_container=fields_container, collapse_labels=True
            )
            # Shared name: same connect call fans out to this pin too.
            wf.set_input_name("label_space", extract_fc_op.inputs.label_space)
            # collapse_labels removes the animated label from the output FC's label
            # set. merge_fields merges all remaining fields into a single Field.
            merge_color_op = dpf.operators.utility.merge_fields(
                fields1=extract_fc_op.outputs.fields_container
            )
            wf.set_output_name("field_to_render", merge_color_op.outputs.merged_field)
            wf.add_operators([extract_fc_op, merge_color_op])

        # Optional deformation path: extract_sub_fc → extract_field → Field
        # Convention for animate_workflow deformation: output "deform_by"
        if deform_by is not False and deform_by is not None:
            if not isinstance(deform_by, dpf.FieldsContainer):
                deform_by = deform_by.eval()
            extract_deform_fc_op = dpf.operators.utility.extract_sub_fc(
                fields_container=deform_by, collapse_labels=True
            )
            # Shared name: same connect call fans out to this pin too.
            wf.set_input_name("label_space", extract_deform_fc_op.inputs.label_space)
            merge_deform_op = dpf.operators.utility.merge_fields(
                fields1=extract_deform_fc_op.outputs.fields_container
            )
            wf.set_output_name("deform_by", merge_deform_op.outputs.merged_field)
            wf.add_operators([extract_deform_fc_op, merge_deform_op])

        wf.progress_bar = False

        # ── build the loop_over Field (values shown in the overlay text) ──────
        if label == "time" and time_freq_support is not None:
            freq_field = time_freq_support.time_frequencies
            values = freq_field.data[label_scoping.ids - 1]
            unit = freq_field.unit
            freq_fmt = ".3e"
        else:
            values = np.array(label_scoping.ids, dtype=float)
            unit = ""
            freq_fmt = "g"

        loop_over_field = dpf.fields_factory.field_from_array(values)
        loop_over_field.scoping.ids = label_scoping.ids
        loop_over_field.unit = unit

        # ── run the animation via the generic Animator.animate ────────────────
        anim = Animator(workflow=wf, **kwargs)
        kwargs.setdefault("freq_kwargs", {"font_size": 12, "fmt": freq_fmt})
        return anim.animate(
            loop_over=loop_over_field,
            output_name="mesh_to_render",
            input_name="label_space",
            save_as=save_as,
            scale_factor=scale_factor,
            label=label,
            **kwargs,
        )

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

    def solid_meshes(self, label_space=None):
        """Retrieve a list of all meshes with solid element shapes.

        Filters the mesh collection to return meshes containing solid elements
        based on the provided label space criteria.

        Parameters
        ----------
        label_space : dict[str, int], optional
            Dictionary containing label-value pairs for filtering meshes.
            Additional labels like timeid, complexid can be specified.
            If None, only the elshape filter will be applied.

        Returns
        -------
        list[:class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`]
            List of meshes corresponding to the request with solid elements.

        Raises
        ------
        ValueError
            If no labels exist in the container, if no elshape label exists,
            or if a specified label is not found in the container.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> from ansys.dpf.core.common import types as dpf_types
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> mesh_container = model.metadata.meshes_container
        >>> assert(len(mesh_container) == 1)
        >>> split_mesh_op = dpf.Operator("split_mesh")
        >>> split_mesh_op.connect(7, mesh_container[0])
        >>> split_mesh_op.connect(13, "elshape")
        >>> splitted_meshes = split_mesh_op.get_output(0, dpf_types.meshes_container)
        >>> solid_meshes = splitted_meshes.solid_meshes({"body": 1})
        """
        if label_space is None:
            label_space = {}
        else:
            label_space = label_space.copy()

        existing_labels = self.labels
        if existing_labels is None:
            raise ValueError("No labels in this mesh container")
        if "elshape" not in existing_labels:
            raise ValueError("No elshape label in this mesh container")

        invalid_labels = [label for label in label_space if label not in existing_labels]
        if invalid_labels:
            raise ValueError(
                f"The following labels are not in this mesh container: {invalid_labels}"
            )

        if server_meet_version("12.0", self._server):
            label_space["elshape"] = elements._element_shapes.SOLID.value
        else:
            label_space["elshape"] = elements._element_shapes_legacy.SOLID.value

        return self.get_meshes(label_space)

    def shell_meshes(self, label_space=None):
        """Retrieve a list of all meshes with shell element shapes.

        Filters the mesh collection to return meshes containing shell elements
        based on the provided label space criteria.

        Parameters
        ----------
        label_space : dict[str, int], optional
            Dictionary containing label-value pairs for filtering meshes.
            Additional labels like timeid, complexid can be specified.
            If None, only the elshape filter will be applied.

        Returns
        -------
        list[:class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`]
            List of meshes corresponding to the request with shell elements.

        Raises
        ------
        ValueError
            If no labels exist in the container, if no elshape label exists,
            or if a specified label is not found in the container.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> from ansys.dpf.core.common import types as dpf_types
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> mesh_container = model.metadata.meshes_container
        >>> assert(len(mesh_container) == 1)
        >>> split_mesh_op = dpf.Operator("split_mesh")
        >>> split_mesh_op.connect(7, mesh_container[0])
        >>> split_mesh_op.connect(13, "elshape")
        >>> splitted_meshes = split_mesh_op.get_output(0, dpf_types.meshes_container)
        >>> shell_meshes = splitted_meshes.shell_meshes({"body": 1})
        """
        if label_space is None:
            label_space = {}
        else:
            label_space = label_space.copy()

        existing_labels = self.labels
        if existing_labels is None:
            raise ValueError("No labels in this mesh container")
        if "elshape" not in existing_labels:
            raise ValueError("No elshape label in this mesh container")

        invalid_labels = [label for label in label_space if label not in existing_labels]
        if invalid_labels:
            raise ValueError(
                f"The following labels are not in this mesh container: {invalid_labels}"
            )

        if server_meet_version("12.0", self._server):
            label_space["elshape"] = elements._element_shapes.SHELL.value
        else:
            label_space["elshape"] = elements._element_shapes_legacy.SHELL.value

        return self.get_meshes(label_space)

    def beam_meshes(self, label_space=None):
        """Retrieve a list of all meshes with beam element shapes.

        Filters the mesh collection to return meshes containing beam elements
        based on the provided label space criteria.

        Parameters
        ----------
        label_space : dict[str, int], optional
            Dictionary containing label-value pairs for filtering meshes.
            Additional labels like timeid, complexid can be specified.
            If None, only the elshape filter will be applied.

        Returns
        -------
        list[:class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`]
            List of meshes corresponding to the request with beam elements.

        Raises
        ------
        ValueError
            If no labels exist in the container, if no elshape label exists,
            or if a specified label is not found in the container.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> from ansys.dpf.core.common import types as dpf_types
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> mesh_container = model.metadata.meshes_container
        >>> assert(len(mesh_container) == 1)
        >>> split_mesh_op = dpf.Operator("split_mesh")
        >>> split_mesh_op.connect(7, mesh_container[0])
        >>> split_mesh_op.connect(13, "elshape")
        >>> splitted_meshes = split_mesh_op.get_output(0, dpf_types.meshes_container)
        >>> beam_meshes = splitted_meshes.beam_meshes({"body": 1})
        """
        if label_space is None:
            label_space = {}
        else:
            label_space = label_space.copy()

        existing_labels = self.labels
        if existing_labels is None:
            raise ValueError("No labels in this mesh container")
        if "elshape" not in existing_labels:
            raise ValueError("No elshape label in this mesh container")

        invalid_labels = [label for label in label_space if label not in existing_labels]
        if invalid_labels:
            raise ValueError(
                f"The following labels are not in this mesh container: {invalid_labels}"
            )

        if server_meet_version("12.0", self._server):
            label_space["elshape"] = elements._element_shapes.BEAM.value
        else:
            label_space["elshape"] = elements._element_shapes_legacy.BEAM.value

        return self.get_meshes(label_space)

    def solid_mesh(self, label_space=None):
        """Retrieve a mesh with solid element shapes.

        Filters the mesh collection to return a mesh containing solid elements
        based on the provided label space criteria. Raises an exception if
        multiple meshes match the criteria.

        Parameters
        ----------
        label_space : dict[str, int], optional
            Dictionary containing label-value pairs for filtering meshes.
            Additional labels like timeid, complexid can be specified.
            If None, only the elshape filter will be applied.

        Returns
        -------
        :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
            Mesh corresponding to the request with solid elements.

        Raises
        ------
        ValueError
            If no labels exist in the container, if no elshape label exists,
            or if a specified label is not found in the container.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> from ansys.dpf.core.common import types as dpf_types
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> mesh_container = model.metadata.meshes_container
        >>> assert(len(mesh_container) == 1)
        >>> split_mesh_op = dpf.Operator("split_mesh")
        >>> split_mesh_op.connect(7, mesh_container[0])
        >>> split_mesh_op.connect(13, "elshape")
        >>> splitted_meshes = split_mesh_op.get_output(0, dpf_types.meshes_container)
        >>> solid_mesh = splitted_meshes.solid_mesh({"body": 1})
        """
        if label_space is None:
            label_space = {}
        else:
            label_space = label_space.copy()

        existing_labels = self.labels
        if existing_labels is None:
            raise ValueError("No labels in this mesh container")
        if "elshape" not in existing_labels:
            raise ValueError("No elshape label in this mesh container")

        invalid_labels = [label for label in label_space if label not in existing_labels]
        if invalid_labels:
            raise ValueError(
                f"The following labels are not in this mesh container: {invalid_labels}"
            )

        if server_meet_version("12.0", self._server):
            label_space["elshape"] = elements._element_shapes.SOLID.value
        else:
            label_space["elshape"] = elements._element_shapes_legacy.SOLID.value

        return self.get_mesh(label_space)

    def shell_mesh(self, label_space=None):
        """Retrieve a mesh with shell element shapes.

        Filters the mesh collection to return a mesh containing shell elements
        based on the provided label space criteria. Raises an exception if
        multiple meshes match the criteria.

        Parameters
        ----------
        label_space : dict[str, int], optional
            Dictionary containing label-value pairs for filtering meshes.
            Additional labels like timeid, complexid can be specified.
            If None, only the elshape filter will be applied.

        Returns
        -------
        :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
            Mesh corresponding to the request with shell elements.

        Raises
        ------
        ValueError
            If no labels exist in the container, if no elshape label exists,
            or if a specified label is not found in the container.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> from ansys.dpf.core.common import types as dpf_types
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> mesh_container = model.metadata.meshes_container
        >>> assert(len(mesh_container) == 1)
        >>> split_mesh_op = dpf.Operator("split_mesh")
        >>> split_mesh_op.connect(7, mesh_container[0])
        >>> split_mesh_op.connect(13, "elshape")
        >>> splitted_meshes = split_mesh_op.get_output(0, dpf_types.meshes_container)
        >>> shell_mesh = splitted_meshes.shell_mesh({"body": 1})
        """
        if label_space is None:
            label_space = {}
        else:
            label_space = label_space.copy()

        existing_labels = self.labels
        if existing_labels is None:
            raise ValueError("No labels in this mesh container")
        if "elshape" not in existing_labels:
            raise ValueError("No elshape label in this mesh container")

        invalid_labels = [label for label in label_space if label not in existing_labels]
        if invalid_labels:
            raise ValueError(
                f"The following labels are not in this mesh container: {invalid_labels}"
            )

        if server_meet_version("12.0", self._server):
            label_space["elshape"] = elements._element_shapes.SHELL.value
        else:
            label_space["elshape"] = elements._element_shapes_legacy.SHELL.value

        return self.get_mesh(label_space)

    def beam_mesh(self, label_space=None):
        """Retrieve a mesh with beam element shapes.

        Filters the mesh collection to return a mesh containing beam elements
        based on the provided label space criteria. Raises an exception if
        multiple meshes match the criteria.

        Parameters
        ----------
        label_space : dict[str, int], optional
            Dictionary containing label-value pairs for filtering meshes.
            Additional labels like timeid, complexid can be specified.
            If None, only the elshape filter will be applied.

        Returns
        -------
        :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
            Mesh corresponding to the request with beam elements.

        Raises
        ------
        ValueError
            If no labels exist in the container, if no elshape label exists,
            or if a specified label is not found in the container.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> from ansys.dpf.core.common import types as dpf_types
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> mesh_container = model.metadata.meshes_container
        >>> assert(len(mesh_container) == 1)
        >>> split_mesh_op = dpf.Operator("split_mesh")
        >>> split_mesh_op.connect(7, mesh_container[0])
        >>> split_mesh_op.connect(13, "elshape")
        >>> splitted_meshes = split_mesh_op.get_output(0, dpf_types.meshes_container)
        >>> beam_mesh = splitted_meshes.beam_mesh({"body": 1})
        """
        if label_space is None:
            label_space = {}
        else:
            label_space = label_space.copy()

        existing_labels = self.labels
        if existing_labels is None:
            raise ValueError("No labels in this mesh container")
        if "elshape" not in existing_labels:
            raise ValueError("No elshape label in this mesh container")

        invalid_labels = [label for label in label_space if label not in existing_labels]
        if invalid_labels:
            raise ValueError(
                f"The following labels are not in this mesh container: {invalid_labels}"
            )

        if server_meet_version("12.0", self._server):
            label_space["elshape"] = elements._element_shapes.BEAM.value
        else:
            label_space["elshape"] = elements._element_shapes_legacy.BEAM.value

        return self.get_mesh(label_space)
