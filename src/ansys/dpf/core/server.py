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
Server.

Contains the directives necessary to start the DPF server.
"""

import copy
import functools
import inspect
import os
import platform
import socket
import sys
import traceback
from typing import Union
import warnings
import weakref

from ansys import dpf
from ansys.dpf.core import errors, server_context
from ansys.dpf.core.misc import get_ansys_path, is_ubuntu
from ansys.dpf.core.server_factory import (
    CommunicationProtocols,
    ServerConfig,
    ServerFactory,
)
from ansys.dpf.core.server_types import DPF_DEFAULT_PORT, LOCALHOST, RUNNING_DOCKER, BaseServer


def shutdown_global_server():
    """Shut down the global DPF server."""
    try:
        if dpf.core.SERVER is not None:
            dpf.core.SERVER = None
    except:
        warnings.warn(traceback.format_exc())
        pass


def has_local_server():
    """Check if a local DPF gRPC server has been created.

    Returns
    -------
    bool
        ``True`` when a local DPF gRPC server has been created.

    """
    return dpf.core.SERVER is not None


def _global_server() -> BaseServer:
    """Retrieve the global server if it exists.

    If the global server has not been specified, check the expected server type in
    the current configuration and start one.


    if the user
    has specified the "DPF_START_SERVER" environment variable.  If
    ``True``, start the server locally.  If ``False``, connect to the
    existing server.
    """
    # if global variable dpf.core.SERVER exists
    if hasattr(dpf, "core") and hasattr(dpf.core, "SERVER"):
        # If no server is currently registered
        if dpf.core.SERVER is None:
            # Depending on the DPF_START_SERVER environment variable,
            # if false, do not start a new server, and try to connect to one with default parameters
            if os.environ.get("DPF_START_SERVER", "").lower() == "false":
                ip = os.environ.get("DPF_IP", LOCALHOST)
                port = int(os.environ.get("DPF_PORT", DPF_DEFAULT_PORT))
                connect_to_server(ip, port)
            # if true, start a server
            else:
                start_local_server(as_global=True)
        return dpf.core.SERVER
    return None


def set_server_configuration(server_config: ServerConfig) -> None:
    """Set the default type of DPF server to use for the current python session, .

    Parameters
    ----------
    server_config: ServerConfig
        Manages the type of server connection to use by default.
    """
    dpf.core.SERVER_CONFIGURATION = server_config


def port_in_use(port, host=LOCALHOST):
    """Check if a port is in use at the given host.

    The port must actually "bind" the address. Just checking to see if a
    socket can be created is insufficient because it's possible to run into
    permission errors like: ``An attempt was made to access a socket in a way
    forbidden by its access permissions.``

    Returns
    -------
    bool
        ``True`` when the port is in use, ``False`` when free.

    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind((host, port))
            return False
        except:
            return True


def shutdown_all_session_servers():
    """Shut down all active servers created by this module."""
    from ansys.dpf.core import _server_instances

    copy_instances = copy.deepcopy(_server_instances)
    for instance in copy_instances:
        try:
            if hasattr(instance(), "shutdown"):
                instance().shutdown()
        except Exception as e:
            print(e.args)
            pass
    shutdown_global_server()


