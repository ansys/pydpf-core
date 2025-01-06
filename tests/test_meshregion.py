# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
import pytest
import vtk

from ansys import dpf
import conftest
from ansys.dpf.core.check_version import server_meet_version


@pytest.fixture()
def simple_bar_model(simple_bar, server_type):
    return dpf.core.Model(simple_bar, server=server_type)


def test_get_scoping_meshedregion_from_operator(simple_bar, server_type):
    dataSource = dpf.core.DataSources(server=server_type)
    dataSource.set_result_file_path(simple_bar)
    mesh = dpf.core.Operator("mapdl::rst::MeshProvider", server=server_type)
    mesh.connect(4, dataSource)
    meshOut = mesh.get_output(0, dpf.core.types.meshed_region)
    scop = meshOut._get_scoping(dpf.core.locations.nodal)
    assert len(scop.ids) == 3751
    scop = meshOut._get_scoping(dpf.core.locations.elemental)
    assert len(scop.ids) == 3000


def test_get_mesh_from_model(simple_bar_model, server_type):
    mesh = simple_bar_model.metadata.meshed_region
    assert len(mesh.nodes.scoping.ids) == 3751
    assert len(mesh.elements.scoping.ids) == 3000


def test_vtk_grid_from_model(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    grid = mesh._as_vtk(include_ids=True)
    assert np.allclose(grid["element_ids"], mesh.elements.scoping.ids)
    assert np.allclose(grid["node_ids"], mesh.nodes.scoping.ids)
    assert all(grid.celltypes == vtk.VTK_HEXAHEDRON)


def test_meshed_region_available_property_fields(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    properties = ["connectivity", "elprops", "eltype", "apdl_element_type", "mat"]
    properties_to_check = mesh.available_property_fields
    for p in properties:
        assert p in properties_to_check


def test_get_element_type_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    assert mesh.elements.element_by_index(1).type.value == 11
    assert mesh.elements.element_by_index(1).type == dpf.core.element_types.Hex8
    assert mesh.elements.element_by_index(1).shape == "solid"

    types = mesh.property_field(dpf.core.common.elemental_properties.element_type)
    assert np.allclose(types.data, np.full_like(types.data, 11))


def test_get_set_unit_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    assert mesh.unit == "m"
    mesh.unit = "km"
    assert mesh.unit == "km"


def test_get_node_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    node = mesh.nodes.node_by_index(1)
    scop = mesh.nodes.scoping
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
    assert np.allclose(field_coordinates.data[0], [0.1, 2.9, 0.1])
    assert np.allclose(mesh.grid.points, field_coordinates.data)

    coordinates = mesh.property_field(dpf.core.common.nodal_properties.coordinates)
    assert np.allclose(coordinates.data, field_coordinates.data)
    assert np.all(coordinates.meshed_region.nodes.scoping.ids == mesh.nodes.scoping.ids)


@conftest.raises_for_servers_version_under("3.0")
def test_set_coordinates_field_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    field_coordinates = mesh.nodes.coordinates_field
    new_data = field_coordinates.data
    new_data[0] = [0.0, 0.0, 0.0]
    field_coordinates.data = new_data
    mesh.nodes.coordinates_field = field_coordinates
    field_coordinates = mesh.nodes.coordinates_field
    assert np.allclose(field_coordinates.data[0], [0.0, 0.0, 0.0])

    new_data[0] = [1.0, 1.0, 1.0]
    field_coordinates.data = new_data
    mesh.set_coordinates_field(field_coordinates)
    field_coordinates = mesh.nodes.coordinates_field
    point_0 = list(mesh.grid.points[0])
    assert np.allclose(field_coordinates.data[0], [1.0, 1.0, 1.0])
    assert np.allclose(point_0, [1.0, 1.0, 1.0])
    field_coordinates.data = field_coordinates.data * 2.0
    mesh.set_coordinates_field(field_coordinates)
    field_coordinates = mesh.nodes.coordinates_field
    point_1 = list(mesh.grid.points[0])
    assert np.allclose(field_coordinates.data[0], [2.0, 2.0, 2.0])
    assert np.allclose(point_1, [2.0, 2.0, 2.0])


def test_get_element_types_field_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    elemcoping = mesh.elements.scoping
    field_element_types = mesh.elements.element_types_field
    assert np.allclose(field_element_types.data[0], [11])
    assert field_element_types.size == elemcoping.size
    assert field_element_types.component_count == 1


@conftest.raises_for_servers_version_under("3.0")
def test_set_element_types_field_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    field_element_types = mesh.elements.element_types_field
    new_data = field_element_types.data
    new_data[0] = 0
    field_element_types.data = new_data
    mesh.elements.element_types_field = field_element_types
    types = mesh.elements.element_types_field
    assert types.data[0] == 0

    new_data[0] = 1
    field_element_types.data = new_data
    mesh.set_property_field(dpf.core.common.elemental_properties.element_type, field_element_types)
    field_element_types = mesh.elements.element_types_field
    assert field_element_types.data[0] == 1


def test_get_materials_field_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    elemcoping = mesh.elements.scoping
    field_mat = mesh.elements.materials_field
    assert field_mat.data[0] == 1
    assert field_mat.size == elemcoping.size
    assert field_mat.component_count == 1

    materials = mesh.property_field(dpf.core.common.elemental_properties.material)
    assert np.allclose(materials.data, field_mat.data)


@conftest.raises_for_servers_version_under("3.0")
def test_set_materials_field_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    materials = mesh.property_field(dpf.core.common.elemental_properties.material)
    new_data = materials.data
    new_data[0] = 0
    materials.data = new_data
    mesh.elements.materials_field = materials
    types = mesh.elements.materials_field
    assert types.data[0] == 0

    new_data[0] = 1
    materials.data = new_data
    mesh.set_property_field(dpf.core.common.elemental_properties.material, materials)
    materials = mesh.elements.materials_field
    assert materials.data[0] == 1


def test_get_connectivities_field_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    field_connect = mesh.elements.connectivities_field
    assert field_connect.data[0] == 1053
    assert field_connect.component_count == 1
    assert np.allclose(
        field_connect.get_entity_data(1),
        [1053, 1062, 1143, 1134, 2492, 2491, 2482, 2483],
    )
    connectivity = mesh.property_field(dpf.core.common.elemental_properties.connectivity)
    assert np.allclose(connectivity.data, field_connect.data)


@conftest.raises_for_servers_version_under("3.0")
def test_set_connectivities_field_meshed_region(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    connectivity = mesh.elements.connectivities_field
    new_connectivity_data = connectivity.data
    assert new_connectivity_data[0] == 1053
    new_connectivity_data[0] = 0
    connectivity.data = new_connectivity_data
    mesh.elements.connectivities_field = connectivity
    connectivity = mesh.elements.connectivities_field
    assert connectivity.data[0] == 0

    new_connectivity_data[0] = 1
    connectivity.data = new_connectivity_data
    mesh.set_property_field(dpf.core.common.elemental_properties.connectivity, connectivity)
    connectivity = mesh.elements.connectivities_field
    assert connectivity.data[0] == 1


def test_get_nodes_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    node = mesh.nodes.node_by_id(1)
    assert node.id == 1
    assert node.index >= 0
    assert node.coordinates != None
    node = mesh.nodes.node_by_index(1)
    assert node.id >= 1
    assert node.index == 1
    assert node.coordinates != None


def test_get_elements_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    el = mesh.elements.element_by_id(1)
    assert el.id == 1
    assert el.index >= 0
    assert el.nodes is not None
    el = mesh.elements.element_by_index(1)
    assert el.id >= 1
    assert el.index == 1
    assert el.nodes is not None


def test_str_meshedregion(simple_bar_model):
    meshed_region = simple_bar_model.metadata.meshed_region
    assert str(len(meshed_region.nodes)) in str(meshed_region)
    assert str(len(meshed_region.elements)) in str(meshed_region)


def test_str_nodes_elements_meshedregion(simple_bar_model):
    meshed_region = simple_bar_model.metadata.meshed_region
    assert "3000" in str(meshed_region.elements)
    assert "3751" in str(meshed_region.nodes)
    assert "Hex" in str(meshed_region.elements.element_by_id(1))
    assert "0" in str(meshed_region.nodes.node_by_id(1))


def test_delete_meshedregion(simple_bar_model):
    mesh = simple_bar_model.metadata.meshed_region
    mesh = None
    import gc

    gc.collect()
    with pytest.raises(Exception):
        mesh.nodes[0]


def test_id_indeces_mapping_on_nodes_1(multishells, server_type):
    model = dpf.core.Model(multishells, server=server_type)
    mesh = model.metadata.meshed_region
    mapping = mesh.nodes.mapping_id_to_index
    nodes = mesh.nodes
    assert len(mapping) == len(nodes)
    assert len(nodes) == 7079
    assert mapping[995] == 994
    assert mapping[500] == 499


def test_id_indeces_mapping_on_nodes_2(allkindofcomplexity, server_type):
    model = dpf.core.Model(allkindofcomplexity, server=server_type)
    mesh = model.metadata.meshed_region
    mapping = mesh.nodes.mapping_id_to_index
    nodes = mesh.nodes
    assert len(mapping) == len(nodes)
    assert len(nodes) == 15129
    assert mapping[20] == 19
    assert mapping[9008] == 9007
    assert mapping[12346] == 12345


def test_id_indeces_mapping_on_elements_1(multishells, server_type):
    model = dpf.core.Model(multishells, server=server_type)
    mesh = model.metadata.meshed_region
    mapping = mesh.elements.mapping_id_to_index
    elements = mesh.elements
    assert len(mapping) == len(elements)
    assert len(elements) == 4220
    assert mapping[2500] == 2895
    assert mapping[1999] == 191


def test_id_indeces_mapping_on_elements_2(allkindofcomplexity, server_type):
    model = dpf.core.Model(allkindofcomplexity, server=server_type)
    mesh = model.metadata.meshed_region
    mapping = mesh.elements.mapping_id_to_index
    elements = mesh.elements
    assert len(mapping) == len(elements)
    if server_meet_version("9.0", mesh._server):
        assert len(elements) == 10294
    else:
        assert len(elements) == 10292
    assert mapping[23] == 24
    assert mapping[4520] == 2011


def test_named_selection_mesh(allkindofcomplexity, server_type):
    model = dpf.core.Model(allkindofcomplexity, server=server_type)
    mesh = model.metadata.meshed_region
    ns = mesh.available_named_selections
    assert ns == [
        "_CM82",
        "_CM86UX_XP",
        "_DISPNONZEROUX",
        "_DISPZEROUZ",
        "_ELMISC",
        "_FIXEDSU",
    ]
    scop = mesh.named_selection("_CM86UX_XP")
    assert len(scop) == 481
    assert scop.location == dpf.core.locations().nodal


@conftest.raises_for_servers_version_under("3.0")
def test_set_named_selection_mesh(allkindofcomplexity, server_type):
    model = dpf.core.Model(allkindofcomplexity, server=server_type)
    mesh = model.metadata.meshed_region
    name = "test"
    scoping = dpf.core.Scoping(server=server_type)
    mesh.set_named_selection_scoping(name, scoping)
    ns = mesh.available_named_selections
    assert "test" in ns


def test_create_meshed_region(server_type):
    mesh = dpf.core.MeshedRegion(num_nodes=4, num_elements=1, server=server_type)
    mesh.nodes.add_node(1, [0.0, 0.0, 0.0])
    assert mesh.nodes.n_nodes == 1
    assert mesh.elements.n_elements == 0
    mesh.nodes.add_node(2, [1.0, 0.0, 0.0])
    mesh.nodes.add_node(3, [1.0, 1.0, 0.0])
    mesh.nodes.add_node(4, [0.0, 1.0, 0.0])
    mesh.elements.add_shell_element(1, [0, 1, 2, 3])

    assert mesh.nodes.n_nodes == 4
    assert mesh.elements.n_elements == 1
    el = mesh.elements.element_by_id(1)
    assert el.shape == "shell"
    assert el.type.value == 16


def test_connectivity_meshed_region(server_type):
    mesh = test_create_all_shaped_meshed_region(server_type)
    connectivity = mesh.elements.connectivities_field
    assert np.allclose(connectivity.get_entity_data_by_id(1), [0, 1, 2, 3])
    assert np.allclose(connectivity.get_entity_data(0), [0, 1, 2, 3])
    assert np.allclose(mesh.elements.element_by_id(1).connectivity, [0, 1, 2, 3])

    nodal_conne = mesh.nodes.nodal_connectivity_field
    assert np.allclose(nodal_conne.get_entity_data_by_id(1), [0])
    assert np.allclose(mesh.nodes.node_by_id(1).nodal_connectivity, [0])

    mesh_nodal = mesh.property_field(dpf.core.common.nodal_properties.nodal_connectivity)
    assert np.allclose(mesh_nodal.data, nodal_conne.data)

    mesh_nodal = mesh.property_field(dpf.core.common.nodal_properties.nodal_connectivity)
    assert np.allclose(mesh_nodal.data, nodal_conne.data)


def test_create_all_shaped_meshed_region(server_type):
    mesh = dpf.core.MeshedRegion(num_nodes=11, num_elements=4, server=server_type)
    assert mesh.nodes.n_nodes == 0
    assert mesh.elements.n_elements == 0

    mesh.nodes.add_node(1, [0.0, 0.0, 0.0])
    mesh.nodes.add_node(2, [1.0, 0.0, 0.0])
    mesh.nodes.add_node(3, [1.0, 1.0, 0.0])
    mesh.nodes.add_node(4, [0.0, 1.0, 0.0])
    mesh.elements.add_shell_element(1, [0, 1, 2, 3])

    mesh.nodes.add_node(5, [0.0, 0.0, 0.0])
    mesh.elements.add_point_element(2, [4])

    mesh.nodes.add_node(6, [0.0, 0.0, 0.0])
    mesh.nodes.add_node(7, [1.0, 0.0, 0.0])
    mesh.elements.add_beam_element(3, [5, 6])

    mesh.nodes.add_node(8, [0.0, 0.0, 0.0])
    mesh.nodes.add_node(9, [1.0, 0.0, 0.0])
    mesh.nodes.add_node(10, [1.0, 1.0, 0.0])
    mesh.nodes.add_node(11, [0.0, 1.0, 1.0])
    mesh.elements.add_solid_element(4, [7, 8, 9, 10])

    assert mesh.nodes.n_nodes == 11
    assert mesh.elements.n_elements == 4
    el = mesh.elements.element_by_id(1)
    assert el.shape == "shell"
    assert el.type.value == 16

    el = mesh.elements.element_by_id(2)
    assert el.shape == "unknown_shape"
    assert el.type.value == 9
    assert el.nodes[0].index == 4

    el = mesh.elements.element_by_id(3)
    assert el.type.value == 18
    assert el.shape == "beam"
    assert len(el.nodes) == 2

    el = mesh.elements.element_by_id(4)
    assert el.type.value == 10
    assert el.shape == "solid"
    assert len(el.nodes) == 4
    return mesh


def test_create_with_yield_meshed_region(server_type):
    ref_mesh = test_create_all_shaped_meshed_region(server_type)
    mesh = dpf.core.MeshedRegion(
        num_nodes=ref_mesh.nodes.n_nodes,
        num_elements=ref_mesh.elements.n_elements,
        server=server_type,
    )
    index = 0
    for node in mesh.nodes.add_nodes(ref_mesh.nodes.n_nodes):
        ref_node = ref_mesh.nodes.node_by_index(index)
        node.id = ref_node.id
        node.coordinates = ref_node.coordinates
        index = index + 1
    index = 0
    for elem in mesh.elements.add_elements(ref_mesh.elements.n_elements):
        ref_elem = ref_mesh.elements.element_by_index(index)
        elem.id = ref_elem.id
        elem.connectivity = ref_elem.connectivity
        elem.shape = ref_elem.shape
        index = index + 1
    assert mesh.nodes.n_nodes == 11
    assert mesh.elements.n_elements == 4
    el = mesh.elements.element_by_id(1)
    assert el.shape == "shell"
    assert el.type.value == 16

    el = mesh.elements.element_by_id(2)
    assert el.shape == "unknown_shape"
    assert el.type.value == 9
    assert el.nodes[0].index == 4

    el = mesh.elements.element_by_id(3)
    assert el.type.value == 18
    assert el.shape == "beam"
    assert len(el.nodes) == 2

    el = mesh.elements.element_by_id(4)
    assert el.type.value == 10
    assert el.shape == "solid"
    assert len(el.nodes) == 4


def test_create_by_copy_meshed_region(server_type):
    ref_mesh = test_create_all_shaped_meshed_region(server_type)
    mesh = dpf.core.MeshedRegion(
        num_nodes=ref_mesh.nodes.n_nodes,
        num_elements=ref_mesh.elements.n_elements,
        server=server_type,
    )
    index = 0
    for node in ref_mesh.nodes:
        ref_node = ref_mesh.nodes.node_by_index(index)
        mesh.nodes.add_node(ref_node.id, ref_node.coordinates)
        index = index + 1
    index = 0
    for elem in ref_mesh.elements:
        ref_elem = ref_mesh.elements.element_by_index(index)
        mesh.elements.add_element(ref_elem.id, ref_elem.shape, ref_elem.connectivity)
        index = index + 1
    assert mesh.nodes.n_nodes == 11
    assert mesh.elements.n_elements == 4
    el = mesh.elements.element_by_id(1)
    assert el.shape == "shell"
    assert el.type.value == 16

    el = mesh.elements.element_by_id(2)
    assert el.shape == "unknown_shape"
    assert el.type.value == 9
    assert el.nodes[0].index == 4

    el = mesh.elements.element_by_id(3)
    assert el.type.value == 18
    assert el.shape == "beam"
    assert len(el.nodes) == 2

    el = mesh.elements.element_by_id(4)
    assert el.type.value == 10
    assert el.shape == "solid"
    assert len(el.nodes) == 4


def test_has_element_shape_meshed_region(server_type):
    mesh = dpf.core.MeshedRegion(num_nodes=11, num_elements=4, server=server_type)
    # Any of those four calls make the second call to has_****_elements wrong when using InProcess
    assert mesh.elements.has_beam_elements is False
    assert mesh.elements.has_solid_elements is False
    assert mesh.elements.has_shell_elements is False
    assert mesh.elements.has_point_elements is False
    assert mesh.elements.n_elements == 0

    mesh.nodes.add_node(1, [0.0, 0.0, 0.0])
    mesh.nodes.add_node(2, [1.0, 0.0, 0.0])
    mesh.nodes.add_node(3, [1.0, 1.0, 0.0])
    mesh.nodes.add_node(4, [0.0, 1.0, 0.0])
    mesh.elements.add_shell_element(1, [0, 1, 2, 3])
    assert mesh.elements.n_elements == 1
    assert mesh.elements.has_beam_elements is False
    assert mesh.elements.has_solid_elements is False
    assert mesh.elements.has_shell_elements is True  # This fails for CDirect
    assert mesh.elements.has_point_elements is False

    mesh.nodes.add_node(5, [0.0, 0.0, 0.0])
    mesh.elements.add_point_element(2, [4])
    assert mesh.elements.has_beam_elements is False
    assert mesh.elements.has_solid_elements is False
    assert mesh.elements.has_shell_elements is True
    assert mesh.elements.has_point_elements is True

    mesh.nodes.add_node(6, [0.0, 0.0, 0.0])
    mesh.nodes.add_node(7, [1.0, 0.0, 0.0])
    mesh.elements.add_beam_element(3, [5, 6])
    assert mesh.elements.has_beam_elements is True
    assert mesh.elements.has_solid_elements is False
    assert mesh.elements.has_shell_elements is True
    assert mesh.elements.has_point_elements is True

    mesh.nodes.add_node(8, [0.0, 0.0, 0.0])
    mesh.nodes.add_node(9, [1.0, 0.0, 0.0])
    mesh.nodes.add_node(10, [1.0, 1.0, 0.0])
    mesh.nodes.add_node(11, [0.0, 1.0, 1.0])
    mesh.elements.add_solid_element(4, [7, 8, 9, 10])
    assert mesh.elements.has_beam_elements is True
    assert mesh.elements.has_solid_elements is True
    assert mesh.elements.has_shell_elements is True
    assert mesh.elements.has_point_elements is True


@pytest.mark.slow
def test_mesh_deep_copy(allkindofcomplexity, server_type):
    # Small mesh
    model = dpf.core.Model(allkindofcomplexity, server=server_type)
    mesh = model.metadata.meshed_region
    copy = mesh.deep_copy()
    assert np.allclose(copy.nodes.scoping.ids, mesh.nodes.scoping.ids)
    assert np.allclose(copy.elements.scoping.ids, mesh.elements.scoping.ids)
    assert copy.unit == mesh.unit
    assert np.allclose(copy.nodes.coordinates_field.data, mesh.nodes.coordinates_field.data)
    assert np.allclose(
        copy.elements.element_types_field.data, mesh.elements.element_types_field.data
    )
    assert np.allclose(
        copy.elements.connectivities_field.data, mesh.elements.connectivities_field.data
    )

    assert np.allclose(
        copy.nodes.coordinates_field.scoping.ids,
        mesh.nodes.coordinates_field.scoping.ids,
    )
    assert np.allclose(
        copy.elements.element_types_field.scoping.ids,
        mesh.elements.element_types_field.scoping.ids,
    )
    assert np.allclose(
        copy.elements.connectivities_field.scoping.ids,
        mesh.elements.connectivities_field.scoping.ids,
    )


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="Available with CFF starting 7.0",
)
def test_mesh_deep_copy_large(fluent_multiphase, server_type):
    model = dpf.core.Model(fluent_multiphase(server=server_type), server=server_type)
    mesh = model.metadata.meshed_region
    copy = mesh.deep_copy()
    assert np.allclose(copy.nodes.scoping.ids, mesh.nodes.scoping.ids)


@pytest.mark.slow
def test_mesh_deep_copy2(simple_bar_model, server_type):
    mesh = simple_bar_model.metadata.meshed_region
    copy = mesh.deep_copy()
    assert np.allclose(copy.nodes.scoping.ids, mesh.nodes.scoping.ids)
    assert np.allclose(copy.elements.scoping.ids, mesh.elements.scoping.ids)
    assert copy.unit == mesh.unit
    assert np.allclose(copy.nodes.coordinates_field.data, mesh.nodes.coordinates_field.data)
    assert np.allclose(
        copy.elements.element_types_field.data, mesh.elements.element_types_field.data
    )
    assert np.allclose(
        copy.elements.connectivities_field.data, mesh.elements.connectivities_field.data
    )

    assert np.allclose(
        copy.nodes.coordinates_field.scoping.ids,
        mesh.nodes.coordinates_field.scoping.ids,
    )
    assert np.allclose(
        copy.elements.element_types_field.scoping.ids,
        mesh.elements.element_types_field.scoping.ids,
    )
    assert np.allclose(
        copy.elements.connectivities_field.scoping.ids,
        mesh.elements.connectivities_field.scoping.ids,
    )


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Bug in server version lower than 4.0",
)
def test_empty_mesh_get_scoping(server_type):
    mesh = dpf.core.MeshedRegion(server=server_type)
    okay = mesh.nodes.scoping is None or len(mesh.nodes.scoping) == 0
    assert okay
    okay = mesh.elements.scoping is None or len(mesh.elements.scoping) == 0
    assert okay
