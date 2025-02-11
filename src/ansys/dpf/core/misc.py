# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Miscellaneous functions for the DPF module."""

import glob
import os
from pathlib import Path
from pkgutil import iter_modules
import platform
import re

from ansys.dpf.core import errors
from ansys.dpf.gate import load_api
from ansys.dpf.gate._version import __ansys_version__

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
    """Return the input path if provided; otherwise, check ANSYS_DPF_PATH, AWP_ROOT, and the latest ansys-dpf-server modules.

    Give input path back if given, else look for ANSYS_DPF_PATH,
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
        if ansys_path:
            ansys_path = ansys_path.replace('"', "")
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
    # parse the version to an int and check for supported
    ansys_folder_name = Path(ansys_path).parts[-1]
    reobj_vXYZ = re.compile("^v[0123456789]{3}$")
    if reobj_vXYZ.match(ansys_folder_name):
        # vXYZ Unified Install folder
        ver = int(str(ansys_path)[-3:])
    else:
        ver = 222
    if ver < 211:
        raise errors.InvalidANSYSVersionError(f"Ansys v{ver} does not support DPF")
    if ver == 211 and is_ubuntu():
        raise OSError("DPF on v211 does not support Ubuntu")
    return ansys_path


def _pythonize_awp_version(version):
    if len(version) != 3:
        return version
    return "20" + version[0:2] + "." + version[2]


def _find_latest_ansys_versions():
    return load_api._find_latest_ansys_versions()


def find_ansys():
    """Check ANSYS environment variables or default paths for the latest installation.

    Search for a standard ANSYS environment variable (AWP_ROOTXXX) or a standard installation
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
        base_path = Path(os.environ["PROGRAMFILES"]) / "ANSYS INC"
    elif os.name == "posix":
        for path in [Path("/usr/ansys_inc"), Path("/ansys_inc")]:
            if path.is_dir():
                base_path = path
    else:
        raise OSError(f"Unsupported OS {os.name}")

    if base_path is None:
        return base_path

    paths = list(base_path.glob("v*"))

    if not paths:
        return None

    versions = {}
    for path in paths:
        ver_str = str(path)[-3:]
        if is_float(ver_str):
            versions[int(ver_str)] = str(path)

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
