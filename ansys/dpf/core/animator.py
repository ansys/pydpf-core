"""
Animator
========
This module contains the DPF animator class.

Contains classes used to animate results based on workflows using PyVista.
"""
import numpy as np
from typing import Union, Sequence

import ansys.dpf.core as core
from ansys.dpf.core.plotter import _sort_supported_kwargs, _PyVistaPlotter


class _InternalAnimatorFactory:
    """
    Factory for _InternalAnimator based on the backend."""
    @staticmethod
    def get_animator_class():
        return _PyVistaAnimator


class _PyVistaAnimator(_PyVistaPlotter):
    """This _InternalAnimator class is based on PyVista"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def animate_workflow(self, frequencies, workflow, output,
                         save_as="", scale_factor=1.0, **kwargs):
        # Extract useful information from the given frequencies Field
        time_unit = frequencies.unit
        inputs = frequencies.data
        if scale_factor is None:
            scale_factor = [False]*len(inputs)
        type_scale = type(scale_factor)
        if type_scale in [int, float]:
            scale_factor = [scale_factor]*len(inputs)
        elif type_scale == list:
            pass
        # elif type_scale in [core.field.Field, core.fields_container.FieldsContainer]:
        #     scale_factor = ["Non-homogenous"]*len(inputs)
        else:
            raise ValueError("Argument scale_factor must be an int, a float, or a list of either, "
                             f"(not {type_scale})")
        # Initiate movie or gif file if necessary
        if save_as:
            if save_as.endswith(".gif"):
                self._plotter.open_gif(save_as)
            else:  # pragma: no cover
                kwargs_in = _sort_supported_kwargs(
                    bound_method=self._plotter.open_movie, **kwargs)
                try:
                    self._plotter.open_movie(save_as, **kwargs_in)
                except ImportError as e:
                    if "imageio ffmpeg plugin you need" in e.msg:
                        raise ImportError("The imageio-ffmpeg library is required to save "
                                          "animations. Please install it first with the command "
                                          "'pip install imageio-ffmpeg'")
                    else:
                        raise e
        freq_kwargs = kwargs.pop("freq_kwargs", {})
        freq_fmt = freq_kwargs.pop("fmt", "")

        cpos = kwargs.pop("cpos", None)
        if cpos:
            if isinstance(cpos[0][0], float):
                cpos = [cpos]*len(inputs)

        def render_field(index):
            # print("Render step", index)
            self._plotter.clear()
            workflow.connect("index", [index])
            field = workflow.get_output(output, core.types.field)
            deform = None
            if "deform_by" in workflow.output_names:
                deform = workflow.get_output("deform_by", core.types.field)
            self.add_field(field, deform_by=deform,
                           scale_factor_legend=scale_factor[index],
                           **kwargs)
            kwargs_in = _sort_supported_kwargs(
                bound_method=self._plotter.add_text, **freq_kwargs)
            str_template = "t={0:{2}} {1}"
            self._plotter.add_text(str_template.format(inputs[index], time_unit, freq_fmt),
                                   **kwargs_in)
            if cpos:
                self._plotter.camera_position = cpos[index]

        try:
            # Write initial frame
            render_field(0)
            # If not off_screen, enable the user to choose the camera position
            if not kwargs.pop("off_screen", None):
                print('Orient the view, then press "q" to close the window '
                      'and produce an animation')
            # Show is necessary even when off_screen to initiate the renderer
            result = self.show_figure(auto_close=False, **kwargs)
            if save_as:
                try:
                    self._plotter.write_frame()
                except AttributeError as e:  # pragma: no cover
                    if "To retrieve an image after the render window has been closed" in e.args[0]:
                        print("Animation canceled.")
                        return result
            # For each time id if more than the first one
            if len(inputs) > 1:
                for t in range(1, len(inputs)):
                    try:
                        render_field(t)
                    except AttributeError as e:  # pragma: no cover
                        if "'NoneType' object has no attribute 'interactor'" in e.args[0]:
                            print("Animation canceled.")
                            return result
                    if save_as:
                        self._plotter.write_frame()
        except Exception as e:  # pragma: no cover
            print(e)
            raise
        self._plotter.close()
        return result


class Animator:
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
            Must have a "to_render" Field output which will be plotted,
            and an "index" int input to define the frame number.
            Optionally, the workflow can also have a "deform_by" Field output,
            which will be used to deform the mesh support.
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
        Must have a "to_render" Field output which will be plotted,
        and an "index" int input to define the frame number.
        Optionally, the workflow can also have a "deform_by" Field output,
        which will be used to deform the mesh support.

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
            Must have a "to_render" Field output which will be plotted,
            and an "index" int input to define the frame number.
            Optionally, the workflow can also have a "deform_by" Field output,
            which will be used to deform the mesh support.

        """
        self._workflow = workflow

    def animate(self, frequencies: core.Field,
                output: str = "to_render",
                save_as: str = None,
                scale_factor: Union[float, Sequence[float]] = 1.0,
                freq_kwargs: dict = {},
                **kwargs):
        """
        Animate the workflow of the Animator, using inputs

        Parameters
        ----------
        frequencies : Field
            Field of frequencies to render. Obtained from TimeFreqSupport.time_frequencies,
            TimeFreqSupport.complex_frequencies or TimeFreqSupport.rpms.
        output : str, optional
            Name of the workflow output to use as Field for each frame's contour.
            Defaults to "to_render".
        save_as : str, optional
            Path of file to save the animation to. Defaults to None. Can be of any format supported
            by pyvista.Plotter.write_frame (.gif, .mp4, ...).
        scale_factor : float, list, optional
            Scale factor to apply when warping the mesh. Defaults to 1.0. Can be a list to make
            scaling frequency-dependent.
        freq_kwargs : dict, optional
            Dictionary of kwargs given to the :func:`pyvista.Plotter.add_text` method, used to
            format the frequency information. Can also contain a "fmt" key,
            defining the format for the frequency displayed with a string such as ".3e".
        **kwargs : optional
            Additional keyword arguments for the animator.
            Used by :func:`pyvista.Plotter` (off_screen, cpos, ...),
            or by :func:`pyvista.Plotter.open_movie`
            (framerate, quality, ...)


        """
        if self.workflow is None:
            raise ValueError("Cannot animate without self.workflow.")
        return self._internal_animator.animate_workflow(frequencies=frequencies,
                                                        workflow=self.workflow,
                                                        output=output,
                                                        save_as=save_as,
                                                        scale_factor=scale_factor,
                                                        freq_kwargs=freq_kwargs,
                                                        **kwargs)


def scale_factor_to_fc(scale_factor, fc):

    def int_to_field(value, shape, scoping):
        field = core.fields_factory.field_from_array(
            np.full(shape=shape, fill_value=value))
        field.scoping = scoping
        return field

    scale_type = type(scale_factor)
    n_sets = fc.time_freq_support.n_sets
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
            raise ValueError(f"The scale_factor list is not the same length as the fields_container"
                             f"being animated ({len(scale_factor)} != {n_sets}).")
        # Turn the scalar list into a FieldsContainer
        fields = []
        for i in range(len(fc)):
            fields.append(int_to_field(scale_factor[i], fc.get_field(0).shape,
                          fc.get_field(0).scoping))
        scale_factor = core.fields_container_factory.over_time_freq_fields_container(fields)
    elif scale_type == int or scale_type == float:
        # Turn the float into a fields_container
        fields = []
        for i in range(n_sets):
            fields.append(int_to_field(scale_factor, fc.get_field(0).shape,
                          fc.get_field(0).scoping))
        scale_factor = core.fields_container_factory.over_time_freq_fields_container(fields)
    else:
        raise ValueError("Argument scale_factor must be an int, a float, or a list of either, "
                         f"(not {scale_type})")
    return scale_factor
