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

from ansys import dpf
import conftest
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_2_0
import copy
from ansys.dpf.core import Scoping
from ansys.dpf.core import errors as dpf_errors


def test_create_scoping():
    scop = Scoping()
    assert scop._internal_obj


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Copying data is " "supported starting server version 3.0",
)
def test_createbycopy_scoping(server_type):
    scop = Scoping(server=server_type)
    scop2 = Scoping(scoping=scop, server=server_type)
    assert scop._internal_obj != scop2._internal_obj


def test_create_scoping_with_ids_location(server_type):
    scop = Scoping(
        ids=[1, 2, 3, 5, 8, 9, 10],
        location=dpf.core.locations.elemental,
        server=server_type,
    )
    assert scop._internal_obj
    assert np.allclose(scop.ids, [1, 2, 3, 5, 8, 9, 10])
    assert scop.location == dpf.core.locations.elemental


def test_set_get_ids_scoping(server_type):
    scop = Scoping(server=server_type)
    ids = [1, 2, 3, 5, 8, 9, 10]
    scop.ids = ids
    assert np.allclose(scop.ids, ids)


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_2_0,
    reason="Requires server version higher than 2.0",
)
def test_set_get_ids_long_scoping():
    scop = Scoping()
    ids = range(1, 1000000)
    scop.ids = ids
    assert np.allclose(scop.ids, ids)
    assert len(scop) == len(ids)


def test_get_ids_return_type_scoping(server_type):
    scop = Scoping(server=server_type)
    ids = [1, 2, 3, 5, 8, 9, 10]
    scop.ids = ids
    assert np.allclose(scop.ids, ids)
    assert isinstance(scop.ids, np.ndarray)
    client_config = dpf.core.settings.get_runtime_client_config(server=server_type)
    return_arrays_init = client_config.return_arrays
    client_config.return_arrays = False
    assert np.allclose(scop.ids, ids)
    assert isinstance(scop.ids, list)
    client_config.return_arrays = return_arrays_init
    assert np.allclose(scop.ids, ids)
    assert isinstance(scop.ids, np.ndarray)
    assert np.allclose(scop._get_ids(True), ids)
    assert isinstance(scop._get_ids(True), np.ndarray)
    assert np.allclose(scop._get_ids(False), ids)
    assert isinstance(scop._get_ids(False), list)


def test_get_location_scoping():
    scop = Scoping()
    scop._set_location("Nodal")
    assert scop._get_location() == "Nodal"
    scop = Scoping()
    scop._set_location(dpf.core.locations.nodal)
    assert scop._get_location() == "Nodal"


def test_get_location_property_scoping(server_type):
    scop = Scoping(server=server_type)
    scop.location = "Nodal"
    assert scop.location == "Nodal"
    scop = Scoping(server=server_type)
    scop.location = dpf.core.locations.nodal
    assert scop.location == "Nodal"


def test_count_scoping():
    scop = Scoping()
    ids = [1, 2, 3, 5, 8, 9, 10]
    scop.ids = ids
    assert scop._count() == len(ids)


def test_set_get_entity_data_scoping(server_type):
    scop = Scoping(server=server_type)
    ids = [1, 2, 3, 5, 8, 9, 10]
    scop.ids = ids
    scop.set_id(0, 11)
    assert scop._get_id(0) == 11
    assert scop._get_index(11) == 0
    scop.set_id(1, 12)
    assert scop._get_id(1) == 12
    assert scop._get_index(12) == 1


def test_print_scoping():
    scop = Scoping()
    ids = [1, 2, 3, 5, 8, 9, 10]
    scop.ids = ids
    assert str(scop)


def test_documentation_string_on_scoping(server_type):
    scop = Scoping(server=server_type)
    ids = [1, 2, 3, 5, 8, 9, 10]
    scop.ids = ids
    scop.location = "blabla"
    to_check = str(scop)
    assert "location" in to_check
    assert "blabla" in to_check
    assert "7 entities" in to_check


def test_iter_scoping(server_type):
    scop = Scoping(server=server_type)
    ids = [1, 2, 3, 5, 8, 9, 10]
    scop.ids = ids
    for i, id in enumerate(scop):
        assert id == ids[i]


