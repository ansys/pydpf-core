"""
convertnum_nod_to_bcs
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "invariant" category
"""

class convertnum_nod_to_bcs(Operator):
    """Converts fields container from NOD to BCS ordering

      available inputs:
        - fields_container (FieldsContainer)
        - data_sources (DataSources)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.invariant.convertnum_nod_to_bcs()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.invariant.convertnum_nod_to_bcs(fields_container=my_fields_container,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="convertnum_nod_to_bcs", config = config, server = server)
        self._inputs = InputsConvertnumNodToBcs(self)
        self._outputs = OutputsConvertnumNodToBcs(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Converts fields container from NOD to BCS ordering""",
                             map_input_pin_spec={
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""fields_container"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""Data_sources (must contain the fullfile).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "convertnum_nod_to_bcs")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsConvertnumNodToBcs 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsConvertnumNodToBcs 
        """
        return super().outputs


#internal name: convertnum_nod_to_bcs
#scripting name: convertnum_nod_to_bcs
class InputsConvertnumNodToBcs(_Inputs):
    """Intermediate class used to connect user inputs to convertnum_nod_to_bcs operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.convertnum_nod_to_bcs()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(convertnum_nod_to_bcs._spec().inputs, op)
        self._fields_container = Input(convertnum_nod_to_bcs._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._fields_container)
        self._data_sources = Input(convertnum_nod_to_bcs._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: fields_container

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.convertnum_nod_to_bcs()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: Data_sources (must contain the fullfile).

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.convertnum_nod_to_bcs()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsConvertnumNodToBcs(_Outputs):
    """Intermediate class used to get outputs from convertnum_nod_to_bcs operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.convertnum_nod_to_bcs()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(convertnum_nod_to_bcs._spec().outputs, op)
        self._fields_container = Output(convertnum_nod_to_bcs._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.invariant.convertnum_nod_to_bcs()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

