"""
.. _ref_inputs:

Inputs
======
"""

import weakref
from textwrap import wrap
from ansys.dpf.core.mapping_types import map_types_to_python
from ansys.dpf.core.outputs import _Outputs, Output
from ansys.dpf import core


class Input:
    """
    Intermediate class internally instantiated by the :class:`ansys.dpf.core.dpf_operator.Operator`.
    Used to connect inputs to the Operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> data_src = dpf.DataSources(examples.msup_transient)
    >>> disp_op = dpf.operators.result.displacement()
    >>> isinstance(disp_op.inputs.data_sources, dpf.inputs.Input)
    True
    >>> disp_op.inputs.data_sources(data_src)
    >>> disp_op.inputs.time_scoping([2])

    """

    def __init__(self, spec, pin, operator, count_ellipsis=-1):
        self._spec = spec
        self._operator = weakref.ref(operator)
        self._pin = pin
        self._count_ellipsis = count_ellipsis
        self._python_expected_types = []
        for cpp_type in self._spec.type_names:
            python_type = map_types_to_python[cpp_type]
            if python_type not in self._python_expected_types:
                self._python_expected_types.append(map_types_to_python[cpp_type])
        if len(self._spec.type_names) == 0:
            self._python_expected_types.append("Any")
        docstr = self.__str__()
        self.name = self._spec.name
        if self._count_ellipsis != -1:
            self.name += str(self._count_ellipsis + 1)
        self._update_doc_str(docstr, self.name)

    def connect(self, inpt):
        """Connect any input (entity or operator output) to a specified input pin of this operator.

        Parameters
        ----------
        inpt : str, int, double, Field, FieldsContainer, Scoping, DataSources, MeshedRegion,
        Output, Outputs, Operator, os.PathLike
            Input of the operator.

        """
        from pathlib import Path
        # always convert ranges to lists
        if isinstance(inpt, range):
            inpt = list(inpt)
        elif isinstance(inpt, core.Operator):
            if hasattr(inpt, "outputs"):
                inpt = inpt.outputs
            else:
                raise ValueError(
                    "The operator to connect in input has no outputs "
                    "available. It cannot be connected."
                )
        elif isinstance(inpt, core.Model):
            inpt = inpt.metadata.data_sources
        elif isinstance(inpt, Path):
            inpt = str(inpt)

        input_type_name = type(inpt).__name__
        if not (
            input_type_name in self._python_expected_types
            or ["Outputs", "Output", "Any"]
        ):
            for types in self._python_expected_types:
                print(types, end=" ")
            print("types are expected for", self._spec.name, "pin")
            return

        corresponding_pins = []
        self._operator()._find_outputs_corresponding_pins(
            self._python_expected_types, inpt, self._pin, corresponding_pins
        )
        if len(corresponding_pins) > 1:
            err_str = "Pin connection is ambiguous, specify the pin with:\n"
            for pin in corresponding_pins:
                err_str += (
                    "   - operator.inputs."
                    + self._spec.name
                    + "(out_op."
                    + inpt._dict_outputs[pin[1]].name
                    + ")"
                )
            raise ValueError(err_str)

        if len(corresponding_pins) == 0:
            err_str = (
                f"The input operator for the {self._spec.name} pin must be "
                "one of the following types:\n"
            )
            err_str += "\n".join(
                [f"- {py_type}" for py_type in self._python_expected_types]
            )
            raise TypeError(err_str)

        from ansys.dpf.core.results import Result

        if isinstance(inpt, _Outputs):
            self._operator().connect(self._pin, inpt._operator, corresponding_pins[0][1])
            self._operator().inputs._connected_inputs[self._pin] = {
                corresponding_pins[0][1]: weakref.ref(inpt._operator)
            }
        elif isinstance(inpt, Output):
            self._operator().connect(self._pin, inpt._operator, inpt._pin)
            self._operator().inputs._connected_inputs[self._pin] = {inpt._pin: weakref.ref(inpt)}
        elif isinstance(inpt, Result):
            self._operator().connect(self._pin, inpt(), corresponding_pins[0][1])
            self._operator().inputs._connected_inputs[self._pin] = {
                corresponding_pins[0][1]: weakref.ref(inpt)
                }
        else:
            self._operator().connect(self._pin, inpt)
            self._operator().inputs._connected_inputs[self._pin] = weakref.ref(inpt) \
                if hasattr(inpt, "__weakref__") else inpt

        self.__inc_if_ellipsis()

    def __call__(self, inpt):
        self.connect(inpt)

    def _update_doc_str(self, docstr, class_name):
        """Dynamically update the docstring of this instance by creating a class on the fly.

        Parameters
        ----------
        docstr :

        class_name :
        """
        child_class = type(class_name, (self.__class__,), {"__doc__": docstr})
        self.__class__ = child_class

    def __str__(self):
        docstr = self._spec.name + " : "
        type_info = self._python_expected_types.copy()
        if self._spec.optional:
            type_info += ["optional"]
        docstr += ", ".join(type_info) + "\n"
        if self._spec.document:
            docstr += "\n".join(wrap(self._spec.document.capitalize())) + "\n"
        if self._count_ellipsis >= 0:
            docstr += "is ellipsis\n"
        return docstr

    def __inc_if_ellipsis(self):
        if self._count_ellipsis >= 0:
            self._count_ellipsis += 1
            if isinstance(self._operator().inputs, _Inputs):
                self._operator().inputs._add_input(
                    self._pin + self._count_ellipsis, self._spec, self._count_ellipsis
                )


