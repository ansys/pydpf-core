from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "averaging" category
"""

#internal name: nodal_fraction_fc
#scripting name: nodal_fraction_fc
def _get_input_spec_nodal_fraction_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container""")
    inpin6 = _PinSpecification(name = "denominator", type_names = ["fields_container"], optional = True, document = """if a fields container is set in this pin, it is used as the denominator of the fraction instead of elemental_nodal_To_nodal_fc""")
    inputs_dict_nodal_fraction_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        6 : inpin6
    }
    return inputs_dict_nodal_fraction_fc[pin]

def _get_output_spec_nodal_fraction_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_fraction_fc = { 
        0 : outpin0
    }
    return outputs_dict_nodal_fraction_fc[pin]

class _InputSpecNodalFractionFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_nodal_fraction_fc(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_fraction_fc(1), 1, op, -1) 
        self.scoping = _Input(_get_input_spec_nodal_fraction_fc(3), 3, op, -1) 
        self.denominator = _Input(_get_input_spec_nodal_fraction_fc(6), 6, op, -1) 

class _OutputSpecNodalFractionFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_fraction_fc(0), 0, op) 

class _NodalFractionFc(_Operator):
    def __init__(self):
         super().__init__("nodal_fraction_fc")
         self._name = "nodal_fraction_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalFractionFc(self._op)
         self.outputs = _OutputSpecNodalFractionFc(self._op)

def nodal_fraction_fc():
    """Operator's description:
Internal name is "nodal_fraction_fc"
Scripting name is "nodal_fraction_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("nodal_fraction_fc")
- using dpf.operators.averaging.nodal_fraction_fc()

Input list: 
   0: fields_container 
   1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
   3: scoping (average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container)
   6: denominator (if a fields container is set in this pin, it is used as the denominator of the fraction instead of elemental_nodal_To_nodal_fc)
Output list: 
   0: fields_container 
"""
    return _NodalFractionFc()

#internal name: ElementalNodal_To_NodalElemental_fc
#scripting name: elemental_nodal_to_nodal_elemental_fc
def _get_input_spec_elemental_nodal_to_nodal_elemental_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inputs_dict_elemental_nodal_to_nodal_elemental_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_elemental_nodal_to_nodal_elemental_fc[pin]

def _get_output_spec_elemental_nodal_to_nodal_elemental_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_nodal_to_nodal_elemental_fc = { 
        0 : outpin0
    }
    return outputs_dict_elemental_nodal_to_nodal_elemental_fc[pin]

class _InputSpecElementalNodalToNodalElementalFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_elemental_nodal_to_nodal_elemental_fc(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elemental_nodal_to_nodal_elemental_fc(1), 1, op, -1) 

class _OutputSpecElementalNodalToNodalElementalFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elemental_nodal_to_nodal_elemental_fc(0), 0, op) 

class _ElementalNodalToNodalElementalFc(_Operator):
    def __init__(self):
         super().__init__("ElementalNodal_To_NodalElemental_fc")
         self._name = "ElementalNodal_To_NodalElemental_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalNodalToNodalElementalFc(self._op)
         self.outputs = _OutputSpecElementalNodalToNodalElementalFc(self._op)

def elemental_nodal_to_nodal_elemental_fc():
    """Operator's description:
Internal name is "ElementalNodal_To_NodalElemental_fc"
Scripting name is "elemental_nodal_to_nodal_elemental_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("ElementalNodal_To_NodalElemental_fc")
- using dpf.operators.averaging.elemental_nodal_to_nodal_elemental_fc()

Input list: 
   0: fields_container 
   1: mesh_scoping 
Output list: 
   0: fields_container 
"""
    return _ElementalNodalToNodalElementalFc()

#internal name: elemental_difference
#scripting name: elemental_difference
def _get_input_spec_elemental_difference(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = False, document = """average only on these entities""")
    inpin10 = _PinSpecification(name = "through_layers", type_names = ["bool"], optional = True, document = """the max elemental difference is taken through the different shell layers if true (default is false)""")
    inputs_dict_elemental_difference = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        10 : inpin10
    }
    return inputs_dict_elemental_difference[pin]

