"""
rotate

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


class rotate(Operator):
    r"""Applies a transformation (rotation) matrix on a field.


    Parameters
    ----------
    field: Field or FieldsContainer
        field or fields container with only one field is expected
    field_rotation_matrix: Field
        3-3 rotation matrix

    Returns
    -------
    field: Field

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.geo.rotate()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_field_rotation_matrix = dpf.Field()
    >>> op.inputs.field_rotation_matrix.connect(my_field_rotation_matrix)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.geo.rotate(
    ...     field=my_field,
    ...     field_rotation_matrix=my_field_rotation_matrix,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self, field=None, field_rotation_matrix=None, config=None, server=None
    ):
        super().__init__(name="rotate", config=config, server=server)
        self._inputs = InputsRotate(self)
        self._outputs = OutputsRotate(self)
        if field is not None:
            self.inputs.field.connect(field)
        if field_rotation_matrix is not None:
            self.inputs.field_rotation_matrix.connect(field_rotation_matrix)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Applies a transformation (rotation) matrix on a field.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document=r"""field or fields container with only one field is expected""",
                ),
                1: PinSpecification(
                    name="field_rotation_matrix",
                    type_names=["field"],
                    optional=False,
                    document=r"""3-3 rotation matrix""",
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
        return Operator.default_config(name="rotate", server=server)

    @property
    def inputs(self) -> InputsRotate:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsRotate.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsRotate:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsRotate.
        """
        return super().outputs


class InputsRotate(_Inputs):
    """Intermediate class used to connect user inputs to
    rotate operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.rotate()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_field_rotation_matrix = dpf.Field()
    >>> op.inputs.field_rotation_matrix.connect(my_field_rotation_matrix)
    """

    def __init__(self, op: Operator):
        super().__init__(rotate._spec().inputs, op)
        self._field = Input(rotate._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._field_rotation_matrix = Input(rotate._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._field_rotation_matrix)

    @property
    def field(self) -> Input:
        r"""Allows to connect field input to the operator.

        field or fields container with only one field is expected

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.rotate()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def field_rotation_matrix(self) -> Input:
        r"""Allows to connect field_rotation_matrix input to the operator.

        3-3 rotation matrix

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.rotate()
        >>> op.inputs.field_rotation_matrix.connect(my_field_rotation_matrix)
        >>> # or
        >>> op.inputs.field_rotation_matrix(my_field_rotation_matrix)
        """
        return self._field_rotation_matrix


class OutputsRotate(_Outputs):
    """Intermediate class used to get outputs from
    rotate operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.rotate()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(rotate._spec().outputs, op)
        self._field = Output(rotate._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.geo.rotate()
        >>> # Get the output from op.outputs. ...
        >>> result_field = op.outputs.field()
        """
        return self._field
