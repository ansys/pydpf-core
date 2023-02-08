from ansys.dpf import core as dpf
import conftest


@conftest.raises_for_servers_version_under("5.0")
def test_set_get_generic_support(server_type):
    support = dpf.GenericSupport("phase", server=server_type)
    field = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    support.set_support_of_property("viscosity", field)
    field = dpf.StringField(server=server_type)
    support.set_support_of_property("names", field)
    field = dpf.PropertyField(location="phase", nature=dpf.natures.scalar, server=server_type)
    support.set_support_of_property("type", field)
    field = dpf.PropertyField(location="phase", nature=dpf.natures.scalar, server=server_type)
    support.set_support_of_property("miscibility", field)
    assert support.available_field_supported_properties() == ["viscosity"]
    assert support.available_string_field_supported_properties() == ["names"]
    assert "type" in support.available_prop_field_supported_properties()
    assert "miscibility" in support.available_prop_field_supported_properties()
    field = support.field_support_by_property("viscosity")
    assert isinstance(field, dpf.Field)
    field = support.field_support_by_property("dummy")
    assert field is None
    field = support.string_field_support_by_property("names")
    assert isinstance(field, dpf.StringField)
    field = support.string_field_support_by_property("dummy")
    assert field is None
    field = support.prop_field_support_by_property("type")
    assert isinstance(field, dpf.PropertyField)
    field = support.prop_field_support_by_property("dummy")
    assert field is None
    field = support.prop_field_support_by_property("miscibility")
    assert isinstance(field, dpf.PropertyField)
