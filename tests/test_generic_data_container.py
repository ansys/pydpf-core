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

import numpy as np
import pytest

from ansys.dpf import core as dpf
import conftest
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0,
    raises_for_servers_version_under,
)


@conftest.raises_for_servers_version_under("7.0")
def test_create_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)
    assert gdc._internal_obj is not None


@conftest.raises_for_servers_version_under("7.0")
def test_set_get_property_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)
    entity = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    gdc.set_property("viscosity", entity)
    new_entity = gdc.get_property("viscosity")
    assert entity.location == new_entity.location


@conftest.raises_for_servers_version_under("7.0")
def test_set_get_data_tree_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)
    entity = dpf.DataTree(server=server_type)
    entity.add(name="john")
    gdc.set_property("persons", entity)
    new_entity = gdc.get_property("persons")
    assert new_entity.get_as("name") == "john"


@conftest.raises_for_servers_version_under("7.0")
def test_get_property_description_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)
    entity = 42
    gdc.set_property("my-int", entity)
    new_entity = gdc.get_property("my-int")
    assert 42 == new_entity

    entity = 4.2
    gdc.set_property("my-float", entity)
    new_entity = gdc.get_property("my-float")
    assert 4.2 == new_entity

    entity = "hello world"
    gdc.set_property("my-string", entity)
    new_entity = gdc.get_property("my-string")
    assert "hello world" == new_entity

    entity = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    gdc.set_property("my-field", entity)

    property_description = gdc.get_property_description()

    assert 4 == len(property_description)
    assert property_description == {
        "my-float": "float",
        "my-int": "int",
        "my-string": "str",
        "my-field": "Field",
    }


@conftest.raises_for_servers_version_under("7.0")
def test_get_by_type_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)
    entity = 42
    gdc.set_property("my-int", entity)
    new_entity = gdc.get_property("my-int")
    assert 42 == new_entity
    new_entity = gdc.get_property("my-int", int)
    assert 42 == new_entity
    new_entity = gdc.get_property("my-int", dpf.types.int)
    assert 42 == new_entity

    entity = 4.2
    gdc.set_property("my-float", entity)
    new_entity = gdc.get_property("my-float")
    assert 4.2 == new_entity
    new_entity = gdc.get_property("my-float", float)
    assert 4.2 == new_entity
    new_entity = gdc.get_property("my-float", dpf.types.double)
    assert 4.2 == new_entity

    entity = "hello world"
    gdc.set_property("my-string", entity)
    new_entity = gdc.get_property("my-string")
    assert "hello world" == new_entity
    new_entity = gdc.get_property("my-string", str)
    assert "hello world" == new_entity
    new_entity = gdc.get_property("my-string", dpf.types.string)
    assert "hello world" == new_entity

    entity = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    gdc.set_property("my-field", entity)
    new_entity = gdc.get_property("my-field")
    assert isinstance(new_entity, dpf.Field)

    new_entity = gdc.get_property("my-field", dpf.Field)
    assert isinstance(new_entity, dpf.Field)

    new_entity = gdc.get_property("my-field", dpf.types.field)
    assert isinstance(new_entity, dpf.Field)


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0, reason="Available for servers >=8.0"
)
def test_get_bytes_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)

    entity = "hello world"
    gdc.set_property("my-string", entity)
    gdc.set_property("my-bytes", entity.encode())
    new_entity = gdc.get_property("my-string")
    assert "hello world" == new_entity
    new_entity = gdc.get_property("my-bytes")
    assert "hello world" == new_entity
    new_entity = gdc.get_property("my-string", str)
    assert "hello world" == new_entity
    new_entity = gdc.get_property("my-string", dpf.types.string)
    assert "hello world" == new_entity
    new_entity = gdc.get_property("my-string", bytes)
    assert b"hello world" == new_entity
    new_entity = gdc.get_property("my-string", dpf.types.bytes)
    assert b"hello world" == new_entity
    new_entity = gdc.get_property("my-bytes", dpf.types.bytes)
    assert b"hello world" == new_entity


@raises_for_servers_version_under("8.1")
def test_set_collection_generic_data_container(server_type):
    coll = dpf.GenericDataContainersCollection(server=server_type)
    gdc = dpf.GenericDataContainer(server=server_type)
    coll.labels = ["body", "time"]
    gdc.set_property("coll", coll)
    assert gdc.get_property("coll", dpf.GenericDataContainersCollection).labels == ["body", "time"]


@raises_for_servers_version_under("9.0")
def test_set_int_vec_generic_data_container(server_type):
    gdc = dpf.GenericDataContainer(server=server_type)
    gdc.set_property("vec", [1, 2, 3])
    gdc.set_property("nparray", np.array([1, 2, 3], dtype=np.int32))
    assert np.allclose(gdc.get_property("vec"), [1, 2, 3])
    assert np.allclose(gdc.get_property("nparray"), [1, 2, 3])
