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

import conftest
from ansys.dpf import core as dpf


@conftest.raises_for_servers_version_under("5.0")
def test_set_get_generic_support(server_type):
    support = dpf.GenericSupport("phase", server=server_type)
    field = dpf.Field(location="phase", nature=dpf.natures.scalar, server=server_type)
    support.set_support_of_property("viscosity", field)
    field = dpf.StringField(server=server_type)
    support.set_support_of_property("names", field)
    field = dpf.PropertyField(location="phase", nature=dpf.natures.scalar, server=server_type)
    support.set_support_of_property("type", field)
    field = dpf.PropertyField(location="phase", nature=dpf.natures.scalar, server=server_type)
    support.set_support_of_property("miscibility", field)
    assert support.available_field_supported_properties() == ["viscosity"]
    assert support.available_string_field_supported_properties() == ["names"]
    assert "type" in support.available_prop_field_supported_properties()
    assert "miscibility" in support.available_prop_field_supported_properties()
    field = support.field_support_by_property("viscosity")
    assert isinstance(field, dpf.Field)
    field = support.field_support_by_property("dummy")
    assert field is None
    field = support.string_field_support_by_property("names")
    assert isinstance(field, dpf.StringField)
    field = support.string_field_support_by_property("dummy")
    assert field is None
    field = support.prop_field_support_by_property("type")
    assert isinstance(field, dpf.PropertyField)
    field = support.prop_field_support_by_property("dummy")
    assert field is None
    field = support.prop_field_support_by_property("miscibility")
    assert isinstance(field, dpf.PropertyField)
