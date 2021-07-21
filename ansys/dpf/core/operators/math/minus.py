"""
minus
=====
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class minus(Operator):
    """Computes the difference of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

      available inputs:
        - fieldA (Field, FieldsContainer, float, list)
        - fieldB (Field, FieldsContainer, float, list)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.minus()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.minus(fieldA=my_fieldA,fieldB=my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="minus", config = config, server = server)
        self._inputs = InputsMinus(self)
        self._outputs = OutputsMinus(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the difference of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container","double","vector<double>"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container","double","vector<double>"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "minus")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMinus 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMinus 
        """
        return super().outputs


#internal name: minus
#scripting name: minus
class InputsMinus(_Inputs):
    """Intermediate class used to connect user inputs to minus operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.minus()
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
    """
    def __init__(self, op: Operator):
        super().__init__(minus._spec().inputs, op)
        self._fieldA = Input(minus._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fieldA)
        self._fieldB = Input(minus._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fieldB)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fieldA : Field, FieldsContainer, float, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.minus()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> #or
        >>> op.inputs.fieldA(my_fieldA)

        """
        return self._fieldA

    @property
    def fieldB(self):
        """Allows to connect fieldB input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fieldB : Field, FieldsContainer, float, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.minus()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> #or
        >>> op.inputs.fieldB(my_fieldB)

        """
        return self._fieldB

class OutputsMinus(_Outputs):
    """Intermediate class used to get outputs from minus operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.minus()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(minus._spec().outputs, op)
        self._field = Output(minus._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.minus()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