def start_local_server(
    ip=LOCALHOST,
    port=DPF_DEFAULT_PORT,
    ansys_path=None,
    as_global=True,
    load_operators=True,
    use_docker_by_default=True,
    docker_config=RUNNING_DOCKER,
    timeout=20.0,
    config=None,
    use_pypim_by_default=True,
    context=None,
) -> BaseServer:
    """Start a new local DPF server at a given port and IP address.

    This method requires Windows and ANSYS 2021 R1 or later. If ``as_global=True``, which is
    the default) the server is stored globally, replacing the one stored previously.
    Otherwise, a user must keep a handle on their server.

    Parameters
    ----------
    ip : str, optional
        IP address of the remote or local instance to connect to. The
        default is ``"LOCALHOST"``.
    port : int, optional
        Port to connect to the remote instance on. The default is
        ``"DPF_DEFAULT_PORT"``, which is 50054.
    ansys_path : str or os.PathLike, optional
        Root path for the Ansys installation directory. For example, ``"/ansys_inc/v212/"``.
        The default is the latest Ansys installation.
    as_global : bool, optional
        Global variable that stores the IP address and port for the DPF
        module. All DPF objects created in this Python session will
        use this IP and port. The default is ``True``.
    load_operators : bool, optional
        Whether to automatically load the math operators. The default is ``True``.
    use_docker_by_default : bool, optional
        If the environment variable DPF_DOCKER is set to a docker name and use_docker_by_default
        is True, the server is ran as a docker (default is True).
    docker_config : server_factory.DockerConfig, optional
        To start DPF server as a docker, specify the docker configuration options here.
    timeout : float, optional
        Maximum number of seconds for the initialization attempt.
        The default is ``10``. Once the specified number of seconds
        passes, the connection fails.
    config: ServerConfig, optional
        Manages the type of server connection to use.
    use_pypim_by_default: bool, optional
        Whether to use PyPIM functionalities by default when a PyPIM environment is detected.
        Defaults to True.
    context: ServerContext, optional
        Defines the settings that will be used to load DPF's plugins.
        A DPF xml file can be used to list the plugins and set up variables. Default is
        `server_context.SERVER_CONTEXT`.

    Returns
    -------
    server : server.ServerBase
    """
    from ansys.dpf.core.misc import is_pypim_configured

    use_docker = use_docker_by_default and docker_config.use_docker
    use_pypim = use_pypim_by_default and is_pypim_configured()
    if not use_docker and not use_pypim:
        ansys_path = get_ansys_path(ansys_path)

    # avoid using any ports in use from existing servers
    used_ports = []
    if dpf.core._server_instances:
        for srv in dpf.core._server_instances:
            if srv() and hasattr(srv(), "port"):
                used_ports.append(srv().port)

    while port in used_ports:
        port += 1

    # verify port is free
    while port_in_use(port):
        port += 1

    if use_docker:
        port = docker_config.find_port_available_for_docker_bind(port)
    else:
        docker_config.use_docker = False

    if context is None:
        context = server_context.SERVER_CONTEXT

    server = None
    n_attempts = 3
    timed_out = False
    for _ in range(n_attempts):
        try:
            # Force LegacyGrpc when on macOS
            if platform.system() == "Darwin":
                config = dpf.core.AvailableServerConfigs.LegacyGrpcServer
            server_type = ServerFactory.get_server_type_from_config(
                config, ansys_path, docker_config
            )
            server_init_signature = inspect.signature(server_type.__init__)
            if (
                "ip" in server_init_signature.parameters.keys()
                and "port" in server_init_signature.parameters.keys()
            ):
                server = server_type(
                    ansys_path,
                    ip,
                    port,
                    as_global=as_global,
                    launch_server=True,
                    load_operators=load_operators,
                    docker_config=docker_config,
                    timeout=timeout,
                    use_pypim=use_pypim,
                    context=context,
                )
            else:
                server = server_type(
                    ansys_path,
                    as_global=as_global,
                    load_operators=load_operators,
                    timeout=timeout,
                    context=context,
                )
            break
        except errors.InvalidPortError:  # allow socket in use errors
            port += 1
        except TimeoutError:
            if timed_out:
                break
            import warnings

            warnings.warn(
                f"Failed to start a server in {timeout}s, "
                + f"trying again once in {timeout * 2.}s."
            )
            timeout *= 2.0
            timed_out = True

    if server is None:
        raise OSError(
            f"Unable to launch the server after {n_attempts} attempts.  "
            f"Check the following path:\n{str(ansys_path)}\n\n"
            "or attempt to use a different port"
        )

    dpf.core._server_instances.append(weakref.ref(server))
    return server


