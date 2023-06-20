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
    assert mesh_info is not None


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_set_get_num_of(server_type):
    mesh_info = dpf.MeshInfo(server=server_type)
    """Number of nodes"""
    num_nodes = 189
    mesh_info.set_number_nodes(189)
    assert mesh_info.get_number_nodes() == num_nodes
    """ Number of elements """
    num_elements = 2
    mesh_info.set_number_elements(2)
    assert mesh_info.get_number_elements() == num_elements


def test_set_get_property_mesh_info(server_type):
    mesh_info = dpf.MeshInfo(server=server_type)
    """Scoping"""
    entity_scoping = dpf.Scoping()
    expected_ids = [1, 2, 3]
    entity_scoping._set_ids(expected_ids)
    mesh_info.set_property("my-property00", entity_scoping)
    result_scoping = mesh_info.get_property("my-property00", dpf.Scoping)
    for x in range(len(expected_ids)):
        assert result_scoping.id(x) == entity_scoping.id(x)
    """ Field """
    entity_field = dpf.Field()
    mesh_info.set_property("my-property01", entity_field)
    result_field = mesh_info.get_property("my-property01", dpf.Field)
    assert result_field.component_count == entity_field.component_count
    """ MeshedRegion """
    entity_meshedregion = dpf.MeshedRegion()
    mesh_info.set_property("my-property02", entity_meshedregion)
    result_meshedregion = mesh_info.get_property("my-property02", dpf.MeshedRegion)
    assert result_meshedregion.nodes.n_nodes == entity_meshedregion.nodes.n_nodes


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_set_get_splittable_by_mesh_info(server_type):
    mesh_info = dpf.MeshInfo(server=server_type)
    entity_splittable = dpf.StringField()
    expected_splittable = {"split_01", "split_02", "split_03"}
    entity_splittable._set_data(expected_splittable)
    mesh_info.set_splittable_by(entity_splittable)
    result_splittable = mesh_info.get_splittable_by()
    for i, strings in enumerate(expected_splittable):
        assert result_splittable.get_entity_data_by_id(i) == entity_splittable.get_entity_data_by_id(i)


def test_set_get_available_elem_types_mesh_info(server_type):
    mesh_info = dpf.MeshInfo(server=server_type)
    expected_available = [1, 2, 3]
    entity_available = dpf.Scoping()
    entity_available._set_ids(expected_available)
    mesh_info.set_available_elem_types(entity_available)
    result_available = mesh_info.get_available_elem_types()
    for x in range(len(expected_available)):
        assert result_available.id(x) == entity_available.id(x)

