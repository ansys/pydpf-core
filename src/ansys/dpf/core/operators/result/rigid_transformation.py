"""
rigid_transformation

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


class rigid_transformation(Operator):
    r"""Extracts rigid body motions from a displacement in input.


    Parameters
    ----------
    streams_container: StreamsContainer, optional
        streams (result file container) (optional)
    data_sources: DataSources
        If the stream is null, retrieves the file path from the data sources.

    Returns
    -------
    fields_container: FieldsContainer

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.rigid_transformation()

    >>> # Make input connections
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.rigid_transformation(
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self, streams_container=None, data_sources=None, config=None, server=None
    ):
        super().__init__(
            name="rigid_transformation_provider", config=config, server=server
        )
        self._inputs = InputsRigidTransformation(self)
        self._outputs = OutputsRigidTransformation(self)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Extracts rigid body motions from a displacement in input.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=True,
                    document=r"""streams (result file container) (optional)""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document=r"""If the stream is null, retrieves the file path from the data sources.""",
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
        return Operator.default_config(
            name="rigid_transformation_provider", server=server
        )

    @property
    def inputs(self) -> InputsRigidTransformation:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsRigidTransformation.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsRigidTransformation:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsRigidTransformation.
        """
        return super().outputs


class InputsRigidTransformation(_Inputs):
    """Intermediate class used to connect user inputs to
    rigid_transformation operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.rigid_transformation()
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(rigid_transformation._spec().inputs, op)
        self._streams_container = Input(
            rigid_transformation._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(rigid_transformation._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)

    @property
    def streams_container(self) -> Input:
        r"""Allows to connect streams_container input to the operator.

        streams (result file container) (optional)

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.rigid_transformation()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self) -> Input:
        r"""Allows to connect data_sources input to the operator.

        If the stream is null, retrieves the file path from the data sources.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.rigid_transformation()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsRigidTransformation(_Outputs):
    """Intermediate class used to get outputs from
    rigid_transformation operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.rigid_transformation()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(rigid_transformation._spec().outputs, op)
        self._fields_container = Output(
            rigid_transformation._spec().output_pin(0), 0, op
        )
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
        >>> op = dpf.operators.result.rigid_transformation()
        >>> # Get the output from op.outputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """
        return self._fields_container
