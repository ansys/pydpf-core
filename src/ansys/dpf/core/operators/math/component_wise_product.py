"""
component_wise_product

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


class component_wise_product(Operator):
    r"""Computes component-wise product between two fields of same
    dimensionality. If one field’s scoping has an ‘overall’ location, then
    this field’s values are applied on the other field entirely. When using
    a constant or ‘work_by_index’, you can use ‘inplace’ to reuse one of the
    fields.


    Parameters
    ----------
    fieldA: Field or FieldsContainer
        field or fields container with only one field is expected
    fieldB: Field or FieldsContainer
        field or fields container with only one field is expected

    Returns
    -------
    field: Field

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.component_wise_product()

    >>> # Make input connections
    >>> my_fieldA = dpf.Field()
    >>> op.inputs.fieldA.connect(my_fieldA)
    >>> my_fieldB = dpf.Field()
    >>> op.inputs.fieldB.connect(my_fieldB)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.component_wise_product(
    ...     fieldA=my_fieldA,
    ...     fieldB=my_fieldB,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="component_wise_product", config=config, server=server)
        self._inputs = InputsComponentWiseProduct(self)
        self._outputs = OutputsComponentWiseProduct(self)
        if fieldA is not None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB is not None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Computes component-wise product between two fields of same
dimensionality. If one field’s scoping has an ‘overall’ location, then
this field’s values are applied on the other field entirely. When using
a constant or ‘work_by_index’, you can use ‘inplace’ to reuse one of the
fields.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fieldA",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document=r"""field or fields container with only one field is expected""",
                ),
                1: PinSpecification(
                    name="fieldB",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document=r"""field or fields container with only one field is expected""",
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
        return Operator.default_config(name="component_wise_product", server=server)

    @property
    def inputs(self) -> InputsComponentWiseProduct:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsComponentWiseProduct.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsComponentWiseProduct:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsComponentWiseProduct.
        """
        return super().outputs


class InputsComponentWiseProduct(_Inputs):
    """Intermediate class used to connect user inputs to
    component_wise_product operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.component_wise_product()
    >>> my_fieldA = dpf.Field()
    >>> op.inputs.fieldA.connect(my_fieldA)
    >>> my_fieldB = dpf.Field()
    >>> op.inputs.fieldB.connect(my_fieldB)
    """

    def __init__(self, op: Operator):
        super().__init__(component_wise_product._spec().inputs, op)
        self._fieldA = Input(component_wise_product._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fieldA)
        self._fieldB = Input(component_wise_product._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._fieldB)

    @property
    def fieldA(self) -> Input:
        r"""Allows to connect fieldA input to the operator.

        field or fields container with only one field is expected

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.component_wise_product()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> # or
        >>> op.inputs.fieldA(my_fieldA)
        """
        return self._fieldA

    @property
    def fieldB(self) -> Input:
        r"""Allows to connect fieldB input to the operator.

        field or fields container with only one field is expected

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.component_wise_product()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> # or
        >>> op.inputs.fieldB(my_fieldB)
        """
        return self._fieldB


class OutputsComponentWiseProduct(_Outputs):
    """Intermediate class used to get outputs from
    component_wise_product operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.component_wise_product()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(component_wise_product._spec().outputs, op)
        self._field = Output(component_wise_product._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.component_wise_product()
        >>> # Get the output from op.outputs. ...
        >>> result_field = op.outputs.field()
        """
        return self._field