def _get_output_spec_elemental_difference(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_difference = { 
        0 : outpin0
    }
    return outputs_dict_elemental_difference[pin]

class _InputSpecElementalDifference(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_elemental_difference(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_elemental_difference(1), 1, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elemental_difference(3), 3, op, -1) 
        self.through_layers = _Input(_get_input_spec_elemental_difference(10), 10, op, -1) 

class _OutputSpecElementalDifference(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elemental_difference(0), 0, op) 

class _ElementalDifference(_Operator):
    def __init__(self):
         super().__init__("elemental_difference")
         self._name = "elemental_difference"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalDifference(self._op)
         self.outputs = _OutputSpecElementalDifference(self._op)

def elemental_difference():
    """Operator's description:
Internal name is "elemental_difference"
Scripting name is "elemental_difference"

This operator can be instantiated in both following ways:
- using dpf.Operator("elemental_difference")
- using dpf.operators.averaging.elemental_difference()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: mesh 
   3: mesh_scoping (average only on these entities)
   10: through_layers (the max elemental difference is taken through the different shell layers if true (default is false))
Output list: 
   0: fields_container 
"""
    return _ElementalDifference()

#internal name: elemental_nodal_To_nodal
#scripting name: elemental_nodal_to_nodal
def _get_input_spec_elemental_nodal_to_nodal(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "should_average", type_names = ["bool"], optional = True, document = """each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities)""")
    inpin3 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = False, document = """average only on these entities""")
    inpin10 = _PinSpecification(name = "through_layers", type_names = ["bool"], optional = True, document = """the max elemental difference is taken through the different shell layers if true (default is false)""")
    inputs_dict_elemental_nodal_to_nodal = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        10 : inpin10
    }
    return inputs_dict_elemental_nodal_to_nodal[pin]

def _get_output_spec_elemental_nodal_to_nodal(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_nodal_to_nodal = { 
        0 : outpin0
    }
    return outputs_dict_elemental_nodal_to_nodal[pin]

class _InputSpecElementalNodalToNodal(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_elemental_nodal_to_nodal(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_elemental_nodal_to_nodal(1), 1, op, -1) 
        self.should_average = _Input(_get_input_spec_elemental_nodal_to_nodal(2), 2, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elemental_nodal_to_nodal(3), 3, op, -1) 
        self.through_layers = _Input(_get_input_spec_elemental_nodal_to_nodal(10), 10, op, -1) 

class _OutputSpecElementalNodalToNodal(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elemental_nodal_to_nodal(0), 0, op) 

class _ElementalNodalToNodal(_Operator):
    def __init__(self):
         super().__init__("elemental_nodal_To_nodal")
         self._name = "elemental_nodal_To_nodal"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalNodalToNodal(self._op)
         self.outputs = _OutputSpecElementalNodalToNodal(self._op)

def elemental_nodal_to_nodal():
    """Operator's description:
Internal name is "elemental_nodal_To_nodal"
Scripting name is "elemental_nodal_to_nodal"

This operator can be instantiated in both following ways:
- using dpf.Operator("elemental_nodal_To_nodal")
- using dpf.operators.averaging.elemental_nodal_to_nodal()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: mesh 
   2: should_average (each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities))
   3: mesh_scoping (average only on these entities)
   10: through_layers (the max elemental difference is taken through the different shell layers if true (default is false))
Output list: 
   0: fields_container 
"""
    return _ElementalNodalToNodal()

#internal name: elemental_difference_fc
#scripting name: elemental_difference_fc
def _get_input_spec_elemental_difference_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")
    inpin10 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """the max elemental difference is taken through the different shell layers if true (default is false)""")
    inputs_dict_elemental_difference_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        10 : inpin10
    }
    return inputs_dict_elemental_difference_fc[pin]

def _get_output_spec_elemental_difference_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_difference_fc = { 
        0 : outpin0
    }
    return outputs_dict_elemental_difference_fc[pin]

class _InputSpecElementalDifferenceFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_elemental_difference_fc(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_elemental_difference_fc(1), 1, op, -1) 
        self.scoping = _Input(_get_input_spec_elemental_difference_fc(3), 3, op, -1) 
        self.collapse_shell_layers = _Input(_get_input_spec_elemental_difference_fc(10), 10, op, -1) 

class _OutputSpecElementalDifferenceFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elemental_difference_fc(0), 0, op) 

class _ElementalDifferenceFc(_Operator):
    def __init__(self):
         super().__init__("elemental_difference_fc")
         self._name = "elemental_difference_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalDifferenceFc(self._op)
         self.outputs = _OutputSpecElementalDifferenceFc(self._op)

