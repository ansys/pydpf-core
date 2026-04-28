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

"""
Animator.

This module contains the DPF animator class.

Contains classes used to animate results based on workflows using PyVista.
"""

from typing import Sequence, Union

import numpy as np

import ansys.dpf.core as core
from ansys.dpf.core.helpers.utils import _sort_supported_kwargs
from ansys.dpf.core.plotter import _PyVistaPlotter


class _InternalAnimatorFactory:
    """Factory for _InternalAnimator based on the backend."""

    @staticmethod
    def get_animator_class():
        return _PyVistaAnimator


class _PyVistaAnimator(_PyVistaPlotter):
    """An InternalAnimator class based on PyVista."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def animate_workflow(
        self,
        loop_over,
        workflow,
        output_name,
        input_name="loop_over",
        save_as="",
        scale_factor=1.0,
        shell_layer=core.shell_layers.top,
        label=None,
        **kwargs,
    ):
        """Animate a workflow, rendering one frame per entry in *loop_over*.

        Each frame the workflow output *output_name* is retrieved as a
        :class:`~ansys.dpf.core.MeshedRegion` and passed to :meth:`add_mesh`.
        When the workflow also exposes a ``"field_to_render"``
        :class:`~ansys.dpf.core.Field` output the mesh is colored by that
        field via :meth:`add_field` instead.  An optional ``"deform_by"``
        :class:`~ansys.dpf.core.Field` output is honoured in both cases.

        Both :meth:`FieldsContainer.animate <ansys.dpf.core.FieldsContainer.animate>` and
        :meth:`MeshesContainer.animate <ansys.dpf.core.MeshesContainer.animate>`
        build workflows that expose ``"mesh_to_render"`` and optionally
        ``"field_to_render"`` so they both use this single rendering path.

        When *label* is set the per-frame workflow input receives a
        ``{label: label_id}`` dict, which is what
        :class:`~ansys.dpf.core.operators.utility.extract_sub_fc` and
        :class:`~ansys.dpf.core.operators.utility.extract_sub_mc` expect.
        When *label* is ``None`` the input receives a 0-based frame-index list,
        which is the fallback for direct :class:`Animator` callers.
        """
        unit = loop_over.unit
        indices = loop_over.scoping.ids

        if scale_factor is None:
            scale_factor = [False] * len(indices)
        type_scale = type(scale_factor)
        if type_scale in [int, float]:
            scale_factor = [float(scale_factor)] * len(indices)
        elif type_scale == list:
            if len(scale_factor) != len(indices):
                raise ValueError(
                    f"The scale_factor list length ({len(scale_factor)}) must match the "
                    f"number of animation frames ({len(indices)})."
                )
        else:
            raise ValueError(
                "Argument scale_factor must be an int, a float, or a list of either, "
                f"(not {type_scale})"
            )
        # Initiate movie or gif file if necessary
        if save_as:
            if save_as.endswith(".gif"):
                self._plotter.open_gif(save_as)
            else:  # pragma: no cover
                kwargs_in = _sort_supported_kwargs(bound_method=self._plotter.open_movie, **kwargs)
                try:
                    self._plotter.open_movie(save_as, **kwargs_in)
                except ImportError as e:
                    if "imageio ffmpeg plugin you need" in e.msg:
                        raise ImportError(
                            "The imageio-ffmpeg library is required to save "
                            "animations. Please install it first with the command "
                            "'pip install imageio-ffmpeg'"
                        )
                    else:
                        raise e
        freq_kwargs = kwargs.pop("freq_kwargs", {})
        freq_fmt = freq_kwargs.pop("fmt", "")

        cpos = kwargs.pop("cpos", None)
        if cpos:
            if isinstance(cpos[0][0], float):
                cpos = [cpos] * len(indices)

        def render_frame(frame):
            self._plotter.clear()

            # ── connect the per-frame input ───────────────────────────────────
            if label is not None:
                # Label-space mode: a single connect fans to all registered
                # label_space inputs (each extract_sub_* op shares the name).
                workflow.connect(input_name, {label: int(indices[frame])})
            else:
                # Fallback for direct Animator.animate() callers that supply a
                # plain workflow driven by a 0-based frame-index list.
                workflow.connect(input_name, [frame])

            # ── retrieve deformation field if the workflow produces one ───────
            deform = None
            if "deform_by" in workflow.output_names:
                deform = workflow.get_output("deform_by", core.types.field)

            # ── render: mesh geometry + optional field coloring ──────────────
            mesh = workflow.get_output(output_name, core.types.meshed_region)
            if "field_to_render" in workflow.output_names:
                # Colorize the mesh by the companion scalar/vector field.
                color_field = workflow.get_output("field_to_render", core.types.field)
                self.add_field(
                    color_field,
                    meshed_region=mesh,
                    deform_by=deform,
                    scale_factor=scale_factor[frame],
                    scale_factor_legend=scale_factor[frame],
                    shell_layer=shell_layer,
                    **kwargs,
                )
            else:
                self.add_mesh(
                    mesh,
                    deform_by=deform,
                    scale_factor=scale_factor[frame],
                    **kwargs,
                )

            # ── per-frame overlay text ────────────────────────────────────────
            kwargs_in = _sort_supported_kwargs(bound_method=self._plotter.add_text, **freq_kwargs)
            prefix = ("t" if label == "time" else label) if label is not None else "t"
            str_template = f"{prefix}={{0:{{2}}}} {{1}}"
            self._plotter.add_text(
                str_template.format(loop_over.data_as_list[frame], unit, freq_fmt), **kwargs_in
            )

            if cpos:
                self._plotter.camera_position = cpos[frame]

        try:

            def animation():
                if save_as:
                    try:
                        self._plotter.write_frame()
                    except AttributeError as e:  # pragma: no cover
                        if (
                            "To retrieve an image after the render window has been closed"
                            in e.args[0]
                        ):
                            print("Animation canceled.")
                            print(e)
                            return result
                # For each additional frame requested
                if len(indices) > 1:
                    for frame in range(1, len(indices)):
                        try:
                            render_frame(frame)
                        except AttributeError as e:  # pragma: no cover
                            if "'NoneType' object has no attribute 'interactor'" in e.args[0]:
                                print("Animation canceled.")
                                return result
                        if save_as:
                            self._plotter.write_frame()

            # Write initial frame
            render_frame(0)
            # If not off_screen, enable the user to choose the camera position
            off_screen = kwargs.pop("off_screen", None)
            if off_screen is None:
                import pyvista as pv

                off_screen = pv.OFF_SCREEN

            if not off_screen:
                self._plotter.add_key_event("a", animation)
                print('Orient the view, then press "a" to produce an animation')
            else:
                animation()
            # Show is necessary even when off_screen to initiate the renderer
            result = self._plotter.show(interactive=True)
            # result = self.show_figure(auto_close=False, **kwargs)
            # result = self._plotter.show()
        except Exception as e:  # pragma: no cover
            print(e)
            raise
        self._plotter.close()
        return result


class Animator:
    """The DPF Animator class.

    Drives an animation by repeatedly connecting per-frame values to a
    :class:`~ansys.dpf.core.Workflow` and rendering the result with PyVista.

    Each frame the workflow's ``"mesh_to_render"`` output is retrieved as a
    :class:`~ansys.dpf.core.MeshedRegion` and rendered with :meth:`add_mesh`.
    When the workflow also exposes a ``"field_to_render"``
    :class:`~ansys.dpf.core.Field` output the mesh is colored by that field.
    An optional ``"deform_by"`` :class:`~ansys.dpf.core.Field` output deforms
    the mesh.  The ``"loop_over"`` (or ``"label_space"``) workflow input drives
    the per-frame iteration.
    """

    def __init__(self, workflow=None, **kwargs):
        """
        Create an Animator object.

        The current Animator is a PyVista based object.

        That means that PyVista must be installed, and that
        it supports **kwargs as parameter (the argument
        must be supported by the installed PyVista version).
        More information about the available arguments are
        available at :class:`pyvista.Plotter`.

        Parameters
        ----------
        workflow : Workflow, optional
            Workflow whose ``"mesh_to_render"`` output is rendered each frame.
            An optional ``"field_to_render"`` output colorizes the mesh, and an
            optional ``"deform_by"`` output deforms it.
            The ``"loop_over"`` (or ``"label_space"``) input drives the iteration.
        **kwargs : optional
            Additional keyword arguments for the plotter. More information
            are available at :class:`pyvista.Plotter`.

        Examples
        --------
        >>> from ansys.dpf.core.animator import Animator
        >>> anim = Animator(notebook=False)

        """
        _InternalAnimatorClass = _InternalAnimatorFactory.get_animator_class()
        self._internal_animator = _InternalAnimatorClass(**kwargs)
        self._workflow = workflow

    @property
    def workflow(self) -> core.Workflow:
        """
        Workflow used to generate a MeshedRegion at each frame of the animation.

        The ``"mesh_to_render"`` output is rendered each frame.
        An optional ``"field_to_render"`` output colorizes the mesh, and an
        optional ``"deform_by"`` output deforms it.
        The ``"loop_over"`` (or ``"label_space"``) input drives the iteration.

        Returns
        -------
        workflow : Workflow
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow: core.Workflow):
        """
        Set the workflow used to generate a MeshedRegion at each frame of the animation.

        Parameters
        ----------
        workflow : Workflow
            Workflow whose ``"mesh_to_render"`` output is rendered each frame.
            An optional ``"field_to_render"`` output colorizes the mesh, and an
            optional ``"deform_by"`` output deforms it.
            The ``"loop_over"`` (or ``"label_space"``) input drives the iteration.

        """
        self._workflow = workflow

    def animate(
        self,
        loop_over: core.Field,
        output_name: str = "mesh_to_render",
        input_name: str = "loop_over",
        save_as: str = None,
        scale_factor: Union[float, Sequence[float]] = 1.0,
        freq_kwargs: dict = None,
        shell_layer: core.shell_layers = core.shell_layers.top,
        label: str = None,
        **kwargs,
    ):
        """
        Animate the workflow of the Animator, using inputs.

        Parameters
        ----------
        loop_over:
            Field of values to loop over.
            Can for example be a subset of sets of TimeFreqSupport.time_frequencies.
            The unit of the Field will be displayed if present.
        output_name:
            Name of the workflow output to retrieve for rendering each frame.
            Must resolve to a :class:`~ansys.dpf.core.MeshedRegion`.
            Defaults to ``"mesh_to_render"``.
        input_name:
            Name of the workflow input to feed the per-frame value into.
            Defaults to ``"loop_over"`` (0-based frame index list for mode-shape animations).
            Use ``"label_space"`` together with *label* for label-space-based animations.
        save_as:
            Path of file to save the animation to. Defaults to None. Can be of any format supported
            by pyvista.Plotter.write_frame (.gif, .mp4, ...).
        scale_factor:
            Scale factor to apply when warping the mesh. Defaults to 1.0. Can be a list to make
            scaling frequency-dependent.
        freq_kwargs:
            Dictionary of kwargs given to the :func:`pyvista.Plotter.add_text` method, used to
            format the frequency information. Can also contain a "fmt" key,
            defining the format for the frequency displayed with a string such as ".3e".
        shell_layer:
            Enum used to set the shell layer if the field to plot
            contains shell elements. Defaults to top layer.
        label : str, optional
            Name of the collection label being animated.  When set, the per-frame
            workflow input receives a ``{label: label_id}`` dict instead of a
            0-based index list, which is required by operators such as
            :class:`~ansys.dpf.core.operators.utility.extract_sub_fc` and
            :class:`~ansys.dpf.core.operators.utility.extract_sub_mc`.  Also
            used as the prefix in the per-frame overlay text
            (e.g. ``"mat"`` → ``"mat=3"``, ``"time"`` → ``"t=0.001 s"``).
            Defaults to ``None`` (index-list input).
        **kwargs : optional
            Additional keyword arguments for the animator.
            Used by :func:`pyvista.Plotter` (off_screen, cpos, ...),
            or by :func:`pyvista.Plotter.open_movie`
            (framerate, quality, ...)
        """
        if freq_kwargs is None:
            freq_kwargs = {"font_size": 12, "fmt": ".3e"}
        if self.workflow is None:
            raise ValueError("Cannot animate without self.workflow.")
        return self._internal_animator.animate_workflow(
            loop_over=loop_over,
            workflow=self.workflow,
            output_name=output_name,
            input_name=input_name,
            save_as=save_as,
            scale_factor=scale_factor,
            freq_kwargs=freq_kwargs,
            shell_layer=shell_layer,
            label=label,
            **kwargs,
        )


