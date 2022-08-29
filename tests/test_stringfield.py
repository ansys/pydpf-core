import numpy as np
import conftest

from ansys import dpf
from ansys.dpf import core
from ansys.dpf.core.common import locations


@conftest.raises_for_servers_version_under("5.0")
def test_scopingdata_string_field(server_type):
    pfield = dpf.core.StringField(server=server_type)
    list_ids = [1, 2, 4, 6, 7]
    assert pfield.data == []
    scop = core.Scoping(ids=list_ids, location=locations.nodal, server=server_type)
    pfield.scoping = scop
    list_data = ["water", "oil", "gaz", "paint", "air"]
    pfield.data = list_data
    pfield.data
    assert pfield.data == list_data
    assert np.allclose(pfield.scoping.ids, list_ids)
    pfield.data = np.asarray(list_data)
    assert pfield.data == list_data


@conftest.raises_for_servers_version_under("5.0")
def test_set_get_data_string_field(server_type):
    field = dpf.core.StringField(nentities=20, server=server_type)
    data = []
    for i in range(0, 20):
        data.append("bla")
    field.data = data
    assert field.data == data
    data.append("true")
    assert field.data != data


@conftest.raises_for_servers_version_under("5.0")
def test_create_string_field_push_back(server_type):
    f_vec = core.StringField(1, server=server_type)
    vec = ["water", "oil", "gaz"]
    f_vec.append(vec, 1)
    assert len(f_vec.data) == 3
    assert f_vec.data[0] == vec[0]
    assert f_vec.data[1] == vec[1]
    assert f_vec.data[2] == vec[2]
    assert f_vec.scoping.ids == [1]
    assert len(f_vec.scoping.ids) == 1

    f_scal = core.StringField(1, server=server_type)
    f_scal.append(["blo"], 1)
    f_scal.append(["blu"], 2)
    assert len(f_scal.data) == 2
    assert f_scal.data[0] == "blo"
    assert f_scal.data[1] == "blu"
    assert len(f_scal.scoping.ids) == 2
    assert f_scal.scoping.ids[0] == 1
    assert f_scal.scoping.ids[1] == 2
    f_scal.append(np.asarray(["blu"]), 3)
    assert f_scal.data[2] == "blu"


@conftest.raises_for_servers_version_under("5.0")
def test_entity_data_string_field(server_type):
    f_vec = core.StringField(1, server=server_type)
    vec = ["water", "oil", "gaz"]
    f_vec.append(vec, 1)
    vec = ["wat"]
    f_vec.append(vec, 2)
    vec = ["gaz"]
    f_vec.append(vec, 3)
    assert f_vec.get_entity_data(0) == ["water", "oil", "gaz"]
    assert f_vec.get_entity_data(1) == ["wat"]
    assert f_vec.get_entity_data(2) == ["gaz"]
    assert f_vec.get_entity_data_by_id(1) == ["water", "oil", "gaz"]
    assert f_vec.get_entity_data_by_id(2) == ["wat"]
    assert f_vec.get_entity_data_by_id(3) == ["gaz"]

