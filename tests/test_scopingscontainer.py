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
        scopingid = sc.get_scoping({"elshape": i, "body": 0, "time": 1})._internal_obj is not None
        assert scopingid != 0
        assert sc.get_scoping(i + 20)._internal_obj is not None
        assert sc[i]._internal_obj is not None
        assert sc.get_label_space(i + 20) == {"elshape": i, "body": 0, "time": 1}
        assert np.allclose(
            sc.get_scoping({"elshape": i, "body": 0, "time": 1}).ids,
            list(range(0, i + 10)),
        )
        assert np.allclose(sc.get_scoping({"elshape": i, "time": 1}).ids, list(range(0, i + 10)))


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


def test_solid_scopings_returns_list(elshape_body_sc):
    result = elshape_body_sc.solid_scopings()
    assert isinstance(result, list), "solid_scopings should return a list"


def test_solid_scopings_no_label_space(elshape_body_sc):
    solid_scopings = elshape_body_sc.solid_scopings()
    assert len(solid_scopings) == 1, f"Expected 1 solid scoping, got {len(solid_scopings)}"


def test_solid_scopings_with_label_space(elshape_body_sc):
    solid_scopings = elshape_body_sc.solid_scopings(label_space={"body": 0})
    assert len(solid_scopings) == 1, f"Expected 1 solid scoping, got {len(solid_scopings)}"


def test_solid_scopings_returns_scoping_instances(elshape_body_sc):
    solid_scopings = elshape_body_sc.solid_scopings()
    for scop in solid_scopings:
        assert isinstance(scop, Scoping), "Each element should be a Scoping"


def test_solid_scopings_no_elshape_label_raises(server_type):
    sc = ScopingsContainer(server=server_type)
    sc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        sc.solid_scopings()


def test_solid_scopings_invalid_label_raises(elshape_body_sc):
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.solid_scopings(label_space={"invalid_label": 0})


