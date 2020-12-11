from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "min_max" category
"""

#internal name: min_max
#scripting name: min_max
def _get_input_spec_min_max(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_min_max = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_min_max
    else:
        return inputs_dict_min_max[pin]

def _get_output_spec_min_max(pin = None):
    outpin0 = _PinSpecification(name = "field_min", type_names = ["field"], document = """""")
    outpin1 = _PinSpecification(name = "field_max", type_names = ["field"], document = """""")
    outputs_dict_min_max = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_min_max
    else:
        return outputs_dict_min_max[pin]

class _InputSpecMinMax(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_min_max(), op)
        self.field = Input(_get_input_spec_min_max(0), 0, op, -1) 

class _OutputSpecMinMax(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_min_max(), op)
        self.field_min = Output(_get_output_spec_min_max(0), 0, op) 
        super().__init__(_get_output_spec_min_max(), op)
        self.field_max = Output(_get_output_spec_min_max(1), 1, op) 

class _MinMax(_Operator):
    """Operator's description:
    Internal name is "min_max"
    Scripting name is "min_max"

    Description: Compute the component-wise minimum (out 0) and maximum (out 1) over a field.

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field_min 
       1: field_max 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max")
    >>> op_way2 = core.operators.min_max.min_max()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("min_max")
        self.inputs = _InputSpecMinMax(self)
        self.outputs = _OutputSpecMinMax(self)

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

def min_max():
    """Operator's description:
    Internal name is "min_max"
    Scripting name is "min_max"

    Description: Compute the component-wise minimum (out 0) and maximum (out 1) over a field.

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field_min 
       1: field_max 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max")
    >>> op_way2 = core.operators.min_max.min_max()
    """
    return _MinMax()

#internal name: min_max_fc
#scripting name: min_max_fc
def _get_input_spec_min_max_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_min_max_fc = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_min_max_fc
    else:
        return inputs_dict_min_max_fc[pin]

def _get_output_spec_min_max_fc(pin = None):
    outpin0 = _PinSpecification(name = "field_min", type_names = ["field"], document = """""")
    outpin1 = _PinSpecification(name = "field_max", type_names = ["field"], document = """""")
    outputs_dict_min_max_fc = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_min_max_fc
    else:
        return outputs_dict_min_max_fc[pin]

class _InputSpecMinMaxFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_min_max_fc(), op)
        self.fields_container = Input(_get_input_spec_min_max_fc(0), 0, op, -1) 

class _OutputSpecMinMaxFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_min_max_fc(), op)
        self.field_min = Output(_get_output_spec_min_max_fc(0), 0, op) 
        super().__init__(_get_output_spec_min_max_fc(), op)
        self.field_max = Output(_get_output_spec_min_max_fc(1), 1, op) 

