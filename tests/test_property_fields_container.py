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
from ansys.dpf.core.property_fields_container import _LabelSpaceKV, _MockPropertyFieldsContainer


def test_property_fields_container(allkindofcomplexity, server_type):
    model = dpf.Model(allkindofcomplexity, server=server_type)
    fields_container = _MockPropertyFieldsContainer(server=server_type)
    fields_container.add_label(label="test")
    assert fields_container.has_label(label="test")
    assert fields_container.labels == ["test"]
    with pytest.raises(ValueError, match="labels already set"):
        fields_container.labels = ["test"]
    field = model.metadata.meshed_region.elements.connectivities_field
    fields_container.add_field(label_space={"test": 42}, field=field)
    assert len(fields_container.label_spaces) == 1
    label_space = fields_container.label_spaces[0]
    assert fields_container.get_label_space(0) == {"test": 42}
    assert isinstance(label_space, _LabelSpaceKV)
    assert label_space.field == field
    assert label_space.dict == {"test": 42}
    label_space.field = model.metadata.meshed_region.elements.element_types_field
    ref = """DPF PropertyFieldsContainer with 1 fields
\t 0: Label Space: {'test': 42} with field
\t\t\t"""  # noqa
    assert ref in str(fields_container)
    with pytest.raises(KeyError, match="label test2 not found"):
        fields_container.get_label_scoping("test2")
    scoping = fields_container.get_label_scoping("test")
    assert isinstance(scoping, dpf.Scoping)
    assert scoping.ids == [1]
    assert scoping.location == ""

    property_field = fields_container.get_entries(0)[0]
    assert isinstance(property_field, dpf.property_field.PropertyField)
    assert fields_container.get_entries({"test": 42})[0] == property_field
    with pytest.raises(KeyError, match="is not in labels:"):
        fields_container.get_entries(({"test2": 0}))
    assert fields_container.get_entry({"test": 42}) == property_field
    with pytest.raises(ValueError, match="Could not find corresponding entry"):
        fields_container.get_entry(({"test": 0}))
    assert fields_container[{"test": 42}] == property_field
    assert len(fields_container) == 1

    assert fields_container.get_fields({"test": 42})[0] == property_field
    assert fields_container.get_field(0) == property_field
