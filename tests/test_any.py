import pytest

import conftest
from ansys.dpf import core as dpf


@conftest.raises_for_servers_version_under("7.0")
def test_create_any(server_type):
    field = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    any_dpf = dpf.Any.new_from(field)

    assert any_dpf._internal_obj is not None


@conftest.raises_for_servers_version_under("7.0")
def test_cast_int_any(server_type):
    entity = 42
    any_dpf = dpf.Any.new_from(entity, server_type)
    new_entity = any_dpf.cast()
    assert 42 == new_entity


@conftest.raises_for_servers_version_under("7.0")
def test_cast_string_any(server_type):
    entity = "hello world"
    any_dpf = dpf.Any.new_from(entity, server_type)
    new_entity = any_dpf.cast()
    assert "hello world" == new_entity


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0,
    reason="for_each not implemented below 8.0",
)
def test_cast_bytes_any(server_type):
    entity = b"hello world"
    any_dpf = dpf.Any.new_from(entity, server_type)
    new_entity = any_dpf.cast()
    assert b"hello world" == new_entity


@conftest.raises_for_servers_version_under("7.0")
def test_cast_float_any(server_type):
    entity = 4.2
    any_dpf = dpf.Any.new_from(entity, server_type)
    new_entity = any_dpf.cast()
    assert 4.2 == new_entity


@conftest.raises_for_servers_version_under("7.0")
def test_cast_field_any(server_type):
    entity = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()
    assert entity.location == new_entity.location


@conftest.raises_for_servers_version_under("7.0")
def test_cast_property_field_any(server_type):
    entity = dpf.PropertyField(nature=dpf.natures.scalar, server=server_type)
    entity.data = [20, 30, 50, 70, 80]
    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()
    assert entity.data.all() == new_entity.data.all()


@conftest.raises_for_servers_version_under("7.0")
def test_cast_string_field_any(server_type):
    list_ids = [1, 2]
    scop = dpf.Scoping(ids=list_ids, server=server_type)
    entity = dpf.StringField(server=server_type)
    entity.scoping = scop
    entity.data = ["hello", "world"]
    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()

    assert entity.data == new_entity.data


@conftest.raises_for_servers_version_under("7.0")
def test_cast_generic_data_container_any(server_type):
    entity = dpf.GenericDataContainer(server=server_type)
    field = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    entity.set_property("field", field)

    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()

    new_field = new_entity.get_property("field")

    assert field.location == new_field.location


@conftest.raises_for_servers_version_under("7.0")
def test_cast_scoping_any(server_type):
    entity = dpf.Scoping(server=server_type, location="phase")
    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()

    assert entity.location == new_entity.location
