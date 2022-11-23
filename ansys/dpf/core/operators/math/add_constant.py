"""
add_constant
============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class add_constant(Operator):
    """Computes the sum of a field (in 0) and a scalar (in 1).

      available inputs:
        - field (Field, FieldsContainer)
        - ponderation (float, list)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.add_constant()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.add_constant(field=my_field,ponderation=my_ponderation)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, ponderation=None, config=None, server=None):
        super().__init__(name="add_constant", config = config, server = server)
        self._inputs = InputsAddConstant(self)
        self._outputs = OutputsAddConstant(self)
        if field !=None:
            self.inputs.field.connect(field)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the sum of a field (in 0) and a scalar (in 1).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "ponderation", type_names=["double","vector<double>"], optional=False, document="""double or vector of double""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "add_constant")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAddConstant 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAddConstant 
        """
        return super().outputs


#internal name: add_constant
#scripting name: add_constant
class InputsAddConstant(_Inputs):
    """Intermediate class used to connect user inputs to add_constant operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.add_constant()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)
    """
    def __init__(self, op: Operator):
        super().__init__(add_constant._spec().inputs, op)
        self._field = Input(add_constant._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._ponderation = Input(add_constant._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._ponderation)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.add_constant()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def ponderation(self):
        """Allows to connect ponderation input to the operator

        - pindoc: double or vector of double

        Parameters
        ----------
        my_ponderation : float, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.add_constant()
        >>> op.inputs.ponderation.connect(my_ponderation)
        >>> #or
        >>> op.inputs.ponderation(my_ponderation)

        """
        return self._ponderation

class OutputsAddConstant(_Outputs):
    """Intermediate class used to get outputs from add_constant operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.add_constant()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(add_constant._spec().outputs, op)
        self._field = Output(add_constant._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.add_constant()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

