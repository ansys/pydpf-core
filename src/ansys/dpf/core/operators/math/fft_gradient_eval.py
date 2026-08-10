"""
fft_gradient_eval
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class fft_gradient_eval(Operator):
    """
Reconstitutes the time-domain signal from a complex FFT coefficients container and
finds its minimum and maximum using an adaptive time-step gradient method.
For each harmonic component at frequency $f_k$, the signal is:

$$F(t) = \sum_k A_k \sin(2\pi f_k t - \phi_k + \tfrac{\pi}{2})$$

where $A_k$ and $\phi_k$ are the amplitude and phase derived from the complex FFT coefficients.
The adaptive stepping enlarges the time step when the signal is far from a candidate extremum
(controlled by the oversampling ratio from pin 2), and refines near the extremum.
Only scalar fields are supported.


      available inputs:
        - fields_container (FieldsContainer)
        - time_scoping (Scoping) (optional)
        - fs_ratio (int) (optional)

      available outputs:
        - coefficients (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.fft_gradient_eval()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_fs_ratio = int()
      >>> op.inputs.fs_ratio.connect(my_fs_ratio)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.fft_gradient_eval(fields_container=my_fields_container,time_scoping=my_time_scoping,fs_ratio=my_fs_ratio)

      >>> # Get output data
      >>> result_coefficients = op.outputs.coefficients()"""
    def __init__(self, fields_container=None, time_scoping=None, fs_ratio=None, config=None, server=None):
        super().__init__(name="fft_eval_gr", config = config, server = server)
        self._inputs = InputsFftGradientEval(self)
        self._outputs = OutputsFftGradientEval(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if fs_ratio !=None:
            self.inputs.fs_ratio.connect(fs_ratio)

    @staticmethod
    def _spec():
        spec = Specification(description="""
Reconstitutes the time-domain signal from a complex FFT coefficients container and
finds its minimum and maximum using an adaptive time-step gradient method.
For each harmonic component at frequency $f_k$, the signal is:

$$F(t) = \sum_k A_k \sin(2\pi f_k t - \phi_k + \tfrac{\pi}{2})$$

where $A_k$ and $\phi_k$ are the amplitude and phase derived from the complex FFT coefficients.
The adaptive stepping enlarges the time step when the signal is far from a candidate extremum
(controlled by the oversampling ratio from pin 2), and refines near the extremum.
Only scalar fields are supported.
""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""Complex FFT coefficients container, as produced by the `fft` operator. Must have a complex label and a frequency-valued time-frequency support. Only scalar fields are supported."""), 
                                 1 : PinSpecification(name = "time_scoping", type_names=["scoping"], optional=True, document="""Frequency scoping. When provided, only the selected frequency set IDs contribute to the reconstruction. When omitted, all set IDs are used."""), 
                                 2 : PinSpecification(name = "fs_ratio", type_names=["int32"], optional=True, document="""Oversampling ratio used to set the base time step as $1/(f_{max} \times \mathit{fs_ratio})$. Default is $20$.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "coefficients", type_names=["fields_container"], optional=False, document="""Time-domain fields container evaluated at the adaptive time steps. One output field per input label combination (excluding the complex label).""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "fft_eval_gr")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsFftGradientEval 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsFftGradientEval 
        """
        return super().outputs


#internal name: fft_eval_gr
#scripting name: fft_gradient_eval
class InputsFftGradientEval(_Inputs):
    """Intermediate class used to connect user inputs to fft_gradient_eval operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.fft_gradient_eval()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_fs_ratio = int()
      >>> op.inputs.fs_ratio.connect(my_fs_ratio)
    """
    def __init__(self, op: Operator):
        super().__init__(fft_gradient_eval._spec().inputs, op)
        self._fields_container = Input(fft_gradient_eval._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._time_scoping = Input(fft_gradient_eval._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._time_scoping)
        self._fs_ratio = Input(fft_gradient_eval._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._fs_ratio)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: Complex FFT coefficients container, as produced by the `fft` operator. Must have a complex label and a frequency-valued time-frequency support. Only scalar fields are supported.

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_gradient_eval()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        - pindoc: Frequency scoping. When provided, only the selected frequency set IDs contribute to the reconstruction. When omitted, all set IDs are used.

        Parameters
        ----------
        my_time_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_gradient_eval()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def fs_ratio(self):
        """Allows to connect fs_ratio input to the operator

        - pindoc: Oversampling ratio used to set the base time step as $1/(f_{max} \times \mathit{fs_ratio})$. Default is $20$.

        Parameters
        ----------
        my_fs_ratio : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_gradient_eval()
        >>> op.inputs.fs_ratio.connect(my_fs_ratio)
        >>> #or
        >>> op.inputs.fs_ratio(my_fs_ratio)

        """
        return self._fs_ratio

class OutputsFftGradientEval(_Outputs):
    """Intermediate class used to get outputs from fft_gradient_eval operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.fft_gradient_eval()
      >>> # Connect inputs : op.inputs. ...
      >>> result_coefficients = op.outputs.coefficients()
    """
    def __init__(self, op: Operator):
        super().__init__(fft_gradient_eval._spec().outputs, op)
        self._coefficients = Output(fft_gradient_eval._spec().output_pin(0), 0, op) 
        self._outputs.append(self._coefficients)

    @property
    def coefficients(self):
        """Allows to get coefficients output of the operator


        - pindoc: Time-domain fields container evaluated at the adaptive time steps. One output field per input label combination (excluding the complex label).

        Returns
        ----------
        my_coefficients : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_gradient_eval()
        >>> # Connect inputs : op.inputs. ...
        >>> result_coefficients = op.outputs.coefficients() 
        """
        return self._coefficients

