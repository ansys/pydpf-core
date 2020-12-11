from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "math" category
"""

#internal name: minus
#scripting name: minus
def _get_input_spec_minus(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_minus = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_minus
    else:
        return inputs_dict_minus[pin]

def _get_output_spec_minus(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_minus = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_minus
    else:
        return outputs_dict_minus[pin]

class _InputSpecMinus(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_minus(), op)
        self.fieldA = Input(_get_input_spec_minus(0), 0, op, -1) 
        super().__init__(_get_input_spec_minus(), op)
        self.fieldB = Input(_get_input_spec_minus(1), 1, op, -1) 

class _OutputSpecMinus(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_minus(), op)
        self.field = Output(_get_output_spec_minus(0), 0, op) 

class _Minus(_Operator):
    """Operator's description:
    Internal name is "minus"
    Scripting name is "minus"

    Description: Computes the difference of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("minus")
    >>> op_way2 = core.operators.math.minus()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("minus")
        self.inputs = _InputSpecMinus(self)
        self.outputs = _OutputSpecMinus(self)

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

def minus():
    """Operator's description:
    Internal name is "minus"
    Scripting name is "minus"

    Description: Computes the difference of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("minus")
    >>> op_way2 = core.operators.math.minus()
    """
    return _Minus()

#internal name: cplx_multiply
#scripting name: cplx_multiply
def _get_input_spec_cplx_multiply(pin = None):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_multiply = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_cplx_multiply
    else:
        return inputs_dict_cplx_multiply[pin]

def _get_output_spec_cplx_multiply(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_multiply = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cplx_multiply
    else:
        return outputs_dict_cplx_multiply[pin]

class _InputSpecCplxMultiply(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cplx_multiply(), op)
        self.fields_containerA = Input(_get_input_spec_cplx_multiply(0), 0, op, -1) 
        super().__init__(_get_input_spec_cplx_multiply(), op)
        self.fields_containerB = Input(_get_input_spec_cplx_multiply(1), 1, op, -1) 

class _OutputSpecCplxMultiply(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cplx_multiply(), op)
        self.fields_container = Output(_get_output_spec_cplx_multiply(0), 0, op) 

class _CplxMultiply(_Operator):
    """Operator's description:
    Internal name is "cplx_multiply"
    Scripting name is "cplx_multiply"

    Description: Computes multiply between two field containers containing complex fields.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cplx_multiply")
    >>> op_way2 = core.operators.math.cplx_multiply()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cplx_multiply")
        self.inputs = _InputSpecCplxMultiply(self)
        self.outputs = _OutputSpecCplxMultiply(self)

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

def cplx_multiply():
    """Operator's description:
    Internal name is "cplx_multiply"
    Scripting name is "cplx_multiply"

    Description: Computes multiply between two field containers containing complex fields.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cplx_multiply")
    >>> op_way2 = core.operators.math.cplx_multiply()
    """
    return _CplxMultiply()

#internal name: unit_convert
#scripting name: unit_convert
def _get_input_spec_unit_convert(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = False, document = """unit as a string, ex 'm' for meter, 'Pa' for pascal,...""")
    inputs_dict_unit_convert = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_unit_convert
    else:
        return inputs_dict_unit_convert[pin]

def _get_output_spec_unit_convert(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_unit_convert = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_unit_convert
    else:
        return outputs_dict_unit_convert[pin]

class _InputSpecUnitConvert(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_unit_convert(), op)
        self.field = Input(_get_input_spec_unit_convert(0), 0, op, -1) 
        super().__init__(_get_input_spec_unit_convert(), op)
        self.unit_name = Input(_get_input_spec_unit_convert(1), 1, op, -1) 

class _OutputSpecUnitConvert(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_unit_convert(), op)
        self.field = Output(_get_output_spec_unit_convert(0), 0, op) 

class _UnitConvert(_Operator):
    """Operator's description:
    Internal name is "unit_convert"
    Scripting name is "unit_convert"

    Description: Convert an input field of a given unit to another unit.

    Input list: 
       0: field 
       1: unit_name (unit as a string, ex 'm' for meter, 'Pa' for pascal,...)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("unit_convert")
    >>> op_way2 = core.operators.math.unit_convert()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("unit_convert")
        self.inputs = _InputSpecUnitConvert(self)
        self.outputs = _OutputSpecUnitConvert(self)

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

def unit_convert():
    """Operator's description:
    Internal name is "unit_convert"
    Scripting name is "unit_convert"

    Description: Convert an input field of a given unit to another unit.

    Input list: 
       0: field 
       1: unit_name (unit as a string, ex 'm' for meter, 'Pa' for pascal,...)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("unit_convert")
    >>> op_way2 = core.operators.math.unit_convert()
    """
    return _UnitConvert()

#internal name: min_max_over_time
#scripting name: min_max_over_time
def _get_input_spec_min_max_over_time(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "angle", type_names = ["double"], optional = True, document = """Phase angle used for complex field container""")
    inpin2 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = True, document = """Phase angle unit. Default is radian.""")
    inpin3 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin4 = _PinSpecification(name = "compute_amplitude", type_names = ["bool"], optional = True, document = """Do calculate amplitude.""")
    inpin5 = _PinSpecification(name = "int32", type_names = ["int32"], optional = False, document = """Define min or max.""")
    inputs_dict_min_max_over_time = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5
    }
    if pin is None:
        return inputs_dict_min_max_over_time
    else:
        return inputs_dict_min_max_over_time[pin]

