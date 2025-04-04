"""
global_to_nodal

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


class global_to_nodal(Operator):
    r"""Rotate results from global coordinate system to local coordinate system.


    Parameters
    ----------
    fieldA: Field
        Vector or tensor field that must be rotated, expressed in global coordinate system.
    fieldB: Field
        Nodal euler angles defined from a result file. Those  must be the rotations from Nodal to Global.

    Returns
    -------
    field: Field
        Rotated field

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.global_to_nodal()

    >>> # Make input connections
    >>> my_fieldA = dpf.Field()
    >>> op.inputs.fieldA.connect(my_fieldA)
    >>> my_fieldB = dpf.Field()
    >>> op.inputs.fieldB.connect(my_fieldB)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.global_to_nodal(
    ...     fieldA=my_fieldA,
    ...     fieldB=my_fieldB,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="GlobalToNodal", config=config, server=server)
        self._inputs = InputsGlobalToNodal(self)
        self._outputs = OutputsGlobalToNodal(self)
        if fieldA is not None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB is not None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Rotate results from global coordinate system to local coordinate system.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fieldA",
                    type_names=["field"],
                    optional=False,
                    document=r"""Vector or tensor field that must be rotated, expressed in global coordinate system.""",
                ),
                1: PinSpecification(
                    name="fieldB",
                    type_names=["field"],
                    optional=False,
                    document=r"""Nodal euler angles defined from a result file. Those  must be the rotations from Nodal to Global.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document=r"""Rotated field""",
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
        return Operator.default_config(name="GlobalToNodal", server=server)

    @property
    def inputs(self) -> InputsGlobalToNodal:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsGlobalToNodal.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsGlobalToNodal:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsGlobalToNodal.
        """
        return super().outputs


class InputsGlobalToNodal(_Inputs):
    """Intermediate class used to connect user inputs to
    global_to_nodal operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.global_to_nodal()
    >>> my_fieldA = dpf.Field()
    >>> op.inputs.fieldA.connect(my_fieldA)
    >>> my_fieldB = dpf.Field()
    >>> op.inputs.fieldB.connect(my_fieldB)
    """

    def __init__(self, op: Operator):
        super().__init__(global_to_nodal._spec().inputs, op)
        self._fieldA = Input(global_to_nodal._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fieldA)
        self._fieldB = Input(global_to_nodal._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._fieldB)

    @property
    def fieldA(self) -> Input:
        r"""Allows to connect fieldA input to the operator.

        Vector or tensor field that must be rotated, expressed in global coordinate system.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.global_to_nodal()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> # or
        >>> op.inputs.fieldA(my_fieldA)
        """
        return self._fieldA

    @property
    def fieldB(self) -> Input:
        r"""Allows to connect fieldB input to the operator.

        Nodal euler angles defined from a result file. Those  must be the rotations from Nodal to Global.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.global_to_nodal()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> # or
        >>> op.inputs.fieldB(my_fieldB)
        """
        return self._fieldB


class OutputsGlobalToNodal(_Outputs):
    """Intermediate class used to get outputs from
    global_to_nodal operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.global_to_nodal()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(global_to_nodal._spec().outputs, op)
        self._field = Output(global_to_nodal._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self) -> Output:
        r"""Allows to get field output of the operator

        Rotated field

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.global_to_nodal()
        >>> # Get the output from op.outputs. ...
        >>> result_field = op.outputs.field()
        """
        return self._field
