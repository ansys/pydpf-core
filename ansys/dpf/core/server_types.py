"""
Server types
============
Contains the different kinds of
servers available for the factory.
"""
import abc
import io
import os
import socket
import subprocess
import time
import warnings
import traceback
from abc import ABC
from threading import Thread

import psutil

import ansys.dpf.core as core
from ansys.dpf.core.check_version import server_meet_version
from ansys.dpf.core import errors, session, server_factory
from ansys.dpf.core._version import (
    server_to_ansys_grpc_dpf_version,
    server_to_ansys_version
)
from ansys.dpf.core.misc import __ansys_version__
from ansys.dpf.gate import load_api, data_processing_grpcapi

import logging

LOG = logging.getLogger(__name__)
LOG.setLevel("DEBUG")
DPF_DEFAULT_PORT = int(os.environ.get("DPF_PORT", 50054))
LOCALHOST = os.environ.get("DPF_IP", "127.0.0.1")
RUNNING_DOCKER = server_factory.create_default_docker_config()

MAX_PORT = 65535


def _get_dll_path(name, ansys_path=None):
    """Helper function to get the right dll path for Linux or Windows"""
    ISPOSIX = os.name == "posix"
    if ansys_path is None:
        ansys_path = os.environ.get("ANSYS_DPF_PATH")
    if ansys_path is None:
        awp_root = "AWP_ROOT" + str(__ansys_version__)
        ANSYS_INSTALL = os.environ.get(awp_root, None)
        if ANSYS_INSTALL is None:
            ANSYS_INSTALL = core.misc.find_ansys()
    else:
        ANSYS_INSTALL = ansys_path
    if ANSYS_INSTALL is None:
        raise ImportError(f"Could not find ansys installation path using {awp_root}.")
    api_path = load_api._get_path_in_install()
    if api_path is None:
        raise ImportError(f"Could not find API path in install.")
    SUB_FOLDERS = os.path.join(ANSYS_INSTALL, api_path)
    if ISPOSIX:
        name = "lib" + name
    return os.path.join(SUB_FOLDERS, name)


def check_valid_ip(ip):
    """Check if a valid IP address is entered.

    This method raises an error when an invalid IP address is entered.
    """
    try:
        socket.inet_aton(ip)
    except OSError:
        raise ValueError(f'Invalid IP address "{ip}"')


def _verify_ansys_path_is_valid(ansys_path, executable, path_in_install=None):
    if path_in_install is None:
        path_in_install = load_api._get_path_in_install()
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
    else:
        if not os.path.exists(os.path.join(dpf_run_dir, executable)):
            raise FileNotFoundError(
                f'DPF executable not found at "{dpf_run_dir}".  '
                f'Unable to locate the executable "{executable}"')
    return dpf_run_dir


