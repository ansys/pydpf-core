import conftest
import pytest
import ansys.dpf.core as dpf


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_9_0,
    reason="Elemental mass operator not functional before 9.0,",
)
def test_operator_elemental_mass_rst(allkindofcomplexity):
    model = dpf.Model(allkindofcomplexity)
    op = dpf.operators.result.elemental_mass(data_sources=model)
    fc = op.eval()
    assert len(fc) == 1
    field: dpf.Field = fc[0]
    assert field.scoping.size == 9271
    assert field.component_count == 1
    assert field.location == dpf.locations.elemental
    assert field.unit == "kg"
