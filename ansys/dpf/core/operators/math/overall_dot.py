"""
overall_dot
===========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class overall_dot(Operator):
    """Compute a dot product between two fields (fields are seen like a single large vector) and return a scalar.

      available inputs:
        - fieldA (Field)
        - fieldB (Field)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.overall_dot()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.overall_dot(fieldA=my_fieldA,fieldB=my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="native::overall_dot", config = config, server = server)
        self._inputs = InputsOverallDot(self)
        self._outputs = OutputsOverallDot(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute a dot product between two fields (fields are seen like a single large vector) and return a scalar.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""Field defined on over-all location, contains a unique scalar value""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "native::overall_dot")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsOverallDot 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsOverallDot 
        """
        return super().outputs


#internal name: native::overall_dot
#scripting name: overall_dot
class InputsOverallDot(_Inputs):
    """Intermediate class used to connect user inputs to overall_dot operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.overall_dot()
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
    """
    def __init__(self, op: Operator):
        super().__init__(overall_dot._spec().inputs, op)
        self._fieldA = Input(overall_dot._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fieldA)
        self._fieldB = Input(overall_dot._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fieldB)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator

        Parameters
        ----------
        my_fieldA : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.overall_dot()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> #or
        >>> op.inputs.fieldA(my_fieldA)

        """
        return self._fieldA

    @property
    def fieldB(self):
        """Allows to connect fieldB input to the operator

        Parameters
        ----------
        my_fieldB : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.overall_dot()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> #or
        >>> op.inputs.fieldB(my_fieldB)

        """
        return self._fieldB

class OutputsOverallDot(_Outputs):
    """Intermediate class used to get outputs from overall_dot operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.overall_dot()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(overall_dot._spec().outputs, op)
        self._field = Output(overall_dot._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        - pindoc: Field defined on over-all location, contains a unique scalar value

        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.overall_dot()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

