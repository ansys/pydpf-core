"""
default_value

Autogenerated DPF operator classes.
"""

from __future__ import annotations

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification
from ansys.dpf.core.config import Config
from ansys.dpf.core.server_types import AnyServerType


class default_value(Operator):
    r"""Default return value from input pin 1 to output pin 0 if there is
    nothing on input pin 0.


    Parameters
    ----------
    forced_value: optional
    default_value:

    Returns
    -------
    output:

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.default_value()

    >>> # Make input connections
    >>> my_forced_value = dpf.()
    >>> op.inputs.forced_value.connect(my_forced_value)
    >>> my_default_value = dpf.()
    >>> op.inputs.default_value.connect(my_default_value)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.default_value(
    ...     forced_value=my_forced_value,
    ...     default_value=my_default_value,
    ... )

    >>> # Get output data
    >>> result_output = op.outputs.output()
    """

    def __init__(self, forced_value=None, default_value=None, config=None, server=None):
        super().__init__(name="default_value", config=config, server=server)
        self._inputs = InputsDefaultValue(self)
        self._outputs = OutputsDefaultValue(self)
        if forced_value is not None:
            self.inputs.forced_value.connect(forced_value)
        if default_value is not None:
            self.inputs.default_value.connect(default_value)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Default return value from input pin 1 to output pin 0 if there is
nothing on input pin 0.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="forced_value",
                    type_names=["any"],
                    optional=True,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="default_value",
                    type_names=["any"],
                    optional=False,
                    document=r"""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="output",
                    optional=False,
                    document=r"""""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server: AnyServerType = None) -> Config:
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server:
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.

        Returns
        -------
        config:
            A new Config instance equivalent to the default config for this operator.
        """
        return Operator.default_config(name="default_value", server=server)

    @property
    def inputs(self) -> InputsDefaultValue:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsDefaultValue.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsDefaultValue:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsDefaultValue.
        """
        return super().outputs


class InputsDefaultValue(_Inputs):
    """Intermediate class used to connect user inputs to
    default_value operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.default_value()
    >>> my_forced_value = dpf.()
    >>> op.inputs.forced_value.connect(my_forced_value)
    >>> my_default_value = dpf.()
    >>> op.inputs.default_value.connect(my_default_value)
    """

    def __init__(self, op: Operator):
        super().__init__(default_value._spec().inputs, op)
        self._forced_value = Input(default_value._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._forced_value)
        self._default_value = Input(default_value._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._default_value)

    @property
    def forced_value(self) -> Input:
        r"""Allows to connect forced_value input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.default_value()
        >>> op.inputs.forced_value.connect(my_forced_value)
        >>> # or
        >>> op.inputs.forced_value(my_forced_value)
        """
        return self._forced_value

    @property
    def default_value(self) -> Input:
        r"""Allows to connect default_value input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.default_value()
        >>> op.inputs.default_value.connect(my_default_value)
        >>> # or
        >>> op.inputs.default_value(my_default_value)
        """
        return self._default_value


class OutputsDefaultValue(_Outputs):
    """Intermediate class used to get outputs from
    default_value operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.default_value()
    >>> # Connect inputs : op.inputs. ...
    >>> result_output = op.outputs.output()
    """

    def __init__(self, op: Operator):
        super().__init__(default_value._spec().outputs, op)
        self._output = Output(default_value._spec().output_pin(0), 0, op)
        self._outputs.append(self._output)

    @property
    def output(self) -> Output:
        r"""Allows to get output output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.default_value()
        >>> # Get the output from op.outputs. ...
        >>> result_output = op.outputs.output()
        """
        return self._output
