"""
path_utilities
==============
Offer tools similar to os.path but taking the os of the
server into account to create path.
"""

import os

import ansys.dpf.core.server_types
from ansys.dpf.core import server as server_module
from pathlib import Path


def join(*args, **kwargs):
    """Join two strings to form a path, following the server
    architecture.
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
        if isinstance(a, (str, Path)) and len(a) > 0:
            parts.append(str(a))
        elif isinstance(a, dpf.core.server_types.LegacyGrpcServer):
            server = a
    if "server" in kwargs:
        server = kwargs["server"]
    if not server:
        server = server_module._global_server()
    if not server:
        if dpf.core.server_types.RUNNING_DOCKER["use_docker"]:
            current_os = "posix"
        else:
            return os.path.join(*args)
    else:
        current_os = server.os

    if len(parts) == 0:
        return ""
    separator = "\\"
    if current_os == 'posix':
        separator = "/"
    path_to_return = parts[0]
    for ipath in range(1, len(parts)):
        path_to_return += separator + parts[ipath]
    return path_to_return

def to_server_os(path, server=None):
    path = str(path)
    if not server:
        server = server_module._global_server()
    if not server:
        return path
    if server.os == 'posix':
        return path.replace("\\", "/")
    else:
        return path.replace("/", "\\")

def downloaded_example_path(server = None):
    on_docker = ansys.dpf.core.server_types.RUNNING_DOCKER["use_docker"]
    if not server:
        server = server_module._global_server()
    if server:
        on_docker = server.on_docker
    if on_docker:  # pragma: no cover
        return "/tmp/downloaded_examples"
    else:
        from ansys.dpf.core import LOCAL_DOWNLOADED_EXAMPLES_PATH
        return LOCAL_DOWNLOADED_EXAMPLES_PATH