class _Inputs:
    def __init__(self, dict_inputs, operator):
        self._dict_inputs = dict_inputs
        self._operator = weakref.ref(operator)
        self._inputs = []
        self._connected_inputs = {}

    def __str__(self):
        docstr = "Available inputs:\n"
        for inp in self._inputs:
            tot_string = inp.__str__()
            input_string = tot_string.split("\n")
            input_string1 = input_string[0]
            line = ["   ", "- ", input_string1]
            docstr += "{:<5}{:<4}{:<20}\n".format(*line)
            for inputstr in input_string:
                if inputstr != input_string1:
                    line = ["   ", "  ", inputstr]
                    docstr += "{:<5}{:<4}{:<20}\n".format(*line)
        return docstr

    def connect(self, inpt):
        """Connect any input (an entity or an operator output) to any input pin of this operator.
        Searches for the input type corresponding to the output.

        Parameters
        ----------
        inpt : str, int, double, bool, list[int], list[float], Field, FieldsContainer, Scoping,
        ScopingsContainer, MeshedRegion, MeshesContainer, DataSources, CyclicSupport, Outputs, os.PathLike  # noqa: E501
            Input of the operator.

        """
        from pathlib import Path
        corresponding_pins = []
        if isinstance(inpt, core.Operator):
            if hasattr(inpt, "outputs"):
                inpt = inpt.outputs
            else:
                raise ValueError(
                    "The operator to connect in input has no outputs "
                    "available. It cannot be connected."
                )
        elif isinstance(inpt, core.Model):
            inpt = inpt.metadata.data_sources
        elif isinstance(inpt, Path):
            inpt = str(inpt)

        input_type_name = type(inpt).__name__
        for input_pin in self._inputs:
            self._operator()._find_outputs_corresponding_pins(
                input_pin._python_expected_types,
                inpt,
                input_pin._pin,
                corresponding_pins,
            )
        if len(corresponding_pins) > 1:
            err_str = "Pin connection is ambiguous, specify the pin with:\n"
            for pin in corresponding_pins:
                if isinstance(pin, tuple):
                    pin = pin[0]
                err_str += (
                    "   - operator.inputs." + self._dict_inputs[pin].name + "(input)\n"
                )
            raise ValueError(err_str)

        if len(corresponding_pins) == 0:
            err_str = "The input should have one of the expected types:\n"
            for pin, spec in self._dict_inputs.items():
                for cpp_type in spec.type_names:
                    err_str += f"   - {map_types_to_python[cpp_type]}\n"
            raise TypeError(err_str)

        from ansys.dpf.core.results import Result
        if isinstance(inpt, Output):
            self._operator().connect(corresponding_pins[0], inpt._operator, inpt._pin)
            self._connected_inputs[corresponding_pins[0]] = {inpt._pin: weakref.ref(inpt._operator)}
        elif isinstance(inpt, _Outputs):
            self._operator().connect(
                corresponding_pins[0][0], inpt._operator, corresponding_pins[0][1]
            )
            self._connected_inputs[corresponding_pins[0][0]] = {
                corresponding_pins[0][1]: weakref.ref(inpt._operator)
            }
        elif isinstance(inpt, Result):
            self._operator().connect(
                corresponding_pins[0][0], inpt(), corresponding_pins[0][1]
            )
            self._connected_inputs[corresponding_pins[0][0]] = {
                corresponding_pins[0][1]: weakref.ref(inpt)
            }
        else:
            self._operator().connect(corresponding_pins[0], inpt)
            self._connected_inputs[corresponding_pins[0]] = weakref.ref(inpt) \
                if hasattr(inpt, "__weakref__") else inpt

    def _add_input(self, pin, spec, count_ellipsis=-1):
        if spec is not None:
            class_input = Input(spec, pin, self._operator(), count_ellipsis)
            class_input.__doc__ = spec.name
            if not hasattr(self, class_input.name):
                setattr(self, class_input.name, class_input)
            else:
                setattr(self, "_" + class_input.name, class_input)
            self._inputs.append(class_input)

    def __call__(self, inpt):
        self.connect(inpt)


# Dynamic class Inputs
class Inputs(_Inputs):
    """
    Intermediate class internally instantiated by the :class:`ansys.dpf.core.dpf_operator.Operator`.
    Used to connect inputs to the Operator by automatically
    checking types to connect correct inputs.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> data_src = dpf.DataSources(examples.msup_transient)
    >>> disp_op = dpf.operators.result.displacement()
    >>> isinstance(disp_op.inputs, dpf.inputs._Inputs)
    True
    >>> disp_op.inputs.connect(data_src)
    >>> disp_op.inputs.connect([2])
    """
    def __init__(self, dict_inputs, operator):
        super().__init__(dict_inputs, operator)

        # dynamically populate input attributes
        for pin, spec in self._dict_inputs.items():
            if spec.ellipsis:
                self._add_input(pin, spec, 0)
            else:
                self._add_input(pin, spec)
