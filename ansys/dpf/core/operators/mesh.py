from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "mesh" category
"""

#internal name: GetSupportFromField
#scripting name: from_field
def _get_input_spec_from_field(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inputs_dict_from_field = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_from_field
    else:
        return inputs_dict_from_field[pin]

def _get_output_spec_from_field(pin = None):
    outpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], document = """""")
    outputs_dict_from_field = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_from_field
    else:
        return outputs_dict_from_field[pin]

class _InputSpecFromField(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_from_field(), op)
        self.field = Input(_get_input_spec_from_field(0), 0, op, -1) 

class _OutputSpecFromField(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_from_field(), op)
        self.mesh = Output(_get_output_spec_from_field(0), 0, op) 

class _FromField(_Operator):
    """Operator's description:
    Internal name is "GetSupportFromField"
    Scripting name is "from_field"

    Description: Returns the meshed region contained in the support of the mesh.

    Input list: 
       0: field 

    Output list: 
       0: mesh 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("GetSupportFromField")
    >>> op_way2 = core.operators.mesh.from_field()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("GetSupportFromField")
        self.inputs = _InputSpecFromField(self)
        self.outputs = _OutputSpecFromField(self)

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

def from_field():
    """Operator's description:
    Internal name is "GetSupportFromField"
    Scripting name is "from_field"

    Description: Returns the meshed region contained in the support of the mesh.

    Input list: 
       0: field 

    Output list: 
       0: mesh 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("GetSupportFromField")
    >>> op_way2 = core.operators.mesh.from_field()
    """
    return _FromField()

#internal name: MeshProvider
#scripting name: mesh_provider
def _get_input_spec_mesh_provider(pin = None):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_mesh_provider = { 
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_mesh_provider
    else:
        return inputs_dict_mesh_provider[pin]

def _get_output_spec_mesh_provider(pin = None):
    outpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], document = """""")
    outputs_dict_mesh_provider = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_mesh_provider
    else:
        return outputs_dict_mesh_provider[pin]

class _InputSpecMeshProvider(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_mesh_provider(), op)
        self.streams_container = Input(_get_input_spec_mesh_provider(3), 3, op, -1) 
        super().__init__(_get_input_spec_mesh_provider(), op)
        self.data_sources = Input(_get_input_spec_mesh_provider(4), 4, op, -1) 

class _OutputSpecMeshProvider(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_mesh_provider(), op)
        self.mesh = Output(_get_output_spec_mesh_provider(0), 0, op) 

class _MeshProvider(_Operator):
    """Operator's description:
    Internal name is "MeshProvider"
    Scripting name is "mesh_provider"

    Description: Read a mesh from result files and cure degenerated elements

    Input list: 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: mesh 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("MeshProvider")
    >>> op_way2 = core.operators.mesh.mesh_provider()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("MeshProvider")
        self.inputs = _InputSpecMeshProvider(self)
        self.outputs = _OutputSpecMeshProvider(self)

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

def mesh_provider():
    """Operator's description:
    Internal name is "MeshProvider"
    Scripting name is "mesh_provider"

    Description: Read a mesh from result files and cure degenerated elements

    Input list: 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: mesh 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("MeshProvider")
    >>> op_way2 = core.operators.mesh.mesh_provider()
    """
    return _MeshProvider()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "mesh" category
"""

#internal name: split_mesh
#scripting name: split_mesh
def _get_input_spec_split_mesh(pin = None):
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """Scoping""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin13 = _PinSpecification(name = "property", type_names = ["string"], optional = False, document = """""")
    inputs_dict_split_mesh = { 
        1 : inpin1,
        7 : inpin7,
        13 : inpin13
    }
    if pin is None:
        return inputs_dict_split_mesh
    else:
        return inputs_dict_split_mesh[pin]

def _get_output_spec_split_mesh(pin = None):
    outputs_dict_split_mesh = {
    }
    if pin is None:
        return outputs_dict_split_mesh
    else:
        return outputs_dict_split_mesh[pin]

class _InputSpecSplitMesh(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_split_mesh(), op)
        self.mesh_scoping = Input(_get_input_spec_split_mesh(1), 1, op, -1) 
        super().__init__(_get_input_spec_split_mesh(), op)
        self.mesh = Input(_get_input_spec_split_mesh(7), 7, op, -1) 
        super().__init__(_get_input_spec_split_mesh(), op)
        self.property = Input(_get_input_spec_split_mesh(13), 13, op, -1) 

class _OutputSpecSplitMesh(_Outputs):
    def __init__(self, op: _Operator):
        pass 

class _SplitMesh(_Operator):
    """Operator's description:
    Internal name is "split_mesh"
    Scripting name is "split_mesh"

    Description: Split the input mesh into several meshes based on a given property (material property be default)

    Input list: 
       1: mesh_scoping (Scoping)
       7: mesh 
       13: property 

    Output list: 
       empty 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("split_mesh")
    >>> op_way2 = core.operators.mesh.split_mesh()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("split_mesh")
        self.inputs = _InputSpecSplitMesh(self)
        self.outputs = _OutputSpecSplitMesh(self)

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

