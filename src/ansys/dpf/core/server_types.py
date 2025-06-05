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
Server types.

Contains the different kinds of
servers available for the factory.
"""

from __future__ import annotations

import abc
from abc import ABC
import ctypes
import io
import os
from pathlib import Path
import socket
import subprocess
import sys
from threading import Lock, Thread
import time
import traceback
from typing import TYPE_CHECKING, Union
import warnings

import psutil

import ansys.dpf.core as core
from ansys.dpf.core import __version__, errors, server_context, server_factory
from ansys.dpf.core._version import min_server_version, server_to_ansys_version
from ansys.dpf.core.check_version import get_server_version, meets_version, server_meet_version
from ansys.dpf.core.server_context import AvailableServerContexts, ServerContext
from ansys.dpf.gate import data_processing_grpcapi, load_api

if TYPE_CHECKING:  # pragma: no cover
    from ansys.dpf.core.server_factory import DockerConfig

import logging

LOG = logging.getLogger(__name__)
LOG.setLevel("DEBUG")
DPF_DEFAULT_PORT = int(os.environ.get("DPF_PORT", 50054))
LOCALHOST = os.environ.get("DPF_IP", "127.0.0.1")
RUNNING_DOCKER = server_factory.create_default_docker_config()

MAX_PORT = 65535


def _get_dll_path(name, ansys_path=None):
    """Helper-function to get the right dll path for Linux or Windows."""
    ISPOSIX = os.name == "posix"
    ANSYS_INSTALL = Path(core.misc.get_ansys_path(ansys_path))
    api_path = load_api._get_path_in_install()
    if api_path is None:
        raise ImportError(f"Could not find API path in install.")
    SUB_FOLDERS = ANSYS_INSTALL / api_path
    if ISPOSIX:
        name = "lib" + name
    return SUB_FOLDERS / name


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
    ansys_path = Path(ansys_path)
    if ansys_path.joinpath(path_in_install).is_dir():
        dpf_run_dir = ansys_path / path_in_install
    else:
        dpf_run_dir = ansys_path
    if not dpf_run_dir.is_dir():
        raise NotADirectoryError(
            f'Invalid ansys path at "{ansys_path}".  '
            "Unable to locate the directory containing DPF at "
            f'"{dpf_run_dir}"'
        )
    else:
        if not dpf_run_dir.joinpath(executable).exists():
            raise FileNotFoundError(
                f'DPF executable not found at "{dpf_run_dir}".  '
                f'Unable to locate the executable "{executable}"'
            )
    return dpf_run_dir


def _run_launch_server_process(
    ip,
    port,
    ansys_path=None,
    docker_config=server_factory.RunningDockerConfig(),
    context: ServerContext = None,
):
    bShell = False
    if docker_config.use_docker:
        docker_server_port = int(os.environ.get("DOCKER_SERVER_PORT", port))
        dpf_run_dir = Path.cwd()
        if os.name == "posix":
            bShell = True
        run_cmd = docker_config.docker_run_cmd_command(docker_server_port, port)
    else:
        if os.name == "nt":
            executable = "Ans.Dpf.Grpc.bat"
            run_cmd = f"{executable} --address {ip} --port {port}"
            if context not in (
                None,
                AvailableServerContexts.entry,
                AvailableServerContexts.premium,
            ):
                run_cmd += f" --context {int(context.licensing_context_type)}"
        else:
            executable = "./Ans.Dpf.Grpc.sh"  # pragma: no cover
            run_cmd = [
                executable,
                f"--address {ip}",
                f"--port {port}",
            ]  # pragma: no cover
            if context not in (
                None,
                AvailableServerContexts.entry,
                AvailableServerContexts.premium,
            ):
                run_cmd.append(f"--context {int(context.licensing_context_type)}")
        path_in_install = load_api._get_path_in_install(internal_folder="bin")
        dpf_run_dir = _verify_ansys_path_is_valid(ansys_path, executable, path_in_install)

    old_dir = Path.cwd()
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
    process, port, timeout, lines, current_errors, stderr=None, stdout=None
):
    if not stderr:

        def read_stderr():
            with io.TextIOWrapper(process.stderr, encoding="utf-8") as log_err:
                for line in log_err:
                    LOG.debug(line)
                    current_errors.append(line)

        stderr = read_stderr
        # check to see if the service started
    if not stdout:

        def read_stdout():
            with io.TextIOWrapper(process.stdout, encoding="utf-8") as log_out:
                for line in log_out:
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
        if (
            "Only one usage of each socket address" in errstr
            or "port is already allocated" in errstr
        ):
            raise errors.InvalidPortError(f"Port {port} in use")
        raise RuntimeError(errstr)


def launch_dpf(
    ansys_path, ip=LOCALHOST, port=DPF_DEFAULT_PORT, timeout=10, context: ServerContext = None
):
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
    context : , optional
        Context to apply to DPF server when launching it.
    """
    process = _run_launch_server_process(ip, port, ansys_path, context=context)
    lines = []
    current_errors = []
    _wait_and_check_server_connection(
        process, port, timeout, lines, current_errors, stderr=None, stdout=None
    )
    return process


