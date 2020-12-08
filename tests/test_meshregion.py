import numpy as np
import pytest
import vtk
from ansys import dpf



@pytest.fixture()
def simple_bar_model(simple_bar):
    return dpf.core.Model(simple_bar)


def test_get_scoping_meshedregion_from_operator(simple_bar):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(simple_bar)
    mesh = dpf.core.Operator("mapdl::rst::MeshProvider")
    mesh.connect(4, dataSource)
    meshOut = mesh.get_output(0, dpf.core.types.meshed_region)
    scop = meshOut._get_scoping(dpf.core.locations.nodal)
    assert len(scop.ids) == 3751
    scop = meshOut._get_scoping(dpf.core.locations.elemental)
    assert len(scop.ids) == 3000


def test_get_mesh_from_model(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    assert len(mesh.nodes.scoping.ids) == 3751
    assert len(mesh.elements.scoping.ids) == 3000


def test_vtk_grid_from_model(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    grid = mesh.grid
    assert np.allclose(grid['element_ids'], mesh.elements.scoping.ids)
    assert np.allclose(grid['node_ids'], mesh.nodes.scoping.ids)
    assert all(grid.celltypes == vtk.VTK_HEXAHEDRON)


def test_get_element_type_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    assert mesh.elements.element_by_index(1).element_type == 11
    assert mesh.elements.element_by_index(1).element_shape == 'solid'


def test_get_unit_meshedregion(simple_bar_model):
    assert simple_bar_model.metadata.meshed_region.unit == 'm'


def test_get_node_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    node = mesh.nodes.node_by_index(1)
    scop = mesh._get_scoping(dpf.core.locations.nodal)
    assert node.id == scop.id(1)
    assert node.index == 1

    expected_coord = [0.1, 2.9, 0.2]
    assert node.coordinates == expected_coord
    assert np.allclose(mesh.grid.points[1], expected_coord)


def test_get_element_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    el = mesh.elements.element_by_index(1)
    scop = mesh.elements.scoping
    assert el.id == scop.id(1)
    assert el.index == 1
    nodes = el.nodes
    assert el.n_nodes == len(nodes)
    node = nodes[0]
    assert node.index == 1053
    assert node.coordinates == [0.1, 1.6, 0.1]


def test_get_coordinates_field_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    nodescoping = mesh.nodes.scoping
    field_coordinates = mesh.nodes.coordinates_field
    assert field_coordinates.component_count == 3
    assert field_coordinates.elementary_data_count == nodescoping.size
    assert np.allclose(field_coordinates.data[0],[0.1,2.9,0.1])
    assert np.allclose(mesh.grid.points, field_coordinates.data)


def test_get_element_types_field_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    elemcoping = mesh.elements.scoping
    field_element_types = mesh.elements.element_types_field
    assert np.allclose(field_element_types.data[0], [11])
    assert field_element_types.size == elemcoping.size
    assert field_element_types.component_count == 1


def test_get_materials_field_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    elemcoping = mesh.elements.scoping
    field_mat = mesh.elements.materials_field
    assert field_mat.data[0] == 1
    assert field_mat.size == elemcoping.size
    assert field_mat.component_count == 1


def test_get_connectivities_field_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    elemcoping = mesh.elements.scoping
    field_connect = mesh.elements.connectivities_field
    assert field_connect.data[0] == 1053
    assert field_connect.component_count == 1
    assert np.allclose(field_connect.get_entity_data(1), [1053, 1062, 1143, 1134, 2492, 2491, 2482, 2483])

def test_get_nodes_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    node = mesh.nodes.node_by_id(1)
    assert node.id ==1
    assert node.index >=0
    assert node.coordinates != None
    node = mesh.nodes.node_by_index(1)
    assert node.id >= 1
    assert node.index ==1
    assert node.coordinates != None


def test_get_elements_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    el = mesh.elements.element_by_id(1)
    assert el.id == 1
    assert el.index >= 0
    assert el.nodes is not None
    el = mesh.elements.element_by_index(1)
    assert el.id >= 1
    assert el.index ==1
    assert el.nodes is not None


def test_str_meshedregion(simple_bar_model):
    meshed_region = simple_bar_model.metadata.meshed_region
    assert str(len(meshed_region.nodes)) in str(meshed_region)
    assert str(len(meshed_region.elements)) in str(meshed_region)


def test_delete_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    del mesh
    with pytest.raises(Exception):
        mesh.nodes[0]


def test_delete_auto_meshedregion(simple_bar):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(simple_bar)
    mesh = dpf.core.Operator("mapdl::rst::MeshProvider")
    mesh.connect(4, dataSource)
    meshOut = mesh.get_output(0, dpf.core.types.meshed_region)
    meshOut2 = dpf.core.meshed_region.MeshedRegion(meshOut._message)
    del meshOut
    with pytest.raises(Exception):
        meshOut2.get_element_type(1)
