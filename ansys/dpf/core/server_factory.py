"""
Server factory, server configuration and communication protocols
================================================================
Contains the server factory as well as the communication
protocols and server configurations available.
"""
from ansys.dpf.core.server_types import DpfServer, GrpcCServer, DirectCServer


class CommunicationProtocols:
    """Defines available communication protocols
    """
    gRPC = "gRPC"
    direct = "direct"


class ServerConfig:
    """Provides an instance of ServerConfig object to manage the server type used
    """
    def __init__(self, c_server=False, remote_protocol=CommunicationProtocols.gRPC):
        self.c_server = c_server
        if not remote_protocol:
            self.remote_protocol = CommunicationProtocols.direct
        else:
            self.remote_protocol = remote_protocol

    def __str__(self):
        return f"Server configuration: c_server={self.c_server}, " \
               f"remote protocol={self.remote_protocol}"


class ServerFactory:
    """Factory for server type choice depending on current configuration.
    """
    @staticmethod
    def get_server_type_from_config(config=None):
        from ansys.dpf.core import SERVER_CONFIGURATION
        if not config:
            config = SERVER_CONFIGURATION
        # dpf.core.SERVER_CONFIGURATION is required to know what type of connection to set
        if config is None:
            # If no SERVER_CONFIGURATION is yet defined, set one with default values
            SERVER_CONFIGURATION = ServerConfig()
            config = SERVER_CONFIGURATION
        if config.remote_protocol == CommunicationProtocols.gRPC and config.c_server is False:
            return DpfServer
        elif config.remote_protocol == CommunicationProtocols.gRPC and config.c_server:
            import os
            from ansys.dpf.core._version import __ansys_version__
            ISPOSIX = os.name == "posix"
            ANSYS_INSTALL = os.environ.get("AWP_ROOT" + str(__ansys_version__), None)
            SUB_FOLDERS = os.path.join(ANSYS_INSTALL, "aisol", "dll" if ISPOSIX else "bin",
                                       "linx64" if ISPOSIX else "winx64")
            os.environ["PATH"] += SUB_FOLDERS
            return GrpcCServer
        elif config.remote_protocol == CommunicationProtocols.direct and config.c_server:
            return DirectCServer
        else:
            raise NotImplementedError("Server config not available.")
