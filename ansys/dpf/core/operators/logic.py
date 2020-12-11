from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "logic" category
"""

#internal name: compare::mesh
#scripting name: identical_meshes
def _get_input_spec_identical_meshes(pin = None):
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
    if pin is None:
        return inputs_dict_identical_meshes
    else:
        return inputs_dict_identical_meshes[pin]

def _get_output_spec_identical_meshes(pin = None):
    outpin0 = _PinSpecification(name = "are_identical", type_names = ["bool"], document = """""")
    outputs_dict_identical_meshes = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_identical_meshes
    else:
        return outputs_dict_identical_meshes[pin]

class _InputSpecIdenticalMeshes(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_identical_meshes(), op)
        self.meshA = Input(_get_input_spec_identical_meshes(0), 0, op, -1) 
        super().__init__(_get_input_spec_identical_meshes(), op)
        self.meshB = Input(_get_input_spec_identical_meshes(1), 1, op, -1) 
        super().__init__(_get_input_spec_identical_meshes(), op)
        self.small_value = Input(_get_input_spec_identical_meshes(2), 2, op, -1) 
        super().__init__(_get_input_spec_identical_meshes(), op)
        self.tolerence = Input(_get_input_spec_identical_meshes(3), 3, op, -1) 

class _OutputSpecIdenticalMeshes(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_identical_meshes(), op)
        self.are_identical = Output(_get_output_spec_identical_meshes(0), 0, op) 

class _IdenticalMeshes(_Operator):
    """Operator's description:
    Internal name is "compare::mesh"
    Scripting name is "identical_meshes"

    Description: Take two meshes and compare them.

    Input list: 
       0: meshA 
       1: meshB 
       2: small_value (define what is a small value for numeric comparison.)
       3: tolerence (define the relative tolerence ceil for numeric comparison.)

    Output list: 
       0: are_identical 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("compare::mesh")
    >>> op_way2 = core.operators.logic.identical_meshes()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("compare::mesh")
        self.inputs = _InputSpecIdenticalMeshes(self)
        self.outputs = _OutputSpecIdenticalMeshes(self)

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

def identical_meshes():
    """Operator's description:
    Internal name is "compare::mesh"
    Scripting name is "identical_meshes"

    Description: Take two meshes and compare them.

    Input list: 
       0: meshA 
       1: meshB 
       2: small_value (define what is a small value for numeric comparison.)
       3: tolerence (define the relative tolerence ceil for numeric comparison.)

    Output list: 
       0: are_identical 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("compare::mesh")
    >>> op_way2 = core.operators.logic.identical_meshes()
    """
    return _IdenticalMeshes()

#internal name: component_selector_fc
#scripting name: component_selector_fc
def _get_input_spec_component_selector_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "component_number", type_names = ["int32"], optional = False, document = """""")
    inputs_dict_component_selector_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_component_selector_fc
    else:
        return inputs_dict_component_selector_fc[pin]

def _get_output_spec_component_selector_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_component_selector_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_component_selector_fc
    else:
        return outputs_dict_component_selector_fc[pin]

class _InputSpecComponentSelectorFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_component_selector_fc(), op)
        self.fields_container = Input(_get_input_spec_component_selector_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_component_selector_fc(), op)
        self.component_number = Input(_get_input_spec_component_selector_fc(1), 1, op, -1) 

class _OutputSpecComponentSelectorFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_component_selector_fc(), op)
        self.fields_container = Output(_get_output_spec_component_selector_fc(0), 0, op) 

