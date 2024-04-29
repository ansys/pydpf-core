import ansys.dpf.core as dpf


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
