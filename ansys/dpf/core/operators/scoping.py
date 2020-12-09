from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "scoping" category
"""

#internal name: GetElementScopingFromMesh
#scripting name: elemental_from_mesh
def _get_input_spec_elemental_from_mesh(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inputs_dict_elemental_from_mesh = { 
        0 : inpin0
    }
    return inputs_dict_elemental_from_mesh[pin]

def _get_output_spec_elemental_from_mesh(pin):
    outpin0 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], document = """""")
    outputs_dict_elemental_from_mesh = { 
        0 : outpin0
    }
    return outputs_dict_elemental_from_mesh[pin]

class _InputSpecElementalFromMesh(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_elemental_from_mesh(0), 0, op, -1) 

class _OutputSpecElementalFromMesh(_Outputs):
    def __init__(self, op: _Operator):
        self.mesh_scoping = _Output(_get_output_spec_elemental_from_mesh(0), 0, op) 

class _ElementalFromMesh(_Operator):
    def __init__(self):
         super().__init__("GetElementScopingFromMesh")
         self._name = "GetElementScopingFromMesh"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalFromMesh(self._op)
         self.outputs = _OutputSpecElementalFromMesh(self._op)

def elemental_from_mesh():
    """Operator's description:
Internal name is "GetElementScopingFromMesh"
Scripting name is "elemental_from_mesh"

This operator can be instantiated in both following ways:
- using dpf.Operator("GetElementScopingFromMesh")
- using dpf.operators.scoping.elemental_from_mesh()

Input list: 
   0: mesh 
Output list: 
   0: mesh_scoping 
"""
    return _ElementalFromMesh()

#internal name: scoping::intersect
#scripting name: intersect
def _get_input_spec_intersect(pin):
    inpin0 = _PinSpecification(name = "scopingA", type_names = ["scoping"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "scopingB", type_names = ["scoping"], optional = False, document = """""")
    inputs_dict_intersect = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_intersect[pin]

def _get_output_spec_intersect(pin):
    outpin0 = _PinSpecification(name = "intersection", type_names = ["scoping"], document = """""")
    outpin1 = _PinSpecification(name = "scopingA_min_intersection", type_names = ["scoping"], document = """""")
    outputs_dict_intersect = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_intersect[pin]

class _InputSpecIntersect(_Inputs):
    def __init__(self, op: _Operator):
        self.scopingA = _Input(_get_input_spec_intersect(0), 0, op, -1) 
        self.scopingB = _Input(_get_input_spec_intersect(1), 1, op, -1) 

class _OutputSpecIntersect(_Outputs):
    def __init__(self, op: _Operator):
        self.intersection = _Output(_get_output_spec_intersect(0), 0, op) 
        self.scopingA_min_intersection = _Output(_get_output_spec_intersect(1), 1, op) 

class _Intersect(_Operator):
    def __init__(self):
         super().__init__("scoping::intersect")
         self._name = "scoping::intersect"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecIntersect(self._op)
         self.outputs = _OutputSpecIntersect(self._op)

def intersect():
    """Operator's description:
Internal name is "scoping::intersect"
Scripting name is "intersect"

This operator can be instantiated in both following ways:
- using dpf.Operator("scoping::intersect")
- using dpf.operators.scoping.intersect()

Input list: 
   0: scopingA 
   1: scopingB 
Output list: 
   0: intersection 
   1: scopingA_min_intersection 
