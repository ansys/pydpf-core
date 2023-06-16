from ansys.dpf import core as dpf
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
)
import pytest

@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_create_any(server_type):
    field = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    any = dpf.Any.new_from(field)
    assert any._internal_obj is not None


# @pytest.mark.skipif(
#     not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
# )
# def test_cast_int_any(server_type):
#     entity = 42
#     any = dpf.Any.new_from(entity, server_type)
#     new_entity = any.cast()
#     assert 42 == new_entity
#
#
# @pytest.mark.skipif(
#     not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
# )
# def test_cast_string_any(server_type):
#     entity = "hello world"
#     any = dpf.Any.new_from(entity, server_type)
#     new_entity = any.cast()
#     assert "hello world" == new_entity
#
#
# @pytest.mark.skipif(
#     not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
# )
# def test_cast_float_any(server_type):
#     entity = 4.2
#     any = dpf.Any.new_from(entity, server_type)
#     new_entity = any.cast()
#     assert 4.2 == new_entity
#
#
# @pytest.mark.skipif(
#     not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
# )
# def test_cast_field_any(server_type):
#     entity = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
#     any = dpf.Any.new_from(entity)
#     new_entity = any.cast()
#     assert entity.location == new_entity.location
#
#
# @pytest.mark.skipif(
#     not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
# )
# def test_cast_property_field_any(server_type):
#     entity = dpf.PropertyField(nature=dpf.natures.scalar, server=server_type)
#     entity.data = [20, 30, 50, 70, 80]
#     any = dpf.Any.new_from(entity)
#     new_entity = any.cast()
#     assert entity.data.all() == new_entity.data.all()
#
#
# @pytest.mark.skipif(
#     not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
# )
# def test_cast_string_field_any(server_type):
#     entity = dpf.StringField(server=server_type)
#     entity.data = ["hello", "world"]
#     any = dpf.Any.new_from(entity)
#     new_entity = any.cast()
#     assert entity.get_entity_data(0)[0] == "hello"
#
#
# @pytest.mark.skipif(
#     not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
# )
# def test_cast_generic_data_container(server_type):
#     entity = dpf.GenericDataContainer(server=server_type)
#     field = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
#     entity.set_property("field", field)
#
#     any = dpf.Any.new_from(entity)
#     new_entity = any.cast()
#
#     new_field = new_entity.get_property("field", dpf.Field)
#
#     assert field.location == new_field.location