class _ComponentSelectorFc(_Operator):
    """Operator's description:
    Internal name is "component_selector_fc"
    Scripting name is "component_selector_fc"

    Description: Create a scalar fields container based on the selected component for each field.

    Input list: 
       0: fields_container 
       1: component_number 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("component_selector_fc")
    >>> op_way2 = core.operators.logic.component_selector_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("component_selector_fc")
        self.inputs = _InputSpecComponentSelectorFc(self)
        self.outputs = _OutputSpecComponentSelectorFc(self)

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

def component_selector_fc():
    """Operator's description:
    Internal name is "component_selector_fc"
    Scripting name is "component_selector_fc"

    Description: Create a scalar fields container based on the selected component for each field.

    Input list: 
       0: fields_container 
       1: component_number 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("component_selector_fc")
    >>> op_way2 = core.operators.logic.component_selector_fc()
    """
    return _ComponentSelectorFc()

#internal name: component_selector
#scripting name: component_selector
def _get_input_spec_component_selector(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "component_number", type_names = ["int32"], optional = False, document = """one or several component index that will be extracted from the initial field.""")
    inpin2 = _PinSpecification(name = "default_value", type_names = ["double"], optional = True, document = """set a default value for components that do not exist""")
    inputs_dict_component_selector = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    if pin is None:
        return inputs_dict_component_selector
    else:
        return inputs_dict_component_selector[pin]

def _get_output_spec_component_selector(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_component_selector = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_component_selector
    else:
        return outputs_dict_component_selector[pin]

class _InputSpecComponentSelector(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_component_selector(), op)
        self.field = Input(_get_input_spec_component_selector(0), 0, op, -1) 
        super().__init__(_get_input_spec_component_selector(), op)
        self.component_number = Input(_get_input_spec_component_selector(1), 1, op, -1) 
        super().__init__(_get_input_spec_component_selector(), op)
        self.default_value = Input(_get_input_spec_component_selector(2), 2, op, -1) 

class _OutputSpecComponentSelector(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_component_selector(), op)
        self.field = Output(_get_output_spec_component_selector(0), 0, op) 

class _ComponentSelector(_Operator):
    """Operator's description:
    Internal name is "component_selector"
    Scripting name is "component_selector"

    Description: Create a scalar/vector field based on the selected component.

    Input list: 
       0: field 
       1: component_number (one or several component index that will be extracted from the initial field.)
       2: default_value (set a default value for components that do not exist)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("component_selector")
    >>> op_way2 = core.operators.logic.component_selector()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("component_selector")
        self.inputs = _InputSpecComponentSelector(self)
        self.outputs = _OutputSpecComponentSelector(self)

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

def component_selector():
    """Operator's description:
    Internal name is "component_selector"
    Scripting name is "component_selector"

    Description: Create a scalar/vector field based on the selected component.

    Input list: 
       0: field 
       1: component_number (one or several component index that will be extracted from the initial field.)
       2: default_value (set a default value for components that do not exist)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("component_selector")
    >>> op_way2 = core.operators.logic.component_selector()
    """
    return _ComponentSelector()

