"""Verify all examples can be accessed or downloaded"""
import pytest

from ansys.dpf import core as dpf

def test_num_threads():
    op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
    c = op.config
    nOrg = c.get_num_threads_option()
    assert nOrg == '0' # defaults to 0
    c.set_num_threads_option(5)
    op.config = c
    assert op.config.get_num_threads_option() == '5'
