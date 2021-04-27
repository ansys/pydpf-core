"""
MinMax Operators
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "min_max" category
"""

#internal name: min_max_by_time
#scripting name: min_max_by_time
class _InputsMinMaxByTime(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_by_time._spec().inputs, op)
        self.fields_container = Input(min_max_by_time._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsMinMaxByTime(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_by_time._spec().outputs, op)
        self.min = Output(min_max_by_time._spec().output_pin(0), 0, op) 
        self._outputs.append(self.min)
        self.max = Output(min_max_by_time._spec().output_pin(1), 1, op) 
        self._outputs.append(self.max)

class min_max_by_time(Operator):
    """Evaluates minimum, maximum by time or frequency over all the entities of each field

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         min (FieldsContainer)
         max (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max_by_time()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_min = op.outputs.min()
      >>> result_max = op.outputs.max()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="min_max_by_time", config = config, server = server)
        self.inputs = _InputsMinMaxByTime(self)
        self.outputs = _OutputsMinMaxByTime(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates minimum, maximum by time or frequency over all the entities of each field""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "min", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "max", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max_by_time")

#internal name: phase_of_max
#scripting name: phase_of_max
class _InputsPhaseOfMax(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(phase_of_max._spec().inputs, op)
        self.real_field = Input(phase_of_max._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.real_field)
        self.imaginary_field = Input(phase_of_max._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.imaginary_field)
        self.abs_value = Input(phase_of_max._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.abs_value)
        self.phase_increment = Input(phase_of_max._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.phase_increment)

class _OutputsPhaseOfMax(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(phase_of_max._spec().outputs, op)
        self.field = Output(phase_of_max._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class phase_of_max(Operator):
    """Evaluates phase of maximum.

      available inputs:
         real_field (Field)
         imaginary_field (Field)
         abs_value (bool) (optional)
         phase_increment (float)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.phase_of_max()

      >>> # Make input connections
      >>> my_real_field = dpf.Field()
      >>> op.inputs.real_field.connect(my_real_field)
      >>> my_imaginary_field = dpf.Field()
      >>> op.inputs.imaginary_field.connect(my_imaginary_field)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_phase_increment = float()
      >>> op.inputs.phase_increment.connect(my_phase_increment)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, real_field=None, imaginary_field=None, abs_value=None, phase_increment=None, config=None, server=None):
        super().__init__(name="phase_of_max", config = config, server = server)
        self.inputs = _InputsPhaseOfMax(self)
        self.outputs = _OutputsPhaseOfMax(self)
        if real_field !=None:
            self.inputs.real_field.connect(real_field)
        if imaginary_field !=None:
            self.inputs.imaginary_field.connect(imaginary_field)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)
        if phase_increment !=None:
            self.inputs.phase_increment.connect(phase_increment)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates phase of maximum.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "real_field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "imaginary_field", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "abs_value", type_names=["bool"], optional=True, document="""Should use absolute value."""), 
                                 3 : PinSpecification(name = "phase_increment", type_names=["double"], optional=False, document="""Phase increment.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "phase_of_max")

