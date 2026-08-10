"""
matrix_inverse
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class matrix_inverse(Operator):
    """
Computes the [matrix inverse](https://en.wikipedia.org/wiki/Invertible_matrix)
for each complex square matrix field in the input fields container.
Both real and imaginary parts must be present (complex label required).
The input fields must be square ($n \times n$) matrices; non-square inputs throw an error.
The output unit is the inverse of the input unit.


      available inputs:
        - fields_container (FieldsContainer)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.matrix_inverse()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.matrix_inverse(fields_container=my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="inverseOp", config = config, server = server)
        self._inputs = InputsMatrixInverse(self)
        self._outputs = OutputsMatrixInverse(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""
Computes the [matrix inverse](https://en.wikipedia.org/wiki/Invertible_matrix)
for each complex square matrix field in the input fields container.
Both real and imaginary parts must be present (complex label required).
The input fields must be square ($n \times n$) matrices; non-square inputs throw an error.
The output unit is the inverse of the input unit.
""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""Fields container of complex square matrix fields to invert. Must have a complex label with real (index 0) and imaginary (index 1) parts. Each field must be a square matrix.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""Fields container of inverted complex matrices. Same label structure as the input. Unit is the inverse of the input unit.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "inverseOp")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsMatrixInverse 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsMatrixInverse 
        """
        return super().outputs


#internal name: inverseOp
#scripting name: matrix_inverse
class InputsMatrixInverse(_Inputs):
    """Intermediate class used to connect user inputs to matrix_inverse operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.matrix_inverse()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
    """
    def __init__(self, op: Operator):
        super().__init__(matrix_inverse._spec().inputs, op)
        self._fields_container = Input(matrix_inverse._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: Fields container of complex square matrix fields to invert. Must have a complex label with real (index 0) and imaginary (index 1) parts. Each field must be a square matrix.

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.matrix_inverse()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

class OutputsMatrixInverse(_Outputs):
    """Intermediate class used to get outputs from matrix_inverse operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.matrix_inverse()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(matrix_inverse._spec().outputs, op)
        self._fields_container = Output(matrix_inverse._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        - pindoc: Fields container of inverted complex matrices. Same label structure as the input. Unit is the inverse of the input unit.

        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.matrix_inverse()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

