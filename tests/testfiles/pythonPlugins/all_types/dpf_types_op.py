from ansys.dpf.core import (
    data_sources,
    data_tree,
    field,
    fields_container,
    meshes_container,
    property_field,
    scoping,
    scopings_container,
    types,
    workflow,
)
from ansys.dpf.core.custom_operator import CustomOperatorBase


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
