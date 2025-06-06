"""
mass_flow_rate

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


class mass_flow_rate(Operator):
    r"""Read Mass Flow Rate by calling the readers defined by the datasources.


    Parameters
    ----------
    time_scoping: Scoping or int or float or Field, optional
        time/freq values (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) required in output. To specify time/freq values at specific load steps, put a Field (and not a list) in input with a scoping located on "TimeFreq_steps". Linear time freq intrapolation is performed if the values are not in the result files and the data at the max time or freq is taken when time/freqs are higher than available time/freqs in result files. To get all data for all time/freq sets, connect an int with value -1.
    mesh_scoping: ScopingsContainer or Scoping, optional
        nodes or elements scoping required in output. The output fields will be scoped on these node or element IDs. To figure out the ordering of the fields data, look at their scoping IDs as they might not be ordered as the input scoping was. The scoping's location indicates whether nodes or elements are asked for. Using scopings container allows you to split the result fields container into domains
    streams_container: StreamsContainer, optional
        result file container allowed to be kept open to cache data
    data_sources: DataSources
        result file path container, used if no streams are set
    mesh: MeshedRegion or MeshesContainer, optional
        prevents from reading the mesh in the result files
    region_scoping: Scoping or int, optional
        region id (integer) or vector of region ids (vector) or region scoping (scoping) of the model (region corresponds to zone for Fluid results or part for LSDyna results).
    qualifiers1: dict, optional
        (for Fluid results only) LabelSpace with combination of zone, phases or species ids
    qualifiers2: dict, optional
        (for Fluid results only) LabelSpace with combination of zone, phases or species ids

    Returns
    -------
    fields_container: FieldsContainer

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.mass_flow_rate()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_region_scoping = dpf.Scoping()
    >>> op.inputs.region_scoping.connect(my_region_scoping)
    >>> my_qualifiers1 = dict()
    >>> op.inputs.qualifiers1.connect(my_qualifiers1)
    >>> my_qualifiers2 = dict()
    >>> op.inputs.qualifiers2.connect(my_qualifiers2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.mass_flow_rate(
    ...     time_scoping=my_time_scoping,
    ...     mesh_scoping=my_mesh_scoping,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     mesh=my_mesh,
    ...     region_scoping=my_region_scoping,
    ...     qualifiers1=my_qualifiers1,
    ...     qualifiers2=my_qualifiers2,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        time_scoping=None,
        mesh_scoping=None,
        streams_container=None,
        data_sources=None,
        mesh=None,
        region_scoping=None,
        qualifiers1=None,
        qualifiers2=None,
        config=None,
        server=None,
    ):
        super().__init__(name="MDOT", config=config, server=server)
        self._inputs = InputsMassFlowRate(self)
        self._outputs = OutputsMassFlowRate(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if region_scoping is not None:
            self.inputs.region_scoping.connect(region_scoping)
        if qualifiers1 is not None:
            self.inputs.qualifiers1.connect(qualifiers1)
        if qualifiers2 is not None:
            self.inputs.qualifiers2.connect(qualifiers2)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Read Mass Flow Rate by calling the readers defined by the datasources.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_scoping",
                    type_names=[
                        "scoping",
                        "int32",
                        "vector<int32>",
                        "double",
                        "field",
                        "vector<double>",
                    ],
                    optional=True,
                    document=r"""time/freq values (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) required in output. To specify time/freq values at specific load steps, put a Field (and not a list) in input with a scoping located on "TimeFreq_steps". Linear time freq intrapolation is performed if the values are not in the result files and the data at the max time or freq is taken when time/freqs are higher than available time/freqs in result files. To get all data for all time/freq sets, connect an int with value -1.""",
                ),
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scopings_container", "scoping"],
                    optional=True,
                    document=r"""nodes or elements scoping required in output. The output fields will be scoped on these node or element IDs. To figure out the ordering of the fields data, look at their scoping IDs as they might not be ordered as the input scoping was. The scoping's location indicates whether nodes or elements are asked for. Using scopings container allows you to split the result fields container into domains""",
                ),
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=True,
                    document=r"""result file container allowed to be kept open to cache data""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document=r"""result file path container, used if no streams are set""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document=r"""prevents from reading the mesh in the result files""",
                ),
                25: PinSpecification(
                    name="region_scoping",
                    type_names=["scoping", "int32", "vector<int32>"],
                    optional=True,
                    document=r"""region id (integer) or vector of region ids (vector) or region scoping (scoping) of the model (region corresponds to zone for Fluid results or part for LSDyna results).""",
                ),
                1000: PinSpecification(
                    name="qualifiers",
                    type_names=["label_space"],
                    optional=True,
                    document=r"""(for Fluid results only) LabelSpace with combination of zone, phases or species ids""",
                ),
                1001: PinSpecification(
                    name="qualifiers",
                    type_names=["label_space"],
                    optional=True,
                    document=r"""(for Fluid results only) LabelSpace with combination of zone, phases or species ids""",
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
        return Operator.default_config(name="MDOT", server=server)

    @property
    def inputs(self) -> InputsMassFlowRate:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsMassFlowRate.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsMassFlowRate:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsMassFlowRate.
        """
        return super().outputs


class InputsMassFlowRate(_Inputs):
    """Intermediate class used to connect user inputs to
    mass_flow_rate operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.mass_flow_rate()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_region_scoping = dpf.Scoping()
    >>> op.inputs.region_scoping.connect(my_region_scoping)
    >>> my_qualifiers1 = dict()
    >>> op.inputs.qualifiers1.connect(my_qualifiers1)
    >>> my_qualifiers2 = dict()
    >>> op.inputs.qualifiers2.connect(my_qualifiers2)
    """

    def __init__(self, op: Operator):
        super().__init__(mass_flow_rate._spec().inputs, op)
        self._time_scoping = Input(mass_flow_rate._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(mass_flow_rate._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._streams_container = Input(mass_flow_rate._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._streams_container)
        self._data_sources = Input(mass_flow_rate._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)
        self._mesh = Input(mass_flow_rate._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)
        self._region_scoping = Input(mass_flow_rate._spec().input_pin(25), 25, op, -1)
        self._inputs.append(self._region_scoping)
        self._qualifiers1 = Input(mass_flow_rate._spec().input_pin(1000), 1000, op, 0)
        self._inputs.append(self._qualifiers1)
        self._qualifiers2 = Input(mass_flow_rate._spec().input_pin(1001), 1001, op, 1)
        self._inputs.append(self._qualifiers2)

    @property
    def time_scoping(self) -> Input:
        r"""Allows to connect time_scoping input to the operator.

        time/freq values (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) required in output. To specify time/freq values at specific load steps, put a Field (and not a list) in input with a scoping located on "TimeFreq_steps". Linear time freq intrapolation is performed if the values are not in the result files and the data at the max time or freq is taken when time/freqs are higher than available time/freqs in result files. To get all data for all time/freq sets, connect an int with value -1.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mass_flow_rate()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def mesh_scoping(self) -> Input:
        r"""Allows to connect mesh_scoping input to the operator.

        nodes or elements scoping required in output. The output fields will be scoped on these node or element IDs. To figure out the ordering of the fields data, look at their scoping IDs as they might not be ordered as the input scoping was. The scoping's location indicates whether nodes or elements are asked for. Using scopings container allows you to split the result fields container into domains

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mass_flow_rate()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def streams_container(self) -> Input:
        r"""Allows to connect streams_container input to the operator.

        result file container allowed to be kept open to cache data

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mass_flow_rate()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self) -> Input:
        r"""Allows to connect data_sources input to the operator.

        result file path container, used if no streams are set

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mass_flow_rate()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def mesh(self) -> Input:
        r"""Allows to connect mesh input to the operator.

        prevents from reading the mesh in the result files

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mass_flow_rate()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def region_scoping(self) -> Input:
        r"""Allows to connect region_scoping input to the operator.

        region id (integer) or vector of region ids (vector) or region scoping (scoping) of the model (region corresponds to zone for Fluid results or part for LSDyna results).

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mass_flow_rate()
        >>> op.inputs.region_scoping.connect(my_region_scoping)
        >>> # or
        >>> op.inputs.region_scoping(my_region_scoping)
        """
        return self._region_scoping

    @property
    def qualifiers1(self) -> Input:
        r"""Allows to connect qualifiers1 input to the operator.

        (for Fluid results only) LabelSpace with combination of zone, phases or species ids

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mass_flow_rate()
        >>> op.inputs.qualifiers1.connect(my_qualifiers1)
        >>> # or
        >>> op.inputs.qualifiers1(my_qualifiers1)
        """
        return self._qualifiers1

    @property
    def qualifiers2(self) -> Input:
        r"""Allows to connect qualifiers2 input to the operator.

        (for Fluid results only) LabelSpace with combination of zone, phases or species ids

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mass_flow_rate()
        >>> op.inputs.qualifiers2.connect(my_qualifiers2)
        >>> # or
        >>> op.inputs.qualifiers2(my_qualifiers2)
        """
        return self._qualifiers2


class OutputsMassFlowRate(_Outputs):
    """Intermediate class used to get outputs from
    mass_flow_rate operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.mass_flow_rate()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(mass_flow_rate._spec().outputs, op)
        self._fields_container = Output(mass_flow_rate._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.result.mass_flow_rate()
        >>> # Get the output from op.outputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """
        return self._fields_container
