from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core import field, scoping, fields_container, meshes_container, scopings_container, property_field, data_sources


class ForwardFieldOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, field.Field)
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
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_property_field"


class ForwardDataSourcesOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, data_sources.DataSources)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_data_sources"
