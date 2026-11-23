# Copyright (C) 2020 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

import gc
import os
import platform
import subprocess
import sys
import time
from unittest.mock import Mock
import warnings

import grpc
import packaging.version
import psutil
import pytest

from ansys import dpf
from ansys.dpf.core import errors, examples, server, server_types
from ansys.dpf.core.server import (
    _global_server,
    connect_to_server,
    get_or_create_server,
    has_local_server,
    set_server_configuration,
    shutdown_all_session_servers,
    start_local_server,
)
from ansys.dpf.core.server_factory import CommunicationProtocols, GrpcMode, ServerConfig
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_10_0,
    raises_for_servers_version_under,
    remove_none_available_config,
    running_docker,
)

server_configs, server_configs_names = remove_none_available_config(
    [
        None,
        ServerConfig(),
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
        ServerConfig(protocol=CommunicationProtocols.InProcess, legacy=False),
        ServerConfig(protocol=None, legacy=False),
    ],
    [
        "none",
        "default",
        "legacy grpc",
        "grpc",
        "in process",
        "None protocol",
    ],
)


@pytest.mark.parametrize("server_type", [server_types.GrpcServer, server_types.LegacyGrpcServer])
def test_server_destructor_when_sys_is_cleared(monkeypatch, server_type):
    server_object = object.__new__(server_type)
    monkeypatch.setattr(server_types, "sys", None)

    server_type.__del__(server_object)


def test_in_process_server_shutdown_releases_metadata_streams():
    server_object = object.__new__(server_types.InProcessServer)
    server_object._session_instance = None
    server_object._own_process = False
    metadata = Mock()
    server_object._metadata_instances = [metadata]

    server_object.shutdown()

    metadata.release_streams.assert_called_once_with()


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

    @raises_for_servers_version_under("7.0")
    def test_server_plugins(self, server_config):
        server_plugins = start_local_server(config=server_config).plugins
        assert isinstance(server_plugins, dict)
        assert "native" in server_plugins.keys()


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_10_0, reason="not working properly before 25R2"
)
@pytest.mark.skipif(running_docker, reason="server start using custom xml not working on Docker")
def test_server_context_custom_xml(remote_config_server_type, testfiles_dir):
    from pathlib import Path

    context = dpf.core.AvailableServerContexts.no_context
    context.xml_path = Path(testfiles_dir) / "DpfCustomDefinedTest.xml"
    server_plugins = start_local_server(config=remote_config_server_type, context=context).plugins
    ref = ["grpc", "native"]
    assert sorted(list(server_plugins.keys())) == ref


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_10_0, reason="not working properly before 25R2"
)
@pytest.mark.skipif(running_docker, reason="server start using custom xml not working on Docker")
def test_server_context_custom_xml_check_operators(remote_config_server_type):
    from pathlib import Path

    context = dpf.core.AvailableServerContexts.no_context
    context.xml_path = Path(dpf.core.misc.get_ansys_path()) / "dpf" / "utilities" / "DpfEmpty.xml"
    server = start_local_server(config=remote_config_server_type, context=context, as_global=False)
    assert len(server.plugins) == 1


@pytest.mark.skipif(
    os.name == "posix" or running_docker,
    reason="lin issue: 2 processes can be run with same port",
)
def test_busy_port(remote_config_server_type):
    my_serv = start_local_server(config=remote_config_server_type)
    busy_port = my_serv.port
    with pytest.raises(errors.InvalidPortError):
        grpc_mode = (
            GrpcMode.Insecure
            if os.environ.get("DPF_DEFAULT_GRPC_MODE", "") == "insecure"
            else GrpcMode.mTLS
        )
        server_types.launch_dpf(
            ansys_path=dpf.core.misc.get_ansys_path(), port=busy_port, grpc_mode=grpc_mode
        )
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
def test_shutting_down_when_explicitly_shutdown_legacy():
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
            "model = dpf.Model(examples.find_static_rst());"
            "dpf.SERVER.shutdown();",
        ]
    )
    time.sleep(2.0)
    new_num_dpf_exe = 0
    for proc in psutil.process_iter():
        if "Ans.Dpf.Grpc" in proc.name():
            new_num_dpf_exe += 1
    assert num_dpf_exe >= new_num_dpf_exe