def test_output_mesh_info_provider():
    dpf.load_library(r"C:\Program Files\ANSYS Inc\v241\dpf\plugins\dpf_cff\Ans.Dpf.CFF.dll", "cff")

    ds = dpf.DataSources()
    ds.set_result_file_path(r"D:\AnsysDev\plugins\Ans.Dpf.CFF\source\Ans.Dpf.CFFTest\test_models\fluent\2D\FFF.cas.h5", "cas")

    mesh_info = dpf.operators.metadata.mesh_info_provider()
    mesh_info.inputs.data_sources(ds)
    mesh_info_out = mesh_info.outputs.generic_data_container()

    """************************ NUMBER OF CELLS/FACES/ZONES ************************"""

    num_cells = mesh_info_out.get_property("num_cells", int)
    num_faces = mesh_info_out.get_property("num_faces", int)
    num_nodes = mesh_info_out.get_property("num_nodes", int)

    assert num_cells == 1344
    assert num_faces == 2773
    assert num_nodes == 1430

    """************************ BODIES ************************"""

    """************ Name ************"""
    body_names = mesh_info_out.get_property("body_name", dpf.StringField)

    body_names_value = body_names._get_data()

    assert len(body_names_value) == 1
    assert body_names_value[0] == "fluid-1"

    """************ Scoping ************"""
    body_scoping = mesh_info_out.get_property("body_scoping", dpf.Scoping)

    assert body_scoping.size == 1
    assert body_scoping[0] == 1

    """************************ ZONES ************************"""

    """************ Name ************"""
    zone_names = mesh_info_out.get_property("zone_name", dpf.StringField)

    zone_names_value = zone_names._get_data()

    assert zone_names_value.size == 6
    assert zone_names_value[0] == "fluid-1"
    assert zone_names_value[1] == "interior-3"
    assert zone_names_value[2] == "symmetry-4"
    assert zone_names_value[3] == "pressure-outlet-5"
    assert zone_names_value[5] == "velocity-inlet-7"

    """************ Scoping ************"""
    zone_scoping = mesh_info_out.get_property("zone_scoping", dpf.Scoping)

    assert zone_scoping.size == 6
    assert zone_scoping[0] == 1
    assert zone_scoping[1] == 3
    assert zone_scoping[2] == 4
    assert zone_scoping[3] == 5
    assert zone_scoping[5] == 7

    """************ Element ************"""
    zone_elements = mesh_info_out.get_property("num_elem_zone", dpf.PropertyField)

    number_of_element_in_zone_value = zone_elements._get_data()

    assert number_of_element_in_zone_value.size == 6
    assert number_of_element_in_zone_value[0] == 1344
    assert number_of_element_in_zone_value[1] == 2603
    assert number_of_element_in_zone_value[2] == 64
    assert number_of_element_in_zone_value[3] == 21
    assert number_of_element_in_zone_value[5] == 15

    """************ CELL ZONES ************"""

    """************ Name ************"""
    cell_zone_name = mesh_info_out.get_property("cell_zone_names", dpf.StringField)

    cell_zone_name_value = cell_zone_name._get_data()

    assert cell_zone_name_value.size == 1
    assert cell_zone_name_value[0] == "fluid-1"

    """************ Scoping ************"""
    cell_zone_scoping = mesh_info_out.get_property("cell_zone_scoping", dpf.Scoping)

    assert cell_zone_scoping.size == 1
    assert cell_zone_scoping[0] == 1

    """************ Element ************"""
    cell_zone_elements = mesh_info_out.get_property("cell_zone_elements", dpf.PropertyField)

    cell_zone_elements_value = cell_zone_elements._get_data()

    assert cell_zone_elements_value.size == 1
    assert cell_zone_elements_value[0] == 1344

    """************ FACE ZONES ************"""

    """************ Name ************"""
    face_zone_names = mesh_info_out.get_property("face_zone_names", dpf.StringField)

    face_zone_names_value = face_zone_names._get_data()

    assert face_zone_names_value.size == 5
    assert face_zone_names_value[0] == "interior-3"
    assert face_zone_names_value[1] == "symmetry-4"
    assert face_zone_names_value[2] == "pressure-outlet-5"
    assert face_zone_names_value[3] == "wall-6"
    assert face_zone_names_value[4] == "velocity-inlet-7"

    """************ Scoping ************"""
    face_zone_scoping = mesh_info_out.get_property("face_zone_scoping", dpf.Scoping)

    assert face_zone_scoping.size == 5
    assert face_zone_scoping[0] == 3
    assert face_zone_scoping[1] == 4
    assert face_zone_scoping[2] == 5
    assert face_zone_scoping[3] == 6
    assert face_zone_scoping[4] == 7

    """************ Element ************"""
    face_zone_elements = mesh_info_out.get_property("face_zone_elements", dpf.PropertyField)

    face_zone_elements_value = face_zone_elements._get_data()

    assert face_zone_elements_value.size == 5
    assert face_zone_elements_value[0] == 2603
    assert face_zone_elements_value[1] == 64
    assert face_zone_elements_value[2] == 21
    assert face_zone_elements_value[3] == 70
    assert face_zone_elements_value[4] == 15