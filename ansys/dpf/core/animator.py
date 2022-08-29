"""
Animator
=======
This module contains the DPF animator class.

Contains classes used to animate results based on workflows using PyVista.
"""
import numpy as np

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
        # Import pyvista
        from ansys.dpf.core.vtk_helper import PyVistaImportError
        try:
            import pyvista as pv
        except ModuleNotFoundError:
            raise PyVistaImportError
        # Filter kwargs
        kwargs_in = _sort_supported_kwargs(
            bound_method=pv.Plotter,
            **kwargs)
        # Initiate pyvista Plotter
        self._plotter = pv.Plotter(**kwargs_in)

    def animate_workflow(self, frequencies, workflow, save_as, scale_factor, **kwargs):
        # Extract useful information from the given frequencies Field
        time_unit = frequencies["frequencies"].unit
        frequencies = frequencies["frequencies"].data
        type_scale = type(scale_factor)
        if scale_factor is None:
            scale_factor = [False]*len(frequencies)
        elif type_scale in [int, float]:
            scale_factor = [scale_factor]*len(frequencies)
        elif type_scale == list:
            pass
        elif type_scale in [core.field.Field, core.fields_container.FieldsContainer]:
            scale_factor = ["Non-homogenous"]*len(frequencies)
        else:
            raise ValueError("Argument scale_factor must be an int, a float, a list of either, "
                             f"a Field or a FieldsContainer (not {type_scale})")
        # Initiate movie or gif file if necessary
        if save_as:
            if save_as.endswith(".gif"):
                self._plotter.open_gif(save_as)
            else:
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
            if type(cpos[0][0]) is float:
                cpos = [cpos]*len(frequencies)

        self._plotter.camera_position = "yz"
        def render_field(index):
            # print("Render step", index)
            self._plotter.clear()
            workflow.connect("index", [index])
            field = workflow.get_output("to_render", core.types.field)
            deform = workflow.get_output("deform_by", core.types.field)
            self.add_field(field, deform_by=deform,
                           scale_factor_legend=scale_factor[index],
                           **kwargs)
            kwargs_in = _sort_supported_kwargs(
                bound_method=self._plotter.add_text, **freq_kwargs)
            str_template = "t={0:{2}} {1}"
            self._plotter.add_text("t={0:{2}} {1}".format(frequencies[index], time_unit, freq_fmt),
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
                self._plotter.write_frame()
            # For each time id
            for t in range(1, len(frequencies)):
                render_field(t)
                if save_as:
                    self._plotter.write_frame()
        except Exception as e:
            print(e)
            raise
        self._plotter.close()
        return result


class Animator:
    def __init__(self, **kwargs):
        _InternalAnimatorClass = _InternalAnimatorFactory.get_animator_class()
        self._internal_animator = _InternalAnimatorClass(**kwargs)
        self.workflow = None

    def add_workflow(self, input=None, output=None, workflow=None):
        if not workflow and not (input and output):
            raise ValueError("Either a workflow or an input and output are required.")
        if workflow:
            self.workflow = workflow
        else:
            if (input is None) or (output is None):
                raise ValueError("input and output must both be given.")
            workflow = core.Workflow()
            # if
            for i in input.keys():
                workflow.set_input_name(i, input[i])
            for o in output.keys():
                workflow.set_output_name(o, output[o])

    def animate(self,  input, save_as, scale_factor, **kwargs):
        if self.workflow is None:
            raise ValueError("Cannot animate without first adding a workflow.")
        return self._internal_animator.animate_workflow(input,
                                                        workflow=self.workflow,
                                                        save_as=save_as,
                                                        scale_factor=scale_factor,
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
        # Turn the Field into a fields_container
        fields = []
        for i in range(n_sets):
            fields.append(scale_factor)
        scale_factor = core.fields_container_factory.over_time_freq_fields_container(fields)
    elif scale_type == core.fields_container.FieldsContainer:
        if scale_factor.time_freq_support.n_sets != n_sets:
            raise ValueError(f"The scale_factor FieldsContainer does not contain the same number of"
                             f" fields as the fields_container being animated "
                             f" ({scale_factor.time_freq_support.n_sets} != {n_sets}).")
    elif scale_type == list:
        if len(scale_factor) != n_sets:
            raise ValueError(f"The scale_factor list is not the same length as the fields_container"
                             f"being animated ({len(scale_factor)} != {n_sets}).")
        # Turn the scalar list into a FieldsContainer
        fields = []
        for i, f in enumerate(fc):
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
    return scale_factor
