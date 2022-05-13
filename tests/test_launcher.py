from unittest.mock import create_autospec
import grpc
import pytest
import sys
import ansys.platform.instancemanagement as pypim

from ansys.dpf import core
from ansys.dpf.core import server
from ansys.dpf.core.misc import is_ubuntu
from ansys.dpf.core.server import DpfServer, __ansys_version__

ansys_path = core.misc.find_ansys()

invalid_version = None
if ansys_path is not None:
    try:
        invalid_version = int(ansys_path[-3:]) < 211
    except:
        invalid_version = True

# skip unless ansys v212 is installed
if ansys_path is None or invalid_version or is_ubuntu():
    pytestmark = pytest.mark.skip("Requires local install of ANSYS 2021R2")


def test_start_local():
    if not core.SERVER:
        core.start_local_server()
    starting_server = id(core.SERVER)
    n_init = len(core._server_instances)
    server = core.start_local_server(as_global=False, ansys_path=core.SERVER.ansys_path)
    assert len(core._server_instances) == n_init + 1
    core._server_instances[-1]().shutdown()

    # ensure global channel didn't change
    assert starting_server == id(core.SERVER)

def test_start_remote(monkeypatch):
    # Test for the Product Instance Management API integration

    # Start a local DPF server and create a mock PyPIM pretending it is starting it
    local_server = core.start_local_server(as_global=False, ansys_path=core.SERVER.ansys_path)
    server_address = local_server._address
    mock_instance = pypim.Instance(
        definition_name="definitions/fake-dpf",
        name="instances/fake-dpf",
        ready=True,
        status_message=None,
        services={"grpc": pypim.Service(uri=server_address, headers={})},
    )
    # Mock the wait_for_ready method so that it immediately returns
    mock_instance.wait_for_ready = create_autospec(mock_instance.wait_for_ready)
    # Mock the deletion method
    mock_instance.delete = create_autospec(mock_instance.delete)

    # Mock the PyPIM client, so that on the "create_instance" call it returns the mock instance
    # Note: the host and port here will not be used.
    mock_client = pypim.Client(channel=grpc.insecure_channel("localhost:12345"))
    mock_client.create_instance = create_autospec(
        mock_client.create_instance, return_value=mock_instance
    )

    # Mock the general pypim connection and configuration check method to expose the mock client.
    mock_connect = create_autospec(pypim.connect, return_value=mock_client)
    monkeypatch.setattr(pypim, "connect", mock_connect)
    monkeypatch.setenv("ANSYS_PLATFORM_INSTANCEMANAGEMENT_CONFIG", "/fake/config.json")

    # Call the generic startup sequence with no arguments
    server = DpfServer()

    # It detected the environment and connected to pypim
    assert mock_connect.called

    # It created a remote instance through PyPIM
    mock_client.create_instance.assert_called_with(
        product_name="dpf", product_version=__ansys_version__
    )

    # It waited for this instance to be ready
    assert mock_instance.wait_for_ready.called

    # It connected using the address provided by PyPIM
    assert server._address == server_address

def test_start_local_failed():
    with pytest.raises(NotADirectoryError):
        core.start_local_server(ansys_path="", use_docker_by_default=False)

def test_start_remote_failed(monkeypatch):
    # Verifies that the error includes the package name to install when using
    # launch_remote_dpf() without the requirements installed.
    monkeypatch.setitem(sys.modules, "ansys.platform.instancemanagement", None)
    with pytest.raises(ImportError) as exc:
        server.launch_remote_dpf()
    assert "ansys-platform-instancemanagement" in str(exc)

def test_server_ip():
    assert core.SERVER.ip != None
    assert core.SERVER.port != None
    assert core.SERVER.version != None

    assert core.SERVER.info["server_process_id"] != None
    assert core.SERVER.info["server_ip"] != None
    assert core.SERVER.info["server_port"] != None
    assert core.SERVER.info["server_version"] != None
