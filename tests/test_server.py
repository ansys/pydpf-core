import pytest
import subprocess
import psutil
import sys
import os
from ansys import dpf
from ansys.dpf.core import errors, server_types
from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols
from ansys.dpf.core.server import set_server_configuration, _global_server
from ansys.dpf.core.server import start_local_server, connect_to_server
from ansys.dpf.core.server import shutdown_all_session_servers, has_local_server
from ansys.dpf.core.server import get_or_create_server
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0

server_configs = [None,
                  ServerConfig(),
                  ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
                  ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
                  ServerConfig(protocol=CommunicationProtocols.InProcess, legacy=False),
                  ServerConfig(protocol=None, legacy=False),
                  ] \
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0 else \
    [None,
     ServerConfig(),
     ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
     ]

server_configs_names = ["none",
                        "default",
                        "legacy grpc",
                        "grpc",
                        "in process",
                        "None protocol",
                        ] \
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0 else \
    ["none",
     "default",
     "legacy grpc",
     ]


@pytest.mark.parametrize("server_config", server_configs, ids=server_configs_names, scope="class")
class TestServerConfigs:
    @pytest.fixture(scope="class", autouse=True)
    def cleanup(self, request):
        """Cleanup a testing directory once we are finished."""

        def reset_server_config():
            set_server_configuration(ServerConfig())

        request.addfinalizer(reset_server_config)

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
        server = start_local_server(timeout=1)
        assert has_local_server()
        server = None
        shutdown_all_session_servers()

    def test_start_local_server_with_config(self, server_config):
        set_server_configuration(None)
        shutdown_all_session_servers()
        start_local_server(config=server_config)
        assert has_local_server()
        shutdown_all_session_servers()

    def test_connect_to_server(self, server_config):
        set_server_configuration(server_config)
        print(dpf.core.SERVER_CONFIGURATION)
        shutdown_all_session_servers()
        start_local_server(timeout=10.)
        print("has_local_server", has_local_server())
        if hasattr(dpf.core.SERVER, "ip"):
            connect_to_server(ip=dpf.core.SERVER.ip, port=dpf.core.SERVER.port, timeout=10.,
                              as_global=False)
        else:
            connect_to_server(timeout=10., as_global=False)
        assert has_local_server()

    def test_shutdown_all_session_servers(self, server_config):
        set_server_configuration(server_config)
        print(dpf.core.SERVER_CONFIGURATION)
        start_local_server(timeout=1)
        shutdown_all_session_servers()
        assert not has_local_server()


@pytest.mark.parametrize("server_config", server_configs)
class TestServer:
    @pytest.fixture(scope="class", autouse=True)
    def cleanup(self, request):
        """Cleanup a testing directory once we are finished."""

        def reset_server_config():
            set_server_configuration(ServerConfig())

        request.addfinalizer(reset_server_config)

    def test_available_api_types(self, server_config):
        set_server_configuration(server_config)
        server = get_or_create_server(None)
        assert has_local_server()
        types = server.available_api_types

    def test_client(self, server_config):
        set_server_configuration(server_config)
        server = get_or_create_server(None)
        assert has_local_server()
        client = server.client


@pytest.mark.skipif(os.name == 'posix', reason="lin issue: 2 processes can be run with same port")
def test_busy_port(remote_config_server_type):
    my_serv = start_local_server(config=remote_config_server_type)
    busy_port = my_serv.port
    with pytest.raises(errors.InvalidPortError):
        server_types.launch_dpf(ansys_path=dpf.core.misc.get_ansys_path(), port=busy_port)
    server = start_local_server(as_global=False, port=busy_port,
                                config=remote_config_server_type)
    assert server.port != busy_port


def test_shutting_down_when_deleted_legacy():
    num_dpf_exe = 0
    for proc in psutil.process_iter():
        if "Ans.Dpf.Grpc" in proc.name():
            num_dpf_exe += 1
    subprocess.check_call([
        sys.executable, "-c",
        "from ansys.dpf import core as dpf;"
        "from ansys.dpf.core import examples;"
        "dpf.SERVER_CONFIGURATION = dpf.server_factory.AvailableServerConfigs.LegacyGrpcServer;"
        "model = dpf.Model(examples.static_rst);"
    ])

    new_num_dpf_exe = 0
    for proc in psutil.process_iter():
        if "Ans.Dpf.Grpc" in proc.name():
            new_num_dpf_exe += 1
    assert num_dpf_exe == new_num_dpf_exe


@pytest.mark.skipif(not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
                    reason='Not existing in version lower than 4.0')
def test_shutting_down_when_deleted():
    num_dpf_exe = 0
    for proc in psutil.process_iter():
        if "Ans.Dpf.Grpc" in proc.name():
            num_dpf_exe += 1
    subprocess.check_call([
        sys.executable, "-c",
        "from ansys.dpf import core as dpf;"
        "from ansys.dpf.core import examples;"
        "dpf.SERVER_CONFIGURATION = dpf.server_factory.AvailableServerConfigs.GrpcServer;"
        "model = dpf.Model(examples.static_rst);"
    ])
    new_num_dpf_exe = 0
    for proc in psutil.process_iter():
        if "Ans.Dpf.Grpc" in proc.name():
            new_num_dpf_exe += 1
    assert num_dpf_exe == new_num_dpf_exe
