# -*- coding: utf-8 -*-
import weakref

import pytest
from ansys.dpf.core import Scoping, ScopingsContainer


@pytest.fixture()
def elshape_body_sc():
    """Returns a scopings continer with 20 scoping split on body and elshape"""
    sc = ScopingsContainer()
    sc.labels = ["elshape", "body"]
    for i in range(0, 20):
        mscop = {"elshape": i + 1, "body": 0}
        scop = Scoping()
        scop.ids = range(0, i + 1)
        sc.add_scoping(mscop, scop)
    return sc


def test_create_scopings_container():
    sc = ScopingsContainer()
    assert sc._message.id != 0


def test_empty_index():
    sc = ScopingsContainer()
    with pytest.raises(IndexError):
        sc[0]


def test_createby_message_copy_scopings_container():
    sc = ScopingsContainer()
    scopings_container2 = ScopingsContainer(scopings_container=sc._message)
    assert sc._message.id == scopings_container2._message.id


def test_createbycopy_scopings_container():
    sc = ScopingsContainer()
    scopings_container2 = ScopingsContainer(scopings_container=sc)
    assert sc._message.id == scopings_container2._message.id


def test_set_get_scoping_scopings_container(elshape_body_sc):
    sc = elshape_body_sc
    assert sc.get_available_ids_for_label("elshape") == list(range(1, 21))
    for i in range(0, 20):
        scopingid = sc.get_scoping({"elshape": i + 1, "body": 0})._message.id
        assert scopingid != 0
        assert sc.get_scoping(i)._message.id != 0
        assert sc.get_scoping({"elshape": i + 1, "body": 0})._message.id != 0
        assert sc.get_scoping({"elshape": i + 1, "body": 0}).ids == list(
            range(0, i + 1)
        )
        assert sc[i]._message.id != 0


def test_set_get_scoping_scopings_container_new_label(elshape_body_sc):
    sc = elshape_body_sc
    assert sc.get_available_ids_for_label("elshape") == list(range(1, 21))
    for i in range(0, 20):
        scopingid = sc.get_scoping({"elshape": i + 1, "body": 0})._message.id
        assert scopingid != 0
        assert sc.get_scoping(i)._message.id != 0
        assert sc.get_scoping({"elshape": i + 1, "body": 0})._message.id != 0
        assert sc[i]._message.id != 0
        assert sc.get_label_space(i) == {"elshape": i + 1, "body": 0}
        assert sc.get_scoping({"elshape": i + 1, "body": 0}).ids == list(
            range(0, i + 1)
        )
    sc.add_label("time")
    for i in range(0, 20):
        mscop = {"elshape": i + 1, "body": 0, "time": 1}
        scop = Scoping()
        scop.ids = range(0, i + 10)
        sc.add_scoping(mscop, scop)
    assert len(sc.get_scopings({"elshape": i + 1, "body": 0})) == 2
    for i in range(0, 20):
        scopingid = sc.get_scoping({"elshape": i + 1, "body": 0, "time": 1})._message.id
        assert scopingid != 0
        assert sc.get_scoping(i + 20)._message.id != 0
        assert sc[i]._message.id != 0
        assert sc.get_label_space(i + 20) == {"elshape": i + 1, "body": 0, "time": 1}
        assert sc.get_scoping({"elshape": i + 1, "body": 0, "time": 1}).ids == list(
            range(0, i + 10)
        )
        assert sc.get_scoping({"elshape": i + 1, "time": 1}).ids == list(
            range(0, i + 10)
        )


def test_get_item_scoping_scopings_container(elshape_body_sc):
    sc = elshape_body_sc
    for i in range(0, 20):
        assert sc[i]._message.id != 0
        assert sc[i].ids == list(range(0, i + 1))


def test_delete_scopings_container():
    sc = ScopingsContainer()
    ref = weakref.ref(sc)
    del sc
    assert ref() is None


def test_str_scopings_container(elshape_body_sc):
    sc = elshape_body_sc
    assert "body" in str(sc)
