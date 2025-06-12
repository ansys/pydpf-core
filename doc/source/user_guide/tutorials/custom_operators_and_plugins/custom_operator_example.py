from ansys.dpf import core as dpf
from ansys.dpf.core.changelog import Changelog
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
        spec.description = "What the Operator does. You can use MarkDown and LaTeX in descriptions."
        spec.inputs = {
            0: PinSpecification(name="name_of_pin_0", type_names=[dpf.Field, dpf.FieldsContainer],
                                document="Describe input pin 0."),
        }
        spec.outputs = {
            0: PinSpecification(name="name_of_pin_0", type_names=[dpf.Field], document="Describe output pin 0."),
        }
        spec.properties = SpecificationProperties(
            user_name="user name",
            category="category",
            license="license",
        )
        # Set the changelog of the operator to track changes
        spec.set_changelog(Changelog()
                           .expect_version("0.0.0")
                           .patch_bump("Describe a patch bump.")
                           .major_bump("Describe a major bump.")
                           .minor_bump("Describe a minor bump.")
                           .expect_version("1.1.0")
        )
        return spec

    def run(self):
        field = self.get_input(0, dpf.Field)
        if field is None:
            field = self.get_input(0, dpf.FieldsContainer)[0]
        # compute data
        self.set_output(0, dpf.Field())
        self.set_succeeded()
