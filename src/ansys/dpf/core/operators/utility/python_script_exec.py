"""
python_script_exec
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class python_script_exec(Operator):
    """Execute python input script.

      available inputs:
        - python_script (str)

      available outputs:
        - output ()

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.python_script_exec()

      >>> # Make input connections
      >>> my_python_script = str()
      >>> op.inputs.python_script.connect(my_python_script)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.python_script_exec(python_script=my_python_script)

      >>> # Get output data
      >>> result_output = op.outputs.output()"""
    def __init__(self, python_script=None, config=None, server=None):
        super().__init__(name="utility::python_script_exec", config = config, server = server)
        self._inputs = InputsPythonScriptExec(self)
        self._outputs = OutputsPythonScriptExec(self)
        if python_script !=None:
            self.inputs.python_script.connect(python_script)

    @staticmethod
    def _spec():
        spec = Specification(description="""Execute python input script.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "python_script", type_names=["string"], optional=False, document="""Input python script""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "output", type_names=[], optional=False, document="""The output can be of any supported type""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "utility::python_script_exec")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPythonScriptExec 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPythonScriptExec 
        """
        return super().outputs


#internal name: utility::python_script_exec
#scripting name: python_script_exec
class InputsPythonScriptExec(_Inputs):
    """Intermediate class used to connect user inputs to python_script_exec operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.python_script_exec()
      >>> my_python_script = str()
      >>> op.inputs.python_script.connect(my_python_script)
    """
    def __init__(self, op: Operator):
        super().__init__(python_script_exec._spec().inputs, op)
        self._python_script = Input(python_script_exec._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._python_script)

    @property
    def python_script(self):
        """Allows to connect python_script input to the operator

        - pindoc: Input python script

        Parameters
        ----------
        my_python_script : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.python_script_exec()
        >>> op.inputs.python_script.connect(my_python_script)
        >>> #or
        >>> op.inputs.python_script(my_python_script)

        """
        return self._python_script

class OutputsPythonScriptExec(_Outputs):
    """Intermediate class used to get outputs from python_script_exec operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.python_script_exec()
      >>> # Connect inputs : op.inputs. ...
    """
    def __init__(self, op: Operator):
        super().__init__(python_script_exec._spec().outputs, op)
        pass 