#internal name: compare::property_field
#scripting name: identical_property_fields
def _get_input_spec_identical_property_fields(pin = None):
    inpin0 = _PinSpecification(name = "property_fieldA", type_names = ["meshed_region"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "property_fieldB", type_names = ["meshed_region"], optional = False, document = """""")
    inputs_dict_identical_property_fields = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_identical_property_fields
    else:
        return inputs_dict_identical_property_fields[pin]

def _get_output_spec_identical_property_fields(pin = None):
    outpin0 = _PinSpecification(name = "are_identical", type_names = ["bool"], document = """""")
    outpin1 = _PinSpecification(name = "informations", type_names = ["string"], document = """""")
    outputs_dict_identical_property_fields = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_identical_property_fields
    else:
        return outputs_dict_identical_property_fields[pin]

class _InputSpecIdenticalPropertyFields(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_identical_property_fields(), op)
        self.property_fieldA = Input(_get_input_spec_identical_property_fields(0), 0, op, -1) 
        super().__init__(_get_input_spec_identical_property_fields(), op)
        self.property_fieldB = Input(_get_input_spec_identical_property_fields(1), 1, op, -1) 

class _OutputSpecIdenticalPropertyFields(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_identical_property_fields(), op)
        self.are_identical = Output(_get_output_spec_identical_property_fields(0), 0, op) 
        super().__init__(_get_output_spec_identical_property_fields(), op)
        self.informations = Output(_get_output_spec_identical_property_fields(1), 1, op) 

class _IdenticalPropertyFields(_Operator):
    """Operator's description:
    Internal name is "compare::property_field"
    Scripting name is "identical_property_fields"

    Description: Take two property fields and compare them.

    Input list: 
       0: property_fieldA 
       1: property_fieldB 

    Output list: 
       0: are_identical 
       1: informations 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("compare::property_field")
    >>> op_way2 = core.operators.logic.identical_property_fields()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("compare::property_field")
        self.inputs = _InputSpecIdenticalPropertyFields(self)
        self.outputs = _OutputSpecIdenticalPropertyFields(self)

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

def identical_property_fields():
    """Operator's description:
    Internal name is "compare::property_field"
    Scripting name is "identical_property_fields"

    Description: Take two property fields and compare them.

    Input list: 
       0: property_fieldA 
       1: property_fieldB 

    Output list: 
       0: are_identical 
       1: informations 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("compare::property_field")
    >>> op_way2 = core.operators.logic.identical_property_fields()
    """
    return _IdenticalPropertyFields()

#internal name: merge::fields_container_label
#scripting name: merge_fields_by_label
def _get_input_spec_merge_fields_by_label(pin = None):
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
    if pin is None:
        return inputs_dict_merge_fields_by_label
    else:
        return inputs_dict_merge_fields_by_label[pin]

def _get_output_spec_merge_fields_by_label(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outpin1 = _PinSpecification(name = "merged_field_support", type_names = ["abstract_field_support"], document = """""")
    outputs_dict_merge_fields_by_label = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_merge_fields_by_label
    else:
        return outputs_dict_merge_fields_by_label[pin]

class _InputSpecMergeFieldsByLabel(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_merge_fields_by_label(), op)
        self.fields_container = Input(_get_input_spec_merge_fields_by_label(0), 0, op, -1) 
        super().__init__(_get_input_spec_merge_fields_by_label(), op)
        self.label = Input(_get_input_spec_merge_fields_by_label(1), 1, op, -1) 
        super().__init__(_get_input_spec_merge_fields_by_label(), op)
        self.merged_field_support = Input(_get_input_spec_merge_fields_by_label(2), 2, op, -1) 
        super().__init__(_get_input_spec_merge_fields_by_label(), op)
        self.sumMerge = Input(_get_input_spec_merge_fields_by_label(3), 3, op, -1) 

class _OutputSpecMergeFieldsByLabel(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_merge_fields_by_label(), op)
        self.fields_container = Output(_get_output_spec_merge_fields_by_label(0), 0, op) 
        super().__init__(_get_output_spec_merge_fields_by_label(), op)
        self.merged_field_support = Output(_get_output_spec_merge_fields_by_label(1), 1, op) 

class _MergeFieldsByLabel(_Operator):
    """Operator's description:
    Internal name is "merge::fields_container_label"
    Scripting name is "merge_fields_by_label"

    Description: Take a fields container and merge its fields that share the same label value.

    Input list: 
       0: fields_container 
       1: label (Label identifier that should be merged.)
       2: merged_field_support (The FieldsContainer's support that has already been merged.)
       3: sumMerge (Default is false. If true redundant quantities are summed instead of being ignored.)

    Output list: 
       0: fields_container 
       1: merged_field_support 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("merge::fields_container_label")
    >>> op_way2 = core.operators.logic.merge_fields_by_label()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("merge::fields_container_label")
        self.inputs = _InputSpecMergeFieldsByLabel(self)
        self.outputs = _OutputSpecMergeFieldsByLabel(self)

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

def merge_fields_by_label():
    """Operator's description:
    Internal name is "merge::fields_container_label"
    Scripting name is "merge_fields_by_label"

    Description: Take a fields container and merge its fields that share the same label value.

    Input list: 
       0: fields_container 
       1: label (Label identifier that should be merged.)
       2: merged_field_support (The FieldsContainer's support that has already been merged.)
       3: sumMerge (Default is false. If true redundant quantities are summed instead of being ignored.)

    Output list: 
       0: fields_container 
       1: merged_field_support 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("merge::fields_container_label")
    >>> op_way2 = core.operators.logic.merge_fields_by_label()
    """
    return _MergeFieldsByLabel()

from . import merge #merge::solid_shell_fields

#internal name: AreFieldsIdentical
#scripting name: identical_fields
def _get_input_spec_identical_fields(pin = None):
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
    if pin is None:
        return inputs_dict_identical_fields
    else:
        return inputs_dict_identical_fields[pin]

def _get_output_spec_identical_fields(pin = None):
    outpin0 = _PinSpecification(name = "boolean", type_names = ["bool"], document = """bool (true if identical...)""")
    outpin1 = _PinSpecification(name = "message", type_names = ["string"], document = """""")
    outputs_dict_identical_fields = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_identical_fields
    else:
        return outputs_dict_identical_fields[pin]

class _InputSpecIdenticalFields(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_identical_fields(), op)
        self.fieldA = Input(_get_input_spec_identical_fields(0), 0, op, -1) 
        super().__init__(_get_input_spec_identical_fields(), op)
        self.fieldB = Input(_get_input_spec_identical_fields(1), 1, op, -1) 
        super().__init__(_get_input_spec_identical_fields(), op)
        self.double_value = Input(_get_input_spec_identical_fields(2), 2, op, -1) 
        super().__init__(_get_input_spec_identical_fields(), op)
        self.double_tolerance = Input(_get_input_spec_identical_fields(3), 3, op, -1) 

class _OutputSpecIdenticalFields(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_identical_fields(), op)
        self.boolean = Output(_get_output_spec_identical_fields(0), 0, op) 
        super().__init__(_get_output_spec_identical_fields(), op)
        self.message = Output(_get_output_spec_identical_fields(1), 1, op) 

class _IdenticalFields(_Operator):
    """Operator's description:
    Internal name is "AreFieldsIdentical"
    Scripting name is "identical_fields"

    Description: Check if two fields are identical.

    Input list: 
       0: fieldA 
       1: fieldB 
       2: double_value (Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).)
       3: double_tolerance (Double relative tolerance.Maximum tolerance gap between to compared values : values within relative tolerance are considered identical(v1 - v2) / v2 < relativeTol(default is 0.001).)

    Output list: 
       0: boolean (bool (true if identical...))
       1: message 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("AreFieldsIdentical")
    >>> op_way2 = core.operators.logic.identical_fields()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("AreFieldsIdentical")
        self.inputs = _InputSpecIdenticalFields(self)
        self.outputs = _OutputSpecIdenticalFields(self)

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

def identical_fields():
    """Operator's description:
    Internal name is "AreFieldsIdentical"
    Scripting name is "identical_fields"

    Description: Check if two fields are identical.

    Input list: 
       0: fieldA 
       1: fieldB 
       2: double_value (Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).)
       3: double_tolerance (Double relative tolerance.Maximum tolerance gap between to compared values : values within relative tolerance are considered identical(v1 - v2) / v2 < relativeTol(default is 0.001).)

    Output list: 
       0: boolean (bool (true if identical...))
       1: message 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("AreFieldsIdentical")
    >>> op_way2 = core.operators.logic.identical_fields()
    """
    return _IdenticalFields()

#internal name: Are_fields_included
#scripting name: included_fields
def _get_input_spec_included_fields(pin = None):
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
    if pin is None:
        return inputs_dict_included_fields
    else:
        return inputs_dict_included_fields[pin]

def _get_output_spec_included_fields(pin = None):
    outpin0 = _PinSpecification(name = "included", type_names = ["bool"], document = """bool (true if belongs...)""")
    outpin1 = _PinSpecification(name = "message", type_names = ["string"], document = """""")
    outputs_dict_included_fields = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_included_fields
    else:
        return outputs_dict_included_fields[pin]

class _InputSpecIncludedFields(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_included_fields(), op)
        self.fieldA = Input(_get_input_spec_included_fields(0), 0, op, -1) 
        super().__init__(_get_input_spec_included_fields(), op)
        self.fieldB = Input(_get_input_spec_included_fields(1), 1, op, -1) 
        super().__init__(_get_input_spec_included_fields(), op)
        self.double_value = Input(_get_input_spec_included_fields(2), 2, op, -1) 
        super().__init__(_get_input_spec_included_fields(), op)
        self.double_tolerance = Input(_get_input_spec_included_fields(3), 3, op, -1) 

class _OutputSpecIncludedFields(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_included_fields(), op)
        self.included = Output(_get_output_spec_included_fields(0), 0, op) 
        super().__init__(_get_output_spec_included_fields(), op)
        self.message = Output(_get_output_spec_included_fields(1), 1, op) 

class _IncludedFields(_Operator):
    """Operator's description:
    Internal name is "Are_fields_included"
    Scripting name is "included_fields"

    Description: Check if one field belongs to another.

    Input list: 
       0: fieldA 
       1: fieldB 
       2: double_value (Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).)
       3: double_tolerance (Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).)

    Output list: 
       0: included (bool (true if belongs...))
       1: message 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("Are_fields_included")
    >>> op_way2 = core.operators.logic.included_fields()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("Are_fields_included")
        self.inputs = _InputSpecIncludedFields(self)
        self.outputs = _OutputSpecIncludedFields(self)

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

