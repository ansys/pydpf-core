"""
time_integration
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class time_integration(Operator):
    """
Computes the cumulative [integral](https://en.wikipedia.org/wiki/Integral) of a scalar
time-varying field using adaptive numerical integration.
The input field must have a time-frequency support that provides the time values.

When `resample_output` (pin 1) is true, the output time steps are resampled by the integrator
(producing a new time support); when false, the output reuses the input time support.
The optional integration constant (pin 4) is added to all output values as an initial condition.


      available inputs:
        - field (Field)
        - resample_output (bool) (optional)
        - absolute_error (float) (optional)
        - minimum_step_size (float) (optional)
        - integration_constant (float) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.time_integration()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_resample_output = bool()
      >>> op.inputs.resample_output.connect(my_resample_output)
      >>> my_absolute_error = float()
      >>> op.inputs.absolute_error.connect(my_absolute_error)
      >>> my_minimum_step_size = float()
      >>> op.inputs.minimum_step_size.connect(my_minimum_step_size)
      >>> my_integration_constant = float()
      >>> op.inputs.integration_constant.connect(my_integration_constant)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.time_integration(field=my_field,resample_output=my_resample_output,absolute_error=my_absolute_error,minimum_step_size=my_minimum_step_size,integration_constant=my_integration_constant)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, resample_output=None, absolute_error=None, minimum_step_size=None, integration_constant=None, config=None, server=None):
        super().__init__(name="TimeIntegration", config = config, server = server)
        self._inputs = InputsTimeIntegration(self)
        self._outputs = OutputsTimeIntegration(self)
        if field !=None:
            self.inputs.field.connect(field)
        if resample_output !=None:
            self.inputs.resample_output.connect(resample_output)
        if absolute_error !=None:
            self.inputs.absolute_error.connect(absolute_error)
        if minimum_step_size !=None:
            self.inputs.minimum_step_size.connect(minimum_step_size)
        if integration_constant !=None:
            self.inputs.integration_constant.connect(integration_constant)

    @staticmethod
    def _spec():
        spec = Specification(description="""
Computes the cumulative [integral](https://en.wikipedia.org/wiki/Integral) of a scalar
time-varying field using adaptive numerical integration.
The input field must have a time-frequency support that provides the time values.

When `resample_output` (pin 1) is true, the output time steps are resampled by the integrator
(producing a new time support); when false, the output reuses the input time support.
The optional integration constant (pin 4) is added to all output values as an initial condition.
""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""Scalar time-varying field to integrate. Must have a time-frequency support."""), 
                                 1 : PinSpecification(name = "resample_output", type_names=["bool"], optional=True, document="""When true, the output is resampled to an adaptively chosen set of time steps. When false (default), the output uses the same time support as the input."""), 
                                 2 : PinSpecification(name = "absolute_error", type_names=["double"], optional=True, document="""Absolute error tolerance for the resampling step. Only used when pin 1 is true."""), 
                                 3 : PinSpecification(name = "minimum_step_size", type_names=["double"], optional=True, document="""Minimum time step size allowed during resampling. Only used when pin 1 is true."""), 
                                 4 : PinSpecification(name = "integration_constant", type_names=["double"], optional=True, document="""Constant added to all integrated values as an initial condition. Default is $0$.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""Integrated scalar field. Has the same unit as (input unit $\times$ second). The time support is either the input support (when pin 1 is false) or a resampled support (when pin 1 is true).""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "TimeIntegration")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsTimeIntegration 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsTimeIntegration 
        """
        return super().outputs


#internal name: TimeIntegration
#scripting name: time_integration
class InputsTimeIntegration(_Inputs):
    """Intermediate class used to connect user inputs to time_integration operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.time_integration()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_resample_output = bool()
      >>> op.inputs.resample_output.connect(my_resample_output)
      >>> my_absolute_error = float()
      >>> op.inputs.absolute_error.connect(my_absolute_error)
      >>> my_minimum_step_size = float()
      >>> op.inputs.minimum_step_size.connect(my_minimum_step_size)
      >>> my_integration_constant = float()
      >>> op.inputs.integration_constant.connect(my_integration_constant)
    """
    def __init__(self, op: Operator):
        super().__init__(time_integration._spec().inputs, op)
        self._field = Input(time_integration._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._resample_output = Input(time_integration._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._resample_output)
        self._absolute_error = Input(time_integration._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._absolute_error)
        self._minimum_step_size = Input(time_integration._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._minimum_step_size)
        self._integration_constant = Input(time_integration._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._integration_constant)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: Scalar time-varying field to integrate. Must have a time-frequency support.

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.time_integration()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def resample_output(self):
        """Allows to connect resample_output input to the operator

        - pindoc: When true, the output is resampled to an adaptively chosen set of time steps. When false (default), the output uses the same time support as the input.

        Parameters
        ----------
        my_resample_output : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.time_integration()
        >>> op.inputs.resample_output.connect(my_resample_output)
        >>> #or
        >>> op.inputs.resample_output(my_resample_output)

        """
        return self._resample_output

    @property
    def absolute_error(self):
        """Allows to connect absolute_error input to the operator

        - pindoc: Absolute error tolerance for the resampling step. Only used when pin 1 is true.

        Parameters
        ----------
        my_absolute_error : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.time_integration()
        >>> op.inputs.absolute_error.connect(my_absolute_error)
        >>> #or
        >>> op.inputs.absolute_error(my_absolute_error)

        """
        return self._absolute_error

    @property
    def minimum_step_size(self):
        """Allows to connect minimum_step_size input to the operator

        - pindoc: Minimum time step size allowed during resampling. Only used when pin 1 is true.

        Parameters
        ----------
        my_minimum_step_size : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.time_integration()
        >>> op.inputs.minimum_step_size.connect(my_minimum_step_size)
        >>> #or
        >>> op.inputs.minimum_step_size(my_minimum_step_size)

        """
        return self._minimum_step_size

    @property
    def integration_constant(self):
        """Allows to connect integration_constant input to the operator

        - pindoc: Constant added to all integrated values as an initial condition. Default is $0$.

        Parameters
        ----------
        my_integration_constant : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.time_integration()
        >>> op.inputs.integration_constant.connect(my_integration_constant)
        >>> #or
        >>> op.inputs.integration_constant(my_integration_constant)

        """
        return self._integration_constant

class OutputsTimeIntegration(_Outputs):
    """Intermediate class used to get outputs from time_integration operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.time_integration()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(time_integration._spec().outputs, op)
        self._field = Output(time_integration._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        - pindoc: Integrated scalar field. Has the same unit as (input unit $\times$ second). The time support is either the input support (when pin 1 is false) or a resampled support (when pin 1 is true).

        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.time_integration()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

