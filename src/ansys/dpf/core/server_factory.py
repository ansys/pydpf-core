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
Server factory, server configuration and communication protocols.

Contains the server factory as well as the communication
protocols and server configurations available.
"""

import io
import logging
import os
import subprocess
import time

from ansys.dpf.gate.load_api import (
    _find_outdated_ansys_version,
    _get_path_in_install,
)


class CommunicationProtocols:
    """Defines available communication protocols.

    Attributes
    ----------
    gRPC = "gRPC"
        Client/Server communication via gRPC.

    InProcess = "InProcess"
        Load the DPF libraries in the Python process, communicates via a CLayer (shared memory).
    """

    gRPC = "gRPC"
    InProcess = "InProcess"


DEFAULT_COMMUNICATION_PROTOCOL = CommunicationProtocols.InProcess
DEFAULT_LEGACY = False


class DockerConfig:
    """Manage DPF Docker configuration and communication.

    Intermediate class encapsulating all the configuration options needed to run a docker
    image of DPF and holding tools to communicate with Docker.

    Parameters
    ----------
    use_docker : bool, optional
        Whether the DPF server should be started in a Docker Container by default.
    docker_name : str, optional
        Name of Docker Image to run.
    mounted_volumes : dict, optional
        Dictionary of key = local path and value = path of mounted volumes in the Docker Image.
        To prevent from uploading result files on the Docker Image
        :func:`ansys.dpc.core.server_factory.RunningDockerConfig.replace_with_mounted_volumes`
        iterates through this dictionary to replace local path instances by their mapped value.
    extra_args : str, optional
        Extra arguments to add to the docker run command.

    """

    def __init__(
        self,
        use_docker: bool = False,
        docker_name: str = "",
        mounted_volumes: dict = None,
        extra_args: str = "",
    ):
        from ansys.dpf.core import LOCAL_DOWNLOADED_EXAMPLES_PATH

        if mounted_volumes is None:
            mounted_volumes = {LOCAL_DOWNLOADED_EXAMPLES_PATH: "/tmp/downloaded_examples"}

        self._use_docker = use_docker
        self._docker_name = docker_name
        self._mounted_volumes = mounted_volumes
        self._extra_args = extra_args

    @property
    def use_docker(self) -> bool:
        """Whether the DPF server should be started in a Docker Container by default.

        Returns
        -------
        bool
        """
        return self._use_docker

    @use_docker.setter
    def use_docker(self, val: bool):
        self._use_docker = val

    @property
    def docker_name(self) -> str:
        """Name of Docker Image to run.

        Returns
        -------
        str
        """
        return self._docker_name

    @property
    def mounted_volumes(self) -> dict:
        """Dictionary of key = local path and value = path of mounted volumes in the Docker Image.

        To prevent from uploading result files on the Docker Image
        :func:`ansys.dpc.core.server_factory.RunningDockerConfig.replace_with_mounted_volumes`
        iterates through this dictionary to replace local path instances by their mapped value.

        Returns
        -------
        dict
        """
        return self._mounted_volumes

    @mounted_volumes.setter
    def mounted_volumes(self, mounted_volumes: dict):
        self._mounted_volumes = mounted_volumes

    @property
    def licensing_args(self) -> str:
        """Generate licensing-related environment variables for the Docker container.

        Returns
        -------
        str
            String containing Docker environment variable settings for licensing,
            including acceptance of license agreements and licensing file path.
        """
        la = os.environ.get("ANSYS_DPF_ACCEPT_LA", "N")
        lf = os.environ.get("ANSYSLMD_LICENSE_FILE", None)
        additional_option = " -e ANSYS_DPF_ACCEPT_LA=" + la + " "
        if lf is not None:
            additional_option += " -e ANSYSLMD_LICENSE_FILE="
            additional_option += lf
            additional_option += " "
        return additional_option

    @property
    def extra_args(self) -> str:
        """Extra arguments to add to the docker run command.

        Returns
        -------
        str
        """
        return self._extra_args

    def docker_run_cmd_command(self, docker_server_port: int, local_port: int) -> str:
        """Build the Docker run command using DockerConfig attributes and specified ports.

        Creates the docker run command with the ``DockerConfig`` attributes as well
        as the ``docker_server_port`` and ``local_port`` passed in as parameters.

        Parameters
        ----------
        docker_server_port : int
            Port used inside the Docker Container to run the gRPC server.
        local_port : int
            Port exposed outside the Docker container bounded to the internal
            ``docker_server_port``.

        Returns
        -------
        str
        """
        mounted_volumes_args = "-v " + " -v ".join(
            key + ":" + val for key, val in self.mounted_volumes.items()
        )
        licensing_options = self.licensing_args
        return (
            f"docker run -d "
            f" {licensing_options} "
            f"-p {local_port}:{docker_server_port} "
            f"{self.extra_args} "
            f"{mounted_volumes_args} "
            f"-e DOCKER_SERVER_PORT={docker_server_port} "
            f"--expose={docker_server_port} "
            f"{self.docker_name}"
        )

    def __str__(self):
        """Return a string representation of the DockerConfig object.

        Includes information about whether Docker is used, the Docker image name,
        mounted volumes, and any extra arguments.

        Returns
        -------
        str
            Formatted string representation of the DockerConfig instance.
        """
        return (
            "DockerConfig with: \n"
            f"\t- use_docker: {self.use_docker}\n"
            f"\t- docker_name: {self.docker_name}\n"
            f"\t- mounted_volume: {self.mounted_volumes}\n"
            f"\t- extra_args: {self.extra_args}\n"
        )

    @staticmethod
    def find_port_available_for_docker_bind(port: int) -> int:
        """Check available internal docker_server_port from the stdout of running Docker containers.

        Parameters
        ----------
        port: int

        Returns
        -------
        port: int
        """
        run_cmd = "docker ps --all"
        b_shell = False
        if os.name == "posix":
            b_shell = True
        with subprocess.Popen(
            run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=b_shell
        ) as process:
            used_ports = []
            with io.TextIOWrapper(process.stdout, encoding="utf-8") as log_out:
                for line in log_out:
                    if not ("CONTAINER ID" in line):
                        split = line.split("0.0.0.0:")
                        if len(split) > 1:
                            used_ports.append(int(split[1].split("-")[0]))

            while port in used_ports:
                port += 1
        return port


class ServerConfig:
    """Provides an instance of ServerConfig object to manage the server type used.

    The default parameters can be overwritten using the DPF_SERVER_TYPE environment
    variable. DPF_SERVER_TYPE=INPROCESS, DPF_SERVER_TYPE=GRPC,
    DPF_SERVER_TYPE=LEGACYGRPC can be used.

    Parameters
    ----------
    protocol : CommunicationProtocols, optional
        Communication protocol for DPF server (e.g. InProcess, gRPC)
    legacy : bool, optional
        If legacy is set to True, the server will be using ansys-grpc-dpf
        Python module. If not, it will communicate with DPF binaries using ctypes
        and DPF CLayer calls.

    Examples
    --------
    Use constructor parameters to manually create servers.

    >>> from ansys.dpf import core as dpf
    >>> in_process_config = dpf.ServerConfig(
    ...     protocol=dpf.server_factory.CommunicationProtocols.InProcess, legacy=False)
    >>> grpc_config = dpf.ServerConfig(
    ...     protocol=dpf.server_factory.CommunicationProtocols.gRPC, legacy=False)
    >>> legacy_grpc_config = dpf.ServerConfig(
    ...     protocol=dpf.server_factory.CommunicationProtocols.gRPC, legacy=True)
    >>> in_process_server = dpf.start_local_server(config=in_process_config, as_global=False)  # doctest: +SKIP
    >>> grpc_server = dpf.start_local_server(config=grpc_config, as_global=False)  # doctest: +SKIP
    >>> legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config, as_global=False)  # doctest: +SKIP

    Use the environment variable to set the default server configuration.

    >>> import os
    >>> os.environ["DPF_SERVER_TYPE"] = "INPROCESS"
    >>> dpf.start_local_server()  # doctest: +SKIP
    <ansys.dpf.core.server_types.InProcessServer object at ...>

    """

    def __init__(
        self,
        protocol: str = DEFAULT_COMMUNICATION_PROTOCOL,
        legacy: bool = DEFAULT_LEGACY,
    ):
        self.legacy = legacy
        if not protocol:
            self.protocol = CommunicationProtocols.InProcess
        else:
            self.protocol = protocol

    def __str__(self):
        """Return a string representation of the ServerConfig instance.

        This method provides a human-readable string summarizing the server configuration,
        including the protocol and whether it's using legacy gRPC.

        Returns
        -------
        str
            String representation of the ServerConfig instance.
        """
        text = f"Server configuration: protocol={self.protocol}"
        if self.legacy:
            text += f" (legacy gRPC)"
        return text

    def __eq__(self, other: "ServerConfig"):
        """Check if two ServerConfig instances are equal.

        Compares the current ServerConfig instance with another one to check if they have
        the same protocol and legacy status.

        Parameters
        ----------
        other : ServerConfig
            The other ServerConfig instance to compare with.

        Returns
        -------
        bool
            True if the instances have the same protocol and legacy status, False otherwise.
        """
        if isinstance(other, ServerConfig):
            return self.legacy == other.legacy and self.protocol == other.protocol
        return False

    def __ne__(self, other):
        """Check if two ServerConfig instances are not equal.

        Compares the current ServerConfig instance with another one to check if they have
        different protocol or legacy status.

        Parameters
        ----------
        other : ServerConfig
            The other ServerConfig instance to compare with.

        Returns
        -------
        bool
            True if the instances have different protocol or legacy status, False otherwise.
        """
        return not self.__eq__(other)


def get_default_server_config(
    server_lower_than_or_equal_to_0_3: bool = False, docker_config: DockerConfig = None
):
    """Return the default configuration depending on the server version.

        - if ansys.dpf.core.SERVER_CONFIGURATION is not None, then this variable is taken
        - if server_lower_than_or_equal_to_0_3 is True, then LegacyGrpcServer is taken
        - if DPF_SERVER_TYPE environment variable is set to ``INPROCESS``, ``GRPC``, or
          ``LEGACYGRPC``, then this variable is taken
        - else DEFAULT_COMMUNICATION_PROTOCOL and DEFAULT_LEGACY are used.

    Raises
    ------
    If DPF_SERVER_TYPE environment variable is set to unknown value.

    """
    from ansys.dpf.core import SERVER_CONFIGURATION

    if SERVER_CONFIGURATION is not None:
        return SERVER_CONFIGURATION

    if docker_config is None:
        docker_config = DockerConfig()

    config = None

    if server_lower_than_or_equal_to_0_3:
        return ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)

    dpf_server_type = os.environ.get("DPF_SERVER_TYPE", None)
    if dpf_server_type and config is None:
        if dpf_server_type == "INPROCESS":
            config = AvailableServerConfigs.InProcessServer
        elif dpf_server_type == "GRPC":
            config = AvailableServerConfigs.GrpcServer
        elif dpf_server_type == "LEGACYGRPC":
            config = AvailableServerConfigs.LegacyGrpcServer
        else:
            raise NotImplementedError(
                f"DPF_SERVER_TYPE environment variable must "
                f"be set to one of the following: INPROCESS, "
                f"GRPC, LEGACYGRPC."
            )
    elif config is None and docker_config.use_docker:
        config = get_default_remote_server_config()
    elif config is None:
        config = ServerConfig(protocol=DEFAULT_COMMUNICATION_PROTOCOL, legacy=DEFAULT_LEGACY)
    return config


def get_default_remote_server_config():
    """Return the default configuration for gRPC communication.

    Follows get_default_server_config

    Raises
    ------
    If DPF_SERVER_TYPE environment variable is set to unknown value.

    """
    config = get_default_server_config()
    if config == AvailableServerConfigs.InProcessServer:
        return AvailableServerConfigs.GrpcServer


class AvailableServerConfigs:
    """Define available server configurations.

    Attributes
    ----------
    LegacyGrpcServer = ServerConfig(CommunicationProtocols.gRPC, legacy=True)
       Using gRPC communication through the python module ansys.grpc.dpf.

    InProcess = ServerConfig(CommunicationProtocols.InProcess, legacy=False)
        Loading DPF in Process.

    GrpcServer = ServerConfig(CommunicationProtocols.gRPC, legacy=False)
        Using gRPC communication through DPF gRPC CLayer Ans.Dpf.GrpcClient.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> in_process_config = dpf.AvailableServerConfigs.InProcessServer
    >>> grpc_config = dpf.AvailableServerConfigs.GrpcServer
    >>> legacy_grpc_config = dpf.AvailableServerConfigs.LegacyGrpcServer
    >>> in_process_server = dpf.start_local_server(config=in_process_config, as_global=False)  # doctest: +SKIP
    >>> grpc_server = dpf.start_local_server(config=grpc_config, as_global=False)  # doctest: +SKIP
    >>> legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config, as_global=False)  # doctest: +SKIP

    """

    LegacyGrpcServer = ServerConfig(CommunicationProtocols.gRPC, legacy=True)
    InProcessServer = ServerConfig(CommunicationProtocols.InProcess, legacy=False)
    GrpcServer = ServerConfig(CommunicationProtocols.gRPC, legacy=False)


class RunningDockerConfig:
    """Holds all the configuration options and the process information of a running Docker image of a DPF server.

    Parameters
    ----------
    docker_config : DockerConfig, optional
        ``DockerConfig`` used to start the docker.
    server_id : int, optional
        Running Docker Container id.
    docker_server_port : int, optional
        Local port exposed to the docker image.

    """

    def __init__(
        self,
        docker_config: DockerConfig = None,
        server_id: int = None,
        docker_server_port: int = None,
    ):
        if docker_config is None:
            docker_config = DockerConfig()
        self._docker_config = docker_config
        self._server_id = server_id
        self._use_docker = self._docker_config.use_docker
        self._port = docker_server_port

    @property
    def use_docker(self) -> bool:
        """Whether the DPF server should be started in a Docker Container by default.

        Returns
        -------
        bool
        """
        return self._use_docker

    @property
    def docker_server_port(self) -> int:
        """Port used inside the Docker Container to run the gRPC server.

        Returns
        -------
        int
        """
        return self._port

    @docker_server_port.setter
    def docker_server_port(self, val: int):
        self._port = val

    @property
    def server_id(self) -> int:
        """Running Docker Container id.

        Returns
        -------
        int
        """
        return self._server_id

    @server_id.setter
    def server_id(self, val: int):
        self._server_id = val

    @property
    def docker_name(self) -> str:
        """Name of Docker running Image.

        Returns
        -------
        str
        """
        return self._docker_config.docker_name

    @property
    def mounted_volumes(self) -> dict:
        """Dictionary of local path to docker path of volumes mounted in the Docker Image.

        These paths are checked for when result files are looked for by the server to prevent from
        uploading them.

        Returns
        -------
        dict
        """
        return self._docker_config.mounted_volumes

    @property
    def extra_args(self) -> str:
        """Extra arguments used in the ``docker run`` command.

        Returns
        -------
        str
        """
        return self._docker_config.extra_args

    def replace_with_mounted_volumes(self, path: str) -> str:
        """Replace local path found in the list of mounted volumes by their mounted path in the docker.

        Parameters
        ----------
        path: str
            Path to search for occurrences of mounted volumes.

        Returns
        -------
        path: str

        """
        if self.use_docker:
            path = os.path.normpath(path)
            for key, val in self.mounted_volumes.items():
                path = path.replace(os.path.normpath(key), val)
        return path

    def remove_docker_image(self) -> None:
        """Stop and Removes the Docker image with its id==server_id."""
        if not self.use_docker or not self.server_id:
            return
        stop_cmd = f"docker stop {self.server_id}"
        b_shell = False
        if os.name == "posix":
            b_shell = True
        with subprocess.Popen(
            stop_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=b_shell
        ) as process:
            rm_cmd = f"docker rm {self.server_id}"
            with io.TextIOWrapper(process.stdout, encoding="utf-8") as log_out:
                for _ in log_out:
                    pass
            try:
                subprocess.run(
                    rm_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    shell=b_shell,
                    check=True,
                )
            except subprocess.CalledProcessError as e:
                if "No such container" in str(e.output):
                    pass
                else:
                    raise e
            process.kill()

    def listen_to_process(
        self,
        log: logging.Logger,
        cmd_lines: list,
        lines: list,
        timeout: float,
        stdout: bool = True,
    ) -> None:
        """Search inside the Docker Container stdout log to fill in this instance's attributes.

        Parameters
        ----------
        log
            Instance of ``logging`` to add debug info to.
        cmd_lines: list
            Stdout of the shell process run ``docker run`` command.
        lines : list
            Internal Container's stdout are copied into ``lines``.
        timeout : float
            When to stop searching for stdout.
        stdout : bool, optional
            Whether to check stdout or stderr.
        """
        self.server_id = cmd_lines[0].replace("\n", "")
        t_timeout = time.time() + timeout
        while time.time() < t_timeout:
            with subprocess.Popen(
                f"docker logs {self.server_id}",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=(os.name == "posix"),
            ) as docker_process:
                self._use_docker = True
                if stdout:
                    with io.TextIOWrapper(docker_process.stdout, encoding="utf-8") as log_out:
                        for line in log_out:
                            log.debug(line)
                            lines.append(line)
                else:
                    with io.TextIOWrapper(docker_process.stderr, encoding="utf-8") as log_error:
                        for line in log_error:
                            if line not in lines:
                                lines.append(line)
                docker_process.kill()

    def docker_run_cmd_command(self, docker_server_port: int, local_port: int) -> str:
        """Return a docker run command using DockerConfig attributes and specified ports.

        Creates the docker run command with the ``DockerConfig`` attributes as well
        as the ``docker_server_port`` and ``local_port`` passed in as parameters.

        Parameters
        ----------
        docker_server_port : int
            Port used inside the Docker Container to run the gRPC server.
        local_port : int
            Port exposed outside the Docker container bounded to the internal
            ``docker_server_port``.

        Returns
        -------
        str
        """
        return self._docker_config.docker_run_cmd_command(docker_server_port, local_port)

    def __str__(self):
        """Return a string representation of the RunningDockerConfig instance.

        This method provides a human-readable string summarizing the docker configuration, and
        the server id.

        Returns
        -------
        str
            String representation of the RunningDockerConfig instance.
        """
        return str(self._docker_config) + f"\t- server_id: {self.server_id}\n"


def create_default_docker_config() -> DockerConfig:
    """Return a docker configuration instance."""
    return DockerConfig(
        use_docker="DPF_DOCKER" in os.environ.keys(),
        docker_name=os.environ.get("DPF_DOCKER", ""),
    )


class ServerFactory:
    """Factory for server type choice depending on current configuration."""

    @staticmethod
    def get_server_type_from_config(
        config: ServerConfig = None,
        ansys_path: str = None,
        docker_config: DockerConfig = None,
    ):
        """Return server type determined from the server configuration."""
        from ansys.dpf.core.server_types import (
            GrpcServer,
            InProcessServer,
            LegacyGrpcServer,
        )

        # dpf.core.SERVER_CONFIGURATION is required to know what type of connection to set
        if config is None:
            # If no SERVER_CONFIGURATION is yet defined, set one with default values
            is_server_old = False
            if ansys_path is not None:
                if "ansys_dpf_server" not in ansys_path:
                    is_server_old = _find_outdated_ansys_version(ansys_path)
            config = get_default_server_config(is_server_old, docker_config)
        if config.protocol == CommunicationProtocols.gRPC and config.legacy:
            return LegacyGrpcServer
        elif config.protocol == CommunicationProtocols.gRPC and not config.legacy:
            return GrpcServer
        elif config.protocol == CommunicationProtocols.InProcess and not config.legacy:
            return InProcessServer
        else:
            raise NotImplementedError("Server config not available.")

    @staticmethod
    def get_remote_server_type_from_config(config: ServerConfig = None):
        """Return remote server type determined from the server configuration."""
        if config is None:
            config = get_default_remote_server_config()
        return ServerFactory.get_server_type_from_config(config)
