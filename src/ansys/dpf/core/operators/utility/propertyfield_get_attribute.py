"""
propertyfield_get_attribute

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


class propertyfield_get_attribute(Operator):
    r"""A PropertyField in pin 0 and a property name (string) in pin 1 are
    expected in input.


    Parameters
    ----------
    property_field: PropertyField
    property_name: str
        Accepted inputs are: 'time_freq_support', 'scoping' and 'header'.

    Returns
    -------
    property: TimeFreqSupport or Scoping or DataTree
        Property value.

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.propertyfield_get_attribute()

    >>> # Make input connections
    >>> my_property_field = dpf.PropertyField()
    >>> op.inputs.property_field.connect(my_property_field)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.propertyfield_get_attribute(
    ...     property_field=my_property_field,
    ...     property_name=my_property_name,
    ... )

    >>> # Get output data
    >>> result_property = op.outputs.property()
    """

    def __init__(
        self, property_field=None, property_name=None, config=None, server=None
    ):
        super().__init__(
            name="propertyfield::get_attribute", config=config, server=server
        )
        self._inputs = InputsPropertyfieldGetAttribute(self)
        self._outputs = OutputsPropertyfieldGetAttribute(self)
        if property_field is not None:
            self.inputs.property_field.connect(property_field)
        if property_name is not None:
            self.inputs.property_name.connect(property_name)

    @staticmethod
    def _spec() -> Specification:
        description = r"""A PropertyField in pin 0 and a property name (string) in pin 1 are
expected in input.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="property_field",
                    type_names=["property_field"],
                    optional=False,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="property_name",
                    type_names=["string"],
                    optional=False,
                    document=r"""Accepted inputs are: 'time_freq_support', 'scoping' and 'header'.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="property",
                    type_names=["time_freq_support", "scoping", "abstract_data_tree"],
                    optional=False,
                    document=r"""Property value.""",
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
        return Operator.default_config(
            name="propertyfield::get_attribute", server=server
        )

    @property
    def inputs(self) -> InputsPropertyfieldGetAttribute:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsPropertyfieldGetAttribute.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsPropertyfieldGetAttribute:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsPropertyfieldGetAttribute.
        """
        return super().outputs


class InputsPropertyfieldGetAttribute(_Inputs):
    """Intermediate class used to connect user inputs to
    propertyfield_get_attribute operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.propertyfield_get_attribute()
    >>> my_property_field = dpf.PropertyField()
    >>> op.inputs.property_field.connect(my_property_field)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)
    """

    def __init__(self, op: Operator):
        super().__init__(propertyfield_get_attribute._spec().inputs, op)
        self._property_field = Input(
            propertyfield_get_attribute._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._property_field)
        self._property_name = Input(
            propertyfield_get_attribute._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._property_name)

    @property
    def property_field(self) -> Input:
        r"""Allows to connect property_field input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.propertyfield_get_attribute()
        >>> op.inputs.property_field.connect(my_property_field)
        >>> # or
        >>> op.inputs.property_field(my_property_field)
        """
        return self._property_field

    @property
    def property_name(self) -> Input:
        r"""Allows to connect property_name input to the operator.

        Accepted inputs are: 'time_freq_support', 'scoping' and 'header'.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.propertyfield_get_attribute()
        >>> op.inputs.property_name.connect(my_property_name)
        >>> # or
        >>> op.inputs.property_name(my_property_name)
        """
        return self._property_name


class OutputsPropertyfieldGetAttribute(_Outputs):
    """Intermediate class used to get outputs from
    propertyfield_get_attribute operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.propertyfield_get_attribute()
    >>> # Connect inputs : op.inputs. ...
    >>> result_property = op.outputs.property()
    """

    def __init__(self, op: Operator):
        super().__init__(propertyfield_get_attribute._spec().outputs, op)
        self.property_as_time_freq_support = Output(
            _modify_output_spec_with_one_type(
                propertyfield_get_attribute._spec().output_pin(0), "time_freq_support"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_time_freq_support)
        self.property_as_scoping = Output(
            _modify_output_spec_with_one_type(
                propertyfield_get_attribute._spec().output_pin(0), "scoping"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_scoping)
        self.property_as_data_tree = Output(
            _modify_output_spec_with_one_type(
                propertyfield_get_attribute._spec().output_pin(0), "data_tree"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_data_tree)
