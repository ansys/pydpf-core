"""
time_derivation
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class time_derivation(Operator):
    """
Computes the time [derivative](https://en.wikipedia.org/wiki/Derivative) of a scalar
time-varying field.
The input field must have a time-frequency support that provides the time values.

When `spline_fitting` (pin 1) is true, the derivative is computed from a
[cubic spline](https://en.wikipedia.org/wiki/Cubic_spline) fit through the input data,
producing smooth derivatives. When false (default), finite differences are used.


      available inputs:
        - field (Field)
        - spline_fitting (bool) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.time_derivation()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_spline_fitting = bool()
      >>> op.inputs.spline_fitting.connect(my_spline_fitting)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.time_derivation(field=my_field,spline_fitting=my_spline_fitting)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, spline_fitting=None, config=None, server=None):
        super().__init__(name="TimeDerivation", config = config, server = server)
        self._inputs = InputsTimeDerivation(self)
        self._outputs = OutputsTimeDerivation(self)
        if field !=None:
            self.inputs.field.connect(field)
        if spline_fitting !=None:
            self.inputs.spline_fitting.connect(spline_fitting)

    @staticmethod
    def _spec():
        spec = Specification(description="""
Computes the time [derivative](https://en.wikipedia.org/wiki/Derivative) of a scalar
time-varying field.
The input field must have a time-frequency support that provides the time values.

When `spline_fitting` (pin 1) is true, the derivative is computed from a
[cubic spline](https://en.wikipedia.org/wiki/Cubic_spline) fit through the input data,
producing smooth derivatives. When false (default), finite differences are used.
""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""Scalar time-varying field to differentiate. Must have a time-frequency support."""), 
                                 1 : PinSpecification(name = "spline_fitting", type_names=["bool"], optional=True, document="""When true, fits a cubic spline to the input data and computes the derivative analytically from the spline. When false (default), uses finite differences.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""Time derivative field. Has the same time support and scoping as the input. Unit is (input unit / second).""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "TimeDerivation")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsTimeDerivation 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsTimeDerivation 
        """
        return super().outputs


#internal name: TimeDerivation
#scripting name: time_derivation
class InputsTimeDerivation(_Inputs):
    """Intermediate class used to connect user inputs to time_derivation operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.time_derivation()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_spline_fitting = bool()
      >>> op.inputs.spline_fitting.connect(my_spline_fitting)
    """
    def __init__(self, op: Operator):
        super().__init__(time_derivation._spec().inputs, op)
        self._field = Input(time_derivation._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._spline_fitting = Input(time_derivation._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._spline_fitting)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: Scalar time-varying field to differentiate. Must have a time-frequency support.

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.time_derivation()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def spline_fitting(self):
        """Allows to connect spline_fitting input to the operator

        - pindoc: When true, fits a cubic spline to the input data and computes the derivative analytically from the spline. When false (default), uses finite differences.

        Parameters
        ----------
        my_spline_fitting : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.time_derivation()
        >>> op.inputs.spline_fitting.connect(my_spline_fitting)
        >>> #or
        >>> op.inputs.spline_fitting(my_spline_fitting)

        """
        return self._spline_fitting

class OutputsTimeDerivation(_Outputs):
    """Intermediate class used to get outputs from time_derivation operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.time_derivation()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(time_derivation._spec().outputs, op)
        self._field = Output(time_derivation._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        - pindoc: Time derivative field. Has the same time support and scoping as the input. Unit is (input unit / second).

        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.time_derivation()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

