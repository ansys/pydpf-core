"""
Server
======
Contains the directives necessary to start the DPF server.
"""
from threading import Thread
import io
import logging
import time
import os
import socket
import subprocess
import grpc
import weakref
import copy

from ansys import dpf
from ansys.dpf.core.misc import find_ansys, is_ubuntu
from ansys.dpf.core import errors

from ansys.dpf.core._version import (
    __ansys_version__,
    server_to_ansys_version,
    server_to_ansys_grpc_dpf_version
)
import ansys.grpc.dpf

from dpf.core.server_types import DpfServer, GrpcCServer, DirectCServer

MAX_PORT = 65535

LOG = logging.getLogger(__name__)
LOG.setLevel("DEBUG")

# default DPF server port
DPF_DEFAULT_PORT = int(os.environ.get("DPF_PORT", 50054))
LOCALHOST = os.environ.get("DPF_IP", "127.0.0.1")

RUNNING_DOCKER = {"use_docker": "DPF_DOCKER" in os.environ.keys()}
if RUNNING_DOCKER["use_docker"]:
    RUNNING_DOCKER["docker_name"] = os.environ.get("DPF_DOCKER")
RUNNING_DOCKER['args'] = ""


def shutdown_global_server():
    try:
        if dpf.core.SERVER != None:
            dpf.core.SERVER.__del__()
    except:
        pass

# atexit.register(shutdown_global_server)


def has_local_server():
    """Check if a local DPF gRPC server has been created.

    Returns
    -------
    bool
        ``True`` when a local DPF gRPC server has been created.

    """
    return dpf.core.SERVER is not None


class CommunicationProtocols:
    gRPC = "gRPC"
    direct = "direct"


class ServerConfig:
    """Provides an instance of ServerConfig object to manage the default server type used
    """
    def __init__(self, c_server=False, remote_protocol=CommunicationProtocols.gRPC):
        self.c_server = c_server
        self.remote_protocol = remote_protocol

    def __str__(self):
        return f"Server configuration: c_server={self.c_server}, " \
               f"remote protocol={self.remote_protocol}"


class ServerFactory:
    @staticmethod
    def get_server_type_from_config():
        config = dpf.core.SERVER_CONFIGURATION
        # dpf.core.SERVER_CONFIGURATION is required to know what type of connection to set
        if config is None:
            # If no SERVER_CONFIGURATION is yet defined, set one with default values
            dpf.core.SERVER_CONFIGURATION = ServerConfig()
            config = dpf.core.SERVER_CONFIGURATION
        if config.remote_protocol == CommunicationProtocols.gRPC and config.c_server is False:
            return DpfServer
        elif config.remote_protocol == CommunicationProtocols.gRPC and config.c_server:
            return GrpcCServer
        elif config.remote_protocol == CommunicationProtocols.direct and config.c_server:
            return DirectCServer
        else:
            raise NotImplementedError("Server config not available.")


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
                start_local_server()
        return dpf.core.SERVER
    return None


def set_server_configuration(server_config: ServerConfig) -> None:
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


def check_valid_ip(ip):
    """Check if a valid IP address is entered.

    This method raises an error when an invalid IP address is entered.
    """
    try:
        socket.inet_aton(ip)
    except OSError:
        raise ValueError(f'Invalid IP address "{ip}"')


def shutdown_all_session_servers():
    """Shut down all active servers created by this module."""
    from ansys.dpf.core import _server_instances

    copy_instances = copy.deepcopy(_server_instances)
    for instance in copy_instances:
        try:
            instance().shutdown()
        except Exception as e:
            print(e.args)
            pass


