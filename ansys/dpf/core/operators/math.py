from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "math" category
"""

#internal name: minus
#scripting name: minus
def _get_input_spec_minus(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_minus = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_minus[pin]

def _get_output_spec_minus(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_minus = { 
        0 : outpin0
    }
    return outputs_dict_minus[pin]

class _InputSpecMinus(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_minus(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_minus(1), 1, op, -1) 

class _OutputSpecMinus(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_minus(0), 0, op) 

class _Minus(_Operator):
    def __init__(self):
         super().__init__("minus")
         self._name = "minus"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecMinus(self._op)
         self.outputs = _OutputSpecMinus(self._op)

def minus():
    """Operator's description:
Internal name is "minus"
Scripting name is "minus"

This operator can be instantiated in both following ways:
- using dpf.Operator("minus")
- using dpf.operators.math.minus()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
   1: fieldB (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _Minus()

#internal name: cplx_multiply
#scripting name: cplx_multiply
def _get_input_spec_cplx_multiply(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_multiply = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_cplx_multiply[pin]

def _get_output_spec_cplx_multiply(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_multiply = { 
        0 : outpin0
    }
    return outputs_dict_cplx_multiply[pin]

class _InputSpecCplxMultiply(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_cplx_multiply(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_cplx_multiply(1), 1, op, -1) 

class _OutputSpecCplxMultiply(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cplx_multiply(0), 0, op) 

class _CplxMultiply(_Operator):
    def __init__(self):
         super().__init__("cplx_multiply")
         self._name = "cplx_multiply"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCplxMultiply(self._op)
         self.outputs = _OutputSpecCplxMultiply(self._op)

def cplx_multiply():
    """Operator's description:
Internal name is "cplx_multiply"
Scripting name is "cplx_multiply"

This operator can be instantiated in both following ways:
- using dpf.Operator("cplx_multiply")
- using dpf.operators.math.cplx_multiply()

Input list: 
   0: fields_containerA 
   1: fields_containerB 
Output list: 
   0: fields_container 
"""
    return _CplxMultiply()

#internal name: unit_convert
#scripting name: unit_convert
def _get_input_spec_unit_convert(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = False, document = """unit as a string, ex 'm' for meter, 'Pa' for pascal,...""")
    inputs_dict_unit_convert = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_unit_convert[pin]

def _get_output_spec_unit_convert(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_unit_convert = { 
        0 : outpin0
    }
    return outputs_dict_unit_convert[pin]

class _InputSpecUnitConvert(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_unit_convert(0), 0, op, -1) 
        self.unit_name = _Input(_get_input_spec_unit_convert(1), 1, op, -1) 

class _OutputSpecUnitConvert(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_unit_convert(0), 0, op) 

class _UnitConvert(_Operator):
    def __init__(self):
         super().__init__("unit_convert")
         self._name = "unit_convert"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecUnitConvert(self._op)
         self.outputs = _OutputSpecUnitConvert(self._op)

def unit_convert():
    """Operator's description:
Internal name is "unit_convert"
Scripting name is "unit_convert"

This operator can be instantiated in both following ways:
- using dpf.Operator("unit_convert")
- using dpf.operators.math.unit_convert()

Input list: 
   0: field 
   1: unit_name (unit as a string, ex 'm' for meter, 'Pa' for pascal,...)
Output list: 
   0: field 
"""
    return _UnitConvert()

#internal name: unit_convert_fc
#scripting name: unit_convert_fc
def _get_input_spec_unit_convert_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = False, document = """unit as a string, ex 'm' for meter, 'Pa' for pascal,...""")
    inputs_dict_unit_convert_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_unit_convert_fc[pin]

def _get_output_spec_unit_convert_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_unit_convert_fc = { 
        0 : outpin0
    }
    return outputs_dict_unit_convert_fc[pin]

class _InputSpecUnitConvertFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_unit_convert_fc(0), 0, op, -1) 
        self.unit_name = _Input(_get_input_spec_unit_convert_fc(1), 1, op, -1) 

class _OutputSpecUnitConvertFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_unit_convert_fc(0), 0, op) 

class _UnitConvertFc(_Operator):
    def __init__(self):
         super().__init__("unit_convert_fc")
         self._name = "unit_convert_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecUnitConvertFc(self._op)
         self.outputs = _OutputSpecUnitConvertFc(self._op)

def unit_convert_fc():
    """Operator's description:
Internal name is "unit_convert_fc"
Scripting name is "unit_convert_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("unit_convert_fc")
- using dpf.operators.math.unit_convert_fc()

Input list: 
   0: fields_container 
   1: unit_name (unit as a string, ex 'm' for meter, 'Pa' for pascal,...)
Output list: 
   0: fields_container 
"""
    return _UnitConvertFc()

#internal name: add
#scripting name: add
def _get_input_spec_add(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_add = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_add[pin]

def _get_output_spec_add(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_add = { 
        0 : outpin0
    }
    return outputs_dict_add[pin]

class _InputSpecAdd(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_add(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_add(1), 1, op, -1) 

class _OutputSpecAdd(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_add(0), 0, op) 

class _Add(_Operator):
    def __init__(self):
         super().__init__("add")
         self._name = "add"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAdd(self._op)
         self.outputs = _OutputSpecAdd(self._op)

def add():
    """Operator's description:
Internal name is "add"
Scripting name is "add"

This operator can be instantiated in both following ways:
- using dpf.Operator("add")
- using dpf.operators.math.add()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
   1: fieldB (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _Add()

#internal name: add_fc
#scripting name: add_fc
def _get_input_spec_add_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container1", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_container2", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_add_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_add_fc[pin]

def _get_output_spec_add_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_add_fc = { 
        0 : outpin0
    }
    return outputs_dict_add_fc[pin]

class _InputSpecAddFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container1 = _Input(_get_input_spec_add_fc(0), 0, op, 0) 
        self.fields_container2 = _Input(_get_input_spec_add_fc(1), 1, op, -1) 

class _OutputSpecAddFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_add_fc(0), 0, op) 

class _AddFc(_Operator):
    def __init__(self):
         super().__init__("add_fc")
         self._name = "add_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAddFc(self._op)
         self.outputs = _OutputSpecAddFc(self._op)

def add_fc():
    """Operator's description:
Internal name is "add_fc"
Scripting name is "add_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("add_fc")
- using dpf.operators.math.add_fc()

Input list: 
   0: fields_container1 
   1: fields_container2 
Output list: 
   0: fields_container 
"""
    return _AddFc()

#internal name: scale
#scripting name: scale
def _get_input_spec_scale(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double","field"], optional = False, document = """Double/Field scoped on overall""")
    inpin2 = _PinSpecification(name = "boolean", type_names = ["bool"], optional = True, document = """bool(optional, default false) if set to true, output of scale is mane dimensionless""")
    inputs_dict_scale = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_scale[pin]

def _get_output_spec_scale(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_scale = { 
        0 : outpin0
    }
    return outputs_dict_scale[pin]

class _InputSpecScale(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_scale(0), 0, op, -1) 
        self.ponderation = _Input(_get_input_spec_scale(1), 1, op, -1) 
        self.boolean = _Input(_get_input_spec_scale(2), 2, op, -1) 

class _OutputSpecScale(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_scale(0), 0, op) 

class _Scale(_Operator):
    def __init__(self):
         super().__init__("scale")
         self._name = "scale"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecScale(self._op)
         self.outputs = _OutputSpecScale(self._op)

def scale():
    """Operator's description:
Internal name is "scale"
Scripting name is "scale"

This operator can be instantiated in both following ways:
- using dpf.Operator("scale")
- using dpf.operators.math.scale()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: ponderation (Double/Field scoped on overall)
   2: boolean (bool(optional, default false) if set to true, output of scale is mane dimensionless)
Output list: 
   0: field 
"""
    return _Scale()

#internal name: Pow_fc
#scripting name: pow_fc
def _get_input_spec_pow_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "factor", type_names = ["double"], optional = False, document = """""")
    inputs_dict_pow_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_pow_fc[pin]

def _get_output_spec_pow_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_pow_fc = { 
        0 : outpin0
    }
    return outputs_dict_pow_fc[pin]

class _InputSpecPowFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_pow_fc(0), 0, op, -1) 
        self.factor = _Input(_get_input_spec_pow_fc(1), 1, op, -1) 

class _OutputSpecPowFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_pow_fc(0), 0, op) 

class _PowFc(_Operator):
    def __init__(self):
         super().__init__("Pow_fc")
         self._name = "Pow_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPowFc(self._op)
         self.outputs = _OutputSpecPowFc(self._op)

def pow_fc():
    """Operator's description:
Internal name is "Pow_fc"
Scripting name is "pow_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("Pow_fc")
- using dpf.operators.math.pow_fc()

Input list: 
   0: fields_container 
   1: factor 
Output list: 
   0: fields_container 
"""
    return _PowFc()

#internal name: phase_of_max
#scripting name: phase_of_max
def _get_input_spec_phase_of_max(pin):
    inpin0 = _PinSpecification(name = "real_field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "imaginary_field", type_names = ["field"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin3 = _PinSpecification(name = "phase_increment", type_names = ["double"], optional = False, document = """Phase increment.""")
    inputs_dict_phase_of_max = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    return inputs_dict_phase_of_max[pin]

def _get_output_spec_phase_of_max(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_phase_of_max = { 
        0 : outpin0
    }
    return outputs_dict_phase_of_max[pin]

class _InputSpecPhaseOfMax(_Inputs):
    def __init__(self, op: _Operator):
        self.real_field = _Input(_get_input_spec_phase_of_max(0), 0, op, -1) 
        self.imaginary_field = _Input(_get_input_spec_phase_of_max(1), 1, op, -1) 
        self.abs_value = _Input(_get_input_spec_phase_of_max(2), 2, op, -1) 
        self.phase_increment = _Input(_get_input_spec_phase_of_max(3), 3, op, -1) 

class _OutputSpecPhaseOfMax(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_phase_of_max(0), 0, op) 

class _PhaseOfMax(_Operator):
    def __init__(self):
         super().__init__("phase_of_max")
         self._name = "phase_of_max"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPhaseOfMax(self._op)
         self.outputs = _OutputSpecPhaseOfMax(self._op)

def phase_of_max():
    """Operator's description:
Internal name is "phase_of_max"
Scripting name is "phase_of_max"

This operator can be instantiated in both following ways:
- using dpf.Operator("phase_of_max")
- using dpf.operators.math.phase_of_max()

Input list: 
   0: real_field 
   1: imaginary_field 
   2: abs_value (Should use absolute value.)
   3: phase_increment (Phase increment.)
Output list: 
   0: field 
"""
    return _PhaseOfMax()

#internal name: sin_fc
#scripting name: sin_fc
def _get_input_spec_sin_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_sin_fc = { 
        0 : inpin0
    }
    return inputs_dict_sin_fc[pin]

def _get_output_spec_sin_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sin_fc = { 
        0 : outpin0
    }
    return outputs_dict_sin_fc[pin]

class _InputSpecSinFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_sin_fc(0), 0, op, -1) 

class _OutputSpecSinFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_sin_fc(0), 0, op) 

class _SinFc(_Operator):
    def __init__(self):
         super().__init__("sin_fc")
         self._name = "sin_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSinFc(self._op)
         self.outputs = _OutputSpecSinFc(self._op)

def sin_fc():
    """Operator's description:
Internal name is "sin_fc"
Scripting name is "sin_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("sin_fc")
- using dpf.operators.math.sin_fc()

Input list: 
   0: fields_container 
Output list: 
   0: fields_container 
"""
    return _SinFc()

#internal name: add_constant
#scripting name: add_constant
def _get_input_spec_add_constant(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double"], optional = False, document = """double or vector of double""")
    inputs_dict_add_constant = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_add_constant[pin]

def _get_output_spec_add_constant(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_add_constant = { 
        0 : outpin0
    }
    return outputs_dict_add_constant[pin]

class _InputSpecAddConstant(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_add_constant(0), 0, op, -1) 
        self.ponderation = _Input(_get_input_spec_add_constant(1), 1, op, -1) 

class _OutputSpecAddConstant(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_add_constant(0), 0, op) 

class _AddConstant(_Operator):
    def __init__(self):
         super().__init__("add_constant")
         self._name = "add_constant"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAddConstant(self._op)
         self.outputs = _OutputSpecAddConstant(self._op)

def add_constant():
    """Operator's description:
Internal name is "add_constant"
Scripting name is "add_constant"

This operator can be instantiated in both following ways:
- using dpf.Operator("add_constant")
- using dpf.operators.math.add_constant()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: ponderation (double or vector of double)
Output list: 
   0: field 
"""
    return _AddConstant()

#internal name: Pow
#scripting name: pow
def _get_input_spec_pow(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "factor", type_names = ["double"], optional = False, document = """""")
    inputs_dict_pow = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_pow[pin]

def _get_output_spec_pow(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_pow = { 
        0 : outpin0
    }
    return outputs_dict_pow[pin]

class _InputSpecPow(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_pow(0), 0, op, -1) 
        self.factor = _Input(_get_input_spec_pow(1), 1, op, -1) 

class _OutputSpecPow(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_pow(0), 0, op) 

class _Pow(_Operator):
    def __init__(self):
         super().__init__("Pow")
         self._name = "Pow"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPow(self._op)
         self.outputs = _OutputSpecPow(self._op)

def pow():
    """Operator's description:
Internal name is "Pow"
Scripting name is "pow"

This operator can be instantiated in both following ways:
- using dpf.Operator("Pow")
- using dpf.operators.math.pow()

Input list: 
   0: field 
   1: factor 
Output list: 
   0: field 
"""
    return _Pow()

#internal name: add_constant_fc
#scripting name: add_constant_fc
def _get_input_spec_add_constant_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double"], optional = False, document = """double or vector of double""")
    inputs_dict_add_constant_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_add_constant_fc[pin]

def _get_output_spec_add_constant_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_add_constant_fc = { 
        0 : outpin0
    }
    return outputs_dict_add_constant_fc[pin]

class _InputSpecAddConstantFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_add_constant_fc(0), 0, op, -1) 
        self.ponderation = _Input(_get_input_spec_add_constant_fc(1), 1, op, -1) 

class _OutputSpecAddConstantFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_add_constant_fc(0), 0, op) 

class _AddConstantFc(_Operator):
    def __init__(self):
         super().__init__("add_constant_fc")
         self._name = "add_constant_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAddConstantFc(self._op)
         self.outputs = _OutputSpecAddConstantFc(self._op)

def add_constant_fc():
    """Operator's description:
Internal name is "add_constant_fc"
Scripting name is "add_constant_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("add_constant_fc")
- using dpf.operators.math.add_constant_fc()

Input list: 
   0: fields_container (field or fields container with only one field is expected)
   1: ponderation (double or vector of double)
Output list: 
   0: fields_container 
"""
    return _AddConstantFc()

#internal name: scale_fc
#scripting name: scale_fc
def _get_input_spec_scale_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double","field"], optional = False, document = """Double/Field scoped on overall""")
    inpin2 = _PinSpecification(name = "boolean", type_names = ["bool"], optional = True, document = """bool(optional, default false) if set to true, output of scale is mane dimensionless""")
    inputs_dict_scale_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_scale_fc[pin]

def _get_output_spec_scale_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_scale_fc = { 
        0 : outpin0
    }
    return outputs_dict_scale_fc[pin]

class _InputSpecScaleFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_scale_fc(0), 0, op, -1) 
        self.ponderation = _Input(_get_input_spec_scale_fc(1), 1, op, -1) 
        self.boolean = _Input(_get_input_spec_scale_fc(2), 2, op, -1) 

class _OutputSpecScaleFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_scale_fc(0), 0, op) 

class _ScaleFc(_Operator):
    def __init__(self):
         super().__init__("scale_fc")
         self._name = "scale_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecScaleFc(self._op)
         self.outputs = _OutputSpecScaleFc(self._op)

def scale_fc():
    """Operator's description:
Internal name is "scale_fc"
Scripting name is "scale_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("scale_fc")
- using dpf.operators.math.scale_fc()

Input list: 
   0: fields_container (field or fields container with only one field is expected)
   1: ponderation (Double/Field scoped on overall)
   2: boolean (bool(optional, default false) if set to true, output of scale is mane dimensionless)
Output list: 
   0: fields_container 
"""
    return _ScaleFc()

#internal name: centroid
#scripting name: centroid
def _get_input_spec_centroid(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin2 = _PinSpecification(name = "factor", type_names = ["double"], optional = False, document = """Scalar""")
    inputs_dict_centroid = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_centroid[pin]

def _get_output_spec_centroid(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_centroid = { 
        0 : outpin0
    }
    return outputs_dict_centroid[pin]

class _InputSpecCentroid(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_centroid(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_centroid(1), 1, op, -1) 
        self.factor = _Input(_get_input_spec_centroid(2), 2, op, -1) 

class _OutputSpecCentroid(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_centroid(0), 0, op) 

class _Centroid(_Operator):
    def __init__(self):
         super().__init__("centroid")
         self._name = "centroid"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCentroid(self._op)
         self.outputs = _OutputSpecCentroid(self._op)

def centroid():
    """Operator's description:
Internal name is "centroid"
Scripting name is "centroid"

This operator can be instantiated in both following ways:
- using dpf.Operator("centroid")
- using dpf.operators.math.centroid()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
   1: fieldB (field or fields container with only one field is expected)
   2: factor (Scalar)
Output list: 
   0: field 
"""
    return _Centroid()

#internal name: sweeping_phase
#scripting name: sweeping_phase
def _get_input_spec_sweeping_phase(pin):
    inpin0 = _PinSpecification(name = "real_field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "imaginary_field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin2 = _PinSpecification(name = "angle", type_names = ["double"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = False, document = """String Unit""")
    inpin4 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = False, document = """""")
    inpin5 = _PinSpecification(name = "imaginary_part_null", type_names = ["bool"], optional = False, document = """if the imaginary part field is empty and this pin is true, then the imaginary part is supposed to be 0 (default is false)""")
    inputs_dict_sweeping_phase = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5
    }
    return inputs_dict_sweeping_phase[pin]

def _get_output_spec_sweeping_phase(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sweeping_phase = { 
        0 : outpin0
    }
    return outputs_dict_sweeping_phase[pin]

class _InputSpecSweepingPhase(_Inputs):
    def __init__(self, op: _Operator):
        self.real_field = _Input(_get_input_spec_sweeping_phase(0), 0, op, -1) 
        self.imaginary_field = _Input(_get_input_spec_sweeping_phase(1), 1, op, -1) 
        self.angle = _Input(_get_input_spec_sweeping_phase(2), 2, op, -1) 
        self.unit_name = _Input(_get_input_spec_sweeping_phase(3), 3, op, -1) 
        self.abs_value = _Input(_get_input_spec_sweeping_phase(4), 4, op, -1) 
        self.imaginary_part_null = _Input(_get_input_spec_sweeping_phase(5), 5, op, -1) 

class _OutputSpecSweepingPhase(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_sweeping_phase(0), 0, op) 

class _SweepingPhase(_Operator):
    def __init__(self):
         super().__init__("sweeping_phase")
         self._name = "sweeping_phase"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSweepingPhase(self._op)
         self.outputs = _OutputSpecSweepingPhase(self._op)

def sweeping_phase():
    """Operator's description:
Internal name is "sweeping_phase"
Scripting name is "sweeping_phase"

This operator can be instantiated in both following ways:
- using dpf.Operator("sweeping_phase")
- using dpf.operators.math.sweeping_phase()

Input list: 
   0: real_field (field or fields container with only one field is expected)
   1: imaginary_field (field or fields container with only one field is expected)
   2: angle 
   3: unit_name (String Unit)
   4: abs_value 
   5: imaginary_part_null (if the imaginary part field is empty and this pin is true, then the imaginary part is supposed to be 0 (default is false))
Output list: 
   0: field 
"""
    return _SweepingPhase()

#internal name: sin
#scripting name: sin
def _get_input_spec_sin(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inputs_dict_sin = { 
        0 : inpin0
    }
    return inputs_dict_sin[pin]

def _get_output_spec_sin(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sin = { 
        0 : outpin0
    }
    return outputs_dict_sin[pin]

class _InputSpecSin(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_sin(0), 0, op, -1) 

class _OutputSpecSin(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_sin(0), 0, op) 

class _Sin(_Operator):
    def __init__(self):
         super().__init__("sin")
         self._name = "sin"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSin(self._op)
         self.outputs = _OutputSpecSin(self._op)

def sin():
    """Operator's description:
Internal name is "sin"
Scripting name is "sin"

This operator can be instantiated in both following ways:
- using dpf.Operator("sin")
- using dpf.operators.math.sin()

Input list: 
   0: field 
Output list: 
   0: field 
"""
    return _Sin()

#internal name: cos
#scripting name: cos
def _get_input_spec_cos(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_cos = { 
        0 : inpin0
    }
    return inputs_dict_cos[pin]

def _get_output_spec_cos(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_cos = { 
        0 : outpin0
    }
    return outputs_dict_cos[pin]

class _InputSpecCos(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_cos(0), 0, op, -1) 

class _OutputSpecCos(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_cos(0), 0, op) 

class _Cos(_Operator):
    def __init__(self):
         super().__init__("cos")
         self._name = "cos"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCos(self._op)
         self.outputs = _OutputSpecCos(self._op)

def cos():
    """Operator's description:
Internal name is "cos"
Scripting name is "cos"

This operator can be instantiated in both following ways:
- using dpf.Operator("cos")
- using dpf.operators.math.cos()

Input list: 
   0: field (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _Cos()

#internal name: cos_fc
#scripting name: cos_fc
def _get_input_spec_cos_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_cos_fc = { 
        0 : inpin0
    }
    return inputs_dict_cos_fc[pin]

def _get_output_spec_cos_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cos_fc = { 
        0 : outpin0
    }
    return outputs_dict_cos_fc[pin]

class _InputSpecCosFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_cos_fc(0), 0, op, -1) 

class _OutputSpecCosFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cos_fc(0), 0, op) 

class _CosFc(_Operator):
    def __init__(self):
         super().__init__("cos_fc")
         self._name = "cos_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCosFc(self._op)
         self.outputs = _OutputSpecCosFc(self._op)

def cos_fc():
    """Operator's description:
Internal name is "cos_fc"
Scripting name is "cos_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("cos_fc")
- using dpf.operators.math.cos_fc()

Input list: 
   0: fields_container (field or fields container with only one field is expected)
Output list: 
   0: fields_container 
"""
    return _CosFc()

#internal name: sweeping_phase_fc
#scripting name: sweeping_phase_fc
def _get_input_spec_sweeping_phase_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "angle", type_names = ["double"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = False, document = """String Unit""")
    inpin4 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = False, document = """""")
    inputs_dict_sweeping_phase_fc = { 
        0 : inpin0,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_sweeping_phase_fc[pin]

def _get_output_spec_sweeping_phase_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sweeping_phase_fc = { 
        0 : outpin0
    }
    return outputs_dict_sweeping_phase_fc[pin]

class _InputSpecSweepingPhaseFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_sweeping_phase_fc(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_sweeping_phase_fc(2), 2, op, -1) 
        self.unit_name = _Input(_get_input_spec_sweeping_phase_fc(3), 3, op, -1) 
        self.abs_value = _Input(_get_input_spec_sweeping_phase_fc(4), 4, op, -1) 

class _OutputSpecSweepingPhaseFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_sweeping_phase_fc(0), 0, op) 

class _SweepingPhaseFc(_Operator):
    def __init__(self):
         super().__init__("sweeping_phase_fc")
         self._name = "sweeping_phase_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSweepingPhaseFc(self._op)
         self.outputs = _OutputSpecSweepingPhaseFc(self._op)

def sweeping_phase_fc():
    """Operator's description:
Internal name is "sweeping_phase_fc"
Scripting name is "sweeping_phase_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("sweeping_phase_fc")
- using dpf.operators.math.sweeping_phase_fc()

Input list: 
   0: fields_container 
   2: angle 
   3: unit_name (String Unit)
   4: abs_value 
Output list: 
   0: fields_container 
"""
    return _SweepingPhaseFc()

#internal name: sqr
#scripting name: sqr
def _get_input_spec_sqr(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqr = { 
        0 : inpin0
    }
    return inputs_dict_sqr[pin]

def _get_output_spec_sqr(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sqr = { 
        0 : outpin0
    }
    return outputs_dict_sqr[pin]

class _InputSpecSqr(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_sqr(0), 0, op, -1) 

class _OutputSpecSqr(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_sqr(0), 0, op) 

class _Sqr(_Operator):
    def __init__(self):
         super().__init__("sqr")
         self._name = "sqr"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSqr(self._op)
         self.outputs = _OutputSpecSqr(self._op)

def sqr():
    """Operator's description:
Internal name is "sqr"
Scripting name is "sqr"

This operator can be instantiated in both following ways:
- using dpf.Operator("sqr")
- using dpf.operators.math.sqr()

Input list: 
   0: field (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _Sqr()

#internal name: CplxOp
#scripting name: linear_combination
def _get_input_spec_linear_combination(pin):
    inpin0 = _PinSpecification(name = "a", type_names = ["double"], optional = False, document = """Double""")
    inpin1 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "b", type_names = ["double"], optional = False, document = """Double""")
    inpin4 = _PinSpecification(name = "fields_containerC", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_linear_combination = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_linear_combination[pin]

def _get_output_spec_linear_combination(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_linear_combination = { 
        0 : outpin0
    }
    return outputs_dict_linear_combination[pin]

class _InputSpecLinearCombination(_Inputs):
    def __init__(self, op: _Operator):
        self.a = _Input(_get_input_spec_linear_combination(0), 0, op, -1) 
        self.fields_containerA = _Input(_get_input_spec_linear_combination(1), 1, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_linear_combination(2), 2, op, -1) 
        self.b = _Input(_get_input_spec_linear_combination(3), 3, op, -1) 
        self.fields_containerC = _Input(_get_input_spec_linear_combination(4), 4, op, -1) 

class _OutputSpecLinearCombination(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_linear_combination(0), 0, op) 

class _LinearCombination(_Operator):
    def __init__(self):
         super().__init__("CplxOp")
         self._name = "CplxOp"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecLinearCombination(self._op)
         self.outputs = _OutputSpecLinearCombination(self._op)

def linear_combination():
    """Operator's description:
Internal name is "CplxOp"
Scripting name is "linear_combination"

This operator can be instantiated in both following ways:
- using dpf.Operator("CplxOp")
- using dpf.operators.math.linear_combination()

Input list: 
   0: a (Double)
   1: fields_containerA 
   2: fields_containerB 
   3: b (Double)
   4: fields_containerC 
Output list: 
   0: fields_container 
"""
    return _LinearCombination()

#internal name: sqr_fc
#scripting name: sqr_fc
def _get_input_spec_sqr_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqr_fc = { 
        0 : inpin0
    }
    return inputs_dict_sqr_fc[pin]

def _get_output_spec_sqr_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sqr_fc = { 
        0 : outpin0
    }
    return outputs_dict_sqr_fc[pin]

class _InputSpecSqrFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_sqr_fc(0), 0, op, -1) 

class _OutputSpecSqrFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_sqr_fc(0), 0, op) 

class _SqrFc(_Operator):
    def __init__(self):
         super().__init__("sqr_fc")
         self._name = "sqr_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSqrFc(self._op)
         self.outputs = _OutputSpecSqrFc(self._op)

def sqr_fc():
    """Operator's description:
Internal name is "sqr_fc"
Scripting name is "sqr_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("sqr_fc")
- using dpf.operators.math.sqr_fc()

Input list: 
   0: fields_container (field or fields container with only one field is expected)
Output list: 
   0: fields_container 
"""
    return _SqrFc()

#internal name: sqrt
#scripting name: sqrt
def _get_input_spec_sqrt(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqrt = { 
        0 : inpin0
    }
    return inputs_dict_sqrt[pin]

def _get_output_spec_sqrt(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sqrt = { 
        0 : outpin0
    }
    return outputs_dict_sqrt[pin]

class _InputSpecSqrt(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_sqrt(0), 0, op, -1) 

class _OutputSpecSqrt(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_sqrt(0), 0, op) 

class _Sqrt(_Operator):
    def __init__(self):
         super().__init__("sqrt")
         self._name = "sqrt"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSqrt(self._op)
         self.outputs = _OutputSpecSqrt(self._op)

def sqrt():
    """Operator's description:
Internal name is "sqrt"
Scripting name is "sqrt"

This operator can be instantiated in both following ways:
- using dpf.Operator("sqrt")
- using dpf.operators.math.sqrt()

Input list: 
   0: field (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _Sqrt()

#internal name: norm
#scripting name: norm
def _get_input_spec_norm(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_norm = { 
        0 : inpin0
    }
    return inputs_dict_norm[pin]

def _get_output_spec_norm(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_norm = { 
        0 : outpin0
    }
    return outputs_dict_norm[pin]

class _InputSpecNorm(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_norm(0), 0, op, -1) 

class _OutputSpecNorm(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_norm(0), 0, op) 

class _Norm(_Operator):
    def __init__(self):
         super().__init__("norm")
         self._name = "norm"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNorm(self._op)
         self.outputs = _OutputSpecNorm(self._op)

def norm():
    """Operator's description:
Internal name is "norm"
Scripting name is "norm"

This operator can be instantiated in both following ways:
- using dpf.Operator("norm")
- using dpf.operators.math.norm()

Input list: 
   0: field (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _Norm()

#internal name: sqrt_fc
#scripting name: sqrt_fc
def _get_input_spec_sqrt_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqrt_fc = { 
        0 : inpin0
    }
    return inputs_dict_sqrt_fc[pin]

def _get_output_spec_sqrt_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sqrt_fc = { 
        0 : outpin0
    }
    return outputs_dict_sqrt_fc[pin]

class _InputSpecSqrtFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_sqrt_fc(0), 0, op, -1) 

class _OutputSpecSqrtFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_sqrt_fc(0), 0, op) 

class _SqrtFc(_Operator):
    def __init__(self):
         super().__init__("sqrt_fc")
         self._name = "sqrt_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSqrtFc(self._op)
         self.outputs = _OutputSpecSqrtFc(self._op)

def sqrt_fc():
    """Operator's description:
Internal name is "sqrt_fc"
Scripting name is "sqrt_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("sqrt_fc")
- using dpf.operators.math.sqrt_fc()

Input list: 
   0: fields_container (field or fields container with only one field is expected)
Output list: 
   0: fields_container 
"""
    return _SqrtFc()

#internal name: norm_fc
#scripting name: norm_fc
def _get_input_spec_norm_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_norm_fc = { 
        0 : inpin0
    }
    return inputs_dict_norm_fc[pin]

def _get_output_spec_norm_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_norm_fc = { 
        0 : outpin0
    }
    return outputs_dict_norm_fc[pin]

class _InputSpecNormFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_norm_fc(0), 0, op, -1) 

class _OutputSpecNormFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_norm_fc(0), 0, op) 

class _NormFc(_Operator):
    def __init__(self):
         super().__init__("norm_fc")
         self._name = "norm_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNormFc(self._op)
         self.outputs = _OutputSpecNormFc(self._op)

def norm_fc():
    """Operator's description:
Internal name is "norm_fc"
Scripting name is "norm_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("norm_fc")
- using dpf.operators.math.norm_fc()

Input list: 
   0: fields_container 
Output list: 
   0: fields_container 
"""
    return _NormFc()

#internal name: component_wise_divide
#scripting name: component_wise_divide
def _get_input_spec_component_wise_divide(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_component_wise_divide = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_component_wise_divide[pin]

def _get_output_spec_component_wise_divide(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_component_wise_divide = { 
        0 : outpin0
    }
    return outputs_dict_component_wise_divide[pin]

class _InputSpecComponentWiseDivide(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_component_wise_divide(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_component_wise_divide(1), 1, op, -1) 

class _OutputSpecComponentWiseDivide(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_component_wise_divide(0), 0, op) 

class _ComponentWiseDivide(_Operator):
    def __init__(self):
         super().__init__("component_wise_divide")
         self._name = "component_wise_divide"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecComponentWiseDivide(self._op)
         self.outputs = _OutputSpecComponentWiseDivide(self._op)

def component_wise_divide():
    """Operator's description:
Internal name is "component_wise_divide"
Scripting name is "component_wise_divide"

This operator can be instantiated in both following ways:
- using dpf.Operator("component_wise_divide")
- using dpf.operators.math.component_wise_divide()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
   1: fieldB (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _ComponentWiseDivide()

#internal name: component_wise_divide_fc
#scripting name: component_wise_divide_fc
def _get_input_spec_component_wise_divide_fc(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_component_wise_divide_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_component_wise_divide_fc[pin]

def _get_output_spec_component_wise_divide_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_component_wise_divide_fc = { 
        0 : outpin0
    }
    return outputs_dict_component_wise_divide_fc[pin]

class _InputSpecComponentWiseDivideFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_component_wise_divide_fc(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_component_wise_divide_fc(1), 1, op, -1) 

class _OutputSpecComponentWiseDivideFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_component_wise_divide_fc(0), 0, op) 

class _ComponentWiseDivideFc(_Operator):
    def __init__(self):
         super().__init__("component_wise_divide_fc")
         self._name = "component_wise_divide_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecComponentWiseDivideFc(self._op)
         self.outputs = _OutputSpecComponentWiseDivideFc(self._op)

def component_wise_divide_fc():
    """Operator's description:
Internal name is "component_wise_divide_fc"
Scripting name is "component_wise_divide_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("component_wise_divide_fc")
- using dpf.operators.math.component_wise_divide_fc()

Input list: 
   0: fields_containerA 
   1: fields_containerB 
Output list: 
   0: fields_container 
"""
    return _ComponentWiseDivideFc()

#internal name: kronecker_prod
#scripting name: kronecker_prod
def _get_input_spec_kronecker_prod(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_kronecker_prod = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_kronecker_prod[pin]

def _get_output_spec_kronecker_prod(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_kronecker_prod = { 
        0 : outpin0
    }
    return outputs_dict_kronecker_prod[pin]

class _InputSpecKroneckerProd(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_kronecker_prod(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_kronecker_prod(1), 1, op, -1) 

class _OutputSpecKroneckerProd(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_kronecker_prod(0), 0, op) 

class _KroneckerProd(_Operator):
    def __init__(self):
         super().__init__("kronecker_prod")
         self._name = "kronecker_prod"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecKroneckerProd(self._op)
         self.outputs = _OutputSpecKroneckerProd(self._op)

def kronecker_prod():
    """Operator's description:
Internal name is "kronecker_prod"
Scripting name is "kronecker_prod"

This operator can be instantiated in both following ways:
- using dpf.Operator("kronecker_prod")
- using dpf.operators.math.kronecker_prod()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
   1: fieldB (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _KroneckerProd()

#internal name: realP_part
#scripting name: real_part
def _get_input_spec_real_part(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_real_part = { 
        0 : inpin0
    }
    return inputs_dict_real_part[pin]

def _get_output_spec_real_part(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_real_part = { 
        0 : outpin0
    }
    return outputs_dict_real_part[pin]

class _InputSpecRealPart(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_real_part(0), 0, op, -1) 

class _OutputSpecRealPart(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_real_part(0), 0, op) 

class _RealPart(_Operator):
    def __init__(self):
         super().__init__("realP_part")
         self._name = "realP_part"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecRealPart(self._op)
         self.outputs = _OutputSpecRealPart(self._op)

def real_part():
    """Operator's description:
Internal name is "realP_part"
Scripting name is "real_part"

This operator can be instantiated in both following ways:
- using dpf.Operator("realP_part")
- using dpf.operators.math.real_part()

Input list: 
   0: fields_container 
Output list: 
   0: fields_container 
"""
    return _RealPart()

#internal name: conjugate
#scripting name: conjugate
def _get_input_spec_conjugate(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_conjugate = { 
        0 : inpin0
    }
    return inputs_dict_conjugate[pin]

def _get_output_spec_conjugate(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_conjugate = { 
        0 : outpin0
    }
    return outputs_dict_conjugate[pin]

class _InputSpecConjugate(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_conjugate(0), 0, op, -1) 

class _OutputSpecConjugate(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_conjugate(0), 0, op) 

class _Conjugate(_Operator):
    def __init__(self):
         super().__init__("conjugate")
         self._name = "conjugate"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecConjugate(self._op)
         self.outputs = _OutputSpecConjugate(self._op)

def conjugate():
    """Operator's description:
Internal name is "conjugate"
Scripting name is "conjugate"

This operator can be instantiated in both following ways:
- using dpf.Operator("conjugate")
- using dpf.operators.math.conjugate()

Input list: 
   0: fields_container 
Output list: 
   0: fields_container 
"""
    return _Conjugate()

#internal name: img_part
#scripting name: img_part
def _get_input_spec_img_part(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_img_part = { 
        0 : inpin0
    }
    return inputs_dict_img_part[pin]

def _get_output_spec_img_part(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_img_part = { 
        0 : outpin0
    }
    return outputs_dict_img_part[pin]

class _InputSpecImgPart(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_img_part(0), 0, op, -1) 

class _OutputSpecImgPart(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_img_part(0), 0, op) 

class _ImgPart(_Operator):
    def __init__(self):
         super().__init__("img_part")
         self._name = "img_part"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecImgPart(self._op)
         self.outputs = _OutputSpecImgPart(self._op)

def img_part():
    """Operator's description:
Internal name is "img_part"
Scripting name is "img_part"

This operator can be instantiated in both following ways:
- using dpf.Operator("img_part")
- using dpf.operators.math.img_part()

Input list: 
   0: fields_container 
Output list: 
   0: fields_container 
"""
    return _ImgPart()

#internal name: amplitude
#scripting name: amplitude
def _get_input_spec_amplitude(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_amplitude = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_amplitude[pin]

def _get_output_spec_amplitude(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_amplitude = { 
        0 : outpin0
    }
    return outputs_dict_amplitude[pin]

class _InputSpecAmplitude(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_amplitude(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_amplitude(1), 1, op, -1) 

class _OutputSpecAmplitude(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_amplitude(0), 0, op) 

class _Amplitude(_Operator):
    def __init__(self):
         super().__init__("amplitude")
         self._name = "amplitude"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAmplitude(self._op)
         self.outputs = _OutputSpecAmplitude(self._op)

def amplitude():
    """Operator's description:
Internal name is "amplitude"
Scripting name is "amplitude"

This operator can be instantiated in both following ways:
- using dpf.Operator("amplitude")
- using dpf.operators.math.amplitude()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
   1: fieldB (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _Amplitude()

#internal name: cplx_add
#scripting name: cplx_add
def _get_input_spec_cplx_add(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_add = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_cplx_add[pin]

def _get_output_spec_cplx_add(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_add = { 
        0 : outpin0
    }
    return outputs_dict_cplx_add[pin]

class _InputSpecCplxAdd(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_cplx_add(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_cplx_add(1), 1, op, -1) 

class _OutputSpecCplxAdd(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cplx_add(0), 0, op) 

class _CplxAdd(_Operator):
    def __init__(self):
         super().__init__("cplx_add")
         self._name = "cplx_add"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCplxAdd(self._op)
         self.outputs = _OutputSpecCplxAdd(self._op)

def cplx_add():
    """Operator's description:
Internal name is "cplx_add"
Scripting name is "cplx_add"

This operator can be instantiated in both following ways:
- using dpf.Operator("cplx_add")
- using dpf.operators.math.cplx_add()

Input list: 
   0: fields_containerA 
   1: fields_containerB 
Output list: 
   0: fields_container 
"""
    return _CplxAdd()

#internal name: cplx_dot
#scripting name: cplx_dot
def _get_input_spec_cplx_dot(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_dot = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_cplx_dot[pin]

def _get_output_spec_cplx_dot(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_dot = { 
        0 : outpin0
    }
    return outputs_dict_cplx_dot[pin]

class _InputSpecCplxDot(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_cplx_dot(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_cplx_dot(1), 1, op, -1) 

class _OutputSpecCplxDot(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cplx_dot(0), 0, op) 

class _CplxDot(_Operator):
    def __init__(self):
         super().__init__("cplx_dot")
         self._name = "cplx_dot"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCplxDot(self._op)
         self.outputs = _OutputSpecCplxDot(self._op)

def cplx_dot():
    """Operator's description:
Internal name is "cplx_dot"
Scripting name is "cplx_dot"

This operator can be instantiated in both following ways:
- using dpf.Operator("cplx_dot")
- using dpf.operators.math.cplx_dot()

Input list: 
   0: fields_containerA 
   1: fields_containerB 
Output list: 
   0: fields_container 
"""
    return _CplxDot()

#internal name: cplx_divide
#scripting name: cplx_divide
def _get_input_spec_cplx_divide(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_divide = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_cplx_divide[pin]

def _get_output_spec_cplx_divide(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_divide = { 
        0 : outpin0
    }
    return outputs_dict_cplx_divide[pin]

class _InputSpecCplxDivide(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_cplx_divide(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_cplx_divide(1), 1, op, -1) 

class _OutputSpecCplxDivide(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cplx_divide(0), 0, op) 

class _CplxDivide(_Operator):
    def __init__(self):
         super().__init__("cplx_divide")
         self._name = "cplx_divide"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCplxDivide(self._op)
         self.outputs = _OutputSpecCplxDivide(self._op)

def cplx_divide():
    """Operator's description:
Internal name is "cplx_divide"
Scripting name is "cplx_divide"

This operator can be instantiated in both following ways:
- using dpf.Operator("cplx_divide")
- using dpf.operators.math.cplx_divide()

Input list: 
   0: fields_containerA 
   1: fields_containerB 
Output list: 
   0: fields_container 
"""
    return _CplxDivide()

#internal name: dot
#scripting name: dot
def _get_input_spec_dot(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_dot = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_dot[pin]

def _get_output_spec_dot(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_dot = { 
        0 : outpin0
    }
    return outputs_dict_dot[pin]

class _InputSpecDot(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_dot(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_dot(1), 1, op, -1) 

class _OutputSpecDot(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_dot(0), 0, op) 

class _Dot(_Operator):
    def __init__(self):
         super().__init__("dot")
         self._name = "dot"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecDot(self._op)
         self.outputs = _OutputSpecDot(self._op)

def dot():
    """Operator's description:
Internal name is "dot"
Scripting name is "dot"

This operator can be instantiated in both following ways:
- using dpf.Operator("dot")
- using dpf.operators.math.dot()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
   1: fieldB (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _Dot()

#internal name: cplx_derive
#scripting name: cplx_derive
def _get_input_spec_cplx_derive(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_derive = { 
        0 : inpin0
    }
    return inputs_dict_cplx_derive[pin]

def _get_output_spec_cplx_derive(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_derive = { 
        0 : outpin0
    }
    return outputs_dict_cplx_derive[pin]

class _InputSpecCplxDerive(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_cplx_derive(0), 0, op, -1) 

class _OutputSpecCplxDerive(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cplx_derive(0), 0, op) 

class _CplxDerive(_Operator):
    def __init__(self):
         super().__init__("cplx_derive")
         self._name = "cplx_derive"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCplxDerive(self._op)
         self.outputs = _OutputSpecCplxDerive(self._op)

def cplx_derive():
    """Operator's description:
Internal name is "cplx_derive"
Scripting name is "cplx_derive"

This operator can be instantiated in both following ways:
- using dpf.Operator("cplx_derive")
- using dpf.operators.math.cplx_derive()

Input list: 
   0: fields_container 
Output list: 
   0: fields_container 
"""
    return _CplxDerive()

#internal name: polar_to_cplx
#scripting name: polar_to_cplx
def _get_input_spec_polar_to_cplx(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_polar_to_cplx = { 
        0 : inpin0
    }
    return inputs_dict_polar_to_cplx[pin]

def _get_output_spec_polar_to_cplx(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_polar_to_cplx = { 
        0 : outpin0
    }
    return outputs_dict_polar_to_cplx[pin]

class _InputSpecPolarToCplx(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_polar_to_cplx(0), 0, op, -1) 

class _OutputSpecPolarToCplx(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_polar_to_cplx(0), 0, op) 

class _PolarToCplx(_Operator):
    def __init__(self):
         super().__init__("polar_to_cplx")
         self._name = "polar_to_cplx"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPolarToCplx(self._op)
         self.outputs = _OutputSpecPolarToCplx(self._op)

def polar_to_cplx():
    """Operator's description:
Internal name is "polar_to_cplx"
Scripting name is "polar_to_cplx"

This operator can be instantiated in both following ways:
- using dpf.Operator("polar_to_cplx")
- using dpf.operators.math.polar_to_cplx()

Input list: 
   0: fields_container 
Output list: 
   0: fields_container 
"""
    return _PolarToCplx()

#internal name: modulus
#scripting name: modulus
def _get_input_spec_modulus(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_modulus = { 
        0 : inpin0
    }
    return inputs_dict_modulus[pin]

def _get_output_spec_modulus(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_modulus = { 
        0 : outpin0
    }
    return outputs_dict_modulus[pin]

class _InputSpecModulus(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_modulus(0), 0, op, -1) 

class _OutputSpecModulus(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_modulus(0), 0, op) 

class _Modulus(_Operator):
    def __init__(self):
         super().__init__("modulus")
         self._name = "modulus"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecModulus(self._op)
         self.outputs = _OutputSpecModulus(self._op)

def modulus():
    """Operator's description:
Internal name is "modulus"
Scripting name is "modulus"

This operator can be instantiated in both following ways:
- using dpf.Operator("modulus")
- using dpf.operators.math.modulus()

Input list: 
   0: fields_container 
Output list: 
   0: fields_container 
"""
    return _Modulus()

#internal name: min_max_over_time
#scripting name: min_max_over_time
def _get_input_spec_min_max_over_time(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "angle", type_names = ["double"], optional = True, document = """Phase angle used for complex field container""")
    inpin2 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = True, document = """Phase angle unit. Default is radian.""")
    inpin3 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin4 = _PinSpecification(name = "compute_amplitude", type_names = ["bool"], optional = True, document = """Do calculate amplitude.""")
    inpin5 = _PinSpecification(name = "int32", type_names = ["int32"], optional = False, document = """Define min or max.""")
    inputs_dict_min_max_over_time = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5
    }
    return inputs_dict_min_max_over_time[pin]

def _get_output_spec_min_max_over_time(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_min_max_over_time = { 
        0 : outpin0
    }
    return outputs_dict_min_max_over_time[pin]

class _InputSpecMinMaxOverTime(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_min_max_over_time(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_min_max_over_time(1), 1, op, -1) 
        self.unit_name = _Input(_get_input_spec_min_max_over_time(2), 2, op, -1) 
        self.abs_value = _Input(_get_input_spec_min_max_over_time(3), 3, op, -1) 
        self.compute_amplitude = _Input(_get_input_spec_min_max_over_time(4), 4, op, -1) 
        self.int32 = _Input(_get_input_spec_min_max_over_time(5), 5, op, -1) 

class _OutputSpecMinMaxOverTime(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_min_max_over_time(0), 0, op) 

class _MinMaxOverTime(_Operator):
    def __init__(self):
         super().__init__("min_max_over_time")
         self._name = "min_max_over_time"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecMinMaxOverTime(self._op)
         self.outputs = _OutputSpecMinMaxOverTime(self._op)

def min_max_over_time():
    """Operator's description:
Internal name is "min_max_over_time"
Scripting name is "min_max_over_time"

This operator can be instantiated in both following ways:
- using dpf.Operator("min_max_over_time")
- using dpf.operators.math.min_max_over_time()

Input list: 
   0: fields_container 
   1: angle (Phase angle used for complex field container)
   2: unit_name (Phase angle unit. Default is radian.)
   3: abs_value (Should use absolute value.)
   4: compute_amplitude (Do calculate amplitude.)
   5: int32 (Define min or max.)
Output list: 
   0: field 
"""
    return _MinMaxOverTime()

#internal name: accumulate
#scripting name: accumulate
def _get_input_spec_accumulate(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_accumulate = { 
        0 : inpin0
    }
    return inputs_dict_accumulate[pin]

def _get_output_spec_accumulate(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_accumulate = { 
        0 : outpin0
    }
    return outputs_dict_accumulate[pin]

class _InputSpecAccumulate(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_accumulate(0), 0, op, -1) 

class _OutputSpecAccumulate(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_accumulate(0), 0, op) 

class _Accumulate(_Operator):
    def __init__(self):
         super().__init__("accumulate")
         self._name = "accumulate"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAccumulate(self._op)
         self.outputs = _OutputSpecAccumulate(self._op)

def accumulate():
    """Operator's description:
Internal name is "accumulate"
Scripting name is "accumulate"

This operator can be instantiated in both following ways:
- using dpf.Operator("accumulate")
- using dpf.operators.math.accumulate()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _Accumulate()

#internal name: generalized_inner_product
#scripting name: generalized_inner_product
def _get_input_spec_generalized_inner_product(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_generalized_inner_product = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_generalized_inner_product[pin]

def _get_output_spec_generalized_inner_product(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_generalized_inner_product = { 
        0 : outpin0
    }
    return outputs_dict_generalized_inner_product[pin]

class _InputSpecGeneralizedInnerProduct(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_generalized_inner_product(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_generalized_inner_product(1), 1, op, -1) 

class _OutputSpecGeneralizedInnerProduct(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_generalized_inner_product(0), 0, op) 

class _GeneralizedInnerProduct(_Operator):
    def __init__(self):
         super().__init__("generalized_inner_product")
         self._name = "generalized_inner_product"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecGeneralizedInnerProduct(self._op)
         self.outputs = _OutputSpecGeneralizedInnerProduct(self._op)

def generalized_inner_product():
    """Operator's description:
Internal name is "generalized_inner_product"
Scripting name is "generalized_inner_product"

This operator can be instantiated in both following ways:
- using dpf.Operator("generalized_inner_product")
- using dpf.operators.math.generalized_inner_product()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
   1: fieldB (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _GeneralizedInnerProduct()

from . import native #native::overall_dot

#internal name: max_over_time
#scripting name: max_over_time
def _get_input_spec_max_over_time(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "angle", type_names = ["double"], optional = True, document = """Phase angle used for complex field container""")
    inpin2 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = True, document = """Phase angle unit. Default is radian.""")
    inpin3 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin4 = _PinSpecification(name = "compute_amplitude", type_names = ["bool"], optional = True, document = """Do calculate amplitude.""")
    inputs_dict_max_over_time = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_max_over_time[pin]

def _get_output_spec_max_over_time(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_max_over_time = { 
        0 : outpin0
    }
    return outputs_dict_max_over_time[pin]

class _InputSpecMaxOverTime(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_max_over_time(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_max_over_time(1), 1, op, -1) 
        self.unit_name = _Input(_get_input_spec_max_over_time(2), 2, op, -1) 
        self.abs_value = _Input(_get_input_spec_max_over_time(3), 3, op, -1) 
        self.compute_amplitude = _Input(_get_input_spec_max_over_time(4), 4, op, -1) 

class _OutputSpecMaxOverTime(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_max_over_time(0), 0, op) 

class _MaxOverTime(_Operator):
    def __init__(self):
         super().__init__("max_over_time")
         self._name = "max_over_time"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecMaxOverTime(self._op)
         self.outputs = _OutputSpecMaxOverTime(self._op)

def max_over_time():
    """Operator's description:
Internal name is "max_over_time"
Scripting name is "max_over_time"

This operator can be instantiated in both following ways:
- using dpf.Operator("max_over_time")
- using dpf.operators.math.max_over_time()

Input list: 
   0: fields_container 
   1: angle (Phase angle used for complex field container)
   2: unit_name (Phase angle unit. Default is radian.)
   3: abs_value (Should use absolute value.)
   4: compute_amplitude (Do calculate amplitude.)
Output list: 
   0: field 
"""
    return _MaxOverTime()

#internal name: time_of_max
#scripting name: time_of_max
def _get_input_spec_time_of_max(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "angle", type_names = ["double"], optional = True, document = """Phase angle used for complex field container""")
    inpin2 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = True, document = """Phase angle unit. Default is radian.""")
    inpin3 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin4 = _PinSpecification(name = "compute_amplitude", type_names = ["bool"], optional = True, document = """Do calculate amplitude.""")
    inputs_dict_time_of_max = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_time_of_max[pin]

def _get_output_spec_time_of_max(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_time_of_max = { 
        0 : outpin0
    }
    return outputs_dict_time_of_max[pin]

class _InputSpecTimeOfMax(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_time_of_max(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_time_of_max(1), 1, op, -1) 
        self.unit_name = _Input(_get_input_spec_time_of_max(2), 2, op, -1) 
        self.abs_value = _Input(_get_input_spec_time_of_max(3), 3, op, -1) 
        self.compute_amplitude = _Input(_get_input_spec_time_of_max(4), 4, op, -1) 

class _OutputSpecTimeOfMax(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_time_of_max(0), 0, op) 

class _TimeOfMax(_Operator):
    def __init__(self):
         super().__init__("time_of_max")
         self._name = "time_of_max"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecTimeOfMax(self._op)
         self.outputs = _OutputSpecTimeOfMax(self._op)

def time_of_max():
    """Operator's description:
Internal name is "time_of_max"
Scripting name is "time_of_max"

This operator can be instantiated in both following ways:
- using dpf.Operator("time_of_max")
- using dpf.operators.math.time_of_max()

Input list: 
   0: fields_container 
   1: angle (Phase angle used for complex field container)
   2: unit_name (Phase angle unit. Default is radian.)
   3: abs_value (Should use absolute value.)
   4: compute_amplitude (Do calculate amplitude.)
Output list: 
   0: field 
"""
    return _TimeOfMax()

#internal name: min_over_time
#scripting name: min_over_time
def _get_input_spec_min_over_time(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "angle", type_names = ["double"], optional = True, document = """Phase angle used for complex field container""")
    inpin2 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = True, document = """Phase angle unit. Default is radian.""")
    inpin3 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin4 = _PinSpecification(name = "compute_amplitude", type_names = ["bool"], optional = True, document = """Do calculate amplitude.""")
    inputs_dict_min_over_time = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_min_over_time[pin]

def _get_output_spec_min_over_time(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_min_over_time = { 
        0 : outpin0
    }
    return outputs_dict_min_over_time[pin]

class _InputSpecMinOverTime(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_min_over_time(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_min_over_time(1), 1, op, -1) 
        self.unit_name = _Input(_get_input_spec_min_over_time(2), 2, op, -1) 
        self.abs_value = _Input(_get_input_spec_min_over_time(3), 3, op, -1) 
        self.compute_amplitude = _Input(_get_input_spec_min_over_time(4), 4, op, -1) 

class _OutputSpecMinOverTime(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_min_over_time(0), 0, op) 

class _MinOverTime(_Operator):
    def __init__(self):
         super().__init__("min_over_time")
         self._name = "min_over_time"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecMinOverTime(self._op)
         self.outputs = _OutputSpecMinOverTime(self._op)

def min_over_time():
    """Operator's description:
Internal name is "min_over_time"
Scripting name is "min_over_time"

This operator can be instantiated in both following ways:
- using dpf.Operator("min_over_time")
- using dpf.operators.math.min_over_time()

Input list: 
   0: fields_container 
   1: angle (Phase angle used for complex field container)
   2: unit_name (Phase angle unit. Default is radian.)
   3: abs_value (Should use absolute value.)
   4: compute_amplitude (Do calculate amplitude.)
Output list: 
   0: field 
"""
    return _MinOverTime()

#internal name: time_of_min
#scripting name: time_of_min
def _get_input_spec_time_of_min(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "angle", type_names = ["double"], optional = True, document = """Phase angle used for complex field container""")
    inpin2 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = True, document = """Phase angle unit. Default is radian.""")
    inpin3 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin4 = _PinSpecification(name = "compute_amplitude", type_names = ["bool"], optional = True, document = """Do calculate amplitude.""")
    inputs_dict_time_of_min = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_time_of_min[pin]

def _get_output_spec_time_of_min(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_time_of_min = { 
        0 : outpin0
    }
    return outputs_dict_time_of_min[pin]

class _InputSpecTimeOfMin(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_time_of_min(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_time_of_min(1), 1, op, -1) 
        self.unit_name = _Input(_get_input_spec_time_of_min(2), 2, op, -1) 
        self.abs_value = _Input(_get_input_spec_time_of_min(3), 3, op, -1) 
        self.compute_amplitude = _Input(_get_input_spec_time_of_min(4), 4, op, -1) 

class _OutputSpecTimeOfMin(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_time_of_min(0), 0, op) 

class _TimeOfMin(_Operator):
    def __init__(self):
         super().__init__("time_of_min")
         self._name = "time_of_min"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecTimeOfMin(self._op)
         self.outputs = _OutputSpecTimeOfMin(self._op)

def time_of_min():
    """Operator's description:
Internal name is "time_of_min"
Scripting name is "time_of_min"

This operator can be instantiated in both following ways:
- using dpf.Operator("time_of_min")
- using dpf.operators.math.time_of_min()

Input list: 
   0: fields_container 
   1: angle (Phase angle used for complex field container)
   2: unit_name (Phase angle unit. Default is radian.)
   3: abs_value (Should use absolute value.)
   4: compute_amplitude (Do calculate amplitude.)
Output list: 
   0: field 
"""
    return _TimeOfMin()

#internal name: max_over_phase
#scripting name: max_over_phase
def _get_input_spec_max_over_phase(pin):
    inpin0 = _PinSpecification(name = "real_field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "imaginary_field", type_names = ["field"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin3 = _PinSpecification(name = "phase_increment", type_names = ["double"], optional = True, document = """Phase increment (default is 10.0 degrees).""")
    inputs_dict_max_over_phase = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    return inputs_dict_max_over_phase[pin]

def _get_output_spec_max_over_phase(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_max_over_phase = { 
        0 : outpin0
    }
    return outputs_dict_max_over_phase[pin]

class _InputSpecMaxOverPhase(_Inputs):
    def __init__(self, op: _Operator):
        self.real_field = _Input(_get_input_spec_max_over_phase(0), 0, op, -1) 
        self.imaginary_field = _Input(_get_input_spec_max_over_phase(1), 1, op, -1) 
        self.abs_value = _Input(_get_input_spec_max_over_phase(2), 2, op, -1) 
        self.phase_increment = _Input(_get_input_spec_max_over_phase(3), 3, op, -1) 

class _OutputSpecMaxOverPhase(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_max_over_phase(0), 0, op) 

class _MaxOverPhase(_Operator):
    def __init__(self):
         super().__init__("max_over_phase")
         self._name = "max_over_phase"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecMaxOverPhase(self._op)
         self.outputs = _OutputSpecMaxOverPhase(self._op)

def max_over_phase():
    """Operator's description:
Internal name is "max_over_phase"
Scripting name is "max_over_phase"

This operator can be instantiated in both following ways:
- using dpf.Operator("max_over_phase")
- using dpf.operators.math.max_over_phase()

Input list: 
   0: real_field 
   1: imaginary_field 
   2: abs_value (Should use absolute value.)
   3: phase_increment (Phase increment (default is 10.0 degrees).)
Output list: 
   0: field 
"""
    return _MaxOverPhase()

#internal name: dot_tensor
#scripting name: dot_tensor
def _get_input_spec_dot_tensor(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_dot_tensor = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_dot_tensor[pin]

def _get_output_spec_dot_tensor(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_dot_tensor = { 
        0 : outpin0
    }
    return outputs_dict_dot_tensor[pin]

class _InputSpecDotTensor(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_dot_tensor(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_dot_tensor(1), 1, op, -1) 

class _OutputSpecDotTensor(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_dot_tensor(0), 0, op) 

class _DotTensor(_Operator):
    def __init__(self):
         super().__init__("dot_tensor")
         self._name = "dot_tensor"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecDotTensor(self._op)
         self.outputs = _OutputSpecDotTensor(self._op)

def dot_tensor():
    """Operator's description:
Internal name is "dot_tensor"
Scripting name is "dot_tensor"

This operator can be instantiated in both following ways:
- using dpf.Operator("dot_tensor")
- using dpf.operators.math.dot_tensor()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
   1: fieldB (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _DotTensor()

#internal name: scale_by_field
#scripting name: scale_by_field
def _get_input_spec_scale_by_field(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_scale_by_field = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_scale_by_field[pin]

def _get_output_spec_scale_by_field(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_scale_by_field = { 
        0 : outpin0
    }
    return outputs_dict_scale_by_field[pin]

class _InputSpecScaleByField(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_scale_by_field(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_scale_by_field(1), 1, op, -1) 

class _OutputSpecScaleByField(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_scale_by_field(0), 0, op) 

class _ScaleByField(_Operator):
    def __init__(self):
         super().__init__("scale_by_field")
         self._name = "scale_by_field"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecScaleByField(self._op)
         self.outputs = _OutputSpecScaleByField(self._op)

def scale_by_field():
    """Operator's description:
Internal name is "scale_by_field"
Scripting name is "scale_by_field"

This operator can be instantiated in both following ways:
- using dpf.Operator("scale_by_field")
- using dpf.operators.math.scale_by_field()

Input list: 
   0: fieldA (field or fields container with only one field is expected)
   1: fieldB (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _ScaleByField()

#internal name: invert
#scripting name: invert
def _get_input_spec_invert(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_invert = { 
        0 : inpin0
    }
    return inputs_dict_invert[pin]

def _get_output_spec_invert(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_invert = { 
        0 : outpin0
    }
    return outputs_dict_invert[pin]

class _InputSpecInvert(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_invert(0), 0, op, -1) 

class _OutputSpecInvert(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_invert(0), 0, op) 

class _Invert(_Operator):
    def __init__(self):
         super().__init__("invert")
         self._name = "invert"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecInvert(self._op)
         self.outputs = _OutputSpecInvert(self._op)

def invert():
    """Operator's description:
Internal name is "invert"
Scripting name is "invert"

This operator can be instantiated in both following ways:
- using dpf.Operator("invert")
- using dpf.operators.math.invert()

Input list: 
   0: field (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _Invert()

