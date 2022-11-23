"""
interface_resultant_contact_force
=================================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class interface_resultant_contact_force(Operator):
    """Read Interface Resultant Contact Force (LSDyna) by calling the readers defined by the datasources.

      available inputs:
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)
        - entity_scoping (Scoping) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.interface_resultant_contact_force()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_entity_scoping = dpf.Scoping()
      >>> op.inputs.entity_scoping.connect(my_entity_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.interface_resultant_contact_force(data_sources=my_data_sources,entity_scoping=my_entity_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, data_sources=None, entity_scoping=None, config=None, server=None):
        super().__init__(name="R_CFR", config = config, server = server)
        self._inputs = InputsInterfaceResultantContactForce(self)
        self._outputs = OutputsInterfaceResultantContactForce(self)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if entity_scoping !=None:
            self.inputs.entity_scoping.connect(entity_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read Interface Resultant Contact Force (LSDyna) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 6 : PinSpecification(name = "entity_scoping", type_names=["scoping"], optional=True, document="""entity (part for matsum, interface for rcforc) where the result will be scoped""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "R_CFR")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsInterfaceResultantContactForce 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsInterfaceResultantContactForce 
        """
        return super().outputs


#internal name: R_CFR
#scripting name: interface_resultant_contact_force
class InputsInterfaceResultantContactForce(_Inputs):
    """Intermediate class used to connect user inputs to interface_resultant_contact_force operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.interface_resultant_contact_force()
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_entity_scoping = dpf.Scoping()
      >>> op.inputs.entity_scoping.connect(my_entity_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(interface_resultant_contact_force._spec().inputs, op)
        self._streams_container = Input(interface_resultant_contact_force._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(interface_resultant_contact_force._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._entity_scoping = Input(interface_resultant_contact_force._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self._entity_scoping)

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        - pindoc: result file container allowed to be kept open to cache data

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.interface_resultant_contact_force()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: result file path container, used if no streams are set

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.interface_resultant_contact_force()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def entity_scoping(self):
        """Allows to connect entity_scoping input to the operator

        - pindoc: entity (part for matsum, interface for rcforc) where the result will be scoped

        Parameters
        ----------
        my_entity_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.interface_resultant_contact_force()
        >>> op.inputs.entity_scoping.connect(my_entity_scoping)
        >>> #or
        >>> op.inputs.entity_scoping(my_entity_scoping)

        """
        return self._entity_scoping

class OutputsInterfaceResultantContactForce(_Outputs):
    """Intermediate class used to get outputs from interface_resultant_contact_force operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.interface_resultant_contact_force()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(interface_resultant_contact_force._spec().outputs, op)
        self._fields_container = Output(interface_resultant_contact_force._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.interface_resultant_contact_force()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

