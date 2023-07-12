import platform
import pytest

from ansys import dpf
from ansys.dpf.core import Model
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
)

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
    str(model.metadata.result_info)


def test_repr_available_results_list(model):
    ar = model.metadata.result_info.available_results
    assert type(ar) is list
    assert all([type(r) is dpf.core.result_info.available_result.AvailableResult for r in ar])
    assert dpf.core.result_info.available_result.AvailableResult.__name__ in str(ar)


@pytest.mark.skipif(platform.system() == "Linux", reason="CFF not available for Linux InProcess.")
@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available with CFF starting 7.0"
)
def test_print_available_result_with_qualifiers(cfx_heating_coil):
    model = Model(cfx_heating_coil)
    ref = """DPF Result
----------
specific_heat
Operator name: "CP"
Number of components: 1
Dimensionality: scalar
Homogeneity: specific_heat
Units: j/kg*k^-1
Location: Nodal
Available qualifier labels:
  - phase: Water at 25 C (2), Copper (3)
  - zone: Default 1 (5), ZN1/FS1 (9), ZN1/FS2 (10), ZN1/FS3 (11), ZN1/FS4 (12), ZN1/FS5 (13), ZN1/FS6 (14), ZN1/FS7 (15), ZN1/FS8 (16), ZN1/FS9 (17), ZN1/FS10 (18), heater (8), ZN2/FS1 (19), ZN2/FS2 (20), ZN2/FS3 (21), ZN2/FS4 (22), ZN2/FS5 (23), ZN2/FS6 (24), ZN2/FS7 (25), ZN2/FS8 (26)
Available qualifier combinations:
  {'phase': 2, 'zone': 5}
  {'phase': 2, 'zone': 9}
  {'phase': 2, 'zone': 10}
  {'phase': 2, 'zone': 11}
  {'phase': 2, 'zone': 12}
  {'phase': 2, 'zone': 13}
  {'phase': 2, 'zone': 14}
  {'phase': 2, 'zone': 15}
  {'phase': 2, 'zone': 16}
  {'phase': 2, 'zone': 17}
  {'phase': 2, 'zone': 18}
  {'phase': 3, 'zone': 8}
  {'phase': 3, 'zone': 19}
  {'phase': 3, 'zone': 20}
  {'phase': 3, 'zone': 21}
  {'phase': 3, 'zone': 22}
  {'phase': 3, 'zone': 23}
  {'phase': 3, 'zone': 24}
  {'phase': 3, 'zone': 25}
  {'phase': 3, 'zone': 26}"""  # noqa: E501
    assert ref in str(model.metadata.result_info.available_results[0])


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
