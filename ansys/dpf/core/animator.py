"""
Animator
=======
This module contains the DPF animator class.

Contains classes used to animate results based on workflows using PyVista.
"""
import ansys.dpf.core
from ansys.dpf.core.plotter import _sort_supported_kwargs


class _InternalAnimatorFactory:
    """
    Factory for _InternalAnimator based on the backend."""
    @staticmethod
    def get_animator_class():
        return _PyVistaAnimator


class _PyVistaAnimator:
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

    def animate_workflow(self, wf_id, frequencies, unit, save_as, **kwargs):
        wf = ansys.dpf.core.Workflow.get_recorded_workflow(wf_id)

        # Initiate movie or gif file if necessary
        if save_as:
            if save_as.endswith(".gif"):
                self._plotter.open_gif(save_as)
            else:
                kwargs_in = _sort_supported_kwargs(
                    bound_method=self._plotter.open_movie, **kwargs)
                self._plotter.open_movie(save_as, **kwargs_in)

        def render_field(id):
            self._plotter.clear()
            wf.connect("index", [id])
            field = wf.get_output("to_render", ansys.dpf.core.types.field)
            self.add_field(field)
            kwargs_in = _sort_supported_kwargs(
                bound_method=self._plotter.add_text, **kwargs)
            self._plotter.add_text(f"t={times[time_id-1]} {unit}", **kwargs_in)

        try:
            # Write initial frame
            render_field(time_ids[0])
            # If not off_screen, enable the user to choose the camera position
            if not kwargs.pop("off_screen", None):
                print('Orient the view, then press "q" to close window and produce movie')
            # Show is necessary even when off_screen to initiate the renderer
            self.show_figure(auto_close=False, **kwargs)
            self._plotter.write_frame()
            # For each time id
            for t in time_ids[1:]:
                render_field(t)
                self._plotter.write_frame()
        except Exception as e:
            print(e)
        self._plotter.close()


class Animator:
    def __init__(self, **kwargs):
        _InternalAnimatorClass = _InternalAnimatorFactory.get_animator_class()
        self._internal_animator = _InternalAnimatorClass(**kwargs)
        self.fields_container = None

    def animate(self, wf_id, frequencies, unit, save_as, **kwargs):
        self._internal_animator.animate_workflow(wf_id, frequencies, unit,
                                                 save_as=save_as,
                                                 **kwargs)