def test_delete_scoping(server_type):
    scop = Scoping(server=server_type)
    del scop
    with pytest.raises(Exception):
        scop.ids


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Copying data is supported starting server version 3.0",
)
def test_delete_auto_scoping(server_type):
    scop = Scoping(server=server_type)
    scop2 = Scoping(scoping=scop)
    del scop
    assert np.allclose(scop2.ids, [])


@pytest.mark.skipif(
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_2_0,
    reason="Requires server version below (or equal) than 2.0",
)
def test_throw_if_unsufficient_version():
    scop = Scoping()
    ids = range(1, int(2e6))
    with pytest.raises(dpf_errors.DpfVersionNotSupported):
        scop.ids = ids
    ids = range(1, int(3e6))
    with pytest.raises(dpf_errors.DpfVersionNotSupported):
        scop.ids = ids
    ids = range(1, 2000)
    scop.ids = ids
    ids_check = scop.ids
    assert np.allclose(ids, ids_check)


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_2_0,
    reason="Requires server version higher than 2.0",
)
def test_field_with_scoping_many_ids(allkindofcomplexity, server_type):
    # set scoping ids with a scoping created from a model
    model = dpf.core.Model(allkindofcomplexity, server=server_type)
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
    scop = dpf.core.Scoping(server=server_type)
    ids = range(1, 1000000)
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
    scop.ids = range(1, int(8e6 / 28))
    assert np.allclose(scop.ids, range(1, int(8e6 / 28)))
    try:
        scop.ids = range(1, int(8.2e6 / 28))
    except:
        return  # check that either more than 8MB works or it throws

    assert np.allclose(scop.ids, range(1, int(8.2e6 / 28)))


def test_as_local_scoping():
    scop = Scoping()
    with scop.as_local_scoping() as loc:
        loc.location = "Nodal"
        for i in range(0, 100):
            loc.append(i + 1)
            assert loc.id(i) == i + 1
            assert loc.index(i + 1) == i
        assert hasattr(loc, "_is_set") is True
        assert loc._is_set is True
    assert np.allclose(scop.ids, list(range(1, 101)))
    assert scop.location == "Nodal"
    with scop.as_local_scoping() as loc:
        assert loc.location == "Nodal"
        for i in range(0, 100):
            assert loc.id(i) == i + 1
            assert loc.index(i + 1) == i
        assert hasattr(loc, "_is_set") is False


def test_as_local_scoping2():
    scop = Scoping()
    with scop.as_local_scoping() as loc:
        loc.location = "Nodal"
        loc.ids = range(1, 101)
        for i in range(0, 100):
            assert loc.id(i) == i + 1
            assert loc.index(i + 1) == i
        assert hasattr(loc, "_is_set") is True
        assert loc._is_set is True
    assert np.allclose(scop.ids, list(range(1, 101)))
    assert scop.location == "Nodal"
    with scop.as_local_scoping() as loc:
        assert loc.location == "Nodal"
        for i in range(0, 100):
            assert loc.id(i) == i + 1
            assert loc.index(i + 1) == i
        assert hasattr(loc, "_is_set") is False


def test_auto_delete_scoping_local():
    scop = Scoping()
    s = scop.as_local_scoping()
    s.append(1)
    del s
    with scop.as_local_scoping() as s:
        assert s[0] == 1


@conftest.raises_for_servers_version_under("4.0")
def test_mutable_ids_data(server_clayer):
    scop = Scoping(server=server_clayer)
    scop.ids = range(1, int(2e6))
    data = scop.ids
    data_copy = copy.deepcopy(data)
    data[0] += 1
    data.commit()
    changed_data = scop.ids
    assert np.allclose(changed_data, data)
    assert not np.allclose(changed_data, data_copy)
    assert np.allclose(changed_data[0], data_copy[0] + 1)
    data[0] += 1
    data = None
    changed_data = scop.ids
    assert np.allclose(changed_data[0], data_copy[0] + 2)


def test_scoping_dont_start_server(server_type):
    s = dpf.core.server._global_server()
    dpf.core.SERVER = None
    assert not dpf.core.server.has_local_server()
    scop = Scoping(server=server_type)
    assert not dpf.core.server.has_local_server()
    ids = [1, 2, 3, 5, 8, 9, 10]
    scop.ids = ids
    scop = Scoping(scoping=scop)
    assert not dpf.core.server.has_local_server()
    assert np.allclose(scop.ids, ids)
    dpf.core.SERVER = s
