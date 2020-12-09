from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

#internal name: core::field::low_pass_fc
#scripting name: field.low_pass_fc
def _get_input_spec_low_pass_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "threshold", type_names = ["double","field"], optional = False, document = """a threshold scalar or a field containing one value is expected""")
    inputs_dict_low_pass_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_low_pass_fc[pin]

def _get_output_spec_low_pass_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_low_pass_fc = { 
        0 : outpin0
    }
    return outputs_dict_low_pass_fc[pin]

class _InputSpecLowPassFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_low_pass_fc(0), 0, op, -1) 
        self.threshold = _Input(_get_input_spec_low_pass_fc(1), 1, op, -1) 

class _OutputSpecLowPassFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_low_pass_fc(0), 0, op) 

class _LowPassFc:
    """Operator's description:
Internal name is "core::field::low_pass_fc"
Scripting name is "field.low_pass_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("core::field::low_pass_fc")
- using dpf.operators.filter.field.low_pass_fc()

Input list: 
   0: fields_container (field or fields container with only one field is expected)
   1: threshold (a threshold scalar or a field containing one value is expected)
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "core::field::low_pass_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecLowPassFc(self._op)
         self.outputs = _OutputSpecLowPassFc(self._op)

def low_pass_fc():
    return _LowPassFc()

#internal name: core::field::band_pass_fc
#scripting name: field.band_pass_fc
def _get_input_spec_band_pass_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "min_threshold", type_names = ["double","field"], optional = False, document = """a min threshold scalar or a field containing one value is expected""")
    inpin2 = _PinSpecification(name = "max_threshold", type_names = ["double","field"], optional = False, document = """a max threshold scalar or a field containing one value is expected""")
    inputs_dict_band_pass_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_band_pass_fc[pin]

def _get_output_spec_band_pass_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_band_pass_fc = { 
        0 : outpin0
    }
    return outputs_dict_band_pass_fc[pin]

class _InputSpecBandPassFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_band_pass_fc(0), 0, op, -1) 
        self.min_threshold = _Input(_get_input_spec_band_pass_fc(1), 1, op, -1) 
        self.max_threshold = _Input(_get_input_spec_band_pass_fc(2), 2, op, -1) 

class _OutputSpecBandPassFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_band_pass_fc(0), 0, op) 

class _BandPassFc:
    """Operator's description:
Internal name is "core::field::band_pass_fc"
Scripting name is "field.band_pass_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("core::field::band_pass_fc")
- using dpf.operators.filter.field.band_pass_fc()

Input list: 
   0: fields_container (field or fields container with only one field is expected)
   1: min_threshold (a min threshold scalar or a field containing one value is expected)
   2: max_threshold (a max threshold scalar or a field containing one value is expected)
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "core::field::band_pass_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecBandPassFc(self._op)
         self.outputs = _OutputSpecBandPassFc(self._op)

def band_pass_fc():
    return _BandPassFc()

#internal name: core::field::high_pass
#scripting name: field.high_pass
def _get_input_spec_high_pass(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "threshold", type_names = ["double","field"], optional = False, document = """a threshold scalar or a field containing one value is expected""")
    inputs_dict_high_pass = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_high_pass[pin]

