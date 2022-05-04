from ansys.dpf.core.custom_operator import CustomOperatorBase

class ForwardIntOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, int)
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
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_str"
