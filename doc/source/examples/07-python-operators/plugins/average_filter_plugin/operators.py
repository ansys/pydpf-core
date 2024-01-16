from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.operator_specification import CustomSpecification, PinSpecification,\
    SpecificationProperties
from ansys.dpf import core as dpf
from average_filter_plugin import common


class IdsWithDataHigherThanAverage(CustomOperatorBase):
    def run(self):
        field = self.get_input(0, dpf.Field)
        average = common.compute_average_of_field(field)
        ids_in = field.scoping.ids
        data_in = field.data
        out = []
        for i, d in enumerate(data_in):
            if d >= average:
                out.append(ids_in[i])
        scoping_out = dpf.Scoping(ids=out, location=field.scoping.location)
        self.set_output(0, scoping_out)
        self.set_succeeded()

    @property
    def specification(self):
        spec = CustomSpecification("Creates a scoping with all the ids having data higher or equal "
                                   "to the average value of the scalar field's data in input.")
        spec.inputs = {
            0: PinSpecification("field", type_names=dpf.Field, document="scalar Field."),
        }
        spec.outputs = {
            0: PinSpecification("scoping", type_names=dpf.Scoping),
        }
        spec.properties = SpecificationProperties(
            user_name="ids with data higher than average",
            category="logic"
        )
        return spec

    @property
    def name(self):
        return "ids_with_data_higher_than_average"


class IdsWithDataLowerThanAverage(CustomOperatorBase):
    def run(self):
        field = self.get_input(0, dpf.Field)
        average = common.compute_average_of_field(field)
        ids_in = field.scoping.ids
        data_in = field.data
        out = []
        for i, d in enumerate(data_in):
            if d <= average:
                out.append(ids_in[i])
        scoping_out = dpf.Scoping(ids=out, location=field.scoping.location)
        self.set_output(0, scoping_out)
        self.set_succeeded()

    @property
    def specification(self):
        spec = CustomSpecification("Creates a scoping with all the ids having data lower or equal "
                                   "to the average value of the scalar field's data in input.")
        spec.inputs = {
            0: PinSpecification("field", type_names=dpf.Field, document="scalar Field."),
        }
        spec.outputs = {
            0: PinSpecification("scoping", type_names=dpf.Scoping),
        }
        spec.properties = SpecificationProperties(
            user_name="ids with data lower than average",
            category="logic"
        )
        return spec

    @property
    def name(self):
        return "ids_with_data_lower_than_average"