def elemental_difference_fc():
    """Operator's description:
Internal name is "elemental_difference_fc"
Scripting name is "elemental_difference_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("elemental_difference_fc")
- using dpf.operators.averaging.elemental_difference_fc()

Input list: 
   0: fields_container 
   1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
   3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
   10: collapse_shell_layers (the max elemental difference is taken through the different shell layers if true (default is false))
Output list: 
   0: fields_container 
"""
    return _ElementalDifferenceFc()

#internal name: elemental_nodal_To_nodal_fc
#scripting name: elemental_nodal_to_nodal_fc
def _get_input_spec_elemental_nodal_to_nodal_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin2 = _PinSpecification(name = "should_average", type_names = ["bool"], optional = True, document = """each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities)""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container""")
    inputs_dict_elemental_nodal_to_nodal_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    return inputs_dict_elemental_nodal_to_nodal_fc[pin]

def _get_output_spec_elemental_nodal_to_nodal_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_nodal_to_nodal_fc = { 
        0 : outpin0
    }
    return outputs_dict_elemental_nodal_to_nodal_fc[pin]

class _InputSpecElementalNodalToNodalFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_elemental_nodal_to_nodal_fc(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_elemental_nodal_to_nodal_fc(1), 1, op, -1) 
        self.should_average = _Input(_get_input_spec_elemental_nodal_to_nodal_fc(2), 2, op, -1) 
        self.scoping = _Input(_get_input_spec_elemental_nodal_to_nodal_fc(3), 3, op, -1) 

class _OutputSpecElementalNodalToNodalFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elemental_nodal_to_nodal_fc(0), 0, op) 

class _ElementalNodalToNodalFc(_Operator):
    def __init__(self):
         super().__init__("elemental_nodal_To_nodal_fc")
         self._name = "elemental_nodal_To_nodal_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalNodalToNodalFc(self._op)
         self.outputs = _OutputSpecElementalNodalToNodalFc(self._op)

def elemental_nodal_to_nodal_fc():
    """Operator's description:
Internal name is "elemental_nodal_To_nodal_fc"
Scripting name is "elemental_nodal_to_nodal_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("elemental_nodal_To_nodal_fc")
- using dpf.operators.averaging.elemental_nodal_to_nodal_fc()

Input list: 
   0: fields_container 
   1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
   2: should_average (each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities))
   3: scoping (average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container)
Output list: 
   0: fields_container 
"""
    return _ElementalNodalToNodalFc()

#internal name: elemental_to_nodal
#scripting name: elemental_to_nodal
def _get_input_spec_elemental_to_nodal(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "force_averaging", type_names = ["int32"], optional = True, document = """averaging on nodes is used if this pin is set to 1 (default is 1 for integrated results and 0 for dicrete ones)""")
    inputs_dict_elemental_to_nodal = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_elemental_to_nodal[pin]

def _get_output_spec_elemental_to_nodal(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_elemental_to_nodal = { 
        0 : outpin0
    }
    return outputs_dict_elemental_to_nodal[pin]

class _InputSpecElementalToNodal(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_elemental_to_nodal(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elemental_to_nodal(1), 1, op, -1) 
        self.force_averaging = _Input(_get_input_spec_elemental_to_nodal(2), 2, op, -1) 

class _OutputSpecElementalToNodal(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_elemental_to_nodal(0), 0, op) 

class _ElementalToNodal(_Operator):
    def __init__(self):
         super().__init__("elemental_to_nodal")
         self._name = "elemental_to_nodal"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalToNodal(self._op)
         self.outputs = _OutputSpecElementalToNodal(self._op)

def elemental_to_nodal():
    """Operator's description:
Internal name is "elemental_to_nodal"
Scripting name is "elemental_to_nodal"

This operator can be instantiated in both following ways:
- using dpf.Operator("elemental_to_nodal")
- using dpf.operators.averaging.elemental_to_nodal()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: mesh_scoping 
   2: force_averaging (averaging on nodes is used if this pin is set to 1 (default is 1 for integrated results and 0 for dicrete ones))
Output list: 
   0: field 
"""
    return _ElementalToNodal()

#internal name: elemental_to_nodal_fc
#scripting name: elemental_to_nodal_fc
def _get_input_spec_elemental_to_nodal_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "force_averaging", type_names = ["int32"], optional = True, document = """averaging on nodes is used if this pin is set to 1 (default is one for integrated results and 0 for dicrete ones)""")
    inputs_dict_elemental_to_nodal_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_elemental_to_nodal_fc[pin]

def _get_output_spec_elemental_to_nodal_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_to_nodal_fc = { 
        0 : outpin0
    }
    return outputs_dict_elemental_to_nodal_fc[pin]

class _InputSpecElementalToNodalFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_elemental_to_nodal_fc(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elemental_to_nodal_fc(1), 1, op, -1) 
        self.force_averaging = _Input(_get_input_spec_elemental_to_nodal_fc(2), 2, op, -1) 

class _OutputSpecElementalToNodalFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elemental_to_nodal_fc(0), 0, op) 

