# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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

import time

import pytest
import subprocess
import platform
import psutil
import sys
import os
import packaging.version

from ansys import dpf
from ansys.dpf.core import errors, server_types
from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols
from ansys.dpf.core.server import set_server_configuration, _global_server
from ansys.dpf.core.server import start_local_server, connect_to_server
from ansys.dpf.core.server import shutdown_all_session_servers, has_local_server
from ansys.dpf.core.server import get_or_create_server
from ansys.dpf.core import server
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    running_docker,
    remove_none_available_config,
)

server_configs, server_configs_names = remove_none_available_config(
    [
        None,
        ServerConfig(),
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
        ServerConfig(protocol=CommunicationProtocols.InProcess, legacy=False),
        ServerConfig(protocol=None, legacy=False),
    ]
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0
    else [
        None,
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
    ],
    [
        "none",
        "default",
        "legacy grpc",
        "grpc",
        "in process",
        "None protocol",
    ]
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0
    else [
        "none",
        "legacy grpc",
    ],
)


@pytest.fixture(autouse=False, scope="function")
def clean_up(request):
    """Count servers once we are finished."""

    def shutdown():
        dpf.core.server.shutdown_all_session_servers()

    request.addfinalizer(shutdown)


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
        # print(dpf.core.SERVER_CONFIGURATION)
        shutdown_all_session_servers()
        _global_server()
        assert has_local_server()

    def test_set_server_configuration(self, server_config):
        set_server_configuration(server_config)
        assert dpf.core.SERVER_CONFIGURATION == server_config

    def test_start_local_server(self, server_config):
        set_server_configuration(server_config)
        # print(dpf.core.SERVER_CONFIGURATION)
        start_local_server(timeout=20)
        assert has_local_server()
        shutdown_all_session_servers()

    def test_server_env_path_cleanup(self, server_config):
        """Test that running and stopping servers does not pollute the system PATH."""
        from ansys.dpf.core.server_types import get_system_path

        path_len_init = len(get_system_path())
        _ = dpf.core.start_local_server(config=server_config)
        assert len(get_system_path()) == path_len_init

    def test_start_local_server_with_config(self, server_config):
        set_server_configuration(None)
        shutdown_all_session_servers()
        start_local_server(config=server_config)
        assert has_local_server()
        shutdown_all_session_servers()

    def test_shutdown_all_session_servers(self, server_config):
        set_server_configuration(server_config)
        # print(dpf.core.SERVER_CONFIGURATION)
        start_local_server(timeout=10.0)
        shutdown_all_session_servers()
        assert not has_local_server()

    def test_start_shutdown_start(self, server_config):
        set_server_configuration(server_config)
        # print(dpf.core.SERVER_CONFIGURATION)
        server = start_local_server(timeout=20)
        server.shutdown()
        server = start_local_server(timeout=20)
        assert has_local_server()
        shutdown_all_session_servers()


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


@pytest.mark.skipif(
    os.name == "posix" or running_docker,
    reason="lin issue: 2 processes can be run with same port",
)
def test_busy_port(remote_config_server_type):
    my_serv = start_local_server(config=remote_config_server_type)
    busy_port = my_serv.port
    with pytest.raises(errors.InvalidPortError):
        server_types.launch_dpf(ansys_path=dpf.core.misc.get_ansys_path(), port=busy_port)
    server = start_local_server(as_global=False, port=busy_port, config=remote_config_server_type)
    assert server.port != busy_port


@pytest.mark.skipif(not running_docker, reason="Only works on Docker")
def test_docker_busy_port(remote_config_server_type, clean_up):
    my_serv = start_local_server(config=remote_config_server_type)
    busy_port = my_serv.external_port
    with pytest.raises(errors.InvalidPortError):
        running_docker_config = dpf.core.server_factory.RunningDockerConfig(
            docker_config=dpf.core.server.RUNNING_DOCKER
        )
        server_types.launch_dpf_on_docker(
            port=busy_port, running_docker_config=running_docker_config
        )
    server = start_local_server(as_global=False, port=busy_port, config=remote_config_server_type)
    assert server.external_port != busy_port