def test_shutting_down_when_explicitly_shutdown():
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
            "model = dpf.Model(examples.find_static_rst());"
            "dpf.SERVER.shutdown();",
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
    # assert server.config == remote_config_server_type


def test_go_away_server():
    for _ in range(0, 5):
        s = start_local_server(config=dpf.core.AvailableServerConfigs.GrpcServer, as_global=False)
        field = dpf.core.Field(server=s)
        assert field._internal_obj is not None


@pytest.mark.skipif(running_docker, reason="Unstable on Docker")
def test_start_after_shutting_down_server():
    remote_server = start_local_server(
        config=dpf.core.AvailableServerConfigs.GrpcServer, as_global=False
    )
    remote_server.shutdown()
    del remote_server
    gc.collect()

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


STOP_TIMEOUT = 30.0


def _is_running(pid: int) -> bool:
    try:
        return psutil.Process(pid).status() != psutil.STATUS_ZOMBIE
    except psutil.NoSuchProcess:
        return False


def _wait_stopped(pid: int, timeout: float = STOP_TIMEOUT) -> bool:
    try:
        psutil.Process(pid).wait(timeout=timeout)
    except psutil.NoSuchProcess:
        pass
    except psutil.TimeoutExpired:
        return False
    return True


def _build_cross_server_workflow():
    config = dpf.core.AvailableServerConfigs.GrpcServer
    server1 = start_local_server(as_global=False, config=config)
    server2 = start_local_server(as_global=False, config=config)
    pids = (server1.info["server_process_id"], server2.info["server_process_id"])

    ds = dpf.core.DataSources(examples.find_static_rst(server=server1), server=server1)
    disp_op = dpf.core.operators.result.displacement(server=server1)
    disp_op.inputs.data_sources.connect(ds)

    norm_op = dpf.core.operators.math.norm_fc(server=server2)
    norm_op.inputs.connect(disp_op.outputs)
    return server1, server2, pids, ds, disp_op, norm_op


@pytest.fixture
def cleanup_pids():
    pids = []
    yield pids
    for pid in pids:
        if _is_running(pid):
            psutil.Process(pid).kill()


# On Docker, server PIDs are container-local and servers in separate containers cannot reach each other.
requires_local_servers = pytest.mark.skipif(
    running_docker, reason="Requires servers running on the local host."
)


@requires_local_servers
@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0,
    reason="Before 8.0, a server used by another server stays alive after shutdown().",
)
def test_owner_shutdown_stops_server_used_by_another_server(cleanup_pids):
    """An explicit ``shutdown()`` by the owner always stops the server."""
    server1, server2, (pid1, pid2), ds, disp_op, norm_op = _build_cross_server_workflow()
    cleanup_pids.extend([pid1, pid2])

    server1.shutdown()
    assert _wait_stopped(pid1), "server1 still running after shutdown()"
    assert _is_running(pid2)

    with pytest.raises(errors.DPFServerException):
        norm_op.get_output(0, dpf.core.types.fields_container)

    server2.shutdown()
    assert _wait_stopped(pid2), "server2 still running after shutdown()"


@requires_local_servers
def test_cross_server_workflow_survives_dereference(cleanup_pids):
    """Dropping the Python references keeps a server alive while DPF objects still use it."""
    server1, server2, (pid1, pid2), ds, disp_op, norm_op = _build_cross_server_workflow()
    cleanup_pids.extend([pid1, pid2])

    del server1
    gc.collect()
    assert not _wait_stopped(pid1, timeout=2.0), "server1 stopped while still used by server2"
    assert _is_running(pid2)

    fc = norm_op.get_output(0, dpf.core.types.fields_container)
    assert fc[0].max().data_as_list[0] > 0.0

    del server2, ds, disp_op, norm_op, fc
    # operators are in reference cycles (op -> op._outputs -> op)
    gc.collect()
    assert _wait_stopped(pid2), "server2 still running after dereference"
    assert _wait_stopped(pid1), "server1 still running after dereference"


