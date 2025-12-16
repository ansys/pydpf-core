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

from __future__ import annotations

from typing import Any, override

import pytest

import ansys.dpf.core as dpf
from ansys.dpf.core import server as server_module
from ansys.dpf.core.operator_specification import Exposures, Specification
from ansys.dpf.core.server_types import BaseServer
from ansys.dpf.gate.generated import operator_specification_abstract_api
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_10_0


@pytest.mark.skipif(
    condition=not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_10_0,
    reason="Aliases available with DPF 10.0 (25R2).",
)
def test_pin_alias(server_type):
    field = dpf.fields_factory.create_scalar_field(
        num_entities=1, location=dpf.locations.nodal, server=server_type
    )
    field.append(data=[1.0], scopingid=1)
    weights = dpf.fields_factory.create_scalar_field(
        num_entities=1, location=dpf.locations.nodal, server=server_type
    )
    weights.append(data=[2.0], scopingid=1)
    ponderation = dpf.fields_factory.create_scalar_field(
        num_entities=1, location=dpf.locations.nodal, server=server_type
    )
    ponderation.append(data=[3.0], scopingid=1)

    # Check new pin name
    output: dpf.Field = dpf.operators.math.scale(
        field=field,
        weights=weights,
        server=server_type,
    ).eval()
    assert output.data_as_list == [2.0]

    # Check alias (check warning)
    with pytest.warns(
        expected_warning=DeprecationWarning,
        match='Operator scale: Input name "ponderation" is deprecated in favor of "weights".',
    ):
        output: dpf.Field = dpf.operators.math.scale(
            field=field,
            ponderation=ponderation,
            server=server_type,
        ).eval()
    assert output.data_as_list == [3.0]

    # Check precedence of new pin name over alias
    output: dpf.Field = dpf.operators.math.scale(
        field=field,
        weights=weights,
        ponderation=ponderation,
        server=server_type,
    ).eval()
    assert output.data_as_list == [2.0]

    # Check connection via inputs of new name
    op = dpf.operators.math.scale(
        field=field,
        server=server_type,
    )
    op.inputs.weights.connect(weights)
    output: dpf.Field = op.eval()
    assert output.data_as_list == [2.0]

    # Check connection via inputs of alias (check warning)
    op = dpf.operators.math.scale(
        field=field,
        server=server_type,
    )
    with pytest.warns(
        expected_warning=DeprecationWarning,
        match='Operator scale: Input name "ponderation" is deprecated in favor of "weights".',
    ):
        op.inputs.ponderation.connect(ponderation)
    output: dpf.Field = op.eval()
    assert output.data_as_list == [3.0]

    # Check effect of consecutive connections
    op = dpf.operators.math.scale(
        field=field,
        server=server_type,
    )
    op.inputs.weights.connect(weights)
    output: dpf.Field = op.eval()
    assert output.data_as_list == [2.0]
    op.inputs.ponderation.connect(ponderation)
    output: dpf.Field = op.eval()
    assert output.data_as_list == [3.0]
    op.inputs.weights.connect(weights)
    output: dpf.Field = op.eval()
    assert output.data_as_list == [2.0]


class MockSpecificationAPI(operator_specification_abstract_api.OperatorSpecificationAbstractAPI):
    @staticmethod
    def DefaultProperties() -> dict[str, Any]:
        return {
            "scripting_name": "operator_scripting_name",
            "internal_name": "operator_internal_name",
            "exposure": Exposures.public,
            "license": "any_dpf_increment",
            "plugin": "unknown",
            "category": "test_category",
            "display_name": "Operator display name",
        }

    @staticmethod
    def Default() -> MockSpecificationAPI:
        return MockSpecificationAPI(properties=MockSpecificationAPI.DefaultProperties())

    @staticmethod
    def New(*, properties: dict[str, Any], add_defaults: bool = False) -> MockSpecificationAPI:
        props = (
            MockSpecificationAPI.DefaultProperties() | properties if add_defaults else properties
        )
        return MockSpecificationAPI(properties=props)

    __properties: dict[str, Any] = dict()

    @override
    def __init__(self, *, properties: dict[str, Any]):
        self.__properties = properties

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def set_property(self, value: dict[str, Any]):
        self.__properties = value

    def operator_specification_get_num_properties(self, *args):
        return len(self.__properties)

    def operator_specification_get_property_key(self, any, index: int, *args):
        props = list(self.__properties.keys())
        return props[index]

    def operator_specification_get_properties(self, any, key, *args):
        return self.__properties[key]


class MockSpecification(Specification):
    def __init__(
        self,
        operator_name: str | None = None,
        specification: Specification | None = None,
        server: server_module.BaseServer | None = None,
        *,
        api: operator_specification_abstract_api.OperatorSpecificationAbstractAPI | None = None,
        internal_obj: Any = None,
    ):
        self._api = api or MockSpecificationAPI.Default()
        self.operator_name = operator_name
        self._internal_obj = internal_obj

        # Properties initialization
        self._properties = None


class TestOperatorSpecification:
    def test_properties(self):
        spec = MockSpecification(
            api=MockSpecificationAPI.New(properties={"scripting_name": None}, add_defaults=True),
            internal_obj=not None,
        )

        props = spec.properties
        scripting_name = props.get("scripting_name")

        assert scripting_name is not None
        assert scripting_name == props.get("internal_name")
