# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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

from dataclasses import dataclass, field
import random

import numpy as np
import pytest

from ansys.dpf.core import (
    CustomTypeField,
    CustomTypeFieldsCollection,
    GenericDataContainer,
    GenericDataContainersCollection,
    StringField,
    StringFieldsCollection,
    Workflow,
    fields_factory,
    operators,
)
from ansys.dpf.core.collection import Collection
from ansys.dpf.core.generic_support import GenericSupport
from ansys.dpf.core.time_freq_support import TimeFreqSupport
import conftest


@conftest.raises_for_servers_version_under("8.1")
def test_create_collection(server_type):
    mc = Collection(server=server_type, entries_type=CustomTypeField)
    assert mc._internal_obj is not None


@conftest.raises_for_servers_version_under("8.1")
def test_empty_index():
    mc = Collection(entries_type=CustomTypeField)
    with pytest.raises(IndexError):
        mc[0]


def create_dummy_custom_type_field(server_type, np_type=np.uint64, size=4):
    pfield = CustomTypeField(np_type, server=server_type)
    pfield.scoping.ids = random.sample(range(10, 30), size)
    list_data = np.array(random.sample(range(10, 30), size), dtype=np_type)
    pfield.data = list_data
    return pfield


def create_dummy_string_field(server_type, size=4):
    pfield = StringField(server=server_type)
    pfield.scoping.ids = random.sample(range(10, 30), size)
    list_data = ["hello" for _ in range(size)]
    pfield.data = list_data
    return pfield


def create_dummy_gdc(server_type, prop="hi"):
    pfield = GenericDataContainer(server=server_type)
    pfield.set_property("prop", prop)
    return pfield


@dataclass
class CollectionTypeHelper:
    type: type
    instance_creator: object
    kwargs: dict = field(default_factory=dict)

    @property
    def name(self):
        return type.__name__


collection_helper = CollectionTypeHelper(
    Collection, create_dummy_custom_type_field, {"entries_type": CustomTypeField}
)
cust_type_field_collection_helper = CollectionTypeHelper(
    CustomTypeFieldsCollection, create_dummy_custom_type_field
)
string_field_collection_helper = CollectionTypeHelper(
    StringFieldsCollection, create_dummy_string_field
)
gdc_collection_helper = CollectionTypeHelper(GenericDataContainersCollection, create_dummy_gdc)


@pytest.mark.parametrize(
    "subtype_creator",
    [collection_helper, cust_type_field_collection_helper, string_field_collection_helper],
    ids=[
        collection_helper.name,
        cust_type_field_collection_helper.name,
        string_field_collection_helper.name,
    ],
)
@conftest.raises_for_servers_version_under("8.1")
def test_fill_collection(server_type, subtype_creator):
    coll = subtype_creator.type(server=server_type, **subtype_creator.kwargs)
    coll.labels = ["body", "time"]
    for i in range(1, 5):
        coll.add_entry(
            {"body": 1, "time": i},
            subtype_creator.instance_creator(server_type=server_type, size=i),
        )
    for i in range(1, 5):
        assert coll.get_entry({"body": 1, "time": i}).shape == i
    assert len(coll.get_entries({"body": 1})) == 4
    assert coll.get_entries({"body": 1})[0].shape == 1
    for i in range(1, 5):
        assert coll[i - 1].shape == i
    for i in range(1, 5):
        assert coll.get_label_space(i - 1) == {"body": 1, "time": i}
    assert (lab in coll.labels for lab in ("body", "time"))
    # assert "collection" in str(coll)


