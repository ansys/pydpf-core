from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from /shared/home1/cbellot/ansys_inc/v212/aisol/dll/linx64/libAns.Dpf.Native.so plugin, from "filter" category
"""

#internal name: core::field::band_pass_fc
#scripting name: field_band_pass_fc
class _InputsFieldBandPassFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(field_band_pass_fc._spec().inputs, op)
        self.fields_container = Input(field_band_pass_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.min_threshold = Input(field_band_pass_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.min_threshold)
        self.max_threshold = Input(field_band_pass_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.max_threshold)

class _OutputsFieldBandPassFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(field_band_pass_fc._spec().outputs, op)
        self.fields_container = Output(field_band_pass_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class field_band_pass_fc(Operator):
    """The band pass filter returns all the values strictly superior to the min threshold value and stricly inferior to the max threshold value in input.

      available inputs:
         fields_container (FieldsContainer)
         min_threshold (float, Field)
         max_threshold (float, Field)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      op = operators.filter.field_band_pass_fc()

    """
    def __init__(self, fields_container=None, min_threshold=None, max_threshold=None, config=None, server=None):
        super().__init__(name="core::field::band_pass_fc", config = config, server = server)
        self.inputs = _InputsFieldBandPassFc(self)
        self.outputs = _OutputsFieldBandPassFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if min_threshold !=None:
            self.inputs.min_threshold.connect(min_threshold)
        if max_threshold !=None:
            self.inputs.max_threshold.connect(max_threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The band pass filter returns all the values strictly superior to the min threshold value and stricly inferior to the max threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "min_threshold", type_names=["double","field"], optional=False, document="""a min threshold scalar or a field containing one value is expected"""), 
                                 2 : PinSpecification(name = "max_threshold", type_names=["double","field"], optional=False, document="""a max threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::field::band_pass_fc")

