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

"""Shutdown contract of gRPC servers, including workflows spanning 2 servers."""

import gc
import warnings

import psutil
import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from conftest import running_docker

# On Docker, server PIDs are container-local and servers in separate containers cannot reach each other.
pytestmark = pytest.mark.skipif(
    running_docker, reason="Requires servers running on the local host."
)

GRPC_CONFIG = dpf.AvailableServerConfigs.GrpcServer
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
    server1 = dpf.start_local_server(as_global=False, config=GRPC_CONFIG)
    server2 = dpf.start_local_server(as_global=False, config=GRPC_CONFIG)
    pids = (server1.info["server_process_id"], server2.info["server_process_id"])

    ds = dpf.DataSources(examples.find_static_rst(server=server1), server=server1)
    disp_op = dpf.operators.result.displacement(server=server1)
    disp_op.inputs.data_sources.connect(ds)

    norm_op = dpf.operators.math.norm_fc(server=server2)
    norm_op.inputs.connect(disp_op.outputs)
    return server1, server2, pids, ds, disp_op, norm_op


def _check_result(norm_op):
    fc = norm_op.get_output(0, dpf.types.fields_container)
    assert len(fc) == 1
    assert fc[0].max().data_as_list[0] > 0.0


@pytest.fixture
def cleanup_pids():
    pids = []
    yield pids
    for pid in pids:
        if _is_running(pid):
            psutil.Process(pid).kill()


def test_owner_shutdown_stops_server_used_by_another_server(cleanup_pids):
    """Method 1: an explicit ``shutdown()`` by the owner always stops the server."""
    server1, server2, (pid1, pid2), ds, disp_op, norm_op = _build_cross_server_workflow()
    cleanup_pids.extend([pid1, pid2])

    server1.shutdown()
    assert _wait_stopped(pid1), "server1 still running after shutdown()"
    assert _is_running(pid2)

    with pytest.raises(Exception):
        norm_op.get_output(0, dpf.types.fields_container)

    server2.shutdown()
    assert _wait_stopped(pid2), "server2 still running after shutdown()"


def test_cross_server_workflow_survives_dereference(cleanup_pids):
    """Method 2: stop servers by dropping the Python references."""
    server1, server2, (pid1, pid2), ds, disp_op, norm_op = _build_cross_server_workflow()
    cleanup_pids.extend([pid1, pid2])

    del server1
    gc.collect()
    assert not _wait_stopped(pid1, timeout=2.0), "server1 stopped while still used by server2"
    assert _is_running(pid2)

    _check_result(norm_op)

    del server2, ds, disp_op, norm_op
    # operators are in reference cycles (op -> op._outputs -> op)
    gc.collect()
    assert _wait_stopped(pid2), "server2 still running after dereference"
    assert _wait_stopped(pid1), "server1 still running after dereference"


def test_shutdown_from_non_owner_is_ignored_with_warning(cleanup_pids):
    owner = dpf.start_local_server(as_global=False, config=GRPC_CONFIG)
    pid = owner.info["server_process_id"]
    cleanup_pids.append(pid)
    connected = dpf.connect_to_server(
        ip=owner.ip, port=owner.port, as_global=False, config=GRPC_CONFIG
    )

    with pytest.warns(UserWarning, match="was not started by this client"):
        connected.shutdown()
    assert not _wait_stopped(pid, timeout=2.0), "server stopped by a client that did not start it"
    assert dpf.Field(server=connected)._internal_obj is not None

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        owner.shutdown()
    assert _wait_stopped(pid), "server still running after shutdown() by its owner"