def _run_launch_server_process(ip, port, ansys_path=None,
                               docker_config=server_factory.DockerConfig()):
    bShell = False
    if docker_config.use_docker:
        docker_server_port = int(os.environ.get("DOCKER_SERVER_PORT", port))
        dpf_run_dir = os.getcwd()
        if os.name == "posix":
            bShell = True
        run_cmd = docker_config.docker_run_cmd_command(docker_server_port, port)
    else:
        if os.name == "nt":
            executable = "Ans.Dpf.Grpc.bat"
            run_cmd = f"{executable} --address {ip} --port {port}"
        else:
            executable = "./Ans.Dpf.Grpc.sh"  # pragma: no cover
            run_cmd = [executable, f"--address {ip}", f"--port {port}"]  # pragma: no cover
        path_in_install = load_api._get_path_in_install(internal_folder="bin")
        dpf_run_dir = _verify_ansys_path_is_valid(ansys_path, executable, path_in_install)

    old_dir = os.getcwd()
    os.chdir(dpf_run_dir)
    if not bShell:
        process = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        process = subprocess.Popen(
            run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
    os.chdir(old_dir)
    return process


def _wait_and_check_server_connection(
        process, port, timeout, lines, current_errors, stderr=None, stdout=None):
    if not stderr:
        def read_stderr():
            for line in io.TextIOWrapper(process.stderr, encoding="utf-8"):
                LOG.error(line)
                current_errors.append(line)

        stderr = read_stderr
        # check to see if the service started
    if not stdout:
        def read_stdout():
            for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
                LOG.debug(line)
                lines.append(line)

        stdout = read_stdout

    # must be in the background since the process reader is blocking
    Thread(target=stdout, daemon=True).start()
    Thread(target=stderr, daemon=True).start()

    t_timeout = time.time() + timeout
    started = False
    timedout = False
    while not started and len(current_errors) == 0:
        # print(lines)
        started = any("server started" in line for line in lines)

        if time.time() > t_timeout:
            if timedout:
                raise TimeoutError(f"Server did not start in {timeout + timeout} seconds")
            timedout = True
            t_timeout += timeout

    # verify there were no errors
    time.sleep(0.01)
    if current_errors:
        try:
            process.kill()
        except PermissionError:
            pass
        errstr = "\n".join(current_errors)
        if "Only one usage of each socket address" in errstr or \
                "port is already allocated" in errstr:
            raise errors.InvalidPortError(f"Port {port} in use")
        raise RuntimeError(errstr)


def launch_dpf(ansys_path, ip=LOCALHOST, port=DPF_DEFAULT_PORT, timeout=10):
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

    """
    process = _run_launch_server_process(ip, port, ansys_path)
    lines = []
    current_errors = []
    _wait_and_check_server_connection(
        process, port, timeout, lines, current_errors, stderr=None, stdout=None)


def launch_dpf_on_docker(docker_config, ansys_path=None, ip=LOCALHOST, port=DPF_DEFAULT_PORT,
                         timeout=10):
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
    docker_config : server_factory.DockerConfig, optional
        To start DPF server as a docker, specify the docker configurations here.

    Returns
    -------
    running_docker_config : server_factory.RunningDockerConfig

    """
    process = _run_launch_server_process(ip, port, ansys_path, docker_config)

    # check to see if the service started
    lines = []
    docker_id = []
    current_errors = []
    running_docker_config = server_factory.RunningDockerConfig(docker_server_port=port)

    def read_stdout():
        for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
            LOG.debug(line)
            lines.append(line)
            running_docker_config.init_with_stdout(docker_config, LOG, lines, timeout)

    _wait_and_check_server_connection(
        process, port, timeout, lines, current_errors, stderr=None, stdout=read_stdout)

    return running_docker_config


def launch_remote_dpf(version=None):
    try:
        import ansys.platform.instancemanagement as pypim
    except ImportError as e:
        raise ImportError("Launching a remote session of DPF requires the installation"
                          + " of ansys-platform-instancemanagement") from e
    version = version or __ansys_version__
    pim = pypim.connect()
    instance = pim.create_instance(product_name="dpf", product_version=version)
    instance.wait_for_ready()
    grpc_service = instance.services["grpc"]
    if grpc_service.headers:
        LOG.error("Communicating with DPF in this remote environment requires metadata."
                  + "This is not supported, you will likely encounter errors or limitations.")
    return instance


def _compare_ansys_grpc_dpf_version(right_grpc_module_version_str: str, grpc_module_version: str):
    if right_grpc_module_version_str:
        import re
        from packaging.version import parse as parse_version
        right_version_first_numbers = re.search(r"\d", right_grpc_module_version_str)
        right_version_numbers = right_grpc_module_version_str[
                                right_version_first_numbers.start():]
        compare = "==" if right_version_first_numbers.start() == 0 else \
            right_grpc_module_version_str[0:right_version_first_numbers.start()].strip()
        if compare == "==":
            return parse_version(grpc_module_version) == parse_version(right_version_numbers)
        elif compare == ">=":
            return parse_version(grpc_module_version) >= parse_version(right_version_numbers)
        elif compare == ">":
            return parse_version(grpc_module_version) > parse_version(right_version_numbers)
        elif compare == "<=":
            return parse_version(grpc_module_version) <= parse_version(right_version_numbers)
        elif compare == "<":
            return parse_version(grpc_module_version) < parse_version(right_version_numbers)
    return True


def check_ansys_grpc_dpf_version(server, timeout):
    import ansys.grpc.dpf
    import grpc
    state = grpc.channel_ready_future(server.channel)
    # verify connection has matured
    tstart = time.time()
    while ((time.time() - tstart) < timeout) and not state._matured:
        time.sleep(0.001)

    if not state._matured:
        raise TimeoutError(
            f"Failed to connect to {server._input_ip}:{server._input_port} in {timeout} seconds"
        )
    compatibility_link = (f"https://dpf.docs.pyansys.com/getting_started/"
                          f"index.html#client-server-compatibility")
    LOG.debug("Established connection to DPF gRPC")
    grpc_module_version = ansys.grpc.dpf.__version__
    server_version = server.version
    right_grpc_module_version = server_to_ansys_grpc_dpf_version.get(server_version, None)
    if right_grpc_module_version is None:  # pragma: no cover
        # warnings.warn(f"No requirement specified on ansys-grpc-dpf for server version "
        #               f"{server_version}. Continuing with the ansys-grpc-dpf version "
        #               f"installed ({grpc_module_version}). In case of unexpected instability, "
        #               f"please refer to the compatibility guidelines given in "
        #               f"{compatibility_link}.")
        return
    if not _compare_ansys_grpc_dpf_version(right_grpc_module_version, grpc_module_version):
        ansys_version_to_use = server_to_ansys_version.get(server_version, 'Unknown')
        ansys_versions = core._version.server_to_ansys_version
        latest_ansys = ansys_versions[max(ansys_versions.keys())]
        raise ImportWarning(f"An incompatibility has been detected between the DPF server version "
                            f"({server_version} "
                            f"from Ansys {ansys_version_to_use})"
                            f" and the ansys-grpc-dpf version installed ({grpc_module_version})."
                            f" Please consider using the latest DPF server available in the "
                            f"{latest_ansys} Ansys unified install.\n"
                            f"To follow the compatibility guidelines given in "
                            f"{compatibility_link} while still using DPF server {server_version}, "
                            f"please install version {right_grpc_module_version} of ansys-grpc-dpf"
                            f" with the command: \n"
                            f"     pip install ansys-grpc-dpf{right_grpc_module_version}"
                            )


class BaseServer(abc.ABC):
    """Abstract class for servers"""

    @abc.abstractmethod
    def __init__(self):
        """Base class for all types of servers: grpc, in process...
        """
        # TODO: Use _server_id to compare servers for equality?
        self._server_id = None
        self._session_instance = None
        self._base_service_instance = None
        self._docker_config = server_factory.RunningDockerConfig()

    def set_as_global(self, as_global=True):
        """Set the current server as global if necessary.

        Parameters
        ----------
        as_global : bool, optional
            Global variable that stores the IP address and port for the DPF
            module. All DPF objects created in this Python session will
            use this IP and port. The default is ``True``.
        """
        # assign to global channel when requested
        if as_global:
            core.SERVER = self

    def has_client(self):
        return not (self.client is None)

    @property
    @abc.abstractmethod
    def client(self):
        pass

    @property
    @abc.abstractmethod
    def version(self):
        pass

    @property
    @abc.abstractmethod
    def available_api_types(self):
        pass

    @abc.abstractmethod
    def get_api_for_type(self, c_api, grpc_api):
        pass

    @property
    def info(self):
        """Server information.

        Returns
        -------
        info : dictionary
            Dictionary with server information, including ``"server_ip"``,
            ``"server_port"``, ``"server_process_id"``, and
            ``"server_version"`` keys.
        """
        return self._base_service.server_info

    def _del_session(self):
        if self._session_instance:
            self._session_instance.delete()
        self._session_instance = None

    @property
    def _session(self):
        if not self._session_instance:
            self._session_instance = session.Session(self)
        return self._session_instance

    @property
    def _base_service(self):
        if not self._base_service_instance:
            from ansys.dpf.core.core import BaseService

            self._base_service_instance = BaseService(self, timeout=1)
        return self._base_service_instance

    @property
    @abc.abstractmethod
    def os(self):
        """Get the operating system of the server

        Returns
        -------
        os : str
            "nt" or "posix"
        """
        pass

    @property
    def on_docker(self):
        return self._docker_config.use_docker

    @property
    def docker_config(self):
        return self._docker_config

    @docker_config.setter
    def docker_config(self, val):
        self._docker_config = val

    @property
    @abc.abstractmethod
    def config(self):
        pass

    @abc.abstractmethod
    def shutdown(self):
        pass

    def check_version(self, required_version, msg=None):
        """Check if the server version matches with a required version.

        Parameters
        ----------
        required_version : str
            Required version to compare with the server version.
        msg : str, optional
            Message for the raised exception if version requirements do not match.

        Raises
        ------
        dpf_errors : errors
            errors.DpfVersionNotSupported is raised if failure.

        Returns
        -------
        bool
            ``True`` if the server version meets the requirement.
        """
        from ansys.dpf.core.check_version import server_meet_version_and_raise

        return server_meet_version_and_raise(required_version, self, msg)

    def meet_version(self, required_version):
        """Check if the server version matches with a required version.

        Parameters
        ----------
        required_version : str
            Required version to compare with the server version.

        Returns
        -------
        bool
            ``True`` if the server version meets the requirement.
        """
        return server_meet_version(required_version, self)

    @property
    @abc.abstractmethod
    def local_server(self) -> bool:
        pass

    @local_server.setter
    @abc.abstractmethod
    def local_server(self, val):
        pass

    def __str__(self):
        return f"DPF Server: {self.info}"

    @abc.abstractmethod
    def __eq__(self, other_server):
        pass

    def __ne__(self, other_server):
        """Return true, if the servers are not equal"""
        return not self.__eq__(other_server)

    def __del__(self):
        try:
            if hasattr(core, "SERVER") and id(core.SERVER) == id(self):
                core.SERVER = None
        except:
            warnings.warn(traceback.format_exc())

        try:
            if hasattr(core, "_server_instances") and core._server_instances is not None:
                for i, server in enumerate(core._server_instances):
                    if server() == self:
                        core._server_instances.remove(server)
        except:
            warnings.warn(traceback.format_exc())


class CServer(BaseServer, ABC):
    """Abstract class for servers going through the DPFClientAPI"""

    def __init__(self,
                 ansys_path=None,
                 load_operators=True):
        super().__init__()
        self._own_process = False
        self.ansys_path = ansys_path
        self._client_api_path = load_api.load_client_api(ansys_path=ansys_path)

    @property
    def available_api_types(self):
        return "c_api"

    def get_api_for_type(self, capi, grpcapi):
        return capi

    def __del__(self):
        try:
            self._del_session()
            if self._own_process:
                self.shutdown()
            super().__del__()
        except:
            warnings.warn(traceback.format_exc())


class GrpcClient:
    def __init__(self, address=None):
        from ansys.dpf.gate import client_capi
        self._internal_obj = client_capi.ClientCAPI.client_new_full_address(address)
        client_capi.ClientCAPI.init_client_environment(self)

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())


