"""
ln_fc
=====
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class ln_fc(Operator):
    """Computes element-wise ln(field[i]).

      available inputs:
        - fields_container (FieldsContainer)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.ln_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.ln_fc(fields_container=my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="ln_fc", config = config, server = server)
        self._inputs = InputsLnFc(self)
        self._outputs = OutputsLnFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise ln(field[i]).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ln_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsLnFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsLnFc 
        """
        return super().outputs


#internal name: ln_fc
#scripting name: ln_fc
class InputsLnFc(_Inputs):
    """Intermediate class used to connect user inputs to ln_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.ln_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
    """
    def __init__(self, op: Operator):
        super().__init__(ln_fc._spec().inputs, op)
        self._fields_container = Input(ln_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.ln_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

class OutputsLnFc(_Outputs):
    """Intermediate class used to get outputs from ln_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.ln_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(ln_fc._spec().outputs, op)
        self._fields_container = Output(ln_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.ln_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

