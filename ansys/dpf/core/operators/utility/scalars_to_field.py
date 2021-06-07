"""
scalars_to_field
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class scalars_to_field(Operator):
    """take a double or a vector of double and transform it in a one entity field of location "numeric".

      available inputs:
        - double_or_vector_double (float, list)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.scalars_to_field()

      >>> # Make input connections
      >>> my_double_or_vector_double = float()
      >>> op.inputs.double_or_vector_double.connect(my_double_or_vector_double)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.scalars_to_field(double_or_vector_double=my_double_or_vector_double)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, double_or_vector_double=None, config=None, server=None):
        super().__init__(name="fieldify", config = config, server = server)
        self._inputs = InputsScalarsToField(self)
        self._outputs = OutputsScalarsToField(self)
        if double_or_vector_double !=None:
            self.inputs.double_or_vector_double.connect(double_or_vector_double)

    @staticmethod
    def _spec():
        spec = Specification(description="""take a double or a vector of double and transform it in a one entity field of location "numeric".""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "double_or_vector_double", type_names=["double","vector<double>"], optional=False, document="""double or vector of double""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "fieldify")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsScalarsToField 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsScalarsToField 
        """
        return super().outputs


#internal name: fieldify
#scripting name: scalars_to_field
class InputsScalarsToField(_Inputs):
    """Intermediate class used to connect user inputs to scalars_to_field operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.scalars_to_field()
      >>> my_double_or_vector_double = float()
      >>> op.inputs.double_or_vector_double.connect(my_double_or_vector_double)
    """
    def __init__(self, op: Operator):
        super().__init__(scalars_to_field._spec().inputs, op)
        self._double_or_vector_double = Input(scalars_to_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._double_or_vector_double)

    @property
    def double_or_vector_double(self):
        """Allows to connect double_or_vector_double input to the operator

        - pindoc: double or vector of double

        Parameters
        ----------
        my_double_or_vector_double : float, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.scalars_to_field()
        >>> op.inputs.double_or_vector_double.connect(my_double_or_vector_double)
        >>> #or
        >>> op.inputs.double_or_vector_double(my_double_or_vector_double)

        """
        return self._double_or_vector_double

class OutputsScalarsToField(_Outputs):
    """Intermediate class used to get outputs from scalars_to_field operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.scalars_to_field()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(scalars_to_field._spec().outputs, op)
        self._field = Output(scalars_to_field._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.utility.scalars_to_field()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

