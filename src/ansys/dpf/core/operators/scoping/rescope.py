"""
rescope

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


class rescope(Operator):
    r"""Rescopes a field on the given scoping. If an ID does not exist in the
    original field, the default value (in 2) is used when defined.


    Parameters
    ----------
    fields: FieldsContainer or Field
    mesh_scoping: Scoping, optional
    default_value: float, optional
        If pin 2 is used, the IDs not found in the field are added with this default value.

    Returns
    -------
    fields: FieldsContainer or Field

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.scoping.rescope()

    >>> # Make input connections
    >>> my_fields = dpf.FieldsContainer()
    >>> op.inputs.fields.connect(my_fields)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_default_value = float()
    >>> op.inputs.default_value.connect(my_default_value)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.scoping.rescope(
    ...     fields=my_fields,
    ...     mesh_scoping=my_mesh_scoping,
    ...     default_value=my_default_value,
    ... )

    >>> # Get output data
    >>> result_fields = op.outputs.fields()
    """

    def __init__(
        self,
        fields=None,
        mesh_scoping=None,
        default_value=None,
        config=None,
        server=None,
    ):
        super().__init__(name="Rescope", config=config, server=server)
        self._inputs = InputsRescope(self)
        self._outputs = OutputsRescope(self)
        if fields is not None:
            self.inputs.fields.connect(fields)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if default_value is not None:
            self.inputs.default_value.connect(default_value)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Rescopes a field on the given scoping. If an ID does not exist in the
original field, the default value (in 2) is used when defined.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields",
                    type_names=["fields_container", "field"],
                    optional=False,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping", "vector<int32>"],
                    optional=True,
                    document=r"""""",
                ),
                2: PinSpecification(
                    name="default_value",
                    type_names=["double", "vector<double>"],
                    optional=True,
                    document=r"""If pin 2 is used, the IDs not found in the field are added with this default value.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields",
                    type_names=["fields_container", "field"],
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
        return Operator.default_config(name="Rescope", server=server)

    @property
    def inputs(self) -> InputsRescope:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsRescope.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsRescope:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsRescope.
        """
        return super().outputs


class InputsRescope(_Inputs):
    """Intermediate class used to connect user inputs to
    rescope operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.rescope()
    >>> my_fields = dpf.FieldsContainer()
    >>> op.inputs.fields.connect(my_fields)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_default_value = float()
    >>> op.inputs.default_value.connect(my_default_value)
    """

    def __init__(self, op: Operator):
        super().__init__(rescope._spec().inputs, op)
        self._fields = Input(rescope._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fields)
        self._mesh_scoping = Input(rescope._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._default_value = Input(rescope._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._default_value)

    @property
    def fields(self) -> Input:
        r"""Allows to connect fields input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.rescope()
        >>> op.inputs.fields.connect(my_fields)
        >>> # or
        >>> op.inputs.fields(my_fields)
        """
        return self._fields

    @property
    def mesh_scoping(self) -> Input:
        r"""Allows to connect mesh_scoping input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.rescope()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def default_value(self) -> Input:
        r"""Allows to connect default_value input to the operator.

        If pin 2 is used, the IDs not found in the field are added with this default value.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.rescope()
        >>> op.inputs.default_value.connect(my_default_value)
        >>> # or
        >>> op.inputs.default_value(my_default_value)
        """
        return self._default_value


class OutputsRescope(_Outputs):
    """Intermediate class used to get outputs from
    rescope operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.rescope()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields = op.outputs.fields()
    """

    def __init__(self, op: Operator):
        super().__init__(rescope._spec().outputs, op)
        self.fields_as_fields_container = Output(
            _modify_output_spec_with_one_type(
                rescope._spec().output_pin(0), "fields_container"
            ),
            0,
            op,
        )
        self._outputs.append(self.fields_as_fields_container)
        self.fields_as_field = Output(
            _modify_output_spec_with_one_type(rescope._spec().output_pin(0), "field"),
            0,
            op,
        )
        self._outputs.append(self.fields_as_field)