@requires_local_servers
@pytest.mark.parametrize(
    "config",
    [
        dpf.core.AvailableServerConfigs.GrpcServer,
        dpf.core.AvailableServerConfigs.LegacyGrpcServer,
    ],
    ids=["gRPC CLayer", "ansys-grpc-dpf"],
)
def test_shutdown_from_non_owner_is_ignored_with_warning(cleanup_pids, config):
    owner = start_local_server(as_global=False, config=config)
    pid = owner.info["server_process_id"]
    cleanup_pids.append(pid)
    connected = connect_to_server(ip=owner.ip, port=owner.port, as_global=False, config=config)

    with pytest.warns(UserWarning, match="was not started by this client"):
        connected.shutdown()
    assert not _wait_stopped(pid, timeout=2.0), "server stopped by a client that did not start it"
    assert dpf.core.Field(server=connected)._internal_obj is not None

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        owner.shutdown()
    assert _wait_stopped(pid), "server still running after shutdown() by its owner"


@requires_local_servers
def test_legacy_shutdown_kills_process_when_release_fails(cleanup_pids):
    server_legacy = start_local_server(
        as_global=False, config=dpf.core.AvailableServerConfigs.LegacyGrpcServer
    )
    pid = server_legacy.info["server_process_id"]
    cleanup_pids.append(pid)

    def failing_release(_):
        raise grpc.RpcError("release failed")

    server_legacy._shutdown_func = (failing_release, None)
    with pytest.warns(UserWarning, match="couldn't properly release server"):
        server_legacy.shutdown()
    assert _wait_stopped(pid), "server still running after a failed release"


# The tests below use server objects without a running DPF server, so they also run on Docker.
def _offline_server(server_type, own_process, **attributes):
    server_object = object.__new__(server_type)
    server_object._own_process = own_process
    server_object.live = True
    server_object._address = "127.0.0.1:0"
    server_object._info_instance = {
        "server_ip": "127.0.0.1",
        "server_port": 0,
        "server_process_id": 0,
    }
    server_object._session_instance = None
    server_object._remote_instance = None
    server_object._docker_config = Mock()
    for name, value in attributes.items():
        setattr(server_object, name, value)
    return server_object


def _raise(exception):
    def func(_):
        raise exception

    return func


@pytest.mark.parametrize("server_type", [server_types.GrpcServer, server_types.LegacyGrpcServer])
def test_shutdown_of_not_owned_server_is_ignored(server_type):
    release = Mock()
    server_object = _offline_server(server_type, own_process=False, _shutdown_func=(release, None))

    with pytest.warns(UserWarning, match="was not started by this client"):
        server_object.shutdown()
    release.assert_not_called()
    assert server_object.live

    server_object.live = False
    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        server_object.shutdown()


def test_grpc_server_shutdown_warns_when_server_calls_fail():
    failing = _raise(errors.DPFServerException("server error"))
    server_object = _offline_server(
        server_types.GrpcServer,
        own_process=True,
        _preparing_shutdown_func=(failing, None),
        _shutdown_func=(failing, None),
    )

    with pytest.warns(UserWarning, match="couldn't prepare shutdown"):
        with pytest.warns(UserWarning, match="couldn't shutdown server"):
            server_object.shutdown()
    assert not server_object.live
    server_object._docker_config.remove_docker_image.assert_called_once_with()


def test_legacy_shutdown_skips_release_when_prepare_fails():
    release = Mock()
    server_object = _offline_server(
        server_types.LegacyGrpcServer,
        own_process=True,
        _preparing_shutdown_func=(_raise(grpc.RpcError("prepare failed")), None),
        _shutdown_func=(release, None),
    )

    with pytest.warns(UserWarning, match="couldn't prepare shutdown"):
        server_object.shutdown()
    release.assert_not_called()
    assert not server_object.live


@pytest.mark.parametrize(
    "kill_error", [None, psutil.NoSuchProcess(0)], ids=["killed", "kill fails"]
)
def test_legacy_shutdown_kills_process_when_release_fails_offline(monkeypatch, kill_error):
    process_cls = Mock()
    process_cls.return_value.kill.side_effect = kill_error
    monkeypatch.setattr(server_types.psutil, "Process", process_cls)
    server_object = _offline_server(
        server_types.LegacyGrpcServer,
        own_process=True,
        _preparing_shutdown_func=(Mock(), None),
        _shutdown_func=(_raise(grpc.RpcError("release failed")), None),
    )

    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        server_object.shutdown()
    messages = [str(w.message) for w in record]

    process_cls.assert_called_once_with(0)
    process_cls.return_value.kill.assert_called_once_with()
    assert any("couldn't properly release server" in m for m in messages)
    assert any("NoSuchProcess" in m for m in messages) == (kill_error is not None)
    assert not server_object.live
