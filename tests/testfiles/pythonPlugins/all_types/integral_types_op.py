from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core import types


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