"""
    return _Intersect()

#internal name: scoping_provider_by_prop
#scripting name: on_property
def _get_input_spec_on_property(pin):
    inpin0 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = False, document = """Nodal or Elemental location are expected""")
    inpin1 = _PinSpecification(name = "property_name", type_names = ["string"], optional = False, document = """ex: "mapdl_element_type", "apdl_type_index", "mapdl_type_id", "material", "apdl_section_id", "apdl_real_id", "shell_axi", "volume_axi"...""")
    inpin2 = _PinSpecification(name = "property_id", type_names = ["int32"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inpin5 = _PinSpecification(name = "inclusive", type_names = ["int32"], optional = True, document = """If element scoping is requested on a nodal named selection, if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included""")
    inputs_dict_on_property = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5
    }
    return inputs_dict_on_property[pin]

def _get_output_spec_on_property(pin):
    outpin0 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], document = """Scoping""")
    outputs_dict_on_property = { 
        0 : outpin0
    }
    return outputs_dict_on_property[pin]

class _InputSpecOnProperty(_Inputs):
    def __init__(self, op: _Operator):
        self.requested_location = _Input(_get_input_spec_on_property(0), 0, op, -1) 
        self.property_name = _Input(_get_input_spec_on_property(1), 1, op, -1) 
        self.property_id = _Input(_get_input_spec_on_property(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_on_property(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_on_property(4), 4, op, -1) 
        self.inclusive = _Input(_get_input_spec_on_property(5), 5, op, -1) 

class _OutputSpecOnProperty(_Outputs):
    def __init__(self, op: _Operator):
        self.mesh_scoping = _Output(_get_output_spec_on_property(0), 0, op) 

class _OnProperty(_Operator):
    def __init__(self):
         super().__init__("scoping_provider_by_prop")
         self._name = "scoping_provider_by_prop"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecOnProperty(self._op)
         self.outputs = _OutputSpecOnProperty(self._op)

def on_property():
    """Operator's description:
Internal name is "scoping_provider_by_prop"
Scripting name is "on_property"

This operator can be instantiated in both following ways:
- using dpf.Operator("scoping_provider_by_prop")
- using dpf.operators.scoping.on_property()

Input list: 
   0: requested_location (Nodal or Elemental location are expected)
   1: property_name (ex: "mapdl_element_type", "apdl_type_index", "mapdl_type_id", "material", "apdl_section_id", "apdl_real_id", "shell_axi", "volume_axi"...)
   2: property_id 
   3: streams_container 
   4: data_sources 
   5: inclusive (If element scoping is requested on a nodal named selection, if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included)
Output list: 
   0: mesh_scoping (Scoping)
"""
    return _OnProperty()

#internal name: transpose_scoping
#scripting name: transpose
def _get_input_spec_transpose(pin):
    inpin0 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping","scopings_container"], optional = False, document = """Scoping or scopings container (the input type is the output type)""")
    inpin1 = _PinSpecification(name = "meshed_region", type_names = ["meshed_region"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "inclusive", type_names = ["int32"], optional = True, document = """if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included""")
    inputs_dict_transpose = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_transpose[pin]

def _get_output_spec_transpose(pin):
    outpin0 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], document = """Scoping or scopings container (the input type is the output type)""")
    outputs_dict_transpose = { 
        0 : outpin0
    }
    return outputs_dict_transpose[pin]

class _InputSpecTranspose(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh_scoping = _Input(_get_input_spec_transpose(0), 0, op, -1) 
        self.meshed_region = _Input(_get_input_spec_transpose(1), 1, op, -1) 
        self.inclusive = _Input(_get_input_spec_transpose(2), 2, op, -1) 

class _OutputSpecTranspose(_Outputs):
    def __init__(self, op: _Operator):
        self.mesh_scoping = _Output(_get_output_spec_transpose(0), 0, op) 

class _Transpose(_Operator):
    def __init__(self):
         super().__init__("transpose_scoping")
         self._name = "transpose_scoping"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecTranspose(self._op)
         self.outputs = _OutputSpecTranspose(self._op)

def transpose():
    """Operator's description:
Internal name is "transpose_scoping"
Scripting name is "transpose"

This operator can be instantiated in both following ways:
- using dpf.Operator("transpose_scoping")
- using dpf.operators.scoping.transpose()

Input list: 
   0: mesh_scoping (Scoping or scopings container (the input type is the output type))
   1: meshed_region 
   2: inclusive (if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included)
Output list: 
   0: mesh_scoping (Scoping or scopings container (the input type is the output type))
