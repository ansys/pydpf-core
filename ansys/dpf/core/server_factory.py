from ansys.dpf.core.server_types import DpfServer, GrpcCServer, DirectCServer


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
        from ansys.dpf.core import SERVER_CONFIGURATION
        config = SERVER_CONFIGURATION
        # dpf.core.SERVER_CONFIGURATION is required to know what type of connection to set
        if config is None:
            # If no SERVER_CONFIGURATION is yet defined, set one with default values
            SERVER_CONFIGURATION = ServerConfig()
            config = SERVER_CONFIGURATION
        if config.remote_protocol == CommunicationProtocols.gRPC and config.c_server is False:
            return DpfServer
        elif config.remote_protocol == CommunicationProtocols.gRPC and config.c_server:
            return GrpcCServer
        elif config.remote_protocol == CommunicationProtocols.direct and config.c_server:
            return DirectCServer
        else:
            raise NotImplementedError("Server config not available.")