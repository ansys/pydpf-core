import os

import pytest
import conftest

import ansys.dpf.core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.core import errors
from conftest import running_docker


@pytest.mark.order(1)
@pytest.mark.skipif(
    running_docker
    or os.environ.get("ANSYS_DPF_ACCEPT_LA", "") == ""
    or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="Tests ANSYS_DPF_ACCEPT_LA",
)
def test_license_agr(restore_accept_la_env):
    # store the server version beforehand
    server_ge_8 = conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0
    dpf.server.shutdown_global_server()
    config = dpf.AvailableServerConfigs.InProcessServer
    init_val = os.environ["ANSYS_DPF_ACCEPT_LA"]
    del os.environ["ANSYS_DPF_ACCEPT_LA"]
    if server_ge_8:
        dpf.start_local_server(config=config, as_global=True)
        dpf.Operator("stream_provider")
    else:
        with pytest.raises(errors.DPFServerException):
            dpf.start_local_server(config=config, as_global=True)
        with pytest.raises(errors.DPFServerException):
            dpf.Operator("stream_provider")
    os.environ["ANSYS_DPF_ACCEPT_LA"] = init_val
    dpf.start_local_server(config=config, as_global=True)
    assert "static" in examples.find_static_rst()
    assert dpf.Operator("stream_provider") is not None


@pytest.mark.order(2)
@pytest.mark.skipif(
    os.environ.get("ANSYS_DPF_ACCEPT_LA", "") == ""
    or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="Tests ANSYS_DPF_ACCEPT_LA",
)
def test_license_agr_remote(remote_config_server_type, restore_accept_la_env):
    init_val = os.environ["ANSYS_DPF_ACCEPT_LA"]
    del os.environ["ANSYS_DPF_ACCEPT_LA"]
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0:
        dpf.start_local_server(config=remote_config_server_type, as_global=True)
    else:
        with pytest.raises(errors.RuntimeError):
            dpf.start_local_server(config=remote_config_server_type, as_global=True)
    # with pytest.raises((errors.DPFServerException, RuntimeError)):
    #     dpf.Operator("stream_provider")  # No remote server to instantiate the operator on
    os.environ["ANSYS_DPF_ACCEPT_LA"] = init_val
    dpf.start_local_server(config=remote_config_server_type, as_global=True)
    assert "static" in examples.find_static_rst()
    assert dpf.Operator("stream_provider") is not None


@pytest.mark.order(4)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0, reason="not supported"
)
@conftest.raises_for_servers_version_under("6.0")
def test_apply_context_remote(remote_config_server_type):
    dpf.server.shutdown_all_session_servers()
    dpf.SERVER_CONFIGURATION = remote_config_server_type
    field = dpf.Field()
    field.append([0.0], 1)
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0:
        if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1:
            with pytest.raises(errors.DPFServerException):
                op = dpf.Operator("core::field::high_pass")
                op.connect(0, field)
                op.connect(1, 0.0)
                op.eval()
        else:
            with pytest.raises(errors.DPFServerException):
                _ = dpf.Operator("core::field::high_pass")
            with pytest.raises(errors.DPFServerException):
                if dpf.SERVER.os == "nt":
                    dpf.load_library("Ans.Dpf.Math.dll", "math_operators")
                else:
                    dpf.load_library("libAns.Dpf.Math.so", "math_operators")
        assert dpf.SERVER.context == dpf.AvailableServerContexts.entry
    else:
        dpf.start_local_server()

    dpf.SERVER.apply_context(dpf.AvailableServerContexts.premium)
    op = dpf.Operator("core::field::high_pass")
    op.connect(0, field)
    op.connect(1, 0.0)
    op.eval()
    field = None
    assert dpf.SERVER.context == dpf.AvailableServerContexts.premium
    dpf.server.shutdown_all_session_servers()
    field = dpf.Field()
    field.append([0.0], 1)
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1:
        with pytest.raises(errors.DPFServerException):
            op = dpf.Operator("core::field::high_pass")
            op.connect(0, field)
            op.connect(1, 0.0)
            op.eval()
    elif conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0:
        with pytest.raises(errors.DPFServerException):
            _ = dpf.Operator("core::field::high_pass")
    dpf.SERVER.apply_context(dpf.AvailableServerContexts.premium)
    _ = dpf.Operator("core::field::high_pass")
    with pytest.raises(errors.DPFServerException):
        dpf.SERVER.apply_context(dpf.AvailableServerContexts.entry)

    assert dpf.SERVER.context == dpf.AvailableServerContexts.premium


@pytest.mark.order(5)
@conftest.raises_for_servers_version_under("4.0")
def test_runtime_client_no_server(remote_config_server_type):
    dpf.server.shutdown_all_session_servers()
    dpf.SERVER_CONFIGURATION = remote_config_server_type
    client_config = dpf.settings.get_runtime_client_config()
    initial = client_config.stream_floats_instead_of_doubles
    client_config.stream_floats_instead_of_doubles = True
    server = dpf.start_local_server(as_global=False)
    client_config = dpf.settings.get_runtime_client_config(server)
    assert client_config.stream_floats_instead_of_doubles is True


    server = dpf.connect_to_server(
        ip=server.ip, port=server.port, as_global=False)
    client_config = dpf.settings.get_runtime_client_config(server)
    assert client_config.stream_floats_instead_of_doubles is True

    dpf.server.shutdown_all_session_servers()
    client_config = dpf.settings.get_runtime_client_config()
    client_config.stream_floats_instead_of_doubles = initial
    assert client_config.stream_floats_instead_of_doubles == initial


@pytest.mark.order("last")  # Mandatory
@pytest.mark.skipif(
    running_docker or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="AWP ROOT is not set with Docker",
)
@conftest.raises_for_servers_version_under("6.0")
def test_apply_context():
    # Carefully: this test only work if the premium context has never been applied before on the
    # in process server, otherwise premium operators will already be loaded. Must be marked as last.
    dpf.server.shutdown_all_session_servers()
    dpf.SERVER_CONFIGURATION = dpf.AvailableServerConfigs.InProcessServer
    field = dpf.Field()
    field.append([0.0], 1)
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0:
        if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1:
            with pytest.raises(errors.DPFServerException):
                op = dpf.Operator("core::field::high_pass")
                op.connect(0, field)
                op.connect(1, 0.0)
                op.eval()
        else:
            with pytest.raises(KeyError):
                dpf.Operator("core::field::high_pass")
            with pytest.raises(errors.DPFServerException):
                if dpf.SERVER.os == "nt":
                    dpf.load_library("Ans.Dpf.Math.dll", "math_operators")
                else:
                    dpf.load_library("libAns.Dpf.Math.so", "math_operators")
        assert dpf.SERVER.context == dpf.AvailableServerContexts.entry
    else:
        dpf.start_local_server()

    dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
    assert dpf.SERVER.context == dpf.AvailableServerContexts.premium
    op = dpf.Operator("core::field::high_pass")
    op.connect(0, field)
    op.connect(1, 0.0)
    op.eval()
    with pytest.raises(errors.DPFServerException):
        dpf.SERVER.apply_context(dpf.AvailableServerContexts.entry)
    assert dpf.SERVER.context == dpf.AvailableServerContexts.premium