"""
    return _Transpose()

#internal name: core::scoping::low_pass
#scripting name: scoping.low_pass
def _get_input_spec_low_pass(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "threshold", type_names = ["double","field"], optional = False, document = """a threshold scalar or a field containing one value is expected""")
    inputs_dict_low_pass = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_low_pass[pin]

def _get_output_spec_low_pass(pin):
    outpin0 = _PinSpecification(name = "scoping", type_names = ["scoping"], document = """""")
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
        self.scoping = _Output(_get_output_spec_low_pass(0), 0, op) 

class _LowPass(_Operator):
    def __init__(self):
         super().__init__("core::scoping::low_pass")
         self._name = "core::scoping::low_pass"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecLowPass(self._op)
         self.outputs = _OutputSpecLowPass(self._op)

def low_pass():
    """Operator's description:
Internal name is "core::scoping::low_pass"
Scripting name is "scoping.low_pass"

This operator can be instantiated in both following ways:
- using dpf.Operator("core::scoping::low_pass")
- using dpf.operators.filter.scoping.low_pass()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: threshold (a threshold scalar or a field containing one value is expected)
Output list: 
   0: scoping 
"""
    return _LowPass()

#internal name: scoping::by_property
#scripting name: splitted_on_property_type
def _get_input_spec_splitted_on_property_type(pin):
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """Scoping""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """mesh region""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = False, document = """location (default is elemental)""")
    inpin13 = _PinSpecification(name = "label1", type_names = ["string"], optional = True, document = """properties to apply the filtering 'mat' and/or 'elshape' (default is 'elshape)""")
    inpin14 = _PinSpecification(name = "label2", type_names = ["string"], optional = False, document = """""")
    inputs_dict_splitted_on_property_type = { 
        1 : inpin1,
        7 : inpin7,
        9 : inpin9,
        13 : inpin13,
        14 : inpin14
    }
    return inputs_dict_splitted_on_property_type[pin]

def _get_output_spec_splitted_on_property_type(pin):
    outpin0 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container"], document = """Scoping""")
    outputs_dict_splitted_on_property_type = { 
        0 : outpin0
    }
    return outputs_dict_splitted_on_property_type[pin]

class _InputSpecSplittedOnPropertyType(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh_scoping = _Input(_get_input_spec_splitted_on_property_type(1), 1, op, -1) 
        self.mesh = _Input(_get_input_spec_splitted_on_property_type(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_splitted_on_property_type(9), 9, op, -1) 
        self.label1 = _Input(_get_input_spec_splitted_on_property_type(13), 13, op, 0) 
        self.label2 = _Input(_get_input_spec_splitted_on_property_type(14), 14, op, -1) 

class _OutputSpecSplittedOnPropertyType(_Outputs):
    def __init__(self, op: _Operator):
        self.mesh_scoping = _Output(_get_output_spec_splitted_on_property_type(0), 0, op) 

class _SplittedOnPropertyType(_Operator):
    def __init__(self):
         super().__init__("scoping::by_property")
         self._name = "scoping::by_property"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSplittedOnPropertyType(self._op)
         self.outputs = _OutputSpecSplittedOnPropertyType(self._op)

def splitted_on_property_type():
    """Operator's description:
Internal name is "scoping::by_property"
Scripting name is "splitted_on_property_type"

This operator can be instantiated in both following ways:
- using dpf.Operator("scoping::by_property")
- using dpf.operators.scoping.splitted_on_property_type()

Input list: 
   1: mesh_scoping (Scoping)
   7: mesh (mesh region)
   9: requested_location (location (default is elemental))
   13: label1 (properties to apply the filtering 'mat' and/or 'elshape' (default is 'elshape))
   14: label2 
Output list: 
   0: mesh_scoping (Scoping)
"""
    return _SplittedOnPropertyType()

#internal name: Rescope
#scripting name: rescope
def _get_input_spec_rescope(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = False, document = """""")
    inputs_dict_rescope = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_rescope[pin]

def _get_output_spec_rescope(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_rescope = { 
        0 : outpin0
    }
    return outputs_dict_rescope[pin]

class _InputSpecRescope(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_rescope(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_rescope(1), 1, op, -1) 

class _OutputSpecRescope(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_rescope(0), 0, op) 

class _Rescope(_Operator):
    def __init__(self):
         super().__init__("Rescope")
         self._name = "Rescope"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecRescope(self._op)
         self.outputs = _OutputSpecRescope(self._op)

def rescope():
    """Operator's description:
Internal name is "Rescope"
Scripting name is "rescope"

This operator can be instantiated in both following ways:
- using dpf.Operator("Rescope")
- using dpf.operators.scoping.rescope()

Input list: 
   0: fields_container 
   1: mesh_scoping 
Output list: 
   0: fields_container 
"""
    return _Rescope()

#internal name: scoping_provider_by_ns
#scripting name: on_named_selection
def _get_input_spec_on_named_selection(pin):
    inpin0 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "named_selection_name", type_names = ["string"], optional = False, document = """the string is expected to be in upper case""")
    inpin2 = _PinSpecification(name = "int_inclusive", type_names = ["int32"], optional = True, document = """If element scoping is requested on a nodal named selection, if Inclusive == 1 then add all the elements adjacent to the nodes.If Inclusive == 0, only the elements which have all their nodes in the named selection are included""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_on_named_selection = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_on_named_selection[pin]

def _get_output_spec_on_named_selection(pin):
    outpin0 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], document = """""")
    outputs_dict_on_named_selection = { 
        0 : outpin0
    }
    return outputs_dict_on_named_selection[pin]

class _InputSpecOnNamedSelection(_Inputs):
    def __init__(self, op: _Operator):
        self.requested_location = _Input(_get_input_spec_on_named_selection(0), 0, op, -1) 
        self.named_selection_name = _Input(_get_input_spec_on_named_selection(1), 1, op, -1) 
        self.int_inclusive = _Input(_get_input_spec_on_named_selection(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_on_named_selection(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_on_named_selection(4), 4, op, -1) 

class _OutputSpecOnNamedSelection(_Outputs):
    def __init__(self, op: _Operator):
        self.mesh_scoping = _Output(_get_output_spec_on_named_selection(0), 0, op) 

class _OnNamedSelection(_Operator):
    def __init__(self):
         super().__init__("scoping_provider_by_ns")
         self._name = "scoping_provider_by_ns"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecOnNamedSelection(self._op)
         self.outputs = _OutputSpecOnNamedSelection(self._op)

def on_named_selection():
    """Operator's description:
Internal name is "scoping_provider_by_ns"
Scripting name is "on_named_selection"

This operator can be instantiated in both following ways:
- using dpf.Operator("scoping_provider_by_ns")
- using dpf.operators.scoping.on_named_selection()

Input list: 
   0: requested_location 
   1: named_selection_name (the string is expected to be in upper case)
   2: int_inclusive (If element scoping is requested on a nodal named selection, if Inclusive == 1 then add all the elements adjacent to the nodes.If Inclusive == 0, only the elements which have all their nodes in the named selection are included)
   3: streams_container 
   4: data_sources 
Output list: 
   0: mesh_scoping 
"""
    return _OnNamedSelection()

#internal name: scoping::connectivity_ids
#scripting name: connectivity_ids
def _get_input_spec_connectivity_ids(pin):
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = False, document = """Elemental scoping""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the support of the scoping is expected if there is no mesh in input""")
    inpin10 = _PinSpecification(name = "take_mid_nodes", type_names = ["bool"], optional = True, document = """default is true""")
    inputs_dict_connectivity_ids = { 
        1 : inpin1,
        7 : inpin7,
        10 : inpin10
    }
    return inputs_dict_connectivity_ids[pin]

def _get_output_spec_connectivity_ids(pin):
    outpin0 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], document = """""")
    outpin1 = _PinSpecification(name = "elemental_scoping", type_names = ["scoping"], document = """same as the input scoping but with ids dupplicated to havve the same size as nodal output scoping""")
    outputs_dict_connectivity_ids = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_connectivity_ids[pin]

