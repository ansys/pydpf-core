# -*- coding: utf-8 -*-

import weakref

import pytest

import conftest
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
        mscop = {"elshape": i + 1, "body": 0}
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


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_createbycopy_meshes_container(server_type):
    mc = MeshesContainer(server=server_type)
    meshes_container2 = MeshesContainer(meshes_container=mc)
    assert mc._internal_obj != meshes_container2._internal_obj


def test_set_get_mesh_meshes_container(elshape_body_mc):
    mc = elshape_body_mc
    assert mc.get_available_ids_for_label("elshape") == list(range(1, 21))
    for i in range(0, 20):
        mesh = mc.get_mesh({"elshape": i + 1, "body": 0})._internal_obj
        assert mesh is not None
        assert mc.get_mesh(i)._internal_obj is not None
        assert mc.get_mesh({"elshape": i + 1, "body": 0})._internal_obj is not None
        assert mc[i]._internal_obj is not None


def test_set_get_mesh_meshes_container_new_label(elshape_body_mc, dummy_mesh):
    mc = elshape_body_mc
    assert mc.get_available_ids_for_label("elshape") == list(range(1, 21))
    for i in range(0, 20):
        mesh = mc.get_mesh({"elshape": i + 1, "body": 0})._internal_obj
        assert mesh is not None
        assert mc.get_mesh(i)._internal_obj is not None
        assert mc.get_mesh({"elshape": i + 1, "body": 0})._internal_obj is not None
        assert mc[i]._internal_obj is not None
        assert mc.get_label_space(i) == {"elshape": i + 1, "body": 0}

    mc.add_label("time")
    for i in range(0, 20):
        mscop = {"elshape": i + 1, "body": 0, "time": 1}
        mc.add_mesh(mscop, dummy_mesh)
    assert len(mc.get_meshes({"elshape": i + 1, "body": 0})) == 2
    for i in range(0, 20):
        mesh = mc.get_mesh({"elshape": i + 1, "body": 0, "time": 1})._internal_obj
        assert mesh is not None
        assert mc.get_mesh(i + 20)._internal_obj is not None
        assert mc[i]._internal_obj is not None
        assert mc.get_label_space(i + 20) == {"elshape": i + 1, "body": 0, "time": 1}
        assert mc.get_mesh({"elshape": i + 1, "body": 0, "time": 1})._internal_obj is not None
        assert mc.get_mesh({"elshape": i + 1, "time": 1})._internal_obj is not None


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
