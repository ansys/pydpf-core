from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "logic" category
"""

#internal name: compare::mesh
#scripting name: identical_meshes
def _get_input_spec_identical_meshes(pin):
    inpin0 = _PinSpecification(name = "meshA", type_names = ["meshed_region"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "meshB", type_names = ["meshed_region"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "small_value", type_names = ["double"], optional = False, document = """define what is a small value for numeric comparison.""")
    inpin3 = _PinSpecification(name = "tolerence", type_names = ["double"], optional = False, document = """define the relative tolerence ceil for numeric comparison.""")
    inputs_dict_identical_meshes = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    return inputs_dict_identical_meshes[pin]

def _get_output_spec_identical_meshes(pin):
    outpin0 = _PinSpecification(name = "are_identical", type_names = ["bool"], document = """""")
    outputs_dict_identical_meshes = { 
        0 : outpin0
    }
    return outputs_dict_identical_meshes[pin]

class _InputSpecIdenticalMeshes(_Inputs):
    def __init__(self, op: _Operator):
        self.meshA = _Input(_get_input_spec_identical_meshes(0), 0, op, -1) 
        self.meshB = _Input(_get_input_spec_identical_meshes(1), 1, op, -1) 
        self.small_value = _Input(_get_input_spec_identical_meshes(2), 2, op, -1) 
        self.tolerence = _Input(_get_input_spec_identical_meshes(3), 3, op, -1) 

class _OutputSpecIdenticalMeshes(_Outputs):
    def __init__(self, op: _Operator):
        self.are_identical = _Output(_get_output_spec_identical_meshes(0), 0, op) 

class _IdenticalMeshes(_Operator):
    def __init__(self):
         super().__init__("compare::mesh")
         self._name = "compare::mesh"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecIdenticalMeshes(self._op)
         self.outputs = _OutputSpecIdenticalMeshes(self._op)

def identical_meshes():
    """Operator's description:
Internal name is "compare::mesh"
Scripting name is "identical_meshes"

This operator can be instantiated in both following ways:
- using dpf.Operator("compare::mesh")
- using dpf.operators.logic.identical_meshes()

Input list: 
   0: meshA 
   1: meshB 
   2: small_value (define what is a small value for numeric comparison.)
   3: tolerence (define the relative tolerence ceil for numeric comparison.)
Output list: 
   0: are_identical 
"""
    return _IdenticalMeshes()

#internal name: component_selector_fc
#scripting name: component_selector_fc
def _get_input_spec_component_selector_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "component_number", type_names = ["int32"], optional = False, document = """""")
    inputs_dict_component_selector_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_component_selector_fc[pin]

def _get_output_spec_component_selector_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_component_selector_fc = { 
        0 : outpin0
    }
    return outputs_dict_component_selector_fc[pin]

class _InputSpecComponentSelectorFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_component_selector_fc(0), 0, op, -1) 
        self.component_number = _Input(_get_input_spec_component_selector_fc(1), 1, op, -1) 

class _OutputSpecComponentSelectorFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_component_selector_fc(0), 0, op) 

class _ComponentSelectorFc(_Operator):
    def __init__(self):
         super().__init__("component_selector_fc")
         self._name = "component_selector_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecComponentSelectorFc(self._op)
         self.outputs = _OutputSpecComponentSelectorFc(self._op)

def component_selector_fc():
    """Operator's description:
Internal name is "component_selector_fc"
Scripting name is "component_selector_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("component_selector_fc")
- using dpf.operators.logic.component_selector_fc()

Input list: 
   0: fields_container 
   1: component_number 
Output list: 
   0: fields_container 
