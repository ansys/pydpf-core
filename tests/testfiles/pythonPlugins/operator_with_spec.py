from ansys.dpf.core import Field
from ansys.dpf.core.custom_operator import CustomOperatorBase, record_operator
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    PinSpecification,
    SpecificationProperties,
)


class AddFloatToFieldData(CustomOperatorBase):
    def run(self):
        field = self.get_input(0, Field)
        to_add = self.get_input(1, float)
        data = field.data
        data += to_add
        self.set_output(0, field)
        self.set_succeeded()

    @property
    def specification(self):
        spec = CustomSpecification()
        spec.description = "Add a custom value to all the data of an input Field"
        spec.inputs = {
            0: PinSpecification("field", [Field], "Field on which float value is added."),
            1: PinSpecification("to_add", [float], "Data to add."),
        }
        spec.outputs = {
            0: PinSpecification("field", [Field], "Field on which the float value is added.")
        }
        spec.properties = SpecificationProperties("custom add to field", "math")
        return spec

    @property
    def name(self):
        return "custom_add_to_field"


def load_operators(*args):
    record_operator(AddFloatToFieldData, *args)
