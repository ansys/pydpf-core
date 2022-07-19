"""Miscellaneous functions for the DPF module."""
import platform
import glob
import os
from pkgutil import iter_modules


DEFAULT_FILE_CHUNK_SIZE = 524288
DYNAMIC_RESULTS = True
RETURN_ARRAYS = True

RUNTIME_CLIENT_CONFIG = None


def module_exists(module_name):
    """Check if a model exists.

    Parameters
    ----------
    module_name : str
        Name of the module.

    """
    return module_name in (name for loader, name, ispkg in iter_modules())


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
    if os.name == "posix":
        return "ubuntu" in platform.platform().lower()
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
    if os.name == "nt":
        base_path = os.path.join(os.environ["PROGRAMFILES"], "ANSYS INC")
    elif os.name == "posix":
        for path in ["/usr/ansys_inc", "/ansys_inc"]:
            if os.path.isdir(path):
                base_path = path
    else:
        raise OSError(f"Unsupported OS {os.name}")

    if base_path is None:
        return base_path

    paths = glob.glob(os.path.join(base_path, "v*"))

    if not paths:
        return None

    versions = {}
    for path in paths:
        ver_str = path[-3:]
        if is_float(ver_str):
            versions[int(ver_str)] = path

    return versions[max(versions.keys())]


def is_pypim_configured():
    """Check if the environment is configured for PyPIM, without using pypim.
    This method is equivalent to ansys.platform.instancemanagement.is_configured(). It's
    reproduced here to avoid having hard dependencies.
    Returns
    -------
    bool
        ``True`` if the environment is setup to use the PIM API, ``False`` otherwise.
    """
    return "ANSYS_PLATFORM_INSTANCEMANAGEMENT_CONFIG" in os.environ
