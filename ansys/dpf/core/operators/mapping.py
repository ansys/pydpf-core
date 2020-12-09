from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "mapping" category
"""

#internal name: solid_to_skin
#scripting name: solid_to_skin
def _get_input_spec_solid_to_skin(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["meshed_region"], optional = True, document = """skin mesh region expected""")
    inputs_dict_solid_to_skin = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_solid_to_skin[pin]

def _get_output_spec_solid_to_skin(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_solid_to_skin = { 
        0 : outpin0
    }
    return outputs_dict_solid_to_skin[pin]

class _InputSpecSolidToSkin(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_solid_to_skin(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_solid_to_skin(1), 1, op, -1) 

class _OutputSpecSolidToSkin(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_solid_to_skin(0), 0, op) 

class _SolidToSkin:
    """Operator's description:
Internal name is "solid_to_skin"
Scripting name is "solid_to_skin"

This operator can be instantiated in both following ways:
- using dpf.Operator("solid_to_skin")
- using dpf.operators.mapping.solid_to_skin()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: mesh_scoping (skin mesh region expected)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "solid_to_skin"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSolidToSkin(self._op)
         self.outputs = _OutputSpecSolidToSkin(self._op)

def solid_to_skin():
    return _SolidToSkin()

#internal name: mapping
#scripting name: on_coordinates
def _get_input_spec_on_coordinates(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "coordinates", type_names = ["field"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "create_support", type_names = ["bool"], optional = True, document = """if this pin is set to true, then, a support associated to the fields consisting of points is created""")
    inpin3 = _PinSpecification(name = "mapping_on_scoping", type_names = ["bool"], optional = True, document = """if this pin is set to true, then the mapping between the coordinates and the fields is created only on the first field scoping""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """if the first field in input has no mesh in support, then the mesh in this pin is expected (default is false)""")
    inputs_dict_on_coordinates = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        7 : inpin7
    }
    return inputs_dict_on_coordinates[pin]

def _get_output_spec_on_coordinates(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_on_coordinates = { 
        0 : outpin0
    }
    return outputs_dict_on_coordinates[pin]

class _InputSpecOnCoordinates(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_on_coordinates(0), 0, op, -1) 
        self.coordinates = _Input(_get_input_spec_on_coordinates(1), 1, op, -1) 
        self.create_support = _Input(_get_input_spec_on_coordinates(2), 2, op, -1) 
        self.mapping_on_scoping = _Input(_get_input_spec_on_coordinates(3), 3, op, -1) 
        self.mesh = _Input(_get_input_spec_on_coordinates(7), 7, op, -1) 

class _OutputSpecOnCoordinates(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_on_coordinates(0), 0, op) 

class _OnCoordinates:
    """Operator's description:
Internal name is "mapping"
Scripting name is "on_coordinates"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapping")
- using dpf.operators.mapping.on_coordinates()

Input list: 
   0: fields_container 
   1: coordinates 
   2: create_support (if this pin is set to true, then, a support associated to the fields consisting of points is created)
   3: mapping_on_scoping (if this pin is set to true, then the mapping between the coordinates and the fields is created only on the first field scoping)
   7: mesh (if the first field in input has no mesh in support, then the mesh in this pin is expected (default is false))
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "mapping"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecOnCoordinates(self._op)
         self.outputs = _OutputSpecOnCoordinates(self._op)

def on_coordinates():
    return _OnCoordinates()

#internal name: scoping::on_coordinates
#scripting name: scoping_on_coordinates
def _get_input_spec_scoping_on_coordinates(pin):
    inpin0 = _PinSpecification(name = "coordinates", type_names = ["field"], optional = False, document = """""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inputs_dict_scoping_on_coordinates = { 
        0 : inpin0,
        7 : inpin7
    }
    return inputs_dict_scoping_on_coordinates[pin]

def _get_output_spec_scoping_on_coordinates(pin):
    outpin0 = _PinSpecification(name = "scoping", type_names = ["scoping"], document = """""")
    outputs_dict_scoping_on_coordinates = { 
        0 : outpin0
    }
    return outputs_dict_scoping_on_coordinates[pin]

class _InputSpecScopingOnCoordinates(_Inputs):
    def __init__(self, op: _Operator):
        self.coordinates = _Input(_get_input_spec_scoping_on_coordinates(0), 0, op, -1) 
        self.mesh = _Input(_get_input_spec_scoping_on_coordinates(7), 7, op, -1) 

class _OutputSpecScopingOnCoordinates(_Outputs):
    def __init__(self, op: _Operator):
        self.scoping = _Output(_get_output_spec_scoping_on_coordinates(0), 0, op) 

class _ScopingOnCoordinates:
    """Operator's description:
Internal name is "scoping::on_coordinates"
Scripting name is "scoping_on_coordinates"

This operator can be instantiated in both following ways:
- using dpf.Operator("scoping::on_coordinates")
- using dpf.operators.mapping.scoping_on_coordinates()

Input list: 
   0: coordinates 
   7: mesh 
Output list: 
   0: scoping 
"""
    def __init__(self):
         self._name = "scoping::on_coordinates"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecScopingOnCoordinates(self._op)
         self.outputs = _OutputSpecScopingOnCoordinates(self._op)

def scoping_on_coordinates():
    return _ScopingOnCoordinates()

