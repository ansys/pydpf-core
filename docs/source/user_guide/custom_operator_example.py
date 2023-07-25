from ansys.dpf import core as dpf
from ansys.dpf.core.custom_operator import CustomOperatorBase, record_operator  # noqa: F401
from ansys.dpf.core.operator_specification import CustomSpecification, SpecificationProperties, \
    PinSpecification


class CustomOperator(CustomOperatorBase):
    @property
    def name(self):
        return "name_of_my_custom_operator"

    @property
    def specification(self) -> CustomSpecification:
        spec = CustomSpecification()
        spec.description = "What the Operator does."
        spec.inputs = {
            0: PinSpecification("name_of_pin_0", [dpf.Field, dpf.FieldsContainer],
                                "Describe pin 0."),
        }
        spec.outputs = {
            0: PinSpecification("name_of_pin_0", [dpf.Field], "Describe pin 0."),
        }
        spec.properties = SpecificationProperties(
            user_name="user name",
            category="category",
            license="license",
        )
        return spec

    def run(self):
        field = self.get_input(0, dpf.Field)
        if field is None:
            field = self.get_input(0, dpf.FieldsContainer)[0]
        # compute data
        self.set_output(0, dpf.Field())
        self.set_succeeded()
