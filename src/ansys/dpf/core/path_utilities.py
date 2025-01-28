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

"""
path_utilities.

Offer tools similar to os.path but taking the os of the
server into account to create path.
"""

import os
from pathlib import Path

from ansys.dpf.core import server as server_module
import ansys.dpf.core.server_types


def join(*args, **kwargs):
    """Join two strings to form a path, following the server architecture.

    Using a server version below 3.0, please ensure that the
    python client and the server's os are similar before
    using this method.

    Parameters
    ----------
    args : str, os.PathLike, LegacyGrpcServer
        Path to join and optionally a server.

    kwargs : LegacyGrpcServer
        server=.

    server : Server
        Specific server to use.

    Returns
    -------
    concatenated_file_path : str
        left_path + right_path concatenated into a single string value.

    """
    server = None
    parts = []
    for a in args:
        if isinstance(a, (str, Path)) and len(str(a)) > 0:
            parts.append(str(a))
        elif isinstance(a, ansys.dpf.core.server_types.LegacyGrpcServer):
            server = a
    if "server" in kwargs:
        server = kwargs["server"]
    if not server:
        server = server_module._global_server()
    if not server:
        if ansys.dpf.core.server_types.RUNNING_DOCKER.use_docker:
            current_os = "posix"
        else:
            return str(Path(args[0]).joinpath(*args[1:]))
    else:
        current_os = server.os

    if len(parts) == 0:
        return ""
    separator = "\\"
    if current_os == "posix":
        separator = "/"
    path_to_return = parts[0]
    for ipath in range(1, len(parts)):
        path_to_return += separator + parts[ipath]
    return path_to_return


def to_server_os(path, server=None):
    """Return path to the server depending on the os."""
    path = str(path)
    server = server_module.get_or_create_server(server)
    path = server.docker_config.replace_with_mounted_volumes(path)
    if server.os == "posix":
        return path.replace("\\", "/")
    else:
        return path.replace("/", "\\")
