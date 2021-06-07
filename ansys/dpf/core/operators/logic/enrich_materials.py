"""
enrich_materials
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "logic" category
"""

class enrich_materials(Operator):
    """Take a MaterialContainer and a stream and enrich the MaterialContainer using stream data.

      available inputs:
        - MaterialContainer (Any)
        - streams (StreamsContainer, FieldsContainer)
        - streams_mapping ()

      available outputs:
        - MaterialContainer (bool)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.enrich_materials()

      >>> # Make input connections
      >>> my_MaterialContainer = dpf.Any()
      >>> op.inputs.MaterialContainer.connect(my_MaterialContainer)
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.logic.enrich_materials(MaterialContainer=my_MaterialContainer,streams=my_streams)

      >>> # Get output data
      >>> result_MaterialContainer = op.outputs.MaterialContainer()"""
    def __init__(self, MaterialContainer=None, streams=None, config=None, server=None):
        super().__init__(name="enrich_materials", config = config, server = server)
        self._inputs = InputsEnrichMaterials(self)
        self._outputs = OutputsEnrichMaterials(self)
        if MaterialContainer !=None:
            self.inputs.MaterialContainer.connect(MaterialContainer)
        if streams !=None:
            self.inputs.streams.connect(streams)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a MaterialContainer and a stream and enrich the MaterialContainer using stream data.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "MaterialContainer", type_names=["any"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "streams", type_names=["streams_container","fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "streams_mapping", type_names=[], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "MaterialContainer", type_names=["bool"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "enrich_materials")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsEnrichMaterials 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsEnrichMaterials 
        """
        return super().outputs


#internal name: enrich_materials
#scripting name: enrich_materials
class InputsEnrichMaterials(_Inputs):
    """Intermediate class used to connect user inputs to enrich_materials operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.logic.enrich_materials()
      >>> my_MaterialContainer = dpf.Any()
      >>> op.inputs.MaterialContainer.connect(my_MaterialContainer)
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)
    """
    def __init__(self, op: Operator):
        super().__init__(enrich_materials._spec().inputs, op)
        self._MaterialContainer = Input(enrich_materials._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._MaterialContainer)
        self._streams = Input(enrich_materials._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._streams)

    @property
    def MaterialContainer(self):
        """Allows to connect MaterialContainer input to the operator

        Parameters
        ----------
        my_MaterialContainer : Any, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.enrich_materials()
        >>> op.inputs.MaterialContainer.connect(my_MaterialContainer)
        >>> #or
        >>> op.inputs.MaterialContainer(my_MaterialContainer)

        """
        return self._MaterialContainer

    @property
    def streams(self):
        """Allows to connect streams input to the operator

        Parameters
        ----------
        my_streams : StreamsContainer, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.enrich_materials()
        >>> op.inputs.streams.connect(my_streams)
        >>> #or
        >>> op.inputs.streams(my_streams)

        """
        return self._streams

class OutputsEnrichMaterials(_Outputs):
    """Intermediate class used to get outputs from enrich_materials operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.logic.enrich_materials()
      >>> # Connect inputs : op.inputs. ...
      >>> result_MaterialContainer = op.outputs.MaterialContainer()
    """
    def __init__(self, op: Operator):
        super().__init__(enrich_materials._spec().outputs, op)
        self._MaterialContainer = Output(enrich_materials._spec().output_pin(0), 0, op) 
        self._outputs.append(self._MaterialContainer)

    @property
    def MaterialContainer(self):
        """Allows to get MaterialContainer output of the operator


        Returns
        ----------
        my_MaterialContainer : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.enrich_materials()
        >>> # Connect inputs : op.inputs. ...
        >>> result_MaterialContainer = op.outputs.MaterialContainer() 
        """
        return self._MaterialContainer

