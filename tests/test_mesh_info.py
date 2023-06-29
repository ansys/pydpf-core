import ansys.dpf.core.generic_data_container
from ansys.dpf import core as dpf
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
)
import pytest
from ansys.dpf.core import examples
from ansys.dpf.core import Model


@pytest.fixture()
def model(fluent_axial_comp, server_clayer):
    model = Model(fluent_axial_comp, server=server_clayer)
    return model


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_create_mesh_info(server_clayer):
    mesh_info = dpf.MeshInfo(server=server_clayer)
    assert mesh_info is not None


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_mesh_info_generic_data_container_getter(model):
    mesh_info = model.metadata.mesh_info
    gdc = mesh_info.generic_data_container
    assert type(gdc) is ansys.dpf.core.generic_data_container.GenericDataContainer


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_mesh_info_generic_data_container_setter(model):
    mesh_info = model.metadata.mesh_info
    gdc = mesh_info.generic_data_container
    gdc.set_property("property_name_00", 0)
    mesh_info.generic_data_container = gdc
    assert mesh_info.generic_data_container == gdc
    with pytest.raises(ValueError) as e:
        mesh_info.generic_data_container = "Wrong type"
        assert "Input value must be a GenericDataContainer." in e


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_set_get_num_of(server_clayer):
    mesh_info = dpf.MeshInfo(server=server_clayer)
    """Number of nodes"""
    num_nodes = 189
    mesh_info.set_number_nodes(189)
    assert mesh_info.get_number_nodes() == num_nodes
    """ Number of elements """
    num_elements = 2
    mesh_info.set_number_elements(2)
    assert mesh_info.get_number_elements() == num_elements


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_set_get_property_mesh_info(server_clayer):
    mesh_info = dpf.MeshInfo(server=server_clayer)

    """Scoping"""
    scoping = dpf.Scoping()
    expected_ids = [1, 2, 3]
    scoping._set_ids(expected_ids)
    mesh_info.set_property("my-property00", scoping)
    result_scoping = mesh_info.get_property("my-property00", dpf.Scoping)
    for x in range(len(expected_ids)):
        assert result_scoping.id(x) == scoping.id(x)

    """ Field """
    field = dpf.Field()
    mesh_info.set_property("my-property01", field)
    result_field = mesh_info.get_property("my-property01", dpf.Field)
    assert result_field.component_count == field.component_count


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_set_get_splittable_by_mesh_info(server_clayer):
    mesh_info = dpf.MeshInfo(server=server_clayer)
    splittable = dpf.StringField()
    expected_splittable = {"split_01", "split_02", "split_03"}
    splittable._set_data(expected_splittable)
    mesh_info.set_splittable_by(splittable)
    result_splittable = mesh_info.get_splittable_by()
    for i, strings in enumerate(expected_splittable):
        assert result_splittable.get_entity_data_by_id(i) == splittable.get_entity_data_by_id(i)


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_set_get_available_elem_types_mesh_info(server_clayer):
    mesh_info = dpf.MeshInfo(server=server_clayer)
    available_results_ids = [1, 2, 3]
    available_results = dpf.Scoping()
    available_results._set_ids(available_results_ids)
    mesh_info.set_available_elem_types(available_results)
    result_available = mesh_info.get_available_elem_types()
    for x in range(len(available_results)):
        assert result_available.id(x) == available_results.id(x)


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_output_mesh_info_provider_fluent(server_clayer):
    ds = dpf.DataSources(server=server_clayer)
    files = examples.download_fluent_multi_species()
    ds.set_result_file_path(files["cas"], "cas")

    mesh_info = dpf.operators.metadata.mesh_info_provider(server=server_clayer)
    mesh_info.connect(4, ds)
    mesh_info_out = mesh_info.outputs.mesh_info()

    assert type(mesh_info_out) == dpf.mesh_info.MeshInfo

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

    """************ Topology ************"""
    body_cell_topology = mesh_info_out.get_property("body_cell_topology", dpf.PropertyField)
    body_face_topology = mesh_info_out.get_property("body_face_topology", dpf.PropertyField)

    body_cell_topology_scoping = body_cell_topology._get_scoping()
    body_face_topology_scoping = body_face_topology._get_scoping()
    body_cell_topology_value = body_cell_topology._get_data()
    body_face_topology_value = body_face_topology._get_data()

    assert body_cell_topology_scoping.size == 1
    assert body_face_topology_scoping.size == 5
    assert body_cell_topology_scoping[0] == 1
    assert body_face_topology_scoping[0] == 1
    assert body_cell_topology_value[0] == 1
    assert body_face_topology_value[0] == 3

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


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_output_mesh_info_provider_flprj(model):
    res = model.metadata.mesh_info

    """************************ NUMBER OF CELLS/FACES/ZONES ************************"""

    num_cells = res.get_property("num_cells", int)
    num_faces = res.get_property("num_faces", int)
    num_nodes = res.get_property("num_nodes", int)

    assert num_cells == 13856
    assert num_faces == 45391
    assert num_nodes == 16660

    """************************ BODIES ************************"""

    """************ Name ************"""
    body_names = res.get_property("body_name", dpf.StringField)

    body_names_value = body_names._get_data()

    assert len(body_names_value) == 2
    assert body_names_value[0] == "fluid-rotor"
    assert body_names_value[1] == "fluid-stator"

    """************ Scoping ************"""
    body_scoping = res.get_property("body_scoping", dpf.Scoping)

    assert body_scoping.size == 2
    assert body_scoping[0] == 13
    assert body_scoping[1] == 28

    """************ Topology ************"""
    body_cell_topology = res.get_property("body_cell_topology", dpf.PropertyField)
    body_face_topology = res.get_property("body_face_topology", dpf.PropertyField)

    body_cell_topology_scoping = body_cell_topology._get_scoping()
    body_face_topology_scoping = body_face_topology._get_scoping()
    body_cell_topology_value = body_cell_topology._get_data()
    body_face_topology_value = body_face_topology._get_data()

    assert body_cell_topology_scoping.size == 2
    assert body_face_topology_scoping.size == 24
    assert body_cell_topology_scoping[0] == 13
    assert body_face_topology_scoping[0] == 13
    assert body_cell_topology_value[0] == 13
    assert body_face_topology_value[0] == 2

    """************************ ZONES ************************"""

    """************ Name ************"""
    zone_names = res.get_property("zone_name", dpf.StringField)

    zone_names_value = zone_names._get_data()

    assert zone_names_value.size == 26
    assert zone_names_value[0] == "fluid-rotor"
    assert zone_names_value[4] == "rotor-inlet"
    assert zone_names_value[8] == "rotor-per-1-shadow"
    assert zone_names_value[12] == "fluid-stator"
    assert zone_names_value[15] == "stator-shroud"
    assert zone_names_value[18] == "stator-blade-1"
    assert zone_names_value[22] == "stator-per-2"
    assert zone_names_value[25] == "stator-per-1-shadow"

    """************ Scoping ************"""
    zone_scoping = res.get_property("zone_scoping", dpf.Scoping)

    assert zone_scoping.size == 26
    assert zone_scoping[0] == 13
    assert zone_scoping[4] == 5
    assert zone_scoping[8] == 9
    assert zone_scoping[12] == 28
    assert zone_scoping[15] == 17
    assert zone_scoping[18] == 20
    assert zone_scoping[22] == 24
    assert zone_scoping[25] == 27

    """************ Element ************"""
    zone_elements = res.get_property("num_elem_zone", dpf.PropertyField)

    number_of_element_in_zone_value = zone_elements._get_data()

    assert number_of_element_in_zone_value.size == 26
    assert number_of_element_in_zone_value[0] == 6080
    assert number_of_element_in_zone_value[4] == 160
    assert number_of_element_in_zone_value[8] == 176
    assert number_of_element_in_zone_value[12] == 7776
    assert number_of_element_in_zone_value[15] == 486
    assert number_of_element_in_zone_value[18] == 320
    assert number_of_element_in_zone_value[22] == 48
    assert number_of_element_in_zone_value[25] == 64

    """************ CELL ZONES ************"""

    """************ Name ************"""
    cell_zone_name = res.get_property("cell_zone_names", dpf.StringField)

    cell_zone_name_value = cell_zone_name._get_data()

    assert cell_zone_name_value.size == 2
    assert cell_zone_name_value[0] == "fluid-rotor"
    assert cell_zone_name_value[1] == "fluid-stator"

    """************ Scoping ************"""
    cell_zone_scoping = res.get_property("cell_zone_scoping", dpf.Scoping)

    assert cell_zone_scoping.size == 2
    assert cell_zone_scoping[0] == 13
    assert cell_zone_scoping[1] == 28

    """************ Element ************"""
    cell_zone_elements = res.get_property("cell_zone_elements", dpf.PropertyField)

    cell_zone_elements_value = cell_zone_elements._get_data()

    assert cell_zone_elements_value.size == 2
    assert cell_zone_elements_value[0] == 6080
    assert cell_zone_elements_value[1] == 7776

    """************ FACE ZONES ************"""

    """************ Name ************"""
    face_zone_names = res.get_property("face_zone_names", dpf.StringField)

    face_zone_names_value = face_zone_names._get_data()

    assert face_zone_names_value.size == 24
    assert face_zone_names_value[0] == "default-interior:0"
    assert face_zone_names_value[1] == "rotor-hub"
    assert face_zone_names_value[5] == "rotor-blade-1"
    assert face_zone_names_value[10] == "rotor-per-2"
    assert face_zone_names_value[15] == "stator-outlet"
    assert face_zone_names_value[20] == "stator-per-2"
    assert face_zone_names_value[23] == "stator-per-1-shadow"

    """************ Scoping ************"""
    face_zone_scoping = res.get_property("face_zone_scoping", dpf.Scoping)

    assert face_zone_scoping.size == 24
    assert face_zone_scoping[0] == 2
    assert face_zone_scoping[1] == 3
    assert face_zone_scoping[5] == 7
    assert face_zone_scoping[10] == 12
    assert face_zone_scoping[15] == 19
    assert face_zone_scoping[20] == 24
    assert face_zone_scoping[23] == 27

    """************ Element ************"""
    face_zone_elements = res.get_property("face_zone_elements", dpf.PropertyField)

    face_zone_elements_value = face_zone_elements._get_data()

    assert face_zone_elements_value.size == 24
    assert face_zone_elements_value[0] == 17092
    assert face_zone_elements_value[1] == 380
    assert face_zone_elements_value[5] == 384
    assert face_zone_elements_value[10] == 48
    assert face_zone_elements_value[15] == 288
    assert face_zone_elements_value[20] == 48
    assert face_zone_elements_value[23] == 64