def included_fields():
    """Operator's description:
    Internal name is "Are_fields_included"
    Scripting name is "included_fields"

    Description: Check if one field belongs to another.

    Input list: 
       0: fieldA 
       1: fieldB 
       2: double_value (Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).)
       3: double_tolerance (Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).)

    Output list: 
       0: included (bool (true if belongs...))
       1: message 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("Are_fields_included")
    >>> op_way2 = core.operators.logic.included_fields()
    """
    return _IncludedFields()

#internal name: AreFieldsIdentical_fc
#scripting name: identical_fc
def _get_input_spec_identical_fc(pin = None):
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
    if pin is None:
        return inputs_dict_identical_fc
    else:
        return inputs_dict_identical_fc[pin]

def _get_output_spec_identical_fc(pin = None):
    outpin0 = _PinSpecification(name = "boolean", type_names = ["bool"], document = """bool (true if identical...)""")
    outputs_dict_identical_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_identical_fc
    else:
        return outputs_dict_identical_fc[pin]

class _InputSpecIdenticalFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_identical_fc(), op)
        self.fields_containerA = Input(_get_input_spec_identical_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_identical_fc(), op)
        self.fields_containerB = Input(_get_input_spec_identical_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_identical_fc(), op)
        self.tolerance = Input(_get_input_spec_identical_fc(2), 2, op, -1) 
        super().__init__(_get_input_spec_identical_fc(), op)
        self.small_value = Input(_get_input_spec_identical_fc(3), 3, op, -1) 

