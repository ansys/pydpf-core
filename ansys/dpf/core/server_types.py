import abc
import io
import os
import platform
import subprocess
import time

import grpc
import psutil

import dpf
from dpf.core import session
from dpf.core.server import LOCALHOST, DPF_DEFAULT_PORT, check_valid_ip, launch_dpf, \
    check_ansys_grpc_dpf_version


class BaseServer(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        self._server_id = None
        self._session_instance = None

    @abc.abstractmethod
    def _has_client(self):
        pass

    @property
    @abc.abstractmethod
    def client(self):  # Si gRPC, return le DPFClient
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
    @abc.abstractmethod
    def _base_service(self):
        pass

    @property
    @abc.abstractmethod
    def info(self):
        pass

    @property
    def _session(self):
        if not self._session_instance:
            self._session_instance = session.Session(self)
        return self._session_instance

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
        return hasattr(self, "_server_id") and self._server_id is not None

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

    def __str__(self):
        return f"DPF Server: {self.info}"

    @abc.abstractmethod
    def __eq__(self, other_server):
        pass

    @abc.abstractmethod
    def __ne__(self, other_server):
        pass

    @abc.abstractmethod
    def __del__(self):
        pass


class CServer(BaseServer):
    def __init__(self):
        raise NotImplementedError

    @property
    def version(self):
        raise NotImplementedError

    @property
    def _base_service(self):
        raise NotImplementedError

    @property
    def info(self):
        raise NotImplementedError

    @property
    def os(self):
        raise NotImplementedError

    def shutdown(self):
        raise NotImplementedError

    def __eq__(self, other_server):
        raise NotImplementedError

    def __ne__(self, other_server):
        raise NotImplementedError

    def __del__(self):
        raise NotImplementedError

    @property
    def available_api_types(self):
        raise NotImplementedError


class GrpcCServer(CServer):
    pass


class DirectCServer(CServer):
    pass


class DpfServer(BaseServer):
    """Provides an instance of the DPF server.

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
    docker_name : str, optional
        To start DPF server as a docker, specify the docker name here.
    """
    def __init__(
        self,
        ansys_path="",
        ip=LOCALHOST,
        port=DPF_DEFAULT_PORT,
        timeout=10,
        as_global=True,
        load_operators=True,
        launch_server=True,
        docker_name=None,
    ):
        """Start the DPF server."""

        # check valid ip and port
        check_valid_ip(ip)
        if not isinstance(port, int):
            raise ValueError("Port must be an integer")

        if os.name == "posix" and "ubuntu" in platform.platform().lower():
            raise OSError("DPF does not support Ubuntu")
        elif launch_server:
            self._server_id = launch_dpf(ansys_path, ip, port,
                                         docker_name=docker_name, timeout=timeout)

        self.channel = grpc.insecure_channel("%s:%d" % (ip, port))

        # assign to global channel when requested
        if as_global:
            dpf.core.SERVER = self

        # TODO: add to PIDs ...

        # store port and ip for later reference
        self._input_ip = ip
        self._input_port = port
        self.live = True
        self.ansys_path = ansys_path
        self._own_process = launch_server
        self._base_service_instance = None
        self._session_instance = None
        self._stubs = {}

        check_ansys_grpc_dpf_version(self, timeout)

    def _has_client(self):
        raise NotImplementedError

    @property
    def client(self):  # Si gRPC, return le DPFClient
        raise NotImplementedError

    @property
    def available_api_types(self):
        raise NotImplementedError

    def get_api_for_type(self, c_api, grpc_api):
        raise NotImplementedError

    def create_stub_if_necessary(self, stub_name, stub_type):
        if not (stub_name in self._stubs.keys()):
            self._stubs[stub_name] = stub_type(self.channel)

    def get_stub(self, stub_name):
        if not (stub_name in self._stubs.keys()):
            return None
        else:
            return self._stubs[stub_name]

    @property
    def _base_service(self):
        if not self._base_service_instance:
            from ansys.dpf.core.core import BaseService

            self._base_service_instance = BaseService(self, timeout=1)
        return self._base_service_instance

    @property
    def _session(self):
        if not self._session_instance:
            self._session_instance = session.Session(self)
        return self._session_instance

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

    @property
    def ip(self):
        """IP address of the server.

        Returns
        -------
        ip : str
        """
        try:
            return self._base_service.server_info["server_ip"]
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
            return self._base_service.server_info["server_port"]
        except:
            return 0

    @property
    def version(self):
        """Version of the server.

        Returns
        -------
        version : str
        """
        return self._base_service.server_info["server_version"]

    @property
    def os(self):
        """Get the operating system of the server

        Returns
        -------
        os : str
            "nt" or "posix"
        """
        return self._base_service.server_info["os"]

    def shutdown(self):
        if self._own_process and self.live and self._base_service:
            self._base_service._prepare_shutdown()
            if self.on_docker:
                run_cmd = f"docker stop {self._server_id}"
                process = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                run_cmd = f"docker rm {self._server_id}"
                for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
                    pass
                process = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                try:
                    self._base_service._release_server()
                except:
                    try:
                        p = psutil.Process(self._base_service.server_info["server_process_id"])
                        p.kill()
                        time.sleep(0.01)
                    except:
                        pass

            self.live = False
            try:
                if id(dpf.core.SERVER) == id(self):
                    dpf.core.SERVER = None
            except:
                pass

            try:
                for i, server in enumerate(dpf.core._server_instances):
                    if server() == self:
                        dpf.core._server_instances.remove(server)
            except:
                pass

    def __eq__(self, other_server):
        """Return true, if the ip and the port are equals"""
        if isinstance(other_server, DpfServer):
            return self.ip == other_server.ip and self.port == other_server.port
        return False

    def __ne__(self, other_server):
        """Return true, if the ip or the port are different"""
        return not self.__eq__(other_server)

    def __del__(self):
        try:
            self.shutdown()
        except:
            pass