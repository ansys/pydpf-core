"""
component_selector_fc

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


class component_selector_fc(Operator):
    r"""Creates a scalar fields container based on the selected component for
    each field.


    Parameters
    ----------
    fields_container: FieldsContainer or Field
    component_number: int
        one or several component index that will be extracted from the initial field.

    Returns
    -------
    fields_container: FieldsContainer

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.logic.component_selector_fc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_component_number = int()
    >>> op.inputs.component_number.connect(my_component_number)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.logic.component_selector_fc(
    ...     fields_container=my_fields_container,
    ...     component_number=my_component_number,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self, fields_container=None, component_number=None, config=None, server=None
    ):
        super().__init__(name="component_selector_fc", config=config, server=server)
        self._inputs = InputsComponentSelectorFc(self)
        self._outputs = OutputsComponentSelectorFc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if component_number is not None:
            self.inputs.component_number.connect(component_number)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Creates a scalar fields container based on the selected component for
each field.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container", "field"],
                    optional=False,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="component_number",
                    type_names=["int32", "vector<int32>"],
                    optional=False,
                    document=r"""one or several component index that will be extracted from the initial field.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
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
        return Operator.default_config(name="component_selector_fc", server=server)

    @property
    def inputs(self) -> InputsComponentSelectorFc:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsComponentSelectorFc.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsComponentSelectorFc:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsComponentSelectorFc.
        """
        return super().outputs


class InputsComponentSelectorFc(_Inputs):
    """Intermediate class used to connect user inputs to
    component_selector_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.component_selector_fc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_component_number = int()
    >>> op.inputs.component_number.connect(my_component_number)
    """

    def __init__(self, op: Operator):
        super().__init__(component_selector_fc._spec().inputs, op)
        self._fields_container = Input(
            component_selector_fc._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._component_number = Input(
            component_selector_fc._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._component_number)

    @property
    def fields_container(self) -> Input:
        r"""Allows to connect fields_container input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.component_selector_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def component_number(self) -> Input:
        r"""Allows to connect component_number input to the operator.

        one or several component index that will be extracted from the initial field.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.component_selector_fc()
        >>> op.inputs.component_number.connect(my_component_number)
        >>> # or
        >>> op.inputs.component_number(my_component_number)
        """
        return self._component_number


class OutputsComponentSelectorFc(_Outputs):
    """Intermediate class used to get outputs from
    component_selector_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.component_selector_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(component_selector_fc._spec().outputs, op)
        self._fields_container = Output(
            component_selector_fc._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self) -> Output:
        r"""Allows to get fields_container output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.component_selector_fc()
        >>> # Get the output from op.outputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """
        return self._fields_container