def split_mesh():
    """Operator's description:
    Internal name is "split_mesh"
    Scripting name is "split_mesh"

    Description: Split the input mesh into several meshes based on a given property (material property be default)

    Input list: 
       1: mesh_scoping (Scoping)
       7: mesh 
       13: property 

    Output list: 
       empty 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("split_mesh")
    >>> op_way2 = core.operators.mesh.split_mesh()
    """
    return _SplitMesh()

#internal name: mesh::by_scoping
#scripting name: from_scoping
def _get_input_spec_from_scoping(pin = None):
    inpin1 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = False, document = """if nodal scoping, then the scoping is transposed respecting the inclusive pin""")
    inpin2 = _PinSpecification(name = "inclusive", type_names = ["int32"], optional = True, document = """if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inputs_dict_from_scoping = { 
        1 : inpin1,
        2 : inpin2,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_from_scoping
    else:
        return inputs_dict_from_scoping[pin]

def _get_output_spec_from_scoping(pin = None):
    outpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], document = """""")
    outputs_dict_from_scoping = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_from_scoping
    else:
        return outputs_dict_from_scoping[pin]

class _InputSpecFromScoping(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_from_scoping(), op)
        self.scoping = Input(_get_input_spec_from_scoping(1), 1, op, -1) 
        super().__init__(_get_input_spec_from_scoping(), op)
        self.inclusive = Input(_get_input_spec_from_scoping(2), 2, op, -1) 
        super().__init__(_get_input_spec_from_scoping(), op)
        self.mesh = Input(_get_input_spec_from_scoping(7), 7, op, -1) 

class _OutputSpecFromScoping(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_from_scoping(), op)
        self.mesh = Output(_get_output_spec_from_scoping(0), 0, op) 

class _FromScoping(_Operator):
    """Operator's description:
    Internal name is "mesh::by_scoping"
    Scripting name is "from_scoping"

    Description: Extracts a meshed region from an other meshed region base on a scoping

    Input list: 
       1: scoping (if nodal scoping, then the scoping is transposed respecting the inclusive pin)
       2: inclusive (if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included)
       7: mesh 

    Output list: 
       0: mesh 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mesh::by_scoping")
    >>> op_way2 = core.operators.mesh.from_scoping()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mesh::by_scoping")
        self.inputs = _InputSpecFromScoping(self)
        self.outputs = _OutputSpecFromScoping(self)

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

def from_scoping():
    """Operator's description:
    Internal name is "mesh::by_scoping"
    Scripting name is "from_scoping"

    Description: Extracts a meshed region from an other meshed region base on a scoping

    Input list: 
       1: scoping (if nodal scoping, then the scoping is transposed respecting the inclusive pin)
       2: inclusive (if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included)
       7: mesh 

    Output list: 
       0: mesh 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mesh::by_scoping")
    >>> op_way2 = core.operators.mesh.from_scoping()
    """
    return _FromScoping()

#internal name: split_fields
#scripting name: split_fields
def _get_input_spec_split_fields(pin = None):
    inpin0 = _PinSpecification(name = "field_or_fields_container", type_names = ["field","fields_container"], optional = False, document = """""")
    inputs_dict_split_fields = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_split_fields
    else:
        return inputs_dict_split_fields[pin]

def _get_output_spec_split_fields(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_split_fields = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_split_fields
    else:
        return outputs_dict_split_fields[pin]

class _InputSpecSplitFields(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_split_fields(), op)
        self.field_or_fields_container = Input(_get_input_spec_split_fields(0), 0, op, -1) 

class _OutputSpecSplitFields(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_split_fields(), op)
        self.fields_container = Output(_get_output_spec_split_fields(0), 0, op) 

class _SplitFields(_Operator):
    """Operator's description:
    Internal name is "split_fields"
    Scripting name is "split_fields"

    Description: Split the input field or fields container based on the input mesh regions 

    Input list: 
       0: field_or_fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("split_fields")
    >>> op_way2 = core.operators.mesh.split_fields()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("split_fields")
        self.inputs = _InputSpecSplitFields(self)
        self.outputs = _OutputSpecSplitFields(self)

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

def split_fields():
    """Operator's description:
    Internal name is "split_fields"
    Scripting name is "split_fields"

    Description: Split the input field or fields container based on the input mesh regions 

    Input list: 
       0: field_or_fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("split_fields")
    >>> op_way2 = core.operators.mesh.split_fields()
    """
    return _SplitFields()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from meshOperatorsCore.dll plugin, from "mesh" category
"""

#internal name: meshed_skin_sector_triangle
#scripting name: tri_mesh_skin
def _get_input_spec_tri_mesh_skin(pin = None):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inputs_dict_tri_mesh_skin = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_tri_mesh_skin
    else:
        return inputs_dict_tri_mesh_skin[pin]

def _get_output_spec_tri_mesh_skin(pin = None):
    outpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], document = """""")
    outpin1 = _PinSpecification(name = "nodes_mesh_scoping", type_names = ["scoping"], document = """""")
    outputs_dict_tri_mesh_skin = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_tri_mesh_skin
    else:
        return outputs_dict_tri_mesh_skin[pin]

