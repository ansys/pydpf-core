from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

#internal name: native::overall_dot
#scripting name: native::overall_dot
def _get_input_spec_overall_dot(pin = None):
    inpin0 = _PinSpecification(name = "FieldA", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "FieldB", type_names = ["field"], optional = False, document = """""")
    inputs_dict_overall_dot = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_overall_dot
    else:
        return inputs_dict_overall_dot[pin]

def _get_output_spec_overall_dot(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """Field defined on over-all location, contains a unique scalar value""")
    outputs_dict_overall_dot = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_overall_dot
    else:
        return outputs_dict_overall_dot[pin]

class _InputSpecOverallDot(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_overall_dot(), op)
        self.FieldA = Input(_get_input_spec_overall_dot(0), 0, op, -1) 
        self.FieldB = Input(_get_input_spec_overall_dot(1), 1, op, -1) 

class _OutputSpecOverallDot(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_overall_dot(), op)
        self.field = Output(_get_output_spec_overall_dot(0), 0, op) 

class _OverallDot(_Operator):
    """Operator's description:
    Internal name is "native::overall_dot"
    Scripting name is "native::overall_dot"

    Description: Compute a sdot product between two fields and return a scalar.

    Input list: 
       0: FieldA 
       1: FieldB 

    Output list: 
       0: field (Field defined on over-all location, contains a unique scalar value)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("native::overall_dot")
    >>> op_way2 = core.operators.math.native::overall_dot()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("native::overall_dot")
        self.inputs = _InputSpecOverallDot(self)
        self.outputs = _OutputSpecOverallDot(self)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def overall_dot():
    """Operator's description:
    Internal name is "native::overall_dot"
    Scripting name is "native::overall_dot"

    Description: Compute a sdot product between two fields and return a scalar.

    Input list: 
       0: FieldA 
       1: FieldB 

    Output list: 
       0: field (Field defined on over-all location, contains a unique scalar value)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("native::overall_dot")
    >>> op_way2 = core.operators.math.native::overall_dot()
    """
    return _OverallDot()

