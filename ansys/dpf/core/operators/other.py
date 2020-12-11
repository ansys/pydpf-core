from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "other" category
"""

#internal name: topology::topology_from_mesh
#scripting name: wrap_in_topology
def _get_input_spec_wrap_in_topology(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region","abstract_topology_entity"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "id", type_names = ["int32"], optional = True, document = """Id that must be attributed to the generated geometry (default is 0).""")
    inputs_dict_wrap_in_topology = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_wrap_in_topology[pin]

def _get_output_spec_wrap_in_topology(pin):
    outpin0 = _PinSpecification(name = "mesh", type_names = ["abstract_topology_entity"], document = """""")
    outputs_dict_wrap_in_topology = { 
        0 : outpin0
    }
    return outputs_dict_wrap_in_topology[pin]

class _InputSpecWrapInTopology(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_wrap_in_topology(0), 0, op, -1) 
        self.id = _Input(_get_input_spec_wrap_in_topology(1), 1, op, -1) 

class _OutputSpecWrapInTopology(_Outputs):
    def __init__(self, op: _Operator):
        self.mesh = _Output(_get_output_spec_wrap_in_topology(0), 0, op) 

class _WrapInTopology(_Operator):
    """Operator's description:
    Internal name is "topology::topology_from_mesh"
    Scripting name is "wrap_in_topology"

    Description: Take various input, and wrap in geometry if necessary.

    Input list: 
       0: mesh 
       1: id (Id that must be attributed to the generated geometry (default is 0).)

    Output list: 
       0: mesh 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("topology::topology_from_mesh")
    >>> op_way2 = core.operators.other.wrap_in_topology()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("topology::topology_from_mesh")
        self._name = "topology::topology_from_mesh"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecWrapInTopology(self._op)
        self.outputs = _OutputSpecWrapInTopology(self._op)

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

def wrap_in_topology():
    """Operator's description:
    Internal name is "topology::topology_from_mesh"
    Scripting name is "wrap_in_topology"

    Description: Take various input, and wrap in geometry if necessary.

    Input list: 
       0: mesh 
       1: id (Id that must be attributed to the generated geometry (default is 0).)

    Output list: 
       0: mesh 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("topology::topology_from_mesh")
    >>> op_way2 = core.operators.other.wrap_in_topology()
    """
    return _WrapInTopology()

