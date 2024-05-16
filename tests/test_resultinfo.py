import pytest

from ansys import dpf
from ansys.dpf.core import Model
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_1,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0,
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
    if not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_1:
        assert res.n_results == 14
    else:
        assert res.n_results == 15
    assert "m, kg, N, s, V, A" in res.unit_system
    assert res.physics_type == mechanical


def test_get_resultinfo(model):
    res = model.metadata.result_info
    assert res.analysis_type == "static"
    if not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_1:
        assert res.n_results == 14
    else:
        assert res.n_results == 15
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
    assert "unsaved_project--Static" in res.main_title
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


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available with CFF starting 7.0"
)
def test_print_available_result_with_qualifiers(cfx_heating_coil, server_type):
    model = Model(cfx_heating_coil(server=server_type), server=server_type)
    ref = """DPF Result
----------
specific_heat
Operator name: "CP"
Number of components: 1
Dimensionality: scalar
Homogeneity: specific_heat
Units: J/kg*K^-1
Location: Nodal
Available qualifier labels:"""  # noqa: E501
    ref2 = "'phase': 2"
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0:
        ref3 = "'zone': 11"
    else:
        ref3 = "'zone': 5"
    ar = model.metadata.result_info.available_results[0]
    got = str(ar)
    assert ref in got
    assert ref2 in got
    assert ref3 in got
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0:
        assert len(ar.qualifier_combinations) == 18
    else:
        assert len(ar.qualifier_combinations) == 20

@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available with CFF starting 7.0"
)
def test_print_result_info_with_qualifiers(cfx_heating_coil, server_type):
    model = Model(cfx_heating_coil(server=server_type), server=server_type)
    ref = """Static analysis
Unit system: SI: m, kg, N, s, V, A, K
Physics Type: Fluid
Available results:
     -  specific_heat: Nodal Specific Heat
     -  epsilon: Nodal Epsilon        
     -  enthalpy: Nodal Enthalpy      
     -  turbulent_kinetic_energy: Nodal Turbulent Kinetic Energy
     -  thermal_conductivity: Nodal Thermal Conductivity
     -  dynamic_viscosity: Nodal Dynamic Viscosity
     -  turbulent_viscosity: Nodal Turbulent Viscosity
     -  static_pressure: Nodal Static Pressure
     -  total_pressure: Nodal Total Pressure
     -  density: Nodal Density        
     -  entropy: Nodal Entropy        
     -  temperature: Nodal Temperature
     -  total_temperature: Nodal Total Temperature
     -  velocity: Nodal Velocity      
Available qualifier labels:"""  # noqa
    assert ref in str(model.metadata.result_info)


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


def test_create_result_info(server_type):
    from ansys.dpf.core.available_result import Homogeneity
    if not server_type.has_client():
        result_info = dpf.core.ResultInfo(
            analysis_type=dpf.core.result_info.analysis_types.static,
            physics_type=dpf.core.result_info.physics_types.mechanical,
            server=server_type
        )
        result_info.add_result(
            operator_name="operator_name",
            scripting_name="scripting_name",
            homogeneity=Homogeneity.temperature,
            location=dpf.core.locations.nodal,
            nature=dpf.core.natures.scalar,
            dimensions=None,
            description="description",
        )
        if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0:
            ref = """Static analysis
Unit system: Undefined
Physics Type: Mechanical
Available results:
     -  scripting_name: Nodal Scripting Name
"""
        elif SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0:
            ref = """Static analysis
Unit system: 
Physics Type: Mechanical
Available results:
     -  scripting_name: Nodal Scripting Name
"""
        else:
            ref = """Static analysis
Unit system: 
Physics Type: Mecanic
Available results:
     -  scripting_name: Nodal Scripting Name
"""
        assert str(result_info) == ref
        with pytest.raises(ValueError, match="requires"):
            _ = dpf.core.ResultInfo()
    else:
        with pytest.raises(NotImplementedError, match="Cannot create a new ResultInfo via gRPC."):
            _ = dpf.core.ResultInfo(
                analysis_type=dpf.core.result_info.analysis_types.static,
                physics_type=dpf.core.result_info.physics_types.mechanical,
                server=server_type
            )


def test_result_info_add_result(model):
    from ansys.dpf.core.available_result import Homogeneity
    res = model.metadata.result_info
    if not model._server.has_client():
        res.add_result(
                operator_name="operator_name",
                scripting_name="scripting_name",
                homogeneity=Homogeneity.temperature,
                location=dpf.core.locations.nodal,
                nature=dpf.core.natures.scalar,
                dimensions=None,
                description="description",
            )
    else:
        with pytest.raises(
                NotImplementedError,
                match="Cannot add a result to a ResultInfo via gRPC."
        ):
            res.add_result(
                    operator_name="operator_name",
                    scripting_name="scripting_name",
                    homogeneity=Homogeneity.temperature,
                    location=dpf.core.locations.nodal,
                    nature=dpf.core.natures.scalar,
                    dimensions=None,
                    description="description",
                )