class GrpcServer(CServer):
    """Server using the gRPC communication protocol"""

    def __init__(self,
                 ansys_path=None,
                 ip=LOCALHOST,
                 port=DPF_DEFAULT_PORT,
                 timeout=10,
                 as_global=True,
                 load_operators=True,
                 launch_server=True,
                 docker_config=RUNNING_DOCKER,
                 use_pypim=True,
                 num_connection_tryouts=3,
                 ):
        # Load DPFClientAPI
        from ansys.dpf.core.misc import is_pypim_configured
        super().__init__(ansys_path=ansys_path, load_operators=load_operators)
        # Load Ans.Dpf.GrpcClient
        self._grpc_client_path = load_api.load_grpc_client(ansys_path=ansys_path)
        self._own_process = launch_server
        self._local_server = False

        address = f"{ip}:{port}"

        self._remote_instance = None
        if launch_server:
            if is_pypim_configured() and not ansys_path and not docker_config.use_docker \
                    and use_pypim:
                self._remote_instance = launch_remote_dpf()
                address = self._remote_instance.services["grpc"].uri
                ip = address.split(":")[-2]
                port = int(address.split(":")[-1])

            elif docker_config.use_docker:
                self.docker_config = launch_dpf_on_docker(
                    docker_config=docker_config,
                    ansys_path=ansys_path, ip=ip, port=port, timeout=timeout)
            else:
                launch_dpf(ansys_path, ip, port, timeout=timeout)
                self._local_server = True

        self._client = GrpcClient(address)

        # store port and ip for later reference
        self._address = address
        self._input_ip = ip
        self._input_port = port
        self.live = True
        self._create_shutdown_funcs()
        self._check_first_call(num_connection_tryouts)
        self.set_as_global(as_global=as_global)

    def _check_first_call(self, num_connection_tryouts):
        for i in range(num_connection_tryouts):
            try:
                self.version
                break
            except errors.DPFServerException as e:
                if ("GOAWAY" not in str(e.args) and "unavailable" not in str(e.args)) \
                        or i == (num_connection_tryouts - 1):
                    raise e

    @property
    def version(self):
        from ansys.dpf.gate import data_processing_capi, integral_types
        api = data_processing_capi.DataProcessingCAPI
        major = integral_types.MutableInt32()
        minor = integral_types.MutableInt32()
        api.data_processing_get_server_version_on_client(self.client, major, minor)
        out = str(int(major)) + "." + str(int(minor))
        return out

    @property
    def os(self):
        from ansys.dpf.gate import data_processing_capi
        api = data_processing_capi.DataProcessingCAPI
        return api.data_processing_get_os_on_client(self.client)

    def _create_shutdown_funcs(self):
        from ansys.dpf.gate import data_processing_capi
        api = data_processing_capi.DataProcessingCAPI
        self._preparing_shutdown_func = (api.data_processing_prepare_shutdown, self.client)
        self._shutdown_func = (api.data_processing_release_server, self.client)

    def shutdown(self):
        if self._remote_instance:
            self._remote_instance.delete()
        try:
            self._preparing_shutdown_func[0](self._preparing_shutdown_func[1])
        except Exception as e:
            warnings.warn("couldn't prepare shutdown: " + str(e.args))
        try:
            self._shutdown_func[0](self._shutdown_func[1])
        except Exception as e:
            warnings.warn("couldn't shutdown server: " + str(e.args))
        self._docker_config.remove_docker_image()

    def __eq__(self, other_server):
        """Return true, if ***** are equals"""
        if isinstance(other_server, GrpcServer):
            # """Return true, if the ip and the port are equals"""
            return self.address == other_server.address
        return False

    @property
    def client(self):
        return self._client

    @property
    def address(self):
        """Address of the server.

        Returns
        -------
        address : str
        """
        return self._address

    @property
    def ip(self):
        """IP address of the server.

        Returns
        -------
        ip : str
        """
        try:
            return self.info["server_ip"]
        except:
            return 0

    @property
    def port(self):
        """Port of the server.

        Returns
        -------
        port : int
        """
        try:
            return self.info["server_port"]
        except:
            return 0

    @property
    def external_ip(self):
        """Public IP address of the server.
        Is the same as  :func:`ansys.dpf.core.LegacyGrpcServer.ip` in all cases except
        for servers using a gateway:
        for example, servers running in Docker Images might have an internal
        :func:`ansys.dpf.core.LegacyGrpcServer.ip` different from the public
        :func:`ansys.dpf.core.LegacyGrpcServer.external_ip`, the latter should be used to get
        connected to the server from outside the Docker Image.

        Returns
        -------
        external_ip : str
        """
        return self._input_ip

    @property
    def external_port(self):
        """Public Port of the server.
        Is the same as  :func:`ansys.dpf.core.LegacyGrpcServer.port` in all cases except
        for servers using a gateway:
        for example, servers running in Docker Images might have an internal
        :func:`ansys.dpf.core.LegacyGrpcServer.port` different from the public
        :func:`ansys.dpf.core.LegacyGrpcServer.external_port`, the latter should be used to get
        connected to the server from outside the Docker Image.

        Returns
        -------
        port : int
        """
        return self._input_port

    @property
    def local_server(self):
        return self._local_server

    @local_server.setter
    def local_server(self, val):
        self._local_server = val

    @property
    def config(self):
        return server_factory.AvailableServerConfigs.GrpcServer


