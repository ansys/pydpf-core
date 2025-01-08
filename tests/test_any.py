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

import conftest
from ansys.dpf import core as dpf


@conftest.raises_for_servers_version_under("7.0")
def test_create_any(server_type):
    field = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    any_dpf = dpf.Any.new_from(field)

    assert any_dpf._internal_obj is not None


@conftest.raises_for_servers_version_under("7.0")
def test_cast_int_any(server_type):
    entity = 42
    any_dpf = dpf.Any.new_from(entity, server_type)
    new_entity = any_dpf.cast()
    assert 42 == new_entity


@conftest.raises_for_servers_version_under("7.0")
def test_cast_string_any(server_type):
    entity = "hello world"
    any_dpf = dpf.Any.new_from(entity, server_type)
    new_entity = any_dpf.cast()
    assert "hello world" == new_entity


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0,
    reason="for_each not implemented below 8.0",
)
def test_cast_bytes_any(server_type):
    entity = b"hello world"
    any_dpf = dpf.Any.new_from(entity, server_type)
    new_entity = any_dpf.cast()
    assert b"hello world" == new_entity


@conftest.raises_for_servers_version_under("7.0")
def test_cast_float_any(server_type):
    entity = 4.2
    any_dpf = dpf.Any.new_from(entity, server_type)
    new_entity = any_dpf.cast()
    assert 4.2 == new_entity


@conftest.raises_for_servers_version_under("7.0")
def test_cast_field_any(server_type):
    entity = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()
    assert entity.location == new_entity.location


@conftest.raises_for_servers_version_under("7.0")
def test_cast_property_field_any(server_type):
    entity = dpf.PropertyField(nature=dpf.natures.scalar, server=server_type)
    entity.data = [20, 30, 50, 70, 80]
    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()
    assert entity.data.all() == new_entity.data.all()


@conftest.raises_for_servers_version_under("7.0")
def test_cast_string_field_any(server_type):
    list_ids = [1, 2]
    scop = dpf.Scoping(ids=list_ids, server=server_type)
    entity = dpf.StringField(server=server_type)
    entity.scoping = scop
    entity.data = ["hello", "world"]
    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()

    assert entity.data == new_entity.data


@conftest.raises_for_servers_version_under("7.0")
def test_cast_generic_data_container_any(server_type):
    entity = dpf.GenericDataContainer(server=server_type)
    field = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    entity.set_property("field", field)

    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()

    new_field = new_entity.get_property("field")

    assert field.location == new_field.location


@conftest.raises_for_servers_version_under("7.0")
def test_cast_scoping_any(server_type):
    entity = dpf.Scoping(server=server_type, location="phase")
    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()

    assert entity.location == new_entity.location


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_9_1,
    reason="for_each not implemented below 8.0. Failing for gRPC CLayer below 9.1 for any.whl",
)
def test_cast_workflow_any(server_type):
    entity = dpf.Workflow(server=server_type)
    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()

    assert new_entity.input_names == []


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_10_0,
    reason="any does not support operator below 10.0",
)
def test_cast_operator_any(server_type):
    entity = dpf.Operator(server=server_type, name="U")
    any_dpf = dpf.Any.new_from(entity)
    new_entity = any_dpf.cast()

    assert entity.name == new_entity.name