class _MinMaxFc(_Operator):
    """Operator's description:
    Internal name is "min_max_fc"
    Scripting name is "min_max_fc"

    Description: Compute the component-wise minimum (out 0) and maximum (out 1) over a fields container.

    Input list: 
       0: fields_container 

    Output list: 
       0: field_min 
       1: field_max 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max_fc")
    >>> op_way2 = core.operators.min_max.min_max_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("min_max_fc")
        self.inputs = _InputSpecMinMaxFc(self)
        self.outputs = _OutputSpecMinMaxFc(self)

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

def min_max_fc():
    """Operator's description:
    Internal name is "min_max_fc"
    Scripting name is "min_max_fc"

    Description: Compute the component-wise minimum (out 0) and maximum (out 1) over a fields container.

    Input list: 
       0: fields_container 

    Output list: 
       0: field_min 
       1: field_max 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max_fc")
    >>> op_way2 = core.operators.min_max.min_max_fc()
    """
    return _MinMaxFc()

#internal name: min_max_over_label_fc
#scripting name: min_max_over_label_fc
def _get_input_spec_min_max_over_label_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "label", type_names = ["string"], optional = False, document = """label name from the fields container""")
    inputs_dict_min_max_over_label_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_min_max_over_label_fc
    else:
        return inputs_dict_min_max_over_label_fc[pin]

def _get_output_spec_min_max_over_label_fc(pin = None):
    outpin0 = _PinSpecification(name = "field_min", type_names = ["field"], document = """""")
    outpin1 = _PinSpecification(name = "field_max", type_names = ["field"], document = """""")
    outputs_dict_min_max_over_label_fc = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_min_max_over_label_fc
    else:
        return outputs_dict_min_max_over_label_fc[pin]

class _InputSpecMinMaxOverLabelFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_min_max_over_label_fc(), op)
        self.fields_container = Input(_get_input_spec_min_max_over_label_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_min_max_over_label_fc(), op)
        self.label = Input(_get_input_spec_min_max_over_label_fc(1), 1, op, -1) 

class _OutputSpecMinMaxOverLabelFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_min_max_over_label_fc(), op)
        self.field_min = Output(_get_output_spec_min_max_over_label_fc(0), 0, op) 
        super().__init__(_get_output_spec_min_max_over_label_fc(), op)
        self.field_max = Output(_get_output_spec_min_max_over_label_fc(1), 1, op) 

class _MinMaxOverLabelFc(_Operator):
    """Operator's description:
    Internal name is "min_max_over_label_fc"
    Scripting name is "min_max_over_label_fc"

    Description: Compute the component-wise minimum (out 0) and maximum (out 1) over all the fields having the same id for the label set in input in the fields container.

    Input list: 
       0: fields_container 
       1: label (label name from the fields container)

    Output list: 
       0: field_min 
       1: field_max 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max_over_label_fc")
    >>> op_way2 = core.operators.min_max.min_max_over_label_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("min_max_over_label_fc")
        self.inputs = _InputSpecMinMaxOverLabelFc(self)
        self.outputs = _OutputSpecMinMaxOverLabelFc(self)

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

def min_max_over_label_fc():
    """Operator's description:
    Internal name is "min_max_over_label_fc"
    Scripting name is "min_max_over_label_fc"

    Description: Compute the component-wise minimum (out 0) and maximum (out 1) over all the fields having the same id for the label set in input in the fields container.

    Input list: 
       0: fields_container 
       1: label (label name from the fields container)

    Output list: 
       0: field_min 
       1: field_max 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max_over_label_fc")
    >>> op_way2 = core.operators.min_max.min_max_over_label_fc()
    """
    return _MinMaxOverLabelFc()