class _InputSpecTriMeshSkin(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_tri_mesh_skin(), op)
        self.mesh = Input(_get_input_spec_tri_mesh_skin(0), 0, op, -1) 

class _OutputSpecTriMeshSkin(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_tri_mesh_skin(), op)
        self.mesh = Output(_get_output_spec_tri_mesh_skin(0), 0, op) 
        super().__init__(_get_output_spec_tri_mesh_skin(), op)
        self.nodes_mesh_scoping = Output(_get_output_spec_tri_mesh_skin(1), 1, op) 

class _TriMeshSkin(_Operator):
    """Operator's description:
    Internal name is "meshed_skin_sector_triangle"
    Scripting name is "tri_mesh_skin"

    Description: Extracts a skin of the mesh in triangles (2D elements) in a new meshed region

    Input list: 
       0: mesh 

    Output list: 
       0: mesh 
       1: nodes_mesh_scoping 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("meshed_skin_sector_triangle")
    >>> op_way2 = core.operators.mesh.tri_mesh_skin()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("meshed_skin_sector_triangle")
        self.inputs = _InputSpecTriMeshSkin(self)
        self.outputs = _OutputSpecTriMeshSkin(self)

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

def tri_mesh_skin():
    """Operator's description:
    Internal name is "meshed_skin_sector_triangle"
    Scripting name is "tri_mesh_skin"

    Description: Extracts a skin of the mesh in triangles (2D elements) in a new meshed region

    Input list: 
       0: mesh 

    Output list: 
       0: mesh 
       1: nodes_mesh_scoping 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("meshed_skin_sector_triangle")
    >>> op_way2 = core.operators.mesh.tri_mesh_skin()
    """
    return _TriMeshSkin()

#internal name: mesh_cut
#scripting name: mesh_cut
def _get_input_spec_mesh_cut(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "iso_value", type_names = ["double"], optional = False, document = """iso value""")
    inpin3 = _PinSpecification(name = "closed_surface", type_names = ["double"], optional = False, document = """1: closed surface, 0:iso surface""")
    inputs_dict_mesh_cut = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3
    }
    if pin is None:
        return inputs_dict_mesh_cut
    else:
        return inputs_dict_mesh_cut[pin]

def _get_output_spec_mesh_cut(pin = None):
    outpin2 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], document = """""")
    outputs_dict_mesh_cut = { 
        2 : outpin2
    }
    if pin is None:
        return outputs_dict_mesh_cut
    else:
        return outputs_dict_mesh_cut[pin]

class _InputSpecMeshCut(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_mesh_cut(), op)
        self.field = Input(_get_input_spec_mesh_cut(0), 0, op, -1) 
        super().__init__(_get_input_spec_mesh_cut(), op)
        self.iso_value = Input(_get_input_spec_mesh_cut(1), 1, op, -1) 
        super().__init__(_get_input_spec_mesh_cut(), op)
        self.closed_surface = Input(_get_input_spec_mesh_cut(3), 3, op, -1) 

class _OutputSpecMeshCut(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_mesh_cut(), op)
        self.mesh = Output(_get_output_spec_mesh_cut(2), 2, op) 

class _MeshCut(_Operator):
    """Operator's description:
    Internal name is "mesh_cut"
    Scripting name is "mesh_cut"

    Description: Extracts a skin of the mesh in triangles (2D elements) in a new meshed region

    Input list: 
       0: field 
       1: iso_value (iso value)
       3: closed_surface (1: closed surface, 0:iso surface)

    Output list: 
       2: mesh 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mesh_cut")
    >>> op_way2 = core.operators.mesh.mesh_cut()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mesh_cut")
        self.inputs = _InputSpecMeshCut(self)
        self.outputs = _OutputSpecMeshCut(self)

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

