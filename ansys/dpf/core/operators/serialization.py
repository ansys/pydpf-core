from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "serialization" category
"""

#internal name: serializer
#scripting name: serializer
def _get_input_spec_serializer(pin = None):
    inpin0 = _PinSpecification(name = "file_path", type_names = ["string"], optional = False, document = """""")
    inputs_dict_serializer = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_serializer
    else:
        return inputs_dict_serializer[pin]

def _get_output_spec_serializer(pin = None):
    outpin0 = _PinSpecification(name = "file_path", type_names = ["string"], document = """""")
    outputs_dict_serializer = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_serializer
    else:
        return outputs_dict_serializer[pin]

class _InputSpecSerializer(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_serializer(), op)
        self.file_path = Input(_get_input_spec_serializer(0), 0, op, -1) 

class _OutputSpecSerializer(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_serializer(), op)
        self.file_path = Output(_get_output_spec_serializer(0), 0, op) 

class _Serializer(_Operator):
    """Operator's description:
    Internal name is "serializer"
    Scripting name is "serializer"

    Description: Take any input and serialize them in a file.

    Input list: 
       0: file_path 

    Output list: 
       0: file_path 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("serializer")
    >>> op_way2 = core.operators.serialization.serializer()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("serializer")
        self.inputs = _InputSpecSerializer(self)
        self.outputs = _OutputSpecSerializer(self)

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

def serializer():
    """Operator's description:
    Internal name is "serializer"
    Scripting name is "serializer"

    Description: Take any input and serialize them in a file.

    Input list: 
       0: file_path 

    Output list: 
       0: file_path 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("serializer")
    >>> op_way2 = core.operators.serialization.serializer()
    """
    return _Serializer()

#internal name: mechanical_csv_to_field
#scripting name: mechanical_csv_to_field
def _get_input_spec_mechanical_csv_to_field(pin = None):
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string","field_definition"], optional = False, document = """""")
    inputs_dict_mechanical_csv_to_field = { 
        1 : inpin1,
        4 : inpin4,
        9 : inpin9
    }
    if pin is None:
        return inputs_dict_mechanical_csv_to_field
    else:
        return inputs_dict_mechanical_csv_to_field[pin]

def _get_output_spec_mechanical_csv_to_field(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_mechanical_csv_to_field = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_mechanical_csv_to_field
    else:
        return outputs_dict_mechanical_csv_to_field[pin]

class _InputSpecMechanicalCsvToField(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_mechanical_csv_to_field(), op)
        self.mesh = Input(_get_input_spec_mechanical_csv_to_field(1), 1, op, -1) 
        super().__init__(_get_input_spec_mechanical_csv_to_field(), op)
        self.data_sources = Input(_get_input_spec_mechanical_csv_to_field(4), 4, op, -1) 
        super().__init__(_get_input_spec_mechanical_csv_to_field(), op)
        self.requested_location = Input(_get_input_spec_mechanical_csv_to_field(9), 9, op, -1) 

class _OutputSpecMechanicalCsvToField(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_mechanical_csv_to_field(), op)
        self.field = Output(_get_output_spec_mechanical_csv_to_field(0), 0, op) 

class _MechanicalCsvToField(_Operator):
    """Operator's description:
    Internal name is "mechanical_csv_to_field"
    Scripting name is "mechanical_csv_to_field"

    Description: Reads mechanical exported csv file

    Input list: 
       1: mesh 
       4: data_sources 
       9: requested_location 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mechanical_csv_to_field")
    >>> op_way2 = core.operators.serialization.mechanical_csv_to_field()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mechanical_csv_to_field")
        self.inputs = _InputSpecMechanicalCsvToField(self)
        self.outputs = _OutputSpecMechanicalCsvToField(self)

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

def mechanical_csv_to_field():
    """Operator's description:
    Internal name is "mechanical_csv_to_field"
    Scripting name is "mechanical_csv_to_field"

    Description: Reads mechanical exported csv file

    Input list: 
       1: mesh 
       4: data_sources 
       9: requested_location 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mechanical_csv_to_field")
    >>> op_way2 = core.operators.serialization.mechanical_csv_to_field()
    """
    return _MechanicalCsvToField()

