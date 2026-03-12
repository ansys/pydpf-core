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

import pytest

from ansys import dpf
from ansys.dpf.core import MeshesContainer
import conftest


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


def test_get_mesh_by_elshape_APIS(elshape_body_mc):
    import numpy as np

    mc = elshape_body_mc

    shell_meshes = mc.shell_meshes()

    assert len(shell_meshes) == 1, f"Expected 1 shell mesh, got {len(shell_meshes)}"

    solid_meshes = mc.solid_meshes()
    assert len(solid_meshes) == 1, f"Expected 1 solid mesh, got {len(solid_meshes)}"

    beam_meshes = mc.beam_meshes()
    assert len(beam_meshes) == 1, f"Expected 1 beam mesh, got {len(beam_meshes)}"

    shell_mesh = mc.shell_mesh(label_space={"body": 0})
    assert np.array_equal(
        shell_meshes[0].nodes.scoping.ids, shell_mesh.nodes.scoping.ids
    ), "Shell meshes should have same node ids"
    assert np.array_equal(
        shell_meshes[0].elements.scoping.ids, shell_mesh.elements.scoping.ids
    ), "Shell meshes should have same element ids"
    assert (
        shell_meshes[0].available_property_fields == shell_mesh.available_property_fields
    ), "Shell meshes should have same property fields"

    solid_mesh = mc.solid_mesh(label_space={"body": 0})
    assert np.array_equal(
        solid_meshes[0].nodes.scoping.ids, solid_mesh.nodes.scoping.ids
    ), "Solid meshes should have same node ids"
    assert np.array_equal(
        solid_meshes[0].elements.scoping.ids, solid_mesh.elements.scoping.ids
    ), "Solid meshes should have same element ids"
    assert (
        solid_meshes[0].available_property_fields == solid_mesh.available_property_fields
    ), "Solid meshes should have same property fields"

    beam_mesh = mc.beam_mesh(label_space={"body": 0})
    assert np.array_equal(
        beam_meshes[0].nodes.scoping.ids, beam_mesh.nodes.scoping.ids
    ), "Beam meshes should have same node ids"
    assert np.array_equal(
        beam_meshes[0].elements.scoping.ids, beam_mesh.elements.scoping.ids
    ), "Beam meshes should have same element ids"
    assert (
        beam_meshes[0].available_property_fields == beam_mesh.available_property_fields
    ), "Beam meshes should have same property fields"
