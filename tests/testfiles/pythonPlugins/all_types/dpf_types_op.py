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

from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core import (
    field,
    scoping,
    fields_container,
    meshes_container,
    scopings_container,
    property_field,
    data_sources,
    types,
    workflow,
    data_tree,
    generic_data_container,
)


class ForwardFieldOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, field.Field)
        f = self.get_input(0, types.field)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_field"


class ForwardScopingOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, scoping.Scoping)
        f = self.get_input(0, types.scoping)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_scoping"


class ForwardFieldsContainerOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, fields_container.FieldsContainer)
        f = self.get_input(0, types.fields_container)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_fields_container"


class ForwardMeshesContainerOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, meshes_container.MeshesContainer)
        f = self.get_input(0, types.meshes_container)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_meshes_container"


class ForwardScopingsContainerOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, scopings_container.ScopingsContainer)
        f = self.get_input(0, types.scopings_container)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_scopings_container"


class ForwardPropertyFieldOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, property_field.PropertyField)
        f = self.get_input(0, types.property_field)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_property_field"


class ForwardStringFieldOperator(CustomOperatorBase):
    def run(self):
        from ansys.dpf.core import string_field

        f = self.get_input(0, string_field.StringField)
        f = self.get_input(0, types.string_field)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_string_field"


class ForwardCustomTypeFieldOperator(CustomOperatorBase):
    def run(self):
        from ansys.dpf.core import custom_type_field

        f = self.get_input(0, custom_type_field.CustomTypeField)
        f = self.get_input(0, types.custom_type_field)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_custom_type_field"


class ForwardDataSourcesOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, data_sources.DataSources)
        f = self.get_input(0, types.data_sources)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_data_sources"


class ForwardWorkflowOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, workflow.Workflow)
        f = self.get_input(0, types.workflow)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_workflow"


class ForwardDataTreeOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, data_tree.DataTree)
        assert not f is None
        f = self.get_input(0, types.data_tree)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_data_tree"


class ForwardGenericDataContainerOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, generic_data_container.GenericDataContainer)
        assert not f is None
        f = self.get_input(0, types.generic_data_container)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_generic_data_container"
