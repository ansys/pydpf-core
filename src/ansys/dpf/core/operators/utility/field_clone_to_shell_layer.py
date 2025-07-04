"""
field_clone_to_shell_layer

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


class field_clone_to_shell_layer(Operator):
    r"""Generates a Field from the Field in input 0 that has the same
    FieldDefinition with the exception of the shellLayers enum that is
    specified in input 1. The DataPointer is recomputed to the appropriate
    value. The Data of the output Field is 0.0 for all entities. Scoping can
    be shared or not based on the optional pin 2.


    Parameters
    ----------
    field: Field
    shell_layer: int
        0: Top, 1: Bottom, 2: TopBottom, 3: Mid, 4: TopBottomMid.
    duplicate_scoping: bool, optional
        If true, a new scoping is computed for the output Field. If false, the input Field scoping is used. Default is false.

    Returns
    -------
    field: Field

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.field_clone_to_shell_layer()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_shell_layer = int()
    >>> op.inputs.shell_layer.connect(my_shell_layer)
    >>> my_duplicate_scoping = bool()
    >>> op.inputs.duplicate_scoping.connect(my_duplicate_scoping)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.field_clone_to_shell_layer(
    ...     field=my_field,
    ...     shell_layer=my_shell_layer,
    ...     duplicate_scoping=my_duplicate_scoping,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        field=None,
        shell_layer=None,
        duplicate_scoping=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="field::clone_to_shell_layer", config=config, server=server
        )
        self._inputs = InputsFieldCloneToShellLayer(self)
        self._outputs = OutputsFieldCloneToShellLayer(self)
        if field is not None:
            self.inputs.field.connect(field)
        if shell_layer is not None:
            self.inputs.shell_layer.connect(shell_layer)
        if duplicate_scoping is not None:
            self.inputs.duplicate_scoping.connect(duplicate_scoping)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Generates a Field from the Field in input 0 that has the same
FieldDefinition with the exception of the shellLayers enum that is
specified in input 1. The DataPointer is recomputed to the appropriate
value. The Data of the output Field is 0.0 for all entities. Scoping can
be shared or not based on the optional pin 2.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="shell_layer",
                    type_names=["int32", "enum dataProcessing::EShellLayers"],
                    optional=False,
                    document=r"""0: Top, 1: Bottom, 2: TopBottom, 3: Mid, 4: TopBottomMid.""",
                ),
                2: PinSpecification(
                    name="duplicate_scoping",
                    type_names=["bool"],
                    optional=True,
                    document=r"""If true, a new scoping is computed for the output Field. If false, the input Field scoping is used. Default is false.""",
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
        return Operator.default_config(
            name="field::clone_to_shell_layer", server=server
        )

    @property
    def inputs(self) -> InputsFieldCloneToShellLayer:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsFieldCloneToShellLayer.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsFieldCloneToShellLayer:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsFieldCloneToShellLayer.
        """
        return super().outputs


class InputsFieldCloneToShellLayer(_Inputs):
    """Intermediate class used to connect user inputs to
    field_clone_to_shell_layer operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.field_clone_to_shell_layer()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_shell_layer = int()
    >>> op.inputs.shell_layer.connect(my_shell_layer)
    >>> my_duplicate_scoping = bool()
    >>> op.inputs.duplicate_scoping.connect(my_duplicate_scoping)
    """

    def __init__(self, op: Operator):
        super().__init__(field_clone_to_shell_layer._spec().inputs, op)
        self._field = Input(field_clone_to_shell_layer._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._shell_layer = Input(
            field_clone_to_shell_layer._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._shell_layer)
        self._duplicate_scoping = Input(
            field_clone_to_shell_layer._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._duplicate_scoping)

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
        >>> op = dpf.operators.utility.field_clone_to_shell_layer()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def shell_layer(self) -> Input:
        r"""Allows to connect shell_layer input to the operator.

        0: Top, 1: Bottom, 2: TopBottom, 3: Mid, 4: TopBottomMid.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.field_clone_to_shell_layer()
        >>> op.inputs.shell_layer.connect(my_shell_layer)
        >>> # or
        >>> op.inputs.shell_layer(my_shell_layer)
        """
        return self._shell_layer

    @property
    def duplicate_scoping(self) -> Input:
        r"""Allows to connect duplicate_scoping input to the operator.

        If true, a new scoping is computed for the output Field. If false, the input Field scoping is used. Default is false.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.field_clone_to_shell_layer()
        >>> op.inputs.duplicate_scoping.connect(my_duplicate_scoping)
        >>> # or
        >>> op.inputs.duplicate_scoping(my_duplicate_scoping)
        """
        return self._duplicate_scoping


class OutputsFieldCloneToShellLayer(_Outputs):
    """Intermediate class used to get outputs from
    field_clone_to_shell_layer operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.field_clone_to_shell_layer()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(field_clone_to_shell_layer._spec().outputs, op)
        self._field = Output(field_clone_to_shell_layer._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.utility.field_clone_to_shell_layer()
        >>> # Get the output from op.outputs. ...
        >>> result_field = op.outputs.field()
        """
        return self._field
