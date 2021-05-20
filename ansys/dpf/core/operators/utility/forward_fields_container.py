"""
forward_fields_container
========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class forward_fields_container(Operator):
    """Return the input field or fields container.

      available inputs:
        - fields (FieldsContainer, Field)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.forward_fields_container()

      >>> # Make input connections
      >>> my_fields = dpf.FieldsContainer()
      >>> op.inputs.fields.connect(my_fields)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.forward_fields_container(fields=my_fields)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields=None, config=None, server=None):
        super().__init__(name="forward_fc", config = config, server = server)
        self._inputs = InputsForwardFieldsContainer(self)
        self._outputs = OutputsForwardFieldsContainer(self)
        if fields !=None:
            self.inputs.fields.connect(fields)

    @staticmethod
    def _spec():
        spec = Specification(description="""Return the input field or fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "forward_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsForwardFieldsContainer 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsForwardFieldsContainer 
        """
        return super().outputs


#internal name: forward_fc
#scripting name: forward_fields_container
class InputsForwardFieldsContainer(_Inputs):
    """Intermediate class used to connect user inputs to forward_fields_container operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.forward_fields_container()
      >>> my_fields = dpf.FieldsContainer()
      >>> op.inputs.fields.connect(my_fields)
    """
    def __init__(self, op: Operator):
        super().__init__(forward_fields_container._spec().inputs, op)
        self._fields = Input(forward_fields_container._spec().input_pin(0), 0, op, -1) 
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

        >>> op = dpf.operators.utility.forward_fields_container()
        >>> op.inputs.fields.connect(my_fields)
        >>> #or
        >>> op.inputs.fields(my_fields)

        """
        return self._fields

class OutputsForwardFieldsContainer(_Outputs):
    """Intermediate class used to get outputs from forward_fields_container operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.forward_fields_container()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(forward_fields_container._spec().outputs, op)
        self._fields_container = Output(forward_fields_container._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.utility.forward_fields_container()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