#internal name: time_of_max_by_entity
#scripting name: time_of_max_by_entity
class _InputsTimeOfMaxByEntity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(time_of_max_by_entity._spec().inputs, op)
        self.fields_container = Input(time_of_max_by_entity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.abs_value = Input(time_of_max_by_entity._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.abs_value)
        self.compute_amplitude = Input(time_of_max_by_entity._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.compute_amplitude)

class _OutputsTimeOfMaxByEntity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(time_of_max_by_entity._spec().outputs, op)
        self.fields_container = Output(time_of_max_by_entity._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class time_of_max_by_entity(Operator):
    """Evaluates time/frequency of maximum.

      available inputs:
         fields_container (FieldsContainer)
         abs_value (bool) (optional)
         compute_amplitude (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.time_of_max_by_entity()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_compute_amplitude = bool()
      >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, abs_value=None, compute_amplitude=None, config=None, server=None):
        super().__init__(name="time_of_max_by_entity", config = config, server = server)
        self.inputs = _InputsTimeOfMaxByEntity(self)
        self.outputs = _OutputsTimeOfMaxByEntity(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)
        if compute_amplitude !=None:
            self.inputs.compute_amplitude.connect(compute_amplitude)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates time/frequency of maximum.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "abs_value", type_names=["bool"], optional=True, document="""Should use absolute value."""), 
                                 4 : PinSpecification(name = "compute_amplitude", type_names=["bool"], optional=True, document="""Do calculate amplitude.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "time_of_max_by_entity")

#internal name: min_max_by_entity
#scripting name: min_max_by_entity
class _InputsMinMaxByEntity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_by_entity._spec().inputs, op)
        self.fields_container = Input(min_max_by_entity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsMinMaxByEntity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_by_entity._spec().outputs, op)
        self.field_min = Output(min_max_by_entity._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field_min)
        self.field_max = Output(min_max_by_entity._spec().output_pin(1), 1, op) 
        self._outputs.append(self.field_max)

class min_max_by_entity(Operator):
    """Compute the entity-wise minimum (out 0) and maximum (out 1) through all fields of a fields container.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         field_min (Field)
         field_max (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max_by_entity()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="min_max_by_entity", config = config, server = server)
        self.inputs = _InputsMinMaxByEntity(self)
        self.outputs = _OutputsMinMaxByEntity(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the entity-wise minimum (out 0) and maximum (out 1) through all fields of a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_min", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "field_max", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max_by_entity")

#internal name: min_max_over_time_by_entity
#scripting name: min_max_over_time_by_entity
class _InputsMinMaxOverTimeByEntity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_over_time_by_entity._spec().inputs, op)
        self.fields_container = Input(min_max_over_time_by_entity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.compute_amplitude = Input(min_max_over_time_by_entity._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.compute_amplitude)

class _OutputsMinMaxOverTimeByEntity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_over_time_by_entity._spec().outputs, op)
        self.min = Output(min_max_over_time_by_entity._spec().output_pin(0), 0, op) 
        self._outputs.append(self.min)
        self.max = Output(min_max_over_time_by_entity._spec().output_pin(1), 1, op) 
        self._outputs.append(self.max)
        self.time_freq_of_min = Output(min_max_over_time_by_entity._spec().output_pin(2), 2, op) 
        self._outputs.append(self.time_freq_of_min)
        self.time_freq_of_max = Output(min_max_over_time_by_entity._spec().output_pin(3), 3, op) 
        self._outputs.append(self.time_freq_of_max)

class min_max_over_time_by_entity(Operator):
    """Evaluates minimum, maximum over time/frequency and returns those min max as well as the time/freq where they occured

      available inputs:
         fields_container (FieldsContainer)
         compute_amplitude (bool) (optional)

      available outputs:
         min (FieldsContainer)
         max (FieldsContainer)
         time_freq_of_min (FieldsContainer)
         time_freq_of_max (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max_over_time_by_entity()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_compute_amplitude = bool()
      >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)

      >>> # Get output data
      >>> result_min = op.outputs.min()
      >>> result_max = op.outputs.max()
      >>> result_time_freq_of_min = op.outputs.time_freq_of_min()
      >>> result_time_freq_of_max = op.outputs.time_freq_of_max()"""
    def __init__(self, fields_container=None, compute_amplitude=None, config=None, server=None):
        super().__init__(name="min_max_over_time_by_entity", config = config, server = server)
        self.inputs = _InputsMinMaxOverTimeByEntity(self)
        self.outputs = _OutputsMinMaxOverTimeByEntity(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if compute_amplitude !=None:
            self.inputs.compute_amplitude.connect(compute_amplitude)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates minimum, maximum over time/frequency and returns those min max as well as the time/freq where they occured""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 4 : PinSpecification(name = "compute_amplitude", type_names=["bool"], optional=True, document="""Do calculate amplitude.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "min", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "max", type_names=["fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "time_freq_of_min", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "time_freq_of_max", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max_over_time_by_entity")