class _ElementalToNodalFc(_Operator):
    def __init__(self):
         super().__init__("elemental_to_nodal_fc")
         self._name = "elemental_to_nodal_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalToNodalFc(self._op)
         self.outputs = _OutputSpecElementalToNodalFc(self._op)

def elemental_to_nodal_fc():
    """Operator's description:
Internal name is "elemental_to_nodal_fc"
Scripting name is "elemental_to_nodal_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("elemental_to_nodal_fc")
- using dpf.operators.averaging.elemental_to_nodal_fc()

Input list: 
   0: fields_container 
   1: mesh_scoping 
   2: force_averaging (averaging on nodes is used if this pin is set to 1 (default is one for integrated results and 0 for dicrete ones))
Output list: 
   0: fields_container 
"""
    return _ElementalToNodalFc()

#internal name: nodal_difference
#scripting name: nodal_difference
def _get_input_spec_nodal_difference(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "should_average", type_names = ["bool"], optional = True, document = """each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities)""")
    inpin3 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = False, document = """average only on these entities""")
    inpin10 = _PinSpecification(name = "through_layers", type_names = ["bool"], optional = True, document = """the max elemental difference is taken through the different shell layers if true (default is false)""")
    inputs_dict_nodal_difference = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        10 : inpin10
    }
    return inputs_dict_nodal_difference[pin]