#internal name: field_to_csv
#scripting name: field_to_csv
def _get_input_spec_field_to_csv(pin = None):
    inpin0 = _PinSpecification(name = "field_or_fields_container", type_names = ["fields_container","field"], optional = False, document = """field_or_fields_container""")
    inpin1 = _PinSpecification(name = "file_path", type_names = ["string"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "storage_type", type_names = ["int32"], optional = True, document = """storage type : if matrices (without any particularity) are included in the fields container, the storage format can be chosen. 0 : flat/line format, 1 : ranked format. If 1 is chosen, the csv can not be read by "csv to field" operator anymore. Default : 0.""")
    inputs_dict_field_to_csv = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    if pin is None:
        return inputs_dict_field_to_csv
    else:
        return inputs_dict_field_to_csv[pin]

def _get_output_spec_field_to_csv(pin = None):
    outputs_dict_field_to_csv = {
    }
    if pin is None:
        return outputs_dict_field_to_csv
    else:
        return outputs_dict_field_to_csv[pin]

class _InputSpecFieldToCsv(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_field_to_csv(), op)
        self.field_or_fields_container = Input(_get_input_spec_field_to_csv(0), 0, op, -1) 
        super().__init__(_get_input_spec_field_to_csv(), op)
        self.file_path = Input(_get_input_spec_field_to_csv(1), 1, op, -1) 
        super().__init__(_get_input_spec_field_to_csv(), op)
        self.storage_type = Input(_get_input_spec_field_to_csv(2), 2, op, -1) 

class _OutputSpecFieldToCsv(_Outputs):
    def __init__(self, op: _Operator):
        pass 

class _FieldToCsv(_Operator):
    """Operator's description:
    Internal name is "field_to_csv"
    Scripting name is "field_to_csv"

    Description: Exports a field or a fields container into a csv file

    Input list: 
       0: field_or_fields_container (field_or_fields_container)
       1: file_path 
       2: storage_type (storage type : if matrices (without any particularity) are included in the fields container, the storage format can be chosen. 0 : flat/line format, 1 : ranked format. If 1 is chosen, the csv can not be read by "csv to field" operator anymore. Default : 0.)

    Output list: 
       empty 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("field_to_csv")
    >>> op_way2 = core.operators.serialization.field_to_csv()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("field_to_csv")
        self.inputs = _InputSpecFieldToCsv(self)
        self.outputs = _OutputSpecFieldToCsv(self)

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

def field_to_csv():
    """Operator's description:
    Internal name is "field_to_csv"
    Scripting name is "field_to_csv"

    Description: Exports a field or a fields container into a csv file

    Input list: 
       0: field_or_fields_container (field_or_fields_container)
       1: file_path 
       2: storage_type (storage type : if matrices (without any particularity) are included in the fields container, the storage format can be chosen. 0 : flat/line format, 1 : ranked format. If 1 is chosen, the csv can not be read by "csv to field" operator anymore. Default : 0.)

    Output list: 
       empty 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("field_to_csv")
    >>> op_way2 = core.operators.serialization.field_to_csv()
    """
    return _FieldToCsv()

#internal name: deserializer
#scripting name: deserializer
def _get_input_spec_deserializer(pin = None):
    inpin0 = _PinSpecification(name = "file_path", type_names = ["string"], optional = False, document = """file path""")
    inputs_dict_deserializer = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_deserializer
    else:
        return inputs_dict_deserializer[pin]

def _get_output_spec_deserializer(pin = None):
    outputs_dict_deserializer = {
    }
    if pin is None:
        return outputs_dict_deserializer
    else:
        return outputs_dict_deserializer[pin]

class _InputSpecDeserializer(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_deserializer(), op)
        self.file_path = Input(_get_input_spec_deserializer(0), 0, op, -1) 

class _OutputSpecDeserializer(_Outputs):
    def __init__(self, op: _Operator):
        pass 
        pass 

class _Deserializer(_Operator):
    """Operator's description:
    Internal name is "deserializer"
    Scripting name is "deserializer"

    Description: Takes a file generated by the serializer and deserializes it into DPF's enitities.

    Input list: 
       0: file_path (file path)

    Output list: 
       empty 
       empty 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("deserializer")
    >>> op_way2 = core.operators.serialization.deserializer()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("deserializer")
        self.inputs = _InputSpecDeserializer(self)
        self.outputs = _OutputSpecDeserializer(self)

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

def deserializer():
    """Operator's description:
    Internal name is "deserializer"
    Scripting name is "deserializer"

    Description: Takes a file generated by the serializer and deserializes it into DPF's enitities.

    Input list: 
       0: file_path (file path)

    Output list: 
       empty 
       empty 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("deserializer")
    >>> op_way2 = core.operators.serialization.deserializer()
    """
    return _Deserializer()

#internal name: csv_to_field
#scripting name: csv_to_field
def _get_input_spec_csv_to_field(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing a file with csv extension""")
    inputs_dict_csv_to_field = { 
        0 : inpin0,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_csv_to_field
    else:
        return inputs_dict_csv_to_field[pin]

def _get_output_spec_csv_to_field(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_csv_to_field = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_csv_to_field
    else:
        return outputs_dict_csv_to_field[pin]

class _InputSpecCsvToField(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_csv_to_field(), op)
        self.time_scoping = Input(_get_input_spec_csv_to_field(0), 0, op, -1) 
        super().__init__(_get_input_spec_csv_to_field(), op)
        self.data_sources = Input(_get_input_spec_csv_to_field(4), 4, op, -1) 

class _OutputSpecCsvToField(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_csv_to_field(), op)
        self.fields_container = Output(_get_output_spec_csv_to_field(0), 0, op) 

class _CsvToField(_Operator):
    """Operator's description:
    Internal name is "csv_to_field"
    Scripting name is "csv_to_field"

    Description: transform csv file to a field or fields container

    Input list: 
       0: time_scoping 
       4: data_sources (data sources containing a file with csv extension)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("csv_to_field")
    >>> op_way2 = core.operators.serialization.csv_to_field()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("csv_to_field")
        self.inputs = _InputSpecCsvToField(self)
        self.outputs = _OutputSpecCsvToField(self)

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

def csv_to_field():
    """Operator's description:
    Internal name is "csv_to_field"
    Scripting name is "csv_to_field"

    Description: transform csv file to a field or fields container

    Input list: 
       0: time_scoping 
       4: data_sources (data sources containing a file with csv extension)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("csv_to_field")
    >>> op_way2 = core.operators.serialization.csv_to_field()
    """
    return _CsvToField()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from meshOperatorsCore.dll plugin, from "serialization" category
"""

#internal name: vtk_export
#scripting name: vtk_export
def _get_input_spec_vtk_export(pin = None):
    inpin0 = _PinSpecification(name = "file_path", type_names = ["string"], optional = False, document = """path with vtk extension were the export occurs""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """necessary if the first field or fields container don't have a mesh in their support""")
    inpin2 = _PinSpecification(name = "fields1", type_names = ["fields_container","field"], optional = False, document = """fields exported""")
    inpin3 = _PinSpecification(name = "fields2", type_names = ["fields_container","field"], optional = False, document = """""")
    inputs_dict_vtk_export = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    if pin is None:
        return inputs_dict_vtk_export
    else:
        return inputs_dict_vtk_export[pin]

def _get_output_spec_vtk_export(pin = None):
    outputs_dict_vtk_export = {
    }
    if pin is None:
        return outputs_dict_vtk_export
    else:
        return outputs_dict_vtk_export[pin]

class _InputSpecVtkExport(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_vtk_export(), op)
        self.file_path = Input(_get_input_spec_vtk_export(0), 0, op, -1) 
        super().__init__(_get_input_spec_vtk_export(), op)
        self.mesh = Input(_get_input_spec_vtk_export(1), 1, op, -1) 
        super().__init__(_get_input_spec_vtk_export(), op)
        self.fields1 = Input(_get_input_spec_vtk_export(2), 2, op, 0) 
        super().__init__(_get_input_spec_vtk_export(), op)
        self.fields2 = Input(_get_input_spec_vtk_export(3), 3, op, -1) 

class _OutputSpecVtkExport(_Outputs):
    def __init__(self, op: _Operator):
        pass 

class _VtkExport(_Operator):
    """Operator's description:
    Internal name is "vtk_export"
    Scripting name is "vtk_export"

    Description: Write the input field and fields container into a given vtk path

    Input list: 
       0: file_path (path with vtk extension were the export occurs)
       1: mesh (necessary if the first field or fields container don't have a mesh in their support)
       2: fields1 (fields exported)
       3: fields2 

    Output list: 
       empty 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("vtk_export")
    >>> op_way2 = core.operators.serialization.vtk_export()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("vtk_export")
        self.inputs = _InputSpecVtkExport(self)
        self.outputs = _OutputSpecVtkExport(self)

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

def vtk_export():
    """Operator's description:
    Internal name is "vtk_export"
    Scripting name is "vtk_export"

    Description: Write the input field and fields container into a given vtk path

    Input list: 
       0: file_path (path with vtk extension were the export occurs)
       1: mesh (necessary if the first field or fields container don't have a mesh in their support)
       2: fields1 (fields exported)
       3: fields2 

    Output list: 
       empty 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("vtk_export")
    >>> op_way2 = core.operators.serialization.vtk_export()
    """
    return _VtkExport()

