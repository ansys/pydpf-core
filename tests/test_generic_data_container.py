from ansys.dpf import core as dpf


def test_create_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)
    assert gdc._internal_obj is not None


def test_set_get_property_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)
    entity = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    gdc.set_property("viscosity", entity)
    new_entity = gdc.get_property("viscosity", dpf.Field)
    assert entity.location == new_entity.location
