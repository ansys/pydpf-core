"""
make_one_on_comp

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


class make_one_on_comp(Operator):
    r"""Takes the input field’s scoping and creates a field full of zeros,
    except for the indexes from pin 1 that will hold 1.0.


    Parameters
    ----------
    fieldA: Field
    scalar_int: int

    Returns
    -------
    field: Field

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.make_one_on_comp()

    >>> # Make input connections
    >>> my_fieldA = dpf.Field()
    >>> op.inputs.fieldA.connect(my_fieldA)
    >>> my_scalar_int = int()
    >>> op.inputs.scalar_int.connect(my_scalar_int)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.make_one_on_comp(
    ...     fieldA=my_fieldA,
    ...     scalar_int=my_scalar_int,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, fieldA=None, scalar_int=None, config=None, server=None):
        super().__init__(name="make_one_on_comp", config=config, server=server)
        self._inputs = InputsMakeOneOnComp(self)
        self._outputs = OutputsMakeOneOnComp(self)
        if fieldA is not None:
            self.inputs.fieldA.connect(fieldA)
        if scalar_int is not None:
            self.inputs.scalar_int.connect(scalar_int)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Takes the input field’s scoping and creates a field full of zeros,
except for the indexes from pin 1 that will hold 1.0.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fieldA",
                    type_names=["field"],
                    optional=False,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="scalar_int",
                    type_names=["int32"],
                    optional=False,
                    document=r"""""",
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
        return Operator.default_config(name="make_one_on_comp", server=server)

    @property
    def inputs(self) -> InputsMakeOneOnComp:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsMakeOneOnComp.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsMakeOneOnComp:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsMakeOneOnComp.
        """
        return super().outputs


class InputsMakeOneOnComp(_Inputs):
    """Intermediate class used to connect user inputs to
    make_one_on_comp operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.make_one_on_comp()
    >>> my_fieldA = dpf.Field()
    >>> op.inputs.fieldA.connect(my_fieldA)
    >>> my_scalar_int = int()
    >>> op.inputs.scalar_int.connect(my_scalar_int)
    """

    def __init__(self, op: Operator):
        super().__init__(make_one_on_comp._spec().inputs, op)
        self._fieldA = Input(make_one_on_comp._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fieldA)
        self._scalar_int = Input(make_one_on_comp._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._scalar_int)

    @property
    def fieldA(self) -> Input:
        r"""Allows to connect fieldA input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.make_one_on_comp()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> # or
        >>> op.inputs.fieldA(my_fieldA)
        """
        return self._fieldA

    @property
    def scalar_int(self) -> Input:
        r"""Allows to connect scalar_int input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.make_one_on_comp()
        >>> op.inputs.scalar_int.connect(my_scalar_int)
        >>> # or
        >>> op.inputs.scalar_int(my_scalar_int)
        """
        return self._scalar_int


class OutputsMakeOneOnComp(_Outputs):
    """Intermediate class used to get outputs from
    make_one_on_comp operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.make_one_on_comp()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(make_one_on_comp._spec().outputs, op)
        self._field = Output(make_one_on_comp._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.make_one_on_comp()
        >>> # Get the output from op.outputs. ...
        >>> result_field = op.outputs.field()
        """
        return self._field
