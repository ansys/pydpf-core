import os

import pytest
from ansys import dpf

if 'AWP_UNIT_TEST_FILES' in os.environ:
    unit_test_files = os.environ['AWP_UNIT_TEST_FILES']
else:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')

TEST_FILE_PATH = os.path.join(unit_test_files, 'DataProcessing', 'rst_operators',
                              'velocity_acceleration', 'file.rst')

if not dpf.core.has_local_server():
    dpf.core.start_local_server()


@pytest.fixture(scope='module')
def model():
    return dpf.core.Model(TEST_FILE_PATH)


def test_get_resultinfo_no_model():
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(TEST_FILE_PATH)
    op = dpf.core.Operator("mapdl::rst::ResultInfoProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.result_info)
    assert res.analysis_type == "static"
    assert res.n_results == 14
    assert res.unit_system == 'Metric (m, kg, N, s, V, A)'
    assert res.physics_type == "mecanic"


def test_get_resultinfo(model):
    res = model.metadata.result_info
    assert 'Static analysis' in str(res)
    assert res.analysis_type == "static"
    assert res.n_results == 14
    assert res.unit_system == 'Metric (m, kg, N, s, V, A)'
    assert res.physics_type == "mecanic"
    
def test_byitem_resultinfo(model):
    res = model.metadata.result_info
    assert res['stress']!=None
    assert res[0]!=None


def test_get_result_resultinfo_from_index(model):
    res = model.metadata.result_info[2]
    assert res.name == "acceleration"
    assert res.n_components == 3
    assert res.dimensionality == "vector"
    assert res.homogeneity == "acceleration"
    assert res.unit == "m/s^2"
    assert res.name == "acceleration"

def test_print_result_info(model):
    print(model.metadata.result_info)

def test_delete_resultinfo():
    new_model = dpf.core.Model(TEST_FILE_PATH)
    res = new_model.metadata.result_info
    res.__del__()
    with pytest.raises(Exception):
        res.n_results


def test_delete_auto_resultinfo():
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(TEST_FILE_PATH)
    op = dpf.core.Operator("mapdl::rst::ResultInfoProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.result_info)
    res_shallow_copy = dpf.core.ResultInfo(res)
    del res
    with pytest.raises(Exception):
        res_shallow_copy.n_results
