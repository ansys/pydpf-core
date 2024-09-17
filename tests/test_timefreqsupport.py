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
import weakref

from ansys import dpf
from ansys.dpf.core import TimeFreqSupport, Model
from ansys.dpf.core import examples
from ansys.dpf.core import fields_factory
from ansys.dpf.core.common import locations
import conftest


@pytest.fixture()
def vel_acc_model(velocity_acceleration):
    return dpf.core.Model(velocity_acceleration)


def test_get_timefreqsupport(velocity_acceleration, server_type):
    dataSource = dpf.core.DataSources(server=server_type)
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider", server=server_type)
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    assert res.n_sets == 5
    assert res.get_frequency(0, 0) == 0.02
    assert res.get_frequency(0, 1) == 0.04
    assert res.get_frequency(cumulative_index=2) == 0.06
    assert res.get_cumulative_index(0, 0) == 0
    assert res.get_cumulative_index(freq=0.06) == 2


def test_model_time_freq_support(vel_acc_model):
    timefreq = vel_acc_model.metadata.time_freq_support
    assert str(timefreq.n_sets) in str(timefreq)
    assert len(timefreq.time_frequencies.data) == timefreq.n_sets
    expected_data = [0.02, 0.04, 0.06, 0.08, 0.1]
    assert np.allclose(expected_data, timefreq.time_frequencies.data)


def test_get_frequencies_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    freq = res.time_frequencies
    assert np.allclose(freq.data, [0.02, 0.04, 0.06, 0.08, 0.1])
    assert freq.scoping.ids == [1]


def test_print_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    assert "Number of sets: 5" in str(res)
    assert "Time (s)" in str(res)
    assert "LoadStep" in str(res)
    assert "Substep" in str(res)


def test_delete_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    res = None
    import gc

    gc.collect()
    with pytest.raises(Exception):
        res.get_frequence(0, 0)


def test_delete_auto_timefreqsupport(simple_rst):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(simple_rst)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    ref = weakref.ref(res)
    res = None
    import gc

    gc.collect()
    assert ref() is None


def test_create_time_freq_support(server_type):
    tfq = TimeFreqSupport(server=server_type)
    assert tfq is not None


def test_update_time_freq_support_real_freq(server_type):
    tfq = TimeFreqSupport(server=server_type)
    frequencies = fields_factory.create_scalar_field(3, server=server_type)
    frequencies.data = [0.1, 0.32, 0.4]
    tfq.time_frequencies = frequencies
    frequencies_check = tfq.time_frequencies
    data1 = frequencies.data
    data2 = frequencies_check.data
    assert np.allclose(data1, data2)
    assert tfq.rpms is None
    assert tfq.complex_frequencies is None


def test_update_time_freq_support_im_freq(server_type):
    tfq = TimeFreqSupport(server=server_type)
    frequencies = fields_factory.create_scalar_field(3, server=server_type)
    frequencies.data = [0.1, 0.32, 0.4]
    tfq.complex_frequencies = frequencies
    frequencies_check = tfq.complex_frequencies
    data1 = frequencies.data
    data2 = frequencies_check.data
    assert np.allclose(data1, data2)
    assert tfq.rpms is None
    assert tfq.time_frequencies is None


def test_update_time_freq_support_rpms(server_type):
    tfq = TimeFreqSupport(server=server_type)
    rpm = fields_factory.create_scalar_field(3, server=server_type)
    rpm.data = [0.1, 0.32, 0.4]
    tfq.rpms = rpm
    rpm_check = tfq.rpms
    assert np.allclose(rpm.data, rpm_check.data)
    assert tfq.time_frequencies is None
    assert tfq.complex_frequencies is None


def test_update_time_freq_support_harmonic_indeces(server_type):
    tfq = TimeFreqSupport(server=server_type)
    harm = fields_factory.create_scalar_field(3, server=server_type)
    harm.data = [0.1, 0.32, 0.4]
    tfq.set_harmonic_indices(harm)
    harm_check = tfq.get_harmonic_indices()
    assert np.allclose(harm.data, harm_check.data)
    assert tfq.time_frequencies is None
    assert tfq.complex_frequencies is None
    assert tfq.rpms is None


def test_update_time_freq_support_harmonic_indices_with_num_stage(server_type):
    tfq = TimeFreqSupport(server=server_type)
    harm = fields_factory.create_scalar_field(3, server=server_type)
    harm.data = [0.12, 0.32, 0.8]
    tfq.set_harmonic_indices(harm, 2)
    harm_check = tfq.get_harmonic_indices(2)
    assert np.allclose(harm.data, harm_check.data)
    assert tfq.time_frequencies is None
    assert tfq.complex_frequencies is None
    assert tfq.rpms is None
    harm_check_2 = tfq.get_harmonic_indices(3)
    assert harm_check_2 is None
    harm_check_3 = tfq.get_harmonic_indices(0)
    assert harm_check_3 is None
    harm_check_4 = tfq.get_harmonic_indices()
    assert harm_check_4 is None