#internal name: min_by_component
#scripting name: min_by_component
def _get_input_spec_min_by_component(pin = None):
    inpin0 = _PinSpecification(name = "use_absolute_value", type_names = ["bool"], optional = False, document = """use_absolute_value""")
    inpin1 = _PinSpecification(name = "fieldA1", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin2 = _PinSpecification(name = "fieldA2", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin3 = _PinSpecification(name = "fieldB2", type_names = ["field","fields_container"], optional = False, document = """""")
    inputs_dict_min_by_component = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    if pin is None:
        return inputs_dict_min_by_component
    else:
        return inputs_dict_min_by_component[pin]

def _get_output_spec_min_by_component(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_min_by_component = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_min_by_component
    else:
        return outputs_dict_min_by_component[pin]

class _InputSpecMinByComponent(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_min_by_component(), op)
        self.use_absolute_value = Input(_get_input_spec_min_by_component(0), 0, op, -1) 
        super().__init__(_get_input_spec_min_by_component(), op)
        self.fieldA1 = Input(_get_input_spec_min_by_component(1), 1, op, 0) 
        super().__init__(_get_input_spec_min_by_component(), op)
        self.fieldA2 = Input(_get_input_spec_min_by_component(2), 2, op, 0) 
        super().__init__(_get_input_spec_min_by_component(), op)
        self.fieldB2 = Input(_get_input_spec_min_by_component(3), 3, op, -1) 

class _OutputSpecMinByComponent(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_min_by_component(), op)
        self.field = Output(_get_output_spec_min_by_component(0), 0, op) 

class _MinByComponent(_Operator):
    """Operator's description:
    Internal name is "min_by_component"
    Scripting name is "min_by_component"

    Description: Give the minimum for each element rank by comparing several fields.

    Input list: 
       0: use_absolute_value (use_absolute_value)
       1: fieldA1 (field or fields container with only one field is expected)
       2: fieldA2 (field or fields container with only one field is expected)
       3: fieldB2 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_by_component")
    >>> op_way2 = core.operators.min_max.min_by_component()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("min_by_component")
        self.inputs = _InputSpecMinByComponent(self)
        self.outputs = _OutputSpecMinByComponent(self)

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

def min_by_component():
    """Operator's description:
    Internal name is "min_by_component"
    Scripting name is "min_by_component"

    Description: Give the minimum for each element rank by comparing several fields.

    Input list: 
       0: use_absolute_value (use_absolute_value)
       1: fieldA1 (field or fields container with only one field is expected)
       2: fieldA2 (field or fields container with only one field is expected)
       3: fieldB2 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_by_component")
    >>> op_way2 = core.operators.min_max.min_by_component()
    """
    return _MinByComponent()

#internal name: max_by_component
#scripting name: max_by_component
def _get_input_spec_max_by_component(pin = None):
    inpin0 = _PinSpecification(name = "use_absolute_value", type_names = ["bool"], optional = False, document = """use_absolute_value""")
    inpin1 = _PinSpecification(name = "fieldA1", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin2 = _PinSpecification(name = "fieldA2", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin3 = _PinSpecification(name = "fieldB2", type_names = ["field","fields_container"], optional = False, document = """""")
    inputs_dict_max_by_component = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    if pin is None:
        return inputs_dict_max_by_component
    else:
        return inputs_dict_max_by_component[pin]

def _get_output_spec_max_by_component(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_max_by_component = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_max_by_component
    else:
        return outputs_dict_max_by_component[pin]

class _InputSpecMaxByComponent(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_max_by_component(), op)
        self.use_absolute_value = Input(_get_input_spec_max_by_component(0), 0, op, -1) 
        super().__init__(_get_input_spec_max_by_component(), op)
        self.fieldA1 = Input(_get_input_spec_max_by_component(1), 1, op, 0) 
        super().__init__(_get_input_spec_max_by_component(), op)
        self.fieldA2 = Input(_get_input_spec_max_by_component(2), 2, op, 0) 
        super().__init__(_get_input_spec_max_by_component(), op)
        self.fieldB2 = Input(_get_input_spec_max_by_component(3), 3, op, -1) 

class _OutputSpecMaxByComponent(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_max_by_component(), op)
        self.field = Output(_get_output_spec_max_by_component(0), 0, op) 

class _MaxByComponent(_Operator):
    """Operator's description:
    Internal name is "max_by_component"
    Scripting name is "max_by_component"

    Description: Give the maximum for each element rank by comparing several fields.

    Input list: 
       0: use_absolute_value (use_absolute_value)
       1: fieldA1 (field or fields container with only one field is expected)
       2: fieldA2 (field or fields container with only one field is expected)
       3: fieldB2 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("max_by_component")
    >>> op_way2 = core.operators.min_max.max_by_component()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("max_by_component")
        self.inputs = _InputSpecMaxByComponent(self)
        self.outputs = _OutputSpecMaxByComponent(self)

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

def max_by_component():
    """Operator's description:
    Internal name is "max_by_component"
    Scripting name is "max_by_component"

    Description: Give the maximum for each element rank by comparing several fields.

    Input list: 
       0: use_absolute_value (use_absolute_value)
       1: fieldA1 (field or fields container with only one field is expected)
       2: fieldA2 (field or fields container with only one field is expected)
       3: fieldB2 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("max_by_component")
    >>> op_way2 = core.operators.min_max.max_by_component()
    """
    return _MaxByComponent()

#internal name: min_max_fc_inc
#scripting name: min_max_fc_inc
def _get_input_spec_min_max_fc_inc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_min_max_fc_inc = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_min_max_fc_inc
    else:
        return inputs_dict_min_max_fc_inc[pin]

def _get_output_spec_min_max_fc_inc(pin = None):
    outpin0 = _PinSpecification(name = "field_min", type_names = ["field"], document = """""")
    outpin1 = _PinSpecification(name = "field_max", type_names = ["field"], document = """""")
    outputs_dict_min_max_fc_inc = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_min_max_fc_inc
    else:
        return outputs_dict_min_max_fc_inc[pin]

class _InputSpecMinMaxFcInc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_min_max_fc_inc(), op)
        self.fields_container = Input(_get_input_spec_min_max_fc_inc(0), 0, op, -1) 

class _OutputSpecMinMaxFcInc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_min_max_fc_inc(), op)
        self.field_min = Output(_get_output_spec_min_max_fc_inc(0), 0, op) 
        super().__init__(_get_output_spec_min_max_fc_inc(), op)
        self.field_max = Output(_get_output_spec_min_max_fc_inc(1), 1, op) 

class _MinMaxFcInc(_Operator):
    """Operator's description:
    Internal name is "min_max_fc_inc"
    Scripting name is "min_max_fc_inc"

    Description: Compute the component-wise minimum (out 0) and maximum (out 1) over a fields container.

    Input list: 
       0: fields_container 

    Output list: 
       0: field_min 
       1: field_max 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max_fc_inc")
    >>> op_way2 = core.operators.min_max.min_max_fc_inc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("min_max_fc_inc")
        self.inputs = _InputSpecMinMaxFcInc(self)
        self.outputs = _OutputSpecMinMaxFcInc(self)

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

def min_max_fc_inc():
    """Operator's description:
    Internal name is "min_max_fc_inc"
    Scripting name is "min_max_fc_inc"

    Description: Compute the component-wise minimum (out 0) and maximum (out 1) over a fields container.

    Input list: 
       0: fields_container 

    Output list: 
       0: field_min 
       1: field_max 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max_fc_inc")
    >>> op_way2 = core.operators.min_max.min_max_fc_inc()
    """
    return _MinMaxFcInc()

#internal name: min_max_inc
#scripting name: min_max_inc
def _get_input_spec_min_max_inc(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_min_max_inc = { 
        0 : inpin0,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_min_max_inc
    else:
        return inputs_dict_min_max_inc[pin]

def _get_output_spec_min_max_inc(pin = None):
    outpin0 = _PinSpecification(name = "field_min", type_names = ["field"], document = """""")
    outpin1 = _PinSpecification(name = "field_max", type_names = ["field"], document = """""")
    outpin2 = _PinSpecification(name = "domain_ids_min", type_names = ["scoping"], document = """""")
    outpin3 = _PinSpecification(name = "domain_ids_max", type_names = ["scoping"], document = """""")
    outputs_dict_min_max_inc = { 
        0 : outpin0,
        1 : outpin1,
        2 : outpin2,
        3 : outpin3
    }
    if pin is None:
        return outputs_dict_min_max_inc
    else:
        return outputs_dict_min_max_inc[pin]

class _InputSpecMinMaxInc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_min_max_inc(), op)
        self.field = Input(_get_input_spec_min_max_inc(0), 0, op, -1) 
        super().__init__(_get_input_spec_min_max_inc(), op)
        self.domain_id = Input(_get_input_spec_min_max_inc(17), 17, op, -1) 

class _OutputSpecMinMaxInc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_min_max_inc(), op)
        self.field_min = Output(_get_output_spec_min_max_inc(0), 0, op) 
        super().__init__(_get_output_spec_min_max_inc(), op)
        self.field_max = Output(_get_output_spec_min_max_inc(1), 1, op) 
        super().__init__(_get_output_spec_min_max_inc(), op)
        self.domain_ids_min = Output(_get_output_spec_min_max_inc(2), 2, op) 
        super().__init__(_get_output_spec_min_max_inc(), op)
        self.domain_ids_max = Output(_get_output_spec_min_max_inc(3), 3, op) 

class _MinMaxInc(_Operator):
    """Operator's description:
    Internal name is "min_max_inc"
    Scripting name is "min_max_inc"

    Description: Compute the component-wise minimum (out 0) and maximum (out 1) over coming fields.

    Input list: 
       0: field 
       17: domain_id 

    Output list: 
       0: field_min 
       1: field_max 
       2: domain_ids_min 
       3: domain_ids_max 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max_inc")
    >>> op_way2 = core.operators.min_max.min_max_inc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("min_max_inc")
        self.inputs = _InputSpecMinMaxInc(self)
        self.outputs = _OutputSpecMinMaxInc(self)

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

def min_max_inc():
    """Operator's description:
    Internal name is "min_max_inc"
    Scripting name is "min_max_inc"

    Description: Compute the component-wise minimum (out 0) and maximum (out 1) over coming fields.

    Input list: 
       0: field 
       17: domain_id 

    Output list: 
       0: field_min 
       1: field_max 
       2: domain_ids_min 
       3: domain_ids_max 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max_inc")
    >>> op_way2 = core.operators.min_max.min_max_inc()
    """
    return _MinMaxInc()

