"""
Server factory, server configuration and communication protocols
================================================================

Contains the server factory as well as the communication
protocols and server configurations available.
"""

from ansys.dpf.gate.load_api import (
    _get_path_in_install,
    _find_outdated_ansys_version,
)


class CommunicationProtocols:
    """Defines available communication protocols

    Attributes
    ----------
    gRPC = "gRPC"
        Client/Server communication via gRPC.

    InProcess = "InProcess"
        Load DPF's libraries in the Python process, communicates via a CLayer (shared memory).
    """

    gRPC = "gRPC"
    InProcess = "InProcess"


DEFAULT_COMMUNICATION_PROTOCOL = CommunicationProtocols.gRPC
DEFAULT_LEGACY = True


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
    ignore_dpf_server_type : bool, optional
        Default is False. DPF_SERVER_TYPE environment variable will be ignored if
        overwrite is set to False.

    Examples
    --------
    Use constructor parameters to manually create servers.

    >>> from ansys.dpf import core as dpf
    >>> in_process_config = dpf.ServerConfig(
    ...     protocol=None, legacy=False)
    >>> grpc_config = dpf.ServerConfig(
    ...     protocol=dpf.server_factory.CommunicationProtocols.gRPC, legacy=False)
    >>> legacy_grpc_config = dpf.ServerConfig(
    ...     protocol=dpf.server_factory.CommunicationProtocols.gRPC, legacy=True)
    >>> in_process_server = dpf.start_local_server(config=in_process_config, as_global=False)
    >>> grpc_server = dpf.start_local_server(config=grpc_config, as_global=False)
    >>> legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config, as_global=False)

    Use the environment variable to set the default server configuration.

    >>> import os
    >>> os.environ["DPF_SERVER_TYPE"] = "INPROCESS"
    >>> in_process_server_using_variable = dpf.start_local_server()

    """

    def __init__(
        self, protocol=DEFAULT_COMMUNICATION_PROTOCOL, legacy=DEFAULT_LEGACY
    ):
        self.legacy = legacy
        if not protocol:
            self.protocol = CommunicationProtocols.InProcess
        else:
            self.protocol = protocol

    def __str__(self):
        text = f"Server configuration: protocol={self.protocol}"
        if self.legacy:
            text += f" (legacy gRPC)"
        return text

    def __eq__(self, other):
        return self.legacy == other.legacy and self.protocol == other.protocol


def get_default_server_config(server_lower_than_or_equal_to_0_3=False):
    if server_lower_than_or_equal_to_0_3:
        return ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)

    _legacy = DEFAULT_LEGACY
    _protocol = DEFAULT_COMMUNICATION_PROTOCOL
    import os

    DPF_SERVER_TYPE = os.environ.get("DPF_SERVER_TYPE", None)
    if DPF_SERVER_TYPE:
        if DPF_SERVER_TYPE == "INPROCESS":
            _protocol = CommunicationProtocols.InProcess
            _legacy = False
        elif DPF_SERVER_TYPE == "GRPC":
            _protocol = CommunicationProtocols.gRPC
            _legacy = False
        elif DPF_SERVER_TYPE == "LEGACYGRPC":
            _protocol = CommunicationProtocols.gRPC
            _legacy = True
        else:
            raise NotImplementedError(
                f"DPF_SERVER_TYPE environment variable must "
                f"be set to one of the following: INPROCESS, "
                f"GRPC, LEGACYGRPC."
            )
    return ServerConfig(protocol=_protocol, legacy=_legacy)


class AvailableServerConfigs:
    """Defines available server configurations

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
    >>> in_process_server = dpf.start_local_server(config=in_process_config, as_global=False)
    >>> grpc_server = dpf.start_local_server(config=grpc_config, as_global=False)
    >>> legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config, as_global=False)

    """

    LegacyGrpcServer = ServerConfig(CommunicationProtocols.gRPC, legacy=True)
    InProcessServer = ServerConfig(
        CommunicationProtocols.InProcess, legacy=False
    )
    GrpcServer = ServerConfig(CommunicationProtocols.gRPC, legacy=False)


class ServerFactory:
    """Factory for server type choice depending on current configuration."""

    @staticmethod
    def get_server_type_from_config(config=None, ansys_path=None):
        from ansys.dpf.core.server_types import (
            LegacyGrpcServer,
            GrpcServer,
            InProcessServer,
        )
        from ansys.dpf.core import SERVER_CONFIGURATION

        if not config:
            config = SERVER_CONFIGURATION
        # dpf.core.SERVER_CONFIGURATION is required to know what type of connection to set
        if config is None:
            # If no SERVER_CONFIGURATION is yet defined, set one with default values
            is_server_old = _find_outdated_ansys_version(ansys_path)
            SERVER_CONFIGURATION = get_default_server_config(is_server_old)
            config = SERVER_CONFIGURATION
        if config.protocol == CommunicationProtocols.gRPC and config.legacy:
            return LegacyGrpcServer
        elif (
            config.protocol == CommunicationProtocols.gRPC
            and not config.legacy
        ):
            import os
            from ansys.dpf.core._version import __ansys_version__

            ANSYS_INSTALL = ansys_path
            if ANSYS_INSTALL is None:
                ANSYS_INSTALL = os.environ.get(
                    "AWP_ROOT" + str(__ansys_version__), None
                )
            if ANSYS_INSTALL is not None:
                SUB_FOLDERS = os.path.join(
                    ANSYS_INSTALL, _get_path_in_install()
                )
                os.environ["PATH"] += SUB_FOLDERS
            return GrpcServer
        elif (
            config.protocol == CommunicationProtocols.InProcess
            and not config.legacy
        ):
            return InProcessServer
        else:
            raise NotImplementedError("Server config not available.")
