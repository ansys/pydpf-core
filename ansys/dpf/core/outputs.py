"""
.. _ref_outputs:

Outputs
=======
"""

from ansys.dpf.core.mapping_types import map_types_to_python
from ansys.dpf.core.common import types
from ansys.dpf.core.operator_specification import PinSpecification
import re


class Output:
    """
    Intermediate class internally instantiated by the :class:`ansys.dpf.core.dpf_operator.Operator`.
    Used to evaluate and get outputs of the Operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> data_src = dpf.DataSources(examples.msup_transient)
    >>> disp_op = dpf.operators.result.displacement()
    >>> disp_op.inputs.data_sources(data_src)
    >>> isinstance(disp_op.outputs.fields_container, dpf.inputs.Output)
    True
    >>> fc = disp_op.outputs.fields_container()
    """
    def __init__(self, spec, pin, operator):
        self._spec = spec
        self._operator = operator
        self._pin = pin
        self._python_expected_types = []
        for cpp_type in self._spec.type_names:
            self._python_expected_types.append(map_types_to_python[cpp_type])

    def get_data(self):
        """Retrieves the output of the operator."""
        type_output = self._spec.type_names[0]
        if type_output == "abstract_meshed_region":
            type_output = types.meshed_region
        elif type_output == "abstract_data_tree":
            type_output = types.data_tree
        elif type_output == "fields_container":
            type_output = types.fields_container
        elif type_output == "scopings_container":
            type_output = types.scopings_container
        elif type_output == "meshes_container":
            type_output = types.meshes_container

        return self._operator.get_output(self._pin, type_output)

    def __call__(self):
        return self.get_data()

    def __str__(self):
        docstr = self._spec.name
        if self._spec.optional:
            docstr += " (optional)"
        docstr += ", expects types:" + "\n"
        for exp_types in self._python_expected_types:
            docstr += "   -" + exp_types + "\n"
        if self._spec.document:
            docstr += "help: " + self._spec.document + "\n"
        return docstr


class _Outputs:
    """
    Parameters
    ----------
    dict_outputs : dict
        Dictionary of outputs.
    operator :

    """

    def __init__(self, dict_outputs, operator):
        self._dict_outputs = dict_outputs
        self._operator = operator
        self._outputs = []

    def _get_given_output(self, input_type_name):
        corresponding_pins = []
        for asked_camel_types in input_type_name:
            for pin in self._dict_outputs:
                for cpp_type in self._dict_outputs[pin].type_names:
                    if map_types_to_python[cpp_type] == asked_camel_types:
                        corresponding_pins.append(pin)
                    elif asked_camel_types == "Any":
                        corresponding_pins.append(pin)
        return corresponding_pins

    def __str__(self):
        docstr = "Available outputs:\n"
        for output in self._outputs:
            tot_string = str(output._spec.name)
            input_string = tot_string.split("\n")
            input_string1 = input_string[0]
            line = ["   ", "- ", input_string1]
            docstr += "{:<5}{:<4}{:<20}\n".format(*line)
            for inputstr in input_string:
                if inputstr != input_string1:
                    line = ["   ", "  ", inputstr]
                    docstr += "{:<5}{:<4}{:<20}".format(*line)
                    docstr += "\n"
        return docstr


def _clearRepeatedMessage(message):
    try:
        while True:
            message.pop(len(message) - 1)
    except:
        pass


def _make_printable_type(type):
    """Remove characters not allowed in function names in Python."""
    chars_to_remove = ["<", ">", "-", "!", "?", "."]
    rx = "[" + re.escape("_".join(chars_to_remove)) + "]"
    type = re.sub(rx, "_", type)
    type = type.replace("abstract_", "")
    return type


def _modify_output_spec_with_one_type(output_spec, type):
    spec = PinSpecification._get_copy(output_spec, [type])
    return spec


class Outputs(_Outputs):
    """
    Intermediate class internally instantiated by the :class:`ansys.dpf.core.dpf_operator.Operator`.
    Used to list the available :class:`ansys.dpf.core.outputs.Output` s of the Operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> data_src = dpf.DataSources(examples.msup_transient)
    >>> disp_op = dpf.operators.result.displacement()
    >>> disp_op.inputs.data_sources(data_src)
    >>> isinstance(disp_op.outputs, dpf.inputs._Outputs)
    True
    >>> fc = disp_op.outputs.fields_container()
    """

    def __init__(self, dict_outputs, operator):
        super().__init__(dict_outputs, operator)
        for pin in self._dict_outputs:
            if (
                len(self._dict_outputs[pin].type_names) == 1
                and self._dict_outputs[pin] is not None
            ):
                output_name = self._dict_outputs[pin].name
                output = Output(self._dict_outputs[pin], pin, self._operator)
                self._outputs.append(output)
                if hasattr(self, output_name):  # for autogenerated code
                    setattr(self, "_" + output_name, output)
                else:
                    setattr(self, output_name, output)
            # generate 1 output by type name
            elif (
                len(self._dict_outputs[pin].type_names) > 1
                and self._dict_outputs[pin] is not None
            ):
                for type in self._dict_outputs[pin].type_names:
                    output_name = (
                        self._dict_outputs[pin].name
                        + "_as_"
                        + _make_printable_type(type)
                    )
                    output = Output(
                        _modify_output_spec_with_one_type(
                            self._dict_outputs[pin], type
                        ),
                        pin,
                        self._operator,
                    )
                    self._outputs.append(output)
                    if hasattr(self, output_name):  # for autogenerated code
                        setattr(self, "_" + output_name, output)
                    else:
                        setattr(self, output_name, output)
