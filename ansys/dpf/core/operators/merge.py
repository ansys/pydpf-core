from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

#internal name: merge::solid_shell_fields
#scripting name: merge::solid_shell_fields
def _get_input_spec_solid_shell_fields(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_solid_shell_fields = { 
        0 : inpin0
    }
    return inputs_dict_solid_shell_fields[pin]

def _get_output_spec_solid_shell_fields(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_solid_shell_fields = { 
        0 : outpin0
    }
    return outputs_dict_solid_shell_fields[pin]

class _InputSpecSolidShellFields(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_solid_shell_fields(0), 0, op, -1) 

class _OutputSpecSolidShellFields(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_solid_shell_fields(0), 0, op) 

class _SolidShellFields(_Operator):
    def __init__(self):
         super().__init__("merge::solid_shell_fields")
         self._name = "merge::solid_shell_fields"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSolidShellFields(self._op)
         self.outputs = _OutputSpecSolidShellFields(self._op)

def solid_shell_fields():
    """Operator's description:
Internal name is "merge::solid_shell_fields"
Scripting name is "merge::solid_shell_fields"

This operator can be instantiated in both following ways:
- using dpf.Operator("merge::solid_shell_fields")
- using dpf.operators.logic.merge::solid_shell_fields()

Input list: 
   0: fields_container 
Output list: 
   0: fields_container 
"""
    return _SolidShellFields()