#internal name: core::scoping::low_pass
#scripting name: scoping_low_pass
class _InputsScopingLowPass(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(scoping_low_pass._spec().inputs, op)
        self.field = Input(scoping_low_pass._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.threshold = Input(scoping_low_pass._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.threshold)

class _OutputsScopingLowPass(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(scoping_low_pass._spec().outputs, op)
        self.scoping = Output(scoping_low_pass._spec().output_pin(0), 0, op) 
        self._outputs.append(self.scoping)

class scoping_low_pass(Operator):
    """The low pass filter returns all the values strictly inferior to the threshold value in input.

      available inputs:
         field (Field, FieldsContainer)
         threshold (float, Field)

      available outputs:
         scoping (Scoping)

      Examples
      --------
      op = operators.filter.scoping_low_pass()

    """
    def __init__(self, field=None, threshold=None, config=None, server=None):
        super().__init__(name="core::scoping::low_pass", config = config, server = server)
        self.inputs = _InputsScopingLowPass(self)
        self.outputs = _OutputsScopingLowPass(self)
        if field !=None:
            self.inputs.field.connect(field)
        if threshold !=None:
            self.inputs.threshold.connect(threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The low pass filter returns all the values strictly inferior to the threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "threshold", type_names=["double","field"], optional=False, document="""a threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::scoping::low_pass")

#internal name: core::field::low_pass
#scripting name: field_low_pass
class _InputsFieldLowPass(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(field_low_pass._spec().inputs, op)
        self.field = Input(field_low_pass._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.threshold = Input(field_low_pass._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.threshold)

class _OutputsFieldLowPass(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(field_low_pass._spec().outputs, op)
        self.field = Output(field_low_pass._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class field_low_pass(Operator):
    """The low pass filter returns all the values strictly inferior to the threshold value in input.

      available inputs:
         field (Field, FieldsContainer)
         threshold (float, Field)

      available outputs:
         field (Field)

      Examples
      --------
      op = operators.filter.field_low_pass()

    """
    def __init__(self, field=None, threshold=None, config=None, server=None):
        super().__init__(name="core::field::low_pass", config = config, server = server)
        self.inputs = _InputsFieldLowPass(self)
        self.outputs = _OutputsFieldLowPass(self)
        if field !=None:
            self.inputs.field.connect(field)
        if threshold !=None:
            self.inputs.threshold.connect(threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The low pass filter returns all the values strictly inferior to the threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "threshold", type_names=["double","field"], optional=False, document="""a threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::field::low_pass")

#internal name: core::field::high_pass_fc
#scripting name: field_high_pass_fc
class _InputsFieldHighPassFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(field_high_pass_fc._spec().inputs, op)
        self.fields_container = Input(field_high_pass_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.threshold = Input(field_high_pass_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.threshold)

class _OutputsFieldHighPassFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(field_high_pass_fc._spec().outputs, op)
        self.fields_container = Output(field_high_pass_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class field_high_pass_fc(Operator):
    """The high pass filter returns all the values strictly superior to the threshold value in input.

      available inputs:
         fields_container (FieldsContainer)
         threshold (float, Field)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      op = operators.filter.field_high_pass_fc()

    """
    def __init__(self, fields_container=None, threshold=None, config=None, server=None):
        super().__init__(name="core::field::high_pass_fc", config = config, server = server)
        self.inputs = _InputsFieldHighPassFc(self)
        self.outputs = _OutputsFieldHighPassFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if threshold !=None:
            self.inputs.threshold.connect(threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The high pass filter returns all the values strictly superior to the threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "threshold", type_names=["double","field"], optional=False, document="""a threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::field::high_pass_fc")

#internal name: core::scoping::high_pass
#scripting name: scoping_high_pass
class _InputsScopingHighPass(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(scoping_high_pass._spec().inputs, op)
        self.field = Input(scoping_high_pass._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.threshold = Input(scoping_high_pass._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.threshold)

class _OutputsScopingHighPass(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(scoping_high_pass._spec().outputs, op)
        self.scoping = Output(scoping_high_pass._spec().output_pin(0), 0, op) 
        self._outputs.append(self.scoping)

class scoping_high_pass(Operator):
    """The high pass filter returns all the values strictly superior to the threshold value in input.

      available inputs:
         field (Field, FieldsContainer)
         threshold (float, Field)

      available outputs:
         scoping (Scoping)

      Examples
      --------
      op = operators.filter.scoping_high_pass()

    """
    def __init__(self, field=None, threshold=None, config=None, server=None):
        super().__init__(name="core::scoping::high_pass", config = config, server = server)
        self.inputs = _InputsScopingHighPass(self)
        self.outputs = _OutputsScopingHighPass(self)
        if field !=None:
            self.inputs.field.connect(field)
        if threshold !=None:
            self.inputs.threshold.connect(threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The high pass filter returns all the values strictly superior to the threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "threshold", type_names=["double","field"], optional=False, document="""a threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::scoping::high_pass")

#internal name: core::field::low_pass_fc
#scripting name: field_low_pass_fc
class _InputsFieldLowPassFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(field_low_pass_fc._spec().inputs, op)
        self.fields_container = Input(field_low_pass_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.threshold = Input(field_low_pass_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.threshold)

class _OutputsFieldLowPassFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(field_low_pass_fc._spec().outputs, op)
        self.fields_container = Output(field_low_pass_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class field_low_pass_fc(Operator):
    """The low pass filter returns all the values strictly inferior to the threshold value in input.

      available inputs:
         fields_container (FieldsContainer)
         threshold (float, Field)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      op = operators.filter.field_low_pass_fc()

    """
    def __init__(self, fields_container=None, threshold=None, config=None, server=None):
        super().__init__(name="core::field::low_pass_fc", config = config, server = server)
        self.inputs = _InputsFieldLowPassFc(self)
        self.outputs = _OutputsFieldLowPassFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if threshold !=None:
            self.inputs.threshold.connect(threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The low pass filter returns all the values strictly inferior to the threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "threshold", type_names=["double","field"], optional=False, document="""a threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::field::low_pass_fc")

#internal name: core::field::band_pass
#scripting name: field_band_pass
class _InputsFieldBandPass(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(field_band_pass._spec().inputs, op)
        self.field = Input(field_band_pass._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.min_threshold = Input(field_band_pass._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.min_threshold)
        self.max_threshold = Input(field_band_pass._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.max_threshold)

class _OutputsFieldBandPass(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(field_band_pass._spec().outputs, op)
        self.field = Output(field_band_pass._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class field_band_pass(Operator):
    """The band pass filter returns all the values strictly superior to the min threshold value and stricly inferior to the max threshold value in input.

      available inputs:
         field (Field, FieldsContainer)
         min_threshold (float, Field)
         max_threshold (float, Field)

      available outputs:
         field (Field)

      Examples
      --------
      op = operators.filter.field_band_pass()

    """
    def __init__(self, field=None, min_threshold=None, max_threshold=None, config=None, server=None):
        super().__init__(name="core::field::band_pass", config = config, server = server)
        self.inputs = _InputsFieldBandPass(self)
        self.outputs = _OutputsFieldBandPass(self)
        if field !=None:
            self.inputs.field.connect(field)
        if min_threshold !=None:
            self.inputs.min_threshold.connect(min_threshold)
        if max_threshold !=None:
            self.inputs.max_threshold.connect(max_threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The band pass filter returns all the values strictly superior to the min threshold value and stricly inferior to the max threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "min_threshold", type_names=["double","field"], optional=False, document="""a min threshold scalar or a field containing one value is expected"""), 
                                 2 : PinSpecification(name = "max_threshold", type_names=["double","field"], optional=False, document="""a max threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::field::band_pass")

#internal name: core::field::high_pass
#scripting name: field_high_pass
class _InputsFieldHighPass(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(field_high_pass._spec().inputs, op)
        self.field = Input(field_high_pass._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.threshold = Input(field_high_pass._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.threshold)

class _OutputsFieldHighPass(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(field_high_pass._spec().outputs, op)
        self.field = Output(field_high_pass._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class field_high_pass(Operator):
    """The high pass filter returns all the values strictly superior to the threshold value in input.

      available inputs:
         field (Field, FieldsContainer)
         threshold (float, Field)

      available outputs:
         field (Field)

      Examples
      --------
      op = operators.filter.field_high_pass()

    """
    def __init__(self, field=None, threshold=None, config=None, server=None):
        super().__init__(name="core::field::high_pass", config = config, server = server)
        self.inputs = _InputsFieldHighPass(self)
        self.outputs = _OutputsFieldHighPass(self)
        if field !=None:
            self.inputs.field.connect(field)
        if threshold !=None:
            self.inputs.threshold.connect(threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The high pass filter returns all the values strictly superior to the threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "threshold", type_names=["double","field"], optional=False, document="""a threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::field::high_pass")

#internal name: core::scoping::band_pass
#scripting name: scoping_band_pass
class _InputsScopingBandPass(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(scoping_band_pass._spec().inputs, op)
        self.field = Input(scoping_band_pass._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.min_threshold = Input(scoping_band_pass._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.min_threshold)
        self.max_threshold = Input(scoping_band_pass._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.max_threshold)

class _OutputsScopingBandPass(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(scoping_band_pass._spec().outputs, op)
        self.scoping = Output(scoping_band_pass._spec().output_pin(0), 0, op) 
        self._outputs.append(self.scoping)

class scoping_band_pass(Operator):
    """The band pass filter returns all the values strictly superior to the min threshold value and stricly inferior to the max threshold value in input.

      available inputs:
         field (Field, FieldsContainer)
         min_threshold (float, Field)
         max_threshold (float, Field)

      available outputs:
         scoping (Scoping)

      Examples
      --------
      op = operators.filter.scoping_band_pass()

    """
    def __init__(self, field=None, min_threshold=None, max_threshold=None, config=None, server=None):
        super().__init__(name="core::scoping::band_pass", config = config, server = server)
        self.inputs = _InputsScopingBandPass(self)
        self.outputs = _OutputsScopingBandPass(self)
        if field !=None:
            self.inputs.field.connect(field)
        if min_threshold !=None:
            self.inputs.min_threshold.connect(min_threshold)
        if max_threshold !=None:
            self.inputs.max_threshold.connect(max_threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The band pass filter returns all the values strictly superior to the min threshold value and stricly inferior to the max threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "min_threshold", type_names=["double","field"], optional=False, document="""a min threshold scalar or a field containing one value is expected"""), 
                                 2 : PinSpecification(name = "max_threshold", type_names=["double","field"], optional=False, document="""a max threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::scoping::band_pass")

