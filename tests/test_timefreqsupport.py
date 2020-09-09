import os

import pytest
import numpy as np

from ansys import dpf


if 'AWP_UNIT_TEST_FILES' in os.environ:
    UNIT_TEST_PATH = os.environ['AWP_UNIT_TEST_FILES']
else:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')

# runs once per testing session
if not dpf.has_local_server():
    dpf.start_local_server()


VEL_ACC_PATH = os.path.join(UNIT_TEST_PATH, 'DataProcessing', 'rst_operators',
                            'velocity_acceleration', 'file.rst')

SIMPLE_MODEL_PATH = os.path.join(UNIT_TEST_PATH, 'DataProcessing', 'rst_operators',
                                 'simpleModel.rst')


@pytest.fixture(scope='module')
def vel_acc_model():
    return dpf.Model(VEL_ACC_PATH)


def test_get_timefreqsupport():
    dataSource = dpf.DataSources()
    dataSource.set_result_file_path(VEL_ACC_PATH)
    op = dpf.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.types.time_freq_support)
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


def test_get_frequencies_timefreqsupport():
    dataSource = dpf.DataSources()
    dataSource.set_result_file_path(VEL_ACC_PATH)
    op = dpf.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.types.time_freq_support)
    freq = res.frequencies
    assert np.allclose(freq.data, [0.02, 0.04, 0.06, 0.08, 0.1])
    assert freq.scoping.ids == [1]

def test_print_timefreqsupport():
    dataSource = dpf.DataSources()
    dataSource.set_result_file_path(VEL_ACC_PATH)
    op = dpf.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.types.time_freq_support)
    print(res)
    
def test_delete_timefreqsupport():
    dataSource = dpf.DataSources()
    dataSource.set_result_file_path(VEL_ACC_PATH)
    op = dpf.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.types.time_freq_support)
    res.__del__()
    with pytest.raises(Exception):
        res.get_frequence(0, 0)


def test_delete_auto_timefreqsupport():
    # path = unitestPath + r'\DataProcessing\rst_operators\simpleModel.rst'
    dataSource = dpf.DataSources()
    dataSource.set_result_file_path(SIMPLE_MODEL_PATH)
    op= dpf.Operator("mapdl::rst::TimeFreqSupportProvider")
    op.connect(4, dataSource)
    res=op.get_output(0, dpf.types.time_freq_support)
    res1 = dpf.TimeFreqSupport(res)
    res.__del__()
    with pytest.raises(Exception):
        res1.n_sets
