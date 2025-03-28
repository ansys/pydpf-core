"""
hdf5dpf_custom_read

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


class hdf5dpf_custom_read(Operator):
    r"""Extract a custom result from an hdf5dpf file. This operator is
    deprecated, please use the ‘custom’ operator instead.


    Parameters
    ----------
    time_scoping: Scoping, optional
    mesh_scoping: Scoping, optional
    streams: StreamsContainer, optional
        Hdf5df file stream.
    data_sources: DataSources, optional
        Hdf5df file data source.
    meta_data: DataTree, optional
        meta_data that may be used to evaluate results or extract workflows.
    result_name:
        Name of the result that must be extracted from the hdf5dpf file

    Returns
    -------
    field_or_fields_container: FieldsContainer or Field

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.hdf5dpf_custom_read()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_streams = dpf.StreamsContainer()
    >>> op.inputs.streams.connect(my_streams)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_meta_data = dpf.DataTree()
    >>> op.inputs.meta_data.connect(my_meta_data)
    >>> my_result_name = dpf.()
    >>> op.inputs.result_name.connect(my_result_name)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.hdf5dpf_custom_read(
    ...     time_scoping=my_time_scoping,
    ...     mesh_scoping=my_mesh_scoping,
    ...     streams=my_streams,
    ...     data_sources=my_data_sources,
    ...     meta_data=my_meta_data,
    ...     result_name=my_result_name,
    ... )

    >>> # Get output data
    >>> result_field_or_fields_container = op.outputs.field_or_fields_container()
    """

    def __init__(
        self,
        time_scoping=None,
        mesh_scoping=None,
        streams=None,
        data_sources=None,
        meta_data=None,
        result_name=None,
        config=None,
        server=None,
    ):
        super().__init__(name="hdf5::h5dpf::custom", config=config, server=server)
        self._inputs = InputsHdf5DpfCustomRead(self)
        self._outputs = OutputsHdf5DpfCustomRead(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if streams is not None:
            self.inputs.streams.connect(streams)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if meta_data is not None:
            self.inputs.meta_data.connect(meta_data)
        if result_name is not None:
            self.inputs.result_name.connect(result_name)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Extract a custom result from an hdf5dpf file. This operator is
deprecated, please use the ‘custom’ operator instead.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document=r"""""",
                ),
                3: PinSpecification(
                    name="streams",
                    type_names=["streams_container"],
                    optional=True,
                    document=r"""Hdf5df file stream.""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=True,
                    document=r"""Hdf5df file data source.""",
                ),
                24: PinSpecification(
                    name="meta_data",
                    type_names=["abstract_data_tree"],
                    optional=True,
                    document=r"""meta_data that may be used to evaluate results or extract workflows.""",
                ),
                60: PinSpecification(
                    name="result_name",
                    type_names=["any"],
                    optional=False,
                    document=r"""Name of the result that must be extracted from the hdf5dpf file""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field_or_fields_container",
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
        return Operator.default_config(name="hdf5::h5dpf::custom", server=server)

    @property
    def inputs(self) -> InputsHdf5DpfCustomRead:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsHdf5DpfCustomRead.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsHdf5DpfCustomRead:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsHdf5DpfCustomRead.
        """
        return super().outputs


class InputsHdf5DpfCustomRead(_Inputs):
    """Intermediate class used to connect user inputs to
    hdf5dpf_custom_read operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.hdf5dpf_custom_read()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_streams = dpf.StreamsContainer()
    >>> op.inputs.streams.connect(my_streams)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_meta_data = dpf.DataTree()
    >>> op.inputs.meta_data.connect(my_meta_data)
    >>> my_result_name = dpf.()
    >>> op.inputs.result_name.connect(my_result_name)
    """

    def __init__(self, op: Operator):
        super().__init__(hdf5dpf_custom_read._spec().inputs, op)
        self._time_scoping = Input(hdf5dpf_custom_read._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(hdf5dpf_custom_read._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._streams = Input(hdf5dpf_custom_read._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._streams)
        self._data_sources = Input(hdf5dpf_custom_read._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)
        self._meta_data = Input(hdf5dpf_custom_read._spec().input_pin(24), 24, op, -1)
        self._inputs.append(self._meta_data)
        self._result_name = Input(hdf5dpf_custom_read._spec().input_pin(60), 60, op, -1)
        self._inputs.append(self._result_name)

    @property
    def time_scoping(self) -> Input:
        r"""Allows to connect time_scoping input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_custom_read()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

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
        >>> op = dpf.operators.serialization.hdf5dpf_custom_read()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def streams(self) -> Input:
        r"""Allows to connect streams input to the operator.

        Hdf5df file stream.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_custom_read()
        >>> op.inputs.streams.connect(my_streams)
        >>> # or
        >>> op.inputs.streams(my_streams)
        """
        return self._streams

    @property
    def data_sources(self) -> Input:
        r"""Allows to connect data_sources input to the operator.

        Hdf5df file data source.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_custom_read()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def meta_data(self) -> Input:
        r"""Allows to connect meta_data input to the operator.

        meta_data that may be used to evaluate results or extract workflows.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_custom_read()
        >>> op.inputs.meta_data.connect(my_meta_data)
        >>> # or
        >>> op.inputs.meta_data(my_meta_data)
        """
        return self._meta_data

    @property
    def result_name(self) -> Input:
        r"""Allows to connect result_name input to the operator.

        Name of the result that must be extracted from the hdf5dpf file

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_custom_read()
        >>> op.inputs.result_name.connect(my_result_name)
        >>> # or
        >>> op.inputs.result_name(my_result_name)
        """
        return self._result_name


class OutputsHdf5DpfCustomRead(_Outputs):
    """Intermediate class used to get outputs from
    hdf5dpf_custom_read operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.hdf5dpf_custom_read()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field_or_fields_container = op.outputs.field_or_fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(hdf5dpf_custom_read._spec().outputs, op)
        self.field_or_fields_container_as_fields_container = Output(
            _modify_output_spec_with_one_type(
                hdf5dpf_custom_read._spec().output_pin(0), "fields_container"
            ),
            0,
            op,
        )
        self._outputs.append(self.field_or_fields_container_as_fields_container)
        self.field_or_fields_container_as_field = Output(
            _modify_output_spec_with_one_type(
                hdf5dpf_custom_read._spec().output_pin(0), "field"
            ),
            0,
            op,
        )
        self._outputs.append(self.field_or_fields_container_as_field)