class _InputSpecConnectivityIds(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh_scoping = _Input(_get_input_spec_connectivity_ids(1), 1, op, -1) 
        self.mesh = _Input(_get_input_spec_connectivity_ids(7), 7, op, -1) 
        self.take_mid_nodes = _Input(_get_input_spec_connectivity_ids(10), 10, op, -1) 

class _OutputSpecConnectivityIds(_Outputs):
    def __init__(self, op: _Operator):
        self.mesh_scoping = _Output(_get_output_spec_connectivity_ids(0), 0, op) 
        self.elemental_scoping = _Output(_get_output_spec_connectivity_ids(1), 1, op) 

class _ConnectivityIds(_Operator):
    def __init__(self):
         super().__init__("scoping::connectivity_ids")
         self._name = "scoping::connectivity_ids"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecConnectivityIds(self._op)
         self.outputs = _OutputSpecConnectivityIds(self._op)

def connectivity_ids():
    """Operator's description:
Internal name is "scoping::connectivity_ids"
Scripting name is "connectivity_ids"

This operator can be instantiated in both following ways:
- using dpf.Operator("scoping::connectivity_ids")
- using dpf.operators.scoping.connectivity_ids()

Input list: 
   1: mesh_scoping (Elemental scoping)
   7: mesh (the support of the scoping is expected if there is no mesh in input)
   10: take_mid_nodes (default is true)
Output list: 
   0: mesh_scoping 
   1: elemental_scoping (same as the input scoping but with ids dupplicated to havve the same size as nodal output scoping)
"""
    return _ConnectivityIds()

#internal name: GetNodeScopingFromMesh
#scripting name: nodal_from_mesh
def _get_input_spec_nodal_from_mesh(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inputs_dict_nodal_from_mesh = { 
        0 : inpin0
    }
    return inputs_dict_nodal_from_mesh[pin]

def _get_output_spec_nodal_from_mesh(pin):
    outpin0 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], document = """""")
    outputs_dict_nodal_from_mesh = { 
        0 : outpin0
    }
    return outputs_dict_nodal_from_mesh[pin]

