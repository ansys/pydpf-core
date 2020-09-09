import pytest

from ansys import dpf
from ansys.dpf import Scoping

if not dpf.has_local_server():
    dpf.start_local_server()


def test_create_scoping():
    scop = Scoping()
    assert scop._message.id


def test_createbycopy_scoping():
    scop = Scoping()
    scop2 = Scoping(scoping=scop._message)
    assert scop._message.id == scop2._message.id


def test_set_get_ids_scoping():
    scop = Scoping()
    ids=[1,2,3,5,8,9,10]
    scop.ids = ids
    assert scop.ids == ids


def test_get_location_scoping():
    scop = Scoping()
    scop._set_location("Nodal")
    assert scop._get_location() == "Nodal"
    scop = Scoping()
    scop._set_location(dpf.locations.nodal)
    assert scop._get_location() == "Nodal"

    
def test_get_location_property_scoping():
    scop = Scoping()
    scop.location = "Nodal"
    assert scop.location == "Nodal"
    scop = Scoping()
    scop.location = dpf.locations.nodal
    assert scop.location == "Nodal"


def test_count_scoping():
    scop = Scoping()
    ids=[1,2,3,5,8,9,10]
    scop.ids = ids
    assert scop._count() == len(ids)


def test_set_get_entity_data_scoping():
    scop = Scoping()
    ids=[1,2,3,5,8,9,10]
    scop.ids= ids 
    scop.set_id(0,11)
    assert scop._get_id(0)==11
    assert scop._get_index(11)==0
    scop.set_id(1,12)
    assert scop._get_id(1)==12
    assert scop._get_index(12)==1


def test_delete_scoping():
    scop = Scoping()
    scop.__del__()
    with pytest.raises(Exception):
        scop.ids


def test_delete_auto_scoping():
    scop = Scoping()
    scop2 = Scoping(scoping=scop)
    scop.__del__()
    with pytest.raises(Exception):
        scop2.ids
