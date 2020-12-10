import pytest
import numpy as np

from ansys import dpf


@pytest.fixture()
def vel_acc_model(velocity_acceleration):
    return dpf.core.Model(velocity_acceleration)


def test_get_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
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
    assert len(timefreq.frequencies.data) == timefreq.n_sets
    expected_data = [0.02, 0.04, 0.06, 0.08, 0.1]
    assert np.allclose(expected_data, timefreq.frequencies.data)


def test_get_frequencies_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    freq = res.frequencies
    assert np.allclose(freq.data, [0.02, 0.04, 0.06, 0.08, 0.1])
    assert freq.scoping.ids == [1]


def test_print_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    assert 'Number of sets: 5' in str(res)
    assert 'Time (s)' in str(res)
    assert 'Loadstep' in str(res)
    assert 'Substep' in str(res)


def test_delete_timefreqsupport(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.time_freq_support)
    res.__del__()
    with pytest.raises(Exception):
        res.get_frequence(0, 0)


def test_delete_auto_timefreqsupport(simple_rst):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(simple_rst)
    op= dpf.core.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res=op.get_output(0, dpf.core.types.time_freq_support)
    res1 = dpf.core.TimeFreqSupport(res._message)
    res.__del__()
    with pytest.raises(Exception):
        res1.n_sets