def _get_output_spec_min_max_over_time(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_min_max_over_time = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_min_max_over_time
    else:
        return outputs_dict_min_max_over_time[pin]

class _InputSpecMinMaxOverTime(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_min_max_over_time(), op)
        self.fields_container = Input(_get_input_spec_min_max_over_time(0), 0, op, -1) 
        super().__init__(_get_input_spec_min_max_over_time(), op)
        self.angle = Input(_get_input_spec_min_max_over_time(1), 1, op, -1) 
        super().__init__(_get_input_spec_min_max_over_time(), op)
        self.unit_name = Input(_get_input_spec_min_max_over_time(2), 2, op, -1) 
        super().__init__(_get_input_spec_min_max_over_time(), op)
        self.abs_value = Input(_get_input_spec_min_max_over_time(3), 3, op, -1) 
        super().__init__(_get_input_spec_min_max_over_time(), op)
        self.compute_amplitude = Input(_get_input_spec_min_max_over_time(4), 4, op, -1) 
        super().__init__(_get_input_spec_min_max_over_time(), op)
        self.int32 = Input(_get_input_spec_min_max_over_time(5), 5, op, -1) 

class _OutputSpecMinMaxOverTime(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_min_max_over_time(), op)
        self.field = Output(_get_output_spec_min_max_over_time(0), 0, op) 

class _MinMaxOverTime(_Operator):
    """Operator's description:
    Internal name is "min_max_over_time"
    Scripting name is "min_max_over_time"

    Description: Evaluates minimum/maximum over time/frequency.

    Input list: 
       0: fields_container 
       1: angle (Phase angle used for complex field container)
       2: unit_name (Phase angle unit. Default is radian.)
       3: abs_value (Should use absolute value.)
       4: compute_amplitude (Do calculate amplitude.)
       5: int32 (Define min or max.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max_over_time")
    >>> op_way2 = core.operators.math.min_max_over_time()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("min_max_over_time")
        self.inputs = _InputSpecMinMaxOverTime(self)
        self.outputs = _OutputSpecMinMaxOverTime(self)

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

def min_max_over_time():
    """Operator's description:
    Internal name is "min_max_over_time"
    Scripting name is "min_max_over_time"

    Description: Evaluates minimum/maximum over time/frequency.

    Input list: 
       0: fields_container 
       1: angle (Phase angle used for complex field container)
       2: unit_name (Phase angle unit. Default is radian.)
       3: abs_value (Should use absolute value.)
       4: compute_amplitude (Do calculate amplitude.)
       5: int32 (Define min or max.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_max_over_time")
    >>> op_way2 = core.operators.math.min_max_over_time()
    """
    return _MinMaxOverTime()

#internal name: minus_fc
#scripting name: minus_fc
def _get_input_spec_minus_fc(pin = None):
    inpin0 = _PinSpecification(name = "field_or_fields_container_A", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "field_or_fields_container_B", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_minus_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_minus_fc
    else:
        return inputs_dict_minus_fc[pin]

def _get_output_spec_minus_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_minus_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_minus_fc
    else:
        return outputs_dict_minus_fc[pin]

class _InputSpecMinusFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_minus_fc(), op)
        self.field_or_fields_container_A = Input(_get_input_spec_minus_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_minus_fc(), op)
        self.field_or_fields_container_B = Input(_get_input_spec_minus_fc(1), 1, op, -1) 

class _OutputSpecMinusFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_minus_fc(), op)
        self.fields_container = Output(_get_output_spec_minus_fc(0), 0, op) 

class _MinusFc(_Operator):
    """Operator's description:
    Internal name is "minus_fc"
    Scripting name is "minus_fc"

    Description: Computes the difference of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

    Input list: 
       0: field_or_fields_container_A (field or fields container with only one field is expected)
       1: field_or_fields_container_B (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("minus_fc")
    >>> op_way2 = core.operators.math.minus_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("minus_fc")
        self.inputs = _InputSpecMinusFc(self)
        self.outputs = _OutputSpecMinusFc(self)

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

def minus_fc():
    """Operator's description:
    Internal name is "minus_fc"
    Scripting name is "minus_fc"

    Description: Computes the difference of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

    Input list: 
       0: field_or_fields_container_A (field or fields container with only one field is expected)
       1: field_or_fields_container_B (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("minus_fc")
    >>> op_way2 = core.operators.math.minus_fc()
    """
    return _MinusFc()

#internal name: accumulate
#scripting name: accumulate
def _get_input_spec_accumulate(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_accumulate = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_accumulate
    else:
        return inputs_dict_accumulate[pin]

def _get_output_spec_accumulate(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_accumulate = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_accumulate
    else:
        return outputs_dict_accumulate[pin]

class _InputSpecAccumulate(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_accumulate(), op)
        self.fieldA = Input(_get_input_spec_accumulate(0), 0, op, -1) 

class _OutputSpecAccumulate(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_accumulate(), op)
        self.field = Output(_get_output_spec_accumulate(0), 0, op) 

class _Accumulate(_Operator):
    """Operator's description:
    Internal name is "accumulate"
    Scripting name is "accumulate"

    Description: Sum all the elementary data of a field to get one elementary data at the end.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("accumulate")
    >>> op_way2 = core.operators.math.accumulate()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("accumulate")
        self.inputs = _InputSpecAccumulate(self)
        self.outputs = _OutputSpecAccumulate(self)

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

def accumulate():
    """Operator's description:
    Internal name is "accumulate"
    Scripting name is "accumulate"

    Description: Sum all the elementary data of a field to get one elementary data at the end.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("accumulate")
    >>> op_way2 = core.operators.math.accumulate()
    """
    return _Accumulate()

#internal name: unit_convert_fc
#scripting name: unit_convert_fc
def _get_input_spec_unit_convert_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = False, document = """unit as a string, ex 'm' for meter, 'Pa' for pascal,...""")
    inputs_dict_unit_convert_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_unit_convert_fc
    else:
        return inputs_dict_unit_convert_fc[pin]

def _get_output_spec_unit_convert_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_unit_convert_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_unit_convert_fc
    else:
        return outputs_dict_unit_convert_fc[pin]

class _InputSpecUnitConvertFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_unit_convert_fc(), op)
        self.fields_container = Input(_get_input_spec_unit_convert_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_unit_convert_fc(), op)
        self.unit_name = Input(_get_input_spec_unit_convert_fc(1), 1, op, -1) 

class _OutputSpecUnitConvertFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_unit_convert_fc(), op)
        self.fields_container = Output(_get_output_spec_unit_convert_fc(0), 0, op) 

class _UnitConvertFc(_Operator):
    """Operator's description:
    Internal name is "unit_convert_fc"
    Scripting name is "unit_convert_fc"

    Description: Convert an input fields container of a given unit to another unit.

    Input list: 
       0: fields_container 
       1: unit_name (unit as a string, ex 'm' for meter, 'Pa' for pascal,...)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("unit_convert_fc")
    >>> op_way2 = core.operators.math.unit_convert_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("unit_convert_fc")
        self.inputs = _InputSpecUnitConvertFc(self)
        self.outputs = _OutputSpecUnitConvertFc(self)

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

def unit_convert_fc():
    """Operator's description:
    Internal name is "unit_convert_fc"
    Scripting name is "unit_convert_fc"

    Description: Convert an input fields container of a given unit to another unit.

    Input list: 
       0: fields_container 
       1: unit_name (unit as a string, ex 'm' for meter, 'Pa' for pascal,...)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("unit_convert_fc")
    >>> op_way2 = core.operators.math.unit_convert_fc()
    """
    return _UnitConvertFc()

#internal name: add
#scripting name: add
def _get_input_spec_add(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_add = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_add
    else:
        return inputs_dict_add[pin]

def _get_output_spec_add(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_add = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_add
    else:
        return outputs_dict_add[pin]

class _InputSpecAdd(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_add(), op)
        self.fieldA = Input(_get_input_spec_add(0), 0, op, -1) 
        super().__init__(_get_input_spec_add(), op)
        self.fieldB = Input(_get_input_spec_add(1), 1, op, -1) 

class _OutputSpecAdd(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_add(), op)
        self.field = Output(_get_output_spec_add(0), 0, op) 

class _Add(_Operator):
    """Operator's description:
    Internal name is "add"
    Scripting name is "add"

    Description: Computes the sum of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field. if one of the input field is empty, the remaining is forwarded to the output.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("add")
    >>> op_way2 = core.operators.math.add()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("add")
        self.inputs = _InputSpecAdd(self)
        self.outputs = _OutputSpecAdd(self)

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

def add():
    """Operator's description:
    Internal name is "add"
    Scripting name is "add"

    Description: Computes the sum of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field. if one of the input field is empty, the remaining is forwarded to the output.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("add")
    >>> op_way2 = core.operators.math.add()
    """
    return _Add()

#internal name: add_fc
#scripting name: add_fc
def _get_input_spec_add_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container1", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_container2", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_add_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_add_fc
    else:
        return inputs_dict_add_fc[pin]

def _get_output_spec_add_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_add_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_add_fc
    else:
        return outputs_dict_add_fc[pin]

class _InputSpecAddFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_add_fc(), op)
        self.fields_container1 = Input(_get_input_spec_add_fc(0), 0, op, 0) 
        super().__init__(_get_input_spec_add_fc(), op)
        self.fields_container2 = Input(_get_input_spec_add_fc(1), 1, op, -1) 

class _OutputSpecAddFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_add_fc(), op)
        self.fields_container = Output(_get_output_spec_add_fc(0), 0, op) 

class _AddFc(_Operator):
    """Operator's description:
    Internal name is "add_fc"
    Scripting name is "add_fc"

    Description: Compute the field-wise sum of the input fields containers.

    Input list: 
       0: fields_container1 
       1: fields_container2 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("add_fc")
    >>> op_way2 = core.operators.math.add_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("add_fc")
        self.inputs = _InputSpecAddFc(self)
        self.outputs = _OutputSpecAddFc(self)

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

def add_fc():
    """Operator's description:
    Internal name is "add_fc"
    Scripting name is "add_fc"

    Description: Compute the field-wise sum of the input fields containers.

    Input list: 
       0: fields_container1 
       1: fields_container2 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("add_fc")
    >>> op_way2 = core.operators.math.add_fc()
    """
    return _AddFc()

#internal name: phase_of_max
#scripting name: phase_of_max
def _get_input_spec_phase_of_max(pin = None):
    inpin0 = _PinSpecification(name = "real_field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "imaginary_field", type_names = ["field"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin3 = _PinSpecification(name = "phase_increment", type_names = ["double"], optional = False, document = """Phase increment.""")
    inputs_dict_phase_of_max = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    if pin is None:
        return inputs_dict_phase_of_max
    else:
        return inputs_dict_phase_of_max[pin]

def _get_output_spec_phase_of_max(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_phase_of_max = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_phase_of_max
    else:
        return outputs_dict_phase_of_max[pin]

class _InputSpecPhaseOfMax(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_phase_of_max(), op)
        self.real_field = Input(_get_input_spec_phase_of_max(0), 0, op, -1) 
        super().__init__(_get_input_spec_phase_of_max(), op)
        self.imaginary_field = Input(_get_input_spec_phase_of_max(1), 1, op, -1) 
        super().__init__(_get_input_spec_phase_of_max(), op)
        self.abs_value = Input(_get_input_spec_phase_of_max(2), 2, op, -1) 
        super().__init__(_get_input_spec_phase_of_max(), op)
        self.phase_increment = Input(_get_input_spec_phase_of_max(3), 3, op, -1) 

class _OutputSpecPhaseOfMax(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_phase_of_max(), op)
        self.field = Output(_get_output_spec_phase_of_max(0), 0, op) 

class _PhaseOfMax(_Operator):
    """Operator's description:
    Internal name is "phase_of_max"
    Scripting name is "phase_of_max"

    Description: Evaluates phase of maximum.

    Input list: 
       0: real_field 
       1: imaginary_field 
       2: abs_value (Should use absolute value.)
       3: phase_increment (Phase increment.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("phase_of_max")
    >>> op_way2 = core.operators.math.phase_of_max()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("phase_of_max")
        self.inputs = _InputSpecPhaseOfMax(self)
        self.outputs = _OutputSpecPhaseOfMax(self)

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

def phase_of_max():
    """Operator's description:
    Internal name is "phase_of_max"
    Scripting name is "phase_of_max"

    Description: Evaluates phase of maximum.

    Input list: 
       0: real_field 
       1: imaginary_field 
       2: abs_value (Should use absolute value.)
       3: phase_increment (Phase increment.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("phase_of_max")
    >>> op_way2 = core.operators.math.phase_of_max()
    """
    return _PhaseOfMax()

#internal name: sin_fc
#scripting name: sin_fc
def _get_input_spec_sin_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_sin_fc = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_sin_fc
    else:
        return inputs_dict_sin_fc[pin]

def _get_output_spec_sin_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sin_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_sin_fc
    else:
        return outputs_dict_sin_fc[pin]

class _InputSpecSinFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_sin_fc(), op)
        self.fields_container = Input(_get_input_spec_sin_fc(0), 0, op, -1) 

class _OutputSpecSinFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_sin_fc(), op)
        self.fields_container = Output(_get_output_spec_sin_fc(0), 0, op) 

class _SinFc(_Operator):
    """Operator's description:
    Internal name is "sin_fc"
    Scripting name is "sin_fc"

    Description: Computes element-wise sin(field[i]).

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sin_fc")
    >>> op_way2 = core.operators.math.sin_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("sin_fc")
        self.inputs = _InputSpecSinFc(self)
        self.outputs = _OutputSpecSinFc(self)

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

def sin_fc():
    """Operator's description:
    Internal name is "sin_fc"
    Scripting name is "sin_fc"

    Description: Computes element-wise sin(field[i]).

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sin_fc")
    >>> op_way2 = core.operators.math.sin_fc()
    """
    return _SinFc()

#internal name: add_constant
#scripting name: add_constant
def _get_input_spec_add_constant(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double"], optional = False, document = """double or vector of double""")
    inputs_dict_add_constant = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_add_constant
    else:
        return inputs_dict_add_constant[pin]

def _get_output_spec_add_constant(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_add_constant = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_add_constant
    else:
        return outputs_dict_add_constant[pin]

class _InputSpecAddConstant(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_add_constant(), op)
        self.field = Input(_get_input_spec_add_constant(0), 0, op, -1) 
        super().__init__(_get_input_spec_add_constant(), op)
        self.ponderation = Input(_get_input_spec_add_constant(1), 1, op, -1) 

class _OutputSpecAddConstant(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_add_constant(), op)
        self.field = Output(_get_output_spec_add_constant(0), 0, op) 

class _AddConstant(_Operator):
    """Operator's description:
    Internal name is "add_constant"
    Scripting name is "add_constant"

    Description: Computes the sum of a field (in 0) and a scalar (in 1).

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: ponderation (double or vector of double)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("add_constant")
    >>> op_way2 = core.operators.math.add_constant()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("add_constant")
        self.inputs = _InputSpecAddConstant(self)
        self.outputs = _OutputSpecAddConstant(self)

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

def add_constant():
    """Operator's description:
    Internal name is "add_constant"
    Scripting name is "add_constant"

    Description: Computes the sum of a field (in 0) and a scalar (in 1).

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: ponderation (double or vector of double)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("add_constant")
    >>> op_way2 = core.operators.math.add_constant()
    """
    return _AddConstant()

#internal name: invert_fc
#scripting name: invert_fc
def _get_input_spec_invert_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_invert_fc = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_invert_fc
    else:
        return inputs_dict_invert_fc[pin]

def _get_output_spec_invert_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_invert_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_invert_fc
    else:
        return outputs_dict_invert_fc[pin]

class _InputSpecInvertFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_invert_fc(), op)
        self.fields_container = Input(_get_input_spec_invert_fc(0), 0, op, -1) 

class _OutputSpecInvertFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_invert_fc(), op)
        self.fields_container = Output(_get_output_spec_invert_fc(0), 0, op) 

class _InvertFc(_Operator):
    """Operator's description:
    Internal name is "invert_fc"
    Scripting name is "invert_fc"

    Description: Compute the element-wise, component-wise, inverse of a field (1./x)

    Input list: 
       0: fields_container (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("invert_fc")
    >>> op_way2 = core.operators.math.invert_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("invert_fc")
        self.inputs = _InputSpecInvertFc(self)
        self.outputs = _OutputSpecInvertFc(self)

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

def invert_fc():
    """Operator's description:
    Internal name is "invert_fc"
    Scripting name is "invert_fc"

    Description: Compute the element-wise, component-wise, inverse of a field (1./x)

    Input list: 
       0: fields_container (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("invert_fc")
    >>> op_way2 = core.operators.math.invert_fc()
    """
    return _InvertFc()

#internal name: Pow
#scripting name: pow
def _get_input_spec_pow(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "factor", type_names = ["double"], optional = False, document = """""")
    inputs_dict_pow = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_pow
    else:
        return inputs_dict_pow[pin]

def _get_output_spec_pow(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_pow = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_pow
    else:
        return outputs_dict_pow[pin]

class _InputSpecPow(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_pow(), op)
        self.field = Input(_get_input_spec_pow(0), 0, op, -1) 
        super().__init__(_get_input_spec_pow(), op)
        self.factor = Input(_get_input_spec_pow(1), 1, op, -1) 

class _OutputSpecPow(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_pow(), op)
        self.field = Output(_get_output_spec_pow(0), 0, op) 

class _Pow(_Operator):
    """Operator's description:
    Internal name is "Pow"
    Scripting name is "pow"

    Description: Computes element-wise field[i]^p.

    Input list: 
       0: field 
       1: factor 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("Pow")
    >>> op_way2 = core.operators.math.pow()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("Pow")
        self.inputs = _InputSpecPow(self)
        self.outputs = _OutputSpecPow(self)

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

def pow():
    """Operator's description:
    Internal name is "Pow"
    Scripting name is "pow"

    Description: Computes element-wise field[i]^p.

    Input list: 
       0: field 
       1: factor 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("Pow")
    >>> op_way2 = core.operators.math.pow()
    """
    return _Pow()

#internal name: add_constant_fc
#scripting name: add_constant_fc
def _get_input_spec_add_constant_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double"], optional = False, document = """double or vector of double""")
    inputs_dict_add_constant_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_add_constant_fc
    else:
        return inputs_dict_add_constant_fc[pin]

def _get_output_spec_add_constant_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_add_constant_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_add_constant_fc
    else:
        return outputs_dict_add_constant_fc[pin]

class _InputSpecAddConstantFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_add_constant_fc(), op)
        self.fields_container = Input(_get_input_spec_add_constant_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_add_constant_fc(), op)
        self.ponderation = Input(_get_input_spec_add_constant_fc(1), 1, op, -1) 

class _OutputSpecAddConstantFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_add_constant_fc(), op)
        self.fields_container = Output(_get_output_spec_add_constant_fc(0), 0, op) 

class _AddConstantFc(_Operator):
    """Operator's description:
    Internal name is "add_constant_fc"
    Scripting name is "add_constant_fc"

    Description: Computes the sum of a field (in 0) and a scalar (in 1).

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: ponderation (double or vector of double)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("add_constant_fc")
    >>> op_way2 = core.operators.math.add_constant_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("add_constant_fc")
        self.inputs = _InputSpecAddConstantFc(self)
        self.outputs = _OutputSpecAddConstantFc(self)

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

def add_constant_fc():
    """Operator's description:
    Internal name is "add_constant_fc"
    Scripting name is "add_constant_fc"

    Description: Computes the sum of a field (in 0) and a scalar (in 1).

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: ponderation (double or vector of double)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("add_constant_fc")
    >>> op_way2 = core.operators.math.add_constant_fc()
    """
    return _AddConstantFc()

#internal name: scale
#scripting name: scale
def _get_input_spec_scale(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double","field"], optional = False, document = """Double/Field scoped on overall""")
    inpin2 = _PinSpecification(name = "boolean", type_names = ["bool"], optional = True, document = """bool(optional, default false) if set to true, output of scale is mane dimensionless""")
    inputs_dict_scale = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    if pin is None:
        return inputs_dict_scale
    else:
        return inputs_dict_scale[pin]

def _get_output_spec_scale(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_scale = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_scale
    else:
        return outputs_dict_scale[pin]

class _InputSpecScale(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_scale(), op)
        self.field = Input(_get_input_spec_scale(0), 0, op, -1) 
        super().__init__(_get_input_spec_scale(), op)
        self.ponderation = Input(_get_input_spec_scale(1), 1, op, -1) 
        super().__init__(_get_input_spec_scale(), op)
        self.boolean = Input(_get_input_spec_scale(2), 2, op, -1) 

class _OutputSpecScale(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_scale(), op)
        self.field = Output(_get_output_spec_scale(0), 0, op) 

class _Scale(_Operator):
    """Operator's description:
    Internal name is "scale"
    Scripting name is "scale"

    Description: Scales a field by a constant factor.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: ponderation (Double/Field scoped on overall)
       2: boolean (bool(optional, default false) if set to true, output of scale is mane dimensionless)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("scale")
    >>> op_way2 = core.operators.math.scale()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("scale")
        self.inputs = _InputSpecScale(self)
        self.outputs = _OutputSpecScale(self)

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

def scale():
    """Operator's description:
    Internal name is "scale"
    Scripting name is "scale"

    Description: Scales a field by a constant factor.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: ponderation (Double/Field scoped on overall)
       2: boolean (bool(optional, default false) if set to true, output of scale is mane dimensionless)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("scale")
    >>> op_way2 = core.operators.math.scale()
    """
    return _Scale()

#internal name: Pow_fc
#scripting name: pow_fc
def _get_input_spec_pow_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "factor", type_names = ["double"], optional = False, document = """""")
    inputs_dict_pow_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_pow_fc
    else:
        return inputs_dict_pow_fc[pin]

def _get_output_spec_pow_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_pow_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_pow_fc
    else:
        return outputs_dict_pow_fc[pin]

class _InputSpecPowFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_pow_fc(), op)
        self.fields_container = Input(_get_input_spec_pow_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_pow_fc(), op)
        self.factor = Input(_get_input_spec_pow_fc(1), 1, op, -1) 

class _OutputSpecPowFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_pow_fc(), op)
        self.fields_container = Output(_get_output_spec_pow_fc(0), 0, op) 

class _PowFc(_Operator):
    """Operator's description:
    Internal name is "Pow_fc"
    Scripting name is "pow_fc"

    Description: Computes element-wise field[i]^p.

    Input list: 
       0: fields_container 
       1: factor 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("Pow_fc")
    >>> op_way2 = core.operators.math.pow_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("Pow_fc")
        self.inputs = _InputSpecPowFc(self)
        self.outputs = _OutputSpecPowFc(self)

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

def pow_fc():
    """Operator's description:
    Internal name is "Pow_fc"
    Scripting name is "pow_fc"

    Description: Computes element-wise field[i]^p.

    Input list: 
       0: fields_container 
       1: factor 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("Pow_fc")
    >>> op_way2 = core.operators.math.pow_fc()
    """
    return _PowFc()

#internal name: scale_fc
#scripting name: scale_fc
def _get_input_spec_scale_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double","field"], optional = False, document = """Double/Field scoped on overall""")
    inpin2 = _PinSpecification(name = "boolean", type_names = ["bool"], optional = True, document = """bool(optional, default false) if set to true, output of scale is mane dimensionless""")
    inputs_dict_scale_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    if pin is None:
        return inputs_dict_scale_fc
    else:
        return inputs_dict_scale_fc[pin]

def _get_output_spec_scale_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_scale_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_scale_fc
    else:
        return outputs_dict_scale_fc[pin]

class _InputSpecScaleFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_scale_fc(), op)
        self.fields_container = Input(_get_input_spec_scale_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_scale_fc(), op)
        self.ponderation = Input(_get_input_spec_scale_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_scale_fc(), op)
        self.boolean = Input(_get_input_spec_scale_fc(2), 2, op, -1) 

class _OutputSpecScaleFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_scale_fc(), op)
        self.fields_container = Output(_get_output_spec_scale_fc(0), 0, op) 

class _ScaleFc(_Operator):
    """Operator's description:
    Internal name is "scale_fc"
    Scripting name is "scale_fc"

    Description: Scales a field by a constant factor.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: ponderation (Double/Field scoped on overall)
       2: boolean (bool(optional, default false) if set to true, output of scale is mane dimensionless)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("scale_fc")
    >>> op_way2 = core.operators.math.scale_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("scale_fc")
        self.inputs = _InputSpecScaleFc(self)
        self.outputs = _OutputSpecScaleFc(self)

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

def scale_fc():
    """Operator's description:
    Internal name is "scale_fc"
    Scripting name is "scale_fc"

    Description: Scales a field by a constant factor.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: ponderation (Double/Field scoped on overall)
       2: boolean (bool(optional, default false) if set to true, output of scale is mane dimensionless)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("scale_fc")
    >>> op_way2 = core.operators.math.scale_fc()
    """
    return _ScaleFc()

#internal name: centroid
#scripting name: centroid
def _get_input_spec_centroid(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin2 = _PinSpecification(name = "factor", type_names = ["double"], optional = False, document = """Scalar""")
    inputs_dict_centroid = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    if pin is None:
        return inputs_dict_centroid
    else:
        return inputs_dict_centroid[pin]

def _get_output_spec_centroid(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_centroid = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_centroid
    else:
        return outputs_dict_centroid[pin]

class _InputSpecCentroid(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_centroid(), op)
        self.fieldA = Input(_get_input_spec_centroid(0), 0, op, -1) 
        super().__init__(_get_input_spec_centroid(), op)
        self.fieldB = Input(_get_input_spec_centroid(1), 1, op, -1) 
        super().__init__(_get_input_spec_centroid(), op)
        self.factor = Input(_get_input_spec_centroid(2), 2, op, -1) 

class _OutputSpecCentroid(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_centroid(), op)
        self.field = Output(_get_output_spec_centroid(0), 0, op) 

class _Centroid(_Operator):
    """Operator's description:
    Internal name is "centroid"
    Scripting name is "centroid"

    Description: Computes centroid of field1 and field2, using fieldOut = field1*(1.-fact)+field2*(fact).

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)
       2: factor (Scalar)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("centroid")
    >>> op_way2 = core.operators.math.centroid()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("centroid")
        self.inputs = _InputSpecCentroid(self)
        self.outputs = _OutputSpecCentroid(self)

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

def centroid():
    """Operator's description:
    Internal name is "centroid"
    Scripting name is "centroid"

    Description: Computes centroid of field1 and field2, using fieldOut = field1*(1.-fact)+field2*(fact).

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)
       2: factor (Scalar)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("centroid")
    >>> op_way2 = core.operators.math.centroid()
    """
    return _Centroid()

#internal name: sweeping_phase
#scripting name: sweeping_phase
def _get_input_spec_sweeping_phase(pin = None):
    inpin0 = _PinSpecification(name = "real_field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "imaginary_field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin2 = _PinSpecification(name = "angle", type_names = ["double"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = False, document = """String Unit""")
    inpin4 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = False, document = """""")
    inpin5 = _PinSpecification(name = "imaginary_part_null", type_names = ["bool"], optional = False, document = """if the imaginary part field is empty and this pin is true, then the imaginary part is supposed to be 0 (default is false)""")
    inputs_dict_sweeping_phase = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5
    }
    if pin is None:
        return inputs_dict_sweeping_phase
    else:
        return inputs_dict_sweeping_phase[pin]

def _get_output_spec_sweeping_phase(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sweeping_phase = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_sweeping_phase
    else:
        return outputs_dict_sweeping_phase[pin]

class _InputSpecSweepingPhase(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_sweeping_phase(), op)
        self.real_field = Input(_get_input_spec_sweeping_phase(0), 0, op, -1) 
        super().__init__(_get_input_spec_sweeping_phase(), op)
        self.imaginary_field = Input(_get_input_spec_sweeping_phase(1), 1, op, -1) 
        super().__init__(_get_input_spec_sweeping_phase(), op)
        self.angle = Input(_get_input_spec_sweeping_phase(2), 2, op, -1) 
        super().__init__(_get_input_spec_sweeping_phase(), op)
        self.unit_name = Input(_get_input_spec_sweeping_phase(3), 3, op, -1) 
        super().__init__(_get_input_spec_sweeping_phase(), op)
        self.abs_value = Input(_get_input_spec_sweeping_phase(4), 4, op, -1) 
        super().__init__(_get_input_spec_sweeping_phase(), op)
        self.imaginary_part_null = Input(_get_input_spec_sweeping_phase(5), 5, op, -1) 

class _OutputSpecSweepingPhase(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_sweeping_phase(), op)
        self.field = Output(_get_output_spec_sweeping_phase(0), 0, op) 

class _SweepingPhase(_Operator):
    """Operator's description:
    Internal name is "sweeping_phase"
    Scripting name is "sweeping_phase"

    Description: Shift the phase of a real and an imaginary fields (in 0 and 1) of a given angle (in 3) of unit (in 4).

    Input list: 
       0: real_field (field or fields container with only one field is expected)
       1: imaginary_field (field or fields container with only one field is expected)
       2: angle 
       3: unit_name (String Unit)
       4: abs_value 
       5: imaginary_part_null (if the imaginary part field is empty and this pin is true, then the imaginary part is supposed to be 0 (default is false))

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sweeping_phase")
    >>> op_way2 = core.operators.math.sweeping_phase()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("sweeping_phase")
        self.inputs = _InputSpecSweepingPhase(self)
        self.outputs = _OutputSpecSweepingPhase(self)

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

def sweeping_phase():
    """Operator's description:
    Internal name is "sweeping_phase"
    Scripting name is "sweeping_phase"

    Description: Shift the phase of a real and an imaginary fields (in 0 and 1) of a given angle (in 3) of unit (in 4).

    Input list: 
       0: real_field (field or fields container with only one field is expected)
       1: imaginary_field (field or fields container with only one field is expected)
       2: angle 
       3: unit_name (String Unit)
       4: abs_value 
       5: imaginary_part_null (if the imaginary part field is empty and this pin is true, then the imaginary part is supposed to be 0 (default is false))

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sweeping_phase")
    >>> op_way2 = core.operators.math.sweeping_phase()
    """
    return _SweepingPhase()

#internal name: sin
#scripting name: sin
def _get_input_spec_sin(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inputs_dict_sin = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_sin
    else:
        return inputs_dict_sin[pin]

def _get_output_spec_sin(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sin = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_sin
    else:
        return outputs_dict_sin[pin]

class _InputSpecSin(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_sin(), op)
        self.field = Input(_get_input_spec_sin(0), 0, op, -1) 

class _OutputSpecSin(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_sin(), op)
        self.field = Output(_get_output_spec_sin(0), 0, op) 

class _Sin(_Operator):
    """Operator's description:
    Internal name is "sin"
    Scripting name is "sin"

    Description: Computes element-wise sin(field[i]).

    Input list: 
       0: field 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sin")
    >>> op_way2 = core.operators.math.sin()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("sin")
        self.inputs = _InputSpecSin(self)
        self.outputs = _OutputSpecSin(self)

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

def sin():
    """Operator's description:
    Internal name is "sin"
    Scripting name is "sin"

    Description: Computes element-wise sin(field[i]).

    Input list: 
       0: field 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sin")
    >>> op_way2 = core.operators.math.sin()
    """
    return _Sin()

#internal name: cos
#scripting name: cos
def _get_input_spec_cos(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_cos = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_cos
    else:
        return inputs_dict_cos[pin]

def _get_output_spec_cos(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_cos = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cos
    else:
        return outputs_dict_cos[pin]

class _InputSpecCos(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cos(), op)
        self.field = Input(_get_input_spec_cos(0), 0, op, -1) 

class _OutputSpecCos(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cos(), op)
        self.field = Output(_get_output_spec_cos(0), 0, op) 

class _Cos(_Operator):
    """Operator's description:
    Internal name is "cos"
    Scripting name is "cos"

    Description: Computes element-wise cos(field[i]).

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cos")
    >>> op_way2 = core.operators.math.cos()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cos")
        self.inputs = _InputSpecCos(self)
        self.outputs = _OutputSpecCos(self)

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

def cos():
    """Operator's description:
    Internal name is "cos"
    Scripting name is "cos"

    Description: Computes element-wise cos(field[i]).

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cos")
    >>> op_way2 = core.operators.math.cos()
    """
    return _Cos()

#internal name: cos_fc
#scripting name: cos_fc
def _get_input_spec_cos_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_cos_fc = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_cos_fc
    else:
        return inputs_dict_cos_fc[pin]

def _get_output_spec_cos_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cos_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cos_fc
    else:
        return outputs_dict_cos_fc[pin]

class _InputSpecCosFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cos_fc(), op)
        self.fields_container = Input(_get_input_spec_cos_fc(0), 0, op, -1) 

class _OutputSpecCosFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cos_fc(), op)
        self.fields_container = Output(_get_output_spec_cos_fc(0), 0, op) 

class _CosFc(_Operator):
    """Operator's description:
    Internal name is "cos_fc"
    Scripting name is "cos_fc"

    Description: Computes element-wise cos(field[i]).

    Input list: 
       0: fields_container (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cos_fc")
    >>> op_way2 = core.operators.math.cos_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cos_fc")
        self.inputs = _InputSpecCosFc(self)
        self.outputs = _OutputSpecCosFc(self)

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

def cos_fc():
    """Operator's description:
    Internal name is "cos_fc"
    Scripting name is "cos_fc"

    Description: Computes element-wise cos(field[i]).

    Input list: 
       0: fields_container (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cos_fc")
    >>> op_way2 = core.operators.math.cos_fc()
    """
    return _CosFc()

#internal name: sweeping_phase_fc
#scripting name: sweeping_phase_fc
def _get_input_spec_sweeping_phase_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "angle", type_names = ["double"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = False, document = """String Unit""")
    inpin4 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = False, document = """""")
    inputs_dict_sweeping_phase_fc = { 
        0 : inpin0,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_sweeping_phase_fc
    else:
        return inputs_dict_sweeping_phase_fc[pin]

def _get_output_spec_sweeping_phase_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sweeping_phase_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_sweeping_phase_fc
    else:
        return outputs_dict_sweeping_phase_fc[pin]

class _InputSpecSweepingPhaseFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_sweeping_phase_fc(), op)
        self.fields_container = Input(_get_input_spec_sweeping_phase_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_sweeping_phase_fc(), op)
        self.angle = Input(_get_input_spec_sweeping_phase_fc(2), 2, op, -1) 
        super().__init__(_get_input_spec_sweeping_phase_fc(), op)
        self.unit_name = Input(_get_input_spec_sweeping_phase_fc(3), 3, op, -1) 
        super().__init__(_get_input_spec_sweeping_phase_fc(), op)
        self.abs_value = Input(_get_input_spec_sweeping_phase_fc(4), 4, op, -1) 

class _OutputSpecSweepingPhaseFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_sweeping_phase_fc(), op)
        self.fields_container = Output(_get_output_spec_sweeping_phase_fc(0), 0, op) 

class _SweepingPhaseFc(_Operator):
    """Operator's description:
    Internal name is "sweeping_phase_fc"
    Scripting name is "sweeping_phase_fc"

    Description: Shift the phase of all the corresponding real and imaginary fields of a fields container for a given angle (in 2) of unit (in 4).

    Input list: 
       0: fields_container 
       2: angle 
       3: unit_name (String Unit)
       4: abs_value 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sweeping_phase_fc")
    >>> op_way2 = core.operators.math.sweeping_phase_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("sweeping_phase_fc")
        self.inputs = _InputSpecSweepingPhaseFc(self)
        self.outputs = _OutputSpecSweepingPhaseFc(self)

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

def sweeping_phase_fc():
    """Operator's description:
    Internal name is "sweeping_phase_fc"
    Scripting name is "sweeping_phase_fc"

    Description: Shift the phase of all the corresponding real and imaginary fields of a fields container for a given angle (in 2) of unit (in 4).

    Input list: 
       0: fields_container 
       2: angle 
       3: unit_name (String Unit)
       4: abs_value 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sweeping_phase_fc")
    >>> op_way2 = core.operators.math.sweeping_phase_fc()
    """
    return _SweepingPhaseFc()

#internal name: sqr
#scripting name: sqr
def _get_input_spec_sqr(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqr = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_sqr
    else:
        return inputs_dict_sqr[pin]

def _get_output_spec_sqr(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sqr = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_sqr
    else:
        return outputs_dict_sqr[pin]

class _InputSpecSqr(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_sqr(), op)
        self.field = Input(_get_input_spec_sqr(0), 0, op, -1) 

class _OutputSpecSqr(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_sqr(), op)
        self.field = Output(_get_output_spec_sqr(0), 0, op) 

class _Sqr(_Operator):
    """Operator's description:
    Internal name is "sqr"
    Scripting name is "sqr"

    Description: Computes element-wise field[i]^2.

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sqr")
    >>> op_way2 = core.operators.math.sqr()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("sqr")
        self.inputs = _InputSpecSqr(self)
        self.outputs = _OutputSpecSqr(self)

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

def sqr():
    """Operator's description:
    Internal name is "sqr"
    Scripting name is "sqr"

    Description: Computes element-wise field[i]^2.

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sqr")
    >>> op_way2 = core.operators.math.sqr()
    """
    return _Sqr()

#internal name: CplxOp
#scripting name: linear_combination
def _get_input_spec_linear_combination(pin = None):
    inpin0 = _PinSpecification(name = "a", type_names = ["double"], optional = False, document = """Double""")
    inpin1 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "b", type_names = ["double"], optional = False, document = """Double""")
    inpin4 = _PinSpecification(name = "fields_containerC", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_linear_combination = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_linear_combination
    else:
        return inputs_dict_linear_combination[pin]

def _get_output_spec_linear_combination(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_linear_combination = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_linear_combination
    else:
        return outputs_dict_linear_combination[pin]

class _InputSpecLinearCombination(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_linear_combination(), op)
        self.a = Input(_get_input_spec_linear_combination(0), 0, op, -1) 
        super().__init__(_get_input_spec_linear_combination(), op)
        self.fields_containerA = Input(_get_input_spec_linear_combination(1), 1, op, -1) 
        super().__init__(_get_input_spec_linear_combination(), op)
        self.fields_containerB = Input(_get_input_spec_linear_combination(2), 2, op, -1) 
        super().__init__(_get_input_spec_linear_combination(), op)
        self.b = Input(_get_input_spec_linear_combination(3), 3, op, -1) 
        super().__init__(_get_input_spec_linear_combination(), op)
        self.fields_containerC = Input(_get_input_spec_linear_combination(4), 4, op, -1) 

class _OutputSpecLinearCombination(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_linear_combination(), op)
        self.fields_container = Output(_get_output_spec_linear_combination(0), 0, op) 

class _LinearCombination(_Operator):
    """Operator's description:
    Internal name is "CplxOp"
    Scripting name is "linear_combination"

    Description: Computes aXY + bZ where a,b (in 0, in 3) are scalar and X,Y,Z (in 1,2,4) are complex numbers.

    Input list: 
       0: a (Double)
       1: fields_containerA 
       2: fields_containerB 
       3: b (Double)
       4: fields_containerC 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("CplxOp")
    >>> op_way2 = core.operators.math.linear_combination()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("CplxOp")
        self.inputs = _InputSpecLinearCombination(self)
        self.outputs = _OutputSpecLinearCombination(self)

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

def linear_combination():
    """Operator's description:
    Internal name is "CplxOp"
    Scripting name is "linear_combination"

    Description: Computes aXY + bZ where a,b (in 0, in 3) are scalar and X,Y,Z (in 1,2,4) are complex numbers.

    Input list: 
       0: a (Double)
       1: fields_containerA 
       2: fields_containerB 
       3: b (Double)
       4: fields_containerC 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("CplxOp")
    >>> op_way2 = core.operators.math.linear_combination()
    """
    return _LinearCombination()

#internal name: sqr_fc
#scripting name: sqr_fc
def _get_input_spec_sqr_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqr_fc = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_sqr_fc
    else:
        return inputs_dict_sqr_fc[pin]

def _get_output_spec_sqr_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sqr_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_sqr_fc
    else:
        return outputs_dict_sqr_fc[pin]

class _InputSpecSqrFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_sqr_fc(), op)
        self.fields_container = Input(_get_input_spec_sqr_fc(0), 0, op, -1) 

class _OutputSpecSqrFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_sqr_fc(), op)
        self.fields_container = Output(_get_output_spec_sqr_fc(0), 0, op) 

class _SqrFc(_Operator):
    """Operator's description:
    Internal name is "sqr_fc"
    Scripting name is "sqr_fc"

    Description: Computes element-wise field[i]^2.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sqr_fc")
    >>> op_way2 = core.operators.math.sqr_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("sqr_fc")
        self.inputs = _InputSpecSqrFc(self)
        self.outputs = _OutputSpecSqrFc(self)

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

def sqr_fc():
    """Operator's description:
    Internal name is "sqr_fc"
    Scripting name is "sqr_fc"

    Description: Computes element-wise field[i]^2.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sqr_fc")
    >>> op_way2 = core.operators.math.sqr_fc()
    """
    return _SqrFc()

#internal name: sqrt
#scripting name: sqrt
def _get_input_spec_sqrt(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqrt = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_sqrt
    else:
        return inputs_dict_sqrt[pin]

def _get_output_spec_sqrt(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sqrt = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_sqrt
    else:
        return outputs_dict_sqrt[pin]

class _InputSpecSqrt(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_sqrt(), op)
        self.field = Input(_get_input_spec_sqrt(0), 0, op, -1) 

class _OutputSpecSqrt(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_sqrt(), op)
        self.field = Output(_get_output_spec_sqrt(0), 0, op) 

class _Sqrt(_Operator):
    """Operator's description:
    Internal name is "sqrt"
    Scripting name is "sqrt"

    Description: Computes element-wise sqrt(field1).

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sqrt")
    >>> op_way2 = core.operators.math.sqrt()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("sqrt")
        self.inputs = _InputSpecSqrt(self)
        self.outputs = _OutputSpecSqrt(self)

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

def sqrt():
    """Operator's description:
    Internal name is "sqrt"
    Scripting name is "sqrt"

    Description: Computes element-wise sqrt(field1).

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sqrt")
    >>> op_way2 = core.operators.math.sqrt()
    """
    return _Sqrt()

#internal name: norm
#scripting name: norm
def _get_input_spec_norm(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_norm = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_norm
    else:
        return inputs_dict_norm[pin]

def _get_output_spec_norm(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_norm = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_norm
    else:
        return outputs_dict_norm[pin]

class _InputSpecNorm(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_norm(), op)
        self.field = Input(_get_input_spec_norm(0), 0, op, -1) 

class _OutputSpecNorm(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_norm(), op)
        self.field = Output(_get_output_spec_norm(0), 0, op) 

class _Norm(_Operator):
    """Operator's description:
    Internal name is "norm"
    Scripting name is "norm"

    Description: Computes the element-wise L2 norm of the field elementary data.

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("norm")
    >>> op_way2 = core.operators.math.norm()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("norm")
        self.inputs = _InputSpecNorm(self)
        self.outputs = _OutputSpecNorm(self)

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

def norm():
    """Operator's description:
    Internal name is "norm"
    Scripting name is "norm"

    Description: Computes the element-wise L2 norm of the field elementary data.

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("norm")
    >>> op_way2 = core.operators.math.norm()
    """
    return _Norm()

#internal name: sqrt_fc
#scripting name: sqrt_fc
def _get_input_spec_sqrt_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqrt_fc = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_sqrt_fc
    else:
        return inputs_dict_sqrt_fc[pin]

def _get_output_spec_sqrt_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sqrt_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_sqrt_fc
    else:
        return outputs_dict_sqrt_fc[pin]

class _InputSpecSqrtFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_sqrt_fc(), op)
        self.fields_container = Input(_get_input_spec_sqrt_fc(0), 0, op, -1) 

class _OutputSpecSqrtFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_sqrt_fc(), op)
        self.fields_container = Output(_get_output_spec_sqrt_fc(0), 0, op) 

class _SqrtFc(_Operator):
    """Operator's description:
    Internal name is "sqrt_fc"
    Scripting name is "sqrt_fc"

    Description: Computes element-wise sqrt(field1).

    Input list: 
       0: fields_container (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sqrt_fc")
    >>> op_way2 = core.operators.math.sqrt_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("sqrt_fc")
        self.inputs = _InputSpecSqrtFc(self)
        self.outputs = _OutputSpecSqrtFc(self)

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

def sqrt_fc():
    """Operator's description:
    Internal name is "sqrt_fc"
    Scripting name is "sqrt_fc"

    Description: Computes element-wise sqrt(field1).

    Input list: 
       0: fields_container (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("sqrt_fc")
    >>> op_way2 = core.operators.math.sqrt_fc()
    """
    return _SqrtFc()

#internal name: norm_fc
#scripting name: norm_fc
def _get_input_spec_norm_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_norm_fc = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_norm_fc
    else:
        return inputs_dict_norm_fc[pin]

def _get_output_spec_norm_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_norm_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_norm_fc
    else:
        return outputs_dict_norm_fc[pin]

class _InputSpecNormFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_norm_fc(), op)
        self.fields_container = Input(_get_input_spec_norm_fc(0), 0, op, -1) 

class _OutputSpecNormFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_norm_fc(), op)
        self.fields_container = Output(_get_output_spec_norm_fc(0), 0, op) 

class _NormFc(_Operator):
    """Operator's description:
    Internal name is "norm_fc"
    Scripting name is "norm_fc"

    Description: Computes the element-wise L2 norm of the field elementary data. This process is applied on eah field of the input fields container.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("norm_fc")
    >>> op_way2 = core.operators.math.norm_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("norm_fc")
        self.inputs = _InputSpecNormFc(self)
        self.outputs = _OutputSpecNormFc(self)

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

def norm_fc():
    """Operator's description:
    Internal name is "norm_fc"
    Scripting name is "norm_fc"

    Description: Computes the element-wise L2 norm of the field elementary data. This process is applied on eah field of the input fields container.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("norm_fc")
    >>> op_way2 = core.operators.math.norm_fc()
    """
    return _NormFc()

#internal name: component_wise_divide
#scripting name: component_wise_divide
def _get_input_spec_component_wise_divide(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_component_wise_divide = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_component_wise_divide
    else:
        return inputs_dict_component_wise_divide[pin]

def _get_output_spec_component_wise_divide(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_component_wise_divide = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_component_wise_divide
    else:
        return outputs_dict_component_wise_divide[pin]

class _InputSpecComponentWiseDivide(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_component_wise_divide(), op)
        self.fieldA = Input(_get_input_spec_component_wise_divide(0), 0, op, -1) 
        super().__init__(_get_input_spec_component_wise_divide(), op)
        self.fieldB = Input(_get_input_spec_component_wise_divide(1), 1, op, -1) 

class _OutputSpecComponentWiseDivide(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_component_wise_divide(), op)
        self.field = Output(_get_output_spec_component_wise_divide(0), 0, op) 

class _ComponentWiseDivide(_Operator):
    """Operator's description:
    Internal name is "component_wise_divide"
    Scripting name is "component_wise_divide"

    Description: Computes component-wise fraction between two fields of same dimensionality. If one field's scoping has overall location, then these field's values are applied on the entire other field.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("component_wise_divide")
    >>> op_way2 = core.operators.math.component_wise_divide()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("component_wise_divide")
        self.inputs = _InputSpecComponentWiseDivide(self)
        self.outputs = _OutputSpecComponentWiseDivide(self)

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

def component_wise_divide():
    """Operator's description:
    Internal name is "component_wise_divide"
    Scripting name is "component_wise_divide"

    Description: Computes component-wise fraction between two fields of same dimensionality. If one field's scoping has overall location, then these field's values are applied on the entire other field.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("component_wise_divide")
    >>> op_way2 = core.operators.math.component_wise_divide()
    """
    return _ComponentWiseDivide()

#internal name: component_wise_divide_fc
#scripting name: component_wise_divide_fc
def _get_input_spec_component_wise_divide_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_component_wise_divide_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_component_wise_divide_fc
    else:
        return inputs_dict_component_wise_divide_fc[pin]

def _get_output_spec_component_wise_divide_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_component_wise_divide_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_component_wise_divide_fc
    else:
        return outputs_dict_component_wise_divide_fc[pin]

class _InputSpecComponentWiseDivideFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_component_wise_divide_fc(), op)
        self.fields_containerA = Input(_get_input_spec_component_wise_divide_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_component_wise_divide_fc(), op)
        self.fields_containerB = Input(_get_input_spec_component_wise_divide_fc(1), 1, op, -1) 

class _OutputSpecComponentWiseDivideFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_component_wise_divide_fc(), op)
        self.fields_container = Output(_get_output_spec_component_wise_divide_fc(0), 0, op) 

class _ComponentWiseDivideFc(_Operator):
    """Operator's description:
    Internal name is "component_wise_divide_fc"
    Scripting name is "component_wise_divide_fc"

    Description: For every two fields with the same label space (from the two input fields containers), computes component-wise fraction between two fields of same dimensionality. If one field's scoping has overall location, then these field's values are applied on the entire other field.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("component_wise_divide_fc")
    >>> op_way2 = core.operators.math.component_wise_divide_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("component_wise_divide_fc")
        self.inputs = _InputSpecComponentWiseDivideFc(self)
        self.outputs = _OutputSpecComponentWiseDivideFc(self)

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

def component_wise_divide_fc():
    """Operator's description:
    Internal name is "component_wise_divide_fc"
    Scripting name is "component_wise_divide_fc"

    Description: For every two fields with the same label space (from the two input fields containers), computes component-wise fraction between two fields of same dimensionality. If one field's scoping has overall location, then these field's values are applied on the entire other field.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("component_wise_divide_fc")
    >>> op_way2 = core.operators.math.component_wise_divide_fc()
    """
    return _ComponentWiseDivideFc()

#internal name: kronecker_prod
#scripting name: kronecker_prod
def _get_input_spec_kronecker_prod(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_kronecker_prod = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_kronecker_prod
    else:
        return inputs_dict_kronecker_prod[pin]

def _get_output_spec_kronecker_prod(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_kronecker_prod = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_kronecker_prod
    else:
        return outputs_dict_kronecker_prod[pin]

class _InputSpecKroneckerProd(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_kronecker_prod(), op)
        self.fieldA = Input(_get_input_spec_kronecker_prod(0), 0, op, -1) 
        super().__init__(_get_input_spec_kronecker_prod(), op)
        self.fieldB = Input(_get_input_spec_kronecker_prod(1), 1, op, -1) 

class _OutputSpecKroneckerProd(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_kronecker_prod(), op)
        self.field = Output(_get_output_spec_kronecker_prod(0), 0, op) 

class _KroneckerProd(_Operator):
    """Operator's description:
    Internal name is "kronecker_prod"
    Scripting name is "kronecker_prod"

    Description: Computes element-wise Kronecker product between two tensor fields.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("kronecker_prod")
    >>> op_way2 = core.operators.math.kronecker_prod()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("kronecker_prod")
        self.inputs = _InputSpecKroneckerProd(self)
        self.outputs = _OutputSpecKroneckerProd(self)

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

def kronecker_prod():
    """Operator's description:
    Internal name is "kronecker_prod"
    Scripting name is "kronecker_prod"

    Description: Computes element-wise Kronecker product between two tensor fields.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("kronecker_prod")
    >>> op_way2 = core.operators.math.kronecker_prod()
    """
    return _KroneckerProd()

#internal name: realP_part
#scripting name: real_part
def _get_input_spec_real_part(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_real_part = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_real_part
    else:
        return inputs_dict_real_part[pin]

def _get_output_spec_real_part(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_real_part = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_real_part
    else:
        return outputs_dict_real_part[pin]

class _InputSpecRealPart(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_real_part(), op)
        self.fields_container = Input(_get_input_spec_real_part(0), 0, op, -1) 

class _OutputSpecRealPart(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_real_part(), op)
        self.fields_container = Output(_get_output_spec_real_part(0), 0, op) 

class _RealPart(_Operator):
    """Operator's description:
    Internal name is "realP_part"
    Scripting name is "real_part"

    Description: Extracts element-wise real part of field containers containing complex fields.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("realP_part")
    >>> op_way2 = core.operators.math.real_part()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("realP_part")
        self.inputs = _InputSpecRealPart(self)
        self.outputs = _OutputSpecRealPart(self)

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

def real_part():
    """Operator's description:
    Internal name is "realP_part"
    Scripting name is "real_part"

    Description: Extracts element-wise real part of field containers containing complex fields.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("realP_part")
    >>> op_way2 = core.operators.math.real_part()
    """
    return _RealPart()

#internal name: conjugate
#scripting name: conjugate
def _get_input_spec_conjugate(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_conjugate = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_conjugate
    else:
        return inputs_dict_conjugate[pin]

def _get_output_spec_conjugate(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_conjugate = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_conjugate
    else:
        return outputs_dict_conjugate[pin]

class _InputSpecConjugate(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_conjugate(), op)
        self.fields_container = Input(_get_input_spec_conjugate(0), 0, op, -1) 

class _OutputSpecConjugate(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_conjugate(), op)
        self.fields_container = Output(_get_output_spec_conjugate(0), 0, op) 

class _Conjugate(_Operator):
    """Operator's description:
    Internal name is "conjugate"
    Scripting name is "conjugate"

    Description: Computes element-wise conjugate of field containers containing complex fields.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("conjugate")
    >>> op_way2 = core.operators.math.conjugate()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("conjugate")
        self.inputs = _InputSpecConjugate(self)
        self.outputs = _OutputSpecConjugate(self)

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

def conjugate():
    """Operator's description:
    Internal name is "conjugate"
    Scripting name is "conjugate"

    Description: Computes element-wise conjugate of field containers containing complex fields.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("conjugate")
    >>> op_way2 = core.operators.math.conjugate()
    """
    return _Conjugate()

#internal name: img_part
#scripting name: img_part
def _get_input_spec_img_part(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_img_part = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_img_part
    else:
        return inputs_dict_img_part[pin]

def _get_output_spec_img_part(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_img_part = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_img_part
    else:
        return outputs_dict_img_part[pin]

class _InputSpecImgPart(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_img_part(), op)
        self.fields_container = Input(_get_input_spec_img_part(0), 0, op, -1) 

class _OutputSpecImgPart(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_img_part(), op)
        self.fields_container = Output(_get_output_spec_img_part(0), 0, op) 

class _ImgPart(_Operator):
    """Operator's description:
    Internal name is "img_part"
    Scripting name is "img_part"

    Description: Extracts element-wise imaginary part of field containers containing complex fields.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("img_part")
    >>> op_way2 = core.operators.math.img_part()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("img_part")
        self.inputs = _InputSpecImgPart(self)
        self.outputs = _OutputSpecImgPart(self)

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

def img_part():
    """Operator's description:
    Internal name is "img_part"
    Scripting name is "img_part"

    Description: Extracts element-wise imaginary part of field containers containing complex fields.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("img_part")
    >>> op_way2 = core.operators.math.img_part()
    """
    return _ImgPart()

#internal name: amplitude
#scripting name: amplitude
def _get_input_spec_amplitude(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_amplitude = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_amplitude
    else:
        return inputs_dict_amplitude[pin]

def _get_output_spec_amplitude(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_amplitude = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_amplitude
    else:
        return outputs_dict_amplitude[pin]

class _InputSpecAmplitude(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_amplitude(), op)
        self.fieldA = Input(_get_input_spec_amplitude(0), 0, op, -1) 
        super().__init__(_get_input_spec_amplitude(), op)
        self.fieldB = Input(_get_input_spec_amplitude(1), 1, op, -1) 

class _OutputSpecAmplitude(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_amplitude(), op)
        self.field = Output(_get_output_spec_amplitude(0), 0, op) 

class _Amplitude(_Operator):
    """Operator's description:
    Internal name is "amplitude"
    Scripting name is "amplitude"

    Description: Computes amplitude of a real and an imaginary field.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("amplitude")
    >>> op_way2 = core.operators.math.amplitude()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("amplitude")
        self.inputs = _InputSpecAmplitude(self)
        self.outputs = _OutputSpecAmplitude(self)

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

def amplitude():
    """Operator's description:
    Internal name is "amplitude"
    Scripting name is "amplitude"

    Description: Computes amplitude of a real and an imaginary field.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("amplitude")
    >>> op_way2 = core.operators.math.amplitude()
    """
    return _Amplitude()

#internal name: cplx_add
#scripting name: cplx_add
def _get_input_spec_cplx_add(pin = None):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_add = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_cplx_add
    else:
        return inputs_dict_cplx_add[pin]

def _get_output_spec_cplx_add(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_add = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cplx_add
    else:
        return outputs_dict_cplx_add[pin]

class _InputSpecCplxAdd(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cplx_add(), op)
        self.fields_containerA = Input(_get_input_spec_cplx_add(0), 0, op, -1) 
        super().__init__(_get_input_spec_cplx_add(), op)
        self.fields_containerB = Input(_get_input_spec_cplx_add(1), 1, op, -1) 

class _OutputSpecCplxAdd(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cplx_add(), op)
        self.fields_container = Output(_get_output_spec_cplx_add(0), 0, op) 

class _CplxAdd(_Operator):
    """Operator's description:
    Internal name is "cplx_add"
    Scripting name is "cplx_add"

    Description: Computes addition between two field containers containing complex fields.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cplx_add")
    >>> op_way2 = core.operators.math.cplx_add()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cplx_add")
        self.inputs = _InputSpecCplxAdd(self)
        self.outputs = _OutputSpecCplxAdd(self)

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

def cplx_add():
    """Operator's description:
    Internal name is "cplx_add"
    Scripting name is "cplx_add"

    Description: Computes addition between two field containers containing complex fields.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cplx_add")
    >>> op_way2 = core.operators.math.cplx_add()
    """
    return _CplxAdd()

#internal name: cplx_dot
#scripting name: cplx_dot
def _get_input_spec_cplx_dot(pin = None):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_dot = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_cplx_dot
    else:
        return inputs_dict_cplx_dot[pin]

def _get_output_spec_cplx_dot(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_dot = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cplx_dot
    else:
        return outputs_dict_cplx_dot[pin]

class _InputSpecCplxDot(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cplx_dot(), op)
        self.fields_containerA = Input(_get_input_spec_cplx_dot(0), 0, op, -1) 
        super().__init__(_get_input_spec_cplx_dot(), op)
        self.fields_containerB = Input(_get_input_spec_cplx_dot(1), 1, op, -1) 

class _OutputSpecCplxDot(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cplx_dot(), op)
        self.fields_container = Output(_get_output_spec_cplx_dot(0), 0, op) 

class _CplxDot(_Operator):
    """Operator's description:
    Internal name is "cplx_dot"
    Scripting name is "cplx_dot"

    Description: Computes product between two field containers containing complex fields.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cplx_dot")
    >>> op_way2 = core.operators.math.cplx_dot()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cplx_dot")
        self.inputs = _InputSpecCplxDot(self)
        self.outputs = _OutputSpecCplxDot(self)

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

def cplx_dot():
    """Operator's description:
    Internal name is "cplx_dot"
    Scripting name is "cplx_dot"

    Description: Computes product between two field containers containing complex fields.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cplx_dot")
    >>> op_way2 = core.operators.math.cplx_dot()
    """
    return _CplxDot()

#internal name: cplx_divide
#scripting name: cplx_divide
def _get_input_spec_cplx_divide(pin = None):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_divide = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_cplx_divide
    else:
        return inputs_dict_cplx_divide[pin]

def _get_output_spec_cplx_divide(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_divide = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cplx_divide
    else:
        return outputs_dict_cplx_divide[pin]

class _InputSpecCplxDivide(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cplx_divide(), op)
        self.fields_containerA = Input(_get_input_spec_cplx_divide(0), 0, op, -1) 
        super().__init__(_get_input_spec_cplx_divide(), op)
        self.fields_containerB = Input(_get_input_spec_cplx_divide(1), 1, op, -1) 

class _OutputSpecCplxDivide(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cplx_divide(), op)
        self.fields_container = Output(_get_output_spec_cplx_divide(0), 0, op) 

class _CplxDivide(_Operator):
    """Operator's description:
    Internal name is "cplx_divide"
    Scripting name is "cplx_divide"

    Description: Computes division between two field containers containing complex fields.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cplx_divide")
    >>> op_way2 = core.operators.math.cplx_divide()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cplx_divide")
        self.inputs = _InputSpecCplxDivide(self)
        self.outputs = _OutputSpecCplxDivide(self)

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

def cplx_divide():
    """Operator's description:
    Internal name is "cplx_divide"
    Scripting name is "cplx_divide"

    Description: Computes division between two field containers containing complex fields.

    Input list: 
       0: fields_containerA 
       1: fields_containerB 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cplx_divide")
    >>> op_way2 = core.operators.math.cplx_divide()
    """
    return _CplxDivide()

#internal name: dot
#scripting name: dot
def _get_input_spec_dot(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_dot = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_dot
    else:
        return inputs_dict_dot[pin]

def _get_output_spec_dot(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_dot = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_dot
    else:
        return outputs_dict_dot[pin]

class _InputSpecDot(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_dot(), op)
        self.fieldA = Input(_get_input_spec_dot(0), 0, op, -1) 
        super().__init__(_get_input_spec_dot(), op)
        self.fieldB = Input(_get_input_spec_dot(1), 1, op, -1) 

class _OutputSpecDot(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_dot(), op)
        self.field = Output(_get_output_spec_dot(0), 0, op) 

class _Dot(_Operator):
    """Operator's description:
    Internal name is "dot"
    Scripting name is "dot"

    Description: Computes element-wise dot product between two vector fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("dot")
    >>> op_way2 = core.operators.math.dot()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("dot")
        self.inputs = _InputSpecDot(self)
        self.outputs = _OutputSpecDot(self)

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

def dot():
    """Operator's description:
    Internal name is "dot"
    Scripting name is "dot"

    Description: Computes element-wise dot product between two vector fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("dot")
    >>> op_way2 = core.operators.math.dot()
    """
    return _Dot()

#internal name: cplx_derive
#scripting name: cplx_derive
def _get_input_spec_cplx_derive(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_derive = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_cplx_derive
    else:
        return inputs_dict_cplx_derive[pin]

def _get_output_spec_cplx_derive(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_derive = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cplx_derive
    else:
        return outputs_dict_cplx_derive[pin]

class _InputSpecCplxDerive(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cplx_derive(), op)
        self.fields_container = Input(_get_input_spec_cplx_derive(0), 0, op, -1) 

class _OutputSpecCplxDerive(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cplx_derive(), op)
        self.fields_container = Output(_get_output_spec_cplx_derive(0), 0, op) 

class _CplxDerive(_Operator):
    """Operator's description:
    Internal name is "cplx_derive"
    Scripting name is "cplx_derive"

    Description: Derive field containers containing complex fields.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cplx_derive")
    >>> op_way2 = core.operators.math.cplx_derive()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cplx_derive")
        self.inputs = _InputSpecCplxDerive(self)
        self.outputs = _OutputSpecCplxDerive(self)

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

def cplx_derive():
    """Operator's description:
    Internal name is "cplx_derive"
    Scripting name is "cplx_derive"

    Description: Derive field containers containing complex fields.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cplx_derive")
    >>> op_way2 = core.operators.math.cplx_derive()
    """
    return _CplxDerive()

#internal name: polar_to_cplx
#scripting name: polar_to_cplx
def _get_input_spec_polar_to_cplx(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_polar_to_cplx = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_polar_to_cplx
    else:
        return inputs_dict_polar_to_cplx[pin]

def _get_output_spec_polar_to_cplx(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_polar_to_cplx = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_polar_to_cplx
    else:
        return outputs_dict_polar_to_cplx[pin]

class _InputSpecPolarToCplx(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_polar_to_cplx(), op)
        self.fields_container = Input(_get_input_spec_polar_to_cplx(0), 0, op, -1) 

class _OutputSpecPolarToCplx(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_polar_to_cplx(), op)
        self.fields_container = Output(_get_output_spec_polar_to_cplx(0), 0, op) 

class _PolarToCplx(_Operator):
    """Operator's description:
    Internal name is "polar_to_cplx"
    Scripting name is "polar_to_cplx"

    Description: Convert complex number from polar form to complex.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("polar_to_cplx")
    >>> op_way2 = core.operators.math.polar_to_cplx()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("polar_to_cplx")
        self.inputs = _InputSpecPolarToCplx(self)
        self.outputs = _OutputSpecPolarToCplx(self)

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

def polar_to_cplx():
    """Operator's description:
    Internal name is "polar_to_cplx"
    Scripting name is "polar_to_cplx"

    Description: Convert complex number from polar form to complex.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("polar_to_cplx")
    >>> op_way2 = core.operators.math.polar_to_cplx()
    """
    return _PolarToCplx()

#internal name: modulus
#scripting name: modulus
def _get_input_spec_modulus(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_modulus = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_modulus
    else:
        return inputs_dict_modulus[pin]

def _get_output_spec_modulus(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_modulus = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_modulus
    else:
        return outputs_dict_modulus[pin]

class _InputSpecModulus(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_modulus(), op)
        self.fields_container = Input(_get_input_spec_modulus(0), 0, op, -1) 

class _OutputSpecModulus(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_modulus(), op)
        self.fields_container = Output(_get_output_spec_modulus(0), 0, op) 

class _Modulus(_Operator):
    """Operator's description:
    Internal name is "modulus"
    Scripting name is "modulus"

    Description: Computes element-wise modulus of field containers containing complex fields.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("modulus")
    >>> op_way2 = core.operators.math.modulus()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("modulus")
        self.inputs = _InputSpecModulus(self)
        self.outputs = _OutputSpecModulus(self)

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

def modulus():
    """Operator's description:
    Internal name is "modulus"
    Scripting name is "modulus"

    Description: Computes element-wise modulus of field containers containing complex fields.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("modulus")
    >>> op_way2 = core.operators.math.modulus()
    """
    return _Modulus()

#internal name: accumulate_fc
#scripting name: accumulate_fc
def _get_input_spec_accumulate_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_accumulate_fc = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_accumulate_fc
    else:
        return inputs_dict_accumulate_fc[pin]

def _get_output_spec_accumulate_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_accumulate_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_accumulate_fc
    else:
        return outputs_dict_accumulate_fc[pin]

class _InputSpecAccumulateFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_accumulate_fc(), op)
        self.fields_container = Input(_get_input_spec_accumulate_fc(0), 0, op, -1) 

class _OutputSpecAccumulateFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_accumulate_fc(), op)
        self.fields_container = Output(_get_output_spec_accumulate_fc(0), 0, op) 

class _AccumulateFc(_Operator):
    """Operator's description:
    Internal name is "accumulate_fc"
    Scripting name is "accumulate_fc"

    Description: Sum all the elementary data of a field to get one elementary data at the end.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("accumulate_fc")
    >>> op_way2 = core.operators.math.accumulate_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("accumulate_fc")
        self.inputs = _InputSpecAccumulateFc(self)
        self.outputs = _OutputSpecAccumulateFc(self)

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

def accumulate_fc():
    """Operator's description:
    Internal name is "accumulate_fc"
    Scripting name is "accumulate_fc"

    Description: Sum all the elementary data of a field to get one elementary data at the end.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("accumulate_fc")
    >>> op_way2 = core.operators.math.accumulate_fc()
    """
    return _AccumulateFc()

#internal name: generalized_inner_product
#scripting name: generalized_inner_product
def _get_input_spec_generalized_inner_product(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_generalized_inner_product = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_generalized_inner_product
    else:
        return inputs_dict_generalized_inner_product[pin]

def _get_output_spec_generalized_inner_product(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_generalized_inner_product = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_generalized_inner_product
    else:
        return outputs_dict_generalized_inner_product[pin]

class _InputSpecGeneralizedInnerProduct(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_generalized_inner_product(), op)
        self.fieldA = Input(_get_input_spec_generalized_inner_product(0), 0, op, -1) 
        super().__init__(_get_input_spec_generalized_inner_product(), op)
        self.fieldB = Input(_get_input_spec_generalized_inner_product(1), 1, op, -1) 

class _OutputSpecGeneralizedInnerProduct(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_generalized_inner_product(), op)
        self.field = Output(_get_output_spec_generalized_inner_product(0), 0, op) 

class _GeneralizedInnerProduct(_Operator):
    """Operator's description:
    Internal name is "generalized_inner_product"
    Scripting name is "generalized_inner_product"

    Description: Computes a general notion of inner product between two fields of possibly different dimensionality.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("generalized_inner_product")
    >>> op_way2 = core.operators.math.generalized_inner_product()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("generalized_inner_product")
        self.inputs = _InputSpecGeneralizedInnerProduct(self)
        self.outputs = _OutputSpecGeneralizedInnerProduct(self)

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

def generalized_inner_product():
    """Operator's description:
    Internal name is "generalized_inner_product"
    Scripting name is "generalized_inner_product"

    Description: Computes a general notion of inner product between two fields of possibly different dimensionality.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("generalized_inner_product")
    >>> op_way2 = core.operators.math.generalized_inner_product()
    """
    return _GeneralizedInnerProduct()

#internal name: scale_by_field
#scripting name: scale_by_field
def _get_input_spec_scale_by_field(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_scale_by_field = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_scale_by_field
    else:
        return inputs_dict_scale_by_field[pin]

def _get_output_spec_scale_by_field(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_scale_by_field = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_scale_by_field
    else:
        return outputs_dict_scale_by_field[pin]

class _InputSpecScaleByField(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_scale_by_field(), op)
        self.fieldA = Input(_get_input_spec_scale_by_field(0), 0, op, -1) 
        super().__init__(_get_input_spec_scale_by_field(), op)
        self.fieldB = Input(_get_input_spec_scale_by_field(1), 1, op, -1) 

class _OutputSpecScaleByField(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_scale_by_field(), op)
        self.field = Output(_get_output_spec_scale_by_field(0), 0, op) 

class _ScaleByField(_Operator):
    """Operator's description:
    Internal name is "scale_by_field"
    Scripting name is "scale_by_field"

    Description: Scales a field (in 0) by a scalar field (in 1). If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("scale_by_field")
    >>> op_way2 = core.operators.math.scale_by_field()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("scale_by_field")
        self.inputs = _InputSpecScaleByField(self)
        self.outputs = _OutputSpecScaleByField(self)

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

def scale_by_field():
    """Operator's description:
    Internal name is "scale_by_field"
    Scripting name is "scale_by_field"

    Description: Scales a field (in 0) by a scalar field (in 1). If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("scale_by_field")
    >>> op_way2 = core.operators.math.scale_by_field()
    """
    return _ScaleByField()

#internal name: generalized_inner_product_fc
#scripting name: generalized_inner_product_fc
def _get_input_spec_generalized_inner_product_fc(pin = None):
    inpin0 = _PinSpecification(name = "field_or_fields_container_A", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "field_or_fields_container_B", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_generalized_inner_product_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_generalized_inner_product_fc
    else:
        return inputs_dict_generalized_inner_product_fc[pin]

def _get_output_spec_generalized_inner_product_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_generalized_inner_product_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_generalized_inner_product_fc
    else:
        return outputs_dict_generalized_inner_product_fc[pin]

class _InputSpecGeneralizedInnerProductFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_generalized_inner_product_fc(), op)
        self.field_or_fields_container_A = Input(_get_input_spec_generalized_inner_product_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_generalized_inner_product_fc(), op)
        self.field_or_fields_container_B = Input(_get_input_spec_generalized_inner_product_fc(1), 1, op, -1) 

class _OutputSpecGeneralizedInnerProductFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_generalized_inner_product_fc(), op)
        self.fields_container = Output(_get_output_spec_generalized_inner_product_fc(0), 0, op) 

class _GeneralizedInnerProductFc(_Operator):
    """Operator's description:
    Internal name is "generalized_inner_product_fc"
    Scripting name is "generalized_inner_product_fc"

    Description: Computes a general notion of inner product between two fields of possibly different dimensionality.

    Input list: 
       0: field_or_fields_container_A (field or fields container with only one field is expected)
       1: field_or_fields_container_B (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("generalized_inner_product_fc")
    >>> op_way2 = core.operators.math.generalized_inner_product_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("generalized_inner_product_fc")
        self.inputs = _InputSpecGeneralizedInnerProductFc(self)
        self.outputs = _OutputSpecGeneralizedInnerProductFc(self)

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

def generalized_inner_product_fc():
    """Operator's description:
    Internal name is "generalized_inner_product_fc"
    Scripting name is "generalized_inner_product_fc"

    Description: Computes a general notion of inner product between two fields of possibly different dimensionality.

    Input list: 
       0: field_or_fields_container_A (field or fields container with only one field is expected)
       1: field_or_fields_container_B (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("generalized_inner_product_fc")
    >>> op_way2 = core.operators.math.generalized_inner_product_fc()
    """
    return _GeneralizedInnerProductFc()

from . import native #native::overall_dot

#internal name: max_over_time
#scripting name: max_over_time
def _get_input_spec_max_over_time(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "angle", type_names = ["double"], optional = True, document = """Phase angle used for complex field container""")
    inpin2 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = True, document = """Phase angle unit. Default is radian.""")
    inpin3 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin4 = _PinSpecification(name = "compute_amplitude", type_names = ["bool"], optional = True, document = """Do calculate amplitude.""")
    inputs_dict_max_over_time = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_max_over_time
    else:
        return inputs_dict_max_over_time[pin]

def _get_output_spec_max_over_time(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_max_over_time = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_max_over_time
    else:
        return outputs_dict_max_over_time[pin]

class _InputSpecMaxOverTime(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_max_over_time(), op)
        self.fields_container = Input(_get_input_spec_max_over_time(0), 0, op, -1) 
        super().__init__(_get_input_spec_max_over_time(), op)
        self.angle = Input(_get_input_spec_max_over_time(1), 1, op, -1) 
        super().__init__(_get_input_spec_max_over_time(), op)
        self.unit_name = Input(_get_input_spec_max_over_time(2), 2, op, -1) 
        super().__init__(_get_input_spec_max_over_time(), op)
        self.abs_value = Input(_get_input_spec_max_over_time(3), 3, op, -1) 
        super().__init__(_get_input_spec_max_over_time(), op)
        self.compute_amplitude = Input(_get_input_spec_max_over_time(4), 4, op, -1) 

class _OutputSpecMaxOverTime(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_max_over_time(), op)
        self.field = Output(_get_output_spec_max_over_time(0), 0, op) 

class _MaxOverTime(_Operator):
    """Operator's description:
    Internal name is "max_over_time"
    Scripting name is "max_over_time"

    Description: Evaluates maximum over time/frequency.

    Input list: 
       0: fields_container 
       1: angle (Phase angle used for complex field container)
       2: unit_name (Phase angle unit. Default is radian.)
       3: abs_value (Should use absolute value.)
       4: compute_amplitude (Do calculate amplitude.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("max_over_time")
    >>> op_way2 = core.operators.math.max_over_time()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("max_over_time")
        self.inputs = _InputSpecMaxOverTime(self)
        self.outputs = _OutputSpecMaxOverTime(self)

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

def max_over_time():
    """Operator's description:
    Internal name is "max_over_time"
    Scripting name is "max_over_time"

    Description: Evaluates maximum over time/frequency.

    Input list: 
       0: fields_container 
       1: angle (Phase angle used for complex field container)
       2: unit_name (Phase angle unit. Default is radian.)
       3: abs_value (Should use absolute value.)
       4: compute_amplitude (Do calculate amplitude.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("max_over_time")
    >>> op_way2 = core.operators.math.max_over_time()
    """
    return _MaxOverTime()

#internal name: time_of_max
#scripting name: time_of_max
def _get_input_spec_time_of_max(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "angle", type_names = ["double"], optional = True, document = """Phase angle used for complex field container""")
    inpin2 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = True, document = """Phase angle unit. Default is radian.""")
    inpin3 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin4 = _PinSpecification(name = "compute_amplitude", type_names = ["bool"], optional = True, document = """Do calculate amplitude.""")
    inputs_dict_time_of_max = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_time_of_max
    else:
        return inputs_dict_time_of_max[pin]

def _get_output_spec_time_of_max(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_time_of_max = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_time_of_max
    else:
        return outputs_dict_time_of_max[pin]

class _InputSpecTimeOfMax(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_time_of_max(), op)
        self.fields_container = Input(_get_input_spec_time_of_max(0), 0, op, -1) 
        super().__init__(_get_input_spec_time_of_max(), op)
        self.angle = Input(_get_input_spec_time_of_max(1), 1, op, -1) 
        super().__init__(_get_input_spec_time_of_max(), op)
        self.unit_name = Input(_get_input_spec_time_of_max(2), 2, op, -1) 
        super().__init__(_get_input_spec_time_of_max(), op)
        self.abs_value = Input(_get_input_spec_time_of_max(3), 3, op, -1) 
        super().__init__(_get_input_spec_time_of_max(), op)
        self.compute_amplitude = Input(_get_input_spec_time_of_max(4), 4, op, -1) 

class _OutputSpecTimeOfMax(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_time_of_max(), op)
        self.field = Output(_get_output_spec_time_of_max(0), 0, op) 

class _TimeOfMax(_Operator):
    """Operator's description:
    Internal name is "time_of_max"
    Scripting name is "time_of_max"

    Description: Evaluates time/frequency of maximum.

    Input list: 
       0: fields_container 
       1: angle (Phase angle used for complex field container)
       2: unit_name (Phase angle unit. Default is radian.)
       3: abs_value (Should use absolute value.)
       4: compute_amplitude (Do calculate amplitude.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("time_of_max")
    >>> op_way2 = core.operators.math.time_of_max()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("time_of_max")
        self.inputs = _InputSpecTimeOfMax(self)
        self.outputs = _OutputSpecTimeOfMax(self)

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

def time_of_max():
    """Operator's description:
    Internal name is "time_of_max"
    Scripting name is "time_of_max"

    Description: Evaluates time/frequency of maximum.

    Input list: 
       0: fields_container 
       1: angle (Phase angle used for complex field container)
       2: unit_name (Phase angle unit. Default is radian.)
       3: abs_value (Should use absolute value.)
       4: compute_amplitude (Do calculate amplitude.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("time_of_max")
    >>> op_way2 = core.operators.math.time_of_max()
    """
    return _TimeOfMax()

#internal name: min_over_time
#scripting name: min_over_time
def _get_input_spec_min_over_time(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "angle", type_names = ["double"], optional = True, document = """Phase angle used for complex field container""")
    inpin2 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = True, document = """Phase angle unit. Default is radian.""")
    inpin3 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin4 = _PinSpecification(name = "compute_amplitude", type_names = ["bool"], optional = True, document = """Do calculate amplitude.""")
    inputs_dict_min_over_time = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_min_over_time
    else:
        return inputs_dict_min_over_time[pin]

def _get_output_spec_min_over_time(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_min_over_time = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_min_over_time
    else:
        return outputs_dict_min_over_time[pin]

class _InputSpecMinOverTime(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_min_over_time(), op)
        self.fields_container = Input(_get_input_spec_min_over_time(0), 0, op, -1) 
        super().__init__(_get_input_spec_min_over_time(), op)
        self.angle = Input(_get_input_spec_min_over_time(1), 1, op, -1) 
        super().__init__(_get_input_spec_min_over_time(), op)
        self.unit_name = Input(_get_input_spec_min_over_time(2), 2, op, -1) 
        super().__init__(_get_input_spec_min_over_time(), op)
        self.abs_value = Input(_get_input_spec_min_over_time(3), 3, op, -1) 
        super().__init__(_get_input_spec_min_over_time(), op)
        self.compute_amplitude = Input(_get_input_spec_min_over_time(4), 4, op, -1) 

class _OutputSpecMinOverTime(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_min_over_time(), op)
        self.field = Output(_get_output_spec_min_over_time(0), 0, op) 

class _MinOverTime(_Operator):
    """Operator's description:
    Internal name is "min_over_time"
    Scripting name is "min_over_time"

    Description: Evaluates minimum over time/frequency.

    Input list: 
       0: fields_container 
       1: angle (Phase angle used for complex field container)
       2: unit_name (Phase angle unit. Default is radian.)
       3: abs_value (Should use absolute value.)
       4: compute_amplitude (Do calculate amplitude.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_over_time")
    >>> op_way2 = core.operators.math.min_over_time()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("min_over_time")
        self.inputs = _InputSpecMinOverTime(self)
        self.outputs = _OutputSpecMinOverTime(self)

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

def min_over_time():
    """Operator's description:
    Internal name is "min_over_time"
    Scripting name is "min_over_time"

    Description: Evaluates minimum over time/frequency.

    Input list: 
       0: fields_container 
       1: angle (Phase angle used for complex field container)
       2: unit_name (Phase angle unit. Default is radian.)
       3: abs_value (Should use absolute value.)
       4: compute_amplitude (Do calculate amplitude.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("min_over_time")
    >>> op_way2 = core.operators.math.min_over_time()
    """
    return _MinOverTime()

#internal name: time_of_min
#scripting name: time_of_min
def _get_input_spec_time_of_min(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "angle", type_names = ["double"], optional = True, document = """Phase angle used for complex field container""")
    inpin2 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = True, document = """Phase angle unit. Default is radian.""")
    inpin3 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin4 = _PinSpecification(name = "compute_amplitude", type_names = ["bool"], optional = True, document = """Do calculate amplitude.""")
    inputs_dict_time_of_min = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_time_of_min
    else:
        return inputs_dict_time_of_min[pin]

def _get_output_spec_time_of_min(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_time_of_min = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_time_of_min
    else:
        return outputs_dict_time_of_min[pin]

class _InputSpecTimeOfMin(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_time_of_min(), op)
        self.fields_container = Input(_get_input_spec_time_of_min(0), 0, op, -1) 
        super().__init__(_get_input_spec_time_of_min(), op)
        self.angle = Input(_get_input_spec_time_of_min(1), 1, op, -1) 
        super().__init__(_get_input_spec_time_of_min(), op)
        self.unit_name = Input(_get_input_spec_time_of_min(2), 2, op, -1) 
        super().__init__(_get_input_spec_time_of_min(), op)
        self.abs_value = Input(_get_input_spec_time_of_min(3), 3, op, -1) 
        super().__init__(_get_input_spec_time_of_min(), op)
        self.compute_amplitude = Input(_get_input_spec_time_of_min(4), 4, op, -1) 

class _OutputSpecTimeOfMin(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_time_of_min(), op)
        self.field = Output(_get_output_spec_time_of_min(0), 0, op) 

class _TimeOfMin(_Operator):
    """Operator's description:
    Internal name is "time_of_min"
    Scripting name is "time_of_min"

    Description: Evaluates time/frequency of minimum.

    Input list: 
       0: fields_container 
       1: angle (Phase angle used for complex field container)
       2: unit_name (Phase angle unit. Default is radian.)
       3: abs_value (Should use absolute value.)
       4: compute_amplitude (Do calculate amplitude.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("time_of_min")
    >>> op_way2 = core.operators.math.time_of_min()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("time_of_min")
        self.inputs = _InputSpecTimeOfMin(self)
        self.outputs = _OutputSpecTimeOfMin(self)

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

def time_of_min():
    """Operator's description:
    Internal name is "time_of_min"
    Scripting name is "time_of_min"

    Description: Evaluates time/frequency of minimum.

    Input list: 
       0: fields_container 
       1: angle (Phase angle used for complex field container)
       2: unit_name (Phase angle unit. Default is radian.)
       3: abs_value (Should use absolute value.)
       4: compute_amplitude (Do calculate amplitude.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("time_of_min")
    >>> op_way2 = core.operators.math.time_of_min()
    """
    return _TimeOfMin()

#internal name: max_over_phase
#scripting name: max_over_phase
def _get_input_spec_max_over_phase(pin = None):
    inpin0 = _PinSpecification(name = "real_field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "imaginary_field", type_names = ["field"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "abs_value", type_names = ["bool"], optional = True, document = """Should use absolute value.""")
    inpin3 = _PinSpecification(name = "phase_increment", type_names = ["double"], optional = True, document = """Phase increment (default is 10.0 degrees).""")
    inputs_dict_max_over_phase = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    if pin is None:
        return inputs_dict_max_over_phase
    else:
        return inputs_dict_max_over_phase[pin]

def _get_output_spec_max_over_phase(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_max_over_phase = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_max_over_phase
    else:
        return outputs_dict_max_over_phase[pin]

class _InputSpecMaxOverPhase(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_max_over_phase(), op)
        self.real_field = Input(_get_input_spec_max_over_phase(0), 0, op, -1) 
        super().__init__(_get_input_spec_max_over_phase(), op)
        self.imaginary_field = Input(_get_input_spec_max_over_phase(1), 1, op, -1) 
        super().__init__(_get_input_spec_max_over_phase(), op)
        self.abs_value = Input(_get_input_spec_max_over_phase(2), 2, op, -1) 
        super().__init__(_get_input_spec_max_over_phase(), op)
        self.phase_increment = Input(_get_input_spec_max_over_phase(3), 3, op, -1) 

class _OutputSpecMaxOverPhase(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_max_over_phase(), op)
        self.field = Output(_get_output_spec_max_over_phase(0), 0, op) 

class _MaxOverPhase(_Operator):
    """Operator's description:
    Internal name is "max_over_phase"
    Scripting name is "max_over_phase"

    Description: Returns, for each entity, the maximum value of (real value * cos(theta) - imaginary value * sin(theta)) for theta in [0, 360] degrees with the increment in input.

    Input list: 
       0: real_field 
       1: imaginary_field 
       2: abs_value (Should use absolute value.)
       3: phase_increment (Phase increment (default is 10.0 degrees).)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("max_over_phase")
    >>> op_way2 = core.operators.math.max_over_phase()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("max_over_phase")
        self.inputs = _InputSpecMaxOverPhase(self)
        self.outputs = _OutputSpecMaxOverPhase(self)

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

def max_over_phase():
    """Operator's description:
    Internal name is "max_over_phase"
    Scripting name is "max_over_phase"

    Description: Returns, for each entity, the maximum value of (real value * cos(theta) - imaginary value * sin(theta)) for theta in [0, 360] degrees with the increment in input.

    Input list: 
       0: real_field 
       1: imaginary_field 
       2: abs_value (Should use absolute value.)
       3: phase_increment (Phase increment (default is 10.0 degrees).)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("max_over_phase")
    >>> op_way2 = core.operators.math.max_over_phase()
    """
    return _MaxOverPhase()

#internal name: dot_tensor
#scripting name: dot_tensor
def _get_input_spec_dot_tensor(pin = None):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_dot_tensor = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_dot_tensor
    else:
        return inputs_dict_dot_tensor[pin]

def _get_output_spec_dot_tensor(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_dot_tensor = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_dot_tensor
    else:
        return outputs_dict_dot_tensor[pin]

class _InputSpecDotTensor(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_dot_tensor(), op)
        self.fieldA = Input(_get_input_spec_dot_tensor(0), 0, op, -1) 
        super().__init__(_get_input_spec_dot_tensor(), op)
        self.fieldB = Input(_get_input_spec_dot_tensor(1), 1, op, -1) 

class _OutputSpecDotTensor(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_dot_tensor(), op)
        self.field = Output(_get_output_spec_dot_tensor(0), 0, op) 

class _DotTensor(_Operator):
    """Operator's description:
    Internal name is "dot_tensor"
    Scripting name is "dot_tensor"

    Description: Computes element-wise dot product between two tensor fields.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("dot_tensor")
    >>> op_way2 = core.operators.math.dot_tensor()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("dot_tensor")
        self.inputs = _InputSpecDotTensor(self)
        self.outputs = _OutputSpecDotTensor(self)

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

def dot_tensor():
    """Operator's description:
    Internal name is "dot_tensor"
    Scripting name is "dot_tensor"

    Description: Computes element-wise dot product between two tensor fields.

    Input list: 
       0: fieldA (field or fields container with only one field is expected)
       1: fieldB (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("dot_tensor")
    >>> op_way2 = core.operators.math.dot_tensor()
    """
    return _DotTensor()

#internal name: scale_by_field_fc
#scripting name: scale_by_field_fc
def _get_input_spec_scale_by_field_fc(pin = None):
    inpin0 = _PinSpecification(name = "field_or_fields_container_A", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "field_or_fields_container_B", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_scale_by_field_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_scale_by_field_fc
    else:
        return inputs_dict_scale_by_field_fc[pin]

def _get_output_spec_scale_by_field_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_scale_by_field_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_scale_by_field_fc
    else:
        return outputs_dict_scale_by_field_fc[pin]

class _InputSpecScaleByFieldFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_scale_by_field_fc(), op)
        self.field_or_fields_container_A = Input(_get_input_spec_scale_by_field_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_scale_by_field_fc(), op)
        self.field_or_fields_container_B = Input(_get_input_spec_scale_by_field_fc(1), 1, op, -1) 

class _OutputSpecScaleByFieldFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_scale_by_field_fc(), op)
        self.fields_container = Output(_get_output_spec_scale_by_field_fc(0), 0, op) 

class _ScaleByFieldFc(_Operator):
    """Operator's description:
    Internal name is "scale_by_field_fc"
    Scripting name is "scale_by_field_fc"

    Description: Scales a field (in 0) by a scalar field (in 1). If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

    Input list: 
       0: field_or_fields_container_A (field or fields container with only one field is expected)
       1: field_or_fields_container_B (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("scale_by_field_fc")
    >>> op_way2 = core.operators.math.scale_by_field_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("scale_by_field_fc")
        self.inputs = _InputSpecScaleByFieldFc(self)
        self.outputs = _OutputSpecScaleByFieldFc(self)

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

def scale_by_field_fc():
    """Operator's description:
    Internal name is "scale_by_field_fc"
    Scripting name is "scale_by_field_fc"

    Description: Scales a field (in 0) by a scalar field (in 1). If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

    Input list: 
       0: field_or_fields_container_A (field or fields container with only one field is expected)
       1: field_or_fields_container_B (field or fields container with only one field is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("scale_by_field_fc")
    >>> op_way2 = core.operators.math.scale_by_field_fc()
    """
    return _ScaleByFieldFc()

#internal name: invert
#scripting name: invert
def _get_input_spec_invert(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_invert = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_invert
    else:
        return inputs_dict_invert[pin]

def _get_output_spec_invert(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_invert = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_invert
    else:
        return outputs_dict_invert[pin]

class _InputSpecInvert(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_invert(), op)
        self.field = Input(_get_input_spec_invert(0), 0, op, -1) 

class _OutputSpecInvert(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_invert(), op)
        self.field = Output(_get_output_spec_invert(0), 0, op) 

class _Invert(_Operator):
    """Operator's description:
    Internal name is "invert"
    Scripting name is "invert"

    Description: Compute the element-wise, component-wise, inverse of a field (1./x)

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("invert")
    >>> op_way2 = core.operators.math.invert()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("invert")
        self.inputs = _InputSpecInvert(self)
        self.outputs = _OutputSpecInvert(self)

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

def invert():
    """Operator's description:
    Internal name is "invert"
    Scripting name is "invert"

    Description: Compute the element-wise, component-wise, inverse of a field (1./x)

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("invert")
    >>> op_way2 = core.operators.math.invert()
    """
    return _Invert()