class _OutputSpecIdenticalFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_identical_fc(), op)
        self.boolean = Output(_get_output_spec_identical_fc(0), 0, op) 

class _IdenticalFc(_Operator):
    """Operator's description:
    Internal name is "AreFieldsIdentical_fc"
    Scripting name is "identical_fc"

    Description: Check if two fields container are identical.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 
       2: tolerance (Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).)
       3: small_value (Double positive small value.Smallest value which will be considered during the comparison step : all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).)

    Output list: 
       0: boolean (bool (true if identical...))

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("AreFieldsIdentical_fc")
    >>> op_way2 = core.operators.logic.identical_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("AreFieldsIdentical_fc")
        self.inputs = _InputSpecIdenticalFc(self)
        self.outputs = _OutputSpecIdenticalFc(self)

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

def identical_fc():
    """Operator's description:
    Internal name is "AreFieldsIdentical_fc"
    Scripting name is "identical_fc"

    Description: Check if two fields container are identical.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 
       2: tolerance (Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).)
       3: small_value (Double positive small value.Smallest value which will be considered during the comparison step : all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).)

    Output list: 
       0: boolean (bool (true if identical...))

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("AreFieldsIdentical_fc")
    >>> op_way2 = core.operators.logic.identical_fc()
    """
    return _IdenticalFc()

#internal name: enrich_materials
#scripting name: enrich_materials
def _get_input_spec_enrich_materials(pin = None):
    inpin1 = _PinSpecification(name = "streams", type_names = ["streams_container"], optional = False, document = """""")
    inputs_dict_enrich_materials = { 
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_enrich_materials
    else:
        return inputs_dict_enrich_materials[pin]

def _get_output_spec_enrich_materials(pin = None):
    outpin0 = _PinSpecification(name = "MaterialContainer", type_names = ["bool"], document = """""")
    outputs_dict_enrich_materials = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_enrich_materials
    else:
        return outputs_dict_enrich_materials[pin]

class _InputSpecEnrichMaterials(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_enrich_materials(), op)
        self.streams = Input(_get_input_spec_enrich_materials(1), 1, op, -1) 

class _OutputSpecEnrichMaterials(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_enrich_materials(), op)
        self.MaterialContainer = Output(_get_output_spec_enrich_materials(0), 0, op) 

class _EnrichMaterials(_Operator):
    """Operator's description:
    Internal name is "enrich_materials"
    Scripting name is "enrich_materials"

    Description: Take a MaterialContainer and a stream and enrich the MaterialContainer using stream data.

    Input list: 
       1: streams 

    Output list: 
       0: MaterialContainer 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("enrich_materials")
    >>> op_way2 = core.operators.logic.enrich_materials()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("enrich_materials")
        self.inputs = _InputSpecEnrichMaterials(self)
        self.outputs = _OutputSpecEnrichMaterials(self)

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