"""
    return _ComponentSelectorFc()

#internal name: component_selector
#scripting name: component_selector
def _get_input_spec_component_selector(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "component_number", type_names = ["int32"], optional = False, document = """one or several component index that will be extracted from the initial field.""")
    inpin2 = _PinSpecification(name = "default_value", type_names = ["double"], optional = True, document = """set a default value for components that do not exist""")
    inputs_dict_component_selector = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_component_selector[pin]

def _get_output_spec_component_selector(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_component_selector = { 
        0 : outpin0
    }
    return outputs_dict_component_selector[pin]

class _InputSpecComponentSelector(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_component_selector(0), 0, op, -1) 
        self.component_number = _Input(_get_input_spec_component_selector(1), 1, op, -1) 
        self.default_value = _Input(_get_input_spec_component_selector(2), 2, op, -1) 

class _OutputSpecComponentSelector(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_component_selector(0), 0, op) 

class _ComponentSelector(_Operator):
    def __init__(self):
         super().__init__("component_selector")
         self._name = "component_selector"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecComponentSelector(self._op)
         self.outputs = _OutputSpecComponentSelector(self._op)

def component_selector():
    """Operator's description:
Internal name is "component_selector"
Scripting name is "component_selector"

This operator can be instantiated in both following ways:
- using dpf.Operator("component_selector")
- using dpf.operators.logic.component_selector()

Input list: 
   0: field 
   1: component_number (one or several component index that will be extracted from the initial field.)
   2: default_value (set a default value for components that do not exist)
Output list: 
   0: field 
"""
    return _ComponentSelector()

#internal name: compare::property_field
#scripting name: identical_property_fields
def _get_input_spec_identical_property_fields(pin):
    inpin0 = _PinSpecification(name = "property_fieldA", type_names = ["meshed_region"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "property_fieldB", type_names = ["meshed_region"], optional = False, document = """""")
    inputs_dict_identical_property_fields = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_identical_property_fields[pin]

def _get_output_spec_identical_property_fields(pin):
    outpin0 = _PinSpecification(name = "are_identical", type_names = ["bool"], document = """""")
    outpin1 = _PinSpecification(name = "informations", type_names = ["string"], document = """""")
    outputs_dict_identical_property_fields = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_identical_property_fields[pin]

class _InputSpecIdenticalPropertyFields(_Inputs):
    def __init__(self, op: _Operator):
        self.property_fieldA = _Input(_get_input_spec_identical_property_fields(0), 0, op, -1) 
        self.property_fieldB = _Input(_get_input_spec_identical_property_fields(1), 1, op, -1) 

class _OutputSpecIdenticalPropertyFields(_Outputs):
    def __init__(self, op: _Operator):
        self.are_identical = _Output(_get_output_spec_identical_property_fields(0), 0, op) 
        self.informations = _Output(_get_output_spec_identical_property_fields(1), 1, op) 

class _IdenticalPropertyFields(_Operator):
    def __init__(self):
         super().__init__("compare::property_field")
         self._name = "compare::property_field"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecIdenticalPropertyFields(self._op)
         self.outputs = _OutputSpecIdenticalPropertyFields(self._op)

def identical_property_fields():
    """Operator's description:
Internal name is "compare::property_field"
Scripting name is "identical_property_fields"

This operator can be instantiated in both following ways:
- using dpf.Operator("compare::property_field")
- using dpf.operators.logic.identical_property_fields()

Input list: 
   0: property_fieldA 
   1: property_fieldB 
Output list: 
   0: are_identical 
   1: informations 
"""
    return _IdenticalPropertyFields()

#internal name: merge::fields_container_label
#scripting name: merge_fields_by_label
def _get_input_spec_merge_fields_by_label(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "label", type_names = ["string"], optional = False, document = """Label identifier that should be merged.""")
    inpin2 = _PinSpecification(name = "merged_field_support", type_names = ["abstract_field_support"], optional = True, document = """The FieldsContainer's support that has already been merged.""")
    inpin3 = _PinSpecification(name = "sumMerge", type_names = ["bool"], optional = True, document = """Default is false. If true redundant quantities are summed instead of being ignored.""")
    inputs_dict_merge_fields_by_label = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    return inputs_dict_merge_fields_by_label[pin]

