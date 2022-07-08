"""
Server factory, server configuration and communication protocols
================================================================
Contains the server factory as well as the communication
protocols and server configurations available.
"""


class CommunicationProtocols:
    """Defines available communication protocols
    """
    gRPC = "gRPC"
    InProcess = "InProcess"


class ServerConfig:
    """Provides an instance of ServerConfig object to manage the server type used
    """
    def __init__(self, protocol=CommunicationProtocols.gRPC, legacy=True):
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


class AvailableServerConfigs:
    """Defines available server configurations
    """
    LegacyGrpcServer = ServerConfig(CommunicationProtocols.gRPC, legacy=True)
    InProcessServer = ServerConfig(CommunicationProtocols.InProcess, legacy=False)
    GrpcServer = ServerConfig(CommunicationProtocols.gRPC, legacy=False)


class ServerFactory:
    """Factory for server type choice depending on current configuration.
    """
    @staticmethod
    def get_server_type_from_config(config=None, ansys_path=None):
        from ansys.dpf.core.server_types import LegacyGrpcServer, GrpcServer, InProcessServer
        from ansys.dpf.core import SERVER_CONFIGURATION
        if not config:
            config = SERVER_CONFIGURATION
        # dpf.core.SERVER_CONFIGURATION is required to know what type of connection to set
        if config is None:
            # If no SERVER_CONFIGURATION is yet defined, set one with default values
            SERVER_CONFIGURATION = ServerConfig()
            config = SERVER_CONFIGURATION
        if config.protocol == CommunicationProtocols.gRPC and config.legacy:
            return LegacyGrpcServer
        elif config.protocol == CommunicationProtocols.gRPC and not config.legacy:
            import os
            from ansys.dpf.core._version import __ansys_version__
            ISPOSIX = os.name == "posix"           
            ANSYS_INSTALL = ansys_path
            if ANSYS_INSTALL is None:
                ANSYS_INSTALL = os.environ.get("AWP_ROOT" + str(__ansys_version__), None)
            if ANSYS_INSTALL is not None:
                SUB_FOLDERS = os.path.join(ANSYS_INSTALL, "aisol", "dll" if ISPOSIX else "bin",
                                           "linx64" if ISPOSIX else "winx64")
                os.environ["PATH"] += SUB_FOLDERS
            return GrpcServer
        elif config.protocol == CommunicationProtocols.InProcess and not config.legacy:
            return InProcessServer
        else:
            raise NotImplementedError("Server config not available.")