def _get_output_spec_nodal_difference(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_difference = { 
        0 : outpin0
    }
    return outputs_dict_nodal_difference[pin]

class _InputSpecNodalDifference(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_nodal_difference(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_difference(1), 1, op, -1) 
        self.should_average = _Input(_get_input_spec_nodal_difference(2), 2, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_difference(3), 3, op, -1) 
        self.through_layers = _Input(_get_input_spec_nodal_difference(10), 10, op, -1) 

class _OutputSpecNodalDifference(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_difference(0), 0, op) 

class _NodalDifference(_Operator):
    def __init__(self):
         super().__init__("nodal_difference")
         self._name = "nodal_difference"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalDifference(self._op)
         self.outputs = _OutputSpecNodalDifference(self._op)

def nodal_difference():
    """Operator's description:
Internal name is "nodal_difference"
Scripting name is "nodal_difference"

This operator can be instantiated in both following ways:
- using dpf.Operator("nodal_difference")
- using dpf.operators.averaging.nodal_difference()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: mesh 
   2: should_average (each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities))
   3: mesh_scoping (average only on these entities)
   10: through_layers (the max elemental difference is taken through the different shell layers if true (default is false))
Output list: 
   0: fields_container 
"""
    return _NodalDifference()

#internal name: nodal_difference_fc
#scripting name: nodal_difference_fc
def _get_input_spec_nodal_difference_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container""")
    inputs_dict_nodal_difference_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3
    }
    return inputs_dict_nodal_difference_fc[pin]

def _get_output_spec_nodal_difference_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_difference_fc = { 
        0 : outpin0
    }
    return outputs_dict_nodal_difference_fc[pin]

class _InputSpecNodalDifferenceFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_nodal_difference_fc(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_difference_fc(1), 1, op, -1) 
        self.scoping = _Input(_get_input_spec_nodal_difference_fc(3), 3, op, -1) 

class _OutputSpecNodalDifferenceFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_difference_fc(0), 0, op) 

class _NodalDifferenceFc(_Operator):
    def __init__(self):
         super().__init__("nodal_difference_fc")
         self._name = "nodal_difference_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalDifferenceFc(self._op)
         self.outputs = _OutputSpecNodalDifferenceFc(self._op)

def nodal_difference_fc():
    """Operator's description:
Internal name is "nodal_difference_fc"
Scripting name is "nodal_difference_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("nodal_difference_fc")
- using dpf.operators.averaging.nodal_difference_fc()

Input list: 
   0: fields_container 
   1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
   3: scoping (average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container)
Output list: 
   0: fields_container 
"""
    return _NodalDifferenceFc()

#internal name: elemental_fraction_fc
#scripting name: elemental_fraction_fc
def _get_input_spec_elemental_fraction_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")
    inpin6 = _PinSpecification(name = "denominator", type_names = ["fields_container"], optional = True, document = """if a fields container is set in this pin, it is used as the denominator of the fraction instead of entity_average_fc""")
    inpin10 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """the elemental difference and the entity average are taken through the different shell layers if true (default is false)""")
    inputs_dict_elemental_fraction_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        6 : inpin6,
        10 : inpin10
    }
    return inputs_dict_elemental_fraction_fc[pin]

def _get_output_spec_elemental_fraction_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_fraction_fc = { 
        0 : outpin0
    }
    return outputs_dict_elemental_fraction_fc[pin]

class _InputSpecElementalFractionFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_elemental_fraction_fc(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_elemental_fraction_fc(1), 1, op, -1) 
        self.scoping = _Input(_get_input_spec_elemental_fraction_fc(3), 3, op, -1) 
        self.denominator = _Input(_get_input_spec_elemental_fraction_fc(6), 6, op, -1) 
        self.collapse_shell_layers = _Input(_get_input_spec_elemental_fraction_fc(10), 10, op, -1) 

class _OutputSpecElementalFractionFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elemental_fraction_fc(0), 0, op) 

class _ElementalFractionFc(_Operator):
    def __init__(self):
         super().__init__("elemental_fraction_fc")
         self._name = "elemental_fraction_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalFractionFc(self._op)
         self.outputs = _OutputSpecElementalFractionFc(self._op)

def elemental_fraction_fc():
    """Operator's description:
Internal name is "elemental_fraction_fc"
Scripting name is "elemental_fraction_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("elemental_fraction_fc")
- using dpf.operators.averaging.elemental_fraction_fc()

Input list: 
   0: fields_container 
   1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
   3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
   6: denominator (if a fields container is set in this pin, it is used as the denominator of the fraction instead of entity_average_fc)
   10: collapse_shell_layers (the elemental difference and the entity average are taken through the different shell layers if true (default is false))
Output list: 
   0: fields_container 
"""
    return _ElementalFractionFc()

#internal name: to_nodal
#scripting name: to_nodal
def _get_input_spec_to_nodal(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inputs_dict_to_nodal = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_to_nodal[pin]

def _get_output_spec_to_nodal(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_to_nodal = { 
        0 : outpin0
    }
    return outputs_dict_to_nodal[pin]

class _InputSpecToNodal(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_to_nodal(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_to_nodal(1), 1, op, -1) 

class _OutputSpecToNodal(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_to_nodal(0), 0, op) 

class _ToNodal(_Operator):
    def __init__(self):
         super().__init__("to_nodal")
         self._name = "to_nodal"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecToNodal(self._op)
         self.outputs = _OutputSpecToNodal(self._op)

def to_nodal():
    """Operator's description:
Internal name is "to_nodal"
Scripting name is "to_nodal"

This operator can be instantiated in both following ways:
- using dpf.Operator("to_nodal")
- using dpf.operators.averaging.to_nodal()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: mesh_scoping 
Output list: 
   0: field 
"""
    return _ToNodal()

#internal name: to_nodal_fc
#scripting name: to_nodal_fc
def _get_input_spec_to_nodal_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inputs_dict_to_nodal_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3
    }
    return inputs_dict_to_nodal_fc[pin]

def _get_output_spec_to_nodal_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_to_nodal_fc = { 
        0 : outpin0
    }
    return outputs_dict_to_nodal_fc[pin]

class _InputSpecToNodalFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_to_nodal_fc(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_to_nodal_fc(1), 1, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_to_nodal_fc(3), 3, op, -1) 

class _OutputSpecToNodalFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_to_nodal_fc(0), 0, op) 

class _ToNodalFc(_Operator):
    def __init__(self):
         super().__init__("to_nodal_fc")
         self._name = "to_nodal_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecToNodalFc(self._op)
         self.outputs = _OutputSpecToNodalFc(self._op)

def to_nodal_fc():
    """Operator's description:
Internal name is "to_nodal_fc"
Scripting name is "to_nodal_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("to_nodal_fc")
- using dpf.operators.averaging.to_nodal_fc()

Input list: 
   0: fields_container 
   1: mesh 
   3: mesh_scoping 
Output list: 
   0: fields_container 
"""
    return _ToNodalFc()

#internal name: ElementalNodal_To_NodalElemental
#scripting name: elemental_nodal_to_nodal_elemental
def _get_input_spec_elemental_nodal_to_nodal_elemental(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inputs_dict_elemental_nodal_to_nodal_elemental = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_elemental_nodal_to_nodal_elemental[pin]

def _get_output_spec_elemental_nodal_to_nodal_elemental(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_elemental_nodal_to_nodal_elemental = { 
        0 : outpin0
    }
    return outputs_dict_elemental_nodal_to_nodal_elemental[pin]

class _InputSpecElementalNodalToNodalElemental(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_elemental_nodal_to_nodal_elemental(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elemental_nodal_to_nodal_elemental(1), 1, op, -1) 

class _OutputSpecElementalNodalToNodalElemental(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_elemental_nodal_to_nodal_elemental(0), 0, op) 

class _ElementalNodalToNodalElemental(_Operator):
    def __init__(self):
         super().__init__("ElementalNodal_To_NodalElemental")
         self._name = "ElementalNodal_To_NodalElemental"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalNodalToNodalElemental(self._op)
         self.outputs = _OutputSpecElementalNodalToNodalElemental(self._op)

def elemental_nodal_to_nodal_elemental():
    """Operator's description:
Internal name is "ElementalNodal_To_NodalElemental"
Scripting name is "elemental_nodal_to_nodal_elemental"

This operator can be instantiated in both following ways:
- using dpf.Operator("ElementalNodal_To_NodalElemental")
- using dpf.operators.averaging.elemental_nodal_to_nodal_elemental()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: mesh_scoping 
Output list: 
   0: field 
"""
    return _ElementalNodalToNodalElemental()

#internal name: extend_to_mid_nodes
#scripting name: extend_to_mid_nodes
def _get_input_spec_extend_to_mid_nodes(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_extend_to_mid_nodes = { 
        0 : inpin0
    }
    return inputs_dict_extend_to_mid_nodes[pin]

def _get_output_spec_extend_to_mid_nodes(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_extend_to_mid_nodes = { 
        0 : outpin0
    }
    return outputs_dict_extend_to_mid_nodes[pin]

class _InputSpecExtendToMidNodes(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_extend_to_mid_nodes(0), 0, op, -1) 

class _OutputSpecExtendToMidNodes(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_extend_to_mid_nodes(0), 0, op) 

class _ExtendToMidNodes(_Operator):
    def __init__(self):
         super().__init__("extend_to_mid_nodes")
         self._name = "extend_to_mid_nodes"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecExtendToMidNodes(self._op)
         self.outputs = _OutputSpecExtendToMidNodes(self._op)

def extend_to_mid_nodes():
    """Operator's description:
Internal name is "extend_to_mid_nodes"
Scripting name is "extend_to_mid_nodes"

This operator can be instantiated in both following ways:
- using dpf.Operator("extend_to_mid_nodes")
- using dpf.operators.averaging.extend_to_mid_nodes()

Input list: 
   0: field (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    return _ExtendToMidNodes()

#internal name: extend_to_mid_nodes_fc
#scripting name: extend_to_mid_nodes_fc
def _get_input_spec_extend_to_mid_nodes_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inputs_dict_extend_to_mid_nodes_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_extend_to_mid_nodes_fc[pin]

def _get_output_spec_extend_to_mid_nodes_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_extend_to_mid_nodes_fc = { 
        0 : outpin0
    }
    return outputs_dict_extend_to_mid_nodes_fc[pin]

class _InputSpecExtendToMidNodesFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_extend_to_mid_nodes_fc(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_extend_to_mid_nodes_fc(1), 1, op, -1) 

class _OutputSpecExtendToMidNodesFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_extend_to_mid_nodes_fc(0), 0, op) 

class _ExtendToMidNodesFc(_Operator):
    def __init__(self):
         super().__init__("extend_to_mid_nodes_fc")
         self._name = "extend_to_mid_nodes_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecExtendToMidNodesFc(self._op)
         self.outputs = _OutputSpecExtendToMidNodesFc(self._op)

def extend_to_mid_nodes_fc():
    """Operator's description:
Internal name is "extend_to_mid_nodes_fc"
Scripting name is "extend_to_mid_nodes_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("extend_to_mid_nodes_fc")
- using dpf.operators.averaging.extend_to_mid_nodes_fc()

Input list: 
   0: fields_container 
   1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
Output list: 
   0: fields_container 
"""
    return _ExtendToMidNodesFc()

#internal name: entity_average
#scripting name: elemental_mean
def _get_input_spec_elemental_mean(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """if true shell layers are averaged as well (default is false)""")
    inpin2 = _PinSpecification(name = "force_averaging", type_names = ["bool"], optional = True, document = """if true you average, if false you just sum""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")
    inputs_dict_elemental_mean = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    return inputs_dict_elemental_mean[pin]

def _get_output_spec_elemental_mean(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_elemental_mean = { 
        0 : outpin0
    }
    return outputs_dict_elemental_mean[pin]

class _InputSpecElementalMean(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_elemental_mean(0), 0, op, -1) 
        self.collapse_shell_layers = _Input(_get_input_spec_elemental_mean(1), 1, op, -1) 
        self.force_averaging = _Input(_get_input_spec_elemental_mean(2), 2, op, -1) 
        self.scoping = _Input(_get_input_spec_elemental_mean(3), 3, op, -1) 

class _OutputSpecElementalMean(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_elemental_mean(0), 0, op) 

class _ElementalMean(_Operator):
    def __init__(self):
         super().__init__("entity_average")
         self._name = "entity_average"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalMean(self._op)
         self.outputs = _OutputSpecElementalMean(self._op)

def elemental_mean():
    """Operator's description:
Internal name is "entity_average"
Scripting name is "elemental_mean"

This operator can be instantiated in both following ways:
- using dpf.Operator("entity_average")
- using dpf.operators.averaging.elemental_mean()

Input list: 
   0: field 
   1: collapse_shell_layers (if true shell layers are averaged as well (default is false))
   2: force_averaging (if true you average, if false you just sum)
   3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
Output list: 
   0: field 
"""
    return _ElementalMean()

#internal name: entity_average_fc
#scripting name: elemental_mean_fc
def _get_input_spec_elemental_mean_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """if true shell layers are averaged as well (default is false)""")
    inpin2 = _PinSpecification(name = "force_averaging", type_names = ["bool"], optional = True, document = """if true you average, if false you just sum""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")
    inpin4 = _PinSpecification(name = "meshed_region", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inputs_dict_elemental_mean_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_elemental_mean_fc[pin]

def _get_output_spec_elemental_mean_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_mean_fc = { 
        0 : outpin0
    }
    return outputs_dict_elemental_mean_fc[pin]

class _InputSpecElementalMeanFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_elemental_mean_fc(0), 0, op, -1) 
        self.collapse_shell_layers = _Input(_get_input_spec_elemental_mean_fc(1), 1, op, -1) 
        self.force_averaging = _Input(_get_input_spec_elemental_mean_fc(2), 2, op, -1) 
        self.scoping = _Input(_get_input_spec_elemental_mean_fc(3), 3, op, -1) 
        self.meshed_region = _Input(_get_input_spec_elemental_mean_fc(4), 4, op, -1) 

class _OutputSpecElementalMeanFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elemental_mean_fc(0), 0, op) 

class _ElementalMeanFc(_Operator):
    def __init__(self):
         super().__init__("entity_average_fc")
         self._name = "entity_average_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalMeanFc(self._op)
         self.outputs = _OutputSpecElementalMeanFc(self._op)

def elemental_mean_fc():
    """Operator's description:
Internal name is "entity_average_fc"
Scripting name is "elemental_mean_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("entity_average_fc")
- using dpf.operators.averaging.elemental_mean_fc()

Input list: 
   0: fields_container 
   1: collapse_shell_layers (if true shell layers are averaged as well (default is false))
   2: force_averaging (if true you average, if false you just sum)
   3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
   4: meshed_region (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
Output list: 
   0: fields_container 
"""
    return _ElementalMeanFc()

#internal name: to_elemental_fc
#scripting name: to_elemental_fc
def _get_input_spec_to_elemental_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin7 = _PinSpecification(name = "smoothen_values", type_names = ["bool"], optional = True, document = """if it is set to true, elemental nodal fields are first averaged on nodes and then averaged on elements (default is false)""")
    inpin10 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """if true shell layers are averaged as well (default is false)""")
    inputs_dict_to_elemental_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        7 : inpin7,
        10 : inpin10
    }
    return inputs_dict_to_elemental_fc[pin]