def test_update_time_freq_support_real_freq_with_ds(velocity_acceleration):
    model = Model(velocity_acceleration)
    disp = model.results.displacement()
    tfq = disp.outputs.fields_container().time_freq_support
    assert tfq.time_frequencies is not None
    frequencies = fields_factory.create_scalar_field(3)
    frequencies.data = [0.1, 0.32, 0.4]
    tfq.time_frequencies = frequencies
    frequencies_check = tfq.time_frequencies
    assert np.allclose(frequencies.data, frequencies_check.data)


def test_append_step_1(server_type):
    tfq = TimeFreqSupport(server=server_type)
    frequencies = [0.1, 0.21, 1.0]
    tfq.append_step(1, frequencies, rpm_value=2.0)
    assert len(tfq.rpms.data) == 1
    assert len(tfq.time_frequencies.data) == 3
    assert tfq.rpms.location == locations.time_freq_step
    assert tfq.time_frequencies.location == locations.time_freq
    assert np.allclose(frequencies, tfq.time_frequencies.data)
    assert np.allclose(2.0, tfq.rpms.data)
    assert tfq.complex_frequencies is None
    assert tfq.get_harmonic_indices() is None
    frequencies2 = [1.1, 2.0]
    tfq.append_step(1, frequencies2, rpm_value=2.0)
    assert len(tfq.rpms.data) == 2
    assert len(tfq.time_frequencies.data) == 5
    assert tfq.rpms.location == locations.time_freq_step
    assert tfq.time_frequencies.location == locations.time_freq
    assert np.allclose(frequencies + frequencies2, tfq.time_frequencies.data)
    assert np.allclose(2.0, tfq.rpms.data)
    assert tfq.complex_frequencies is None
    assert tfq.get_harmonic_indices() is None


def test_append_step_2(server_type):
    tfq = TimeFreqSupport(server=server_type)
    tfq.append_step(1, [0.1, 0.21, 1.0], rpm_value=2.0, step_harmonic_indices=[1.0, 2.0, 3.0])
    tfq.append_step(2, [1.1, 2.0], rpm_value=2.3, step_harmonic_indices=[1.0, 2.0])
    tfq.append_step(3, [0.23, 0.25], rpm_value=3.0, step_harmonic_indices=[1.0, 2.0])
    assert len(tfq.rpms.data) == 3
    assert len(tfq.time_frequencies.data) == 7
    assert len(tfq.get_harmonic_indices().data) == 7
    assert tfq.rpms.location == locations.time_freq_step
    assert tfq.get_harmonic_indices().location == locations.time_freq
    assert tfq.time_frequencies.location == locations.time_freq
    assert np.allclose([0.1, 0.21, 1.0, 1.1, 2.0, 0.23, 0.25], tfq.time_frequencies.data)
    assert np.allclose([2.0, 2.3, 3.0], tfq.rpms.data)
    assert tfq.complex_frequencies is None


def test_append_step_3(server_type):
    tfq = TimeFreqSupport(server=server_type)
    tfq.append_step(
        1,
        [0.1, 0.21],
        rpm_value=2.0,
        step_harmonic_indices={1: [1.0, 2.0], 2: [3.0, 3.1]},
    )
    assert len(tfq.rpms.data) == 1
    assert len(tfq.time_frequencies.data) == 2
    assert len(tfq.get_harmonic_indices(1).data) == 2
    assert len(tfq.get_harmonic_indices(2).data) == 2
    assert tfq.get_harmonic_indices() is None
    assert tfq.rpms.location == locations.time_freq_step
    assert tfq.get_harmonic_indices(1).location == locations.time_freq
    assert tfq.get_harmonic_indices(2).location == locations.time_freq
    assert tfq.time_frequencies.location == locations.time_freq
    assert np.allclose([1.0, 2.0], tfq.get_harmonic_indices(1).data)
    assert np.allclose([3.0, 3.1], tfq.get_harmonic_indices(2).data)
    assert tfq.complex_frequencies is None


def test_deep_copy_time_freq_support(velocity_acceleration):
    model = Model(velocity_acceleration)
    tf = model.metadata.time_freq_support
    copy = tf.deep_copy()
    assert np.allclose(tf.time_frequencies.data, copy.time_frequencies.data)
    assert tf.time_frequencies.scoping.ids == copy.time_frequencies.scoping.ids


