"""Miscellaneous functions for the DPF module."""
import platform
import glob
import os
from pkgutil import iter_modules


DEFAULT_FILE_CHUNK_SIZE =65536

# ANSYS CPython Workbench environment may not have scooby installed.
try:
    from scooby import Report as ScoobyReport
except ImportError:
    class ScoobyReport():
        """Placeholder for Scooby report."""

        def __init__(self, *args, **kwargs):
            raise ImportError('Install `scooby` with `pip install scooby` to use '
                              'this feature')


def module_exists(module_name):
    """Check if a model exists.
    
    Parameters
    ----------
    module_name : str
        Name of the module.
        
    """
    return module_name in (name for loader, name, ispkg in iter_modules())


class Report(ScoobyReport):
    """Generate a report of the installed packages for DPF-Core."""

    def __init__(self, additional=None, ncol=3, text_width=80, sort=False,
                 gpu=True):
        """Generate a :class:`scooby.Report` instance.

        Parameters
        ----------
        additional : list(ModuleType), list(str)
            List of packages or package names to add to the output information.
        ncol : int, optional
            Number of package columns in the HTML table. This parameter has effect 
            only if ``mode='HTML'`` or ``mode='html'``. The default is ``3``.
        text_width : int, optional
            Width of the text for non-HTML display modes. The default is ``80``.
        sort : bool, optional
            Whether to sort the packages alphabetically. The default is "False``.
        gpu : bool, optional
            Whether to gather information about the GPU. The default is ``True``.
            If rendering issues are experiencd, set to ``False`` to safely generate
            the report.

        """

        # Mandatory packages.
        core = ['ansys.grpc.dpf']

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
    """Check if a string can be converted to a float.
    
    Parameters
    ----------
    string : str
       String to check.
    
    Returns
    -------
    bool
        ``True`` if the input can be converted to a float, ``False`` if otherwise.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_ubuntu():
    """Check if the operating system is Ubuntu.
    
    Returns
    -------
    bool
        ``True`` when the operating system is Ubuntu, ``False`` if otherwise.
    """
    if os.name == 'posix':
        return 'ubuntu' in platform.platform().lower()
    return False


def find_ansys():
    """Search the standard installation location to find the path to the latest Ansys installation.
        
    Returns
    -------
    ansys_path : str
        Full path to the latest version of the Ansys installation. 

    Examples
    --------
    Return path of latest Ansys version on Windows.

    >>> from ansys.dpf.core.misc import find_ansys
    >>> path = find_ansys()
    
    Return path of latest Ansys version on Linux.

    >>> path = find_ansys()
    
    """
    base_path = None
    if os.name == 'nt':
        base_path = os.path.join(os.environ['PROGRAMFILES'], 'ANSYS INC')
    elif os.name == 'posix':
        for path in ['/usr/ansys_inc', '/ansys_inc']:
            if os.path.isdir(path):
                base_path = path
    else:
        raise OSError(f'Unsupported OS {os.name}')

    if base_path is None:
        return base_path

    paths = glob.glob(os.path.join(base_path, 'v*'))

    if not paths:
        return None

    versions = {}
    for path in paths:
        ver_str = path[-3:]
        if is_float(ver_str):
            versions[int(ver_str)] = path

    return versions[max(versions.keys())]