def start_local_server(
    ip=LOCALHOST,
    port=DPF_DEFAULT_PORT,
    ansys_path=None,
    as_global=True,
    load_operators=True,
    use_docker_by_default=True,
    docker_name=None,
    timeout=10.
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
    port : int
        Port to connect to the remote instance on. The default is
        ``"DPF_DEFAULT_PORT"``, which is 50054.
    ansys_path : str, optional
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

    Returns
    -------
    server : server.ServerBase
    """
    use_docker = use_docker_by_default and (docker_name or RUNNING_DOCKER["use_docker"])
    if not use_docker:
        if ansys_path is None:
            ansys_path = os.environ.get("AWP_ROOT" + __ansys_version__, find_ansys())
        if ansys_path is None:
            raise ValueError(
                "Unable to automatically locate the Ansys path  "
                f"for version {__ansys_version__}."
                "Manually enter one when starting the server or set it "
                'as the environment variable "ANSYS_PATH"'
            )

        # verify path exists
        if not os.path.isdir(ansys_path):
            raise NotADirectoryError(f'Invalid Ansys path "{ansys_path}"')

        # parse the version to an int and check for supported
        try:
            ver = int(ansys_path[-3:])
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
            if srv():
                used_ports.append(srv().port)

    while port in used_ports:
        port += 1

    # verify port is free
    while port_in_use(port):
        port += 1

    if use_docker:
        port = _find_port_available_for_docker_bind(port)

    server = None
    n_attempts = 10
    for _ in range(n_attempts):
        try:
            server = ServerFactory().get_server_type_from_config()(
                ansys_path, ip, port, as_global=as_global,
                load_operators=load_operators, docker_name=docker_name
            )
            break
        except errors.InvalidPortError:  # allow socket in use errors
            port += 1

    if server is None:
        raise OSError(
            f"Unable to launch the server after {n_attempts} attempts.  "
            "Check the following path:\n{ansys_path}\n\n"
            "or attempt to use a different port"
        )

    dpf.core._server_instances.append(weakref.ref(server))
    return server


def connect_to_server(ip=LOCALHOST, port=DPF_DEFAULT_PORT, as_global=True, timeout=5):
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
    server = ServerFactory().get_server_type_from_config()(ip=ip, port=port,
                                                      as_global=as_global, launch_server=False,
                                                      timeout=timeout)
    dpf.core._server_instances.append(weakref.ref(server))
    return server


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
    process = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    used_ports = []
    for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
        if not ("CONTAINER ID" in line):
            split = line.split("0.0.0.0:")
            if len(split) > 1:
                used_ports.append(int(split[1].split("-")[0]))
    while port in used_ports:
        port += 1
    return port


def _run_launch_server_process(ansys_path, ip, port, docker_name):
    if docker_name:
        docker_server_port = int(os.environ.get("DOCKER_SERVER_PORT", port))
        dpf_run_dir = os.getcwd()
        from ansys.dpf.core import LOCAL_DOWNLOADED_EXAMPLES_PATH
        if os.name == "nt":
            run_cmd = f"docker run -d -p {port}:{docker_server_port} " \
                      f"{RUNNING_DOCKER['args']} " \
                      f'-v "{LOCAL_DOWNLOADED_EXAMPLES_PATH}:/tmp/downloaded_examples" ' \
                      f"-e DOCKER_SERVER_PORT={docker_server_port} " \
                      f"--expose={docker_server_port} " \
                      f"{docker_name}"
        else:
            run_cmd = ["docker run",
                       "-d",
                       f"-p"+f"{port}:{docker_server_port}",
                       RUNNING_DOCKER['args'],
                       f'-v "{LOCAL_DOWNLOADED_EXAMPLES_PATH}:/tmp/downloaded_examples"'
                       f"-e DOCKER_SERVER_PORT={docker_server_port}",
                       f"--expose={docker_server_port}",
                       docker_name]
    else:
        if os.name == "nt":
            run_cmd = f"Ans.Dpf.Grpc.bat --address {ip} --port {port}"
            path_in_install = "aisol/bin/winx64"
        else:
            run_cmd = ["./Ans.Dpf.Grpc.sh", f"--address {ip}", f"--port {port}"]
            path_in_install = "aisol/bin/linx64"

        # verify ansys path is valid
        if os.path.isdir(f"{ansys_path}/{path_in_install}"):
            dpf_run_dir = f"{ansys_path}/{path_in_install}"
        else:
            dpf_run_dir = f"{ansys_path}"
        if not os.path.isdir(dpf_run_dir):
            raise NotADirectoryError(
                f'Invalid ansys path at "{ansys_path}".  '
                "Unable to locate the directory containing DPF at "
                f'"{dpf_run_dir}"'
            )

    old_dir = os.getcwd()
    os.chdir(dpf_run_dir)
    process = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.chdir(old_dir)
    return process


def launch_dpf(ansys_path, ip=LOCALHOST, port=DPF_DEFAULT_PORT, timeout=10, docker_name=None):
    """Launch Ansys DPF.

    Parameters
    ----------
    ansys_path : str, optional
        Root path for the Ansys installation directory. For example, ``"/ansys_inc/v212/"``.
        The default is the latest Ansys installation.
    ip : str, optional
        IP address of the remote or local instance to connect to. The
        default is ``"LOCALHOST"``.
    port : int
        Port to connect to the remote instance on. The default is
        ``"DPF_DEFAULT_PORT"``, which is 50054.
    timeout : float, optional
        Maximum number of seconds for the initialization attempt.
        The default is ``10``. Once the specified number of seconds
        passes, the connection fails.
    docker_name : str, optional
        To start DPF server as a docker, specify the docker name here.

    Returns
    -------
    process : subprocess.Popen
        DPF Process.
    """
    process = _run_launch_server_process(ansys_path, ip, port, docker_name)

    # check to see if the service started
    lines = []
    docker_id = []

    def read_stdout():
        for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
            LOG.debug(line)
            lines.append(line)
        if docker_name:
            docker_id.append(lines[0].replace("\n", ""))
            docker_process = subprocess.Popen(f"docker logs {docker_id[0]}",
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
            for line in io.TextIOWrapper(docker_process.stdout, encoding="utf-8"):
                LOG.debug(line)
                lines.append(line)

    current_errors = []

    def read_stderr():
        for line in io.TextIOWrapper(process.stderr, encoding="utf-8"):
            LOG.error(line)
            current_errors.append(line)

    # must be in the background since the process reader is blocking
    Thread(target=read_stdout, daemon=True).start()
    Thread(target=read_stderr, daemon=True).start()

    t_timeout = time.time() + timeout
    started = False
    while not started:
        started = any("server started" in line for line in lines)

        if time.time() > t_timeout:
            raise TimeoutError(f"Server did not start in {timeout} seconds")

    # verify there were no errors
    time.sleep(0.1)
    if current_errors:
        try:
            process.kill()
        except PermissionError:
            pass
        errstr = "\n".join(errors)
        if "Only one usage of each socket address" in errstr:
            raise errors.InvalidPortError(f"Port {port} in use")
        raise RuntimeError(errstr)

    if len(docker_id) > 0:
        return docker_id[0]


def check_ansys_grpc_dpf_version(server, timeout):
    state = grpc.channel_ready_future(server.channel)
    # verify connection has matured
    tstart = time.time()
    while ((time.time() - tstart) < timeout) and not state._matured:
        time.sleep(0.001)

    if not state._matured:
        raise TimeoutError(
            f"Failed to connect to {server._input_ip}:{server._input_port} in {timeout} seconds"
        )

    LOG.debug("Established connection to DPF gRPC")
    grpc_module_version = ansys.grpc.dpf.__version__
    server_version = server.version
    right_grpc_module_version = server_to_ansys_grpc_dpf_version.get(server_version, None)
    if right_grpc_module_version and right_grpc_module_version != grpc_module_version:
        raise ImportWarning(f"2022R1 Ansys unified install is available. "
                            f"To use DPF server from Ansys "
                            f"{server_to_ansys_version.get(server_version, 'Unknown')}"
                            f" (dpf.SERVER.version=='{server_version}'), "
                            f"install version {right_grpc_module_version} of ansys-grpc-dpf"
                            f" with the command: \n"
                            f"     pip install ansys-grpc-dpf=={right_grpc_module_version}"
                            )
