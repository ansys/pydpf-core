import os

import pytest
import conftest

from ansys import dpf
from ansys.dpf.core import examples
from conftest import running_docker


@pytest.mark.order(1)
@pytest.mark.skipif(
    running_docker
    or os.environ.get("ANSYS_DPF_ACCEPT_LA", "") is ""
    or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="Tests ANSYS_DPF_ACCEPT_LA",
)
def test_license_agr():
    config = dpf.core.AvailableServerConfigs.InProcessServer
    init_val = os.environ["ANSYS_DPF_ACCEPT_LA"]
    del os.environ["ANSYS_DPF_ACCEPT_LA"]
    with pytest.raises(dpf.core.errors.DPFServerException):
        dpf.core.start_local_server(config=config, as_global=True)
    with pytest.raises(dpf.core.errors.DPFServerException):
        dpf.core.Operator("stream_provider")
    os.environ["ANSYS_DPF_ACCEPT_LA"] = init_val
    dpf.core.start_local_server(config=config, as_global=True)
    assert "static" in examples.find_static_rst()
    assert dpf.core.Operator("stream_provider") is not None


@pytest.mark.order(2)
@pytest.mark.skipif(
    os.environ.get("ANSYS_DPF_ACCEPT_LA", "") is ""
    or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="Tests ANSYS_DPF_ACCEPT_LA",
)
def test_license_agr_remote(remote_config_server_type):
    init_val = os.environ["ANSYS_DPF_ACCEPT_LA"]
    del os.environ["ANSYS_DPF_ACCEPT_LA"]
    with pytest.raises(RuntimeError):  # runtime error raised when server is started
        dpf.core.start_local_server(config=remote_config_server_type, as_global=True)
    with pytest.raises((dpf.core.errors.DPFServerException, RuntimeError)):
        dpf.core.Operator("stream_provider")
    os.environ["ANSYS_DPF_ACCEPT_LA"] = init_val
    dpf.core.start_local_server(config=remote_config_server_type, as_global=True)
    assert "static" in examples.find_static_rst()
    assert dpf.core.Operator("stream_provider") is not None


@pytest.mark.order(4)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0, reason="not supported"
)
@conftest.raises_for_servers_version_under("6.0")
def test_apply_context_remote(remote_config_server_type):
    dpf.core.server.shutdown_all_session_servers()
    dpf.core.SERVER_CONFIGURATION = remote_config_server_type
    field = dpf.core.Field()
    field.append([0.0], 1)
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0:
        if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1:
            with pytest.raises(dpf.core.errors.DPFServerException):
                op = dpf.core.Operator("core::field::high_pass")
                op.connect(0, field)
                op.connect(1, 0.0)
                op.eval()
        else:
            with pytest.raises(dpf.core.errors.DPFServerException):
                op = dpf.core.Operator("core::field::high_pass")
            with pytest.raises(dpf.core.errors.DPFServerException):
                if dpf.core.SERVER.os == "nt":
                    dpf.core.load_library("Ans.Dpf.Math.dll", "math_operators")
                else:
                    dpf.core.load_library("libAns.Dpf.Math.so", "math_operators")
        assert dpf.core.SERVER.context == dpf.core.AvailableServerContexts.entry
    else:
        dpf.core.start_local_server()

    dpf.core.SERVER.apply_context(dpf.core.AvailableServerContexts.premium)
    op = dpf.core.Operator("core::field::high_pass")
    op.connect(0, field)
    op.connect(1, 0.0)
    op.eval()
    assert dpf.core.SERVER.context == dpf.core.AvailableServerContexts.premium
    dpf.core.server.shutdown_all_session_servers()
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1:
        with pytest.raises(dpf.core.errors.DPFServerException):
            op = dpf.core.Operator("core::field::high_pass")
            op.connect(0, field)
            op.connect(1, 0.0)
            op.eval()
    elif conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0:
        with pytest.raises(dpf.core.errors.DPFServerException):
            op = dpf.core.Operator("core::field::high_pass")
    dpf.core.set_default_server_context(dpf.core.AvailableServerContexts.premium)
    dpf.core.Operator("core::field::high_pass")
    with pytest.raises(dpf.core.errors.DPFServerException):
        dpf.core.set_default_server_context(dpf.core.AvailableServerContexts.entry)
    with pytest.raises(dpf.core.errors.DPFServerException):
        dpf.core.SERVER.apply_context(dpf.core.AvailableServerContexts.entry)

    assert dpf.core.SERVER.context == dpf.core.AvailableServerContexts.premium


@pytest.mark.order("last")  # Mandatory
@pytest.mark.skipif(
    running_docker or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="AWP ROOT is not set with Docker",
)
@conftest.raises_for_servers_version_under("6.0")
def test_apply_context():
    # Carefully: this test only work if the premium context has never been applied before on the
    # in process server, otherwise premium operators will already be loaded. Must be marked as last.
    dpf.core.server.shutdown_all_session_servers()
    dpf.core.SERVER_CONFIGURATION = dpf.core.AvailableServerConfigs.InProcessServer
    field = dpf.core.Field()
    field.append([0.0], 1)
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0:
        if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1:
            with pytest.raises(dpf.core.errors.DPFServerException):
                op = dpf.core.Operator("core::field::high_pass")
                op.connect(0, field)
                op.connect(1, 0.0)
                op.eval()
        else:
            with pytest.raises(KeyError):
                dpf.core.Operator("core::field::high_pass")
            with pytest.raises(dpf.core.errors.DPFServerException):
                if dpf.core.SERVER.os == "nt":
                    dpf.core.load_library("Ans.Dpf.Math.dll", "math_operators")
                else:
                    dpf.core.load_library("libAns.Dpf.Math.so", "math_operators")
        assert dpf.core.SERVER.context == dpf.core.AvailableServerContexts.entry
    else:
        dpf.core.start_local_server()

    dpf.core.set_default_server_context(dpf.core.AvailableServerContexts.premium)
    assert dpf.core.SERVER.context == dpf.core.AvailableServerContexts.premium
    op = dpf.core.Operator("core::field::high_pass")
    op.connect(0, field)
    op.connect(1, 0.0)
    op.eval()
    with pytest.raises(dpf.core.errors.DPFServerException):
        dpf.core.set_default_server_context(dpf.core.AvailableServerContexts.entry)
    with pytest.raises(dpf.core.errors.DPFServerException):
        dpf.core.SERVER.apply_context(dpf.core.AvailableServerContexts.entry)
    assert dpf.core.SERVER.context == dpf.core.AvailableServerContexts.premium
