import sys
from unittest.mock import create_autospec

import ansys.platform.instancemanagement as pypim
import grpc
import pytest

from ansys.dpf.core import server_types
from ansys.dpf.core.misc import __ansys_version__
from ansys.dpf.core.server_factory import ServerFactory


def test_start_remote(monkeypatch):
    # Test for the Product Instance Management API integration

    # Start a local DPF server and create a mock PyPIM pretending it is starting it
    from ansys.dpf import core
    from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols
    conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)
    local_server = core.start_local_server(as_global=False, config=conf)
    server_address = f"{local_server.ip}:{local_server.port}"
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

    # Call the generic startup sequence with no indication on how to launch it
    server_type = ServerFactory().get_server_type_from_config(conf)
    server = server_type(as_global=False)

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

    # Stop the server
    server.shutdown()

    # The delete instance is called
    assert mock_instance.delete.called


def test_start_remote_failed(monkeypatch):
    # Verifies that the error includes the package name to install when using
    # launch_remote_dpf() without the requirements installed.
    monkeypatch.setitem(sys.modules, "ansys.platform.instancemanagement", None)
    with pytest.raises(ImportError) as exc:
        server_types.launch_remote_dpf()
    assert "ansys-platform-instancemanagement" in str(exc)
