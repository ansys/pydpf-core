# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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

import sys
from unittest.mock import create_autospec

import grpc
import pytest

from ansys.dpf.core import server_types
from ansys.dpf.core.server_factory import ServerFactory
import ansys.platform.instancemanagement as pypim
from conftest import running_docker


@pytest.mark.skipif(running_docker, reason="not for Docker")
def test_start_remote(monkeypatch):
    # Test for the Product Instance Management API integration

    # Start a local DPF server and create a mock PyPIM pretending it is starting it
    from ansys.dpf import core
    from ansys.dpf.core.server_factory import CommunicationProtocols, ServerConfig

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
    mock_client.create_instance.assert_called_with(product_name="dpf", product_version=None)

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
