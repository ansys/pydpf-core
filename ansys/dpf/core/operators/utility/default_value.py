"""
default_value
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class default_value(Operator):
    """default return value from input pin 1 to output pin 0 if there is nothing on input pin 0.

      available inputs:
        - forced_value (Any) (optional)
        - default_value (Any)

      available outputs:
        - output ()

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.default_value()

      >>> # Make input connections
      >>> my_forced_value = dpf.Any()
      >>> op.inputs.forced_value.connect(my_forced_value)
      >>> my_default_value = dpf.Any()
      >>> op.inputs.default_value.connect(my_default_value)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.default_value(forced_value=my_forced_value,default_value=my_default_value)

      >>> # Get output data
      >>> result_output = op.outputs.output()"""
    def __init__(self, forced_value=None, default_value=None, config=None, server=None):
        super().__init__(name="default_value", config = config, server = server)
        self._inputs = InputsDefaultValue(self)
        self._outputs = OutputsDefaultValue(self)
        if forced_value !=None:
            self.inputs.forced_value.connect(forced_value)
        if default_value !=None:
            self.inputs.default_value.connect(default_value)

    @staticmethod
    def _spec():
        spec = Specification(description="""default return value from input pin 1 to output pin 0 if there is nothing on input pin 0.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "forced_value", type_names=["any"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "default_value", type_names=["any"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "output", type_names=[], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "default_value")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsDefaultValue 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsDefaultValue 
        """
        return super().outputs


#internal name: default_value
#scripting name: default_value
class InputsDefaultValue(_Inputs):
    """Intermediate class used to connect user inputs to default_value operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.default_value()
      >>> my_forced_value = dpf.Any()
      >>> op.inputs.forced_value.connect(my_forced_value)
      >>> my_default_value = dpf.Any()
      >>> op.inputs.default_value.connect(my_default_value)
    """
    def __init__(self, op: Operator):
        super().__init__(default_value._spec().inputs, op)
        self._forced_value = Input(default_value._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._forced_value)
        self._default_value = Input(default_value._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._default_value)

    @property
    def forced_value(self):
        """Allows to connect forced_value input to the operator

        Parameters
        ----------
        my_forced_value : Any, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.default_value()
        >>> op.inputs.forced_value.connect(my_forced_value)
        >>> #or
        >>> op.inputs.forced_value(my_forced_value)

        """
        return self._forced_value

    @property
    def default_value(self):
        """Allows to connect default_value input to the operator

        Parameters
        ----------
        my_default_value : Any, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.default_value()
        >>> op.inputs.default_value.connect(my_default_value)
        >>> #or
        >>> op.inputs.default_value(my_default_value)

        """
        return self._default_value

class OutputsDefaultValue(_Outputs):
    """Intermediate class used to get outputs from default_value operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.default_value()
      >>> # Connect inputs : op.inputs. ...
    """
    def __init__(self, op: Operator):
        super().__init__(default_value._spec().outputs, op)
        pass 

