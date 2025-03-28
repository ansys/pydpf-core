"""
component_selector

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


class component_selector(Operator):
    r"""Creates a scalar/vector field based on the selected component.


    Parameters
    ----------
    field: Field or FieldsContainer
    component_number: int
        One or several component index that will be extracted from the initial field.
    default_value: float, optional
        Set a default value for components that do not exist.

    Returns
    -------
    field: Field

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.logic.component_selector()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_component_number = int()
    >>> op.inputs.component_number.connect(my_component_number)
    >>> my_default_value = float()
    >>> op.inputs.default_value.connect(my_default_value)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.logic.component_selector(
    ...     field=my_field,
    ...     component_number=my_component_number,
    ...     default_value=my_default_value,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        field=None,
        component_number=None,
        default_value=None,
        config=None,
        server=None,
    ):
        super().__init__(name="component_selector", config=config, server=server)
        self._inputs = InputsComponentSelector(self)
        self._outputs = OutputsComponentSelector(self)
        if field is not None:
            self.inputs.field.connect(field)
        if component_number is not None:
            self.inputs.component_number.connect(component_number)
        if default_value is not None:
            self.inputs.default_value.connect(default_value)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Creates a scalar/vector field based on the selected component.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="component_number",
                    type_names=["int32", "vector<int32>"],
                    optional=False,
                    document=r"""One or several component index that will be extracted from the initial field.""",
                ),
                2: PinSpecification(
                    name="default_value",
                    type_names=["double"],
                    optional=True,
                    document=r"""Set a default value for components that do not exist.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
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
        return Operator.default_config(name="component_selector", server=server)

    @property
    def inputs(self) -> InputsComponentSelector:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsComponentSelector.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsComponentSelector:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsComponentSelector.
        """
        return super().outputs


class InputsComponentSelector(_Inputs):
    """Intermediate class used to connect user inputs to
    component_selector operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.component_selector()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_component_number = int()
    >>> op.inputs.component_number.connect(my_component_number)
    >>> my_default_value = float()
    >>> op.inputs.default_value.connect(my_default_value)
    """

    def __init__(self, op: Operator):
        super().__init__(component_selector._spec().inputs, op)
        self._field = Input(component_selector._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._component_number = Input(
            component_selector._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._component_number)
        self._default_value = Input(component_selector._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._default_value)

    @property
    def field(self) -> Input:
        r"""Allows to connect field input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.component_selector()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def component_number(self) -> Input:
        r"""Allows to connect component_number input to the operator.

        One or several component index that will be extracted from the initial field.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.component_selector()
        >>> op.inputs.component_number.connect(my_component_number)
        >>> # or
        >>> op.inputs.component_number(my_component_number)
        """
        return self._component_number

    @property
    def default_value(self) -> Input:
        r"""Allows to connect default_value input to the operator.

        Set a default value for components that do not exist.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.component_selector()
        >>> op.inputs.default_value.connect(my_default_value)
        >>> # or
        >>> op.inputs.default_value(my_default_value)
        """
        return self._default_value


class OutputsComponentSelector(_Outputs):
    """Intermediate class used to get outputs from
    component_selector operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.component_selector()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(component_selector._spec().outputs, op)
        self._field = Output(component_selector._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self) -> Output:
        r"""Allows to get field output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.component_selector()
        >>> # Get the output from op.outputs. ...
        >>> result_field = op.outputs.field()
        """
        return self._field
