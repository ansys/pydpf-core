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

from ansys.dpf import core as dpf
from ansys.dpf.core import fields_factory


def test_perf_vec_setters(server_type):
    num_entities = int(1e5)
    field = fields_factory.create_scalar_field(
        num_entities=num_entities, location=dpf.locations.elemental, server=server_type
    )
    field.name = "my_field"
    field.data = np.zeros(num_entities, dtype=np.int32)
    field.scoping.ids = np.zeros(num_entities, dtype=np.int32)

    all_indices = np.arange(num_entities)
    chunks = np.array_split(all_indices, 200)

    for index, chunk in enumerate(chunks):
        field.data[chunk] = int(index)
        field.scoping.ids[chunk] = chunk


def test_perf_vec_getters(server_type):
    num_entities = int(1e5)
    field = fields_factory.create_scalar_field(
        num_entities=num_entities, location=dpf.locations.elemental, server=server_type
    )
    field.name = "my_field"
    field.data = np.zeros(num_entities, dtype=np.int32)
    field.scoping.ids = np.zeros(num_entities, dtype=np.int32)

    all_indices = np.arange(num_entities)
    chunks = np.array_split(all_indices, 200)

    for index, chunk in enumerate(chunks):
        d = field.data[chunk]
        d = field.scoping.ids[chunk]


def test_update_empty_dpf_vector_prop_field(server_type):
    prop_field = dpf.PropertyField(server=server_type)
    prop_field.data = np.zeros((100))
    prop_field.scoping.ids = list(range(1, 100))
    assert np.allclose(prop_field.get_entity_data(1), [0])
    dp = prop_field._data_pointer
    dp = None
    assert np.allclose(prop_field.get_entity_data(1), [0])


def test_update_empty_dpf_vector_field(server_type):
    field = dpf.Field(server=server_type)
    field.data = np.zeros((100), dtype=np.double)
    field.scoping.ids = list(range(1, 100))
    assert np.allclose(field.get_entity_data(1), [0])
    dp = field._data_pointer
    dp = None
    assert np.allclose(field.get_entity_data(1), [0])


def test_update_empty_dpf_vector_string_field(server_type):
    string_field = dpf.StringField(server=server_type)
    string_field.data = ["high", "goodbye", "hello"]
    string_field.scoping.ids = list(range(1, 3))
    assert string_field.get_entity_data(1) == ["goodbye"]
    dp = string_field._data_pointer
    dp = None
    assert string_field.get_entity_data(1) == ["goodbye"]


def test_update_empty_dpf_vector_custom_type_field(server_type):
    field = dpf.CustomTypeField(unitary_type=np.double, server=server_type)
    field.data = np.zeros((100), dtype=np.double)
    field.scoping.ids = list(range(1, 100))
    assert np.allclose(field.get_entity_data(1), [0])
    dp = field._data_pointer
    dp = None
    assert np.allclose(field.get_entity_data(1), [0])
