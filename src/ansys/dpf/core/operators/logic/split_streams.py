"""
split_streams

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


class split_streams(Operator):
    r"""Splits a Streams into multiple coherent streams, actual number of
    outputs is always less or equal to the given desired number of ouputs.


    Parameters
    ----------
    streams: StreamsContainer
        Streams to split.
    output_count: int
        Number of desired outputs.

    Returns
    -------
    output_count: int
        Actual number of outputs.
    outputs1: StreamsContainer
        Streams outputs.
    outputs2: StreamsContainer
        Streams outputs.

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.logic.split_streams()

    >>> # Make input connections
    >>> my_streams = dpf.StreamsContainer()
    >>> op.inputs.streams.connect(my_streams)
    >>> my_output_count = int()
    >>> op.inputs.output_count.connect(my_output_count)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.logic.split_streams(
    ...     streams=my_streams,
    ...     output_count=my_output_count,
    ... )

    >>> # Get output data
    >>> result_output_count = op.outputs.output_count()
    >>> result_outputs1 = op.outputs.outputs1()
    >>> result_outputs2 = op.outputs.outputs2()
    """

    def __init__(self, streams=None, output_count=None, config=None, server=None):
        super().__init__(name="splitter::streams", config=config, server=server)
        self._inputs = InputsSplitStreams(self)
        self._outputs = OutputsSplitStreams(self)
        if streams is not None:
            self.inputs.streams.connect(streams)
        if output_count is not None:
            self.inputs.output_count.connect(output_count)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Splits a Streams into multiple coherent streams, actual number of
outputs is always less or equal to the given desired number of ouputs.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="streams",
                    type_names=["streams_container"],
                    optional=False,
                    document=r"""Streams to split.""",
                ),
                1: PinSpecification(
                    name="output_count",
                    type_names=["int32"],
                    optional=False,
                    document=r"""Number of desired outputs.""",
                ),
            },
            map_output_pin_spec={
                -1: PinSpecification(
                    name="output_count",
                    type_names=["int32"],
                    optional=False,
                    document=r"""Actual number of outputs.""",
                ),
                0: PinSpecification(
                    name="outputs1",
                    type_names=["streams_container"],
                    optional=False,
                    document=r"""Streams outputs.""",
                ),
                1: PinSpecification(
                    name="outputs2",
                    type_names=["streams_container"],
                    optional=False,
                    document=r"""Streams outputs.""",
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
        return Operator.default_config(name="splitter::streams", server=server)

    @property
    def inputs(self) -> InputsSplitStreams:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsSplitStreams.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsSplitStreams:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsSplitStreams.
        """
        return super().outputs


class InputsSplitStreams(_Inputs):
    """Intermediate class used to connect user inputs to
    split_streams operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.split_streams()
    >>> my_streams = dpf.StreamsContainer()
    >>> op.inputs.streams.connect(my_streams)
    >>> my_output_count = int()
    >>> op.inputs.output_count.connect(my_output_count)
    """

    def __init__(self, op: Operator):
        super().__init__(split_streams._spec().inputs, op)
        self._streams = Input(split_streams._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._streams)
        self._output_count = Input(split_streams._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._output_count)

    @property
    def streams(self) -> Input:
        r"""Allows to connect streams input to the operator.

        Streams to split.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.split_streams()
        >>> op.inputs.streams.connect(my_streams)
        >>> # or
        >>> op.inputs.streams(my_streams)
        """
        return self._streams

    @property
    def output_count(self) -> Input:
        r"""Allows to connect output_count input to the operator.

        Number of desired outputs.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.split_streams()
        >>> op.inputs.output_count.connect(my_output_count)
        >>> # or
        >>> op.inputs.output_count(my_output_count)
        """
        return self._output_count


class OutputsSplitStreams(_Outputs):
    """Intermediate class used to get outputs from
    split_streams operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.split_streams()
    >>> # Connect inputs : op.inputs. ...
    >>> result_output_count = op.outputs.output_count()
    >>> result_outputs1 = op.outputs.outputs1()
    >>> result_outputs2 = op.outputs.outputs2()
    """

    def __init__(self, op: Operator):
        super().__init__(split_streams._spec().outputs, op)
        self._output_count = Output(split_streams._spec().output_pin(-1), -1, op)
        self._outputs.append(self._output_count)
        self._outputs1 = Output(split_streams._spec().output_pin(0), 0, op)
        self._outputs.append(self._outputs1)
        self._outputs2 = Output(split_streams._spec().output_pin(1), 1, op)
        self._outputs.append(self._outputs2)

    @property
    def output_count(self) -> Output:
        r"""Allows to get output_count output of the operator

        Actual number of outputs.

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.split_streams()
        >>> # Get the output from op.outputs. ...
        >>> result_output_count = op.outputs.output_count()
        """
        return self._output_count

    @property
    def outputs1(self) -> Output:
        r"""Allows to get outputs1 output of the operator

        Streams outputs.

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.split_streams()
        >>> # Get the output from op.outputs. ...
        >>> result_outputs1 = op.outputs.outputs1()
        """
        return self._outputs1

    @property
    def outputs2(self) -> Output:
        r"""Allows to get outputs2 output of the operator

        Streams outputs.

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.split_streams()
        >>> # Get the output from op.outputs. ...
        >>> result_outputs2 = op.outputs.outputs2()
        """
        return self._outputs2