def _get_output_spec_high_pass(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_high_pass = { 
        0 : outpin0
    }
    return outputs_dict_high_pass[pin]

class _InputSpecHighPass(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_high_pass(0), 0, op, -1) 
        self.threshold = _Input(_get_input_spec_high_pass(1), 1, op, -1) 

class _OutputSpecHighPass(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_high_pass(0), 0, op) 

class _HighPass:
    """Operator's description:
Internal name is "core::field::high_pass"
Scripting name is "field.high_pass"

This operator can be instantiated in both following ways:
- using dpf.Operator("core::field::high_pass")
- using dpf.operators.filter.field.high_pass()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: threshold (a threshold scalar or a field containing one value is expected)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "core::field::high_pass"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecHighPass(self._op)
         self.outputs = _OutputSpecHighPass(self._op)

def high_pass():
    return _HighPass()

#internal name: core::field::high_pass_fc
#scripting name: field.high_pass_fc
def _get_input_spec_high_pass_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "threshold", type_names = ["double","field"], optional = False, document = """a threshold scalar or a field containing one value is expected""")
    inputs_dict_high_pass_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_high_pass_fc[pin]

def _get_output_spec_high_pass_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_high_pass_fc = { 
        0 : outpin0
    }
    return outputs_dict_high_pass_fc[pin]

class _InputSpecHighPassFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_high_pass_fc(0), 0, op, -1) 
        self.threshold = _Input(_get_input_spec_high_pass_fc(1), 1, op, -1) 

class _OutputSpecHighPassFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_high_pass_fc(0), 0, op) 

class _HighPassFc:
    """Operator's description:
Internal name is "core::field::high_pass_fc"
Scripting name is "field.high_pass_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("core::field::high_pass_fc")
- using dpf.operators.filter.field.high_pass_fc()

Input list: 
   0: fields_container (field or fields container with only one field is expected)
   1: threshold (a threshold scalar or a field containing one value is expected)
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "core::field::high_pass_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecHighPassFc(self._op)
         self.outputs = _OutputSpecHighPassFc(self._op)

def high_pass_fc():
    return _HighPassFc()

#internal name: core::field::low_pass
#scripting name: field.low_pass
def _get_input_spec_low_pass(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "threshold", type_names = ["double","field"], optional = False, document = """a threshold scalar or a field containing one value is expected""")
    inputs_dict_low_pass = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_low_pass[pin]

def _get_output_spec_low_pass(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_low_pass = { 
        0 : outpin0
    }
    return outputs_dict_low_pass[pin]

class _InputSpecLowPass(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_low_pass(0), 0, op, -1) 
        self.threshold = _Input(_get_input_spec_low_pass(1), 1, op, -1) 

class _OutputSpecLowPass(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_low_pass(0), 0, op) 

class _LowPass:
    """Operator's description:
Internal name is "core::field::low_pass"
Scripting name is "field.low_pass"

This operator can be instantiated in both following ways:
- using dpf.Operator("core::field::low_pass")
- using dpf.operators.filter.field.low_pass()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: threshold (a threshold scalar or a field containing one value is expected)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "core::field::low_pass"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecLowPass(self._op)
         self.outputs = _OutputSpecLowPass(self._op)

def low_pass():
    return _LowPass()

#internal name: core::field::band_pass
#scripting name: field.band_pass
def _get_input_spec_band_pass(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "min_threshold", type_names = ["double","field"], optional = False, document = """a min threshold scalar or a field containing one value is expected""")
    inpin2 = _PinSpecification(name = "max_threshold", type_names = ["double","field"], optional = False, document = """a max threshold scalar or a field containing one value is expected""")
    inputs_dict_band_pass = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_band_pass[pin]

def _get_output_spec_band_pass(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_band_pass = { 
        0 : outpin0
    }
    return outputs_dict_band_pass[pin]

class _InputSpecBandPass(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_band_pass(0), 0, op, -1) 
        self.min_threshold = _Input(_get_input_spec_band_pass(1), 1, op, -1) 
        self.max_threshold = _Input(_get_input_spec_band_pass(2), 2, op, -1) 

class _OutputSpecBandPass(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_band_pass(0), 0, op) 

class _BandPass:
    """Operator's description:
Internal name is "core::field::band_pass"
Scripting name is "field.band_pass"

This operator can be instantiated in both following ways:
- using dpf.Operator("core::field::band_pass")
- using dpf.operators.filter.field.band_pass()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: min_threshold (a min threshold scalar or a field containing one value is expected)
   2: max_threshold (a max threshold scalar or a field containing one value is expected)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "core::field::band_pass"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecBandPass(self._op)
         self.outputs = _OutputSpecBandPass(self._op)

def band_pass():
    return _BandPass()

