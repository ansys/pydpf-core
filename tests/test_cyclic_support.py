import gc
import weakref

import pytest
from ansys import dpf
from ansys.dpf import core as dpf


def test_cyc_support_from_model(cyclic_lin_rst):
    data_sources = dpf.DataSources(cyclic_lin_rst)
    model = dpf.Model(data_sources)
    result_info = model.metadata.result_info
    assert result_info.cyclic_symmetry_type == "single_stage"
    assert result_info.has_cyclic == True

    cyc_support = result_info.cyclic_support
    assert cyc_support.num_sectors() == 15
    assert cyc_support.num_stages == 1
    assert cyc_support.sectors_set_for_expansion().ids == [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ]
    assert len(cyc_support.base_elements_scoping().ids) == 9
    assert len(cyc_support.base_nodes_scoping().ids) == 32

    exp = cyc_support.expand_node_id(1)
    assert exp.ids == [
        1,
        33,
        65,
        97,
        129,
        161,
        193,
        225,
        257,
        289,
        321,
        353,
        385,
        417,
        449,
    ]

    exp = cyc_support.expand_element_id(1)
    assert exp.ids == [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109, 118, 127]

    exp = cyc_support.expand_node_id(1, [0, 1, 2])
    assert exp.ids == [1, 33, 65]

    exp = cyc_support.expand_element_id(1, [0, 1, 2])
    assert exp.ids == [1, 10, 19]


def test_cyc_support_from_to_operator(cyclic_lin_rst):
    data_sources = dpf.DataSources(cyclic_lin_rst)
    model = dpf.Model(data_sources)
    result_info = model.metadata.result_info
    cyc_support = result_info.cyclic_support
    op = dpf.operators.metadata.cyclic_mesh_expansion(cyclic_support=cyc_support)
    exp = op.outputs.cyclic_support()
    mesh = op.outputs.meshed_region()
    assert exp.num_sectors() == 15
    assert exp.num_stages == 1
    assert exp.sectors_set_for_expansion().ids == [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ]
    assert len(exp.base_elements_scoping().ids) == 9
    assert len(exp.base_nodes_scoping().ids) == 32


def test_cyc_support_from_to_workflow(cyclic_lin_rst):
    data_sources = dpf.DataSources(cyclic_lin_rst)
    model = dpf.Model(data_sources)
    result_info = model.metadata.result_info
    cyc_support = result_info.cyclic_support
    op = dpf.operators.metadata.cyclic_mesh_expansion()
    wf = dpf.Workflow()
    wf.set_input_name("sup", op.inputs.cyclic_support)
    wf.set_output_name("sup", op.outputs.cyclic_support)
    wf.connect("sup", cyc_support)
    exp = wf.get_output("sup", dpf.types.cyclic_support)
    mesh = op.outputs.meshed_region()
    assert exp.num_sectors() == 15
    assert exp.num_stages == 1
    assert exp.sectors_set_for_expansion().ids == [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ]
    assert len(exp.base_elements_scoping().ids) == 9
    assert len(exp.base_nodes_scoping().ids) == 32


def test_delete_cyc_support(cyclic_lin_rst):
    data_sources = dpf.DataSources(cyclic_lin_rst)
    model = dpf.Model(data_sources)
    result_info = model.metadata.result_info
    cyc_support = result_info.cyclic_support
    cyc_support.__del__()
    with pytest.raises(Exception):
        cyc_support.num_stages


def test_delete_auto_cyc_support(cyclic_lin_rst):
    data_sources = dpf.DataSources(cyclic_lin_rst)
    model = dpf.Model(data_sources)
    result_info = model.metadata.result_info
    cyc_support = result_info.cyclic_support
    op_ref = weakref.ref(cyc_support)

    del cyc_support
    gc.collect()
    assert op_ref() is None