def _get_output_spec_to_elemental_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_to_elemental_fc = { 
        0 : outpin0
    }
    return outputs_dict_to_elemental_fc[pin]

class _InputSpecToElementalFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_to_elemental_fc(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_to_elemental_fc(1), 1, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_to_elemental_fc(3), 3, op, -1) 
        self.smoothen_values = _Input(_get_input_spec_to_elemental_fc(7), 7, op, -1) 
        self.collapse_shell_layers = _Input(_get_input_spec_to_elemental_fc(10), 10, op, -1) 

class _OutputSpecToElementalFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_to_elemental_fc(0), 0, op) 

class _ToElementalFc(_Operator):
    def __init__(self):
         super().__init__("to_elemental_fc")
         self._name = "to_elemental_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecToElementalFc(self._op)
         self.outputs = _OutputSpecToElementalFc(self._op)

def to_elemental_fc():
    """Operator's description:
Internal name is "to_elemental_fc"
Scripting name is "to_elemental_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("to_elemental_fc")
- using dpf.operators.averaging.to_elemental_fc()

Input list: 
   0: fields_container 
   1: mesh 
   3: mesh_scoping 
   7: smoothen_values (if it is set to true, elemental nodal fields are first averaged on nodes and then averaged on elements (default is false))
   10: collapse_shell_layers (if true shell layers are averaged as well (default is false))
Output list: 
   0: fields_container 
"""
    return _ToElementalFc()