def mesh_cut():
    """Operator's description:
    Internal name is "mesh_cut"
    Scripting name is "mesh_cut"

    Description: Extracts a skin of the mesh in triangles (2D elements) in a new meshed region

    Input list: 
       0: field 
       1: iso_value (iso value)
       3: closed_surface (1: closed surface, 0:iso surface)

    Output list: 
       2: mesh 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mesh_cut")
    >>> op_way2 = core.operators.mesh.mesh_cut()
    """
    return _MeshCut()

#internal name: meshed_external_layer_sector
#scripting name: external_layer
def _get_input_spec_external_layer(pin = None):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inputs_dict_external_layer = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_external_layer
    else:
        return inputs_dict_external_layer[pin]

def _get_output_spec_external_layer(pin = None):
    outpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], document = """""")
    outpin1 = _PinSpecification(name = "nodes_mesh_scoping", type_names = ["scoping"], document = """""")
    outpin2 = _PinSpecification(name = "elements_mesh_scoping", type_names = ["scoping"], document = """""")
    outputs_dict_external_layer = { 
        0 : outpin0,
        1 : outpin1,
        2 : outpin2
    }
    if pin is None:
        return outputs_dict_external_layer
    else:
        return outputs_dict_external_layer[pin]

class _InputSpecExternalLayer(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_external_layer(), op)
        self.mesh = Input(_get_input_spec_external_layer(0), 0, op, -1) 

class _OutputSpecExternalLayer(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_external_layer(), op)
        self.mesh = Output(_get_output_spec_external_layer(0), 0, op) 
        super().__init__(_get_output_spec_external_layer(), op)
        self.nodes_mesh_scoping = Output(_get_output_spec_external_layer(1), 1, op) 
        super().__init__(_get_output_spec_external_layer(), op)
        self.elements_mesh_scoping = Output(_get_output_spec_external_layer(2), 2, op) 

