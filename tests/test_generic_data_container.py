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


def test_get_property_description_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)
    entity = 42
    gdc.set_property("my-int", entity)
    new_entity = gdc.get_property("my-int", int)
    assert 42 == new_entity

    entity = 4.2
    gdc.set_property("my-float", entity)
    new_entity = gdc.get_property("my-float", float)
    assert 4.2 == new_entity

    entity = "hello world"
    gdc.set_property("my-string", entity)
    new_entity = gdc.get_property("my-string", str)
    assert "hello world" == new_entity

    property_description = gdc.get_property_description()

    assert 3 == len(property_description)
    assert property_description == {"my-float":"double", "my-int":"int32", "my-string":"string"}
