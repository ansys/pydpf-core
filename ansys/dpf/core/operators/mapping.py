from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "mapping" category
"""

#internal name: solid_to_skin
#scripting name: solid_to_skin
def _get_input_spec_solid_to_skin(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["meshed_region"], optional = True, document = """skin mesh region expected""")
    inputs_dict_solid_to_skin = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_solid_to_skin
    else:
        return inputs_dict_solid_to_skin[pin]

def _get_output_spec_solid_to_skin(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_solid_to_skin = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_solid_to_skin
    else:
        return outputs_dict_solid_to_skin[pin]

class _InputSpecSolidToSkin(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_solid_to_skin(), op)
        self.field = Input(_get_input_spec_solid_to_skin(0), 0, op, -1) 
        super().__init__(_get_input_spec_solid_to_skin(), op)
        self.mesh_scoping = Input(_get_input_spec_solid_to_skin(1), 1, op, -1) 

class _OutputSpecSolidToSkin(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_solid_to_skin(), op)
        self.field = Output(_get_output_spec_solid_to_skin(0), 0, op) 

class _SolidToSkin(_Operator):
    """Operator's description:
    Internal name is "solid_to_skin"
    Scripting name is "solid_to_skin"

    Description: Maps a field defined on solid elements to a field defined on skin elements.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh_scoping (skin mesh region expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("solid_to_skin")
    >>> op_way2 = core.operators.mapping.solid_to_skin()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("solid_to_skin")
        self.inputs = _InputSpecSolidToSkin(self)
        self.outputs = _OutputSpecSolidToSkin(self)

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

def solid_to_skin():
    """Operator's description:
    Internal name is "solid_to_skin"
    Scripting name is "solid_to_skin"

    Description: Maps a field defined on solid elements to a field defined on skin elements.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh_scoping (skin mesh region expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("solid_to_skin")
    >>> op_way2 = core.operators.mapping.solid_to_skin()
    """
    return _SolidToSkin()

#internal name: mapping
#scripting name: on_coordinates
def _get_input_spec_on_coordinates(pin = None):
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
    if pin is None:
        return inputs_dict_on_coordinates
    else:
        return inputs_dict_on_coordinates[pin]

def _get_output_spec_on_coordinates(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_on_coordinates = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_on_coordinates
    else:
        return outputs_dict_on_coordinates[pin]

class _InputSpecOnCoordinates(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_on_coordinates(), op)
        self.fields_container = Input(_get_input_spec_on_coordinates(0), 0, op, -1) 
        super().__init__(_get_input_spec_on_coordinates(), op)
        self.coordinates = Input(_get_input_spec_on_coordinates(1), 1, op, -1) 
        super().__init__(_get_input_spec_on_coordinates(), op)
        self.create_support = Input(_get_input_spec_on_coordinates(2), 2, op, -1) 
        super().__init__(_get_input_spec_on_coordinates(), op)
        self.mapping_on_scoping = Input(_get_input_spec_on_coordinates(3), 3, op, -1) 
        super().__init__(_get_input_spec_on_coordinates(), op)
        self.mesh = Input(_get_input_spec_on_coordinates(7), 7, op, -1) 

class _OutputSpecOnCoordinates(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_on_coordinates(), op)
        self.fields_container = Output(_get_output_spec_on_coordinates(0), 0, op) 

class _OnCoordinates(_Operator):
    """Operator's description:
    Internal name is "mapping"
    Scripting name is "on_coordinates"

    Description: Evaluates a result on specified coordinates (interpolates results inside elements with shape functions).

    Input list: 
       0: fields_container 
       1: coordinates 
       2: create_support (if this pin is set to true, then, a support associated to the fields consisting of points is created)
       3: mapping_on_scoping (if this pin is set to true, then the mapping between the coordinates and the fields is created only on the first field scoping)
       7: mesh (if the first field in input has no mesh in support, then the mesh in this pin is expected (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapping")
    >>> op_way2 = core.operators.mapping.on_coordinates()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapping")
        self.inputs = _InputSpecOnCoordinates(self)
        self.outputs = _OutputSpecOnCoordinates(self)

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

def on_coordinates():
    """Operator's description:
    Internal name is "mapping"
    Scripting name is "on_coordinates"

    Description: Evaluates a result on specified coordinates (interpolates results inside elements with shape functions).

    Input list: 
       0: fields_container 
       1: coordinates 
       2: create_support (if this pin is set to true, then, a support associated to the fields consisting of points is created)
       3: mapping_on_scoping (if this pin is set to true, then the mapping between the coordinates and the fields is created only on the first field scoping)
       7: mesh (if the first field in input has no mesh in support, then the mesh in this pin is expected (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapping")
    >>> op_way2 = core.operators.mapping.on_coordinates()
    """
    return _OnCoordinates()

#internal name: scoping::on_coordinates
#scripting name: scoping_on_coordinates
def _get_input_spec_scoping_on_coordinates(pin = None):
    inpin0 = _PinSpecification(name = "coordinates", type_names = ["field"], optional = False, document = """""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inputs_dict_scoping_on_coordinates = { 
        0 : inpin0,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_scoping_on_coordinates
    else:
        return inputs_dict_scoping_on_coordinates[pin]

def _get_output_spec_scoping_on_coordinates(pin = None):
    outpin0 = _PinSpecification(name = "scoping", type_names = ["scoping"], document = """""")
    outputs_dict_scoping_on_coordinates = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_scoping_on_coordinates
    else:
        return outputs_dict_scoping_on_coordinates[pin]

class _InputSpecScopingOnCoordinates(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_scoping_on_coordinates(), op)
        self.coordinates = Input(_get_input_spec_scoping_on_coordinates(0), 0, op, -1) 
        super().__init__(_get_input_spec_scoping_on_coordinates(), op)
        self.mesh = Input(_get_input_spec_scoping_on_coordinates(7), 7, op, -1) 

class _OutputSpecScopingOnCoordinates(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_scoping_on_coordinates(), op)
        self.scoping = Output(_get_output_spec_scoping_on_coordinates(0), 0, op) 

class _ScopingOnCoordinates(_Operator):
    """Operator's description:
    Internal name is "scoping::on_coordinates"
    Scripting name is "scoping_on_coordinates"

    Description: Finds the Elemental scoping of a set of coordinates.

    Input list: 
       0: coordinates 
       7: mesh 

    Output list: 
       0: scoping 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("scoping::on_coordinates")
    >>> op_way2 = core.operators.mapping.scoping_on_coordinates()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("scoping::on_coordinates")
        self.inputs = _InputSpecScopingOnCoordinates(self)
        self.outputs = _OutputSpecScopingOnCoordinates(self)

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

def scoping_on_coordinates():
    """Operator's description:
    Internal name is "scoping::on_coordinates"
    Scripting name is "scoping_on_coordinates"

    Description: Finds the Elemental scoping of a set of coordinates.

    Input list: 
       0: coordinates 
       7: mesh 

    Output list: 
       0: scoping 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("scoping::on_coordinates")
    >>> op_way2 = core.operators.mapping.scoping_on_coordinates()
    """
    return _ScopingOnCoordinates()

