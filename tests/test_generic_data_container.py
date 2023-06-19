from ansys.dpf import core as dpf
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
)
import pytest


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_create_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)
    assert gdc._internal_obj is not None


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_set_get_property_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer()
    entity = dpf.Scoping()
    gdc.set_property("viscosity", entity)
    new_entity = gdc.get_property("viscosity", dpf.Scoping)
    assert entity.location == new_entity.location


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
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

    entity = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    gdc.set_property("my-field", entity)

    property_description = gdc.get_property_description()

    assert 4 == len(property_description)
    assert property_description == {
        "my-float": "float",
        "my-int": "int",
        "my-string": "str",
        "my-field": "Field",
    }

def test_get_property_description_scoping_generic_data_container():
    gdc = dpf.GenericDataContainer()

    scoping = dpf.Scoping()
    scoping.location = dpf.locations.elemental
    scoping.ids = [1, 2]
    gdc.set_property("my-scoping", scoping)

    property_description = gdc.get_property_description()

    assert 1 == len(property_description)
    assert property_description == {
        "my-scoping": "Scoping",
    }

def test_get_property_description_meshed_region_generic_data_container():
    gdc = dpf.GenericDataContainer()

    meshed_region = dpf.MeshedRegion()
    gdc.set_property("my-meshed_region", meshed_region)

    property_description = gdc.get_property_description()

    assert 1 == len(property_description)
    assert property_description == {
        "my-meshed_region": "MeshedRegion",
    }