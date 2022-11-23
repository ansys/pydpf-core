"""
eigen_vectors
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "invariant" category
"""

class eigen_vectors(Operator):
    """Computes the element-wise eigen vectors for each tensor in the field

      available inputs:
        - field (FieldsContainer, Field)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.invariant.eigen_vectors()

      >>> # Make input connections
      >>> my_field = dpf.FieldsContainer()
      >>> op.inputs.field.connect(my_field)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.invariant.eigen_vectors(field=my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="eig_vectors", config = config, server = server)
        self._inputs = InputsEigenVectors(self)
        self._outputs = OutputsEigenVectors(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise eigen vectors for each tensor in the field""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["fields_container","field"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "eig_vectors")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsEigenVectors 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsEigenVectors 
        """
        return super().outputs


#internal name: eig_vectors
#scripting name: eigen_vectors
class InputsEigenVectors(_Inputs):
    """Intermediate class used to connect user inputs to eigen_vectors operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.eigen_vectors()
      >>> my_field = dpf.FieldsContainer()
      >>> op.inputs.field.connect(my_field)
    """
    def __init__(self, op: Operator):
        super().__init__(eigen_vectors._spec().inputs, op)
        self._field = Input(eigen_vectors._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_field : FieldsContainer, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.eigen_vectors()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

class OutputsEigenVectors(_Outputs):
    """Intermediate class used to get outputs from eigen_vectors operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.eigen_vectors()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(eigen_vectors._spec().outputs, op)
        self._field = Output(eigen_vectors._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.invariant.eigen_vectors()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

