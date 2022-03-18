import ansys.grpc.dpf
import pytest

from ansys import dpf
from ansys.dpf.core import path_utilities
from ansys.dpf.core.check_version import meets_version, get_server_version
from ansys.dpf.core.server import RemoteProtocols, ServerConfig
from ansys.dpf.core.server import set_server_configuration, _global_server
from ansys.dpf.core.server import start_local_server, connect_to_server
from ansys.dpf.core.server import shutdown_all_session_servers, has_local_server
from conftest import running_docker


server_configs = [None,
                  ServerConfig(),
                  ServerConfig(c_server=True),
                  ServerConfig(remote_protocol=None),
                  ServerConfig(c_server=True, remote_protocol=None)]


@pytest.mark.parametrize("server_config", server_configs)
class TestServerConfigs:
    def test__global_server(self, server_config):
        set_server_configuration(server_config)
        print(dpf.core.SERVER_CONFIGURATION)
        shutdown_all_session_servers()
        _global_server()
        assert has_local_server()

    def test_set_server_configuration(self, server_config):
        set_server_configuration(server_config)
        assert dpf.core.SERVER_CONFIGURATION == server_config

    def test_start_local_server(self, server_config):
        set_server_configuration(server_config)
        print(dpf.core.SERVER_CONFIGURATION)
        shutdown_all_session_servers()
        start_local_server(timeout=1)
        assert has_local_server()

    def test_connect_to_server(self, server_config):
        set_server_configuration(server_config)
        print(dpf.core.SERVER_CONFIGURATION)
        shutdown_all_session_servers()
        start_local_server(timeout=10.)
        print("has_local_server", has_local_server())
        connect_to_server(timeout=10., as_global=False)
        assert has_local_server()

    def test_shutdown_all_session_servers(self, server_config):
        set_server_configuration(server_config)
        print(dpf.core.SERVER_CONFIGURATION)
        start_local_server(timeout=1)
        shutdown_all_session_servers()
        assert not has_local_server()
