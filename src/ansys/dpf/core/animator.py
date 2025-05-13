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
        mode_number=None,
        scale_factor=1.0,
        shell_layer=core.shell_layers.top,
        **kwargs,
    ):
        unit = loop_over.unit
        indices = loop_over.scoping.ids

        if scale_factor is None:
            scale_factor = [False] * len(indices)
        type_scale = type(scale_factor)
        if type_scale in [int, float]:
            scale_factor = [scale_factor] * len(indices)
        elif type_scale == list:
            pass
        # elif type_scale in [core.field.Field, core.fields_container.FieldsContainer]:
        #     scale_factor = ["Non-homogenous"]*len(indices)
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

            if mode_number is None:
                workflow.connect(input_name, [frame])

            else:
                workflow.connect(input_name, loop_over.data[frame])

            field = workflow.get_output(output_name, core.types.field)
            deform = None
            if "deform_by" in workflow.output_names:
                deform = workflow.get_output("deform_by", core.types.field)
            self.add_field(
                field,
                deform_by=deform,
                scale_factor_legend=scale_factor[frame],
                shell_layer=shell_layer,
                **kwargs,
            )
            kwargs_in = _sort_supported_kwargs(bound_method=self._plotter.add_text, **freq_kwargs)
            if mode_number is None:
                str_template = "t={0:{2}} {1}"
                self._plotter.add_text(
                    str_template.format(indices[frame], unit, freq_fmt), **kwargs_in
                )
            else:
                str_template = "frq={0:{2}} {1}"
                self._plotter.add_text(
                    str_template.format(mode_number, unit, freq_fmt), **kwargs_in
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
    """The DPF animator class."""

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
            Workflow used to generate a Field at each frame of the animation.
            By default, the "to_render" Field output will be plotted,
            and the "loop_over" input defines what the animation iterates on.
            Optionally, the workflow can also have a "deform_by" Field output,
            used to deform the mesh support.
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
        Workflow used to generate a Field at each frame of the animation.

        By default, the "to_render" Field output will be plotted,
        and the "loop_over" input defines what the animation iterates on.
        Optionally, the workflow can also have a "deform_by" Field output,
        used to deform the mesh support.

        Returns
        -------
        workflow : Workflow
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow: core.Workflow):
        """
        Set the workflow used to generate a Field at each frame of the animation.

        Parameters
        ----------
        workflow : Workflow
            Workflow used to generate a Field at each frame of the animation.
            By default, the "to_render" Field output will be plotted,
            and the "loop_over" input defines what the animation iterates on.
            Optionally, the workflow can also have a "deform_by" Field output,
            used to deform the mesh support.

        """
        self._workflow = workflow

    def animate(
        self,
        loop_over: core.Field,
        output_name: str = "to_render",
        input_name: str = "loop_over",
        save_as: str = None,
        scale_factor: Union[float, Sequence[float]] = 1.0,
        freq_kwargs: dict = None,
        shell_layer: core.shell_layers = core.shell_layers.top,
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
            Name of the workflow output to use as Field for each frame's contour.
            Defaults to "to_render".
        input_name:
            Name of the workflow inputs to feed loop_over values into.
            Defaults to "loop_over".
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
