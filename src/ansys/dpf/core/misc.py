"""Miscellaneous functions for the DPF module."""
import platform
import glob
import os

import packaging.version
import pkg_resources
import importlib
from pkgutil import iter_modules
from ansys.dpf.gate._version import __ansys_version__
from ansys.dpf.gate import load_api

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
    """Give input path back if given, else look for ANSYS_DPF_PATH,
    then among AWP_ROOT and installed ansys-dpf-server modules to take the latest available.

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
    # Then check for usual installation folders with AWP_ROOT and installed modules
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
            '- or by setting it by default with the environment variable "ANSYS_DPF_PATH"'
        )
    return ansys_path


def _pythonize_awp_version(version):
    if len(version) != 3:
        return version
    return "20" + version[0:2] + "." + version[2]


def _find_latest_ansys_versions():
    if hasattr(load_api, "_find_latest_ansys_versions"):
        return load_api._find_latest_ansys_versions()
    awp_versions = [key[-3:] for key in os.environ.keys() if "AWP_ROOT" in key]
    installed_packages_list = {}

    for awp_version in awp_versions:
        if not awp_version.isnumeric():
            continue
        ansys_path = os.environ.get("AWP_ROOT" + awp_version)
        if ansys_path:
            installed_packages_list[
                packaging.version.parse(_pythonize_awp_version(awp_version))
            ] = ansys_path

    installed_packages = pkg_resources.working_set
    for i in installed_packages:
        if "ansys-dpf-server" in i.key:
            file_name = pkg_resources.to_filename(i.project_name.replace("ansys-dpf-", ""))
            try:
                module = importlib.import_module("ansys.dpf." + file_name)
                installed_packages_list[
                    packaging.version.parse(module.__version__)
                ] = module.__path__[0]
            except ModuleNotFoundError:
                pass
            except AttributeError:
                pass
    if len(installed_packages_list) > 0:
        return installed_packages_list[sorted(installed_packages_list)[-1]]


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
    latest_install = _find_latest_ansys_versions()
    if latest_install:
        return latest_install

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
