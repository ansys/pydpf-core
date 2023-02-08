from ansys.dpf.core import types
from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    PinSpecification,
    SpecificationProperties,
)


class ForwardIntOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, int)
        f = self.get_input(0, types.int)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_int"


class ForwardFloatOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, float)
        f = self.get_input(0, types.double)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_float"


class ForwardBoolOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, bool)
        f = self.get_input(0, types.bool)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_bool"


class ForwardStringOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, str)
        f = self.get_input(0, types.string)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_str"


class ForwardVecIntOperator(CustomOperatorBase):
    def run(self):
        input = self.get_input(0, types.vec_int)
        self.set_output(0, input)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_vec_int"


class SetOutVecDoubleOperator(CustomOperatorBase):
    def run(self):
        out = [1.0, 2.0, 3.0]
        self.set_output(0, out)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_set_out_vec_double"


class SetOutNpArrayIntOperator(CustomOperatorBase):
    def run(self):
        import numpy

        out = numpy.ones((100, 2), dtype=numpy.int32)
        self.set_output(0, out)
        self.set_succeeded()

    @property
    def specification(self):
        spec = CustomSpecification()
        spec.outputs = {0: PinSpecification("flat_int_vec", type_names=types.vec_int)}
        spec.description = (
            "Sets a numpy array of shape (100,2) as output. " "The array is flatten by DPF."
        )
        spec.properties = SpecificationProperties(
            user_name="set out numpy array of int", category="logic"
        )
        return spec

    @property
    def name(self):
        return "custom_set_out_np_int"


class SetOutNpArrayDoubleOperator(CustomOperatorBase):
    def run(self):
        import numpy

        out = numpy.ones((100, 2))
        self.set_output(0, out)
        self.set_succeeded()

    @property
    def specification(self):
        spec = CustomSpecification(
            "Sets a numpy array of shape (100,2) as output." " The array is flatten by DPF."
        )
        spec.outputs = {0: PinSpecification("flat_double_vec", type_names=types.vec_double)}
        spec.properties = SpecificationProperties(
            user_name="set out numpy array of double", category="logic"
        )
        return spec

    @property
    def name(self):
        return "custom_set_out_np_double"
