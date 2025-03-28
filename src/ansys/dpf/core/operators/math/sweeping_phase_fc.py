"""
sweeping_phase_fc

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


class sweeping_phase_fc(Operator):
    r"""Shifts the phase of all the corresponding real and imaginary fields of a
    fields container for a given angle (in 2) of a unit (in 4).


    Parameters
    ----------
    fields_container: FieldsContainer
    angle: float
    unit_name: str, optional
        String Unit. Supported values: "deg" or "rad". Default: "rad".
    abs_value: bool

    Returns
    -------
    fields_container: FieldsContainer

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.sweeping_phase_fc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_angle = float()
    >>> op.inputs.angle.connect(my_angle)
    >>> my_unit_name = str()
    >>> op.inputs.unit_name.connect(my_unit_name)
    >>> my_abs_value = bool()
    >>> op.inputs.abs_value.connect(my_abs_value)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.sweeping_phase_fc(
    ...     fields_container=my_fields_container,
    ...     angle=my_angle,
    ...     unit_name=my_unit_name,
    ...     abs_value=my_abs_value,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_container=None,
        angle=None,
        unit_name=None,
        abs_value=None,
        config=None,
        server=None,
    ):
        super().__init__(name="sweeping_phase_fc", config=config, server=server)
        self._inputs = InputsSweepingPhaseFc(self)
        self._outputs = OutputsSweepingPhaseFc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if angle is not None:
            self.inputs.angle.connect(angle)
        if unit_name is not None:
            self.inputs.unit_name.connect(unit_name)
        if abs_value is not None:
            self.inputs.abs_value.connect(abs_value)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Shifts the phase of all the corresponding real and imaginary fields of a
fields container for a given angle (in 2) of a unit (in 4).
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document=r"""""",
                ),
                2: PinSpecification(
                    name="angle",
                    type_names=["double"],
                    optional=False,
                    document=r"""""",
                ),
                3: PinSpecification(
                    name="unit_name",
                    type_names=["string"],
                    optional=True,
                    document=r"""String Unit. Supported values: "deg" or "rad". Default: "rad".""",
                ),
                4: PinSpecification(
                    name="abs_value",
                    type_names=["bool"],
                    optional=False,
                    document=r"""""",
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
        return Operator.default_config(name="sweeping_phase_fc", server=server)

    @property
    def inputs(self) -> InputsSweepingPhaseFc:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsSweepingPhaseFc.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsSweepingPhaseFc:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsSweepingPhaseFc.
        """
        return super().outputs


class InputsSweepingPhaseFc(_Inputs):
    """Intermediate class used to connect user inputs to
    sweeping_phase_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.sweeping_phase_fc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_angle = float()
    >>> op.inputs.angle.connect(my_angle)
    >>> my_unit_name = str()
    >>> op.inputs.unit_name.connect(my_unit_name)
    >>> my_abs_value = bool()
    >>> op.inputs.abs_value.connect(my_abs_value)
    """

    def __init__(self, op: Operator):
        super().__init__(sweeping_phase_fc._spec().inputs, op)
        self._fields_container = Input(
            sweeping_phase_fc._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._angle = Input(sweeping_phase_fc._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._angle)
        self._unit_name = Input(sweeping_phase_fc._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._unit_name)
        self._abs_value = Input(sweeping_phase_fc._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._abs_value)

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
        >>> op = dpf.operators.math.sweeping_phase_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def angle(self) -> Input:
        r"""Allows to connect angle input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.sweeping_phase_fc()
        >>> op.inputs.angle.connect(my_angle)
        >>> # or
        >>> op.inputs.angle(my_angle)
        """
        return self._angle

    @property
    def unit_name(self) -> Input:
        r"""Allows to connect unit_name input to the operator.

        String Unit. Supported values: "deg" or "rad". Default: "rad".

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.sweeping_phase_fc()
        >>> op.inputs.unit_name.connect(my_unit_name)
        >>> # or
        >>> op.inputs.unit_name(my_unit_name)
        """
        return self._unit_name

    @property
    def abs_value(self) -> Input:
        r"""Allows to connect abs_value input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.sweeping_phase_fc()
        >>> op.inputs.abs_value.connect(my_abs_value)
        >>> # or
        >>> op.inputs.abs_value(my_abs_value)
        """
        return self._abs_value


class OutputsSweepingPhaseFc(_Outputs):
    """Intermediate class used to get outputs from
    sweeping_phase_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.sweeping_phase_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(sweeping_phase_fc._spec().outputs, op)
        self._fields_container = Output(sweeping_phase_fc._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.sweeping_phase_fc()
        >>> # Get the output from op.outputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """
        return self._fields_container
