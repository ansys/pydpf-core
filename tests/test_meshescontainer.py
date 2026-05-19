# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

# -*- coding: utf-8 -*-

import weakref

import numpy as np
import pytest

from ansys import dpf
from ansys.dpf.core import MeshesContainer


# TO DO: add server type
@pytest.fixture()
def dummy_mesh(server_type):
    """Returns a mesh"""
    mesh = dpf.core.MeshedRegion(server=server_type)
    mesh.nodes.add_node(1, [0.0, 0.0, 0.0])
    mesh.nodes.add_node(2, [1.0, 1.0, 1.0])
    mesh.elements.add_beam_element(1, [0, 1])
    return mesh


@pytest.fixture()
def elshape_body_mc(dummy_mesh):
    """Returns a meshes container with 20 mesh split on body and elshape"""
    mc = MeshesContainer(server=dummy_mesh._server)
    mc.labels = ["elshape", "body"]
    for i in range(0, 20):
        mscop = {"elshape": i, "body": 0}
        mc.add_mesh(mscop, dummy_mesh)
    return mc


def test_create_meshes_container(server_type):
    mc = MeshesContainer()
    assert mc._internal_obj is not None


def test_empty_index():
    mc = MeshesContainer()
    with pytest.raises(IndexError):
        mc[0]


def test_createby_message_copy_meshes_container(server_type_legacy_grpc):
    mc = MeshesContainer(server=server_type_legacy_grpc)
    meshes_container2 = MeshesContainer(
        meshes_container=mc._internal_obj, server=server_type_legacy_grpc
    )
    assert mc._internal_obj == meshes_container2._internal_obj


def test_createbycopy_meshes_container(server_type):
    mc = MeshesContainer(server=server_type)
    meshes_container2 = MeshesContainer(meshes_container=mc)
    assert mc._internal_obj != meshes_container2._internal_obj


def test_set_get_mesh_meshes_container(elshape_body_mc):
    mc = elshape_body_mc
    assert mc.get_available_ids_for_label("elshape") == list(range(0, 20))
    for i in range(0, 20):
        mesh = mc.get_mesh({"elshape": i, "body": 0})._internal_obj
        assert mesh is not None
        assert mc.get_mesh(i)._internal_obj is not None
        assert mc.get_mesh({"elshape": i, "body": 0})._internal_obj is not None
        assert mc[i]._internal_obj is not None


def test_set_get_mesh_meshes_container_new_label(elshape_body_mc, dummy_mesh):
    mc = elshape_body_mc
    assert mc.get_available_ids_for_label("elshape") == list(range(0, 20))
    for i in range(0, 20):
        mesh = mc.get_mesh({"elshape": i, "body": 0})._internal_obj
        assert mesh is not None
        assert mc.get_mesh(i)._internal_obj is not None
        assert mc.get_mesh({"elshape": i, "body": 0})._internal_obj is not None
        assert mc[i]._internal_obj is not None
        assert mc.get_label_space(i) == {"elshape": i, "body": 0}

    mc.add_label("time")
    for i in range(0, 20):
        mscop = {"elshape": i, "body": 0, "time": 1}
        mc.add_mesh(mscop, dummy_mesh)
    assert len(mc.get_meshes({"elshape": i, "body": 0})) == 2
    for i in range(0, 20):
        mesh = mc.get_mesh({"elshape": i, "body": 0, "time": 1})._internal_obj
        assert mesh is not None
        assert mc.get_mesh(i + 20)._internal_obj is not None
        assert mc[i]._internal_obj is not None
        assert mc.get_label_space(i + 20) == {"elshape": i, "body": 0, "time": 1}
        assert mc.get_mesh({"elshape": i, "body": 0, "time": 1})._internal_obj is not None
        assert mc.get_mesh({"elshape": i, "time": 1})._internal_obj is not None


def test_get_item_mesh_meshes_container(elshape_body_mc):
    mc = elshape_body_mc
    for i in range(0, 20):
        assert mc[i]._internal_obj is not None


def test_delete_meshes_container():
    mc = MeshesContainer()
    ref = weakref.ref(mc)
    mc = None
    import gc

    gc.collect()
    assert ref() is None


def test_str_meshes_container(elshape_body_mc):
    mc = elshape_body_mc
    assert "body" in str(mc)