def _get_output_spec_merge_fields_by_label(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outpin1 = _PinSpecification(name = "merged_field_support", type_names = ["abstract_field_support"], document = """""")
    outputs_dict_merge_fields_by_label = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_merge_fields_by_label[pin]

class _InputSpecMergeFieldsByLabel(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_merge_fields_by_label(0), 0, op, -1) 
        self.label = _Input(_get_input_spec_merge_fields_by_label(1), 1, op, -1) 
        self.merged_field_support = _Input(_get_input_spec_merge_fields_by_label(2), 2, op, -1) 
        self.sumMerge = _Input(_get_input_spec_merge_fields_by_label(3), 3, op, -1) 

class _OutputSpecMergeFieldsByLabel(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_merge_fields_by_label(0), 0, op) 
        self.merged_field_support = _Output(_get_output_spec_merge_fields_by_label(1), 1, op) 

class _MergeFieldsByLabel(_Operator):
    def __init__(self):
         super().__init__("merge::fields_container_label")
         self._name = "merge::fields_container_label"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecMergeFieldsByLabel(self._op)
         self.outputs = _OutputSpecMergeFieldsByLabel(self._op)

def merge_fields_by_label():
    """Operator's description:
Internal name is "merge::fields_container_label"
Scripting name is "merge_fields_by_label"

This operator can be instantiated in both following ways:
- using dpf.Operator("merge::fields_container_label")
- using dpf.operators.logic.merge_fields_by_label()

Input list: 
   0: fields_container 
   1: label (Label identifier that should be merged.)
   2: merged_field_support (The FieldsContainer's support that has already been merged.)
   3: sumMerge (Default is false. If true redundant quantities are summed instead of being ignored.)
Output list: 
   0: fields_container 
   1: merged_field_support 
"""
    return _MergeFieldsByLabel()

from . import merge #merge::solid_shell_fields

#internal name: AreFieldsIdentical
#scripting name: identical_fields
def _get_input_spec_identical_fields(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "double_value", type_names = ["double"], optional = True, document = """Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).""")
    inpin3 = _PinSpecification(name = "double_tolerance", type_names = ["double"], optional = True, document = """Double relative tolerance.Maximum tolerance gap between to compared values : values within relative tolerance are considered identical(v1 - v2) / v2 < relativeTol(default is 0.001).""")
    inputs_dict_identical_fields = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    return inputs_dict_identical_fields[pin]

def _get_output_spec_identical_fields(pin):
    outpin0 = _PinSpecification(name = "boolean", type_names = ["bool"], document = """bool (true if identical...)""")
    outpin1 = _PinSpecification(name = "message", type_names = ["string"], document = """""")
    outputs_dict_identical_fields = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_identical_fields[pin]

class _InputSpecIdenticalFields(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_identical_fields(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_identical_fields(1), 1, op, -1) 
        self.double_value = _Input(_get_input_spec_identical_fields(2), 2, op, -1) 
        self.double_tolerance = _Input(_get_input_spec_identical_fields(3), 3, op, -1) 

class _OutputSpecIdenticalFields(_Outputs):
    def __init__(self, op: _Operator):
        self.boolean = _Output(_get_output_spec_identical_fields(0), 0, op) 
        self.message = _Output(_get_output_spec_identical_fields(1), 1, op) 

class _IdenticalFields(_Operator):
    def __init__(self):
         super().__init__("AreFieldsIdentical")
         self._name = "AreFieldsIdentical"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecIdenticalFields(self._op)
         self.outputs = _OutputSpecIdenticalFields(self._op)

def identical_fields():
    """Operator's description:
Internal name is "AreFieldsIdentical"
Scripting name is "identical_fields"

This operator can be instantiated in both following ways:
- using dpf.Operator("AreFieldsIdentical")
- using dpf.operators.logic.identical_fields()

Input list: 
   0: fieldA 
   1: fieldB 
   2: double_value (Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).)
   3: double_tolerance (Double relative tolerance.Maximum tolerance gap between to compared values : values within relative tolerance are considered identical(v1 - v2) / v2 < relativeTol(default is 0.001).)
Output list: 
   0: boolean (bool (true if identical...))
   1: message 
"""
    return _IdenticalFields()

#internal name: Are_fields_included
#scripting name: included_fields
def _get_input_spec_included_fields(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "double_value", type_names = ["double"], optional = False, document = """Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).""")
    inpin3 = _PinSpecification(name = "double_tolerance", type_names = ["double"], optional = True, document = """Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).""")
    inputs_dict_included_fields = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    return inputs_dict_included_fields[pin]

def _get_output_spec_included_fields(pin):
    outpin0 = _PinSpecification(name = "included", type_names = ["bool"], document = """bool (true if belongs...)""")
    outpin1 = _PinSpecification(name = "message", type_names = ["string"], document = """""")
    outputs_dict_included_fields = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_included_fields[pin]

class _InputSpecIncludedFields(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_included_fields(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_included_fields(1), 1, op, -1) 
        self.double_value = _Input(_get_input_spec_included_fields(2), 2, op, -1) 
        self.double_tolerance = _Input(_get_input_spec_included_fields(3), 3, op, -1) 

class _OutputSpecIncludedFields(_Outputs):
    def __init__(self, op: _Operator):
        self.included = _Output(_get_output_spec_included_fields(0), 0, op) 
        self.message = _Output(_get_output_spec_included_fields(1), 1, op) 

class _IncludedFields(_Operator):
    def __init__(self):
         super().__init__("Are_fields_included")
         self._name = "Are_fields_included"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecIncludedFields(self._op)
         self.outputs = _OutputSpecIncludedFields(self._op)

def included_fields():
    """Operator's description:
Internal name is "Are_fields_included"
Scripting name is "included_fields"

This operator can be instantiated in both following ways:
- using dpf.Operator("Are_fields_included")
- using dpf.operators.logic.included_fields()

Input list: 
   0: fieldA 
   1: fieldB 
   2: double_value (Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).)
   3: double_tolerance (Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).)
Output list: 
   0: included (bool (true if belongs...))
   1: message 
"""
    return _IncludedFields()

#internal name: AreFieldsIdentical_fc
#scripting name: identical_fc
def _get_input_spec_identical_fc(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "tolerance", type_names = ["double"], optional = False, document = """Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).""")
    inpin3 = _PinSpecification(name = "small_value", type_names = ["double"], optional = False, document = """Double positive small value.Smallest value which will be considered during the comparison step : all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).""")
    inputs_dict_identical_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    return inputs_dict_identical_fc[pin]

def _get_output_spec_identical_fc(pin):
    outpin0 = _PinSpecification(name = "boolean", type_names = ["bool"], document = """bool (true if identical...)""")
    outputs_dict_identical_fc = { 
        0 : outpin0
    }
    return outputs_dict_identical_fc[pin]

class _InputSpecIdenticalFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_identical_fc(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_identical_fc(1), 1, op, -1) 
        self.tolerance = _Input(_get_input_spec_identical_fc(2), 2, op, -1) 
        self.small_value = _Input(_get_input_spec_identical_fc(3), 3, op, -1) 

class _OutputSpecIdenticalFc(_Outputs):
    def __init__(self, op: _Operator):
        self.boolean = _Output(_get_output_spec_identical_fc(0), 0, op) 

class _IdenticalFc(_Operator):
    def __init__(self):
         super().__init__("AreFieldsIdentical_fc")
         self._name = "AreFieldsIdentical_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecIdenticalFc(self._op)
         self.outputs = _OutputSpecIdenticalFc(self._op)

def identical_fc():
    """Operator's description:
Internal name is "AreFieldsIdentical_fc"
Scripting name is "identical_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("AreFieldsIdentical_fc")
- using dpf.operators.logic.identical_fc()

Input list: 
   0: fields_containerA 
   1: fields_containerB 
   2: tolerance (Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).)
   3: small_value (Double positive small value.Smallest value which will be considered during the comparison step : all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).)
Output list: 
   0: boolean (bool (true if identical...))
"""
    return _IdenticalFc()