class InProcessServer(CServer):
    """Server using the InProcess communication protocol"""

    def __init__(self,
                 ansys_path=None,
                 as_global=True,
                 load_operators=True,
                 timeout=None):
        # Load DPFClientAPI
        super().__init__(ansys_path=ansys_path, load_operators=load_operators)
        # Load DataProcessingCore
        from ansys.dpf.gate.utils import data_processing_core_load_api
        from ansys.dpf.gate import data_processing_capi
        name = "DataProcessingCore"
        path = _get_dll_path(name, ansys_path)
        try:
            data_processing_core_load_api(path, "common")
        except Exception as e:
            if not os.path.isdir(os.path.dirname(path)):
                raise NotADirectoryError(
                    f"DPF directory not found at {os.path.dirname(path)}"
                    f"Unable to locate the following file: {path}")
            raise e
        data_processing_capi.DataProcessingCAPI.data_processing_initialize_with_context(1, None)
        self.set_as_global(as_global=as_global)

    @property
    def version(self):
        from ansys.dpf.gate import data_processing_capi, integral_types
        api = data_processing_capi.DataProcessingCAPI
        major = integral_types.MutableInt32()
        minor = integral_types.MutableInt32()
        api.data_processing_get_server_version(major, minor)
        out = str(int(major)) + "." + str(int(minor))
        return out

    @property
    def os(self):
        # Since it is InProcess, one could return the current os
        return os.name

    def shutdown(self):
        pass

    def __eq__(self, other_server):
        """Return true, if the ip and the port are equals"""
        return isinstance(other_server, InProcessServer)

    @property
    def client(self):
        return None

    @property
    def local_server(self):
        return True

    @local_server.setter
    def local_server(self, val):
        if not val:
            raise NotImplementedError("an in process server can only be local.")

    @property
    def config(self):
        return server_factory.AvailableServerConfigs.InProcessServer


