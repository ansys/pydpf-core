"""Miscellaneous functions for DPF module"""
import glob
import os
from pkgutil import iter_modules


# ANSYS CPython workbench enviornment may not have scooby installed
try:
    from scooby import Report as ScoobyReport
except ImportError:
    class ScoobyReport():
        """Placeholder for scooby.Report"""

        def __init__(self, *args, **kwargs):
            raise ImportError('Install `scooby` with `pip install scooby` to use '
                              'this feature')


def module_exists(module_name):
    """Returns True when a module exists"""
    return module_name in (name for loader, name, ispkg in iter_modules())


class Report(ScoobyReport):
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


def is_float(string):
    """Returns true when a string can be converted to a float"""
    try:
        float(string)
        return True
    except ValueError:
        return False


def find_ansys():
    """Searches for ansys path within the standard install location
    and returns the path of the latest version.

    Reutrns
    -------
    ansys_path : str
        Full path to ANSYS.  For example:
        'C:\\Program Files\\ANSYS Inc\\v211'
    """
    base_path = os.path.join(os.environ['PROGRAMFILES'], 'ANSYS INC')
    
    if os.name == 'nt':
        paths = glob.glob(os.path.join(base_path, 'v*'))

    if not paths:
        return None

    versions = {}
    for path in paths:
        ver_str = path[-3:]
        if is_float(ver_str):
            versions[int(ver_str)] = path

    return versions[max(versions.keys())]
