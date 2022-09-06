"""
Server
======
Contains the directives necessary to start the DPF server.
"""
import io
import os
import socket
import subprocess
import weakref
import copy
import inspect
import warnings
import traceback

from ansys import dpf

from ansys.dpf.core.misc import is_ubuntu, get_ansys_path
from ansys.dpf.core import errors

from ansys.dpf.core.server_factory import ServerConfig, ServerFactory, CommunicationProtocols
from ansys.dpf.core.server_types import DPF_DEFAULT_PORT, LOCALHOST, RUNNING_DOCKER


def shutdown_global_server():
    try:
        if dpf.core.SERVER is not None:
            dpf.core.SERVER.__del__()
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


def _global_server():
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
    """Sets, for the current python session, the default type of DPF server to use.

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
    _server_instances.clear()


def start_local_server(
    ip=LOCALHOST,
    port=DPF_DEFAULT_PORT,
    ansys_path=None,
    as_global=True,
    load_operators=True,
    use_docker_by_default=True,
    docker_name=None,
    timeout=10.,
    config=None,
    use_pypim_by_default=True
):
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
    docker_name : str, optional
        To start DPF server as a docker, specify the docker name here.
    timeout : float, optional
        Maximum number of seconds for the initialization attempt.
        The default is ``10``. Once the specified number of seconds
        passes, the connection fails.
    config: ServerConfig, optional
        Manages the type of server connection to use.
    use_pypim_by_default: bool, optional
        Whether to use PyPIM functionalities by default when a PyPIM environment is detected.
        Defaults to True.

    Returns
    -------
    server : server.ServerBase
    """
    from ansys.dpf.core.misc import is_pypim_configured
    use_docker = use_docker_by_default and (docker_name or RUNNING_DOCKER["use_docker"])
    use_pypim = use_pypim_by_default and is_pypim_configured()
    if not use_docker and not use_pypim:
        ansys_path = get_ansys_path(ansys_path)
        # parse the version to an int and check for supported
        try:
            ver = int(str(ansys_path)[-3:])
            if ver < 211:
                raise errors.InvalidANSYSVersionError(f"Ansys v{ver} does not support DPF")
            if ver == 211 and is_ubuntu():
                raise OSError("DPF on v211 does not support Ubuntu")
        except ValueError:
            pass
    elif RUNNING_DOCKER["use_docker"]:
        docker_name = RUNNING_DOCKER["docker_name"]

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
        port = _find_port_available_for_docker_bind(port)
        config = ServerConfig(CommunicationProtocols.gRPC)

    server = None
    n_attempts = 10
    timed_out = False
    for _ in range(n_attempts):
        try:
            server_type = ServerFactory.get_server_type_from_config(config, ansys_path)
            server_init_signature = inspect.signature(server_type.__init__)
            if "ip" in server_init_signature.parameters.keys() and \
                    "port" in server_init_signature.parameters.keys():
                server = server_type(
                    ansys_path, ip, port, as_global=as_global, launch_server=True,
                    load_operators=load_operators, docker_name=docker_name, timeout=timeout,
                    use_pypim=use_pypim)
            else:
                server = server_type(
                    ansys_path, as_global=as_global,
                    load_operators=load_operators, docker_name=docker_name, timeout=timeout)
            break
        except errors.InvalidPortError:  # allow socket in use errors
            port += 1
        except TimeoutError:
            if timed_out:
                break
            import warnings
            warnings.warn(f"Failed to start a server in {timeout}s, " +
                          f"trying again once in {timeout*2.}s.")
            timeout *= 2.
            timed_out = True

    if server is None:
        raise OSError(
            f"Unable to launch the server after {n_attempts} attempts.  "
            "Check the following path:\n{str(ansys_path)}\n\n"
            "or attempt to use a different port"
        )

    dpf.core._server_instances.append(weakref.ref(server))
    return server


def connect_to_server(ip=LOCALHOST, port=DPF_DEFAULT_PORT, as_global=True, timeout=5, config=None):
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
        Manages the type of server connection to use.

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
    def connect():
        server_init_signature = inspect.signature(server_type.__init__)
        if "ip" in server_init_signature.parameters.keys() \
                and "port" in server_init_signature.parameters.keys():
            server = server_type(
                ip=ip, port=port, as_global=as_global, launch_server=False
            )
        else:
            server = server_type(
                as_global=as_global
            )
        dpf.core._server_instances.append(weakref.ref(server))
        return server

    server_type = ServerFactory.get_remote_server_type_from_config(config)
    try:
        return connect()
    except ModuleNotFoundError as e:
        if "gatebin" in e.msg:
            server_type = ServerFactory.get_remote_server_type_from_config(
                ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True))
            warnings.warn(UserWarning("Could not connect to remote server as ansys-dpf--gatebin "
                                      "is missing. Trying again using LegacyGrpcServer.\n"
                                      f"The error stated:\n{e.msg}"))
            return connect()


def get_or_create_server(server):
    """Returns the given server or if None, creates a new one.

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


def _find_port_available_for_docker_bind(port):
    run_cmd = "docker ps --all"
    if os.name == 'posix':
        process = subprocess.Popen(
            run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
    else:
        process = subprocess.Popen(
            run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    used_ports = []
    for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
        if not ("CONTAINER ID" in line):
            split = line.split("0.0.0.0:")
            if len(split) > 1:
                used_ports.append(int(split[1].split("-")[0]))
    while port in used_ports:
        port += 1
    return port