class _InputSpecNodalFromMesh(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_nodal_from_mesh(0), 0, op, -1) 

class _OutputSpecNodalFromMesh(_Outputs):
    def __init__(self, op: _Operator):
        self.mesh_scoping = _Output(_get_output_spec_nodal_from_mesh(0), 0, op) 

class _NodalFromMesh(_Operator):
    def __init__(self):
         super().__init__("GetNodeScopingFromMesh")
         self._name = "GetNodeScopingFromMesh"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalFromMesh(self._op)
         self.outputs = _OutputSpecNodalFromMesh(self._op)

def nodal_from_mesh():
    """Operator's description:
Internal name is "GetNodeScopingFromMesh"
Scripting name is "nodal_from_mesh"

This operator can be instantiated in both following ways:
- using dpf.Operator("GetNodeScopingFromMesh")
- using dpf.operators.scoping.nodal_from_mesh()

Input list: 
   0: mesh 
Output list: 
   0: mesh_scoping 
"""
    return _NodalFromMesh()

#internal name: rescope_fc
#scripting name: change_fc
def _get_input_spec_change_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "scopings_container", type_names = ["scopings_container"], optional = False, document = """""")
    inputs_dict_change_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_change_fc[pin]

def _get_output_spec_change_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_change_fc = { 
        0 : outpin0
    }
    return outputs_dict_change_fc[pin]

class _InputSpecChangeFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_change_fc(0), 0, op, -1) 
        self.scopings_container = _Input(_get_input_spec_change_fc(1), 1, op, -1) 

class _OutputSpecChangeFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_change_fc(0), 0, op) 

class _ChangeFc(_Operator):
    def __init__(self):
         super().__init__("rescope_fc")
         self._name = "rescope_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecChangeFc(self._op)
         self.outputs = _OutputSpecChangeFc(self._op)

