"""
rescope_fc

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


class rescope_fc(Operator):
    r"""Rescopes a field on the given scoping. If an ID does not exist in the
    original field, the default value (in 2) is used when defined.


    Parameters
    ----------
    fields_container: FieldsContainer
    mesh_scoping: Scoping, optional
    default_value: float, optional
        If pin 2 is used, the IDs not found in the field are added with this default value.

    Returns
    -------
    fields_container: FieldsContainer

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.scoping.rescope_fc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_default_value = float()
    >>> op.inputs.default_value.connect(my_default_value)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.scoping.rescope_fc(
    ...     fields_container=my_fields_container,
    ...     mesh_scoping=my_mesh_scoping,
    ...     default_value=my_default_value,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_container=None,
        mesh_scoping=None,
        default_value=None,
        config=None,
        server=None,
    ):
        super().__init__(name="Rescope_fc", config=config, server=server)
        self._inputs = InputsRescopeFc(self)
        self._outputs = OutputsRescopeFc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
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
                    name="fields_container",
                    type_names=["fields_container"],
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
        return Operator.default_config(name="Rescope_fc", server=server)

    @property
    def inputs(self) -> InputsRescopeFc:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsRescopeFc.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsRescopeFc:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsRescopeFc.
        """
        return super().outputs


class InputsRescopeFc(_Inputs):
    """Intermediate class used to connect user inputs to
    rescope_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.rescope_fc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_default_value = float()
    >>> op.inputs.default_value.connect(my_default_value)
    """

    def __init__(self, op: Operator):
        super().__init__(rescope_fc._spec().inputs, op)
        self._fields_container = Input(rescope_fc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fields_container)
        self._mesh_scoping = Input(rescope_fc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._default_value = Input(rescope_fc._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._default_value)

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
        >>> op = dpf.operators.scoping.rescope_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

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
        >>> op = dpf.operators.scoping.rescope_fc()
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
        >>> op = dpf.operators.scoping.rescope_fc()
        >>> op.inputs.default_value.connect(my_default_value)
        >>> # or
        >>> op.inputs.default_value(my_default_value)
        """
        return self._default_value


class OutputsRescopeFc(_Outputs):
    """Intermediate class used to get outputs from
    rescope_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.rescope_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(rescope_fc._spec().outputs, op)
        self._fields_container = Output(rescope_fc._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.scoping.rescope_fc()
        >>> # Get the output from op.outputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """
        return self._fields_container
