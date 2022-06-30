"""
Animator
=======
This module contains the DPF animator class.

Contains classes used to animate results based on workflows using PyVista.
"""


class _InternalAnimatorFactory:
    """
    Factory for _InternalAnimator based on the backend."""
    @staticmethod
    def get_animator_class():
        return _PyVistaAnimator


class _PyVistaAnimator:
    """This _InternalAnimator class is based on PyVista"""
    def __init__(self, kwargs):
        # Import pyvista
        from vtk_helper import PyVistaImportError
        try:
            import pyvista as pv
        except ModuleNotFoundError:
            raise PyVistaImportError


class Animator:
    def __init__(self, **kwargs):
        _InternalAnimatorClass = _InternalAnimatorFactory.get_animator_class()
        self._internal_animator = _InternalAnimatorClass(**kwargs)

    def add_fields_container(self, self1):
        pass

    def animate(self, save_as, warping_field, scale_factor, param):
        pass

    def _render_field(self, time_id):
        self._plotter.clear()
        warp_by = None
        if warping_field:
            warp_by = warping_field.on_time_scoping([time_id])
        self.add_field(fc.get_field_by_time_id(time_id),
                       warping_field=warp_by,
                       scaling_factor=scale_factor)
        kwargs_in = _sort_supported_kwargs(
            bound_method=self._plotter.add_text, **kwargs)
        self._plotter.add_text(f"t={times[time_id-1]} {unit}", **kwargs_in)