@pytest.mark.skipif(
    platform.system() == "Linux" and platform.python_version().startswith("3.7"),
    reason="Known failure in the GitHub pipeline for 3.7 on Ubuntu",
)
@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Not working for server version lower than 4.0",
)
def test_shutting_down_when_deleted_legacy():
    num_dpf_exe = 0
    for proc in psutil.process_iter():
        if "Ans.Dpf.Grpc" in proc.name():
            num_dpf_exe += 1
    subprocess.check_call(
        [
            sys.executable,
            "-c",
            "from ansys.dpf import core as dpf;"
            "from ansys.dpf.core import examples;"
            "dpf.SERVER_CONFIGURATION = dpf.server_factory.AvailableServerConfigs.LegacyGrpcServer;"
            "model = dpf.Model(examples.find_static_rst());",
        ]
    )
    time.sleep(2.0)
    new_num_dpf_exe = 0
    for proc in psutil.process_iter():
        if "Ans.Dpf.Grpc" in proc.name():
            new_num_dpf_exe += 1
    assert num_dpf_exe >= new_num_dpf_exe


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Not existing in version lower than 4.0",
)
def test_shutting_down_when_deleted():
    num_dpf_exe = 0
    for proc in psutil.process_iter():
        if "Ans.Dpf.Grpc" in proc.name():
            num_dpf_exe += 1
    subprocess.check_call(
        [
            sys.executable,
            "-c",
            "from ansys.dpf import core as dpf;"
            "from ansys.dpf.core import examples;"
            "dpf.SERVER_CONFIGURATION = dpf.server_factory.AvailableServerConfigs.GrpcServer;"
            "model = dpf.Model(examples.find_static_rst());",
        ]
    )
    time.sleep(2.0)
    new_num_dpf_exe = 0
    for proc in psutil.process_iter():
        if "Ans.Dpf.Grpc" in proc.name():
            new_num_dpf_exe += 1
    assert num_dpf_exe >= new_num_dpf_exe


def test_eq_server_config():
    assert (
        dpf.core.AvailableServerConfigs.InProcessServer
        == dpf.core.AvailableServerConfigs.InProcessServer
    )
    assert dpf.core.AvailableServerConfigs.GrpcServer == dpf.core.AvailableServerConfigs.GrpcServer
    assert (
        dpf.core.AvailableServerConfigs.LegacyGrpcServer
        == dpf.core.AvailableServerConfigs.LegacyGrpcServer
    )
    assert (
        not dpf.core.AvailableServerConfigs.LegacyGrpcServer
        == dpf.core.AvailableServerConfigs.InProcessServer
    )
    assert dpf.core.AvailableServerConfigs.LegacyGrpcServer == dpf.core.ServerConfig(
        protocol=dpf.core.server_factory.CommunicationProtocols.gRPC, legacy=True
    )
    assert dpf.core.AvailableServerConfigs.GrpcServer == dpf.core.ServerConfig(
        protocol=dpf.core.server_factory.CommunicationProtocols.gRPC, legacy=False
    )
    assert dpf.core.AvailableServerConfigs.InProcessServer == dpf.core.ServerConfig(
        protocol=None, legacy=False
    )
    assert not dpf.core.AvailableServerConfigs.InProcessServer == dpf.core.ServerConfig(
        protocol=dpf.core.server_factory.CommunicationProtocols.gRPC, legacy=False
    )
    assert not dpf.core.AvailableServerConfigs.InProcessServer is None


def test_connect_to_remote_server(remote_config_server_type):
    server_type_remote_process = start_local_server(
        config=remote_config_server_type, as_global=False
    )
    server = connect_to_server(
        ip=server_type_remote_process.external_ip,
        port=server_type_remote_process.external_port,
        timeout=10.0,
        as_global=False,
        config=remote_config_server_type,
    )
    assert server.external_ip == server_type_remote_process.external_ip
    assert server.external_port == server_type_remote_process.external_port
    assert server.config == remote_config_server_type


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Not existing in version lower than 4.0",
)
def test_go_away_server():
    for _ in range(0, 5):
        s = start_local_server(config=dpf.core.AvailableServerConfigs.GrpcServer, as_global=False)
        field = dpf.core.Field(server=s)
        assert field._internal_obj is not None


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Not existing in version lower than 4.0",
)
@pytest.mark.skipif(running_docker, reason="Unstable on Docker")
def test_start_after_shutting_down_server():
    remote_server = start_local_server(
        config=dpf.core.AvailableServerConfigs.GrpcServer, as_global=False
    )
    remote_server.shutdown()

    time.sleep(2.0)

    remote_server = start_local_server(
        config=dpf.core.AvailableServerConfigs.GrpcServer, as_global=False
    )
    info = remote_server.info
    remote_server.shutdown()
    assert info is not None


def test_check_ansys_grpc_dpf_version_raise():
    remote_server = start_local_server(
        config=dpf.core.AvailableServerConfigs.LegacyGrpcServer, as_global=False
    )

    class MockServer:
        def __init__(self, server):
            for attribute in ["channel", "_input_ip", "_input_port"]:
                setattr(self, attribute, getattr(server, attribute))

        @property
        def version(self):
            return "1.0"

    print(MockServer(remote_server).version)
    with pytest.raises(
        ValueError, match="Error connecting to DPF LegacyGrpcServer with version 1.0"
    ):
        dpf.core.server_types.check_ansys_grpc_dpf_version(MockServer(remote_server), timeout=2.0)


@pytest.mark.skipif(
    running_docker,
    reason="can only work with local DPF server install",
)
def test_available_servers():
    out = server.available_servers()
    assert len(out) > 0
    for version in out:
        vout = str(version).replace(".", "_")
        if packaging.version.parse(version) > packaging.version.parse("2022.1"):
            meth = "start_" + vout + "_server"
            assert hasattr(server, meth)
            start = getattr(server, meth)
            srv = start()
            assert srv.local_server
            srv = out[version]()
            assert srv.local_server