def test_solid_scopings_does_not_mutate_input(elshape_body_sc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_sc.solid_scopings(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_shell_scopings_returns_list(elshape_body_sc):
    result = elshape_body_sc.shell_scopings()
    assert isinstance(result, list), "shell_scopings should return a list"


def test_shell_scopings_no_label_space(elshape_body_sc):
    shell_scopings = elshape_body_sc.shell_scopings()
    assert len(shell_scopings) == 1, f"Expected 1 shell scoping, got {len(shell_scopings)}"


def test_shell_scopings_with_label_space(elshape_body_sc):
    shell_scopings = elshape_body_sc.shell_scopings(label_space={"body": 0})
    assert len(shell_scopings) == 1, f"Expected 1 shell scoping, got {len(shell_scopings)}"


def test_shell_scopings_returns_scoping_instances(elshape_body_sc):
    shell_scopings = elshape_body_sc.shell_scopings()
    for scop in shell_scopings:
        assert isinstance(scop, Scoping), "Each element should be a Scoping"


def test_shell_scopings_no_elshape_label_raises(server_type):
    sc = ScopingsContainer(server=server_type)
    sc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        sc.shell_scopings()


def test_shell_scopings_invalid_label_raises(elshape_body_sc):
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.shell_scopings(label_space={"nonexistent": 0})


def test_shell_scopings_does_not_mutate_input(elshape_body_sc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_sc.shell_scopings(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_beam_scopings_returns_list(elshape_body_sc):
    result = elshape_body_sc.beam_scopings()
    assert isinstance(result, list), "beam_scopings should return a list"


def test_beam_scopings_no_label_space(elshape_body_sc):
    beam_scopings = elshape_body_sc.beam_scopings()
    assert len(beam_scopings) == 1, f"Expected 1 beam scoping, got {len(beam_scopings)}"


def test_beam_scopings_with_label_space(elshape_body_sc):
    beam_scopings = elshape_body_sc.beam_scopings(label_space={"body": 0})
    assert len(beam_scopings) == 1, f"Expected 1 beam scoping, got {len(beam_scopings)}"


def test_beam_scopings_returns_scoping_instances(elshape_body_sc):
    beam_scopings = elshape_body_sc.beam_scopings()
    for scop in beam_scopings:
        assert isinstance(scop, Scoping), "Each element should be a Scoping"


def test_beam_scopings_no_elshape_label_raises(server_type):
    sc = ScopingsContainer(server=server_type)
    sc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        sc.beam_scopings()


def test_beam_scopings_invalid_label_raises(elshape_body_sc):
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.beam_scopings(label_space={"fake_label": 99})


def test_beam_scopings_does_not_mutate_input(elshape_body_sc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_sc.beam_scopings(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_solid_scoping_returns_scoping(elshape_body_sc):
    solid_scoping = elshape_body_sc.solid_scoping(label_space={"body": 0})
    assert isinstance(solid_scoping, Scoping), "solid_scoping should return a Scoping"


def test_solid_scoping_consistent_with_solid_scopings(elshape_body_sc):
    solid_scopings = elshape_body_sc.solid_scopings(label_space={"body": 0})
    solid_scoping = elshape_body_sc.solid_scoping(label_space={"body": 0})
    assert np.array_equal(
        solid_scopings[0].ids, solid_scoping.ids
    ), "solid_scopings and solid_scoping should have same ids"
    assert (
        solid_scopings[0].location == solid_scoping.location
    ), "solid_scopings and solid_scoping should have same location"


def test_solid_scoping_no_elshape_label_raises(server_type):
    sc = ScopingsContainer(server=server_type)
    sc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        sc.solid_scoping()


def test_solid_scoping_invalid_label_raises(elshape_body_sc):
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.solid_scoping(label_space={"wrong_label": 0})


def test_solid_scoping_does_not_mutate_input(elshape_body_sc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_sc.solid_scoping(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_solid_scoping_has_ids(elshape_body_sc):
    solid_scoping = elshape_body_sc.solid_scoping(label_space={"body": 0})
    assert solid_scoping.ids is not None, "Solid scoping should have ids"


def test_shell_scoping_returns_scoping(elshape_body_sc):
    shell_scoping = elshape_body_sc.shell_scoping(label_space={"body": 0})
    assert isinstance(shell_scoping, Scoping), "shell_scoping should return a Scoping"


def test_shell_scoping_consistent_with_shell_scopings(elshape_body_sc):
    shell_scopings = elshape_body_sc.shell_scopings(label_space={"body": 0})
    shell_scoping = elshape_body_sc.shell_scoping(label_space={"body": 0})
    assert np.array_equal(
        shell_scopings[0].ids, shell_scoping.ids
    ), "shell_scopings and shell_scoping should have same ids"
    assert (
        shell_scopings[0].location == shell_scoping.location
    ), "shell_scopings and shell_scoping should have same location"


def test_shell_scoping_no_elshape_label_raises(server_type):
    sc = ScopingsContainer(server=server_type)
    sc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        sc.shell_scoping()


def test_shell_scoping_invalid_label_raises(elshape_body_sc):
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.shell_scoping(label_space={"wrong_label": 0})


def test_shell_scoping_does_not_mutate_input(elshape_body_sc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_sc.shell_scoping(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_shell_scoping_has_ids(elshape_body_sc):
    shell_scoping = elshape_body_sc.shell_scoping(label_space={"body": 0})
    assert shell_scoping.ids is not None, "Shell scoping should have ids"


def test_beam_scoping_returns_scoping(elshape_body_sc):
    beam_scoping = elshape_body_sc.beam_scoping(label_space={"body": 0})
    assert isinstance(beam_scoping, Scoping), "beam_scoping should return a Scoping"


def test_beam_scoping_consistent_with_beam_scopings(elshape_body_sc):
    beam_scopings = elshape_body_sc.beam_scopings(label_space={"body": 0})
    beam_scoping = elshape_body_sc.beam_scoping(label_space={"body": 0})
    assert np.array_equal(
        beam_scopings[0].ids, beam_scoping.ids
    ), "beam_scopings and beam_scoping should have same ids"
    assert (
        beam_scopings[0].location == beam_scoping.location
    ), "beam_scopings and beam_scoping should have same location"


def test_beam_scoping_no_elshape_label_raises(server_type):
    sc = ScopingsContainer(server=server_type)
    sc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        sc.beam_scoping()


def test_beam_scoping_invalid_label_raises(elshape_body_sc):
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.beam_scoping(label_space={"wrong_label": 0})


def test_beam_scoping_does_not_mutate_input(elshape_body_sc):
    label_space = {"body": 0}
    original = label_space.copy()
    elshape_body_sc.beam_scoping(label_space=label_space)
    assert label_space == original, "Input label_space should not be mutated"


def test_beam_scoping_has_ids(elshape_body_sc):
    beam_scoping = elshape_body_sc.beam_scoping(label_space={"body": 0})
    assert beam_scoping.ids is not None, "Beam scoping should have ids"


def test_singular_and_plural_scoping_apis_consistent(elshape_body_sc):
    for plural_fn, singular_fn in [
        (elshape_body_sc.solid_scopings, elshape_body_sc.solid_scoping),
        (elshape_body_sc.shell_scopings, elshape_body_sc.shell_scoping),
        (elshape_body_sc.beam_scopings, elshape_body_sc.beam_scoping),
    ]:
        scopings = plural_fn(label_space={"body": 0})
        scoping_single = singular_fn(label_space={"body": 0})
        assert len(scopings) == 1, f"Expected exactly 1 scoping from {plural_fn.__name__}"
        assert np.array_equal(
            scopings[0].ids, scoping_single.ids
        ), f"Ids mismatch for {plural_fn.__name__} vs {singular_fn.__name__}"
        assert (
            scopings[0].location == scoping_single.location
        ), f"Location mismatch for {plural_fn.__name__} vs {singular_fn.__name__}"


def test_none_label_space_same_as_default_scopings(elshape_body_sc):
    solid_none = elshape_body_sc.solid_scopings(label_space=None)
    solid_default = elshape_body_sc.solid_scopings()
    assert len(solid_none) == len(
        solid_default
    ), "None label_space should behave the same as default"


def test_empty_dict_label_space_same_as_default_scopings(elshape_body_sc):
    solid_empty = elshape_body_sc.solid_scopings(label_space={})
    solid_default = elshape_body_sc.solid_scopings()
    assert len(solid_empty) == len(
        solid_default
    ), "Empty dict label_space should behave the same as default"


def test_all_scoping_shapes_no_elshape_raises(server_type):
    sc = ScopingsContainer(server=server_type)
    sc.labels = ["body"]
    with pytest.raises(ValueError, match="No elshape label"):
        sc.solid_scopings()
    with pytest.raises(ValueError, match="No elshape label"):
        sc.shell_scopings()
    with pytest.raises(ValueError, match="No elshape label"):
        sc.beam_scopings()
    with pytest.raises(ValueError, match="No elshape label"):
        sc.solid_scoping()
    with pytest.raises(ValueError, match="No elshape label"):
        sc.shell_scoping()
    with pytest.raises(ValueError, match="No elshape label"):
        sc.beam_scoping()


def test_all_scoping_shapes_invalid_label_raises(elshape_body_sc):
    invalid_ls = {"nonexistent_label": 0}
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.solid_scopings(label_space=invalid_ls)
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.shell_scopings(label_space=invalid_ls)
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.beam_scopings(label_space=invalid_ls)
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.solid_scoping(label_space=invalid_ls)
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.shell_scoping(label_space=invalid_ls)
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.beam_scoping(label_space=invalid_ls)


def test_all_scoping_shapes_do_not_mutate_input(elshape_body_sc):
    for method in [
        elshape_body_sc.solid_scopings,
        elshape_body_sc.shell_scopings,
        elshape_body_sc.beam_scopings,
        elshape_body_sc.solid_scoping,
        elshape_body_sc.shell_scoping,
        elshape_body_sc.beam_scoping,
    ]:
        label_space = {"body": 0}
        original = label_space.copy()
        method(label_space=label_space)
        assert label_space == original, f"{method.__name__} mutated the input label_space"


def test_multiple_invalid_labels_raises_scopings(elshape_body_sc):
    with pytest.raises(ValueError, match="not in this scoping container"):
        elshape_body_sc.solid_scopings(label_space={"invalid1": 0, "invalid2": 1})
