"""
csv_to_field

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


class csv_to_field(Operator):
    r"""transform csv file to a field or fields container


    Parameters
    ----------
    time_scoping: Scoping, optional
    data_sources: DataSources
        data sources containing a file with csv extension

    Returns
    -------
    fields_container: FieldsContainer

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.csv_to_field()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.csv_to_field(
    ...     time_scoping=my_time_scoping,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, time_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="csv_to_field", config=config, server=server)
        self._inputs = InputsCsvToField(self)
        self._outputs = OutputsCsvToField(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec() -> Specification:
        description = r"""transform csv file to a field or fields container
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
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document=r"""data sources containing a file with csv extension""",
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
        return Operator.default_config(name="csv_to_field", server=server)

    @property
    def inputs(self) -> InputsCsvToField:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsCsvToField.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsCsvToField:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsCsvToField.
        """
        return super().outputs


class InputsCsvToField(_Inputs):
    """Intermediate class used to connect user inputs to
    csv_to_field operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.csv_to_field()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(csv_to_field._spec().inputs, op)
        self._time_scoping = Input(csv_to_field._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._time_scoping)
        self._data_sources = Input(csv_to_field._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)

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
        >>> op = dpf.operators.serialization.csv_to_field()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def data_sources(self) -> Input:
        r"""Allows to connect data_sources input to the operator.

        data sources containing a file with csv extension

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.csv_to_field()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsCsvToField(_Outputs):
    """Intermediate class used to get outputs from
    csv_to_field operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.csv_to_field()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(csv_to_field._spec().outputs, op)
        self._fields_container = Output(csv_to_field._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.serialization.csv_to_field()
        >>> # Get the output from op.outputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """
        return self._fields_container
