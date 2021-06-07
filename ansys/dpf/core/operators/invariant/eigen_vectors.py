"""
eigen_vectors
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "invariant" category
"""

class eigen_vectors(Operator):
    """Computes the element-wise eigen vectors for each tensor in the fields of the field container

      available inputs:
        - fields (FieldsContainer, Field)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.invariant.eigen_vectors()

      >>> # Make input connections
      >>> my_fields = dpf.FieldsContainer()
      >>> op.inputs.fields.connect(my_fields)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.invariant.eigen_vectors(fields=my_fields)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields=None, config=None, server=None):
        super().__init__(name="eig_vectors", config = config, server = server)
        self._inputs = InputsEigenVectors(self)
        self._outputs = OutputsEigenVectors(self)
        if fields !=None:
            self.inputs.fields.connect(fields)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise eigen vectors for each tensor in the fields of the field container""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
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
      >>> my_fields = dpf.FieldsContainer()
      >>> op.inputs.fields.connect(my_fields)
    """
    def __init__(self, op: Operator):
        super().__init__(eigen_vectors._spec().inputs, op)
        self._fields = Input(eigen_vectors._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields)

    @property
    def fields(self):
        """Allows to connect fields input to the operator

        Parameters
        ----------
        my_fields : FieldsContainer, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.eigen_vectors()
        >>> op.inputs.fields.connect(my_fields)
        >>> #or
        >>> op.inputs.fields(my_fields)

        """
        return self._fields

class OutputsEigenVectors(_Outputs):
    """Intermediate class used to get outputs from eigen_vectors operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.eigen_vectors()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(eigen_vectors._spec().outputs, op)
        self._fields_container = Output(eigen_vectors._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.invariant.eigen_vectors()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