def change_fc():
    """Operator's description:
Internal name is "rescope_fc"
Scripting name is "change_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("rescope_fc")
- using dpf.operators.scoping.change_fc()

Input list: 
   0: fields_container 
   1: scopings_container 
Output list: 
   0: fields_container 
"""
    return _ChangeFc()

#internal name: core::scoping::high_pass
#scripting name: scoping.high_pass
def _get_input_spec_high_pass(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "threshold", type_names = ["double","field"], optional = False, document = """a threshold scalar or a field containing one value is expected""")
    inputs_dict_high_pass = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_high_pass[pin]

def _get_output_spec_high_pass(pin):
    outpin0 = _PinSpecification(name = "scoping", type_names = ["scoping"], document = """""")
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
        self.scoping = _Output(_get_output_spec_high_pass(0), 0, op) 

class _HighPass(_Operator):
    def __init__(self):
         super().__init__("core::scoping::high_pass")
         self._name = "core::scoping::high_pass"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecHighPass(self._op)
         self.outputs = _OutputSpecHighPass(self._op)

def high_pass():
    """Operator's description:
Internal name is "core::scoping::high_pass"
Scripting name is "scoping.high_pass"

This operator can be instantiated in both following ways:
- using dpf.Operator("core::scoping::high_pass")
- using dpf.operators.filter.scoping.high_pass()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: threshold (a threshold scalar or a field containing one value is expected)
Output list: 
   0: scoping 
"""
    return _HighPass()

#internal name: core::scoping::band_pass
#scripting name: scoping.band_pass
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
    outpin0 = _PinSpecification(name = "scoping", type_names = ["scoping"], document = """""")
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
        self.scoping = _Output(_get_output_spec_band_pass(0), 0, op) 

class _BandPass(_Operator):
    def __init__(self):
         super().__init__("core::scoping::band_pass")
         self._name = "core::scoping::band_pass"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecBandPass(self._op)
         self.outputs = _OutputSpecBandPass(self._op)

def band_pass():
    """Operator's description:
Internal name is "core::scoping::band_pass"
Scripting name is "scoping.band_pass"

This operator can be instantiated in both following ways:
- using dpf.Operator("core::scoping::band_pass")
- using dpf.operators.filter.scoping.band_pass()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: min_threshold (a min threshold scalar or a field containing one value is expected)
   2: max_threshold (a max threshold scalar or a field containing one value is expected)
Output list: 
   0: scoping 
"""
    return _BandPass()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "scoping" category
"""

#internal name: MeshScopingProvider
#scripting name: from_mesh
def _get_input_spec_from_mesh(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """if nothing the operator returns the nodes scoping, possible locations are: Nodal or Elemental""")
    inputs_dict_from_mesh = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_from_mesh[pin]

def _get_output_spec_from_mesh(pin):
    outpin0 = _PinSpecification(name = "scoping", type_names = ["scoping"], document = """""")
    outputs_dict_from_mesh = { 
        0 : outpin0
    }
    return outputs_dict_from_mesh[pin]

class _InputSpecFromMesh(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_from_mesh(0), 0, op, -1) 
        self.requested_location = _Input(_get_input_spec_from_mesh(1), 1, op, -1) 

class _OutputSpecFromMesh(_Outputs):
    def __init__(self, op: _Operator):
        self.scoping = _Output(_get_output_spec_from_mesh(0), 0, op) 

class _FromMesh(_Operator):
    def __init__(self):
         super().__init__("MeshScopingProvider")
         self._name = "MeshScopingProvider"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecFromMesh(self._op)
         self.outputs = _OutputSpecFromMesh(self._op)

def from_mesh():
    """Operator's description:
Internal name is "MeshScopingProvider"
Scripting name is "from_mesh"

This operator can be instantiated in both following ways:
- using dpf.Operator("MeshScopingProvider")
- using dpf.operators.scoping.from_mesh()

Input list: 
   0: mesh 
   1: requested_location (if nothing the operator returns the nodes scoping, possible locations are: Nodal or Elemental)
Output list: 
   0: scoping 
"""
    return _FromMesh()

