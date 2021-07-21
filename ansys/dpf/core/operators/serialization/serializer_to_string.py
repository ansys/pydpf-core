"""
serializer_to_string
====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "serialization" category
"""

class serializer_to_string(Operator):
    """Take any input and serialize them in a string.

      available inputs:
        - any_input1 (Any)
        - any_input2 (Any)

      available outputs:
        - serialized_string (str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.serialization.serializer_to_string()

      >>> # Make input connections
      >>> my_any_input1 = dpf.Any()
      >>> op.inputs.any_input1.connect(my_any_input1)
      >>> my_any_input2 = dpf.Any()
      >>> op.inputs.any_input2.connect(my_any_input2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.serialization.serializer_to_string(any_input1=my_any_input1,any_input2=my_any_input2)

      >>> # Get output data
      >>> result_serialized_string = op.outputs.serialized_string()"""
    def __init__(self, any_input1=None, any_input2=None, config=None, server=None):
        super().__init__(name="serializer_to_string", config = config, server = server)
        self._inputs = InputsSerializerToString(self)
        self._outputs = OutputsSerializerToString(self)
        if any_input1 !=None:
            self.inputs.any_input1.connect(any_input1)
        if any_input2 !=None:
            self.inputs.any_input2.connect(any_input2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take any input and serialize them in a string.""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "any_input", type_names=["any"], optional=False, document="""any input"""), 
                                 2 : PinSpecification(name = "any_input", type_names=["any"], optional=False, document="""any input""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "serialized_string", type_names=["string"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "serializer_to_string")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSerializerToString 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSerializerToString 
        """
        return super().outputs


#internal name: serializer_to_string
#scripting name: serializer_to_string
class InputsSerializerToString(_Inputs):
    """Intermediate class used to connect user inputs to serializer_to_string operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.serializer_to_string()
      >>> my_any_input1 = dpf.Any()
      >>> op.inputs.any_input1.connect(my_any_input1)
      >>> my_any_input2 = dpf.Any()
      >>> op.inputs.any_input2.connect(my_any_input2)
    """
    def __init__(self, op: Operator):
        super().__init__(serializer_to_string._spec().inputs, op)
        self._any_input1 = Input(serializer_to_string._spec().input_pin(1), 1, op, 0) 
        self._inputs.append(self._any_input1)
        self._any_input2 = Input(serializer_to_string._spec().input_pin(2), 2, op, 1) 
        self._inputs.append(self._any_input2)

    @property
    def any_input1(self):
        """Allows to connect any_input1 input to the operator

        - pindoc: any input

        Parameters
        ----------
        my_any_input1 : Any, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.serializer_to_string()
        >>> op.inputs.any_input1.connect(my_any_input1)
        >>> #or
        >>> op.inputs.any_input1(my_any_input1)

        """
        return self._any_input1

    @property
    def any_input2(self):
        """Allows to connect any_input2 input to the operator

        - pindoc: any input

        Parameters
        ----------
        my_any_input2 : Any, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.serializer_to_string()
        >>> op.inputs.any_input2.connect(my_any_input2)
        >>> #or
        >>> op.inputs.any_input2(my_any_input2)

        """
        return self._any_input2

class OutputsSerializerToString(_Outputs):
    """Intermediate class used to get outputs from serializer_to_string operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.serializer_to_string()
      >>> # Connect inputs : op.inputs. ...
      >>> result_serialized_string = op.outputs.serialized_string()
    """
    def __init__(self, op: Operator):
        super().__init__(serializer_to_string._spec().outputs, op)
        self._serialized_string = Output(serializer_to_string._spec().output_pin(0), 0, op) 
        self._outputs.append(self._serialized_string)

    @property
    def serialized_string(self):
        """Allows to get serialized_string output of the operator


        Returns
        ----------
        my_serialized_string : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.serializer_to_string()
        >>> # Connect inputs : op.inputs. ...
        >>> result_serialized_string = op.outputs.serialized_string() 
        """
        return self._serialized_string

