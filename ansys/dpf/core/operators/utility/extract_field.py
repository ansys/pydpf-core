"""
extract_field
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class extract_field(Operator):
    """Extract the fields at the indices defined in the vector (in 1) form the fields container (in:0).

      available inputs:
        - fields_container (Field, FieldsContainer)
        - indices (list) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.extract_field()

      >>> # Make input connections
      >>> my_fields_container = dpf.Field()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_indices = dpf.list()
      >>> op.inputs.indices.connect(my_indices)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.extract_field(fields_container=my_fields_container,indices=my_indices)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fields_container=None, indices=None, config=None, server=None):
        super().__init__(name="ExtractFromFC", config = config, server = server)
        self._inputs = InputsExtractField(self)
        self._outputs = OutputsExtractField(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if indices !=None:
            self.inputs.indices.connect(indices)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extract the fields at the indices defined in the vector (in 1) form the fields container (in:0).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["field","fields_container"], optional=False, document="""if a field is in input, it is passed on as output"""), 
                                 1 : PinSpecification(name = "indices", type_names=["vector<int32>"], optional=True, document="""default is the first field""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ExtractFromFC")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsExtractField 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsExtractField 
        """
        return super().outputs


#internal name: ExtractFromFC
#scripting name: extract_field
class InputsExtractField(_Inputs):
    """Intermediate class used to connect user inputs to extract_field operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.extract_field()
      >>> my_fields_container = dpf.Field()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_indices = dpf.list()
      >>> op.inputs.indices.connect(my_indices)
    """
    def __init__(self, op: Operator):
        super().__init__(extract_field._spec().inputs, op)
        self._fields_container = Input(extract_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._indices = Input(extract_field._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._indices)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: if a field is in input, it is passed on as output

        Parameters
        ----------
        my_fields_container : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_field()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def indices(self):
        """Allows to connect indices input to the operator

        - pindoc: default is the first field

        Parameters
        ----------
        my_indices : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_field()
        >>> op.inputs.indices.connect(my_indices)
        >>> #or
        >>> op.inputs.indices(my_indices)

        """
        return self._indices

class OutputsExtractField(_Outputs):
    """Intermediate class used to get outputs from extract_field operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.extract_field()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(extract_field._spec().outputs, op)
        self._field = Output(extract_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_field()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

