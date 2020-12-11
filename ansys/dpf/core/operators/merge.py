from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

#internal name: merge::solid_shell_fields
#scripting name: merge::solid_shell_fields
def _get_input_spec_solid_shell_fields(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_solid_shell_fields = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_solid_shell_fields
    else:
        return inputs_dict_solid_shell_fields[pin]

def _get_output_spec_solid_shell_fields(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_solid_shell_fields = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_solid_shell_fields
    else:
        return outputs_dict_solid_shell_fields[pin]

class _InputSpecSolidShellFields(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_solid_shell_fields(), op)
        self.fields_container = Input(_get_input_spec_solid_shell_fields(0), 0, op, -1) 

class _OutputSpecSolidShellFields(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_solid_shell_fields(), op)
        self.fields_container = Output(_get_output_spec_solid_shell_fields(0), 0, op) 

class _SolidShellFields(_Operator):
    """Operator's description:
    Internal name is "merge::solid_shell_fields"
    Scripting name is "merge::solid_shell_fields"

    Description: Makes a fields based on fields container containing shell and solid fields with respect to time steps/frequencies.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("merge::solid_shell_fields")
    >>> op_way2 = core.operators.logic.merge::solid_shell_fields()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("merge::solid_shell_fields")
        self.inputs = _InputSpecSolidShellFields(self)
        self.outputs = _OutputSpecSolidShellFields(self)

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

def solid_shell_fields():
    """Operator's description:
    Internal name is "merge::solid_shell_fields"
    Scripting name is "merge::solid_shell_fields"

    Description: Makes a fields based on fields container containing shell and solid fields with respect to time steps/frequencies.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("merge::solid_shell_fields")
    >>> op_way2 = core.operators.logic.merge::solid_shell_fields()
    """
    return _SolidShellFields()

