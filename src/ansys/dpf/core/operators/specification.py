from ansys.dpf.core.operator_specification import SpecificationBase, PinSpecification


class Specification(SpecificationBase):
    def __init__(self, description=None, map_input_pin_spec=None, map_output_pin_spec=None, config=None):

        self._description = description
        self._map_input_pin_spec = map_input_pin_spec
        self._map_output_pin_spec = map_output_pin_spec



    @property
    def map_input_pin_spec(self):
        return self._map_input_pin_spec

    @property
    def map_output_pin_spec(self):
        return self._map_output_pin_spec

    @property
    def inputs(self):
        return self._map_input_pin_spec

    @property
    def outputs(self):
        return self._map_output_pin_spec

    def output_pin(self, pin_num):
        return self._map_output_pin_spec[pin_num]

    def input_pin(self, pin_num):
        return self._map_input_pin_spec[pin_num]

    @property
    def description(self):
        return self._description

    def __str__(self):
        out = ""
        for key, i in self._asdict().items():
            out += key + ": " + str(i) + "\n\n"
        return out
