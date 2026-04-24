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

import ansys.dpf.core as dpf


def test_label_space_(server_type):
    reference = {"test": 1, "various": 2}
    ls = dpf.LabelSpace(label_space=reference)
    assert dict(ls) == reference
    assert str(ls)
    reference = {"test": 1, "various": 2}
    ls.fill(label_space=reference)


def test_label_space_copy_construction(server_type):
    """Test that LabelSpace can be constructed from another LabelSpace."""
    reference = {"time": 1, "zone": 2}
    ls = dpf.LabelSpace(label_space=reference)
    ls_copy = dpf.LabelSpace(label_space=ls)
    assert dict(ls_copy) == reference


def test_label_space_str_ordering(server_type):
    """Test that __str__ returns keys in sorted (deterministic) order."""
    # Insert in non-alphabetical order
    ls = dpf.LabelSpace(label_space={"zone": 2, "node": 42, "time": 1})
    result = str(ls)
    # Keys should appear in sorted order: node < time < zone
    assert result == "{'node': 42, 'time': 1, 'zone': 2}"


def test_label_space_dict_ordering(server_type):
    """Test that __dict__() returns keys in sorted (deterministic) order."""
    ls = dpf.LabelSpace(label_space={"zone": 2, "node": 42, "time": 1})
    d = ls.__dict__()
    assert list(d.keys()) == sorted(d.keys())
