"""Verify all examples can be accessed or downloaded"""
import pytest
from conftest import SERVER_VERSION_HIGHER_THAN_4_0
from ansys.dpf import core as dpf


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0, reason='Requires server version higher than 4.0')
def test_num_threads():
    op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
    c = op.config
    nOrg = c.get_num_threads_option()
    assert nOrg == '0'  # defaults to 0
    c.set_num_threads_option(5)
    op.config = c
    assert op.config.get_num_threads_option() == '5'
