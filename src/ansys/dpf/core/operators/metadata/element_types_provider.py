"""
element_types_provider

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


class element_types_provider(Operator):
    r"""Reads element types data from the result files contained in the streams
    or data sources.


    Parameters
    ----------
    solver_element_types_ids: int, optional
        Element Type ids to recover used by the solver. If not set, all available element types to be recovered.
    streams: StreamsContainer, optional
        Result file container allowed to be kept open to cache data.
    data_sources: DataSources
        Result file path container, used if no streams are set.

    Returns
    -------
    element_types_data: GenericDataContainer
        The generic_data_container has a class_name: ElementTypesProperties. It contains the following property fields: element_routine_number: Element routine number. E.g 186 for SOLID186, keyopts: Element type option keys, kdofs: DOF/node for this element type.This is a bit mapping, nodelm: Number of nodes for this element type, nodfor: Number of nodes per element having nodal forces, nodstr: Number of nodes per element having nodal stresses, new_gen_element: Element of new generation.

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.metadata.element_types_provider()

    >>> # Make input connections
    >>> my_solver_element_types_ids = int()
    >>> op.inputs.solver_element_types_ids.connect(my_solver_element_types_ids)
    >>> my_streams = dpf.StreamsContainer()
    >>> op.inputs.streams.connect(my_streams)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.metadata.element_types_provider(
    ...     solver_element_types_ids=my_solver_element_types_ids,
    ...     streams=my_streams,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_element_types_data = op.outputs.element_types_data()
    """

    def __init__(
        self,
        solver_element_types_ids=None,
        streams=None,
        data_sources=None,
        config=None,
        server=None,
    ):
        super().__init__(name="element_types_provider", config=config, server=server)
        self._inputs = InputsElementTypesProvider(self)
        self._outputs = OutputsElementTypesProvider(self)
        if solver_element_types_ids is not None:
            self.inputs.solver_element_types_ids.connect(solver_element_types_ids)
        if streams is not None:
            self.inputs.streams.connect(streams)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Reads element types data from the result files contained in the streams
or data sources.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                1: PinSpecification(
                    name="solver_element_types_ids",
                    type_names=["int32", "vector<int32>"],
                    optional=True,
                    document=r"""Element Type ids to recover used by the solver. If not set, all available element types to be recovered.""",
                ),
                3: PinSpecification(
                    name="streams",
                    type_names=["streams_container"],
                    optional=True,
                    document=r"""Result file container allowed to be kept open to cache data.""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document=r"""Result file path container, used if no streams are set.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="element_types_data",
                    type_names=["generic_data_container"],
                    optional=False,
                    document=r"""The generic_data_container has a class_name: ElementTypesProperties. It contains the following property fields: element_routine_number: Element routine number. E.g 186 for SOLID186, keyopts: Element type option keys, kdofs: DOF/node for this element type.This is a bit mapping, nodelm: Number of nodes for this element type, nodfor: Number of nodes per element having nodal forces, nodstr: Number of nodes per element having nodal stresses, new_gen_element: Element of new generation.""",
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
        return Operator.default_config(name="element_types_provider", server=server)

    @property
    def inputs(self) -> InputsElementTypesProvider:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsElementTypesProvider.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsElementTypesProvider:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsElementTypesProvider.
        """
        return super().outputs


class InputsElementTypesProvider(_Inputs):
    """Intermediate class used to connect user inputs to
    element_types_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.metadata.element_types_provider()
    >>> my_solver_element_types_ids = int()
    >>> op.inputs.solver_element_types_ids.connect(my_solver_element_types_ids)
    >>> my_streams = dpf.StreamsContainer()
    >>> op.inputs.streams.connect(my_streams)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(element_types_provider._spec().inputs, op)
        self._solver_element_types_ids = Input(
            element_types_provider._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._solver_element_types_ids)
        self._streams = Input(element_types_provider._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._streams)
        self._data_sources = Input(
            element_types_provider._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)

    @property
    def solver_element_types_ids(self) -> Input:
        r"""Allows to connect solver_element_types_ids input to the operator.

        Element Type ids to recover used by the solver. If not set, all available element types to be recovered.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.metadata.element_types_provider()
        >>> op.inputs.solver_element_types_ids.connect(my_solver_element_types_ids)
        >>> # or
        >>> op.inputs.solver_element_types_ids(my_solver_element_types_ids)
        """
        return self._solver_element_types_ids

    @property
    def streams(self) -> Input:
        r"""Allows to connect streams input to the operator.

        Result file container allowed to be kept open to cache data.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.metadata.element_types_provider()
        >>> op.inputs.streams.connect(my_streams)
        >>> # or
        >>> op.inputs.streams(my_streams)
        """
        return self._streams

    @property
    def data_sources(self) -> Input:
        r"""Allows to connect data_sources input to the operator.

        Result file path container, used if no streams are set.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.metadata.element_types_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsElementTypesProvider(_Outputs):
    """Intermediate class used to get outputs from
    element_types_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.metadata.element_types_provider()
    >>> # Connect inputs : op.inputs. ...
    >>> result_element_types_data = op.outputs.element_types_data()
    """

    def __init__(self, op: Operator):
        super().__init__(element_types_provider._spec().outputs, op)
        self._element_types_data = Output(
            element_types_provider._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._element_types_data)

    @property
    def element_types_data(self) -> Output:
        r"""Allows to get element_types_data output of the operator

        The generic_data_container has a class_name: ElementTypesProperties. It contains the following property fields: element_routine_number: Element routine number. E.g 186 for SOLID186, keyopts: Element type option keys, kdofs: DOF/node for this element type.This is a bit mapping, nodelm: Number of nodes for this element type, nodfor: Number of nodes per element having nodal forces, nodstr: Number of nodes per element having nodal stresses, new_gen_element: Element of new generation.

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.metadata.element_types_provider()
        >>> # Get the output from op.outputs. ...
        >>> result_element_types_data = op.outputs.element_types_data()
        """
        return self._element_types_data
