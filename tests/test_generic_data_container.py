from ansys import dpf


def test_create_generic_data_container(server_type):
    gdc = dpf.core.GenericDataContainer(server=server_type)
    assert gdc._internal_obj is not None


def test_get_property_generic_data_container(server_type):
    gdc = dpf.core.GenericDataContainer(server=server_type)
    field = gdc.get_property("property", dpf.core.PropertyField)
    assert field is not None
