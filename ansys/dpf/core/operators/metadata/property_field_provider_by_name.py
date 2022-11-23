"""
property_field_provider_by_name
===============================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "metadata" category
"""

class property_field_provider_by_name(Operator):
    """Provides the property values for a set of elements for a defined property name.

      available inputs:
        - mesh_scoping (Scoping) (optional)
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)
        - property_name (str)

      available outputs:
        - property_field (PropertyField)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.property_field_provider_by_name()

      >>> # Make input connections
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_property_name = str()
      >>> op.inputs.property_name.connect(my_property_name)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.metadata.property_field_provider_by_name(mesh_scoping=my_mesh_scoping,streams_container=my_streams_container,data_sources=my_data_sources,property_name=my_property_name)

      >>> # Get output data
      >>> result_property_field = op.outputs.property_field()"""
    def __init__(self, mesh_scoping=None, streams_container=None, data_sources=None, property_name=None, config=None, server=None):
        super().__init__(name="property_field_provider_by_name", config = config, server = server)
        self._inputs = InputsPropertyFieldProviderByName(self)
        self._outputs = OutputsPropertyFieldProviderByName(self)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if property_name !=None:
            self.inputs.property_name.connect(property_name)

    @staticmethod
    def _spec():
        spec = Specification(description="""Provides the property values for a set of elements for a defined property name.""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""scoping that defines the set of elements to fetch the property values for. If not specified, applied on all the elements of the mesh."""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""optional if using a dataSources"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""optional if using a streamsContainer"""), 
                                 13 : PinSpecification(name = "property_name", type_names=["string"], optional=False, document="""property to read, that can be the following: elements_connectivity, nodes_connectivity, material, element_type, mapdl_element_type, mapdl_element_type_id harmonic_index, step, substep, keyopt_i (i = 1 -> 18).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "property_field", type_names=["property_field"], optional=False, document="""property field""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "property_field_provider_by_name")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPropertyFieldProviderByName 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPropertyFieldProviderByName 
        """
        return super().outputs


#internal name: property_field_provider_by_name
#scripting name: property_field_provider_by_name
class InputsPropertyFieldProviderByName(_Inputs):
    """Intermediate class used to connect user inputs to property_field_provider_by_name operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.property_field_provider_by_name()
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_property_name = str()
      >>> op.inputs.property_name.connect(my_property_name)
    """
    def __init__(self, op: Operator):
        super().__init__(property_field_provider_by_name._spec().inputs, op)
        self._mesh_scoping = Input(property_field_provider_by_name._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._streams_container = Input(property_field_provider_by_name._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(property_field_provider_by_name._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._property_name = Input(property_field_provider_by_name._spec().input_pin(13), 13, op, -1) 
        self._inputs.append(self._property_name)

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        - pindoc: scoping that defines the set of elements to fetch the property values for. If not specified, applied on all the elements of the mesh.

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.property_field_provider_by_name()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        - pindoc: optional if using a dataSources

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.property_field_provider_by_name()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: optional if using a streamsContainer

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.property_field_provider_by_name()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def property_name(self):
        """Allows to connect property_name input to the operator

        - pindoc: property to read, that can be the following: elements_connectivity, nodes_connectivity, material, element_type, mapdl_element_type, mapdl_element_type_id harmonic_index, step, substep, keyopt_i (i = 1 -> 18).

        Parameters
        ----------
        my_property_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.property_field_provider_by_name()
        >>> op.inputs.property_name.connect(my_property_name)
        >>> #or
        >>> op.inputs.property_name(my_property_name)

        """
        return self._property_name

class OutputsPropertyFieldProviderByName(_Outputs):
    """Intermediate class used to get outputs from property_field_provider_by_name operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.property_field_provider_by_name()
      >>> # Connect inputs : op.inputs. ...
      >>> result_property_field = op.outputs.property_field()
    """
    def __init__(self, op: Operator):
        super().__init__(property_field_provider_by_name._spec().outputs, op)
        self._property_field = Output(property_field_provider_by_name._spec().output_pin(0), 0, op) 
        self._outputs.append(self._property_field)

    @property
    def property_field(self):
        """Allows to get property_field output of the operator


        - pindoc: property field

        Returns
        ----------
        my_property_field : PropertyField, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.property_field_provider_by_name()
        >>> # Connect inputs : op.inputs. ...
        >>> result_property_field = op.outputs.property_field() 
        """
        return self._property_field

