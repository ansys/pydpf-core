"""
fft_multi_harmonic_minmax
=========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class fft_multi_harmonic_minmax(Operator):
    """
Finds the minimum and maximum of a multi-harmonic field over one period using an adaptive time-stepping
gradient method. The field is expressed as a [Fourier series](https://en.wikipedia.org/wiki/Fourier_series)
over harmonic orders corresponding to integer multiples of the operating speed (RPMs).
For each spatial entity, the series is evaluated at adaptively chosen time instants over one period
and the pointwise minimum and maximum are extracted.

ElementalNodal locations are not supported.


      available inputs:
        - fields_container (FieldsContainer)
        - rpm_scoping (Scoping) (optional)
        - fs_ratio (int) (optional)
        - num_subdivisions (int) (optional)
        - max_num_subdivisions (int) (optional)
        - num_cycles (int) (optional)
        - use_harmonic_zero (bool) (optional)
        - calculate_time_series (bool) (optional)
        - substeps_selector (list) (optional)

      available outputs:
        - field_min (FieldsContainer)
        - field_max (FieldsContainer)
        - all_fields (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.fft_multi_harmonic_minmax()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_rpm_scoping = dpf.Scoping()
      >>> op.inputs.rpm_scoping.connect(my_rpm_scoping)
      >>> my_fs_ratio = int()
      >>> op.inputs.fs_ratio.connect(my_fs_ratio)
      >>> my_num_subdivisions = int()
      >>> op.inputs.num_subdivisions.connect(my_num_subdivisions)
      >>> my_max_num_subdivisions = int()
      >>> op.inputs.max_num_subdivisions.connect(my_max_num_subdivisions)
      >>> my_num_cycles = int()
      >>> op.inputs.num_cycles.connect(my_num_cycles)
      >>> my_use_harmonic_zero = bool()
      >>> op.inputs.use_harmonic_zero.connect(my_use_harmonic_zero)
      >>> my_calculate_time_series = bool()
      >>> op.inputs.calculate_time_series.connect(my_calculate_time_series)
      >>> my_substeps_selector = dpf.list()
      >>> op.inputs.substeps_selector.connect(my_substeps_selector)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.fft_multi_harmonic_minmax(fields_container=my_fields_container,rpm_scoping=my_rpm_scoping,fs_ratio=my_fs_ratio,num_subdivisions=my_num_subdivisions,max_num_subdivisions=my_max_num_subdivisions,num_cycles=my_num_cycles,use_harmonic_zero=my_use_harmonic_zero,calculate_time_series=my_calculate_time_series,substeps_selector=my_substeps_selector)

      >>> # Get output data
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()
      >>> result_all_fields = op.outputs.all_fields()"""
    def __init__(self, fields_container=None, rpm_scoping=None, fs_ratio=None, num_subdivisions=None, max_num_subdivisions=None, num_cycles=None, use_harmonic_zero=None, calculate_time_series=None, substeps_selector=None, config=None, server=None):
        super().__init__(name="fft_multi_harmonic_minmax", config = config, server = server)
        self._inputs = InputsFftMultiHarmonicMinmax(self)
        self._outputs = OutputsFftMultiHarmonicMinmax(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if rpm_scoping !=None:
            self.inputs.rpm_scoping.connect(rpm_scoping)
        if fs_ratio !=None:
            self.inputs.fs_ratio.connect(fs_ratio)
        if num_subdivisions !=None:
            self.inputs.num_subdivisions.connect(num_subdivisions)
        if max_num_subdivisions !=None:
            self.inputs.max_num_subdivisions.connect(max_num_subdivisions)
        if num_cycles !=None:
            self.inputs.num_cycles.connect(num_cycles)
        if use_harmonic_zero !=None:
            self.inputs.use_harmonic_zero.connect(use_harmonic_zero)
        if calculate_time_series !=None:
            self.inputs.calculate_time_series.connect(calculate_time_series)
        if substeps_selector !=None:
            self.inputs.substeps_selector.connect(substeps_selector)

    @staticmethod
    def _spec():
        spec = Specification(description="""
Finds the minimum and maximum of a multi-harmonic field over one period using an adaptive time-stepping
gradient method. The field is expressed as a [Fourier series](https://en.wikipedia.org/wiki/Fourier_series)
over harmonic orders corresponding to integer multiples of the operating speed (RPMs).
For each spatial entity, the series is evaluated at adaptively chosen time instants over one period
and the pointwise minimum and maximum are extracted.

ElementalNodal locations are not supported.
""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""Complex multi-harmonic results fields container. Must have a complex label and a time-frequency support whose values are the harmonic excitation frequencies (RPMs). ElementalNodal results are not supported."""), 
                                 1 : PinSpecification(name = "rpm_scoping", type_names=["scoping"], optional=True, document="""RPM scoping. When provided, only the selected RPM set IDs are included in the Fourier series. When omitted, all available RPMs are used."""), 
                                 2 : PinSpecification(name = "fs_ratio", type_names=["int32"], optional=True, document="""Oversampling ratio used to set the uniform time step as $1/(f_{max} \times \mathit{fs_ratio})$. Default is $20$."""), 
                                 3 : PinSpecification(name = "num_subdivisions", type_names=["int32"], optional=True, document="""Number of uniform time subdivisions per period. When provided, overrides the adaptive step computation. Default is $-1$ (adaptive)."""), 
                                 4 : PinSpecification(name = "max_num_subdivisions", type_names=["int32"], optional=True, document="""Maximum number of time subdivisions to avoid excessively fine discretisation. Default is $8000$."""), 
                                 5 : PinSpecification(name = "num_cycles", type_names=["int32"], optional=True, document="""Number of periods over which the signal is evaluated. Default is $2$."""), 
                                 6 : PinSpecification(name = "use_harmonic_zero", type_names=["bool"], optional=True, document="""When true, includes the harmonic-zero (constant) term for the first RPM. Default is false."""), 
                                 7 : PinSpecification(name = "calculate_time_series", type_names=["bool"], optional=True, document="""When true (default), computes the full time series at output pin 2. Set to false to skip the time-series output and only compute min and max, which reduces computation time."""), 
                                 8 : PinSpecification(name = "substeps_selector", type_names=["vector<int32>"], optional=True, document="""List of harmonic order (substep) indices to include. When omitted, all available substeps are used.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_min", type_names=["fields_container"], optional=False, document="""Fields container of pointwise minimum values over one period. Same spatial layout as the input."""), 
                                 1 : PinSpecification(name = "field_max", type_names=["fields_container"], optional=False, document="""Fields container of pointwise maximum values over one period. Same spatial layout as the input."""), 
                                 2 : PinSpecification(name = "all_fields", type_names=["fields_container"], optional=False, document="""Full time-series fields container over the evaluation period. Only produced when pin 7 is true (default).""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "fft_multi_harmonic_minmax")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsFftMultiHarmonicMinmax 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsFftMultiHarmonicMinmax 
        """
        return super().outputs


#internal name: fft_multi_harmonic_minmax
#scripting name: fft_multi_harmonic_minmax
class InputsFftMultiHarmonicMinmax(_Inputs):
    """Intermediate class used to connect user inputs to fft_multi_harmonic_minmax operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_rpm_scoping = dpf.Scoping()
      >>> op.inputs.rpm_scoping.connect(my_rpm_scoping)
      >>> my_fs_ratio = int()
      >>> op.inputs.fs_ratio.connect(my_fs_ratio)
      >>> my_num_subdivisions = int()
      >>> op.inputs.num_subdivisions.connect(my_num_subdivisions)
      >>> my_max_num_subdivisions = int()
      >>> op.inputs.max_num_subdivisions.connect(my_max_num_subdivisions)
      >>> my_num_cycles = int()
      >>> op.inputs.num_cycles.connect(my_num_cycles)
      >>> my_use_harmonic_zero = bool()
      >>> op.inputs.use_harmonic_zero.connect(my_use_harmonic_zero)
      >>> my_calculate_time_series = bool()
      >>> op.inputs.calculate_time_series.connect(my_calculate_time_series)
      >>> my_substeps_selector = dpf.list()
      >>> op.inputs.substeps_selector.connect(my_substeps_selector)
    """
    def __init__(self, op: Operator):
        super().__init__(fft_multi_harmonic_minmax._spec().inputs, op)
        self._fields_container = Input(fft_multi_harmonic_minmax._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._rpm_scoping = Input(fft_multi_harmonic_minmax._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._rpm_scoping)
        self._fs_ratio = Input(fft_multi_harmonic_minmax._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._fs_ratio)
        self._num_subdivisions = Input(fft_multi_harmonic_minmax._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._num_subdivisions)
        self._max_num_subdivisions = Input(fft_multi_harmonic_minmax._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._max_num_subdivisions)
        self._num_cycles = Input(fft_multi_harmonic_minmax._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._num_cycles)
        self._use_harmonic_zero = Input(fft_multi_harmonic_minmax._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self._use_harmonic_zero)
        self._calculate_time_series = Input(fft_multi_harmonic_minmax._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._calculate_time_series)
        self._substeps_selector = Input(fft_multi_harmonic_minmax._spec().input_pin(8), 8, op, -1) 
        self._inputs.append(self._substeps_selector)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: Complex multi-harmonic results fields container. Must have a complex label and a time-frequency support whose values are the harmonic excitation frequencies (RPMs). ElementalNodal results are not supported.

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def rpm_scoping(self):
        """Allows to connect rpm_scoping input to the operator

        - pindoc: RPM scoping. When provided, only the selected RPM set IDs are included in the Fourier series. When omitted, all available RPMs are used.

        Parameters
        ----------
        my_rpm_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.rpm_scoping.connect(my_rpm_scoping)
        >>> #or
        >>> op.inputs.rpm_scoping(my_rpm_scoping)

        """
        return self._rpm_scoping

    @property
    def fs_ratio(self):
        """Allows to connect fs_ratio input to the operator

        - pindoc: Oversampling ratio used to set the uniform time step as $1/(f_{max} \times \mathit{fs_ratio})$. Default is $20$.

        Parameters
        ----------
        my_fs_ratio : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.fs_ratio.connect(my_fs_ratio)
        >>> #or
        >>> op.inputs.fs_ratio(my_fs_ratio)

        """
        return self._fs_ratio

    @property
    def num_subdivisions(self):
        """Allows to connect num_subdivisions input to the operator

        - pindoc: Number of uniform time subdivisions per period. When provided, overrides the adaptive step computation. Default is $-1$ (adaptive).

        Parameters
        ----------
        my_num_subdivisions : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.num_subdivisions.connect(my_num_subdivisions)
        >>> #or
        >>> op.inputs.num_subdivisions(my_num_subdivisions)

        """
        return self._num_subdivisions

    @property
    def max_num_subdivisions(self):
        """Allows to connect max_num_subdivisions input to the operator

        - pindoc: Maximum number of time subdivisions to avoid excessively fine discretisation. Default is $8000$.

        Parameters
        ----------
        my_max_num_subdivisions : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.max_num_subdivisions.connect(my_max_num_subdivisions)
        >>> #or
        >>> op.inputs.max_num_subdivisions(my_max_num_subdivisions)

        """
        return self._max_num_subdivisions

    @property
    def num_cycles(self):
        """Allows to connect num_cycles input to the operator

        - pindoc: Number of periods over which the signal is evaluated. Default is $2$.

        Parameters
        ----------
        my_num_cycles : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.num_cycles.connect(my_num_cycles)
        >>> #or
        >>> op.inputs.num_cycles(my_num_cycles)

        """
        return self._num_cycles

    @property
    def use_harmonic_zero(self):
        """Allows to connect use_harmonic_zero input to the operator

        - pindoc: When true, includes the harmonic-zero (constant) term for the first RPM. Default is false.

        Parameters
        ----------
        my_use_harmonic_zero : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.use_harmonic_zero.connect(my_use_harmonic_zero)
        >>> #or
        >>> op.inputs.use_harmonic_zero(my_use_harmonic_zero)

        """
        return self._use_harmonic_zero

    @property
    def calculate_time_series(self):
        """Allows to connect calculate_time_series input to the operator

        - pindoc: When true (default), computes the full time series at output pin 2. Set to false to skip the time-series output and only compute min and max, which reduces computation time.

        Parameters
        ----------
        my_calculate_time_series : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.calculate_time_series.connect(my_calculate_time_series)
        >>> #or
        >>> op.inputs.calculate_time_series(my_calculate_time_series)

        """
        return self._calculate_time_series

    @property
    def substeps_selector(self):
        """Allows to connect substeps_selector input to the operator

        - pindoc: List of harmonic order (substep) indices to include. When omitted, all available substeps are used.

        Parameters
        ----------
        my_substeps_selector : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.substeps_selector.connect(my_substeps_selector)
        >>> #or
        >>> op.inputs.substeps_selector(my_substeps_selector)

        """
        return self._substeps_selector

class OutputsFftMultiHarmonicMinmax(_Outputs):
    """Intermediate class used to get outputs from fft_multi_harmonic_minmax operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()
      >>> result_all_fields = op.outputs.all_fields()
    """
    def __init__(self, op: Operator):
        super().__init__(fft_multi_harmonic_minmax._spec().outputs, op)
        self._field_min = Output(fft_multi_harmonic_minmax._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field_min)
        self._field_max = Output(fft_multi_harmonic_minmax._spec().output_pin(1), 1, op) 
        self._outputs.append(self._field_max)
        self._all_fields = Output(fft_multi_harmonic_minmax._spec().output_pin(2), 2, op) 
        self._outputs.append(self._all_fields)

    @property
    def field_min(self):
        """Allows to get field_min output of the operator


        - pindoc: Fields container of pointwise minimum values over one period. Same spatial layout as the input.

        Returns
        ----------
        my_field_min : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_min = op.outputs.field_min() 
        """
        return self._field_min

    @property
    def field_max(self):
        """Allows to get field_max output of the operator


        - pindoc: Fields container of pointwise maximum values over one period. Same spatial layout as the input.

        Returns
        ----------
        my_field_max : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_max = op.outputs.field_max() 
        """
        return self._field_max

    @property
    def all_fields(self):
        """Allows to get all_fields output of the operator


        - pindoc: Full time-series fields container over the evaluation period. Only produced when pin 7 is true (default).

        Returns
        ----------
        my_all_fields : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> # Connect inputs : op.inputs. ...
        >>> result_all_fields = op.outputs.all_fields() 
        """
        return self._all_fields