#internal name: nodal_to_elemental
#scripting name: nodal_to_elemental
def _get_input_spec_nodal_to_elemental(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin10 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """if true shell layers are averaged as well (default is false)""")
    inputs_dict_nodal_to_elemental = { 
        0 : inpin0,
        1 : inpin1,
        10 : inpin10
    }
    return inputs_dict_nodal_to_elemental[pin]

def _get_output_spec_nodal_to_elemental(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_nodal_to_elemental = { 
        0 : outpin0
    }
    return outputs_dict_nodal_to_elemental[pin]

class _InputSpecNodalToElemental(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_nodal_to_elemental(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_to_elemental(1), 1, op, -1) 
        self.collapse_shell_layers = _Input(_get_input_spec_nodal_to_elemental(10), 10, op, -1) 

class _OutputSpecNodalToElemental(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_nodal_to_elemental(0), 0, op) 

class _NodalToElemental(_Operator):
    def __init__(self):
         super().__init__("nodal_to_elemental")
         self._name = "nodal_to_elemental"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalToElemental(self._op)
         self.outputs = _OutputSpecNodalToElemental(self._op)

def nodal_to_elemental():
    """Operator's description:
Internal name is "nodal_to_elemental"
Scripting name is "nodal_to_elemental"

This operator can be instantiated in both following ways:
- using dpf.Operator("nodal_to_elemental")
- using dpf.operators.averaging.nodal_to_elemental()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: mesh_scoping 
   10: collapse_shell_layers (if true shell layers are averaged as well (default is false))
Output list: 
   0: field 
"""
    return _NodalToElemental()

#internal name: nodal_to_elemental_fc
#scripting name: nodal_to_elemental_fc
def _get_input_spec_nodal_to_elemental_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")
    inpin10 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """if true shell layers are averaged as well (default is false)""")
    inputs_dict_nodal_to_elemental_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        10 : inpin10
    }
    return inputs_dict_nodal_to_elemental_fc[pin]

