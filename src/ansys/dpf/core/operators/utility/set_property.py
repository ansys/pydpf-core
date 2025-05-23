"""
set_property

Autogenerated DPF operator classes.
"""

from __future__ import annotations

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.outputs import _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification
from ansys.dpf.core.config import Config
from ansys.dpf.core.server_types import AnyServerType


class set_property(Operator):
    r"""Sets a property to an input field/field container.


    Parameters
    ----------
    field: Field or FieldsContainer
    property_name: str
        Property to set
    property_value: str or int or float
        Property to set

    Returns
    -------
    field: Field or FieldsContainer

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.set_property()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)
    >>> my_property_value = str()
    >>> op.inputs.property_value.connect(my_property_value)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.set_property(
    ...     field=my_field,
    ...     property_name=my_property_name,
    ...     property_value=my_property_value,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        field=None,
        property_name=None,
        property_value=None,
        config=None,
        server=None,
    ):
        super().__init__(name="field::set_property", config=config, server=server)
        self._inputs = InputsSetProperty(self)
        self._outputs = OutputsSetProperty(self)
        if field is not None:
            self.inputs.field.connect(field)
        if property_name is not None:
            self.inputs.property_name.connect(property_name)
        if property_value is not None:
            self.inputs.property_value.connect(property_value)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Sets a property to an input field/field container.
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
                    name="property_name",
                    type_names=["string"],
                    optional=False,
                    document=r"""Property to set""",
                ),
                2: PinSpecification(
                    name="property_value",
                    type_names=["string", "int32", "double"],
                    optional=False,
                    document=r"""Property to set""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
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
        return Operator.default_config(name="field::set_property", server=server)

    @property
    def inputs(self) -> InputsSetProperty:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsSetProperty.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsSetProperty:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsSetProperty.
        """
        return super().outputs


class InputsSetProperty(_Inputs):
    """Intermediate class used to connect user inputs to
    set_property operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.set_property()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)
    >>> my_property_value = str()
    >>> op.inputs.property_value.connect(my_property_value)
    """

    def __init__(self, op: Operator):
        super().__init__(set_property._spec().inputs, op)
        self._field = Input(set_property._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._property_name = Input(set_property._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._property_name)
        self._property_value = Input(set_property._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._property_value)

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
        >>> op = dpf.operators.utility.set_property()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def property_name(self) -> Input:
        r"""Allows to connect property_name input to the operator.

        Property to set

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.set_property()
        >>> op.inputs.property_name.connect(my_property_name)
        >>> # or
        >>> op.inputs.property_name(my_property_name)
        """
        return self._property_name

    @property
    def property_value(self) -> Input:
        r"""Allows to connect property_value input to the operator.

        Property to set

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.set_property()
        >>> op.inputs.property_value.connect(my_property_value)
        >>> # or
        >>> op.inputs.property_value(my_property_value)
        """
        return self._property_value


class OutputsSetProperty(_Outputs):
    """Intermediate class used to get outputs from
    set_property operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.set_property()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(set_property._spec().outputs, op)
        self.field_as_field = Output(
            _modify_output_spec_with_one_type(
                set_property._spec().output_pin(0), "field"
            ),
            0,
            op,
        )
        self._outputs.append(self.field_as_field)
        self.field_as_fields_container = Output(
            _modify_output_spec_with_one_type(
                set_property._spec().output_pin(0), "fields_container"
            ),
            0,
            op,
        )
        self._outputs.append(self.field_as_fields_container)