def scale_factor_to_fc(scale_factor, fc):
    """Scale the fields being animated by a factor.

    Parameters
    ----------
    scale_factor : int, float, list
        Scale factor to apply to the animated field.
    fc : FieldsContainer
        FieldsContainer containing the fields being animated.
    """

    def int_to_field(value, shape, scoping):
        field = core.fields_factory.field_from_array(np.full(shape=shape, fill_value=value))
        field.scoping = scoping
        return field

    scale_type = type(scale_factor)
    n_sets = len(fc)
    if scale_type == core.field.Field:
        raise NotImplementedError("Scaling by a Field is not yet implemented.")
        # # Turn the Field into a fields_container
        # fields = []
        # for i in range(n_sets):
        #     fields.append(scale_factor)
        # scale_factor = core.fields_container_factory.over_time_freq_fields_container(fields)
    elif scale_type == core.fields_container.FieldsContainer:
        raise NotImplementedError("Scaling by a FieldsContainer is not yet implemented.")
        # if scale_factor.time_freq_support.n_sets != n_sets:
        #     raise ValueError(f"The scale_factor FieldsContainer does not contain the same "
        #                      f"number of fields as the fields_container being animated "
        #                      f" ({scale_factor.time_freq_support.n_sets} != {n_sets}).")
    elif scale_type == list:
        if len(scale_factor) != n_sets:
            raise ValueError(
                f"The scale_factor list is not the same length as the fields_container"
                f"being animated ({len(scale_factor)} != {n_sets})."
            )
        # Turn the scalar list into a FieldsContainer
        fields = []
        for i in range(len(fc)):
            fields.append(
                int_to_field(scale_factor[i], fc.get_field(0).shape, fc.get_field(0).scoping)
            )
        scale_factor = core.fields_container_factory.over_time_freq_fields_container(fields)
    elif scale_type == int or scale_type == float:
        # Turn the float into a fields_container
        fields = []
        for i in range(n_sets):
            fields.append(
                int_to_field(scale_factor, fc.get_field(0).shape, fc.get_field(0).scoping)
            )
        scale_factor = core.fields_container_factory.over_time_freq_fields_container(fields)
    else:
        raise ValueError(
            "Argument scale_factor must be an int, a float, or a list of either, "
            f"(not {scale_type})"
        )
    return scale_factor
