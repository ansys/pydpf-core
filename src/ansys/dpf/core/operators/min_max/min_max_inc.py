"""
min_max_inc

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


class min_max_inc(Operator):
    r"""Compute the component-wise minimum (out 0) and maximum (out 1) over
    coming fields.


    Parameters
    ----------
    field: Field
    domain_id: int, optional

    Returns
    -------
    field_min: Field
    field_max: Field
    domain_ids_min: Scoping
    domain_ids_max: Scoping

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.min_max.min_max_inc()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_domain_id = int()
    >>> op.inputs.domain_id.connect(my_domain_id)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.min_max.min_max_inc(
    ...     field=my_field,
    ...     domain_id=my_domain_id,
    ... )

    >>> # Get output data
    >>> result_field_min = op.outputs.field_min()
    >>> result_field_max = op.outputs.field_max()
    >>> result_domain_ids_min = op.outputs.domain_ids_min()
    >>> result_domain_ids_max = op.outputs.domain_ids_max()
    """

    def __init__(self, field=None, domain_id=None, config=None, server=None):
        super().__init__(name="min_max_inc", config=config, server=server)
        self._inputs = InputsMinMaxInc(self)
        self._outputs = OutputsMinMaxInc(self)
        if field is not None:
            self.inputs.field.connect(field)
        if domain_id is not None:
            self.inputs.domain_id.connect(domain_id)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Compute the component-wise minimum (out 0) and maximum (out 1) over
coming fields.
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
                17: PinSpecification(
                    name="domain_id",
                    type_names=["int32"],
                    optional=True,
                    document=r"""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field_min",
                    type_names=["field"],
                    optional=False,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="field_max",
                    type_names=["field"],
                    optional=False,
                    document=r"""""",
                ),
                2: PinSpecification(
                    name="domain_ids_min",
                    type_names=["scoping"],
                    optional=False,
                    document=r"""""",
                ),
                3: PinSpecification(
                    name="domain_ids_max",
                    type_names=["scoping"],
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
        return Operator.default_config(name="min_max_inc", server=server)

    @property
    def inputs(self) -> InputsMinMaxInc:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsMinMaxInc.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsMinMaxInc:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsMinMaxInc.
        """
        return super().outputs


class InputsMinMaxInc(_Inputs):
    """Intermediate class used to connect user inputs to
    min_max_inc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.min_max.min_max_inc()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_domain_id = int()
    >>> op.inputs.domain_id.connect(my_domain_id)
    """

    def __init__(self, op: Operator):
        super().__init__(min_max_inc._spec().inputs, op)
        self._field = Input(min_max_inc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._domain_id = Input(min_max_inc._spec().input_pin(17), 17, op, -1)
        self._inputs.append(self._domain_id)

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
        >>> op = dpf.operators.min_max.min_max_inc()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def domain_id(self) -> Input:
        r"""Allows to connect domain_id input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_max_inc()
        >>> op.inputs.domain_id.connect(my_domain_id)
        >>> # or
        >>> op.inputs.domain_id(my_domain_id)
        """
        return self._domain_id


class OutputsMinMaxInc(_Outputs):
    """Intermediate class used to get outputs from
    min_max_inc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.min_max.min_max_inc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field_min = op.outputs.field_min()
    >>> result_field_max = op.outputs.field_max()
    >>> result_domain_ids_min = op.outputs.domain_ids_min()
    >>> result_domain_ids_max = op.outputs.domain_ids_max()
    """

    def __init__(self, op: Operator):
        super().__init__(min_max_inc._spec().outputs, op)
        self._field_min = Output(min_max_inc._spec().output_pin(0), 0, op)
        self._outputs.append(self._field_min)
        self._field_max = Output(min_max_inc._spec().output_pin(1), 1, op)
        self._outputs.append(self._field_max)
        self._domain_ids_min = Output(min_max_inc._spec().output_pin(2), 2, op)
        self._outputs.append(self._domain_ids_min)
        self._domain_ids_max = Output(min_max_inc._spec().output_pin(3), 3, op)
        self._outputs.append(self._domain_ids_max)

    @property
    def field_min(self) -> Output:
        r"""Allows to get field_min output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_max_inc()
        >>> # Get the output from op.outputs. ...
        >>> result_field_min = op.outputs.field_min()
        """
        return self._field_min

    @property
    def field_max(self) -> Output:
        r"""Allows to get field_max output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_max_inc()
        >>> # Get the output from op.outputs. ...
        >>> result_field_max = op.outputs.field_max()
        """
        return self._field_max

    @property
    def domain_ids_min(self) -> Output:
        r"""Allows to get domain_ids_min output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_max_inc()
        >>> # Get the output from op.outputs. ...
        >>> result_domain_ids_min = op.outputs.domain_ids_min()
        """
        return self._domain_ids_min

    @property
    def domain_ids_max(self) -> Output:
        r"""Allows to get domain_ids_max output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_max_inc()
        >>> # Get the output from op.outputs. ...
        >>> result_domain_ids_max = op.outputs.domain_ids_max()
        """
        return self._domain_ids_max
