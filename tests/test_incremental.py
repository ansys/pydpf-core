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

import numpy as np
import pytest

from ansys.dpf import core
from ansys.dpf.core import common
import conftest


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="for_each not implemented below 6.0",
)
def test_incremental_results(server_type, plate_msup):
    ds = core.DataSources(plate_msup, server=server_type)
    scoping = core.time_freq_scoping_factory.scoping_on_all_time_freqs(ds)

    def create_wf():
        res_op = core.operators.result.displacement(
            data_sources=ds, time_scoping=scoping, server=server_type
        )
        concat_op = core.Operator("incremental::merge::fields_container", server=server_type)
        concat_op.connect(0, res_op, 0)

        return (res_op, concat_op)

    # incremental
    (start_op, end_op) = create_wf()
    inc_op = core.split_workflow_in_chunks(start_op, end_op, scoping, chunk_size=5)

    (_, ref_op) = create_wf()

    inc_fc = inc_op.get_output(0, core.types.fields_container)
    ref_fc = ref_op.get_output(0, core.types.fields_container)

    assert len(inc_fc.get_time_scoping()) == len(ref_fc.get_time_scoping())
    for id in ref_fc.get_time_scoping().ids:
        ref_field = ref_fc.get_field_by_time_id(id)
        inc_field = inc_fc.get_field_by_time_id(id)
        assert np.isclose(ref_field.data, inc_field.data).all()


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="for_each not implemented below 6.0",
)
def test_incremental_minmax(server_type, plate_msup):
    ds = core.DataSources(plate_msup, server=server_type)
    scoping = core.time_freq_scoping_factory.scoping_on_all_time_freqs(ds)

    def create_wf():
        res_op = core.operators.result.displacement(
            data_sources=ds, time_scoping=scoping, server=server_type
        )
        minmax_op = core.operators.min_max.min_max_fc_inc(res_op, server=server_type)

        return (res_op, minmax_op)

    # incremental
    (start_op, end_op) = create_wf()
    inc_op = core.split_workflow_in_chunks(start_op, end_op, scoping, chunk_size=5)

    # reference
    (_, ref_op) = create_wf()

    # assert
    inc_field_min = inc_op.get_output(0, core.types.field)
    inc_field_max = inc_op.get_output(1, core.types.field)
    ref_field_min = ref_op.get_output(0, core.types.field)
    ref_field_max = ref_op.get_output(1, core.types.field)

    assert np.isclose(ref_field_min.data, inc_field_min.data).all()
    assert np.isclose(ref_field_max.data, inc_field_max.data).all()


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="for_each not implemented below 6.0",
)
def test_incremental_accumulate(server_type, plate_msup):
    ds = core.DataSources(plate_msup, server=server_type)
    scoping = core.time_freq_scoping_factory.scoping_on_all_time_freqs(ds)

    def create_wf():
        res_op = core.operators.result.displacement(
            data_sources=ds, time_scoping=scoping, server=server_type
        )
        acc_op = core.operators.math.accumulate_over_label_fc(res_op, server=server_type)
        acc_op.connect(1, common.DefinitionLabels.time)

        return (res_op, acc_op)

    # incremental
    (start_op, end_op) = create_wf()
    inc_op = core.split_workflow_in_chunks(start_op, end_op, scoping, chunk_size=5)

    # reference
    (_, ref_op) = create_wf()

    # assert
    inc_field = inc_op.get_output(0, core.types.field)
    ref_field = ref_op.get_output(0, core.types.field)

    assert np.isclose(ref_field.data, inc_field.data).all()


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="for_each not implemented below 6.0",
)
def test_incremental_average(server_type, plate_msup):
    ds = core.DataSources(plate_msup, server=server_type)
    scoping = core.time_freq_scoping_factory.scoping_on_all_time_freqs(ds)

    def create_wf():
        res_op = core.operators.result.displacement(
            data_sources=ds, time_scoping=scoping, server=server_type
        )
        avg_op = core.operators.math.average_over_label_fc(res_op, server=server_type)
        avg_op.connect(1, common.DefinitionLabels.time)
        return (res_op, avg_op)

    # incremental
    (start_op, end_op) = create_wf()
    inc_op = core.split_workflow_in_chunks(start_op, end_op, scoping, chunk_size=5)

    # reference
    (_, ref_op) = create_wf()

    # assert
    inc_field = inc_op.get_output(0, core.types.field)
    ref_field = ref_op.get_output(0, core.types.field)

    assert np.isclose(ref_field.data, inc_field.data).all()


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="for_each not implemented below 6.0",
)
def test_incremental_estimation(server_type, plate_msup):
    ds = core.DataSources(plate_msup, server=server_type)
    scoping = core.time_freq_scoping_factory.scoping_on_all_time_freqs(ds)

    def create_wf():
        res_op = core.operators.result.displacement(
            data_sources=ds, time_scoping=scoping, server=server_type
        )
        concat_op = core.Operator("incremental::merge::fields_container", server=server_type)
        concat_op.connect(0, res_op, 0)

        return (res_op, concat_op)

    # incremental
    (start_op, end_op) = create_wf()

    helper = core.IncrementalHelper(start_op, end_op, scoping, scoping_pin=0)
    # 9432 bytes per output according to the heuristic for this plate_msup example
    chunk_size = helper.estimate_size(max_bytes=50 * 1024)

    assert chunk_size == 5
