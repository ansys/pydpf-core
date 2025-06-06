"""
mapdl_material_properties

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


class mapdl_material_properties(Operator):
    r"""Read the values of the properties of a material for a given materials
    property field (property field that contains materials information for
    each element of a mesh).It returns a fields container containing a field
    for each material property, with only one value per material. The
    following keys can be used: Young’s modulus (keys: EX, EY, EZ),
    Poisson’s ratio (keys: NUXY, NUYZ, NUXZ), Shear Modulus (keys: GXY, GYZ,
    GXZ), Coefficient of Thermal Expansion (keys: ALPX, ALPY, ALPZ), Volumic
    Mass (key: DENS), second Lame’s coefficient (key: MU), Damping
    coefficient (key: DAMP), thermal Conductivity (keys: KXX, KYY, KZZ),
    Resistivity (keys: RSVX, RSVY, RSVZ), Specific heat in constant volume
    (key: C), Film coefficient (key: HF), Viscosity (key: VISC), Emissivity
    (key: EMIS).


    Parameters
    ----------
    properties_name: str
    materials: PropertyField
        Property field that contains a material id per element.
    streams_container: StreamsContainer
    data_sources: DataSources

    Returns
    -------
    properties_value: FieldsContainer

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.mapdl_material_properties()

    >>> # Make input connections
    >>> my_properties_name = str()
    >>> op.inputs.properties_name.connect(my_properties_name)
    >>> my_materials = dpf.PropertyField()
    >>> op.inputs.materials.connect(my_materials)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.mapdl_material_properties(
    ...     properties_name=my_properties_name,
    ...     materials=my_materials,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_properties_value = op.outputs.properties_value()
    """

    def __init__(
        self,
        properties_name=None,
        materials=None,
        streams_container=None,
        data_sources=None,
        config=None,
        server=None,
    ):
        super().__init__(name="mapdl_material_properties", config=config, server=server)
        self._inputs = InputsMapdlMaterialProperties(self)
        self._outputs = OutputsMapdlMaterialProperties(self)
        if properties_name is not None:
            self.inputs.properties_name.connect(properties_name)
        if materials is not None:
            self.inputs.materials.connect(materials)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Read the values of the properties of a material for a given materials
property field (property field that contains materials information for
each element of a mesh).It returns a fields container containing a field
for each material property, with only one value per material. The
following keys can be used: Young’s modulus (keys: EX, EY, EZ),
Poisson’s ratio (keys: NUXY, NUYZ, NUXZ), Shear Modulus (keys: GXY, GYZ,
GXZ), Coefficient of Thermal Expansion (keys: ALPX, ALPY, ALPZ), Volumic
Mass (key: DENS), second Lame’s coefficient (key: MU), Damping
coefficient (key: DAMP), thermal Conductivity (keys: KXX, KYY, KZZ),
Resistivity (keys: RSVX, RSVY, RSVZ), Specific heat in constant volume
(key: C), Film coefficient (key: HF), Viscosity (key: VISC), Emissivity
(key: EMIS).
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="properties_name",
                    type_names=["string", "vector<string>"],
                    optional=False,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="materials",
                    type_names=["property_field"],
                    optional=False,
                    document=r"""Property field that contains a material id per element.""",
                ),
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=False,
                    document=r"""""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document=r"""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="properties_value",
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
        return Operator.default_config(name="mapdl_material_properties", server=server)

    @property
    def inputs(self) -> InputsMapdlMaterialProperties:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsMapdlMaterialProperties.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsMapdlMaterialProperties:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsMapdlMaterialProperties.
        """
        return super().outputs


class InputsMapdlMaterialProperties(_Inputs):
    """Intermediate class used to connect user inputs to
    mapdl_material_properties operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.mapdl_material_properties()
    >>> my_properties_name = str()
    >>> op.inputs.properties_name.connect(my_properties_name)
    >>> my_materials = dpf.PropertyField()
    >>> op.inputs.materials.connect(my_materials)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(mapdl_material_properties._spec().inputs, op)
        self._properties_name = Input(
            mapdl_material_properties._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._properties_name)
        self._materials = Input(
            mapdl_material_properties._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._materials)
        self._streams_container = Input(
            mapdl_material_properties._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(
            mapdl_material_properties._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)

    @property
    def properties_name(self) -> Input:
        r"""Allows to connect properties_name input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mapdl_material_properties()
        >>> op.inputs.properties_name.connect(my_properties_name)
        >>> # or
        >>> op.inputs.properties_name(my_properties_name)
        """
        return self._properties_name

    @property
    def materials(self) -> Input:
        r"""Allows to connect materials input to the operator.

        Property field that contains a material id per element.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mapdl_material_properties()
        >>> op.inputs.materials.connect(my_materials)
        >>> # or
        >>> op.inputs.materials(my_materials)
        """
        return self._materials

    @property
    def streams_container(self) -> Input:
        r"""Allows to connect streams_container input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mapdl_material_properties()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self) -> Input:
        r"""Allows to connect data_sources input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mapdl_material_properties()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsMapdlMaterialProperties(_Outputs):
    """Intermediate class used to get outputs from
    mapdl_material_properties operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.mapdl_material_properties()
    >>> # Connect inputs : op.inputs. ...
    >>> result_properties_value = op.outputs.properties_value()
    """

    def __init__(self, op: Operator):
        super().__init__(mapdl_material_properties._spec().outputs, op)
        self._properties_value = Output(
            mapdl_material_properties._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._properties_value)

    @property
    def properties_value(self) -> Output:
        r"""Allows to get properties_value output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mapdl_material_properties()
        >>> # Get the output from op.outputs. ...
        >>> result_properties_value = op.outputs.properties_value()
        """
        return self._properties_value
