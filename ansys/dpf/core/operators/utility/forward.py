"""
forward
=======
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class forward(Operator):
    """Return all the inputs as outputs.

      available inputs:
        - any (Any)

      available outputs:
        - any ()

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.forward()

      >>> # Make input connections
      >>> my_any = dpf.Any()
      >>> op.inputs.any.connect(my_any)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.forward(any=my_any)

      >>> # Get output data
      >>> result_any = op.outputs.any()"""
    def __init__(self, any=None, config=None, server=None):
        super().__init__(name="forward", config = config, server = server)
        self._inputs = InputsForward(self)
        self._outputs = OutputsForward(self)
        if any !=None:
            self.inputs.any.connect(any)

    @staticmethod
    def _spec():
        spec = Specification(description="""Return all the inputs as outputs.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "any", type_names=["any"], optional=False, document="""any type of input""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "any", type_names=[], optional=False, document="""same types as inputs""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "forward")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsForward 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsForward 
        """
        return super().outputs


#internal name: forward
#scripting name: forward
class InputsForward(_Inputs):
    """Intermediate class used to connect user inputs to forward operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.forward()
      >>> my_any = dpf.Any()
      >>> op.inputs.any.connect(my_any)
    """
    def __init__(self, op: Operator):
        super().__init__(forward._spec().inputs, op)
        self._any = Input(forward._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._any)

    @property
    def any(self):
        """Allows to connect any input to the operator

        - pindoc: any type of input

        Parameters
        ----------
        my_any : Any, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.forward()
        >>> op.inputs.any.connect(my_any)
        >>> #or
        >>> op.inputs.any(my_any)

        """
        return self._any

class OutputsForward(_Outputs):
    """Intermediate class used to get outputs from forward operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.forward()
      >>> # Connect inputs : op.inputs. ...
    """
    def __init__(self, op: Operator):
        super().__init__(forward._spec().outputs, op)
        pass 

