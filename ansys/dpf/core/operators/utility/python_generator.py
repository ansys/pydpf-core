"""
python_generator
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class python_generator(Operator):
    """Generates .py file with specifications for loaded plugin(s).

      available inputs:
        - dll_source_path (str)
        - output_path (str)

      available outputs:


      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.python_generator()

      >>> # Make input connections
      >>> my_dll_source_path = str()
      >>> op.inputs.dll_source_path.connect(my_dll_source_path)
      >>> my_output_path = str()
      >>> op.inputs.output_path.connect(my_output_path)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.python_generator(dll_source_path=my_dll_source_path,output_path=my_output_path)

      >>> # Get output data"""
    def __init__(self, dll_source_path=None, output_path=None, config=None, server=None):
        super().__init__(name="python_generator", config = config, server = server)
        self._inputs = InputsPythonGenerator(self)
        self._outputs = OutputsPythonGenerator(self)
        if dll_source_path !=None:
            self.inputs.dll_source_path.connect(dll_source_path)
        if output_path !=None:
            self.inputs.output_path.connect(output_path)

    @staticmethod
    def _spec():
        spec = Specification(description="""Generates .py file with specifications for loaded plugin(s).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "dll_source_path", type_names=["string"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "output_path", type_names=["string"], optional=False, document="""""")},
                             map_output_pin_spec={
})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "python_generator")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPythonGenerator 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPythonGenerator 
        """
        return super().outputs


#internal name: python_generator
#scripting name: python_generator
class InputsPythonGenerator(_Inputs):
    """Intermediate class used to connect user inputs to python_generator operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.python_generator()
      >>> my_dll_source_path = str()
      >>> op.inputs.dll_source_path.connect(my_dll_source_path)
      >>> my_output_path = str()
      >>> op.inputs.output_path.connect(my_output_path)
    """
    def __init__(self, op: Operator):
        super().__init__(python_generator._spec().inputs, op)
        self._dll_source_path = Input(python_generator._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._dll_source_path)
        self._output_path = Input(python_generator._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._output_path)

    @property
    def dll_source_path(self):
        """Allows to connect dll_source_path input to the operator

        Parameters
        ----------
        my_dll_source_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.python_generator()
        >>> op.inputs.dll_source_path.connect(my_dll_source_path)
        >>> #or
        >>> op.inputs.dll_source_path(my_dll_source_path)

        """
        return self._dll_source_path

    @property
    def output_path(self):
        """Allows to connect output_path input to the operator

        Parameters
        ----------
        my_output_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.python_generator()
        >>> op.inputs.output_path.connect(my_output_path)
        >>> #or
        >>> op.inputs.output_path(my_output_path)

        """
        return self._output_path

class OutputsPythonGenerator(_Outputs):
    """Intermediate class used to get outputs from python_generator operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.python_generator()
      >>> # Connect inputs : op.inputs. ...
    """
    def __init__(self, op: Operator):
        super().__init__(python_generator._spec().outputs, op)
        pass 

