"""
Animator
=======
This module contains the DPF animator class.

Contains classes used to animate results based on workflows using PyVista.
"""
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

    def animate_workflow(self, wf_id, frequencies, save_as, deform_by, scale_factor, **kwargs):
        # Retrieve the workflow to animate
        wf = core.Workflow.get_recorded_workflow(wf_id)
        # Extract useful information from the given frequencies Field
        unit = frequencies.unit
        frequencies = frequencies.data
        # Initiate movie or gif file if necessary
        if save_as:
            if save_as.endswith(".gif"):
                self._plotter.open_gif(save_as)
            else:
                kwargs_in = _sort_supported_kwargs(
                    bound_method=self._plotter.open_movie, **kwargs)
                self._plotter.open_movie(save_as, **kwargs_in)
        freq_kwargs = kwargs.pop("freq_kwargs", {})
        freq_fmt = freq_kwargs.pop("fmt", "")

        def render_field(index):
            # print("Render step", index)
            self._plotter.clear()
            wf.connect("index", [index])
            field = wf.get_output("to_render", core.types.field)
            deform = deform_by[index] if deform_by else None
            self.add_field(field, deform_by=deform, scale_factor=scale_factor, **kwargs)
            kwargs_in = _sort_supported_kwargs(
                bound_method=self._plotter.add_text, **freq_kwargs)
            str_template = "t={0:{2}} {1}"
            self._plotter.add_text("t={0:{2}} {1}".format(frequencies[index], unit, freq_fmt),
                                   **kwargs_in)

        try:
            # Write initial frame
            render_field(0)
            # If not off_screen, enable the user to choose the camera position
            if not kwargs.pop("off_screen", None):
                print('Orient the view, then press "q" to close window and produce movie')
            # Show is necessary even when off_screen to initiate the renderer
            self.show_figure(auto_close=False)
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
            if
            for i in input.keys():
                workflow.set_input_name(i, input[i])
            for o in output.keys():
                workflow.set_output_name(o, output[o])

    def animate(self, input, save_as, deform_by, scale_factor, **kwargs):
        self._internal_animator.animate_workflow(input,
                                                 save_as=save_as,
                                                 deform_by=deform_by,
                                                 scale_factor=scale_factor,
                                                 **kwargs)
