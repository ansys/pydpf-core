# -*- coding: utf-8 -*-

import weakref

import pytest

from ansys import dpf
from ansys.dpf.core import MeshesContainer, MeshedRegion
from ansys.dpf.core import errors as dpf_errors


@pytest.fixture()
def dummy_mesh(allkindofcomplexity):
    """Returns a mesh"""
    model = dpf.core.Model(allkindofcomplexity)
    return model.metadata.meshed_region

@pytest.fixture()
def elshape_body_mc(dummy_mesh):
    """Returns a meshes container with 20 mesh splitted on body and elshape"""
    mc= MeshesContainer()
    mc.labels =['elshape','body']
    for i in range(0,20):
        mscop = {"elshape":i+1,"body":0}
        mc.add_mesh(mscop,dummy_mesh)
    return mc



def test_create_meshes_container():
    mc = MeshesContainer()
    assert mc._message.id != 0


def test_empty_index():
    mc = MeshesContainer()
    with pytest.raises(IndexError):
        mc[0]


def test_createby_message_copy_meshes_container():
    mc= MeshesContainer()
    meshes_container2 = MeshesContainer(meshes_container=mc._message)
    assert mc._message.id == meshes_container2._message.id


def test_createbycopy_meshes_container():
    mc= MeshesContainer()
    meshes_container2 = MeshesContainer(meshes_container=mc)
    assert mc._message.id == meshes_container2._message.id


def test_set_get_mesh_meshes_container(elshape_body_mc): 
    mc =elshape_body_mc
    assert mc.get_available_ids_for_label("elshape") == list(range(1,21))
    for i in range(0,20):
        meshid =mc.get_meshes({"elshape":i+1,"body":0})._message.id
        assert meshid !=0
        assert mc.get_meshes(i)._message.id !=0
        assert mc.get_meshes({"elshape":i+1,"body":0})._message.id !=0
        assert mc[i]._message.id != 0


def test_set_get_mesh_meshes_container_new_label(elshape_body_mc, dummy_mesh): 
    mc =elshape_body_mc
    assert mc.get_available_ids_for_label("elshape") == list(range(1,21))
    for i in range(0,20):
        meshid =mc.get_meshes({"elshape":i+1,"body":0})._message.id
        assert meshid !=0
        assert mc.get_meshes(i)._message.id !=0
        assert mc.get_meshes({"elshape":i+1,"body":0})._message.id !=0
        assert mc[i]._message.id != 0
        assert mc.get_label_space(i)=={"elshape":i+1,"body":0}
       
    mc.add_label('time')
    for i in range(0,20):
        mscop ={"elshape":i+1,"body":0, "time":1}
        mc.add_mesh(mscop,dummy_mesh)
    assert len(mc.get_meshes({"elshape":i+1,"body":0}))==2
    for i in range(0,20):
        meshid =mc.get_meshes({"elshape":i+1,"body":0, "time":1})._message.id
        assert meshid !=0
        assert mc.get_meshes(i+20)._message.id !=0
        assert mc[i]._message.id != 0
        assert mc.get_label_space(i+20)=={"elshape":i+1,"body":0, "time":1}
        assert mc.get_meshes({"elshape":i+1,"body":0, "time":1})._message.id !=0
        assert mc.get_meshes({"elshape":i+1, "time":1})._message.id !=0


def test_get_item_mesh_meshes_container(elshape_body_mc): 
    mc =elshape_body_mc
    for i in range(0,20):
        assert mc[i]._message.id !=0


def test_delete_meshes_container():
    mc = MeshesContainer()
    ref = weakref.ref(mc)
    del mc
    assert ref() is None


# @pytest.mark.skipif(ON_WINDOWS_AZURE, reason='Causes segfault on Azure')
def test_delete_auto_meshes_container():
    mc = MeshesContainer()
    sc2 = MeshesContainer(meshes_container=mc)
    del mc
    with pytest.raises(dpf_errors.DPFServerNullObject):
        sc2._info


def test_str_meshes_container(elshape_body_mc): 
    mc =elshape_body_mc
    assert 'body' in str(mc)

