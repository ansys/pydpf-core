"""
torque
======
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "result" category
"""

class torque(Operator):
    """Compute torque of a force based on a 3D point.

      available inputs:
        - fields_container (FieldsContainer)
        - vector_of_double (list)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.torque()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_vector_of_double = dpf.list()
      >>> op.inputs.vector_of_double.connect(my_vector_of_double)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.torque(fields_container=my_fields_container,vector_of_double=my_vector_of_double)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, vector_of_double=None, config=None, server=None):
        super().__init__(name="torque", config = config, server = server)
        self._inputs = InputsTorque(self)
        self._outputs = OutputsTorque(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if vector_of_double !=None:
            self.inputs.vector_of_double.connect(vector_of_double)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute torque of a force based on a 3D point.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""fields_container"""), 
                                 1 : PinSpecification(name = "vector_of_double", type_names=["vector<double>"], optional=False, document="""vector_of_double""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "torque")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsTorque 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsTorque 
        """
        return super().outputs


#internal name: torque
#scripting name: torque
class InputsTorque(_Inputs):
    """Intermediate class used to connect user inputs to torque operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.torque()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_vector_of_double = dpf.list()
      >>> op.inputs.vector_of_double.connect(my_vector_of_double)
    """
    def __init__(self, op: Operator):
        super().__init__(torque._spec().inputs, op)
        self._fields_container = Input(torque._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._vector_of_double = Input(torque._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._vector_of_double)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: fields_container

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.torque()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def vector_of_double(self):
        """Allows to connect vector_of_double input to the operator

        - pindoc: vector_of_double

        Parameters
        ----------
        my_vector_of_double : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.torque()
        >>> op.inputs.vector_of_double.connect(my_vector_of_double)
        >>> #or
        >>> op.inputs.vector_of_double(my_vector_of_double)

        """
        return self._vector_of_double

class OutputsTorque(_Outputs):
    """Intermediate class used to get outputs from torque operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.torque()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(torque._spec().outputs, op)
        self._fields_container = Output(torque._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.torque()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

