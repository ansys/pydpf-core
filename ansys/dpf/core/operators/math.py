from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "math" category
"""

#internal name: minus
#scripting name: minus
def _get_input_spec_minus(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_minus = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_minus[pin]

def _get_output_spec_minus(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_minus = { 
        0 : outpin0
    }
    return outputs_dict_minus[pin]

class _InputSpecMinus(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_minus(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_minus(1), 1, op, -1) 

class _OutputSpecMinus(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_minus(0), 0, op) 

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
        self._name = "minus"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecMinus(self._op)
        self.outputs = _OutputSpecMinus(self._op)

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
def _get_input_spec_cplx_multiply(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_multiply = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_cplx_multiply[pin]

def _get_output_spec_cplx_multiply(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_multiply = { 
        0 : outpin0
    }
    return outputs_dict_cplx_multiply[pin]

class _InputSpecCplxMultiply(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_cplx_multiply(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_cplx_multiply(1), 1, op, -1) 

class _OutputSpecCplxMultiply(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cplx_multiply(0), 0, op) 

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
        self._name = "cplx_multiply"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecCplxMultiply(self._op)
        self.outputs = _OutputSpecCplxMultiply(self._op)

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
def _get_input_spec_unit_convert(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = False, document = """unit as a string, ex 'm' for meter, 'Pa' for pascal,...""")
    inputs_dict_unit_convert = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_unit_convert[pin]

def _get_output_spec_unit_convert(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_unit_convert = { 
        0 : outpin0
    }
    return outputs_dict_unit_convert[pin]

class _InputSpecUnitConvert(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_unit_convert(0), 0, op, -1) 
        self.unit_name = _Input(_get_input_spec_unit_convert(1), 1, op, -1) 

class _OutputSpecUnitConvert(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_unit_convert(0), 0, op) 

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
        self._name = "unit_convert"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecUnitConvert(self._op)
        self.outputs = _OutputSpecUnitConvert(self._op)

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
def _get_input_spec_min_max_over_time(pin):
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
    return inputs_dict_min_max_over_time[pin]

def _get_output_spec_min_max_over_time(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_min_max_over_time = { 
        0 : outpin0
    }
    return outputs_dict_min_max_over_time[pin]

class _InputSpecMinMaxOverTime(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_min_max_over_time(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_min_max_over_time(1), 1, op, -1) 
        self.unit_name = _Input(_get_input_spec_min_max_over_time(2), 2, op, -1) 
        self.abs_value = _Input(_get_input_spec_min_max_over_time(3), 3, op, -1) 
        self.compute_amplitude = _Input(_get_input_spec_min_max_over_time(4), 4, op, -1) 
        self.int32 = _Input(_get_input_spec_min_max_over_time(5), 5, op, -1) 

class _OutputSpecMinMaxOverTime(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_min_max_over_time(0), 0, op) 

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
        self._name = "min_max_over_time"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecMinMaxOverTime(self._op)
        self.outputs = _OutputSpecMinMaxOverTime(self._op)

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
def _get_input_spec_minus_fc(pin):
    inpin0 = _PinSpecification(name = "field_or_fields_container_A", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "field_or_fields_container_B", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_minus_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_minus_fc[pin]

def _get_output_spec_minus_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_minus_fc = { 
        0 : outpin0
    }
    return outputs_dict_minus_fc[pin]

class _InputSpecMinusFc(_Inputs):
    def __init__(self, op: _Operator):
        self.field_or_fields_container_A = _Input(_get_input_spec_minus_fc(0), 0, op, -1) 
        self.field_or_fields_container_B = _Input(_get_input_spec_minus_fc(1), 1, op, -1) 

class _OutputSpecMinusFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_minus_fc(0), 0, op) 

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
        self._name = "minus_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecMinusFc(self._op)
        self.outputs = _OutputSpecMinusFc(self._op)

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
def _get_input_spec_accumulate(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_accumulate = { 
        0 : inpin0
    }
    return inputs_dict_accumulate[pin]

def _get_output_spec_accumulate(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_accumulate = { 
        0 : outpin0
    }
    return outputs_dict_accumulate[pin]

class _InputSpecAccumulate(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_accumulate(0), 0, op, -1) 

class _OutputSpecAccumulate(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_accumulate(0), 0, op) 

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
        self._name = "accumulate"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecAccumulate(self._op)
        self.outputs = _OutputSpecAccumulate(self._op)

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
def _get_input_spec_unit_convert_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "unit_name", type_names = ["string"], optional = False, document = """unit as a string, ex 'm' for meter, 'Pa' for pascal,...""")
    inputs_dict_unit_convert_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_unit_convert_fc[pin]

def _get_output_spec_unit_convert_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_unit_convert_fc = { 
        0 : outpin0
    }
    return outputs_dict_unit_convert_fc[pin]

class _InputSpecUnitConvertFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_unit_convert_fc(0), 0, op, -1) 
        self.unit_name = _Input(_get_input_spec_unit_convert_fc(1), 1, op, -1) 

class _OutputSpecUnitConvertFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_unit_convert_fc(0), 0, op) 

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
        self._name = "unit_convert_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecUnitConvertFc(self._op)
        self.outputs = _OutputSpecUnitConvertFc(self._op)

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
def _get_input_spec_add(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_add = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_add[pin]

def _get_output_spec_add(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_add = { 
        0 : outpin0
    }
    return outputs_dict_add[pin]

class _InputSpecAdd(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_add(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_add(1), 1, op, -1) 

class _OutputSpecAdd(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_add(0), 0, op) 

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
        self._name = "add"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecAdd(self._op)
        self.outputs = _OutputSpecAdd(self._op)

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
def _get_input_spec_add_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container1", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_container2", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_add_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_add_fc[pin]

def _get_output_spec_add_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_add_fc = { 
        0 : outpin0
    }
    return outputs_dict_add_fc[pin]

class _InputSpecAddFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container1 = _Input(_get_input_spec_add_fc(0), 0, op, 0) 
        self.fields_container2 = _Input(_get_input_spec_add_fc(1), 1, op, -1) 

class _OutputSpecAddFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_add_fc(0), 0, op) 

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
        self._name = "add_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecAddFc(self._op)
        self.outputs = _OutputSpecAddFc(self._op)

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
def _get_input_spec_phase_of_max(pin):
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
    return inputs_dict_phase_of_max[pin]

def _get_output_spec_phase_of_max(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_phase_of_max = { 
        0 : outpin0
    }
    return outputs_dict_phase_of_max[pin]

class _InputSpecPhaseOfMax(_Inputs):
    def __init__(self, op: _Operator):
        self.real_field = _Input(_get_input_spec_phase_of_max(0), 0, op, -1) 
        self.imaginary_field = _Input(_get_input_spec_phase_of_max(1), 1, op, -1) 
        self.abs_value = _Input(_get_input_spec_phase_of_max(2), 2, op, -1) 
        self.phase_increment = _Input(_get_input_spec_phase_of_max(3), 3, op, -1) 

class _OutputSpecPhaseOfMax(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_phase_of_max(0), 0, op) 

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
        self._name = "phase_of_max"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecPhaseOfMax(self._op)
        self.outputs = _OutputSpecPhaseOfMax(self._op)

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
def _get_input_spec_sin_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_sin_fc = { 
        0 : inpin0
    }
    return inputs_dict_sin_fc[pin]

def _get_output_spec_sin_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sin_fc = { 
        0 : outpin0
    }
    return outputs_dict_sin_fc[pin]

class _InputSpecSinFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_sin_fc(0), 0, op, -1) 

class _OutputSpecSinFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_sin_fc(0), 0, op) 

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
        self._name = "sin_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecSinFc(self._op)
        self.outputs = _OutputSpecSinFc(self._op)

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
def _get_input_spec_add_constant(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double"], optional = False, document = """double or vector of double""")
    inputs_dict_add_constant = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_add_constant[pin]

def _get_output_spec_add_constant(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_add_constant = { 
        0 : outpin0
    }
    return outputs_dict_add_constant[pin]

class _InputSpecAddConstant(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_add_constant(0), 0, op, -1) 
        self.ponderation = _Input(_get_input_spec_add_constant(1), 1, op, -1) 

class _OutputSpecAddConstant(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_add_constant(0), 0, op) 

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
        self._name = "add_constant"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecAddConstant(self._op)
        self.outputs = _OutputSpecAddConstant(self._op)

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
def _get_input_spec_invert_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_invert_fc = { 
        0 : inpin0
    }
    return inputs_dict_invert_fc[pin]

def _get_output_spec_invert_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_invert_fc = { 
        0 : outpin0
    }
    return outputs_dict_invert_fc[pin]

class _InputSpecInvertFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_invert_fc(0), 0, op, -1) 

class _OutputSpecInvertFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_invert_fc(0), 0, op) 

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
        self._name = "invert_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecInvertFc(self._op)
        self.outputs = _OutputSpecInvertFc(self._op)

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
def _get_input_spec_pow(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "factor", type_names = ["double"], optional = False, document = """""")
    inputs_dict_pow = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_pow[pin]

def _get_output_spec_pow(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_pow = { 
        0 : outpin0
    }
    return outputs_dict_pow[pin]

class _InputSpecPow(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_pow(0), 0, op, -1) 
        self.factor = _Input(_get_input_spec_pow(1), 1, op, -1) 

class _OutputSpecPow(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_pow(0), 0, op) 

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
        self._name = "Pow"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecPow(self._op)
        self.outputs = _OutputSpecPow(self._op)

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
def _get_input_spec_add_constant_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double"], optional = False, document = """double or vector of double""")
    inputs_dict_add_constant_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_add_constant_fc[pin]

def _get_output_spec_add_constant_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_add_constant_fc = { 
        0 : outpin0
    }
    return outputs_dict_add_constant_fc[pin]

class _InputSpecAddConstantFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_add_constant_fc(0), 0, op, -1) 
        self.ponderation = _Input(_get_input_spec_add_constant_fc(1), 1, op, -1) 

class _OutputSpecAddConstantFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_add_constant_fc(0), 0, op) 

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
        self._name = "add_constant_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecAddConstantFc(self._op)
        self.outputs = _OutputSpecAddConstantFc(self._op)

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
def _get_input_spec_scale(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double","field"], optional = False, document = """Double/Field scoped on overall""")
    inpin2 = _PinSpecification(name = "boolean", type_names = ["bool"], optional = True, document = """bool(optional, default false) if set to true, output of scale is mane dimensionless""")
    inputs_dict_scale = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_scale[pin]

def _get_output_spec_scale(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_scale = { 
        0 : outpin0
    }
    return outputs_dict_scale[pin]

class _InputSpecScale(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_scale(0), 0, op, -1) 
        self.ponderation = _Input(_get_input_spec_scale(1), 1, op, -1) 
        self.boolean = _Input(_get_input_spec_scale(2), 2, op, -1) 

class _OutputSpecScale(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_scale(0), 0, op) 

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
        self._name = "scale"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecScale(self._op)
        self.outputs = _OutputSpecScale(self._op)

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
def _get_input_spec_pow_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "factor", type_names = ["double"], optional = False, document = """""")
    inputs_dict_pow_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_pow_fc[pin]

def _get_output_spec_pow_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_pow_fc = { 
        0 : outpin0
    }
    return outputs_dict_pow_fc[pin]

class _InputSpecPowFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_pow_fc(0), 0, op, -1) 
        self.factor = _Input(_get_input_spec_pow_fc(1), 1, op, -1) 

class _OutputSpecPowFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_pow_fc(0), 0, op) 

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
        self._name = "Pow_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecPowFc(self._op)
        self.outputs = _OutputSpecPowFc(self._op)

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
def _get_input_spec_scale_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "ponderation", type_names = ["double","field"], optional = False, document = """Double/Field scoped on overall""")
    inpin2 = _PinSpecification(name = "boolean", type_names = ["bool"], optional = True, document = """bool(optional, default false) if set to true, output of scale is mane dimensionless""")
    inputs_dict_scale_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_scale_fc[pin]

def _get_output_spec_scale_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_scale_fc = { 
        0 : outpin0
    }
    return outputs_dict_scale_fc[pin]

class _InputSpecScaleFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_scale_fc(0), 0, op, -1) 
        self.ponderation = _Input(_get_input_spec_scale_fc(1), 1, op, -1) 
        self.boolean = _Input(_get_input_spec_scale_fc(2), 2, op, -1) 

class _OutputSpecScaleFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_scale_fc(0), 0, op) 

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
        self._name = "scale_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecScaleFc(self._op)
        self.outputs = _OutputSpecScaleFc(self._op)

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
def _get_input_spec_centroid(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin2 = _PinSpecification(name = "factor", type_names = ["double"], optional = False, document = """Scalar""")
    inputs_dict_centroid = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_centroid[pin]

def _get_output_spec_centroid(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_centroid = { 
        0 : outpin0
    }
    return outputs_dict_centroid[pin]

class _InputSpecCentroid(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_centroid(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_centroid(1), 1, op, -1) 
        self.factor = _Input(_get_input_spec_centroid(2), 2, op, -1) 

class _OutputSpecCentroid(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_centroid(0), 0, op) 

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
        self._name = "centroid"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecCentroid(self._op)
        self.outputs = _OutputSpecCentroid(self._op)

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
def _get_input_spec_sweeping_phase(pin):
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
    return inputs_dict_sweeping_phase[pin]

def _get_output_spec_sweeping_phase(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sweeping_phase = { 
        0 : outpin0
    }
    return outputs_dict_sweeping_phase[pin]

class _InputSpecSweepingPhase(_Inputs):
    def __init__(self, op: _Operator):
        self.real_field = _Input(_get_input_spec_sweeping_phase(0), 0, op, -1) 
        self.imaginary_field = _Input(_get_input_spec_sweeping_phase(1), 1, op, -1) 
        self.angle = _Input(_get_input_spec_sweeping_phase(2), 2, op, -1) 
        self.unit_name = _Input(_get_input_spec_sweeping_phase(3), 3, op, -1) 
        self.abs_value = _Input(_get_input_spec_sweeping_phase(4), 4, op, -1) 
        self.imaginary_part_null = _Input(_get_input_spec_sweeping_phase(5), 5, op, -1) 

class _OutputSpecSweepingPhase(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_sweeping_phase(0), 0, op) 

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
        self._name = "sweeping_phase"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecSweepingPhase(self._op)
        self.outputs = _OutputSpecSweepingPhase(self._op)

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
def _get_input_spec_sin(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inputs_dict_sin = { 
        0 : inpin0
    }
    return inputs_dict_sin[pin]

def _get_output_spec_sin(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sin = { 
        0 : outpin0
    }
    return outputs_dict_sin[pin]

class _InputSpecSin(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_sin(0), 0, op, -1) 

class _OutputSpecSin(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_sin(0), 0, op) 

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
        self._name = "sin"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecSin(self._op)
        self.outputs = _OutputSpecSin(self._op)

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
def _get_input_spec_cos(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_cos = { 
        0 : inpin0
    }
    return inputs_dict_cos[pin]

def _get_output_spec_cos(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_cos = { 
        0 : outpin0
    }
    return outputs_dict_cos[pin]

class _InputSpecCos(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_cos(0), 0, op, -1) 

class _OutputSpecCos(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_cos(0), 0, op) 

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
        self._name = "cos"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecCos(self._op)
        self.outputs = _OutputSpecCos(self._op)

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
def _get_input_spec_cos_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_cos_fc = { 
        0 : inpin0
    }
    return inputs_dict_cos_fc[pin]

def _get_output_spec_cos_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cos_fc = { 
        0 : outpin0
    }
    return outputs_dict_cos_fc[pin]

class _InputSpecCosFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_cos_fc(0), 0, op, -1) 

class _OutputSpecCosFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cos_fc(0), 0, op) 

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
        self._name = "cos_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecCosFc(self._op)
        self.outputs = _OutputSpecCosFc(self._op)

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
def _get_input_spec_sweeping_phase_fc(pin):
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
    return inputs_dict_sweeping_phase_fc[pin]

def _get_output_spec_sweeping_phase_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sweeping_phase_fc = { 
        0 : outpin0
    }
    return outputs_dict_sweeping_phase_fc[pin]

class _InputSpecSweepingPhaseFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_sweeping_phase_fc(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_sweeping_phase_fc(2), 2, op, -1) 
        self.unit_name = _Input(_get_input_spec_sweeping_phase_fc(3), 3, op, -1) 
        self.abs_value = _Input(_get_input_spec_sweeping_phase_fc(4), 4, op, -1) 

class _OutputSpecSweepingPhaseFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_sweeping_phase_fc(0), 0, op) 

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
        self._name = "sweeping_phase_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecSweepingPhaseFc(self._op)
        self.outputs = _OutputSpecSweepingPhaseFc(self._op)

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
def _get_input_spec_sqr(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqr = { 
        0 : inpin0
    }
    return inputs_dict_sqr[pin]

def _get_output_spec_sqr(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sqr = { 
        0 : outpin0
    }
    return outputs_dict_sqr[pin]

class _InputSpecSqr(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_sqr(0), 0, op, -1) 

class _OutputSpecSqr(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_sqr(0), 0, op) 

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
        self._name = "sqr"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecSqr(self._op)
        self.outputs = _OutputSpecSqr(self._op)

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
def _get_input_spec_linear_combination(pin):
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
    return inputs_dict_linear_combination[pin]

def _get_output_spec_linear_combination(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_linear_combination = { 
        0 : outpin0
    }
    return outputs_dict_linear_combination[pin]

class _InputSpecLinearCombination(_Inputs):
    def __init__(self, op: _Operator):
        self.a = _Input(_get_input_spec_linear_combination(0), 0, op, -1) 
        self.fields_containerA = _Input(_get_input_spec_linear_combination(1), 1, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_linear_combination(2), 2, op, -1) 
        self.b = _Input(_get_input_spec_linear_combination(3), 3, op, -1) 
        self.fields_containerC = _Input(_get_input_spec_linear_combination(4), 4, op, -1) 

class _OutputSpecLinearCombination(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_linear_combination(0), 0, op) 

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
        self._name = "CplxOp"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecLinearCombination(self._op)
        self.outputs = _OutputSpecLinearCombination(self._op)

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
def _get_input_spec_sqr_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqr_fc = { 
        0 : inpin0
    }
    return inputs_dict_sqr_fc[pin]

def _get_output_spec_sqr_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sqr_fc = { 
        0 : outpin0
    }
    return outputs_dict_sqr_fc[pin]

class _InputSpecSqrFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_sqr_fc(0), 0, op, -1) 

class _OutputSpecSqrFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_sqr_fc(0), 0, op) 

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
        self._name = "sqr_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecSqrFc(self._op)
        self.outputs = _OutputSpecSqrFc(self._op)

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
def _get_input_spec_sqrt(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqrt = { 
        0 : inpin0
    }
    return inputs_dict_sqrt[pin]

def _get_output_spec_sqrt(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_sqrt = { 
        0 : outpin0
    }
    return outputs_dict_sqrt[pin]

class _InputSpecSqrt(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_sqrt(0), 0, op, -1) 

class _OutputSpecSqrt(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_sqrt(0), 0, op) 

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
        self._name = "sqrt"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecSqrt(self._op)
        self.outputs = _OutputSpecSqrt(self._op)

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
def _get_input_spec_norm(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_norm = { 
        0 : inpin0
    }
    return inputs_dict_norm[pin]

def _get_output_spec_norm(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_norm = { 
        0 : outpin0
    }
    return outputs_dict_norm[pin]

class _InputSpecNorm(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_norm(0), 0, op, -1) 

class _OutputSpecNorm(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_norm(0), 0, op) 

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
        self._name = "norm"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecNorm(self._op)
        self.outputs = _OutputSpecNorm(self._op)

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
def _get_input_spec_sqrt_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_sqrt_fc = { 
        0 : inpin0
    }
    return inputs_dict_sqrt_fc[pin]

def _get_output_spec_sqrt_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_sqrt_fc = { 
        0 : outpin0
    }
    return outputs_dict_sqrt_fc[pin]

class _InputSpecSqrtFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_sqrt_fc(0), 0, op, -1) 

class _OutputSpecSqrtFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_sqrt_fc(0), 0, op) 

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
        self._name = "sqrt_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecSqrtFc(self._op)
        self.outputs = _OutputSpecSqrtFc(self._op)

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
def _get_input_spec_norm_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_norm_fc = { 
        0 : inpin0
    }
    return inputs_dict_norm_fc[pin]

def _get_output_spec_norm_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_norm_fc = { 
        0 : outpin0
    }
    return outputs_dict_norm_fc[pin]

class _InputSpecNormFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_norm_fc(0), 0, op, -1) 

class _OutputSpecNormFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_norm_fc(0), 0, op) 

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
        self._name = "norm_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecNormFc(self._op)
        self.outputs = _OutputSpecNormFc(self._op)

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
def _get_input_spec_component_wise_divide(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_component_wise_divide = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_component_wise_divide[pin]

def _get_output_spec_component_wise_divide(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_component_wise_divide = { 
        0 : outpin0
    }
    return outputs_dict_component_wise_divide[pin]

class _InputSpecComponentWiseDivide(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_component_wise_divide(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_component_wise_divide(1), 1, op, -1) 

class _OutputSpecComponentWiseDivide(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_component_wise_divide(0), 0, op) 

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
        self._name = "component_wise_divide"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecComponentWiseDivide(self._op)
        self.outputs = _OutputSpecComponentWiseDivide(self._op)

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
def _get_input_spec_component_wise_divide_fc(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_component_wise_divide_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_component_wise_divide_fc[pin]

def _get_output_spec_component_wise_divide_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_component_wise_divide_fc = { 
        0 : outpin0
    }
    return outputs_dict_component_wise_divide_fc[pin]

class _InputSpecComponentWiseDivideFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_component_wise_divide_fc(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_component_wise_divide_fc(1), 1, op, -1) 

class _OutputSpecComponentWiseDivideFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_component_wise_divide_fc(0), 0, op) 

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
        self._name = "component_wise_divide_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecComponentWiseDivideFc(self._op)
        self.outputs = _OutputSpecComponentWiseDivideFc(self._op)

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
def _get_input_spec_kronecker_prod(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_kronecker_prod = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_kronecker_prod[pin]

def _get_output_spec_kronecker_prod(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_kronecker_prod = { 
        0 : outpin0
    }
    return outputs_dict_kronecker_prod[pin]

class _InputSpecKroneckerProd(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_kronecker_prod(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_kronecker_prod(1), 1, op, -1) 

class _OutputSpecKroneckerProd(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_kronecker_prod(0), 0, op) 

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
        self._name = "kronecker_prod"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecKroneckerProd(self._op)
        self.outputs = _OutputSpecKroneckerProd(self._op)

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
def _get_input_spec_real_part(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_real_part = { 
        0 : inpin0
    }
    return inputs_dict_real_part[pin]

def _get_output_spec_real_part(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_real_part = { 
        0 : outpin0
    }
    return outputs_dict_real_part[pin]

class _InputSpecRealPart(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_real_part(0), 0, op, -1) 

class _OutputSpecRealPart(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_real_part(0), 0, op) 

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
        self._name = "realP_part"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecRealPart(self._op)
        self.outputs = _OutputSpecRealPart(self._op)

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
def _get_input_spec_conjugate(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_conjugate = { 
        0 : inpin0
    }
    return inputs_dict_conjugate[pin]

def _get_output_spec_conjugate(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_conjugate = { 
        0 : outpin0
    }
    return outputs_dict_conjugate[pin]

class _InputSpecConjugate(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_conjugate(0), 0, op, -1) 

class _OutputSpecConjugate(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_conjugate(0), 0, op) 

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
        self._name = "conjugate"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecConjugate(self._op)
        self.outputs = _OutputSpecConjugate(self._op)

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
def _get_input_spec_img_part(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_img_part = { 
        0 : inpin0
    }
    return inputs_dict_img_part[pin]

def _get_output_spec_img_part(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_img_part = { 
        0 : outpin0
    }
    return outputs_dict_img_part[pin]

class _InputSpecImgPart(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_img_part(0), 0, op, -1) 

class _OutputSpecImgPart(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_img_part(0), 0, op) 

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
        self._name = "img_part"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecImgPart(self._op)
        self.outputs = _OutputSpecImgPart(self._op)

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
def _get_input_spec_amplitude(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_amplitude = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_amplitude[pin]

def _get_output_spec_amplitude(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_amplitude = { 
        0 : outpin0
    }
    return outputs_dict_amplitude[pin]

class _InputSpecAmplitude(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_amplitude(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_amplitude(1), 1, op, -1) 

class _OutputSpecAmplitude(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_amplitude(0), 0, op) 

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
        self._name = "amplitude"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecAmplitude(self._op)
        self.outputs = _OutputSpecAmplitude(self._op)

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
def _get_input_spec_cplx_add(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_add = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_cplx_add[pin]

def _get_output_spec_cplx_add(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_add = { 
        0 : outpin0
    }
    return outputs_dict_cplx_add[pin]

class _InputSpecCplxAdd(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_cplx_add(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_cplx_add(1), 1, op, -1) 

class _OutputSpecCplxAdd(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cplx_add(0), 0, op) 

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
        self._name = "cplx_add"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecCplxAdd(self._op)
        self.outputs = _OutputSpecCplxAdd(self._op)

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
def _get_input_spec_cplx_dot(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_dot = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_cplx_dot[pin]

def _get_output_spec_cplx_dot(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_dot = { 
        0 : outpin0
    }
    return outputs_dict_cplx_dot[pin]

class _InputSpecCplxDot(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_cplx_dot(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_cplx_dot(1), 1, op, -1) 

class _OutputSpecCplxDot(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cplx_dot(0), 0, op) 

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
        self._name = "cplx_dot"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecCplxDot(self._op)
        self.outputs = _OutputSpecCplxDot(self._op)

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
def _get_input_spec_cplx_divide(pin):
    inpin0 = _PinSpecification(name = "fields_containerA", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "fields_containerB", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_divide = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_cplx_divide[pin]

def _get_output_spec_cplx_divide(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_divide = { 
        0 : outpin0
    }
    return outputs_dict_cplx_divide[pin]

class _InputSpecCplxDivide(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_containerA = _Input(_get_input_spec_cplx_divide(0), 0, op, -1) 
        self.fields_containerB = _Input(_get_input_spec_cplx_divide(1), 1, op, -1) 

class _OutputSpecCplxDivide(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cplx_divide(0), 0, op) 

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
        self._name = "cplx_divide"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecCplxDivide(self._op)
        self.outputs = _OutputSpecCplxDivide(self._op)

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
def _get_input_spec_dot(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_dot = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_dot[pin]

def _get_output_spec_dot(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_dot = { 
        0 : outpin0
    }
    return outputs_dict_dot[pin]

class _InputSpecDot(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_dot(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_dot(1), 1, op, -1) 

class _OutputSpecDot(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_dot(0), 0, op) 

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
        self._name = "dot"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecDot(self._op)
        self.outputs = _OutputSpecDot(self._op)

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
def _get_input_spec_cplx_derive(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_cplx_derive = { 
        0 : inpin0
    }
    return inputs_dict_cplx_derive[pin]

def _get_output_spec_cplx_derive(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_cplx_derive = { 
        0 : outpin0
    }
    return outputs_dict_cplx_derive[pin]

class _InputSpecCplxDerive(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_cplx_derive(0), 0, op, -1) 

class _OutputSpecCplxDerive(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cplx_derive(0), 0, op) 

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
        self._name = "cplx_derive"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecCplxDerive(self._op)
        self.outputs = _OutputSpecCplxDerive(self._op)

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
def _get_input_spec_polar_to_cplx(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_polar_to_cplx = { 
        0 : inpin0
    }
    return inputs_dict_polar_to_cplx[pin]

def _get_output_spec_polar_to_cplx(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_polar_to_cplx = { 
        0 : outpin0
    }
    return outputs_dict_polar_to_cplx[pin]

class _InputSpecPolarToCplx(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_polar_to_cplx(0), 0, op, -1) 

class _OutputSpecPolarToCplx(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_polar_to_cplx(0), 0, op) 

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
        self._name = "polar_to_cplx"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecPolarToCplx(self._op)
        self.outputs = _OutputSpecPolarToCplx(self._op)

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
def _get_input_spec_modulus(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_modulus = { 
        0 : inpin0
    }
    return inputs_dict_modulus[pin]

def _get_output_spec_modulus(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_modulus = { 
        0 : outpin0
    }
    return outputs_dict_modulus[pin]

class _InputSpecModulus(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_modulus(0), 0, op, -1) 

class _OutputSpecModulus(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_modulus(0), 0, op) 

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
        self._name = "modulus"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecModulus(self._op)
        self.outputs = _OutputSpecModulus(self._op)

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
def _get_input_spec_accumulate_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_accumulate_fc = { 
        0 : inpin0
    }
    return inputs_dict_accumulate_fc[pin]

def _get_output_spec_accumulate_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_accumulate_fc = { 
        0 : outpin0
    }
    return outputs_dict_accumulate_fc[pin]

class _InputSpecAccumulateFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_accumulate_fc(0), 0, op, -1) 

class _OutputSpecAccumulateFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_accumulate_fc(0), 0, op) 

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
        self._name = "accumulate_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecAccumulateFc(self._op)
        self.outputs = _OutputSpecAccumulateFc(self._op)

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
def _get_input_spec_generalized_inner_product(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_generalized_inner_product = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_generalized_inner_product[pin]

def _get_output_spec_generalized_inner_product(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_generalized_inner_product = { 
        0 : outpin0
    }
    return outputs_dict_generalized_inner_product[pin]

class _InputSpecGeneralizedInnerProduct(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_generalized_inner_product(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_generalized_inner_product(1), 1, op, -1) 

class _OutputSpecGeneralizedInnerProduct(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_generalized_inner_product(0), 0, op) 

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
        self._name = "generalized_inner_product"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecGeneralizedInnerProduct(self._op)
        self.outputs = _OutputSpecGeneralizedInnerProduct(self._op)

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
def _get_input_spec_scale_by_field(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_scale_by_field = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_scale_by_field[pin]

def _get_output_spec_scale_by_field(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_scale_by_field = { 
        0 : outpin0
    }
    return outputs_dict_scale_by_field[pin]

class _InputSpecScaleByField(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_scale_by_field(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_scale_by_field(1), 1, op, -1) 

class _OutputSpecScaleByField(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_scale_by_field(0), 0, op) 

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
        self._name = "scale_by_field"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecScaleByField(self._op)
        self.outputs = _OutputSpecScaleByField(self._op)

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
def _get_input_spec_generalized_inner_product_fc(pin):
    inpin0 = _PinSpecification(name = "field_or_fields_container_A", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "field_or_fields_container_B", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_generalized_inner_product_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_generalized_inner_product_fc[pin]

def _get_output_spec_generalized_inner_product_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_generalized_inner_product_fc = { 
        0 : outpin0
    }
    return outputs_dict_generalized_inner_product_fc[pin]

class _InputSpecGeneralizedInnerProductFc(_Inputs):
    def __init__(self, op: _Operator):
        self.field_or_fields_container_A = _Input(_get_input_spec_generalized_inner_product_fc(0), 0, op, -1) 
        self.field_or_fields_container_B = _Input(_get_input_spec_generalized_inner_product_fc(1), 1, op, -1) 

class _OutputSpecGeneralizedInnerProductFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_generalized_inner_product_fc(0), 0, op) 

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
        self._name = "generalized_inner_product_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecGeneralizedInnerProductFc(self._op)
        self.outputs = _OutputSpecGeneralizedInnerProductFc(self._op)

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
def _get_input_spec_max_over_time(pin):
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
    return inputs_dict_max_over_time[pin]

def _get_output_spec_max_over_time(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_max_over_time = { 
        0 : outpin0
    }
    return outputs_dict_max_over_time[pin]

class _InputSpecMaxOverTime(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_max_over_time(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_max_over_time(1), 1, op, -1) 
        self.unit_name = _Input(_get_input_spec_max_over_time(2), 2, op, -1) 
        self.abs_value = _Input(_get_input_spec_max_over_time(3), 3, op, -1) 
        self.compute_amplitude = _Input(_get_input_spec_max_over_time(4), 4, op, -1) 

class _OutputSpecMaxOverTime(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_max_over_time(0), 0, op) 

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
        self._name = "max_over_time"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecMaxOverTime(self._op)
        self.outputs = _OutputSpecMaxOverTime(self._op)

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
def _get_input_spec_time_of_max(pin):
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
    return inputs_dict_time_of_max[pin]

def _get_output_spec_time_of_max(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_time_of_max = { 
        0 : outpin0
    }
    return outputs_dict_time_of_max[pin]

class _InputSpecTimeOfMax(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_time_of_max(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_time_of_max(1), 1, op, -1) 
        self.unit_name = _Input(_get_input_spec_time_of_max(2), 2, op, -1) 
        self.abs_value = _Input(_get_input_spec_time_of_max(3), 3, op, -1) 
        self.compute_amplitude = _Input(_get_input_spec_time_of_max(4), 4, op, -1) 

class _OutputSpecTimeOfMax(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_time_of_max(0), 0, op) 

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
        self._name = "time_of_max"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecTimeOfMax(self._op)
        self.outputs = _OutputSpecTimeOfMax(self._op)

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
def _get_input_spec_min_over_time(pin):
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
    return inputs_dict_min_over_time[pin]

def _get_output_spec_min_over_time(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_min_over_time = { 
        0 : outpin0
    }
    return outputs_dict_min_over_time[pin]

class _InputSpecMinOverTime(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_min_over_time(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_min_over_time(1), 1, op, -1) 
        self.unit_name = _Input(_get_input_spec_min_over_time(2), 2, op, -1) 
        self.abs_value = _Input(_get_input_spec_min_over_time(3), 3, op, -1) 
        self.compute_amplitude = _Input(_get_input_spec_min_over_time(4), 4, op, -1) 

class _OutputSpecMinOverTime(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_min_over_time(0), 0, op) 

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
        self._name = "min_over_time"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecMinOverTime(self._op)
        self.outputs = _OutputSpecMinOverTime(self._op)

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
def _get_input_spec_time_of_min(pin):
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
    return inputs_dict_time_of_min[pin]

def _get_output_spec_time_of_min(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_time_of_min = { 
        0 : outpin0
    }
    return outputs_dict_time_of_min[pin]

class _InputSpecTimeOfMin(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_time_of_min(0), 0, op, -1) 
        self.angle = _Input(_get_input_spec_time_of_min(1), 1, op, -1) 
        self.unit_name = _Input(_get_input_spec_time_of_min(2), 2, op, -1) 
        self.abs_value = _Input(_get_input_spec_time_of_min(3), 3, op, -1) 
        self.compute_amplitude = _Input(_get_input_spec_time_of_min(4), 4, op, -1) 

class _OutputSpecTimeOfMin(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_time_of_min(0), 0, op) 

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
        self._name = "time_of_min"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecTimeOfMin(self._op)
        self.outputs = _OutputSpecTimeOfMin(self._op)

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
def _get_input_spec_max_over_phase(pin):
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
    return inputs_dict_max_over_phase[pin]

def _get_output_spec_max_over_phase(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_max_over_phase = { 
        0 : outpin0
    }
    return outputs_dict_max_over_phase[pin]

class _InputSpecMaxOverPhase(_Inputs):
    def __init__(self, op: _Operator):
        self.real_field = _Input(_get_input_spec_max_over_phase(0), 0, op, -1) 
        self.imaginary_field = _Input(_get_input_spec_max_over_phase(1), 1, op, -1) 
        self.abs_value = _Input(_get_input_spec_max_over_phase(2), 2, op, -1) 
        self.phase_increment = _Input(_get_input_spec_max_over_phase(3), 3, op, -1) 

class _OutputSpecMaxOverPhase(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_max_over_phase(0), 0, op) 

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
        self._name = "max_over_phase"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecMaxOverPhase(self._op)
        self.outputs = _OutputSpecMaxOverPhase(self._op)

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
def _get_input_spec_dot_tensor(pin):
    inpin0 = _PinSpecification(name = "fieldA", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "fieldB", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_dot_tensor = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_dot_tensor[pin]

def _get_output_spec_dot_tensor(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_dot_tensor = { 
        0 : outpin0
    }
    return outputs_dict_dot_tensor[pin]

class _InputSpecDotTensor(_Inputs):
    def __init__(self, op: _Operator):
        self.fieldA = _Input(_get_input_spec_dot_tensor(0), 0, op, -1) 
        self.fieldB = _Input(_get_input_spec_dot_tensor(1), 1, op, -1) 

class _OutputSpecDotTensor(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_dot_tensor(0), 0, op) 

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
        self._name = "dot_tensor"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecDotTensor(self._op)
        self.outputs = _OutputSpecDotTensor(self._op)

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
def _get_input_spec_scale_by_field_fc(pin):
    inpin0 = _PinSpecification(name = "field_or_fields_container_A", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "field_or_fields_container_B", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_scale_by_field_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_scale_by_field_fc[pin]

def _get_output_spec_scale_by_field_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_scale_by_field_fc = { 
        0 : outpin0
    }
    return outputs_dict_scale_by_field_fc[pin]

class _InputSpecScaleByFieldFc(_Inputs):
    def __init__(self, op: _Operator):
        self.field_or_fields_container_A = _Input(_get_input_spec_scale_by_field_fc(0), 0, op, -1) 
        self.field_or_fields_container_B = _Input(_get_input_spec_scale_by_field_fc(1), 1, op, -1) 

class _OutputSpecScaleByFieldFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_scale_by_field_fc(0), 0, op) 

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
        self._name = "scale_by_field_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecScaleByFieldFc(self._op)
        self.outputs = _OutputSpecScaleByFieldFc(self._op)

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
def _get_input_spec_invert(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_invert = { 
        0 : inpin0
    }
    return inputs_dict_invert[pin]

def _get_output_spec_invert(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_invert = { 
        0 : outpin0
    }
    return outputs_dict_invert[pin]

class _InputSpecInvert(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_invert(0), 0, op, -1) 

class _OutputSpecInvert(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_invert(0), 0, op) 

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
        self._name = "invert"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecInvert(self._op)
        self.outputs = _OutputSpecInvert(self._op)

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

