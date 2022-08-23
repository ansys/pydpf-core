"""Miscellaneous functions for the DPF module."""
import platform
import glob
import os
from pkgutil import iter_modules
from ansys.dpf.gate._version import (
    __ansys_version__
)


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


def get_ansys_path(ansys_path=None):
    """Give input path back if given, else look for ANSYS_DPF_PATH, then AWP_ROOT+__ansys_version__,
    then calls for find_ansys as a last resort.

    Parameters
    ----------
    ansys_path : str
        Full path to an Ansys installation to use.

    Returns
    -------
    ansys_path : str
        Full path to an Ansys installation.

    """
    # If no custom path was given in input
    # First check the environment variable for a custom path
    if ansys_path is None:
        ansys_path = os.environ.get("ANSYS_DPF_PATH")
    # Then check for usual installation folders with AWP_ROOT and find_ansys
    if ansys_path is None:
        ansys_path = os.environ.get("AWP_ROOT" + __ansys_version__)
    if ansys_path is None:
        ansys_path = find_ansys()
    # If still no install has been found, throw an exception
    if ansys_path is None:
        raise ValueError(
            "Unable to locate any Ansys installation.\n"
            f'Make sure the "AWP_ROOT{__ansys_version__}" environment variable '
            f"is set if using ANSYS version {__ansys_version__}.\n"
            "You can also manually define the path to the ANSYS installation root folder"
            " of the version you want to use (vXXX folder):\n"
            '- when starting the server with "start_local_server(ansys_path=*/vXXX)"\n'
            '- or by setting it by default with the environment variable "ANSYS_DPF_PATH"')
    return ansys_path


def find_ansys():
    """Search for a standard ANSYS environment variable (AWP_ROOTXXX) or a standard installation
    location to find the path to the latest Ansys installation.

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
    versions = [key[-3:] for key in os.environ.keys() if "AWP_ROOT" in key]
    for version in sorted(versions, reverse=True):
        if not version.isnumeric():
            continue
        ansys_path = os.environ.get("AWP_ROOT" + version)
        if ansys_path:
            return ansys_path

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
