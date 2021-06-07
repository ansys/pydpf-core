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
    """Compute a sdot product between two fields and return a scalar.

      available inputs:
        - FieldA (Field)
        - FieldB (Field)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.overall_dot()

      >>> # Make input connections
      >>> my_FieldA = dpf.Field()
      >>> op.inputs.FieldA.connect(my_FieldA)
      >>> my_FieldB = dpf.Field()
      >>> op.inputs.FieldB.connect(my_FieldB)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.overall_dot(FieldA=my_FieldA,FieldB=my_FieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, FieldA=None, FieldB=None, config=None, server=None):
        super().__init__(name="native::overall_dot", config = config, server = server)
        self._inputs = InputsOverallDot(self)
        self._outputs = OutputsOverallDot(self)
        if FieldA !=None:
            self.inputs.FieldA.connect(FieldA)
        if FieldB !=None:
            self.inputs.FieldB.connect(FieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute a sdot product between two fields and return a scalar.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "FieldA", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "FieldB", type_names=["field"], optional=False, document="""""")},
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
      >>> my_FieldA = dpf.Field()
      >>> op.inputs.FieldA.connect(my_FieldA)
      >>> my_FieldB = dpf.Field()
      >>> op.inputs.FieldB.connect(my_FieldB)
    """
    def __init__(self, op: Operator):
        super().__init__(overall_dot._spec().inputs, op)
        self._FieldA = Input(overall_dot._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._FieldA)
        self._FieldB = Input(overall_dot._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._FieldB)

    @property
    def FieldA(self):
        """Allows to connect FieldA input to the operator

        Parameters
        ----------
        my_FieldA : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.overall_dot()
        >>> op.inputs.FieldA.connect(my_FieldA)
        >>> #or
        >>> op.inputs.FieldA(my_FieldA)

        """
        return self._FieldA

    @property
    def FieldB(self):
        """Allows to connect FieldB input to the operator

        Parameters
        ----------
        my_FieldB : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.overall_dot()
        >>> op.inputs.FieldB.connect(my_FieldB)
        >>> #or
        >>> op.inputs.FieldB(my_FieldB)

        """
        return self._FieldB

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