def test_solid_meshes_returns_list(elshape_body_mc):
    result = elshape_body_mc.solid_meshes()
    assert isinstance(result, list), "solid_meshes should return a list"


def test_solid_meshes_no_label_space(elshape_body_mc):
    solid_meshes = elshape_body_mc.solid_meshes()
    assert len(solid_meshes) == 1, f"Expected 1 solid mesh, got {len(solid_meshes)}"


def test_solid_meshes_with_label_space(elshape_body_mc):
    solid_meshes = elshape_body_mc.solid_meshes(label_space={"body": 0})
    assert len(solid_meshes) == 1, f"Expected 1 solid mesh, got {len(solid_meshes)}"


def test_solid_meshes_returns_meshed_regions(elshape_body_mc):
    solid_meshes = elshape_body_mc.solid_meshes()
    for mesh in solid_meshes:
        assert isinstance(mesh, dpf.core.MeshedRegion), "Each element should be a MeshedRegion"


def test_solid_meshes_no_elshape_label_raises(server_type):
    mc = MeshesContainer(server=server_type)
    mc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        mc.solid_meshes()


def test_solid_meshes_invalid_label_raises(elshape_body_mc):
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.solid_meshes(label_space={"invalid_label": 0})


def test_solid_meshes_does_not_mutate_input(elshape_body_mc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_mc.solid_meshes(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_shell_meshes_returns_list(elshape_body_mc):
    result = elshape_body_mc.shell_meshes()
    assert isinstance(result, list), "shell_meshes should return a list"


def test_shell_meshes_no_label_space(elshape_body_mc):
    shell_meshes = elshape_body_mc.shell_meshes()
    assert len(shell_meshes) == 1, f"Expected 1 shell mesh, got {len(shell_meshes)}"


def test_shell_meshes_with_label_space(elshape_body_mc):
    shell_meshes = elshape_body_mc.shell_meshes(label_space={"body": 0})
    assert len(shell_meshes) == 1, f"Expected 1 shell mesh, got {len(shell_meshes)}"


def test_shell_meshes_returns_meshed_regions(elshape_body_mc):
    shell_meshes = elshape_body_mc.shell_meshes()
    for mesh in shell_meshes:
        assert isinstance(mesh, dpf.core.MeshedRegion), "Each element should be a MeshedRegion"


def test_shell_meshes_no_elshape_label_raises(server_type):
    mc = MeshesContainer(server=server_type)
    mc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        mc.shell_meshes()


def test_shell_meshes_invalid_label_raises(elshape_body_mc):
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.shell_meshes(label_space={"nonexistent": 0})


def test_shell_meshes_does_not_mutate_input(elshape_body_mc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_mc.shell_meshes(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_beam_meshes_returns_list(elshape_body_mc):
    result = elshape_body_mc.beam_meshes()
    assert isinstance(result, list), "beam_meshes should return a list"


def test_beam_meshes_no_label_space(elshape_body_mc):
    beam_meshes = elshape_body_mc.beam_meshes()
    assert len(beam_meshes) == 1, f"Expected 1 beam mesh, got {len(beam_meshes)}"


def test_beam_meshes_with_label_space(elshape_body_mc):
    beam_meshes = elshape_body_mc.beam_meshes(label_space={"body": 0})
    assert len(beam_meshes) == 1, f"Expected 1 beam mesh, got {len(beam_meshes)}"


def test_beam_meshes_returns_meshed_regions(elshape_body_mc):
    beam_meshes = elshape_body_mc.beam_meshes()
    for mesh in beam_meshes:
        assert isinstance(mesh, dpf.core.MeshedRegion), "Each element should be a MeshedRegion"


def test_beam_meshes_no_elshape_label_raises(server_type):
    mc = MeshesContainer(server=server_type)
    mc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        mc.beam_meshes()


def test_beam_meshes_invalid_label_raises(elshape_body_mc):
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.beam_meshes(label_space={"fake_label": 99})


def test_beam_meshes_does_not_mutate_input(elshape_body_mc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_mc.beam_meshes(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_solid_mesh_returns_meshed_region(elshape_body_mc):
    solid_mesh = elshape_body_mc.solid_mesh(label_space={"body": 0})
    assert isinstance(solid_mesh, dpf.core.MeshedRegion), "solid_mesh should return a MeshedRegion"


def test_solid_mesh_consistent_with_solid_meshes(elshape_body_mc):
    solid_meshes = elshape_body_mc.solid_meshes(label_space={"body": 0})
    solid_mesh = elshape_body_mc.solid_mesh(label_space={"body": 0})
    assert np.array_equal(
        solid_meshes[0].nodes.scoping.ids, solid_mesh.nodes.scoping.ids
    ), "Solid meshes and solid_mesh should have same node ids"
    assert np.array_equal(
        solid_meshes[0].elements.scoping.ids, solid_mesh.elements.scoping.ids
    ), "Solid meshes and solid_mesh should have same element ids"
    assert (
        solid_meshes[0].available_property_fields == solid_mesh.available_property_fields
    ), "Solid meshes and solid_mesh should have same property fields"


def test_solid_mesh_no_elshape_label_raises(server_type):
    mc = MeshesContainer(server=server_type)
    mc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        mc.solid_mesh()


def test_solid_mesh_invalid_label_raises(elshape_body_mc):
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.solid_mesh(label_space={"wrong_label": 0})


def test_solid_mesh_does_not_mutate_input(elshape_body_mc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_mc.solid_mesh(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_solid_mesh_has_nodes(elshape_body_mc):
    solid_mesh = elshape_body_mc.solid_mesh(label_space={"body": 0})
    assert solid_mesh.nodes.n_nodes > 0, "Solid mesh should have nodes"


def test_solid_mesh_has_elements(elshape_body_mc):
    solid_mesh = elshape_body_mc.solid_mesh(label_space={"body": 0})
    assert solid_mesh.elements.n_elements > 0, "Solid mesh should have elements"


def test_shell_mesh_returns_meshed_region(elshape_body_mc):
    shell_mesh = elshape_body_mc.shell_mesh(label_space={"body": 0})
    assert isinstance(shell_mesh, dpf.core.MeshedRegion), "shell_mesh should return a MeshedRegion"


def test_shell_mesh_consistent_with_shell_meshes(elshape_body_mc):
    shell_meshes = elshape_body_mc.shell_meshes(label_space={"body": 0})
    shell_mesh = elshape_body_mc.shell_mesh(label_space={"body": 0})
    assert np.array_equal(
        shell_meshes[0].nodes.scoping.ids, shell_mesh.nodes.scoping.ids
    ), "Shell meshes and shell_mesh should have same node ids"
    assert np.array_equal(
        shell_meshes[0].elements.scoping.ids, shell_mesh.elements.scoping.ids
    ), "Shell meshes and shell_mesh should have same element ids"
    assert (
        shell_meshes[0].available_property_fields == shell_mesh.available_property_fields
    ), "Shell meshes and shell_mesh should have same property fields"


def test_shell_mesh_no_elshape_label_raises(server_type):
    mc = MeshesContainer(server=server_type)
    mc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        mc.shell_mesh()


def test_shell_mesh_invalid_label_raises(elshape_body_mc):
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.shell_mesh(label_space={"wrong_label": 0})


def test_shell_mesh_does_not_mutate_input(elshape_body_mc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_mc.shell_mesh(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_shell_mesh_has_nodes(elshape_body_mc):
    shell_mesh = elshape_body_mc.shell_mesh(label_space={"body": 0})
    assert shell_mesh.nodes.n_nodes > 0, "Shell mesh should have nodes"


def test_shell_mesh_has_elements(elshape_body_mc):
    shell_mesh = elshape_body_mc.shell_mesh(label_space={"body": 0})
    assert shell_mesh.elements.n_elements > 0, "Shell mesh should have elements"


def test_beam_mesh_returns_meshed_region(elshape_body_mc):
    beam_mesh = elshape_body_mc.beam_mesh(label_space={"body": 0})
    assert isinstance(beam_mesh, dpf.core.MeshedRegion), "beam_mesh should return a MeshedRegion"


def test_beam_mesh_consistent_with_beam_meshes(elshape_body_mc):
    beam_meshes = elshape_body_mc.beam_meshes(label_space={"body": 0})
    beam_mesh = elshape_body_mc.beam_mesh(label_space={"body": 0})
    assert np.array_equal(
        beam_meshes[0].nodes.scoping.ids, beam_mesh.nodes.scoping.ids
    ), "Beam meshes and beam_mesh should have same node ids"
    assert np.array_equal(
        beam_meshes[0].elements.scoping.ids, beam_mesh.elements.scoping.ids
    ), "Beam meshes and beam_mesh should have same element ids"
    assert (
        beam_meshes[0].available_property_fields == beam_mesh.available_property_fields
    ), "Beam meshes and beam_mesh should have same property fields"


def test_beam_mesh_no_elshape_label_raises(server_type):
    mc = MeshesContainer(server=server_type)
    mc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        mc.beam_mesh()


def test_beam_mesh_invalid_label_raises(elshape_body_mc):
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.beam_mesh(label_space={"wrong_label": 0})


def test_beam_mesh_does_not_mutate_input(elshape_body_mc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_mc.beam_mesh(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_beam_mesh_has_nodes(elshape_body_mc):
    beam_mesh = elshape_body_mc.beam_mesh(label_space={"body": 0})
    assert beam_mesh.nodes.n_nodes > 0, "Beam mesh should have nodes"


def test_beam_mesh_has_elements(elshape_body_mc):
    beam_mesh = elshape_body_mc.beam_mesh(label_space={"body": 0})
    assert beam_mesh.elements.n_elements > 0, "Beam mesh should have elements"


def test_singular_and_plural_apis_consistent(elshape_body_mc):
    for plural_fn, singular_fn in [
        (elshape_body_mc.solid_meshes, elshape_body_mc.solid_mesh),
        (elshape_body_mc.shell_meshes, elshape_body_mc.shell_mesh),
        (elshape_body_mc.beam_meshes, elshape_body_mc.beam_mesh),
    ]:
        meshes = plural_fn(label_space={"body": 0})
        mesh = singular_fn(label_space={"body": 0})
        assert len(meshes) == 1, f"Expected exactly 1 mesh from {plural_fn.__name__}"
        assert np.array_equal(
            meshes[0].nodes.scoping.ids, mesh.nodes.scoping.ids
        ), f"Node ids mismatch for {plural_fn.__name__} vs {singular_fn.__name__}"
        assert np.array_equal(
            meshes[0].elements.scoping.ids, mesh.elements.scoping.ids
        ), f"Element ids mismatch for {plural_fn.__name__} vs {singular_fn.__name__}"


def test_none_label_space_same_as_default(elshape_body_mc):
    solid_none = elshape_body_mc.solid_meshes(label_space=None)
    solid_default = elshape_body_mc.solid_meshes()
    assert len(solid_none) == len(
        solid_default
    ), "None label_space should behave the same as default"


def test_empty_dict_label_space_same_as_default(elshape_body_mc):
    solid_empty = elshape_body_mc.solid_meshes(label_space={})
    solid_default = elshape_body_mc.solid_meshes()
    assert len(solid_empty) == len(
        solid_default
    ), "Empty dict label_space should behave the same as default"


def test_all_shapes_no_elshape_raises(server_type):
    mc = MeshesContainer(server=server_type)
    mc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        mc.solid_meshes()
    with pytest.raises(ValueError, match="No elshape label"):
        mc.shell_meshes()
    with pytest.raises(ValueError, match="No elshape label"):
        mc.beam_meshes()
    with pytest.raises(ValueError, match="No elshape label"):
        mc.solid_mesh()
    with pytest.raises(ValueError, match="No elshape label"):
        mc.shell_mesh()
    with pytest.raises(ValueError, match="No elshape label"):
        mc.beam_mesh()


def test_all_shapes_invalid_label_raises(elshape_body_mc):
    invalid_ls = {"nonexistent_label": 0}
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.solid_meshes(label_space=invalid_ls)
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.shell_meshes(label_space=invalid_ls)
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.beam_meshes(label_space=invalid_ls)
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.solid_mesh(label_space=invalid_ls)
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.shell_mesh(label_space=invalid_ls)
    with pytest.raises(ValueError, match="not in this mesh container"):
        elshape_body_mc.beam_mesh(label_space=invalid_ls)


def test_all_shapes_do_not_mutate_input(elshape_body_mc):
    for method in [
        elshape_body_mc.solid_meshes,
        elshape_body_mc.shell_meshes,
        elshape_body_mc.beam_meshes,
        elshape_body_mc.solid_mesh,
        elshape_body_mc.shell_mesh,
        elshape_body_mc.beam_mesh,
    ]:
        label_space = {"body": 0}
        original = label_space.copy()
        method(label_space=label_space)
        assert label_space == original, f"{method.__name__} mutated the input label_space"
