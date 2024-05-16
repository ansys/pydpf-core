import numpy as np
from ansys.dpf import core as dpf
from ansys.dpf.core.custom_operator import CustomOperatorBase, record_operator
from ansys.dpf.core.operator_specification import CustomSpecification, SpecificationProperties, \
    PinSpecification


class EasyStatistics(CustomOperatorBase):
    @property
    def name(self):
        return "easy_statistics"

    @property
    def specification(self) -> CustomSpecification:
        spec = CustomSpecification()
        spec.description = "Compute the first quartile, the median, the third quartile and" \
                           " the variance of a scalar Field with numpy"
        spec.inputs = {
            0: PinSpecification("field", [dpf.Field, dpf.FieldsContainer],
                                "scalar Field on which the statistics quantities is computed."),
        }
        spec.outputs = {
            0: PinSpecification("first_quartile", [float]),
            1: PinSpecification("median", [float]),
            2: PinSpecification("third_quartile", [float]),
            3: PinSpecification("variance", [float]),
        }
        spec.properties = SpecificationProperties("easy statistics", "math")
        return spec

    def run(self):
        field = self.get_input(0, dpf.Field)
        if field is None:
            field = self.get_input(0, dpf.FieldsContainer)[0]
        # compute stats
        first_quartile_val = np.quantile(field.data, 0.25)
        median_val = np.quantile(field.data, 0.5)
        third_quartile_val = np.quantile(field.data, 0.75)
        variance_val = np.var(field.data)
        self.set_output(0, first_quartile_val)
        self.set_output(1, median_val)
        self.set_output(2, third_quartile_val)
        self.set_output(3, float(variance_val))
        self.set_succeeded()


def load_operators(*args):
    record_operator(EasyStatistics, *args)
