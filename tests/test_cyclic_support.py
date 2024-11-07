# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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

import gc
import weakref
import numpy as np

import pytest

from ansys import dpf
from ansys.dpf import core as dpf


def test_cyc_support_from_model(cyclic_lin_rst):
    data_sources = dpf.DataSources(cyclic_lin_rst)
    model = dpf.Model(data_sources)
    result_info = model.metadata.result_info
    assert result_info.cyclic_symmetry_type == "single_stage"
    assert result_info.has_cyclic is True

    cyc_support = result_info.cyclic_support
    assert cyc_support.num_sectors() == 15
    assert cyc_support.num_stages == 1
    assert np.allclose(
        cyc_support.sectors_set_for_expansion().ids,
        [
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
        ],
    )
    assert len(cyc_support.base_elements_scoping().ids) == 9
    assert len(cyc_support.base_nodes_scoping().ids) == 32

    exp = cyc_support.expand_node_id(1)
    assert np.allclose(
        exp.ids,
        [
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
        ],
    )

    exp = cyc_support.expand_element_id(1)
    assert np.allclose(exp.ids, [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109, 118, 127])

    exp = cyc_support.expand_node_id(1, [0, 1, 2])
    assert np.allclose(exp.ids, [1, 33, 65])

    exp = cyc_support.expand_element_id(1, [0, 1, 2])
    assert np.allclose(exp.ids, [1, 10, 19])

    exp = cyc_support.cs().scoping
    assert np.allclose(exp.ids, [12])


def test_cyc_support_from_to_operator(cyclic_lin_rst, server_type):
    data_sources = dpf.DataSources(cyclic_lin_rst, server=server_type)
    model = dpf.Model(data_sources, server=server_type)
    result_info = model.metadata.result_info
    cyc_support = result_info.cyclic_support
    op = dpf.operators.metadata.cyclic_mesh_expansion(
        cyclic_support=cyc_support, server=server_type
    )
    exp = op.outputs.cyclic_support()
    mesh = op.outputs.meshed_region()
    assert exp.num_sectors() == 15
    assert exp.num_stages == 1
    assert np.allclose(
        exp.sectors_set_for_expansion().ids,
        [
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
        ],
    )
    assert len(exp.base_elements_scoping().ids) == 9
    assert len(exp.base_nodes_scoping().ids) == 32


@pytest.mark.xfail(raises=dpf.errors.ServerTypeError)
def test_cyc_support_from_to_workflow(cyclic_lin_rst, server_type):
    data_sources = dpf.DataSources(cyclic_lin_rst, server=server_type)
    model = dpf.Model(data_sources, server=server_type)
    result_info = model.metadata.result_info
    cyc_support = result_info.cyclic_support
    op = dpf.operators.metadata.cyclic_mesh_expansion(server=server_type)
    wf = dpf.Workflow(server=server_type)
    wf.progress_bar = False
    wf.set_input_name("sup", op.inputs.cyclic_support)
    wf.set_output_name("sup", op.outputs.cyclic_support)
    wf.connect("sup", cyc_support)
    exp = wf.get_output("sup", dpf.types.cyclic_support)
    mesh = op.outputs.meshed_region()
    assert exp.num_sectors() == 15
    assert exp.num_stages == 1
    assert np.allclose(
        exp.sectors_set_for_expansion().ids,
        [
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
        ],
    )
    assert len(exp.base_elements_scoping().ids) == 9
    assert len(exp.base_nodes_scoping().ids) == 32


def test_cyc_support_multistage(cyclic_multistage):
    model = dpf.Model(cyclic_multistage)
    cyc_support = model.metadata.result_info.cyclic_support
    assert np.allclose(
        cyc_support.expand_element_id(1, stage_num=0).ids,
        [1, 1558, 2533, 3508, 4483, 5458],
    )
    assert np.allclose(
        cyc_support.expand_node_id(1, stage_num=0).ids,
        [1, 3596, 5816, 8036, 10256, 12476],
    )
    assert np.allclose(cyc_support.sectors_set_for_expansion(stage_num=1).ids, list(range(0, 12)))

    high_low_map = my_cyclic_support.high_low_map(0)
    assert np.allclose(high_low_map.get_entity_data_by_id(1446), 1447)
    assert np.allclose(high_low_map.get_entity_data_by_id(2946), 2948)
    assert np.allclose(high_low_map.get_entity_data_by_id(1452), 1466)

    low_high_map = my_cyclic_support.low_high_map(1)
    assert np.allclose(low_high_map.get_entity_data_by_id(995), 939)
    assert np.allclose(low_high_map.get_entity_data_by_id(53), 54)
    assert np.allclose(low_high_map.get_entity_data_by_id(70), 56)


def test_delete_cyc_support(cyclic_lin_rst, server_type_legacy_grpc):
    data_sources = dpf.DataSources(cyclic_lin_rst, server=server_type_legacy_grpc)
    model = dpf.Model(data_sources, server=server_type_legacy_grpc)
    result_info = model.metadata.result_info
    cyc_support = result_info.cyclic_support
    cyc_support2 = dpf.CyclicSupport(
        cyclic_support=cyc_support._internal_obj, server=cyc_support._server
    )
    cyc_support = None
    import gc

    gc.collect()
    with pytest.raises(Exception):
        cyc_support2.num_stages


def test_delete_auto_cyc_support(cyclic_lin_rst):
    data_sources = dpf.DataSources(cyclic_lin_rst)
    model = dpf.Model(data_sources)
    result_info = model.metadata.result_info
    cyc_support = result_info.cyclic_support
    op_ref = weakref.ref(cyc_support)

    cyc_support = None
    gc.collect()
    assert op_ref() is None


@pytest.mark.skipif(True, reason="Used to test memory leaks.")
def test_cyc_support_memory_leaks(cyclic_lin_rst):
    import gc

    for i in range(2000):
        gc.collect()
        data_sources = dpf.DataSources(cyclic_lin_rst)
        model = dpf.Model(data_sources)
        result_info = model.metadata.result_info
        cyc_support = result_info.cyclic_support
        a = cyc_support.num_stages
        b = cyc_support.num_sectors()
        c = cyc_support.sectors_set_for_expansion()
        d = cyc_support.base_elements_scoping()
        e = cyc_support.base_nodes_scoping()