def launch_dpf_on_docker(
    running_docker_config=server_factory.RunningDockerConfig(),
    ansys_path=None,
    ip=LOCALHOST,
    port=DPF_DEFAULT_PORT,
    timeout=10.0,
):
    """Launch Ansys DPF.

    Parameters
    ----------
    running_docker_config : server_factory.RunningDockerConfig, optional
        To start DPF server as a docker, specify the docker configurations here.
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
    process = _run_launch_server_process(ip, port, ansys_path, running_docker_config)

    # check to see if the service started
    cmd_lines = []
    # Creating lock for threads
    lock = Lock()
    lock.acquire()
    lines = []
    current_errors = []
    running_docker_config.docker_server_port = port

    def read_stdout():
        with io.TextIOWrapper(process.stdout, encoding="utf-8") as log_out:
            for line in log_out:
                LOG.debug(line)
                cmd_lines.append(line)
                lock.release()
            running_docker_config.listen_to_process(LOG, cmd_lines, lines, timeout)

    def read_stderr():
        with io.TextIOWrapper(process.stderr, encoding="utf-8") as log_err:
            for line in log_err:
                LOG.error(line)
                current_errors.append(line)
            while lock.locked():
                pass
            running_docker_config.listen_to_process(LOG, cmd_lines, current_errors, timeout, False)

    _wait_and_check_server_connection(
        process,
        port,
        timeout,
        lines,
        current_errors,
        stderr=read_stderr,
        stdout=read_stdout,
    )


def launch_remote_dpf(version=None):
    """Launch a remote dpf server."""
    try:
        import ansys.platform.instancemanagement as pypim
    except ImportError as e:
        raise ImportError(
            "Launching a remote session of DPF requires the installation"
            + " of ansys-platform-instancemanagement"
        ) from e
    pim = pypim.connect()

    # Possible improvement:
    # When the version is not specified, it would be possible to use
    # pim.list_definition(product_name="dpf") and select a version compatible with the current
    # pydpf version, following the compatibility rules
    instance = pim.create_instance(product_name="dpf", product_version=version)
    instance.wait_for_ready()
    grpc_service = instance.services["grpc"]
    if grpc_service.headers:
        LOG.error(
            "Communicating with DPF in this remote environment requires metadata."
            + "This is not supported, you will likely encounter errors or limitations."
        )
    return instance


def _compare_ansys_grpc_dpf_version(right_grpc_module_version_str: str, grpc_module_version: str):
    if right_grpc_module_version_str:
        import re

        from packaging.version import parse as parse_version

        right_version_first_numbers = re.search(r"\d", right_grpc_module_version_str)
        right_version_numbers = right_grpc_module_version_str[right_version_first_numbers.start() :]
        compare = (
            "=="
            if right_version_first_numbers.start() == 0
            else right_grpc_module_version_str[0 : right_version_first_numbers.start()].strip()
        )
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
    """Check DPF grpc server version."""
    import grpc
    from packaging import version

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
    if version.parse(server.version) < version.parse(min_server_version):
        raise ValueError(
            f"Error connecting to DPF LegacyGrpcServer with version {server.version} "
            f"(ANSYS {server_to_ansys_version[server.version]}): "
            f"ansys-dpf-core {__version__} does not support DPF servers below "
            f"{min_server_version} ({server_to_ansys_version[min_server_version]})."
        )


class GhostServer:
    """Class used to keep in memory the port used by previous servers."""

    ip: str
    _port: int
    close_time: float

    def __init__(self, ip: str, port: int, close_time: float = None):
        """
        Class used to keep in memory the port used by previous servers.

        To be used internally.

        Adds a timeout before reusing ports of shutdown servers.
        """
        self.ip = ip
        self._port = port
        self.closed_time = close_time
        if self.closed_time is None:
            self.closed_time = time.time()

    @property
    def port(self) -> int:
        """Returns the port of shutdown server if the shutdown happened less than 10s ago."""
        if time.time() - self.closed_time > 10:
            return -1
        return self._port

    def __call__(self, *args, **kwargs):
        """Provide for making the instance callable to simply return the instance itself."""
        return self


class BaseServer(abc.ABC):
    """Abstract class for servers."""

    @abc.abstractmethod
    def __init__(self):
        """Define the base class for all server types, including grpc, in-process, and others."""
        # TODO: Use _server_id to compare servers for equality?
        # https://github.com/ansys/pydpf-core/issues/1984, todo was added in this PR
        self._server_id = None
        self._session_instance = None
        self._base_service_instance = None
        self._context = None
        self._info_instance = None
        self._docker_config = server_factory.RunningDockerConfig()
        self._server_meet_version = {}

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
        """Check if server has a connected client."""
        return not (self.client is None)

    @property
    @abc.abstractmethod
    def client(self):
        """Must be implemented by subclasses."""
        pass

    @property
    @abc.abstractmethod
    def version(self):
        """Must be implemented by subclasses."""
        pass

    @property
    @abc.abstractmethod
    def available_api_types(self):
        """Must be implemented by subclasses."""
        pass

    @abc.abstractmethod
    def get_api_for_type(self, capi, grpcapi):
        """Must be implemented by subclasses."""
        pass

    @property
    def info(self):
        """Server information.

        Returns
        -------
        info : dictionary
            Dictionary with server information, including ``"server_ip"``,
            ``"server_port"``, ``"server_process_id"``, ``"server_version"`` , ``"os"``
            and ``"path"`` keys.
        """
        if not self._info_instance:
            self._info_instance = self._base_service.server_info
            self._info_instance["path"] = self.ansys_path
        return self._info_instance

    def _del_session(self):
        if self._session_instance:
            self._session_instance.delete()
        self._session_instance = None

    @property
    def session(self):
        """Plan event callbacks from the server, such as progress bars during workflow execution and logging.

        Returns
        -------
        ansys.dpf.core.session.Session
        """
        if not self._session_instance:
            from ansys.dpf.core import session

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
        """Get the operating system of the server.

        Returns
        -------
        os : str
            "nt" or "posix"
        """
        pass

    @property
    def on_docker(self):
        """Whether the DPF server should be started in a Docker Container by default."""
        return self._docker_config.use_docker

    @property
    def docker_config(self):
        """Return the docker config associated with the server."""
        return self._docker_config

    @docker_config.setter
    def docker_config(self, val):
        self._docker_config = val

    @property
    @abc.abstractmethod
    def config(self):
        """Must be implemented by subclasses."""
        pass

    @abc.abstractmethod
    def shutdown(self):
        """Must be implemented by subclasses."""
        pass

    def release(self):
        """Clear the available Operators and Releases licenses when necessary.

        Notes
        -----
        Available with server's version starting at 6.0 (Ansys 2023R2).
        """
        self._base_service.release_dpf()

    def apply_context(self, context):
        """Define the settings that will be used to load DPF's plugins.

        A DPF xml file can be used to list the plugins and set up variables.

        Parameters
        ----------
        context : ServerContext
            The context allows to choose which capabilities are available server side.

        Notes
        -----
        Available with server's version starting at 6.0 (Ansys 2023R2).
        """
        self._base_service.apply_context(context)
        self._context = context

    @property
    def context(self):
        """Returns the settings used to load DPF's plugins.

        To update the context server side, use
        :func:`ansys.dpf.core.BaseServer.server_types.apply_context`

        Returns
        -------
        ServerContext
        """
        return self._context

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
        if required_version not in self._server_meet_version:
            meet = meets_version(get_server_version(self), required_version)
            self._server_meet_version[required_version] = meet
            return meet
        return self._server_meet_version[required_version]

    @property
    @abc.abstractmethod
    def local_server(self) -> bool:
        """Must be implemented by subclasses."""
        pass

    @local_server.setter
    @abc.abstractmethod
    def local_server(self, val):
        pass

    def __str__(self):
        """Return string representation of the instance."""
        return f"DPF Server: {self.info}"

    @abc.abstractmethod
    def __eq__(self, other_server):
        """Must be implemented by subclasses."""
        pass

    def __ne__(self, other_server):
        """Return true, if the servers are not equal."""
        return not self.__eq__(other_server)

    def __del__(self):
        """
        Clean up resources associated with the instance.

        Raises
        ------
        Warning
            If an exception occurs while attempting to delete resources.
        """
        try:
            if hasattr(core, "SERVER") and id(core.SERVER) == id(self):
                core.SERVER = None
        except:
            warnings.warn(traceback.format_exc())

        try:
            if hasattr(core, "_server_instances") and core._server_instances is not None:
                for i, server in enumerate(core._server_instances):
                    if server() == self:
                        if hasattr(self, "_input_ip") and hasattr(self, "_input_port"):
                            # keeps a ghost instance with the used port and ip to prevent
                            # from reusing the port to soon after shutting down: bug
                            core._server_instances[i] = GhostServer(
                                self._input_ip, self._input_port
                            )
                        else:
                            core._server_instances.remove(server)
        except:
            warnings.warn(traceback.format_exc())


class CServer(BaseServer, ABC):
    """Abstract class for servers going through the DPFClientAPI."""

    def __init__(self, ansys_path=None, load_operators=True):
        super().__init__()
        self._own_process = False
        self.ansys_path = ansys_path
        self._client_api_path = load_api.load_client_api(ansys_path=ansys_path)

    @property
    def available_api_types(self):
        """Return available api type, always c_api."""
        return "c_api"

    def get_api_for_type(self, capi, grpcapi):
        """Return api for type."""
        return capi

    def __del__(self):
        """
        Clean up resources associated with the instance.

        Raises
        ------
        Warning
            If an exception occurs while attempting to delete resources.
        """
        try:
            self._del_session()
            if self._own_process:
                self.shutdown()
            super().__del__()
        except:
            warnings.warn(traceback.format_exc())


class GrpcClient:
    """Client using the gRPC communication protocol."""

    def __init__(self):
        from ansys.dpf.gate import client_capi

        client_capi.ClientCAPI.init_client_environment(self)

    def set_address(self, address, server):
        """Set client address."""
        from ansys.dpf.core import misc, settings

        if misc.RUNTIME_CLIENT_CONFIG is not None:
            self_config = settings.get_runtime_client_config(server=server)
            misc.RUNTIME_CLIENT_CONFIG.copy_config(self_config)
        from ansys.dpf.gate import client_capi

        self._internal_obj = client_capi.ClientCAPI.client_new_full_address(address)

    def __del__(self):
        """
        Clean up resources associated with the instance.

        This method calls the deleter function to release resources. If an exception
        occurs during deletion, a warning is issued.

        Raises
        ------
        Warning
            If an exception occurs while attempting to delete resources.
        """
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())


class GrpcServer(CServer):
    """Server using the gRPC communication protocol."""

    def __init__(
        self,
        ansys_path: Union[str, None] = None,
        ip: str = LOCALHOST,
        port: str = DPF_DEFAULT_PORT,
        timeout: float = 10.0,
        as_global: bool = True,
        load_operators: bool = True,
        launch_server: bool = True,
        docker_config: DockerConfig = RUNNING_DOCKER,
        use_pypim: bool = True,
        context: server_context.ServerContext = server_context.SERVER_CONTEXT,
    ):
        # Load DPFClientAPI
        from ansys.dpf.core.misc import is_pypim_configured

        self.live = False
        super().__init__(ansys_path=ansys_path, load_operators=load_operators)
        # Load Ans.Dpf.GrpcClient
        self._grpc_client_path = load_api.load_grpc_client(ansys_path=ansys_path)

        self._client = GrpcClient()
        self._own_process = launch_server
        self._local_server = False
        self._os = None
        self._version = None

        address = f"{ip}:{port}"

        self._remote_instance = None
        start_time = time.time()
        if launch_server:
            if (
                is_pypim_configured()
                and not ansys_path
                and not docker_config.use_docker
                and use_pypim
            ):
                self._remote_instance = launch_remote_dpf()
                address = self._remote_instance.services["grpc"].uri
                ip = address.split(":")[-2]
                port = int(address.split(":")[-1])

            elif docker_config.use_docker:
                self.docker_config = server_factory.RunningDockerConfig(docker_config)
                launch_dpf_on_docker(
                    running_docker_config=self.docker_config,
                    ansys_path=ansys_path,
                    ip=ip,
                    port=port,
                    timeout=timeout,
                )
            else:
                launch_dpf(ansys_path, ip, port, timeout=timeout, context=context)
                self._local_server = True

        # store port and ip for later reference
        self._client.set_address(address, self)
        self._address = address
        self._input_ip = ip
        self._input_port = port
        self.live = True
        self._create_shutdown_funcs()
        self._check_first_call(timeout=timeout - (time.time() - start_time))  # Pass remaining time
        if context:
            try:
                self._base_service.initialize_with_context(context)
                self._context = context
            except errors.DpfVersionNotSupported:
                pass
        self.set_as_global(as_global=as_global)

    def _check_first_call(self, timeout: float):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                _ = self.version
                break
            except errors.DPFServerException as e:
                if "GOAWAY" in str(e.args) or "unavailable" in str(e.args):
                    time.sleep(0.5)
                else:
                    raise e

    @property
    def version(self):
        """Get the version of the server.

        Returns
        -------
        version : str
            The version of the server in 'major.minor' format.
        """
        if not self._version:
            from ansys.dpf.gate import data_processing_capi, integral_types

            api = data_processing_capi.DataProcessingCAPI
            major = integral_types.MutableInt32()
            minor = integral_types.MutableInt32()
            api.data_processing_get_server_version_on_client(self.client, major, minor)
            self._version = str(int(major)) + "." + str(int(minor))
        return self._version

    @property
    def os(self):
        """Get the operating system on which the server is running."""
        if not self._os:
            from ansys.dpf.gate import data_processing_capi

            api = data_processing_capi.DataProcessingCAPI
            self._os = api.data_processing_get_os_on_client(self.client)
        return self._os

    def _create_shutdown_funcs(self):
        from ansys.dpf.gate import data_processing_capi

        api = data_processing_capi.DataProcessingCAPI
        self._preparing_shutdown_func = (
            api.data_processing_prepare_shutdown,
            self.client,
        )
        self._shutdown_func = (api.data_processing_release_server, self.client)

    def shutdown(self):
        """Shutdown the server instance."""
        if self.live:
            _ = self.info  # initializing the info variable (giving access to ip and port): this can be required if start_local_server is called afterwards
            if self._remote_instance:
                self._remote_instance.delete()
            try:
                if hasattr(self, "_preparing_shutdown_func"):
                    self._preparing_shutdown_func[0](self._preparing_shutdown_func[1])
            except Exception as e:
                warnings.warn("couldn't prepare shutdown: " + str(e.args))
            try:
                if hasattr(self, "_shutdown_func"):
                    self._shutdown_func[0](self._shutdown_func[1])
            except Exception as e:
                warnings.warn("couldn't shutdown server: " + str(e.args))

            self._docker_config.remove_docker_image()
            self.live = False

    def __eq__(self, other_server):
        """Return true, if ***** are equals."""
        if isinstance(other_server, GrpcServer):
            # """Return true, if the ip and the port are equals"""
            return self.address == other_server.address
        return False

    @property
    def client(self):
        """Get the client associated with the server.

        Returns
        -------
        client : GrpcClient
            The GrpcClient instance associated with the server.
        """
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
        return self.info["server_ip"]

    @property
    def port(self):
        """Port of the server.

        Returns
        -------
        port : int
        """
        return self.info["server_port"]

    @property
    def external_ip(self):
        """Public IP address of the server.

        Is the same as  :func:`ansys.dpf.core.GrpcServer.ip` in all cases except
        for servers using a gateway:
        for example, servers running in Docker Images might have an internal
        :func:`ansys.dpf.core.GrpcServer.ip` different from the public
        :func:`ansys.dpf.core.GrpcServer.external_ip`, the latter should be used to get
        connected to the server from outside the Docker Image.

        Returns
        -------
        external_ip : str
        """
        return self._input_ip

    @property
    def external_port(self):
        """Public Port of the server.

        Is the same as  :func:`ansys.dpf.core.GrpcServer.port` in all cases except
        for servers using a gateway:
        for example, servers running in Docker Images might have an internal
        :func:`ansys.dpf.core.GrpcServer.port` different from the public
        :func:`ansys.dpf.core.GrpcServer.external_port`, the latter should be used to get
        connected to the server from outside the Docker Image.

        Returns
        -------
        port : int
        """
        return self._input_port

    @property
    def local_server(self):
        """Get whether the server is running locally.

        Returns
        -------
        local_server : bool
            True if the server is running locally, False otherwise.
        """
        return self._local_server

    @local_server.setter
    def local_server(self, val):
        self._local_server = val

    @property
    def config(self):
        """Get the server configuration for the gRPC server.

        Returns
        -------
        config : AvailableServerConfigs
            The server configuration for the gRPC server from the AvailableServerConfigs.
        """
        return server_factory.AvailableServerConfigs.GrpcServer


class InProcessServer(CServer):
    """Server using the InProcess communication protocol."""

    _version: str = None

    def __init__(
        self,
        ansys_path: Union[str, None] = None,
        as_global: bool = True,
        load_operators: bool = True,
        timeout: None = None,
        context: server_context.AvailableServerContexts = server_context.SERVER_CONTEXT,
    ):
        # Load DPFClientAPI
        super().__init__(ansys_path=ansys_path, load_operators=load_operators)
        # Load DataProcessingCore
        from ansys.dpf.gate.utils import data_processing_core_load_api

        name = "DataProcessingCore"
        path = _get_dll_path(name, ansys_path)
        try:
            data_processing_core_load_api(str(path), "common")
        except Exception as e:
            if not path.parent.is_dir():
                raise NotADirectoryError(
                    f"DPF directory not found at {path.parent}"
                    f"Unable to locate the following file: {path}"
                )
            raise e
        if context:
            try:
                self.apply_context(context)
            except errors.DpfVersionNotSupported:
                self._base_service.initialize_with_context(
                    server_context.AvailableServerContexts.premium
                )
                self._context = server_context.AvailableServerContexts.premium
                pass
        self.set_as_global(as_global=as_global)
        # Update the python os.environment
        if not os.name == "posix":
            # Forced to use ctypes to get the updated PATH due to sys.exec not the Python
            # interpreter when running Python plugin test VS project
            # The better solution would be to not need to update the path
            os.environ["PATH"] = get_system_path()

    @property
    def version(self):
        """Get the version of the InProcess server.

        Returns
        -------
        version : str
            The version of the InProcess server in the format "major.minor".
        """
        if self._version is None:
            from ansys.dpf.gate import data_processing_capi, integral_types

            api = data_processing_capi.DataProcessingCAPI
            major = integral_types.MutableInt32()
            minor = integral_types.MutableInt32()
            api.data_processing_get_server_version(major, minor)
            out = str(int(major)) + "." + str(int(minor))
            self._version = out
        return self._version

    @property
    def os(self):
        """Get the operating system of the InProcess server.

        Returns
        -------
        os : str
            The operating system name. For InProcess servers,
            it typically returns the current OS, e.g., "posix" or "nt".
        """
        # Since it is InProcess, one could return the current os
        return os.name

    def shutdown(self):  # noqa: D102
        pass

    def __eq__(self, other_server):
        """Return true, if the ip and the port are equals."""
        return isinstance(other_server, InProcessServer)

    @property
    def client(self):
        """Get the client for the InProcess server.

        Returns
        -------
        client : None
            InProcess servers do not have a client, so this property returns None.
        """
        return None

    @property
    def local_server(self):
        """Get whether the InProcess server is running locally.

        Returns
        -------
        local_server : bool
            True, as the InProcess server is always local.
        """
        return True

    @local_server.setter
    def local_server(self, val):
        if not val:
            raise NotImplementedError("an in process server can only be local.")

    @property
    def config(self):
        """Get the server configuration for the InProcess server.

        Returns
        -------
        config : AvailableServerConfigs
            The server configuration for the InProcess server from the AvailableServerConfigs.
        """
        return server_factory.AvailableServerConfigs.InProcessServer


def get_system_path() -> str:
    """Return the current PATH environment variable value of the system."""
    if not os.name == "posix":
        ctypes.windll.kernel32.GetEnvironmentVariableA.argtypes = (
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_int,
        )
        ctypes.windll.kernel32.GetEnvironmentVariableA.restype = ctypes.c_int
        name = "PATH"
        b_name = name.encode("utf-8")
        size = 32767
        buffer = ctypes.create_string_buffer(b"", size)
        _ = ctypes.windll.kernel32.GetEnvironmentVariableA(b_name, buffer, size)
        return buffer.value.decode("utf-8")
    else:
        return sys.path


class LegacyGrpcServer(BaseServer):
    """Provides an instance of the DPF server using InProcess gRPC.

    Kept for backward-compatibility with dpf servers <0.5.0.

    Parameters
    ----------
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
        ansys_path: Union[str, None] = None,
        ip: str = LOCALHOST,
        port: str = DPF_DEFAULT_PORT,
        timeout: float = 5.0,
        as_global: bool = True,
        load_operators: bool = True,
        launch_server: bool = True,
        docker_config: DockerConfig = RUNNING_DOCKER,
        use_pypim: bool = True,
        context: server_context.ServerContext = server_context.SERVER_CONTEXT,
    ):
        """Start the DPF server."""
        # Use ansys.grpc.dpf
        from ansys.dpf.core.misc import is_pypim_configured

        self.live = False
        super().__init__()
        self._own_process = launch_server
        self._local_server = False
        self._stubs = {}
        self.channel = None

        # Load Ans.Dpf.Grpc?
        import grpc

        # check valid ip and port
        check_valid_ip(ip)
        if not isinstance(port, int):
            raise ValueError("Port must be an integer")

        address = f"{ip}:{port}"

        self._remote_instance = None
        if launch_server:
            if (
                is_pypim_configured()
                and not ansys_path
                and not docker_config.use_docker
                and use_pypim
            ):
                self._remote_instance = launch_remote_dpf()
                address = self._remote_instance.services["grpc"].uri
                ip = address.split(":")[-2]
                port = int(address.split(":")[-1])
            else:
                if docker_config.use_docker:
                    self.docker_config = server_factory.RunningDockerConfig(docker_config)
                    launch_dpf_on_docker(
                        running_docker_config=self.docker_config,
                        ansys_path=ansys_path,
                        ip=ip,
                        port=port,
                        timeout=timeout,
                    )
                else:
                    launch_dpf(ansys_path, ip, port, timeout=timeout, context=context)
                    self._local_server = True
        from ansys.dpf.core import misc, settings

        if misc.RUNTIME_CLIENT_CONFIG is not None:
            self_config = settings.get_runtime_client_config(server=self)
            misc.RUNTIME_CLIENT_CONFIG.copy_config(self_config)
        self.channel = grpc.insecure_channel(address)

        # store the address for later reference
        self._address = address
        self._input_ip = ip
        self._input_port = port
        self.live = True
        self.ansys_path = ansys_path

        self._create_shutdown_funcs()

        check_ansys_grpc_dpf_version(self, timeout)
        if context:
            try:
                self._base_service.initialize_with_context(context)
                self._context = context
            except errors.DpfVersionNotSupported:
                pass
        self.set_as_global(as_global=as_global)

    def _create_shutdown_funcs(self):
        self._core_api = data_processing_grpcapi.DataProcessingGRPCAPI
        self._core_api.init_data_processing_environment(self)
        self._core_api.bind_delete_server_func(self)

    @property
    def client(self):
        """Get the client instance for the server.

        This property returns the current instance of the server itself as the client,
        providing access to the server's functionalities through the `LegacyGrpcServer` instance.
        """
        return self

    @property
    def available_api_types(self):
        """Get the list of available API types for the server.

        This property returns the list of API types that are available through
        the current server instance, which are stored in the `_stubs` attribute.

        Returns
        -------
        list
            A list of available API types (stub objects) for the server.
        """
        return list(self._stubs.values())

    def get_api_for_type(self, capi, grpcapi):
        """Get the API for the given type."""
        return grpcapi

    def create_stub_if_necessary(self, stub_name, stub_type):
        """Create and store a gRPC stub if it doesn't already exist.

        This method checks if the specified stub (by `stub_name`) exists. If not, it creates
        the stub using the given `stub_type` and stores it in the `_stubs` dictionary.
        """
        if self.channel and not stub_name in self._stubs:
            self._stubs[stub_name] = stub_type(self.channel)

    def get_stub(self, stub_name):
        """Retrieve the gRPC stub for the given name.

        This method checks if the stub corresponding to `stub_name` exists in the `_stubs`
        dictionary and returns it. If the stub does not exist, it returns `None`.
        """
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
        return self.info["server_ip"]

    @property
    def port(self):
        """Port of the server.

        Returns
        -------
        port : int
        """
        return self.info["server_port"]

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
        """Get the operating system of the server.

        Returns
        -------
        os : str
            "nt" or "posix"
        """
        return self.info["os"]

    @property
    def info(self):
        """Return information about the server instance."""
        if not self._info_instance:
            self._info_instance = self._base_service.server_info
        return self._info_instance

    @property
    def local_server(self):
        """Get whether the server is running locally.

        Returns
        -------
        local_server : bool
            True if the server is running locally, False otherwise.
        """
        return self._local_server

    @local_server.setter
    def local_server(self, val):
        self._local_server = val

    def shutdown(self):
        """Shutdown server instance."""
        if self._own_process and self.live:
            _ = self.info  # initializing the info variable (giving access to ip and port): this can be required if start_local_server is called afterwards
            if self._remote_instance:
                self._remote_instance.delete()
            try:
                if hasattr(self, "_preparing_shutdown_func"):
                    self._preparing_shutdown_func[0](self._preparing_shutdown_func[1])
            except Exception as e:
                warnings.warn("couldn't prepare shutdown: " + str(e.args))

            else:
                try:
                    if hasattr(self, "_shutdown_func"):
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
        """Get the server configuration for the LegacyGrpcServer server.

        Returns
        -------
        config : AvailableServerConfigs
            The server configuration for the LegacyGrpcServer server from the AvailableServerConfigs.
        """
        return server_factory.AvailableServerConfigs.LegacyGrpcServer

    def __eq__(self, other_server):
        """Return true, if the ip and the port are equals."""
        if isinstance(other_server, LegacyGrpcServer):
            return self.ip == other_server.ip and self.port == other_server.port
        return False

    def __del__(self):
        """
        Clean up resources associated with the instance.

        Raises
        ------
        Warning
            If an exception occurs while attempting to delete resources.
        """
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

AnyServerType = Union[LegacyGrpcServer, InProcessServer, GrpcServer]