def _get_output_spec_nodal_to_elemental_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_to_elemental_fc = { 
        0 : outpin0
    }
    return outputs_dict_nodal_to_elemental_fc[pin]

class _InputSpecNodalToElementalFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_nodal_to_elemental_fc(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_to_elemental_fc(1), 1, op, -1) 
        self.scoping = _Input(_get_input_spec_nodal_to_elemental_fc(3), 3, op, -1) 
        self.collapse_shell_layers = _Input(_get_input_spec_nodal_to_elemental_fc(10), 10, op, -1) 

class _OutputSpecNodalToElementalFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_to_elemental_fc(0), 0, op) 

class _NodalToElementalFc(_Operator):
    def __init__(self):
         super().__init__("nodal_to_elemental_fc")
         self._name = "nodal_to_elemental_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalToElementalFc(self._op)
         self.outputs = _OutputSpecNodalToElementalFc(self._op)

def nodal_to_elemental_fc():
    """Operator's description:
Internal name is "nodal_to_elemental_fc"
Scripting name is "nodal_to_elemental_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("nodal_to_elemental_fc")
- using dpf.operators.averaging.nodal_to_elemental_fc()

Input list: 
   0: fields_container 
   1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
   3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
   10: collapse_shell_layers (if true shell layers are averaged as well (default is false))
Output list: 
   0: fields_container 
"""
    return _NodalToElementalFc()

