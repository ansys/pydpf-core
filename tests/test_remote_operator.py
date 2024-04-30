import numpy as np
from conftest import local_servers
import conftest
from ansys.dpf import core
from ansys.dpf.core import operators as ops
import pytest


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_connect_remote_operators(simple_bar):
    data_sources1 = core.DataSources(simple_bar)
    op1 = ops.result.displacement(data_sources=data_sources1)
    data_sources2 = core.DataSources(simple_bar, server=local_servers[0])
    op2 = ops.result.displacement(data_sources=data_sources2, server=local_servers[0])
    add = ops.math.add_fc(op1, op2)
    fc = add.outputs.fields_container()
    assert np.allclose(fc[0].data, 2 * op1.outputs.fields_container()[0].data)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_connect_3remote_operators(simple_bar):
    data_sources1 = core.DataSources(simple_bar)
    op1 = ops.result.displacement(data_sources=data_sources1)
    data_sources2 = core.DataSources(simple_bar, server=local_servers[0])
    op2 = ops.result.displacement(data_sources=data_sources2, server=local_servers[0])
    add = ops.math.add_fc(op1, op2, server=local_servers[1])
    fc = add.outputs.fields_container()
    assert np.allclose(fc[0].data, 2 * op1.outputs.fields_container()[0].data)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Connecting data from different servers is " "supported starting server version 4.0",
)
def test_connect_remote_data_to_operator(simple_bar):
    data_sources1 = core.DataSources(simple_bar)
    op2 = ops.result.displacement(data_sources=data_sources1, server=local_servers[0])
    add = ops.math.add_fc(op2, op2, server=local_servers[1])
    fc = add.outputs.fields_container()
    assert np.allclose(fc[0].data, 2 * op2.outputs.fields_container()[0].data)