def enrich_materials():
    """Operator's description:
    Internal name is "enrich_materials"
    Scripting name is "enrich_materials"

    Description: Take a MaterialContainer and a stream and enrich the MaterialContainer using stream data.

    Input list: 
       1: streams 

    Output list: 
       0: MaterialContainer 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("enrich_materials")
    >>> op_way2 = core.operators.logic.enrich_materials()
    """
    return _EnrichMaterials()

#internal name: loop_over_workflow_int_vec
#scripting name: loop_over_workflow_int_vec
def _get_input_spec_loop_over_workflow_int_vec(pin = None):
    inpin1 = _PinSpecification(name = "input_name", type_names = ["string"], optional = False, document = """name of the workflow's input pin to loop over""")
    inputs_dict_loop_over_workflow_int_vec = { 
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_loop_over_workflow_int_vec
    else:
        return inputs_dict_loop_over_workflow_int_vec[pin]

def _get_output_spec_loop_over_workflow_int_vec(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_loop_over_workflow_int_vec = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_loop_over_workflow_int_vec
    else:
        return outputs_dict_loop_over_workflow_int_vec[pin]

class _InputSpecLoopOverWorkflowIntVec(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_loop_over_workflow_int_vec(), op)
        self.input_name = Input(_get_input_spec_loop_over_workflow_int_vec(1), 1, op, -1) 

class _OutputSpecLoopOverWorkflowIntVec(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_loop_over_workflow_int_vec(), op)
        self.fields_container = Output(_get_output_spec_loop_over_workflow_int_vec(0), 0, op) 

class _LoopOverWorkflowIntVec(_Operator):
    """Operator's description:
    Internal name is "loop_over_workflow_int_vec"
    Scripting name is "loop_over_workflow_int_vec"

    Description: Loop over the number of ellipsis pin (from pin 3) and for each of these inputs connect the input to the workflow, evaluate the workfow and store the results in a fields container

    Input list: 
       1: input_name (name of the workflow's input pin to loop over)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("loop_over_workflow_int_vec")
    >>> op_way2 = core.operators.logic.loop_over_workflow_int_vec()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("loop_over_workflow_int_vec")
        self.inputs = _InputSpecLoopOverWorkflowIntVec(self)
        self.outputs = _OutputSpecLoopOverWorkflowIntVec(self)

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

def loop_over_workflow_int_vec():
    """Operator's description:
    Internal name is "loop_over_workflow_int_vec"
    Scripting name is "loop_over_workflow_int_vec"

    Description: Loop over the number of ellipsis pin (from pin 3) and for each of these inputs connect the input to the workflow, evaluate the workfow and store the results in a fields container

    Input list: 
       1: input_name (name of the workflow's input pin to loop over)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("loop_over_workflow_int_vec")
    >>> op_way2 = core.operators.logic.loop_over_workflow_int_vec()
    """
    return _LoopOverWorkflowIntVec()