def connect_to_server(
    ip=LOCALHOST,
    port=DPF_DEFAULT_PORT,
    as_global=True,
    timeout=10.0,
    config=None,
    context=None,
):
    """Connect to an existing DPF server.

    This method sets the global default channel that is then used for the
    duration of the DPF session.

    Parameters
    ----------
    ip : str
        IP address of the remote or local instance to connect to. The
        default is ``"LOCALHOST"``.
    port : int
        Port to connect to the remote instance on. The default is
        ``"DPF_DEFAULT_PORT"``, which is 50054.
    as_global : bool, optional
        Global variable that stores the IP address and port for the DPF
        module. All DPF objects created in this Python session will
        use this IP and port. The default is ``True``.
    timeout : float, optional
        Maximum number of seconds for the initialization attempt.
        The default is ``10``. Once the specified number of seconds
        passes, the connection fails.
    config: ServerConfig, optional
        Manages the type of server connection to use. Forced to LegacyGrpc on macOS.
    context: ServerContext, optional
        Defines the settings that will be used to load DPF's plugins.
        A DPF xml file can be used to list the plugins and set up variables. Default is
        `server_context.SERVER_CONTEXT`.

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    Create a server.

    >>> #server = dpf.start_local_server(ip = '127.0.0.1')
    >>> #port = server.port

    Connect to a remote server at a non-default port.

    >>> #specified_server = dpf.connect_to_server('127.0.0.1', port, as_global=False)

    Connect to the localhost at the default port.

    >>> #unspecified_server = dpf.connect_to_server(as_global=False)

    """
    if context is None:
        context = server_context.SERVER_CONTEXT

    def connect():
        server_init_signature = inspect.signature(server_type.__init__)
        if (
            "ip" in server_init_signature.parameters.keys()
            and "port" in server_init_signature.parameters.keys()
        ):
            server = server_type(
                ip=ip,
                port=port,
                as_global=as_global,
                launch_server=False,
                context=context,
                timeout=timeout,
            )
        else:
            server = server_type(as_global=as_global, context=context)
        dpf.core._server_instances.append(weakref.ref(server))
        return server

    # Enforce LegacyGrpc when on macOS
    if platform.system() == "Darwin":
        config = dpf.core.AvailableServerConfigs.LegacyGrpcServer

    server_type = ServerFactory.get_remote_server_type_from_config(config)
    try:
        return connect()
    except ModuleNotFoundError as e:
        if "use a LegacyGrpcServer" in e.msg:
            server_type = ServerFactory.get_remote_server_type_from_config(
                ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)
            )
            warnings.warn(
                UserWarning(
                    "Could not connect to remote server as ansys.dpf.gatebin "
                    "is missing. Trying again using LegacyGrpcServer.\n"
                    f"The error stated:\n{e.msg}"
                )
            )
            return connect()
        raise e


def get_or_create_server(server: BaseServer) -> Union[BaseServer, None]:
    """Return the given server or if None, creates a new one.

    Parameters
    ----------
    server: BaseServer, None

    Returns
    -------
    server: returns the newly created server, or the server given.
    """
    if server:
        return server
    return _global_server()


def available_servers():
    """Search all available installed DPF servers on the current machine.

    This method binds new functions to the server module, which helps to choose the appropriate version.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> #out = dpf.server.available_servers()

    After this call, you can do the following:

    >>> #server = dpf.server.start_2024_2_server()

    Equivalent to:
    >>> #server = out["2024.1"]()

    Returns
    -------
    server: dict{str:func}
        Map of available DPF servers with key=version, value=function starting server when called.
        See :py:func:`ansys.dpf.core.server.start_local_server` for function doc.
    """
    from ansys.dpf.gate import load_api

    unified = load_api._paths_to_dpf_in_unified_installs()
    standalone = load_api._paths_to_dpf_server_library_installs()

    strver = {}

    out = {}
    strver.update(unified)
    strver.update(standalone)
    for version, path in strver.items():
        bound_method = start_local_server
        method2 = functools.partial(bound_method, ansys_path=path)
        vout = str(version).replace(".", "_")
        setattr(sys.modules[__name__], "start_" + vout + "_server", method2)
        out[str(version)] = method2

    return out
