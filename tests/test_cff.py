import pytest
import conftest
from ansys.dpf import core as dpf


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
def test_cff_model(server_type, fluent_multi_species):
    ds = fluent_multi_species(server_type)
    model = dpf.Model(ds, server=server_type)
    assert "Fluid" in str(model)
    assert model is not None
    mesh = model.metadata.meshed_region
    assert "faces" in str(mesh)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
@pytest.mark.parametrize(
    "result_name",
    [
        "specific_heat",
        "epsilon",
        "enthalpy",
        "turbulent_kinetic_energy",
        "thermal_conductivity",
        "dynamic_viscosity",
        "turbulent_viscosity",
        "static_pressure",
        "total_pressure",
        "density",
        "entropy",
        "wall_shear_stress",
        "temperature",
        "total_temperature",
        "velocity",
    ],
)
def test_results_cfx(cfx_heating_coil, result_name, server_type):
    model = dpf.Model(cfx_heating_coil(server=server_type), server=server_type)
    print(model)
    result_op = getattr(model.results, result_name)()
    result = result_op.eval()
    assert isinstance(result, dpf.FieldsContainer)
    result_op.connect(1000, {"phase": 2})
    result = result_op.eval()
    assert isinstance(result, dpf.FieldsContainer)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
@pytest.mark.parametrize(
    "result_name",
    [
        "enthalpy",
        "mass_flow_rate",
        "static_pressure",
        "surface_heat_rate",
        "density",
        "temperature",
        "velocity",
    ],
)
def test_results_fluent(fluent_mixing_elbow_steady_state, result_name, server_type):
    model = dpf.Model(fluent_mixing_elbow_steady_state(server=server_type), server=server_type)
    result_op = getattr(model.results, result_name)()
    result = result_op.eval()
    assert isinstance(result, dpf.FieldsContainer)
    result_op.connect(1000, {"phase": 1})
    result = result_op.eval()
    assert isinstance(result, dpf.FieldsContainer)