def test_deep_copy_time_freq_support_harmonic():
    model = Model(examples.download_multi_harmonic_result())
    tf = model.metadata.time_freq_support
    copy = tf.deep_copy()
    assert np.allclose(tf.time_frequencies.data, copy.time_frequencies.data)
    assert np.allclose(tf.time_frequencies.scoping.ids, copy.time_frequencies.scoping.ids)
    assert tf.time_frequencies.unit == copy.time_frequencies.unit
    assert np.allclose(tf.complex_frequencies.data, copy.complex_frequencies.data)
    assert np.allclose(tf.complex_frequencies.scoping.ids, copy.complex_frequencies.scoping.ids)
    assert np.allclose(tf.rpms.data, copy.rpms.data)
    assert np.allclose(tf.rpms.scoping.ids, copy.rpms.scoping.ids)


def test_deep_copy_time_freq_support_multi_stage():
    model = Model(examples.download_multi_stage_cyclic_result())
    tf = model.metadata.time_freq_support
    copy = tf.deep_copy()
    assert np.allclose(tf.time_frequencies.data, copy.time_frequencies.data)
    assert tf.time_frequencies.scoping.ids == copy.time_frequencies.scoping.ids
    assert tf.time_frequencies.unit == copy.time_frequencies.unit
    assert np.allclose(tf.get_harmonic_indices(0).data, copy.get_harmonic_indices(0).data)
    assert tf.get_harmonic_indices(0).scoping.ids == copy.get_harmonic_indices(0).scoping.ids
    assert np.allclose(tf.get_harmonic_indices(1).data, copy.get_harmonic_indices(1).data)
    assert tf.get_harmonic_indices(1).scoping.ids == copy.get_harmonic_indices(1).scoping.ids

    assert len(tf.get_harmonic_indices(0).data) == 6
    assert len(tf.get_harmonic_indices(1).data) == 6


@conftest.raises_for_servers_version_under("3.0")
def test_operator_connect_get_output_time_freq_support(velocity_acceleration):
    model = Model(velocity_acceleration)
    tf = model.metadata.time_freq_support
    op = dpf.core.operators.utility.forward(tf)
    tfout = op.get_output(0, dpf.core.types.time_freq_support)
    assert np.allclose(tf.time_frequencies.data, tfout.time_frequencies.data)


@conftest.raises_for_servers_version_under("3.0")
def test_workflow_connect_get_output_time_freq_support(velocity_acceleration):
    model = Model(velocity_acceleration)
    tf = model.metadata.time_freq_support
    wf = dpf.core.Workflow()
    wf.progress_bar = False
    op = dpf.core.operators.utility.forward()
    wf.set_input_name("tf", op, 0)
    wf.set_output_name("tf", op, 0)
    wf.connect("tf", tf)
    tfout = wf.get_output("tf", dpf.core.types.time_freq_support)
    assert np.allclose(tf.time_frequencies.data, tfout.time_frequencies.data)


@pytest.mark.skipif(True, reason="used to check memory leaks")
def test_timefreqsupport_memory_leaks():
    import gc
    from ansys.dpf.core import start_local_server
    from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols

    config = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)
    # config = ServerConfig(protocol=CommunicationProtocols.gRPC)
    # config = ServerConfig(protocol=CommunicationProtocols.InProcess)
    server = start_local_server(config=config, as_global=False)
    for i in range(0, 2000):
        gc.collect()
        # print("\nIteration", i)
        tfq = TimeFreqSupport(server=server)
        frequencies = fields_factory.create_scalar_field(3, server=server)
        frequencies.data = [0.1, 0.32, 0.4]
        tfq.time_frequencies = frequencies
        frequencies_check = tfq.time_frequencies  # Call to get
        tfq.complex_frequencies = frequencies
        frequencies_cplx_check = tfq.complex_frequencies  # Call to get
        tfq.rpms = frequencies
        rpm_check = tfq.rpms  # Call to get
        tfq.set_harmonic_indices(frequencies)
        harm_check = tfq.get_harmonic_indices()  # Call to get


@conftest.raises_for_servers_version_under("5.0")
def test_getters_support_base(server_type):
    tfq = TimeFreqSupport(server=server_type)
    frequencies = fields_factory.create_scalar_field(3, server=server_type)
    frequencies.data = [0.1, 0.32, 0.4]
    tfq.time_frequencies = frequencies
    tfq.complex_frequencies = frequencies
    rpm = fields_factory.create_scalar_field(3, server=server_type)
    rpm.data = [0.1, 0.32, 0.4]
    tfq.rpms = rpm
    harm = fields_factory.create_scalar_field(3, server=server_type)
    harm.data = [0.1, 0.32, 0.4]
    tfq.set_harmonic_indices(harm)
    expected_props = ["time_freqs", "imaginary_freqs", "rpms", "harmonic_indices"]
    assert tfq.available_string_field_supported_properties() == []
    assert tfq.available_prop_field_supported_properties() == []
    for prop in expected_props:
        assert prop in tfq.available_field_supported_properties()
        field = tfq.field_support_by_property(prop)
        assert isinstance(field, dpf.core.Field)

    field = tfq.field_support_by_property("time_freqs")
    assert np.allclose(field.data, [0.1, 0.32, 0.4])
