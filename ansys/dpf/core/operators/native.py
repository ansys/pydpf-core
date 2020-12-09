from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

#internal name: native::overall_dot
#scripting name: native::overall_dot
def _get_input_spec_overall_dot(pin):
    inpin0 = _PinSpecification(name = "FieldA", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "FieldB", type_names = ["field"], optional = False, document = """""")
    inputs_dict_overall_dot = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_overall_dot[pin]

def _get_output_spec_overall_dot(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """Field defined on over-all location, contains a unique scalar value""")
    outputs_dict_overall_dot = { 
        0 : outpin0
    }
    return outputs_dict_overall_dot[pin]

class _InputSpecOverallDot(_Inputs):
    def __init__(self, op: _Operator):
        self.FieldA = _Input(_get_input_spec_overall_dot(0), 0, op, -1) 
        self.FieldB = _Input(_get_input_spec_overall_dot(1), 1, op, -1) 

class _OutputSpecOverallDot(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_overall_dot(0), 0, op) 

class _OverallDot(_Operator):
    def __init__(self):
         super().__init__("native::overall_dot")
         self._name = "native::overall_dot"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecOverallDot(self._op)
         self.outputs = _OutputSpecOverallDot(self._op)

def overall_dot():
    """Operator's description:
Internal name is "native::overall_dot"
Scripting name is "native::overall_dot"

This operator can be instantiated in both following ways:
- using dpf.Operator("native::overall_dot")
- using dpf.operators.math.native::overall_dot()

Input list: 
   0: FieldA 
   1: FieldB 
Output list: 
   0: field (Field defined on over-all location, contains a unique scalar value)
"""
    return _OverallDot()

