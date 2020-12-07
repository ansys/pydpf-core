"""Miscellaneous functions for DPF module"""
from pkgutil import iter_modules


# ANSYS CPython workbench enviornment may not have scooby installed
try:
    from scooby import Report
except ImportError:
    class Report():
        """Placeholder for scooby.Report"""

        def __init__(self, *args, **kwargs):
            raise ImportError('Install `scooby` with `pip install scooby` to use '
                              'this feature')


def module_exists(module_name):
    """Returns True when a module exists"""
    return module_name in (name for loader, name, ispkg in iter_modules())


class Report(Report):
    """Generate a report of the installed packages for ansys-dpf-core"""

    def __init__(self, additional=None, ncol=3, text_width=80, sort=False,
                 gpu=True):
        """Generate a :class:`scooby.Report` instance.

        Parameters
        ----------
        additional : list(ModuleType), list(str)
            List of packages or package names to add to output information.

        ncol : int, optional
            Number of package-columns in html table; only has effect if
            ``mode='HTML'`` or ``mode='html'``. Defaults to 3.

        text_width : int, optional
            The text width for non-HTML display modes

        sort : bool, optional
            Alphabetically sort the packages

        gpu : bool
            Gather information about the GPU. Defaults to ``True`` but if
            experiencing renderinng issues, pass ``False`` to safely generate
            a report.

        """

        # Mandatory packages.
        core = ['pyvista', 'matplotlib', 'PIL', 'pexpect', 'ansys.grpc.dpf']

        # Optional packages.
        optional = []

        # Information about the GPU - bare except in case there is a rendering
        # bug that the user is trying to report.
        if gpu:
            from pyvista.utilities.errors import GPUInfo
            try:
                extra_meta = [(t[1], t[0]) for t in GPUInfo().get_info()]
            except:
                extra_meta = ("GPU Details", "error")
        else:
            extra_meta = ("GPU Details", "None")

        super().__init__(additional=additional, core=core,
                         optional=optional, ncol=ncol,
                         text_width=text_width, sort=sort,
                         extra_meta=extra_meta)
