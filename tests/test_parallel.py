"""
Verify all examples can be accessed or downloaded

"""
import pytest

from ansys.dpf import core as dpf
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Requires server version higher than 4.0",
)
def test_num_threads():
    op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
    c = op.config
    nOrg = c.get_num_threads_option()
    assert nOrg == "0"  # defaults to 0
    c.set_num_threads_option(5)
    op.config = c
    assert op.config.get_num_threads_option() == "5"
