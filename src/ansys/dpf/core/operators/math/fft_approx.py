"""
fft_approx
==========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class fft_approx(Operator):
    """
Computes a frequency-filtered smooth curve fitting using the
[Fast Fourier Transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
and cubic spline interpolation, operating along the time axis for each spatial entity.
For each entity (node i), the time-series $y(t)$ is fitted; the FFT filter removes
frequency components above the cutoff frequency (pin 7), and the cubic spline reconstructs
the filtered signal at the original time steps.
First and second time derivatives of the fitted curve are available at output pins 1 and 2.


      available inputs:
        - time_scoping (list, Scoping) (optional)
        - mesh_scoping (Scoping, ScopingsContainer) (optional)
        - entity_to_fit (FieldsContainer)
        - component_number (int)
        - first_derivative (bool) (optional)
        - second_derivative (bool) (optional)
        - fit_data (bool) (optional)
        - cutoff_fr (float, int) (optional)

      available outputs:
        - fitted_entity_y (FieldsContainer)
        - first_der_dy (FieldsContainer)
        - second_der_d2y (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.fft_approx()

      >>> # Make input connections
      >>> my_time_scoping = dpf.list()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_entity_to_fit = dpf.FieldsContainer()
      >>> op.inputs.entity_to_fit.connect(my_entity_to_fit)
      >>> my_component_number = int()
      >>> op.inputs.component_number.connect(my_component_number)
      >>> my_first_derivative = bool()
      >>> op.inputs.first_derivative.connect(my_first_derivative)
      >>> my_second_derivative = bool()
      >>> op.inputs.second_derivative.connect(my_second_derivative)
      >>> my_fit_data = bool()
      >>> op.inputs.fit_data.connect(my_fit_data)
      >>> my_cutoff_fr = float()
      >>> op.inputs.cutoff_fr.connect(my_cutoff_fr)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.fft_approx(time_scoping=my_time_scoping,mesh_scoping=my_mesh_scoping,entity_to_fit=my_entity_to_fit,component_number=my_component_number,first_derivative=my_first_derivative,second_derivative=my_second_derivative,fit_data=my_fit_data,cutoff_fr=my_cutoff_fr)

      >>> # Get output data
      >>> result_fitted_entity_y = op.outputs.fitted_entity_y()
      >>> result_first_der_dy = op.outputs.first_der_dy()
      >>> result_second_der_d2y = op.outputs.second_der_d2y()"""
    def __init__(self, time_scoping=None, mesh_scoping=None, entity_to_fit=None, component_number=None, first_derivative=None, second_derivative=None, fit_data=None, cutoff_fr=None, config=None, server=None):
        super().__init__(name="fft_approx", config = config, server = server)
        self._inputs = InputsFftApprox(self)
        self._outputs = OutputsFftApprox(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if entity_to_fit !=None:
            self.inputs.entity_to_fit.connect(entity_to_fit)
        if component_number !=None:
            self.inputs.component_number.connect(component_number)
        if first_derivative !=None:
            self.inputs.first_derivative.connect(first_derivative)
        if second_derivative !=None:
            self.inputs.second_derivative.connect(second_derivative)
        if fit_data !=None:
            self.inputs.fit_data.connect(fit_data)
        if cutoff_fr !=None:
            self.inputs.cutoff_fr.connect(cutoff_fr)

    @staticmethod
    def _spec():
        spec = Specification(description="""
Computes a frequency-filtered smooth curve fitting using the
[Fast Fourier Transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
and cubic spline interpolation, operating along the time axis for each spatial entity.
For each entity (node i), the time-series $y(t)$ is fitted; the FFT filter removes
frequency components above the cutoff frequency (pin 7), and the cubic spline reconstructs
the filtered signal at the original time steps.
First and second time derivatives of the fitted curve are available at output pins 1 and 2.
""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["vector<int32>","scoping"], optional=True, document="""Time scoping to select which time steps are used as input. When omitted, all time steps in the fields container are used."""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping","scopings_container"], optional=True, document="""Spatial scoping to restrict which entities are processed. When omitted, all entities in the fields container are processed."""), 
                                 2 : PinSpecification(name = "entity_to_fit", type_names=["fields_container"], optional=False, document="""Time-varying fields container to fit. Nodal and elemental locations are supported (elemental-nodal inputs are averaged to elemental)."""), 
                                 3 : PinSpecification(name = "component_number", type_names=["int32"], optional=False, document="""Zero-based index of the component to fit. For example, $0$ for the X-component, $1$ for Y, and so on. Required when the input has more than one component."""), 
                                 4 : PinSpecification(name = "first_derivative", type_names=["bool"], optional=True, document="""When true, computes the first time derivative of the fitted curve at output pin 1. Default is false."""), 
                                 5 : PinSpecification(name = "second_derivative", type_names=["bool"], optional=True, document="""When true, computes the second time derivative of the fitted curve at output pin 2. Default is false."""), 
                                 6 : PinSpecification(name = "fit_data", type_names=["bool"], optional=True, document="""When true, computes the fitted values at output pin 0. Default is false."""), 
                                 7 : PinSpecification(name = "cutoff_fr", type_names=["double","int32"], optional=True, document="""Cutoff frequency for the FFT filter. Harmonics above this frequency are removed before spline fitting. Default is $10$.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fitted_entity_y", type_names=["fields_container"], optional=False, document="""Fitted time-series fields container. Only produced when pin 6 is true. Same spatial and time layout as the input."""), 
                                 1 : PinSpecification(name = "first_der_dy", type_names=["fields_container"], optional=False, document="""First time derivative $\mathrm{d}y/\mathrm{d}t$ of the fitted curve. Only produced when pin 4 is true. Same layout as pin 0."""), 
                                 2 : PinSpecification(name = "second_der_d2y", type_names=["fields_container"], optional=False, document="""Second time derivative $\mathrm{d}^2y/\mathrm{d}t^2$ of the fitted curve. Only produced when pin 5 is true. Same layout as pin 0.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "fft_approx")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsFftApprox 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsFftApprox 
        """
        return super().outputs


#internal name: fft_approx
#scripting name: fft_approx
class InputsFftApprox(_Inputs):
    """Intermediate class used to connect user inputs to fft_approx operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.fft_approx()
      >>> my_time_scoping = dpf.list()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_entity_to_fit = dpf.FieldsContainer()
      >>> op.inputs.entity_to_fit.connect(my_entity_to_fit)
      >>> my_component_number = int()
      >>> op.inputs.component_number.connect(my_component_number)
      >>> my_first_derivative = bool()
      >>> op.inputs.first_derivative.connect(my_first_derivative)
      >>> my_second_derivative = bool()
      >>> op.inputs.second_derivative.connect(my_second_derivative)
      >>> my_fit_data = bool()
      >>> op.inputs.fit_data.connect(my_fit_data)
      >>> my_cutoff_fr = float()
      >>> op.inputs.cutoff_fr.connect(my_cutoff_fr)
    """
    def __init__(self, op: Operator):
        super().__init__(fft_approx._spec().inputs, op)
        self._time_scoping = Input(fft_approx._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(fft_approx._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._entity_to_fit = Input(fft_approx._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._entity_to_fit)
        self._component_number = Input(fft_approx._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._component_number)
        self._first_derivative = Input(fft_approx._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._first_derivative)
        self._second_derivative = Input(fft_approx._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._second_derivative)
        self._fit_data = Input(fft_approx._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self._fit_data)
        self._cutoff_fr = Input(fft_approx._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._cutoff_fr)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        - pindoc: Time scoping to select which time steps are used as input. When omitted, all time steps in the fields container are used.

        Parameters
        ----------
        my_time_scoping : list, Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        - pindoc: Spatial scoping to restrict which entities are processed. When omitted, all entities in the fields container are processed.

        Parameters
        ----------
        my_mesh_scoping : Scoping, ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def entity_to_fit(self):
        """Allows to connect entity_to_fit input to the operator

        - pindoc: Time-varying fields container to fit. Nodal and elemental locations are supported (elemental-nodal inputs are averaged to elemental).

        Parameters
        ----------
        my_entity_to_fit : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.entity_to_fit.connect(my_entity_to_fit)
        >>> #or
        >>> op.inputs.entity_to_fit(my_entity_to_fit)

        """
        return self._entity_to_fit

    @property
    def component_number(self):
        """Allows to connect component_number input to the operator

        - pindoc: Zero-based index of the component to fit. For example, $0$ for the X-component, $1$ for Y, and so on. Required when the input has more than one component.

        Parameters
        ----------
        my_component_number : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.component_number.connect(my_component_number)
        >>> #or
        >>> op.inputs.component_number(my_component_number)

        """
        return self._component_number

    @property
    def first_derivative(self):
        """Allows to connect first_derivative input to the operator

        - pindoc: When true, computes the first time derivative of the fitted curve at output pin 1. Default is false.

        Parameters
        ----------
        my_first_derivative : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.first_derivative.connect(my_first_derivative)
        >>> #or
        >>> op.inputs.first_derivative(my_first_derivative)

        """
        return self._first_derivative

    @property
    def second_derivative(self):
        """Allows to connect second_derivative input to the operator

        - pindoc: When true, computes the second time derivative of the fitted curve at output pin 2. Default is false.

        Parameters
        ----------
        my_second_derivative : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.second_derivative.connect(my_second_derivative)
        >>> #or
        >>> op.inputs.second_derivative(my_second_derivative)

        """
        return self._second_derivative

    @property
    def fit_data(self):
        """Allows to connect fit_data input to the operator

        - pindoc: When true, computes the fitted values at output pin 0. Default is false.

        Parameters
        ----------
        my_fit_data : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.fit_data.connect(my_fit_data)
        >>> #or
        >>> op.inputs.fit_data(my_fit_data)

        """
        return self._fit_data

    @property
    def cutoff_fr(self):
        """Allows to connect cutoff_fr input to the operator

        - pindoc: Cutoff frequency for the FFT filter. Harmonics above this frequency are removed before spline fitting. Default is $10$.

        Parameters
        ----------
        my_cutoff_fr : float, int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.cutoff_fr.connect(my_cutoff_fr)
        >>> #or
        >>> op.inputs.cutoff_fr(my_cutoff_fr)

        """
        return self._cutoff_fr

class OutputsFftApprox(_Outputs):
    """Intermediate class used to get outputs from fft_approx operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.fft_approx()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fitted_entity_y = op.outputs.fitted_entity_y()
      >>> result_first_der_dy = op.outputs.first_der_dy()
      >>> result_second_der_d2y = op.outputs.second_der_d2y()
    """
    def __init__(self, op: Operator):
        super().__init__(fft_approx._spec().outputs, op)
        self._fitted_entity_y = Output(fft_approx._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fitted_entity_y)
        self._first_der_dy = Output(fft_approx._spec().output_pin(1), 1, op) 
        self._outputs.append(self._first_der_dy)
        self._second_der_d2y = Output(fft_approx._spec().output_pin(2), 2, op) 
        self._outputs.append(self._second_der_d2y)

    @property
    def fitted_entity_y(self):
        """Allows to get fitted_entity_y output of the operator


        - pindoc: Fitted time-series fields container. Only produced when pin 6 is true. Same spatial and time layout as the input.

        Returns
        ----------
        my_fitted_entity_y : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fitted_entity_y = op.outputs.fitted_entity_y() 
        """
        return self._fitted_entity_y

    @property
    def first_der_dy(self):
        """Allows to get first_der_dy output of the operator


        - pindoc: First time derivative $\mathrm{d}y/\mathrm{d}t$ of the fitted curve. Only produced when pin 4 is true. Same layout as pin 0.

        Returns
        ----------
        my_first_der_dy : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> # Connect inputs : op.inputs. ...
        >>> result_first_der_dy = op.outputs.first_der_dy() 
        """
        return self._first_der_dy

    @property
    def second_der_d2y(self):
        """Allows to get second_der_d2y output of the operator


        - pindoc: Second time derivative $\mathrm{d}^2y/\mathrm{d}t^2$ of the fitted curve. Only produced when pin 5 is true. Same layout as pin 0.

        Returns
        ----------
        my_second_der_d2y : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_approx()
        >>> # Connect inputs : op.inputs. ...
        >>> result_second_der_d2y = op.outputs.second_der_d2y() 
        """
        return self._second_der_d2y

