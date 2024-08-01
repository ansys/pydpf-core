import pytest
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_9_1
from ansys.dpf import core as dpf


@pytest.mark.skipif(
    condition=not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_9_1,
    reason="operator available with DPF 9.1 (2025.1.pre1)"
)
def test_cff_boundary_conditions_provider(server_type, cfx_heating_coil):
    model = dpf.Model(cfx_heating_coil())
    bcp = model.operator("cff::cas::boundary_conditions_provider")
    bc = bcp.get_output(0, output_type=dpf.GenericDataContainersCollection)
    assert isinstance(bc, dpf.CollectionBase)
    assert str(bc) == "Collection of 6 GenericDataContainer"
    b: dpf.GenericDataContainer = bc[0]
    assert isinstance(b, dpf.GenericDataContainer)
    assert b.get_property("name") == "Default 1 Side1 Boundary1"
    assert b.get_property("type") == "INTERFACE"