#internal name: max_over_time_by_entity
#scripting name: max_over_time_by_entity
class _InputsMaxOverTimeByEntity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(max_over_time_by_entity._spec().inputs, op)
        self.fields_container = Input(max_over_time_by_entity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.abs_value = Input(max_over_time_by_entity._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.abs_value)
        self.compute_amplitude = Input(max_over_time_by_entity._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.compute_amplitude)

class _OutputsMaxOverTimeByEntity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(max_over_time_by_entity._spec().outputs, op)
        self.fields_container = Output(max_over_time_by_entity._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class max_over_time_by_entity(Operator):
    """Evaluates maximum over time/frequency.

      available inputs:
         fields_container (FieldsContainer)
         abs_value (bool) (optional)
         compute_amplitude (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.max_over_time_by_entity()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_compute_amplitude = bool()
      >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, abs_value=None, compute_amplitude=None, config=None, server=None):
        super().__init__(name="max_over_time_by_entity", config = config, server = server)
        self.inputs = _InputsMaxOverTimeByEntity(self)
        self.outputs = _OutputsMaxOverTimeByEntity(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)
        if compute_amplitude !=None:
            self.inputs.compute_amplitude.connect(compute_amplitude)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates maximum over time/frequency.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "abs_value", type_names=["bool"], optional=True, document="""Should use absolute value."""), 
                                 4 : PinSpecification(name = "compute_amplitude", type_names=["bool"], optional=True, document="""Do calculate amplitude.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "max_over_time_by_entity")

#internal name: min_over_time_by_entity
#scripting name: min_over_time_by_entity
class _InputsMinOverTimeByEntity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(min_over_time_by_entity._spec().inputs, op)
        self.fields_container = Input(min_over_time_by_entity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.abs_value = Input(min_over_time_by_entity._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.abs_value)
        self.compute_amplitude = Input(min_over_time_by_entity._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.compute_amplitude)

class _OutputsMinOverTimeByEntity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(min_over_time_by_entity._spec().outputs, op)
        self.fields_container = Output(min_over_time_by_entity._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class min_over_time_by_entity(Operator):
    """Evaluates minimum over time/frequency.

      available inputs:
         fields_container (FieldsContainer)
         abs_value (bool) (optional)
         compute_amplitude (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_over_time_by_entity()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_compute_amplitude = bool()
      >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, abs_value=None, compute_amplitude=None, config=None, server=None):
        super().__init__(name="min_over_time_by_entity", config = config, server = server)
        self.inputs = _InputsMinOverTimeByEntity(self)
        self.outputs = _OutputsMinOverTimeByEntity(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)
        if compute_amplitude !=None:
            self.inputs.compute_amplitude.connect(compute_amplitude)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates minimum over time/frequency.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "abs_value", type_names=["bool"], optional=True, document="""Should use absolute value."""), 
                                 4 : PinSpecification(name = "compute_amplitude", type_names=["bool"], optional=True, document="""Do calculate amplitude.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_over_time_by_entity")

#internal name: time_of_min_by_entity
#scripting name: time_of_min_by_entity
class _InputsTimeOfMinByEntity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(time_of_min_by_entity._spec().inputs, op)
        self.fields_container = Input(time_of_min_by_entity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.abs_value = Input(time_of_min_by_entity._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.abs_value)
        self.compute_amplitude = Input(time_of_min_by_entity._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.compute_amplitude)

class _OutputsTimeOfMinByEntity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(time_of_min_by_entity._spec().outputs, op)
        self.fields_container = Output(time_of_min_by_entity._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class time_of_min_by_entity(Operator):
    """Evaluates time/frequency of minimum.

      available inputs:
         fields_container (FieldsContainer)
         abs_value (bool) (optional)
         compute_amplitude (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.time_of_min_by_entity()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_compute_amplitude = bool()
      >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, abs_value=None, compute_amplitude=None, config=None, server=None):
        super().__init__(name="time_of_min_by_entity", config = config, server = server)
        self.inputs = _InputsTimeOfMinByEntity(self)
        self.outputs = _OutputsTimeOfMinByEntity(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)
        if compute_amplitude !=None:
            self.inputs.compute_amplitude.connect(compute_amplitude)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates time/frequency of minimum.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "abs_value", type_names=["bool"], optional=True, document="""Should use absolute value."""), 
                                 4 : PinSpecification(name = "compute_amplitude", type_names=["bool"], optional=True, document="""Do calculate amplitude.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "time_of_min_by_entity")

#internal name: max_over_phase
#scripting name: max_over_phase
class _InputsMaxOverPhase(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(max_over_phase._spec().inputs, op)
        self.real_field = Input(max_over_phase._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.real_field)
        self.imaginary_field = Input(max_over_phase._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.imaginary_field)
        self.abs_value = Input(max_over_phase._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.abs_value)
        self.phase_increment = Input(max_over_phase._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.phase_increment)

class _OutputsMaxOverPhase(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(max_over_phase._spec().outputs, op)
        self.field = Output(max_over_phase._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class max_over_phase(Operator):
    """Returns, for each entity, the maximum value of (real value * cos(theta) - imaginary value * sin(theta)) for theta in [0, 360]degrees with the increment in input.

      available inputs:
         real_field (Field)
         imaginary_field (Field)
         abs_value (bool) (optional)
         phase_increment (float) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.max_over_phase()

      >>> # Make input connections
      >>> my_real_field = dpf.Field()
      >>> op.inputs.real_field.connect(my_real_field)
      >>> my_imaginary_field = dpf.Field()
      >>> op.inputs.imaginary_field.connect(my_imaginary_field)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_phase_increment = float()
      >>> op.inputs.phase_increment.connect(my_phase_increment)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, real_field=None, imaginary_field=None, abs_value=None, phase_increment=None, config=None, server=None):
        super().__init__(name="max_over_phase", config = config, server = server)
        self.inputs = _InputsMaxOverPhase(self)
        self.outputs = _OutputsMaxOverPhase(self)
        if real_field !=None:
            self.inputs.real_field.connect(real_field)
        if imaginary_field !=None:
            self.inputs.imaginary_field.connect(imaginary_field)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)
        if phase_increment !=None:
            self.inputs.phase_increment.connect(phase_increment)

    @staticmethod
    def _spec():
        spec = Specification(description="""Returns, for each entity, the maximum value of (real value * cos(theta) - imaginary value * sin(theta)) for theta in [0, 360]degrees with the increment in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "real_field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "imaginary_field", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "abs_value", type_names=["bool"], optional=True, document="""Should use absolute value."""), 
                                 3 : PinSpecification(name = "phase_increment", type_names=["double"], optional=True, document="""Phase increment (default is 10.0 degrees).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "max_over_phase")

#internal name: min_max
#scripting name: min_max
class _InputsMinMax(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(min_max._spec().inputs, op)
        self.field = Input(min_max._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsMinMax(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(min_max._spec().outputs, op)
        self.field_min = Output(min_max._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field_min)
        self.field_max = Output(min_max._spec().output_pin(1), 1, op) 
        self._outputs.append(self.field_max)

class min_max(Operator):
    """Compute the component-wise minimum (out 0) and maximum (out 1) over a field.

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field_min (Field)
         field_max (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Get output data
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="min_max", config = config, server = server)
        self.inputs = _InputsMinMax(self)
        self.outputs = _OutputsMinMax(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the component-wise minimum (out 0) and maximum (out 1) over a field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_min", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "field_max", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max")

#internal name: min_max_fc
#scripting name: min_max_fc
class _InputsMinMaxFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_fc._spec().inputs, op)
        self.fields_container = Input(min_max_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsMinMaxFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_fc._spec().outputs, op)
        self.field_min = Output(min_max_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field_min)
        self.field_max = Output(min_max_fc._spec().output_pin(1), 1, op) 
        self._outputs.append(self.field_max)

class min_max_fc(Operator):
    """Compute the component-wise minimum (out 0) and maximum (out 1) over a fields container.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         field_min (Field)
         field_max (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="min_max_fc", config = config, server = server)
        self.inputs = _InputsMinMaxFc(self)
        self.outputs = _OutputsMinMaxFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the component-wise minimum (out 0) and maximum (out 1) over a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_min", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "field_max", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max_fc")

#internal name: min_max_over_label_fc
#scripting name: min_max_over_label_fc
class _InputsMinMaxOverLabelFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_over_label_fc._spec().inputs, op)
        self.fields_container = Input(min_max_over_label_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.label = Input(min_max_over_label_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.label)

class _OutputsMinMaxOverLabelFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_over_label_fc._spec().outputs, op)
        self.field_min = Output(min_max_over_label_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field_min)
        self.field_max = Output(min_max_over_label_fc._spec().output_pin(1), 1, op) 
        self._outputs.append(self.field_max)
        self.domain_ids_min = Output(min_max_over_label_fc._spec().output_pin(2), 2, op) 
        self._outputs.append(self.domain_ids_min)
        self.domain_ids_max = Output(min_max_over_label_fc._spec().output_pin(3), 3, op) 
        self._outputs.append(self.domain_ids_max)
        self.scoping_ids_min = Output(min_max_over_label_fc._spec().output_pin(4), 4, op) 
        self._outputs.append(self.scoping_ids_min)
        self.scoping_ids_max = Output(min_max_over_label_fc._spec().output_pin(5), 5, op) 
        self._outputs.append(self.scoping_ids_max)

class min_max_over_label_fc(Operator):
    """Create two fields (0 min 1 max) by looping over the fields container in input and taking the min/max value by component through all the fields having the same id for the label set in input (in pin 1). If no label is specified or if the specified label doesn't exist, the operation is done over all the fields. The fields out are located on the label set in input, so their scoping are the labels ids.For each min max value, the label id for one other fields container labels is kept and returned in a scoping in pin 2 (min) and 3 (max).The field's scoping ids of the value kept in min max are also returned in the scopings in pin 4 (min) and 5 (max).

      available inputs:
         fields_container (FieldsContainer)
         label (str)

      available outputs:
         field_min (Field)
         field_max (Field)
         domain_ids_min (Scoping)
         domain_ids_max (Scoping)
         scoping_ids_min (Scoping)
         scoping_ids_max (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max_over_label_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_label = str()
      >>> op.inputs.label.connect(my_label)

      >>> # Get output data
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()
      >>> result_domain_ids_min = op.outputs.domain_ids_min()
      >>> result_domain_ids_max = op.outputs.domain_ids_max()
      >>> result_scoping_ids_min = op.outputs.scoping_ids_min()
      >>> result_scoping_ids_max = op.outputs.scoping_ids_max()"""
    def __init__(self, fields_container=None, label=None, config=None, server=None):
        super().__init__(name="min_max_over_label_fc", config = config, server = server)
        self.inputs = _InputsMinMaxOverLabelFc(self)
        self.outputs = _OutputsMinMaxOverLabelFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if label !=None:
            self.inputs.label.connect(label)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create two fields (0 min 1 max) by looping over the fields container in input and taking the min/max value by component through all the fields having the same id for the label set in input (in pin 1). If no label is specified or if the specified label doesn't exist, the operation is done over all the fields. The fields out are located on the label set in input, so their scoping are the labels ids.For each min max value, the label id for one other fields container labels is kept and returned in a scoping in pin 2 (min) and 3 (max).The field's scoping ids of the value kept in min max are also returned in the scopings in pin 4 (min) and 5 (max).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "label", type_names=["string"], optional=False, document="""label name from the fields container""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_min", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "field_max", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "domain_ids_min", type_names=["scoping"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "domain_ids_max", type_names=["scoping"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "scoping_ids_min", type_names=["scoping"], optional=False, document=""""""), 
                                 5 : PinSpecification(name = "scoping_ids_max", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max_over_label_fc")

#internal name: min_by_component
#scripting name: min_by_component
class _InputsMinByComponent(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(min_by_component._spec().inputs, op)
        self.use_absolute_value = Input(min_by_component._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.use_absolute_value)
        self.fieldA1 = Input(min_by_component._spec().input_pin(1), 1, op, 0) 
        self._inputs.append(self.fieldA1)
        self.fieldA2 = Input(min_by_component._spec().input_pin(2), 2, op, 1) 
        self._inputs.append(self.fieldA2)
        self.fieldB2 = Input(min_by_component._spec().input_pin(3), 3, op, 1) 
        self._inputs.append(self.fieldB2)

class _OutputsMinByComponent(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(min_by_component._spec().outputs, op)
        self.field = Output(min_by_component._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class min_by_component(Operator):
    """Give the maximum for each element rank by comparing several fields.

      available inputs:
         use_absolute_value (bool)
         fieldA1 (Field, FieldsContainer)
         fieldA2 (Field, FieldsContainer)
         fieldB2 (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_by_component()

      >>> # Make input connections
      >>> my_use_absolute_value = bool()
      >>> op.inputs.use_absolute_value.connect(my_use_absolute_value)
      >>> my_fieldA1 = dpf.Field()
      >>> op.inputs.fieldA1.connect(my_fieldA1)
      >>> my_fieldA2 = dpf.Field()
      >>> op.inputs.fieldA2.connect(my_fieldA2)
      >>> my_fieldB2 = dpf.Field()
      >>> op.inputs.fieldB2.connect(my_fieldB2)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, use_absolute_value=None, fieldA1=None, fieldA2=None, fieldB2=None, config=None, server=None):
        super().__init__(name="min_by_component", config = config, server = server)
        self.inputs = _InputsMinByComponent(self)
        self.outputs = _OutputsMinByComponent(self)
        if use_absolute_value !=None:
            self.inputs.use_absolute_value.connect(use_absolute_value)
        if fieldA1 !=None:
            self.inputs.fieldA1.connect(fieldA1)
        if fieldA2 !=None:
            self.inputs.fieldA2.connect(fieldA2)
        if fieldB2 !=None:
            self.inputs.fieldB2.connect(fieldB2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Give the maximum for each element rank by comparing several fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "use_absolute_value", type_names=["bool"], optional=False, document="""use_absolute_value"""), 
                                 1 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 2 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 3 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_by_component")

#internal name: max_by_component
#scripting name: max_by_component
class _InputsMaxByComponent(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(max_by_component._spec().inputs, op)
        self.use_absolute_value = Input(max_by_component._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.use_absolute_value)
        self.fieldA1 = Input(max_by_component._spec().input_pin(1), 1, op, 0) 
        self._inputs.append(self.fieldA1)
        self.fieldA2 = Input(max_by_component._spec().input_pin(2), 2, op, 1) 
        self._inputs.append(self.fieldA2)
        self.fieldB2 = Input(max_by_component._spec().input_pin(3), 3, op, 1) 
        self._inputs.append(self.fieldB2)

class _OutputsMaxByComponent(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(max_by_component._spec().outputs, op)
        self.field = Output(max_by_component._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class max_by_component(Operator):
    """Give the maximum for each element rank by comparing several fields.

      available inputs:
         use_absolute_value (bool)
         fieldA1 (Field, FieldsContainer)
         fieldA2 (Field, FieldsContainer)
         fieldB2 (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.max_by_component()

      >>> # Make input connections
      >>> my_use_absolute_value = bool()
      >>> op.inputs.use_absolute_value.connect(my_use_absolute_value)
      >>> my_fieldA1 = dpf.Field()
      >>> op.inputs.fieldA1.connect(my_fieldA1)
      >>> my_fieldA2 = dpf.Field()
      >>> op.inputs.fieldA2.connect(my_fieldA2)
      >>> my_fieldB2 = dpf.Field()
      >>> op.inputs.fieldB2.connect(my_fieldB2)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, use_absolute_value=None, fieldA1=None, fieldA2=None, fieldB2=None, config=None, server=None):
        super().__init__(name="max_by_component", config = config, server = server)
        self.inputs = _InputsMaxByComponent(self)
        self.outputs = _OutputsMaxByComponent(self)
        if use_absolute_value !=None:
            self.inputs.use_absolute_value.connect(use_absolute_value)
        if fieldA1 !=None:
            self.inputs.fieldA1.connect(fieldA1)
        if fieldA2 !=None:
            self.inputs.fieldA2.connect(fieldA2)
        if fieldB2 !=None:
            self.inputs.fieldB2.connect(fieldB2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Give the maximum for each element rank by comparing several fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "use_absolute_value", type_names=["bool"], optional=False, document="""use_absolute_value"""), 
                                 1 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 2 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 3 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "max_by_component")

#internal name: min_max_fc_inc
#scripting name: min_max_fc_inc
class _InputsMinMaxFcInc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_fc_inc._spec().inputs, op)
        self.fields_container = Input(min_max_fc_inc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsMinMaxFcInc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_fc_inc._spec().outputs, op)
        self.field_min = Output(min_max_fc_inc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field_min)
        self.field_max = Output(min_max_fc_inc._spec().output_pin(1), 1, op) 
        self._outputs.append(self.field_max)

class min_max_fc_inc(Operator):
    """Compute the component-wise minimum (out 0) and maximum (out 1) over a fields container.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         field_min (Field)
         field_max (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max_fc_inc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="min_max_fc_inc", config = config, server = server)
        self.inputs = _InputsMinMaxFcInc(self)
        self.outputs = _OutputsMinMaxFcInc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the component-wise minimum (out 0) and maximum (out 1) over a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_min", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "field_max", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max_fc_inc")

#internal name: min_max_inc
#scripting name: min_max_inc
class _InputsMinMaxInc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_inc._spec().inputs, op)
        self.field = Input(min_max_inc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.domain_id = Input(min_max_inc._spec().input_pin(17), 17, op, -1) 
        self._inputs.append(self.domain_id)

class _OutputsMinMaxInc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(min_max_inc._spec().outputs, op)
        self.field_min = Output(min_max_inc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field_min)
        self.field_max = Output(min_max_inc._spec().output_pin(1), 1, op) 
        self._outputs.append(self.field_max)
        self.domain_ids_min = Output(min_max_inc._spec().output_pin(2), 2, op) 
        self._outputs.append(self.domain_ids_min)
        self.domain_ids_max = Output(min_max_inc._spec().output_pin(3), 3, op) 
        self._outputs.append(self.domain_ids_max)

class min_max_inc(Operator):
    """Compute the component-wise minimum (out 0) and maximum (out 1) over coming fields.

      available inputs:
         field (Field)
         domain_id (int) (optional)

      available outputs:
         field_min (Field)
         field_max (Field)
         domain_ids_min (Scoping)
         domain_ids_max (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max_inc()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_domain_id = int()
      >>> op.inputs.domain_id.connect(my_domain_id)

      >>> # Get output data
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()
      >>> result_domain_ids_min = op.outputs.domain_ids_min()
      >>> result_domain_ids_max = op.outputs.domain_ids_max()"""
    def __init__(self, field=None, domain_id=None, config=None, server=None):
        super().__init__(name="min_max_inc", config = config, server = server)
        self.inputs = _InputsMinMaxInc(self)
        self.outputs = _OutputsMinMaxInc(self)
        if field !=None:
            self.inputs.field.connect(field)
        if domain_id !=None:
            self.inputs.domain_id.connect(domain_id)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the component-wise minimum (out 0) and maximum (out 1) over coming fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 17 : PinSpecification(name = "domain_id", type_names=["int32"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_min", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "field_max", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "domain_ids_min", type_names=["scoping"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "domain_ids_max", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max_inc")

