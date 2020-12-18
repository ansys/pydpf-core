from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

#internal name: core::field::low_pass_fc
#scripting name: field.low_pass_fc
def _get_input_spec_low_pass_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "threshold", type_names = ["double","field"], optional = False, document = """a threshold scalar or a field containing one value is expected""")
    inputs_dict_low_pass_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_low_pass_fc
    else:
        return inputs_dict_low_pass_fc[pin]

def _get_output_spec_low_pass_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_low_pass_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_low_pass_fc
    else:
        return outputs_dict_low_pass_fc[pin]

class _InputSpecLowPassFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_low_pass_fc(), op)
        self.fields_container = Input(_get_input_spec_low_pass_fc(0), 0, op, -1) 
        self.threshold = Input(_get_input_spec_low_pass_fc(1), 1, op, -1) 

class _OutputSpecLowPassFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_low_pass_fc(), op)
        self.fields_container = Output(_get_output_spec_low_pass_fc(0), 0, op) 

class _LowPassFc(_Operator):
    """Operator's description:
    Internal name is "core::field::low_pass_fc"
    Scripting name is "field.low_pass_fc"

    Description: The low pass filter returns all the values strictly inferior to the threshold value in input.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: threshold (a threshold scalar or a field containing one value is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::low_pass_fc")
    >>> op_way2 = core.operators.filter.field.low_pass_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("core::field::low_pass_fc")
        self.inputs = _InputSpecLowPassFc(self)
        self.outputs = _OutputSpecLowPassFc(self)

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

def low_pass_fc():
    """Operator's description:
    Internal name is "core::field::low_pass_fc"
    Scripting name is "field.low_pass_fc"

    Description: The low pass filter returns all the values strictly inferior to the threshold value in input.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: threshold (a threshold scalar or a field containing one value is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::low_pass_fc")
    >>> op_way2 = core.operators.filter.field.low_pass_fc()
    """
    return _LowPassFc()

#internal name: core::field::band_pass_fc
#scripting name: field.band_pass_fc
def _get_input_spec_band_pass_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "min_threshold", type_names = ["double","field"], optional = False, document = """a min threshold scalar or a field containing one value is expected""")
    inpin2 = _PinSpecification(name = "max_threshold", type_names = ["double","field"], optional = False, document = """a max threshold scalar or a field containing one value is expected""")
    inputs_dict_band_pass_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    if pin is None:
        return inputs_dict_band_pass_fc
    else:
        return inputs_dict_band_pass_fc[pin]

def _get_output_spec_band_pass_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_band_pass_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_band_pass_fc
    else:
        return outputs_dict_band_pass_fc[pin]

class _InputSpecBandPassFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_band_pass_fc(), op)
        self.fields_container = Input(_get_input_spec_band_pass_fc(0), 0, op, -1) 
        self.min_threshold = Input(_get_input_spec_band_pass_fc(1), 1, op, -1) 
        self.max_threshold = Input(_get_input_spec_band_pass_fc(2), 2, op, -1) 

class _OutputSpecBandPassFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_band_pass_fc(), op)
        self.fields_container = Output(_get_output_spec_band_pass_fc(0), 0, op) 

class _BandPassFc(_Operator):
    """Operator's description:
    Internal name is "core::field::band_pass_fc"
    Scripting name is "field.band_pass_fc"

    Description: The band pass filter returns all the values strictly superior to the min threshold value and stricly inferior to the max threshold value in input.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: min_threshold (a min threshold scalar or a field containing one value is expected)
       2: max_threshold (a max threshold scalar or a field containing one value is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::band_pass_fc")
    >>> op_way2 = core.operators.filter.field.band_pass_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("core::field::band_pass_fc")
        self.inputs = _InputSpecBandPassFc(self)
        self.outputs = _OutputSpecBandPassFc(self)

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

def band_pass_fc():
    """Operator's description:
    Internal name is "core::field::band_pass_fc"
    Scripting name is "field.band_pass_fc"

    Description: The band pass filter returns all the values strictly superior to the min threshold value and stricly inferior to the max threshold value in input.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: min_threshold (a min threshold scalar or a field containing one value is expected)
       2: max_threshold (a max threshold scalar or a field containing one value is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::band_pass_fc")
    >>> op_way2 = core.operators.filter.field.band_pass_fc()
    """
    return _BandPassFc()

#internal name: core::field::high_pass
#scripting name: field.high_pass
def _get_input_spec_high_pass(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "threshold", type_names = ["double","field"], optional = False, document = """a threshold scalar or a field containing one value is expected""")
    inputs_dict_high_pass = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_high_pass
    else:
        return inputs_dict_high_pass[pin]

def _get_output_spec_high_pass(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_high_pass = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_high_pass
    else:
        return outputs_dict_high_pass[pin]

class _InputSpecHighPass(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_high_pass(), op)
        self.field = Input(_get_input_spec_high_pass(0), 0, op, -1) 
        self.threshold = Input(_get_input_spec_high_pass(1), 1, op, -1) 

class _OutputSpecHighPass(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_high_pass(), op)
        self.field = Output(_get_output_spec_high_pass(0), 0, op) 

class _HighPass(_Operator):
    """Operator's description:
    Internal name is "core::field::high_pass"
    Scripting name is "field.high_pass"

    Description: The high pass filter returns all the values strictly superior to the threshold value in input.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: threshold (a threshold scalar or a field containing one value is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::high_pass")
    >>> op_way2 = core.operators.filter.field.high_pass()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("core::field::high_pass")
        self.inputs = _InputSpecHighPass(self)
        self.outputs = _OutputSpecHighPass(self)

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

def high_pass():
    """Operator's description:
    Internal name is "core::field::high_pass"
    Scripting name is "field.high_pass"

    Description: The high pass filter returns all the values strictly superior to the threshold value in input.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: threshold (a threshold scalar or a field containing one value is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::high_pass")
    >>> op_way2 = core.operators.filter.field.high_pass()
    """
    return _HighPass()

#internal name: core::field::high_pass_fc
#scripting name: field.high_pass_fc
def _get_input_spec_high_pass_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "threshold", type_names = ["double","field"], optional = False, document = """a threshold scalar or a field containing one value is expected""")
    inputs_dict_high_pass_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_high_pass_fc
    else:
        return inputs_dict_high_pass_fc[pin]

def _get_output_spec_high_pass_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_high_pass_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_high_pass_fc
    else:
        return outputs_dict_high_pass_fc[pin]

class _InputSpecHighPassFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_high_pass_fc(), op)
        self.fields_container = Input(_get_input_spec_high_pass_fc(0), 0, op, -1) 
        self.threshold = Input(_get_input_spec_high_pass_fc(1), 1, op, -1) 

class _OutputSpecHighPassFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_high_pass_fc(), op)
        self.fields_container = Output(_get_output_spec_high_pass_fc(0), 0, op) 

class _HighPassFc(_Operator):
    """Operator's description:
    Internal name is "core::field::high_pass_fc"
    Scripting name is "field.high_pass_fc"

    Description: The high pass filter returns all the values strictly superior to the threshold value in input.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: threshold (a threshold scalar or a field containing one value is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::high_pass_fc")
    >>> op_way2 = core.operators.filter.field.high_pass_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("core::field::high_pass_fc")
        self.inputs = _InputSpecHighPassFc(self)
        self.outputs = _OutputSpecHighPassFc(self)

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

def high_pass_fc():
    """Operator's description:
    Internal name is "core::field::high_pass_fc"
    Scripting name is "field.high_pass_fc"

    Description: The high pass filter returns all the values strictly superior to the threshold value in input.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: threshold (a threshold scalar or a field containing one value is expected)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::high_pass_fc")
    >>> op_way2 = core.operators.filter.field.high_pass_fc()
    """
    return _HighPassFc()

#internal name: core::field::low_pass
#scripting name: field.low_pass
def _get_input_spec_low_pass(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "threshold", type_names = ["double","field"], optional = False, document = """a threshold scalar or a field containing one value is expected""")
    inputs_dict_low_pass = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_low_pass
    else:
        return inputs_dict_low_pass[pin]

def _get_output_spec_low_pass(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_low_pass = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_low_pass
    else:
        return outputs_dict_low_pass[pin]

class _InputSpecLowPass(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_low_pass(), op)
        self.field = Input(_get_input_spec_low_pass(0), 0, op, -1) 
        self.threshold = Input(_get_input_spec_low_pass(1), 1, op, -1) 

class _OutputSpecLowPass(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_low_pass(), op)
        self.field = Output(_get_output_spec_low_pass(0), 0, op) 

class _LowPass(_Operator):
    """Operator's description:
    Internal name is "core::field::low_pass"
    Scripting name is "field.low_pass"

    Description: The low pass filter returns all the values strictly inferior to the threshold value in input.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: threshold (a threshold scalar or a field containing one value is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::low_pass")
    >>> op_way2 = core.operators.filter.field.low_pass()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("core::field::low_pass")
        self.inputs = _InputSpecLowPass(self)
        self.outputs = _OutputSpecLowPass(self)

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

def low_pass():
    """Operator's description:
    Internal name is "core::field::low_pass"
    Scripting name is "field.low_pass"

    Description: The low pass filter returns all the values strictly inferior to the threshold value in input.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: threshold (a threshold scalar or a field containing one value is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::low_pass")
    >>> op_way2 = core.operators.filter.field.low_pass()
    """
    return _LowPass()

#internal name: core::field::band_pass
#scripting name: field.band_pass
def _get_input_spec_band_pass(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "min_threshold", type_names = ["double","field"], optional = False, document = """a min threshold scalar or a field containing one value is expected""")
    inpin2 = _PinSpecification(name = "max_threshold", type_names = ["double","field"], optional = False, document = """a max threshold scalar or a field containing one value is expected""")
    inputs_dict_band_pass = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    if pin is None:
        return inputs_dict_band_pass
    else:
        return inputs_dict_band_pass[pin]

def _get_output_spec_band_pass(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_band_pass = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_band_pass
    else:
        return outputs_dict_band_pass[pin]

class _InputSpecBandPass(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_band_pass(), op)
        self.field = Input(_get_input_spec_band_pass(0), 0, op, -1) 
        self.min_threshold = Input(_get_input_spec_band_pass(1), 1, op, -1) 
        self.max_threshold = Input(_get_input_spec_band_pass(2), 2, op, -1) 

class _OutputSpecBandPass(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_band_pass(), op)
        self.field = Output(_get_output_spec_band_pass(0), 0, op) 

class _BandPass(_Operator):
    """Operator's description:
    Internal name is "core::field::band_pass"
    Scripting name is "field.band_pass"

    Description: The band pass filter returns all the values strictly superior to the min threshold value and stricly inferior to the max threshold value in input.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: min_threshold (a min threshold scalar or a field containing one value is expected)
       2: max_threshold (a max threshold scalar or a field containing one value is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::band_pass")
    >>> op_way2 = core.operators.filter.field.band_pass()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("core::field::band_pass")
        self.inputs = _InputSpecBandPass(self)
        self.outputs = _OutputSpecBandPass(self)

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

def band_pass():
    """Operator's description:
    Internal name is "core::field::band_pass"
    Scripting name is "field.band_pass"

    Description: The band pass filter returns all the values strictly superior to the min threshold value and stricly inferior to the max threshold value in input.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: min_threshold (a min threshold scalar or a field containing one value is expected)
       2: max_threshold (a max threshold scalar or a field containing one value is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("core::field::band_pass")
    >>> op_way2 = core.operators.filter.field.band_pass()
    """
    return _BandPass()

