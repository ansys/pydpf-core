"""
fields_container_matrices_label

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


class fields_container_matrices_label(Operator):
    r"""Merge fields of fields container into field matrices. The output is a
    fields container of field matrices.


    Parameters
    ----------
    fields_container: FieldsContainer
        fields container to be merged
    label: str
        Label where the merge is required
    time_scoping: int or Scoping, optional
        if it's specified, fields container of field matrices is constructed only on the specified time scoping

    Returns
    -------
    fields_container: FieldsContainer
        fields container of field matrices obtained after merging.

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.fields_container_matrices_label()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_label = str()
    >>> op.inputs.label.connect(my_label)
    >>> my_time_scoping = int()
    >>> op.inputs.time_scoping.connect(my_time_scoping)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.fields_container_matrices_label(
    ...     fields_container=my_fields_container,
    ...     label=my_label,
    ...     time_scoping=my_time_scoping,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_container=None,
        label=None,
        time_scoping=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="merge::fields_container_matrices_label", config=config, server=server
        )
        self._inputs = InputsFieldsContainerMatricesLabel(self)
        self._outputs = OutputsFieldsContainerMatricesLabel(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if label is not None:
            self.inputs.label.connect(label)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Merge fields of fields container into field matrices. The output is a
fields container of field matrices.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document=r"""fields container to be merged""",
                ),
                1: PinSpecification(
                    name="label",
                    type_names=["string"],
                    optional=False,
                    document=r"""Label where the merge is required""",
                ),
                2: PinSpecification(
                    name="time_scoping",
                    type_names=["int32", "vector<int32>", "scoping"],
                    optional=True,
                    document=r"""if it's specified, fields container of field matrices is constructed only on the specified time scoping""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document=r"""fields container of field matrices obtained after merging.""",
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
            name="merge::fields_container_matrices_label", server=server
        )

    @property
    def inputs(self) -> InputsFieldsContainerMatricesLabel:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsFieldsContainerMatricesLabel.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsFieldsContainerMatricesLabel:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsFieldsContainerMatricesLabel.
        """
        return super().outputs


class InputsFieldsContainerMatricesLabel(_Inputs):
    """Intermediate class used to connect user inputs to
    fields_container_matrices_label operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.fields_container_matrices_label()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_label = str()
    >>> op.inputs.label.connect(my_label)
    >>> my_time_scoping = int()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    """

    def __init__(self, op: Operator):
        super().__init__(fields_container_matrices_label._spec().inputs, op)
        self._fields_container = Input(
            fields_container_matrices_label._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._label = Input(
            fields_container_matrices_label._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._label)
        self._time_scoping = Input(
            fields_container_matrices_label._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._time_scoping)

    @property
    def fields_container(self) -> Input:
        r"""Allows to connect fields_container input to the operator.

        fields container to be merged

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.fields_container_matrices_label()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def label(self) -> Input:
        r"""Allows to connect label input to the operator.

        Label where the merge is required

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.fields_container_matrices_label()
        >>> op.inputs.label.connect(my_label)
        >>> # or
        >>> op.inputs.label(my_label)
        """
        return self._label

    @property
    def time_scoping(self) -> Input:
        r"""Allows to connect time_scoping input to the operator.

        if it's specified, fields container of field matrices is constructed only on the specified time scoping

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.fields_container_matrices_label()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping


class OutputsFieldsContainerMatricesLabel(_Outputs):
    """Intermediate class used to get outputs from
    fields_container_matrices_label operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.fields_container_matrices_label()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(fields_container_matrices_label._spec().outputs, op)
        self._fields_container = Output(
            fields_container_matrices_label._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self) -> Output:
        r"""Allows to get fields_container output of the operator

        fields container of field matrices obtained after merging.

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.fields_container_matrices_label()
        >>> # Get the output from op.outputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """
        return self._fields_container
