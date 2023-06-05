import pytest

from ansys import dpf
from ansys.dpf.core import Model
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0

if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0:
    mechanical = "mechanical"
else:
    mechanical = "mecanic"


@pytest.fixture()
def model(velocity_acceleration, server_type):
    return dpf.core.Model(velocity_acceleration, server=server_type)


def test_get_resultinfo_no_model(velocity_acceleration, server_type):
    dataSource = dpf.core.DataSources(velocity_acceleration, server=server_type)
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::ResultInfoProvider", server=server_type)
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.result_info)
    assert res.analysis_type == "static"
    assert res.n_results == 14
    assert "m, kg, N, s, V, A" in res.unit_system
    assert res.physics_type == mechanical


def test_get_resultinfo(model):
    res = model.metadata.result_info
    assert res.analysis_type == "static"
    assert res.n_results == 14
    assert "m, kg, N, s, V, A" in res.unit_system
    assert res.physics_type == mechanical
    assert "Static analysis" in str(res)


def test_get_resultinfo_2(simple_bar, server_type):
    model = Model(simple_bar, server=server_type)
    res = model.metadata.result_info
    assert res.unit_system_name == "MKS: m, kg, N, s, V, A, degC"
    assert res.solver_version == "19.3"
    assert res.solver_date == 20181005
    assert res.solver_time == 170340
    assert res.user_name == "afaure"
    assert res.job_name == "file_Static22_0"
    assert res.product_name == "FULL"
    assert res.main_title == "unsaved_project--Static"
    assert res.cyclic_support is None


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
    assert res.qualifiers == []


def test_print_result_info(model):
    print(model.metadata.result_info)


@pytest.mark.skipif(True, reason="Used to test memory leaks")
def test_result_info_memory_leaks(model):
    import gc

    for i in range(1000):
        gc.collect()
        metadata = model.metadata
        res = metadata.result_info
        # Still leaking, but maybe from the Operator.connect
        # in Metadata._load_result_info()
        u = res.unit_system_name
        c = res.cyclic_support
        # v = res.solver_version
        # date = res.solver_date
        # time = res.solver_time
        # na = res.user_name
        # j = res.job_name
        # n = res.product_name
        # t = res.main_title
