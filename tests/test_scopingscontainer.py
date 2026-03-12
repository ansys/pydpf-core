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

from ansys.dpf.core import Scoping, ScopingsContainer
import conftest


@pytest.fixture()
def elshape_body_sc(server_type):
    """Returns a scopings container with 20 scoping split on body and elshape"""
    sc = ScopingsContainer(server=server_type)
    sc.labels = ["elshape", "body"]
    for i in range(0, 20):
        mscop = {"elshape": i, "body": 0}
        scop = Scoping(server=server_type)
        scop.ids = range(0, i)
        sc.add_scoping(mscop, scop)
    return sc


def test_create_scopings_container(server_type):
    sc = ScopingsContainer(server=server_type)
    assert sc._internal_obj is not None


def test_empty_index(server_type):
    sc = ScopingsContainer(server=server_type)
    with pytest.raises(IndexError):
        sc[0]


def test_createby_message_copy_scopings_container(server_type_legacy_grpc):
    sc = ScopingsContainer(server=server_type_legacy_grpc)
    scopings_container2 = ScopingsContainer(
        scopings_container=sc._internal_obj, server=server_type_legacy_grpc
    )
    assert sc._internal_obj == scopings_container2._internal_obj


def test_createbycopy_scopings_container(server_type):
    sc = ScopingsContainer(server=server_type)
    scopings_container2 = ScopingsContainer(scopings_container=sc)
    assert sc._internal_obj != scopings_container2._internal_obj


def test_set_get_scoping_scopings_container(elshape_body_sc):
    sc = elshape_body_sc
    assert sc.get_available_ids_for_label("elshape") == list(range(0, 20))
    for i in range(0, 20):
        scopingid = sc.get_scoping({"elshape": i, "body": 0})._internal_obj is not None
        assert scopingid != 0
        assert sc.get_scoping(i)._internal_obj is not None
        assert sc.get_scoping({"elshape": i, "body": 0})._internal_obj is not None
        assert np.allclose(sc.get_scoping({"elshape": i, "body": 0}).ids, list(range(0, i)))
        assert sc[i]._internal_obj is not None


def test_set_get_scoping_scopings_container_new_label(elshape_body_sc):
    sc = elshape_body_sc
    assert sc.get_available_ids_for_label("elshape") == list(range(0, 20))
    for i in range(0, 20):
        scopingid = sc.get_scoping({"elshape": i, "body": 0})._internal_obj
        assert scopingid is not None
        assert sc.get_scoping(i)._internal_obj is not None
        assert sc.get_scoping({"elshape": i, "body": 0})._internal_obj is not None
        assert sc[i]._internal_obj is not None
        assert sc.get_label_space(i) == {"elshape": i, "body": 0}
        assert np.allclose(sc.get_scoping({"elshape": i, "body": 0}).ids, list(range(0, i)))
    sc.add_label("time")
    for i in range(0, 20):
        mscop = {"elshape": i, "body": 0, "time": 1}
        scop = Scoping(server=sc._server)
        scop.ids = range(0, i + 10)
        sc.add_scoping(mscop, scop)
    assert len(sc.get_scopings({"elshape": i, "body": 0})) == 2
    for i in range(0, 20):
        scopingid = (
            sc.get_scoping({"elshape": i, "body": 0, "time": 1})._internal_obj is not None
        )
        assert scopingid != 0
        assert sc.get_scoping(i + 20)._internal_obj is not None
        assert sc[i]._internal_obj is not None
        assert sc.get_label_space(i + 20) == {"elshape": i, "body": 0, "time": 1}
        assert np.allclose(
            sc.get_scoping({"elshape": i, "body": 0, "time": 1}).ids,
            list(range(0, i + 10)),
        )
        assert np.allclose(
            sc.get_scoping({"elshape": i, "time": 1}).ids, list(range(0, i + 10))
        )


def test_get_item_scoping_scopings_container(elshape_body_sc):
    sc = elshape_body_sc
    for i in range(0, 20):
        assert sc[i]._internal_obj is not None
        assert np.allclose(sc[i].ids, list(range(0, i)))


def test_delete_scopings_container(server_type):
    sc = ScopingsContainer()
    ref = weakref.ref(sc)
    del sc
    assert ref() is None


def test_str_scopings_container(elshape_body_sc):
    sc = elshape_body_sc
    assert "body" in str(sc)


def test_get_scoping_by_elshape_APIS(elshape_body_sc):
    sc = elshape_body_sc

    shell_scopings = sc.shell_scopings()
    assert len(shell_scopings) == 1, f"Expected 1 shell scoping, got {len(shell_scopings)}"

    solid_scopings = sc.solid_scopings()
    assert len(solid_scopings) == 1, f"Expected 1 solid scoping, got {len(solid_scopings)}"

    beam_scopings = sc.beam_scopings()
    assert len(beam_scopings) == 1, f"Expected 1 beam scoping, got {len(beam_scopings)}"

    shell_scoping = sc.shell_scoping(label_space={"body": 0})
    import numpy as np

    assert np.array_equal(
        shell_scopings[0].ids, shell_scoping.ids
    ), "Shell scopings should have same ids"
    assert (
        shell_scopings[0].location == shell_scoping.location
    ), "Shell scopings should have same location"

    solid_scoping = sc.solid_scoping(label_space={"body": 0})
    assert np.array_equal(
        solid_scopings[0].ids, solid_scoping.ids
    ), "Solid scopings should have same ids"
    assert (
        solid_scopings[0].location == solid_scoping.location
    ), "Solid scopings should have same location"

    beam_scoping = sc.beam_scoping(label_space={"body": 0})
    assert np.array_equal(
        beam_scopings[0].ids, beam_scoping.ids
    ), "Beam scopings should have same ids"
    assert (
        beam_scopings[0].location == beam_scoping.location
    ), "Beam scopings should have same location"
