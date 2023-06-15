from ansys.dpf import core as dpf
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
)
import pytest


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_create_mesh_info(server_type):
    mesh_info = dpf.MeshInfo(server=server_type)
    assert mesh_info._internal_obj is not None


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)

def test_set_get_num_of(server_type):
    """ Number of nodes """
    mesh_info = dpf.MeshInfo(server=server_type)
    num_nodes = 189
    mesh_info.set_number_nodes(189)
    assert mesh_info.get_number_nodes() == num_nodes
    """ Number of elements """
    num_elements = 2
    mesh_info.set_number_elements(2)
    assert mesh_info.get_number_elements() == num_elements

def test_set_get_property_mesh_info(server_type):
    """ Scoping """
    mesh_info = dpf.MeshInfo(server=server_type)
    entity_scoping = dpf.Scoping()
    expected_ids = {3, 2, 1}
    entity_scoping.set_id(expected_ids)
    mesh_info.set_property("my-property00", entity_scoping)
    result_scoping = mesh_info.get_property("my-property00", dpf.Scoping)
    assert result_scoping.ids == entity_scoping.ids
    """ Field """
    entity_field = dpf.Field()
    mesh_info.set_property("my-property01", entity_field)
    result_field = mesh_info.get_property("my-property01", dpf.Field)
    assert result_field.component_count == entity_field.component_count
    """ MeshedRegion """
    entity_meshedregion = dpf.MeshedRegion()
    mesh_info.set_property("my-property02", entity_meshedregion)
    result_meshedregion = mesh_info.get_property("my-property02", dpf.MeshedRegion)
    assert result_meshedregion.elements == entity_meshedregion.elements

@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_set_get_splittable_by_mesh_info(server_type):
    mesh_info = dpf.MeshInfo(server=server_type)
    entity_splittable = dpf.StringField()
    expected_splittable = ["split_01", "split_02", "split_03"]
    entity_splittable._set_data(expected_splittable)
    mesh_info.set_splittable_by(entity_splittable)
    result_splittable = mesh_info.get_splittable_by()
    for i, strings in enumerate(expected_splittable):
        assert result_splittable.get_entity_data_by_id(i) == expected_splittable[i]

def test_set_get_splittable_by_mesh_info(server_type):
    mesh_info = dpf.MeshInfo(server=server_type)
    entity_available = dpf.Scoping()
    expected_available = [3, 2, 1]
    entity_available.set_id(expected_available)
    mesh_info.set_available_elem_types(entity_available)
    result_available = mesh_info.get_available_elem_types()
    for i, strings in enumerate(expected_available):
        assert result_available.id(i) == expected_available[i]
