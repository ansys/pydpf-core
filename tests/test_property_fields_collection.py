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

import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core.property_fields_collection import PropertyFieldsCollection


def test_property_fields_collection(allkindofcomplexity, server_type):
    """Test PropertyFieldsCollection class."""
    model = dpf.Model(allkindofcomplexity, server=server_type)

    # Create a PropertyFieldsCollection
    pfc = PropertyFieldsCollection(server=server_type)

    # Test adding labels
    pfc.add_label(label="test")
    assert pfc.has_label(label="test")
    assert pfc.labels == ["test"]

    # Test adding another label
    pfc.add_label(label="body")
    assert pfc.has_label(label="body")
    assert pfc.labels == ["body", "test"]

    # Get a property field from the model
    property_field = model.metadata.meshed_region.elements.connectivities_field

    # Test add_entry method
    pfc.add_entry(label_space={"test": 42, "body": 0}, entry=property_field)
    assert len(pfc) == 1

    # Test get_label_space
    label_space = pfc.get_label_space(0)
    assert label_space == {"test": 42, "body": 0}

    scoping = pfc.get_label_scoping("test")
    assert isinstance(scoping, dpf.Scoping)
    assert 42 in scoping.ids

    # Test get_entries with label space
    entries = pfc.get_entries({"test": 42, "body": 0})
    assert len(entries) >= 1
    retrieved_field = entries[0]
    assert isinstance(retrieved_field, dpf.PropertyField)

    # Test get_entry with label space
    entry = pfc.get_entry({"test": 42, "body": 0})
    assert isinstance(entry, dpf.PropertyField)

    # Test get_entry with index
    entry_by_index = pfc.get_entry(0)
    assert isinstance(entry_by_index, dpf.PropertyField)

    # Test __getitem__ with index
    field_by_index = pfc[0]
    assert isinstance(field_by_index, dpf.PropertyField)

    # Test __getitem__ with label space
    field_by_label = pfc.get_entry({"test": 42, "body": 0})
    assert isinstance(field_by_label, dpf.PropertyField)

    # Test adding more entries with different label spaces
    property_field2 = model.metadata.meshed_region.elements.element_types_field
    pfc.add_entry(label_space={"test": 43, "body": 0}, entry=property_field2)
    assert len(pfc) == 2

    # Test retrieving multiple entries with partial label space
    entries_body0 = pfc.get_entries({"body": 0})
    assert len(entries_body0) == 2

    # Test get_available_ids_for_label
    test_ids = pfc.get_available_ids_for_label("test")
    assert 42 in test_ids
    assert 43 in test_ids


def test_property_fields_collection_from_scratch(server_type):
    """Test creating PropertyFieldsCollection from scratch without a model."""
    # Create a PropertyFieldsCollection
    pfc = PropertyFieldsCollection(server=server_type)

    # Set labels
    pfc.labels = ["time", "body"]
    assert pfc.labels == ["body", "time"]

    # Create property fields and add them
    for i in range(3):
        label_space = {"time": i + 1, "body": 0}
        pfield = dpf.PropertyField(server=server_type)
        pfield.data = list(range(i * 10, (i + 1) * 10))
        pfc.add_entry(label_space, pfield)

    # Verify collection size
    assert len(pfc) == 3

    # Test get_entries with full label space
    entries = pfc.get_entries({"time": 1, "body": 0})
    assert len(entries) >= 1
    assert isinstance(entries[0], dpf.PropertyField)

    # Test get_entries with partial label space
    all_time_fields = pfc.get_entries({"body": 0})
    assert len(all_time_fields) == 3

    # Test get_entry by index
    first_field = pfc.get_entry(0)
    assert isinstance(first_field, dpf.PropertyField)

    # Test get_entry by label space
    time2_field = pfc.get_entry({"time": 2, "body": 0})
    assert isinstance(time2_field, dpf.PropertyField)

    # Test __getitem__
    field_idx = pfc[1]
    assert isinstance(field_idx, dpf.PropertyField)

    field_label = pfc.get_entry({"time": 3, "body": 0})
    assert isinstance(field_label, dpf.PropertyField)

    # Test get_label_space
    ls0 = pfc.get_label_space(0)
    assert ls0["time"] == 1
    assert ls0["body"] == 0

    ls2 = pfc.get_label_space(2)
    assert ls2["time"] == 3
    assert ls2["body"] == 0

    # Test get_label_scoping
    time_scoping = pfc.get_label_scoping("time")
    assert isinstance(time_scoping, dpf.Scoping)
    assert 1 in time_scoping.ids
    assert 2 in time_scoping.ids
    assert 3 in time_scoping.ids

    # Test get_available_ids_for_label
    time_ids = pfc.get_available_ids_for_label("time")
    assert 1 in time_ids
    assert 2 in time_ids
    assert 3 in time_ids

    body_ids = pfc.get_available_ids_for_label("body")
    assert 0 in body_ids

    # Test has_label
    assert pfc.has_label("time")
    assert pfc.has_label("body")
    assert not pfc.has_label("complex")

    # Test add_label
    pfc.add_label("complex", default_value=0)
    assert pfc.has_label("complex")
    assert "complex" in pfc.labels
