import numpy as np
import pytest
from conftest import local_servers
from ansys.dpf import core
from ansys.dpf.core import operators as ops
from ansys.dpf.core import examples
from ansys.dpf.core.check_version import meets_version, get_server_version

SERVER_VERSION_HIGHER_THAN_4_0 = meets_version(get_server_version(core._global_server()), "4.0")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_connect_remote_operators(simple_bar):
    data_sources1 = core.DataSources(simple_bar)
    op1 = ops.result.displacement(data_sources=data_sources1)
    data_sources2 = core.DataSources(simple_bar, server=local_servers[0])
    op2 = ops.result.displacement(data_sources=data_sources2, server=local_servers[0])
    add = ops.math.add_fc(op1, op2)
    fc = add.outputs.fields_container()
    assert np.allclose(fc[0].data, 2*op1.outputs.fields_container()[0].data)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_connect_3remote_operators(simple_bar):
    data_sources1 = core.DataSources(simple_bar)
    op1 = ops.result.displacement(data_sources=data_sources1)
    data_sources2 = core.DataSources(simple_bar, server=local_servers[0])
    op2 = ops.result.displacement(data_sources=data_sources2, server=local_servers[0])
    add = ops.math.add_fc(op1, op2, server=local_servers[1])
    fc = add.outputs.fields_container()
    assert np.allclose(fc[0].data, 2*op1.outputs.fields_container()[0].data)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_connect_remote_data_to_operator(simple_bar):
    data_sources1 = core.DataSources(simple_bar)
    op2 = ops.result.displacement(data_sources=data_sources1, server=local_servers[0])
    add = ops.math.add_fc(op2, op2, server=local_servers[1])
    fc = add.outputs.fields_container()
    assert np.allclose(fc[0].data, 2*op2.outputs.fields_container()[0].data)
