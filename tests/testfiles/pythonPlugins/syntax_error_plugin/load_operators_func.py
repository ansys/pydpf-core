from ansys.dpf.core.custom_operator import CustomOperatorBase, record_operator


class SyntaxeError(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, int)
        self.set_ouuuuuutput(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "raising"


def load_operators(*args):
    record_operator(SyntaxeError, *args)
