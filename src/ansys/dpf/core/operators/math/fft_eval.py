"""
fft_eval
========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class fft_eval(Operator):
    """
Reconstructs the time-domain signal from a complex FFT coefficients container.
For each complex coefficient at frequency $f_k$, evaluates the
[inverse Fourier series](https://en.wikipedia.org/wiki/Fourier_series):

$$f(t) = \sum_k \bigl(\mathrm{Re}[k]\,\cos(2\pi f_k t) + \mathrm{Im}[k]\,\sin(2\pi f_k t)\bigr)$$

The sum runs over all frequency set IDs in the input, or over the scoping from pin 1 when provided.
Only scalar fields (one component) are supported.


      available inputs:
        - fields_container (FieldsContainer)
        - time_scoping (Scoping) (optional)
        - field_t (Field)

      available outputs:
        - field (Field)
        - offset (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.fft_eval()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_field_t = dpf.Field()
      >>> op.inputs.field_t.connect(my_field_t)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.fft_eval(fields_container=my_fields_container,time_scoping=my_time_scoping,field_t=my_field_t)

      >>> # Get output data
      >>> result_field = op.outputs.field()
      >>> result_offset = op.outputs.offset()"""
    def __init__(self, fields_container=None, time_scoping=None, field_t=None, config=None, server=None):
        super().__init__(name="fft_eval", config = config, server = server)
        self._inputs = InputsFftEval(self)
        self._outputs = OutputsFftEval(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if field_t !=None:
            self.inputs.field_t.connect(field_t)

    @staticmethod
    def _spec():
        spec = Specification(description="""
Reconstructs the time-domain signal from a complex FFT coefficients container.
For each complex coefficient at frequency $f_k$, evaluates the
[inverse Fourier series](https://en.wikipedia.org/wiki/Fourier_series):

$$f(t) = \sum_k \bigl(\mathrm{Re}[k]\,\cos(2\pi f_k t) + \mathrm{Im}[k]\,\sin(2\pi f_k t)\bigr)$$

The sum runs over all frequency set IDs in the input, or over the scoping from pin 1 when provided.
Only scalar fields (one component) are supported.
""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""Complex FFT coefficients container, as produced by the `fft` operator. Must have a complex label and a frequency-valued time-frequency support."""), 
                                 1 : PinSpecification(name = "time_scoping", type_names=["scoping"], optional=True, document="""Frequency scoping. When provided, only the selected frequency set IDs contribute to the reconstruction. When omitted, all set IDs are used."""), 
                                 2 : PinSpecification(name = "field_t", type_names=["field"], optional=False, document="""Field of time values at which to evaluate the reconstructed signal. The output contains one entity per entry in this field.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""Reconstructed time-domain fields container. One output field per input label combination (excluding the complex label), each evaluated at the time values from pin 2."""), 
                                 2 : PinSpecification(name = "offset", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "fft_eval")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsFftEval 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsFftEval 
        """
        return super().outputs


#internal name: fft_eval
#scripting name: fft_eval
class InputsFftEval(_Inputs):
    """Intermediate class used to connect user inputs to fft_eval operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.fft_eval()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_field_t = dpf.Field()
      >>> op.inputs.field_t.connect(my_field_t)
    """
    def __init__(self, op: Operator):
        super().__init__(fft_eval._spec().inputs, op)
        self._fields_container = Input(fft_eval._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._time_scoping = Input(fft_eval._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._time_scoping)
        self._field_t = Input(fft_eval._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._field_t)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: Complex FFT coefficients container, as produced by the `fft` operator. Must have a complex label and a frequency-valued time-frequency support.

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_eval()
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

        >>> op = dpf.operators.math.fft_eval()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def field_t(self):
        """Allows to connect field_t input to the operator

        - pindoc: Field of time values at which to evaluate the reconstructed signal. The output contains one entity per entry in this field.

        Parameters
        ----------
        my_field_t : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_eval()
        >>> op.inputs.field_t.connect(my_field_t)
        >>> #or
        >>> op.inputs.field_t(my_field_t)

        """
        return self._field_t

class OutputsFftEval(_Outputs):
    """Intermediate class used to get outputs from fft_eval operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.fft_eval()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
      >>> result_offset = op.outputs.offset()
    """
    def __init__(self, op: Operator):
        super().__init__(fft_eval._spec().outputs, op)
        self._field = Output(fft_eval._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)
        self._offset = Output(fft_eval._spec().output_pin(2), 2, op) 
        self._outputs.append(self._offset)

    @property
    def field(self):
        """Allows to get field output of the operator


        - pindoc: Reconstructed time-domain fields container. One output field per input label combination (excluding the complex label), each evaluated at the time values from pin 2.

        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_eval()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

    @property
    def offset(self):
        """Allows to get offset output of the operator


        Returns
        ----------
        my_offset : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_eval()
        >>> # Connect inputs : op.inputs. ...
        >>> result_offset = op.outputs.offset() 
        """
        return self._offset