@conftest.raises_for_servers_version_under("8.1")
def test_fill_gdc_collection(server_type):
    coll = GenericDataContainersCollection(server=server_type)
    coll.labels = ["body", "time"]
    for i in range(1, 5):
        coll.add_entry({"body": 1, "time": i}, create_dummy_gdc(server_type=server_type, prop=i))
    for i in range(1, 5):
        assert coll.get_entry({"body": 1, "time": i}).get_property("prop") == i
    assert len(coll.get_entries({"body": 1})) == 4
    assert coll.get_entries({"body": 1})[0].get_property("prop") == 1
    for i in range(1, 5):
        assert coll[i - 1].get_property("prop") == i
    for i in range(1, 5):
        assert coll.get_label_space(i - 1) == {"body": 1, "time": i}
    assert (lab in coll.labels for lab in ("body", "time"))
    # assert "collection" in str(coll)


@pytest.mark.parametrize(
    "subtype_creator",
    [collection_helper, cust_type_field_collection_helper, string_field_collection_helper],
    ids=[
        collection_helper.name,
        cust_type_field_collection_helper.name,
        string_field_collection_helper.name,
    ],
)
@conftest.raises_for_servers_version_under("8.1")
def test_set_support_collection(server_type, subtype_creator):
    coll = subtype_creator.type(server=server_type, **subtype_creator.kwargs)
    coll.labels = ["body", "time"]
    tfq = TimeFreqSupport(server=server_type)
    frequencies = fields_factory.create_scalar_field(3, server=server_type)
    frequencies.append([1.0], 1)
    tfq.time_frequencies = frequencies

    gen_support = GenericSupport(name="body", server=server_type)
    str_f = StringField(server=server_type)
    str_f.append(["inlet"], 1)
    gen_support.set_support_of_property("name", str_f)

    coll.set_support("time", tfq)
    coll.set_support("body", gen_support)

    assert coll.get_support("time").available_field_supported_properties() == ["time_freqs"]
    assert coll.get_support("body").available_string_field_supported_properties() == ["name"]
    assert coll.get_support("body").string_field_support_by_property("name").data == ["inlet"]


@pytest.mark.parametrize(
    "subtype_creator",
    [
        collection_helper,
        cust_type_field_collection_helper,
        string_field_collection_helper,
        gdc_collection_helper,
    ],
    ids=[
        collection_helper.name,
        cust_type_field_collection_helper.name,
        string_field_collection_helper.name,
        gdc_collection_helper.name,
    ],
)
@conftest.raises_for_servers_version_under("8.1")
def test_connect_collection_operator(server_type, subtype_creator):
    coll = subtype_creator.type(server=server_type, **subtype_creator.kwargs)
    coll.labels = ["body"]
    coll.add_entry({"body": 1}, subtype_creator.instance_creator(server_type=server_type))
    op = operators.utility.forward(server=server_type)
    op.connect(0, coll)
    out = op.get_output(0, subtype_creator.type)
    assert out is not None
    assert len(out) == 1
    op.inputs.connect(coll)
    out = op.get_output(0, subtype_creator.type)
    assert out is not None
    assert len(out) == 1


@pytest.mark.parametrize(
    "subtype_creator",
    [
        collection_helper,
        cust_type_field_collection_helper,
        string_field_collection_helper,
        gdc_collection_helper,
    ],
    ids=[
        collection_helper.name,
        cust_type_field_collection_helper.name,
        string_field_collection_helper.name,
        gdc_collection_helper.name,
    ],
)
@conftest.raises_for_servers_version_under("8.1")
def test_connect_collection_workflow(server_type, subtype_creator):
    coll = subtype_creator.type(server=server_type, **subtype_creator.kwargs)
    coll.labels = ["body"]
    coll.add_entry({"body": 1}, subtype_creator.instance_creator(server_type=server_type))
    wf = Workflow(server=server_type)
    op = operators.utility.forward(server=server_type)
    wf.set_input_name("in", 0, op)
    wf.set_output_name("out", op, 0)
    wf.connect("in", coll)
    out = wf.get_output("out", subtype_creator.type)
    assert out is not None
    assert len(out) == 1
    op.inputs.connect(coll)
    out = op.get_output(0, subtype_creator.type)
    assert out is not None
    assert len(out) == 1
