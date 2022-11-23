"""
sqrt
====
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class sqrt(Operator):
    """Computes element-wise sqrt(field1).

      available inputs:
        - field (Field, FieldsContainer)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.sqrt()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.sqrt(field=my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="sqrt", config = config, server = server)
        self._inputs = InputsSqrt(self)
        self._outputs = OutputsSqrt(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise sqrt(field1).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sqrt")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSqrt 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSqrt 
        """
        return super().outputs


#internal name: sqrt
#scripting name: sqrt
class InputsSqrt(_Inputs):
    """Intermediate class used to connect user inputs to sqrt operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.sqrt()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
    """
    def __init__(self, op: Operator):
        super().__init__(sqrt._spec().inputs, op)
        self._field = Input(sqrt._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)

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

        >>> op = dpf.operators.math.sqrt()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

class OutputsSqrt(_Outputs):
    """Intermediate class used to get outputs from sqrt operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.sqrt()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(sqrt._spec().outputs, op)
        self._field = Output(sqrt._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.sqrt()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

