import pytest
import numpy as np

from ansys import dpf
from ansys.dpf.core import Scoping
import numpy as np
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core.check_version import meets_version, get_server_version

serv = dpf.core.start_local_server('127.0.0.1', 50075)
SERVER_VERSION_HIGHER_THAN_2_0 = meets_version(get_server_version(serv), "2.1")
# serv.shutdown()

def test_create_scoping():
    scop = Scoping()
    assert scop._message.id


def test_createbycopy_scoping():
    scop = Scoping()
    scop2 = Scoping(scoping=scop._message)
    assert scop._message.id == scop2._message.id


def test_create_scoping_with_ids_location():
    scop = Scoping(ids=[1,2,3,5,8,9,10], location=dpf.core.locations.elemental)
    assert scop._message.id
    assert scop.ids == [1,2,3,5,8,9,10]
    assert scop.location == dpf.core.locations.elemental


def test_set_get_ids_scoping():
    scop = Scoping()
    ids=[1,2,3,5,8,9,10]
    scop.ids = ids
    assert scop.ids == ids

@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_2_0, reason='Requires server version higher than 2.0')
def test_set_get_ids_long_scoping():
    scop = Scoping()
    ids=range(1,1000000)
    scop.ids = ids
    assert np.allclose(scop.ids,ids)


def test_get_location_scoping():
    scop = Scoping()
    scop._set_location("Nodal")
    assert scop._get_location() == "Nodal"
    scop = Scoping()
    scop._set_location(dpf.core.locations.nodal)
    assert scop._get_location() == "Nodal"


def test_get_location_property_scoping():
    scop = Scoping()
    scop.location = "Nodal"
    assert scop.location == "Nodal"
    scop = Scoping()
    scop.location = dpf.core.locations.nodal
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
    

def test_print_scoping():
    scop = Scoping()
    ids=[1,2,3,5,8,9,10]
    scop.ids= ids 
    print(scop)

def test_iter_scoping():
    scop = Scoping()
    ids=[1,2,3,5,8,9,10]
    scop.ids =ids
    for i,id in enumerate(scop):
        assert id == ids[i]

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

@pytest.mark.skipif(SERVER_VERSION_HIGHER_THAN_2_0, reason='Requires server version below (or equal) than 2.0')
def test_throw_if_unsufficient_version():
    scop = Scoping()
    ids = range(1, int(2e6))
    with pytest.raises(dpf_errors.DpfVersionNotSupported):
        scop.ids = ids
    ids = range(1,  int(3e6))
    with pytest.raises(dpf_errors.DpfVersionNotSupported):
        scop.ids = ids
    ids = range(1, 2000)
    scop.ids = ids
    ids_check = scop.ids
    assert np.allclose(ids, ids_check)

@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_2_0, reason='Requires server version higher than 2.0')
def test_field_with_scoping_many_ids(allkindofcomplexity):
    # set scoping ids with a scoping created from a model
    model = dpf.core.Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    nnodes = mesh.nodes.n_nodes
    assert nnodes == 15129
    nod_ids = mesh.nodes.scoping.ids
    mesh.nodes.scoping.ids = nod_ids
    new_nod_ids = mesh.nodes.scoping.ids
    assert np.allclose(nod_ids, new_nod_ids)
    modif_nod_ids = nod_ids
    modif_nod_ids[245] = 45
    modif_nod_ids[1129] = 69
    modif_nod_ids[1999] = 2086
    modif_nod_ids[9046] = 12
    modif_nod_ids[12907] = 7894
    modif_nod_ids[15128] = 2789
    mesh.nodes.scoping.ids = modif_nod_ids
    new_modif_nod_ids = mesh.nodes.scoping.ids
    assert np.allclose(new_modif_nod_ids, modif_nod_ids)
    
    # set scoping ids with a scoping created from scratch
    scop = dpf.core.Scoping()
    ids=range(1,1000000)
    scop.ids = ids
    ids_check = scop.ids
    assert np.allclose(ids_check, ids)
    modif_ids = ids_check
    modif_ids[245] = 45
    modif_ids[10046] = 69
    modif_ids[1999] = 2086
    modif_ids[50067] = 12
    modif_ids[999345] = 7894
    modif_ids[506734] = 2789
    # np.ndarray
    scop.ids = np.array(modif_ids)
    new_modif_ids = scop.ids
    assert np.allclose(new_modif_ids, modif_ids)
    # list
    modif_ids = modif_ids
    scop.ids = modif_ids
    new_modif_ids = scop.ids
    assert np.allclose(new_modif_ids, modif_ids)
    
    
def test_largest_set_ids_one_shot():
    scop = dpf.core.Scoping()
    scop.ids = range(1, int(8e6/28))
    assert np.allclose( scop.ids,range(1, int(8e6/28)))
    try :
        scop.ids = range(1, int(8.2e6/28))
    except :
        return #check that either more than 8MB works or it throws
    
    assert np.allclose( scop.ids,range(1, int(8.2e6/28)))
    