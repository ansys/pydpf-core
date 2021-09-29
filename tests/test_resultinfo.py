import pytest
from ansys import dpf
from ansys.dpf.core import Model


@pytest.fixture()
def model(velocity_acceleration):
    return dpf.core.Model(velocity_acceleration)


def test_get_resultinfo_no_model(velocity_acceleration):
    dataSource = dpf.core.DataSources(velocity_acceleration)
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::ResultInfoProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.result_info)
    assert res.analysis_type == "static"
    assert res.n_results == 14
    assert res.unit_system == "Metric (m, kg, N, s, V, A)"
    assert res.physics_type == "mecanic"


def test_get_resultinfo(model):
    res = model.metadata.result_info
    assert "Analysis: static" in str(res)
    assert res.analysis_type == "static"
    assert res.n_results == 14
    assert res.unit_system == "Metric (m, kg, N, s, V, A)"
    assert res.physics_type == "mecanic"


def test_get_resultinfo_2(simple_bar):
    model = Model(simple_bar)
    res = model.metadata.result_info
    assert res.unit_system_name == "MKS: m, kg, N, s, V, A, degC"
    assert res.solver_version == "19.3"
    assert res.solver_date == 20181005
    assert res.solver_time == 170340
    assert res.user_name == "afaure"
    assert res.job_name == "file_Static22_0"
    assert res.product_name == "FULL"
    assert res.main_title == "unsaved_project--Static"


def test_byitem_resultinfo(model):
    res = model.metadata.result_info
    assert res["stress"] is not None
    assert res[0] is not None


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


def test_delete_resultinfo(velocity_acceleration):
    new_model = dpf.core.Model(velocity_acceleration)
    res = new_model.metadata.result_info
    res.__del__()
    with pytest.raises(Exception):
        res.n_results


def test_delete_auto_resultinfo(velocity_acceleration):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::ResultInfoProvider")
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.result_info)
    res_shallow_copy = dpf.core.ResultInfo(res)
    del res
    with pytest.raises(Exception):
        res_shallow_copy.n_results