class _ExternalLayer(_Operator):
    """Operator's description:
    Internal name is "meshed_external_layer_sector"
    Scripting name is "external_layer"

    Description: Extracts the external layer (thick skin) of the mesh (3D elements) in a new meshed region

    Input list: 
       0: mesh 

    Output list: 
       0: mesh 
       1: nodes_mesh_scoping 
       2: elements_mesh_scoping 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("meshed_external_layer_sector")
    >>> op_way2 = core.operators.mesh.external_layer()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("meshed_external_layer_sector")
        self.inputs = _InputSpecExternalLayer(self)
        self.outputs = _OutputSpecExternalLayer(self)

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

def external_layer():
    """Operator's description:
    Internal name is "meshed_external_layer_sector"
    Scripting name is "external_layer"

    Description: Extracts the external layer (thick skin) of the mesh (3D elements) in a new meshed region

    Input list: 
       0: mesh 

    Output list: 
       0: mesh 
       1: nodes_mesh_scoping 
       2: elements_mesh_scoping 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("meshed_external_layer_sector")
    >>> op_way2 = core.operators.mesh.external_layer()
    """
    return _ExternalLayer()

#internal name: meshed_skin_sector
#scripting name: skin
def _get_input_spec_skin(pin = None):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inputs_dict_skin = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_skin
    else:
        return inputs_dict_skin[pin]

def _get_output_spec_skin(pin = None):
    outpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], document = """skin meshed region with facets and facets_to_ele property fields""")
    outpin1 = _PinSpecification(name = "nodes_mesh_scoping", type_names = ["scoping"], document = """""")
    outpin3 = _PinSpecification(name = "property_field_new_elements_to_old", type_names = ["property_field"], document = """""")
    outputs_dict_skin = { 
        0 : outpin0,
        1 : outpin1,
        3 : outpin3
    }
    if pin is None:
        return outputs_dict_skin
    else:
        return outputs_dict_skin[pin]

class _InputSpecSkin(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_skin(), op)
        self.mesh = Input(_get_input_spec_skin(0), 0, op, -1) 
        super().__init__(_get_input_spec_skin(), op)
        self.mesh_scoping = Input(_get_input_spec_skin(1), 1, op, -1) 

class _OutputSpecSkin(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_skin(), op)
        self.mesh = Output(_get_output_spec_skin(0), 0, op) 
        super().__init__(_get_output_spec_skin(), op)
        self.nodes_mesh_scoping = Output(_get_output_spec_skin(1), 1, op) 
        pass 
        super().__init__(_get_output_spec_skin(), op)
        self.property_field_new_elements_to_old = Output(_get_output_spec_skin(3), 3, op) 

class _Skin(_Operator):
    """Operator's description:
    Internal name is "meshed_skin_sector"
    Scripting name is "skin"

    Description: Extracts a skin of the mesh (2D elements) in a new meshed region

    Input list: 
       0: mesh 
       1: mesh_scoping 

    Output list: 
       0: mesh (skin meshed region with facets and facets_to_ele property fields)
       1: nodes_mesh_scoping 
       empty 
       3: property_field_new_elements_to_old 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("meshed_skin_sector")
    >>> op_way2 = core.operators.mesh.skin()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("meshed_skin_sector")
        self.inputs = _InputSpecSkin(self)
        self.outputs = _OutputSpecSkin(self)

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

def skin():
    """Operator's description:
    Internal name is "meshed_skin_sector"
    Scripting name is "skin"

    Description: Extracts a skin of the mesh (2D elements) in a new meshed region

    Input list: 
       0: mesh 
       1: mesh_scoping 

    Output list: 
       0: mesh (skin meshed region with facets and facets_to_ele property fields)
       1: nodes_mesh_scoping 
       empty 
       3: property_field_new_elements_to_old 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("meshed_skin_sector")
    >>> op_way2 = core.operators.mesh.skin()
    """
    return _Skin()

#internal name: stl_export
#scripting name: stl_export
def _get_input_spec_stl_export(pin = None):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "file_path", type_names = ["string"], optional = False, document = """""")
    inputs_dict_stl_export = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_stl_export
    else:
        return inputs_dict_stl_export[pin]

def _get_output_spec_stl_export(pin = None):
    outpin0 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], document = """""")
    outputs_dict_stl_export = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stl_export
    else:
        return outputs_dict_stl_export[pin]

class _InputSpecStlExport(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stl_export(), op)
        self.mesh = Input(_get_input_spec_stl_export(0), 0, op, -1) 
        super().__init__(_get_input_spec_stl_export(), op)
        self.file_path = Input(_get_input_spec_stl_export(1), 1, op, -1) 

class _OutputSpecStlExport(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stl_export(), op)
        self.data_sources = Output(_get_output_spec_stl_export(0), 0, op) 

class _StlExport(_Operator):
    """Operator's description:
    Internal name is "stl_export"
    Scripting name is "stl_export"

    Description: export a mesh into a stl file.

    Input list: 
       0: mesh 
       1: file_path 

    Output list: 
       0: data_sources 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("stl_export")
    >>> op_way2 = core.operators.mesh.stl_export()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("stl_export")
        self.inputs = _InputSpecStlExport(self)
        self.outputs = _OutputSpecStlExport(self)

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

def stl_export():
    """Operator's description:
    Internal name is "stl_export"
    Scripting name is "stl_export"

    Description: export a mesh into a stl file.

    Input list: 
       0: mesh 
       1: file_path 

    Output list: 
       0: data_sources 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("stl_export")
    >>> op_way2 = core.operators.mesh.stl_export()
    """
    return _StlExport()