class LegacyGrpcServer(BaseServer):
    """Provides an instance of the DPF server using InProcess gRPC.
    Kept for backward-compatibility with dpf servers <0.5.0.

    Parameters
    -----------
    ansys_path : str
        Path for the DPF executable.
    ip : str
        IP address of the remote or local instance to connect to. The
        default is ``"LOCALHOST"``.
    port : int
        Port to connect to the remote instance on. The default is
        ``"DPF_DEFAULT_PORT"``, which is 50054.
    timeout : float, optional
        Maximum number of seconds for the initialization attempt.
        The default is ``10``. Once the specified number of seconds
        passes, the connection fails.
    as_global : bool, optional
        Global variable that stores the IP address and port for the DPF
        module. All DPF objects created in this Python session will
        use this IP and port. The default is ``True``.
    load_operators : bool, optional
        Whether to automatically load the math operators. The default
        is ``True``.
    launch_server : bool, optional
        Whether to launch the server on Windows.
    docker_config : server_factory.DockerConfig, optional
        To start DPF server as a docker, specify the docker name here.
    use_pypim: bool, optional
        Whether to use PyPIM functionalities by default when a PyPIM environment is detected.
        Defaults to True.
    """

    def __init__(
            self,
            ansys_path=None,
            ip=LOCALHOST,
            port=DPF_DEFAULT_PORT,
            timeout=10,
            as_global=True,
            load_operators=True,
            launch_server=True,
            docker_config=RUNNING_DOCKER,
            use_pypim=True,
    ):
        """Start the DPF server."""
        # Use ansys.grpc.dpf
        from ansys.dpf.core.misc import is_pypim_configured
        super().__init__()

        self._info_instance = None
        self._own_process = launch_server
        self.live = False
        self._local_server = False

        # Load Ans.Dpf.Grpc?
        import grpc

        # check valid ip and port
        check_valid_ip(ip)
        if not isinstance(port, int):
            raise ValueError("Port must be an integer")

        address = f"{ip}:{port}"

        self._remote_instance = None
        if launch_server:
            if is_pypim_configured() and not ansys_path and not docker_config.use_docker \
                    and use_pypim:
                self._remote_instance = launch_remote_dpf()
                address = self._remote_instance.services["grpc"].uri
                ip = address.split(":")[-2]
                port = int(address.split(":")[-1])
            else:

                if docker_config.use_docker:
                    self.docker_config = launch_dpf_on_docker(docker_config=docker_config,
                                                              ansys_path=ansys_path, ip=ip,
                                                              port=port, timeout=timeout)
                else:
                    launch_dpf(ansys_path, ip, port, timeout=timeout)
                    self._local_server = True

        self.channel = grpc.insecure_channel(address)

        # store the address for later reference
        self._address = address
        self._input_ip = ip
        self._input_port = port
        self.live = True
        self.ansys_path = ansys_path
        self._stubs = {}

        self._create_shutdown_funcs()

        check_ansys_grpc_dpf_version(self, timeout)
        self.set_as_global(as_global=as_global)

    def _create_shutdown_funcs(self):
        self._core_api = data_processing_grpcapi.DataProcessingGRPCAPI
        self._core_api.init_data_processing_environment(self)
        self._core_api.bind_delete_server_func(self)

    @property
    def client(self):
        return self

    @property
    def available_api_types(self):
        return list(self._stubs.values())

    def get_api_for_type(self, capi, grpcapi):
        return grpcapi

    def create_stub_if_necessary(self, stub_name, stub_type):
        if not (stub_name in self._stubs.keys()):
            self._stubs[stub_name] = stub_type(self.channel)

    def get_stub(self, stub_name):
        if not (stub_name in self._stubs.keys()):
            return None
        else:
            return self._stubs[stub_name]

    @property
    def ip(self):
        """IP address of the server.

        Returns
        -------
        ip : str
        """
        try:
            return self.info["server_ip"]
        except:
            return ""

    @property
    def port(self):
        """Port of the server.

        Returns
        -------
        port : int
        """
        try:
            return self.info["server_port"]
        except:
            return 0

    @property
    def external_ip(self):
        """Public IP address of the server.
        Is the same as  :func:`ansys.dpf.core.LegacyGrpcServer.ip` in all cases except
        for servers using a gateway:
        for example, servers running in Docker Images might have an internal
        :func:`ansys.dpf.core.LegacyGrpcServer.ip` different from the public
        :func:`ansys.dpf.core.LegacyGrpcServer.external_ip`, the latter should be used to get
        connected to the server from outside the Docker Image.

        Returns
        -------
        external_ip : str
        """
        return self._input_ip

    @property
    def external_port(self):
        """Public Port of the server.
        Is the same as  :func:`ansys.dpf.core.LegacyGrpcServer.port` in all cases except
        for servers using a gateway:
        for example, servers running in Docker Images might have an internal
        :func:`ansys.dpf.core.LegacyGrpcServer.port` different from the public
        :func:`ansys.dpf.core.LegacyGrpcServer.external_port`, the latter should be used to get
        connected to the server from outside the Docker Image.

        Returns
        -------
        port : int
        """
        return self._input_port

    @property
    def version(self):
        """Version of the server.

        Returns
        -------
        version : str
        """
        return self.info["server_version"]

    @property
    def os(self):
        """Get the operating system of the server

        Returns
        -------
        os : str
            "nt" or "posix"
        """
        return self.info["os"]

    @property
    def info(self):
        if not self._info_instance:
            self._info_instance = self._base_service.server_info
        return self._info_instance

    @property
    def local_server(self):
        return self._local_server

    @local_server.setter
    def local_server(self, val):
        self._local_server = val

    def shutdown(self):
        if self._own_process and self.live:
            try:
                self._preparing_shutdown_func[0](self._preparing_shutdown_func[1])
            except Exception as e:
                warnings.warn("couldn't prepare shutdown: " + str(e.args))

            if self._remote_instance:
                self._remote_instance.delete()
            else:
                try:
                    self._shutdown_func[0](self._shutdown_func[1])
                except Exception as e:
                    try:
                        if self.meet_version("4.0"):
                            warnings.warn(
                                f"couldn't properly release server: {str(e.args)}"
                                ".\n Killing process."
                            )
                        p = psutil.Process(self.info["server_process_id"])
                        p.kill()
                        time.sleep(0.01)
                    except:
                        warnings.warn(traceback.format_exc())

            self.live = False
            self._docker_config.remove_docker_image()

    @property
    def config(self):
        return server_factory.AvailableServerConfigs.LegacyGrpcServer

    def __eq__(self, other_server):
        """Return true, if the ip and the port are equals"""
        if isinstance(other_server, LegacyGrpcServer):
            return self.ip == other_server.ip and self.port == other_server.port
        return False

    def __del__(self):
        try:
            self._del_session()
            if self._own_process:
                self.shutdown()
            super().__del__()
        except:
            warnings.warn(traceback.format_exc())


# Python 3.10
# from typing import TypeAlias
# DpfServer: TypeAlias = LegacyGrpcServer
# Python <3.10
DpfServer = LegacyGrpcServer
