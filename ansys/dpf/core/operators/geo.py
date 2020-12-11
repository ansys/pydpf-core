from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "geo" category
"""

#internal name: topology::mass
#scripting name: mass
def _get_input_spec_mass(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """Mesh scoping, if not set, all the elements of the mesh are considered.""")
    inpin2 = _PinSpecification(name = "field", type_names = ["field"], optional = True, document = """Elemental or nodal ponderation used in computation.""")
    inputs_dict_mass = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_mass[pin]

def _get_output_spec_mass(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_mass = { 
        0 : outpin0
    }
    return outputs_dict_mass[pin]

class _InputSpecMass(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_mass(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_mass(1), 1, op, -1) 
        self.field = _Input(_get_input_spec_mass(2), 2, op, -1) 

class _OutputSpecMass(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_mass(0), 0, op) 

class _Mass(_Operator):
    """Operator's description:
    Internal name is "topology::mass"
    Scripting name is "mass"

    Description: Compute the mass of a set of elements.

    Input list: 
       0: mesh 
       1: mesh_scoping (Mesh scoping, if not set, all the elements of the mesh are considered.)
       2: field (Elemental or nodal ponderation used in computation.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("topology::mass")
    >>> op_way2 = core.operators.geo.mass()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("topology::mass")
        self._name = "topology::mass"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecMass(self._op)
        self.outputs = _OutputSpecMass(self._op)

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

def mass():
    """Operator's description:
    Internal name is "topology::mass"
    Scripting name is "mass"

    Description: Compute the mass of a set of elements.

    Input list: 
       0: mesh 
       1: mesh_scoping (Mesh scoping, if not set, all the elements of the mesh are considered.)
       2: field (Elemental or nodal ponderation used in computation.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("topology::mass")
    >>> op_way2 = core.operators.geo.mass()
    """
    return _Mass()

#internal name: normals_provider_nl
#scripting name: normals_provider_nl
def _get_input_spec_normals_provider_nl(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """skin or shell mesh region""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = False, document = """""")
    inputs_dict_normals_provider_nl = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_normals_provider_nl[pin]

def _get_output_spec_normals_provider_nl(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_normals_provider_nl = { 
        0 : outpin0
    }
    return outputs_dict_normals_provider_nl[pin]

class _InputSpecNormalsProviderNl(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_normals_provider_nl(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_normals_provider_nl(1), 1, op, -1) 

class _OutputSpecNormalsProviderNl(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_normals_provider_nl(0), 0, op) 

class _NormalsProviderNl(_Operator):
    """Operator's description:
    Internal name is "normals_provider_nl"
    Scripting name is "normals_provider_nl"

    Description: Compute the normals on nodes/elements based on integration points(more accurate for non-linear elements), on a skin mesh

    Input list: 
       0: mesh (skin or shell mesh region)
       1: mesh_scoping 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("normals_provider_nl")
    >>> op_way2 = core.operators.geo.normals_provider_nl()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("normals_provider_nl")
        self._name = "normals_provider_nl"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecNormalsProviderNl(self._op)
        self.outputs = _OutputSpecNormalsProviderNl(self._op)

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

def normals_provider_nl():
    """Operator's description:
    Internal name is "normals_provider_nl"
    Scripting name is "normals_provider_nl"

    Description: Compute the normals on nodes/elements based on integration points(more accurate for non-linear elements), on a skin mesh

    Input list: 
       0: mesh (skin or shell mesh region)
       1: mesh_scoping 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("normals_provider_nl")
    >>> op_way2 = core.operators.geo.normals_provider_nl()
    """
    return _NormalsProviderNl()

#internal name: transform_cylindrical_cs_fc
#scripting name: to_cylindrical_cs_fc
def _get_input_spec_to_cylindrical_cs_fc(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "coordinate_system", type_names = ["field"], optional = True, document = """3-3 rotation matrix and origin coordinates must be set here to define a coordinate system.""")
    inputs_dict_to_cylindrical_cs_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_to_cylindrical_cs_fc[pin]

def _get_output_spec_to_cylindrical_cs_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_to_cylindrical_cs_fc = { 
        0 : outpin0
    }
    return outputs_dict_to_cylindrical_cs_fc[pin]

class _InputSpecToCylindricalCsFc(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_to_cylindrical_cs_fc(0), 0, op, -1) 
        self.coordinate_system = _Input(_get_input_spec_to_cylindrical_cs_fc(1), 1, op, -1) 

class _OutputSpecToCylindricalCsFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_to_cylindrical_cs_fc(0), 0, op) 

class _ToCylindricalCsFc(_Operator):
    """Operator's description:
    Internal name is "transform_cylindrical_cs_fc"
    Scripting name is "to_cylindrical_cs_fc"

    Description: Transform all the fields of a fields container (not defined with a cynlindrical coordinate system) to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.

    Input list: 
       0: field 
       1: coordinate_system (3-3 rotation matrix and origin coordinates must be set here to define a coordinate system.)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("transform_cylindrical_cs_fc")
    >>> op_way2 = core.operators.geo.to_cylindrical_cs_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("transform_cylindrical_cs_fc")
        self._name = "transform_cylindrical_cs_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecToCylindricalCsFc(self._op)
        self.outputs = _OutputSpecToCylindricalCsFc(self._op)

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

def to_cylindrical_cs_fc():
    """Operator's description:
    Internal name is "transform_cylindrical_cs_fc"
    Scripting name is "to_cylindrical_cs_fc"

    Description: Transform all the fields of a fields container (not defined with a cynlindrical coordinate system) to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.

    Input list: 
       0: field 
       1: coordinate_system (3-3 rotation matrix and origin coordinates must be set here to define a coordinate system.)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("transform_cylindrical_cs_fc")
    >>> op_way2 = core.operators.geo.to_cylindrical_cs_fc()
    """
    return _ToCylindricalCsFc()

#internal name: element::integrate
#scripting name: integrate_over_elements
def _get_input_spec_integrate_over_elements(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """Integrate the input field over a specific scoping.""")
    inpin2 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """Mesh to integrate on, if not provided the one from input field is provided.""")
    inputs_dict_integrate_over_elements = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_integrate_over_elements[pin]

def _get_output_spec_integrate_over_elements(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_integrate_over_elements = { 
        0 : outpin0
    }
    return outputs_dict_integrate_over_elements[pin]

class _InputSpecIntegrateOverElements(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_integrate_over_elements(0), 0, op, -1) 
        self.scoping = _Input(_get_input_spec_integrate_over_elements(1), 1, op, -1) 
        self.mesh = _Input(_get_input_spec_integrate_over_elements(2), 2, op, -1) 

class _OutputSpecIntegrateOverElements(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_integrate_over_elements(0), 0, op) 

class _IntegrateOverElements(_Operator):
    """Operator's description:
    Internal name is "element::integrate"
    Scripting name is "integrate_over_elements"

    Description: Integration of an input field over mesh.

    Input list: 
       0: field 
       1: scoping (Integrate the input field over a specific scoping.)
       2: mesh (Mesh to integrate on, if not provided the one from input field is provided.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("element::integrate")
    >>> op_way2 = core.operators.geo.integrate_over_elements()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("element::integrate")
        self._name = "element::integrate"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecIntegrateOverElements(self._op)
        self.outputs = _OutputSpecIntegrateOverElements(self._op)

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

def integrate_over_elements():
    """Operator's description:
    Internal name is "element::integrate"
    Scripting name is "integrate_over_elements"

    Description: Integration of an input field over mesh.

    Input list: 
       0: field 
       1: scoping (Integrate the input field over a specific scoping.)
       2: mesh (Mesh to integrate on, if not provided the one from input field is provided.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("element::integrate")
    >>> op_way2 = core.operators.geo.integrate_over_elements()
    """
    return _IntegrateOverElements()

#internal name: topology::center_of_gravity
#scripting name: center_of_gravity
def _get_input_spec_center_of_gravity(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """Mesh scoping, if not set, all the elements of the mesh are considered.""")
    inpin2 = _PinSpecification(name = "field", type_names = ["field"], optional = True, document = """Elemental or nodal ponderation used in computation.""")
    inputs_dict_center_of_gravity = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_center_of_gravity[pin]

def _get_output_spec_center_of_gravity(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], document = """Center of gravity as a mesh""")
    outputs_dict_center_of_gravity = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_center_of_gravity[pin]

class _InputSpecCenterOfGravity(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_center_of_gravity(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_center_of_gravity(1), 1, op, -1) 
        self.field = _Input(_get_input_spec_center_of_gravity(2), 2, op, -1) 

class _OutputSpecCenterOfGravity(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_center_of_gravity(0), 0, op) 
        self.mesh = _Output(_get_output_spec_center_of_gravity(1), 1, op) 

class _CenterOfGravity(_Operator):
    """Operator's description:
    Internal name is "topology::center_of_gravity"
    Scripting name is "center_of_gravity"

    Description: Compute the center of gravity of a set of elements

    Input list: 
       0: mesh 
       1: mesh_scoping (Mesh scoping, if not set, all the elements of the mesh are considered.)
       2: field (Elemental or nodal ponderation used in computation.)

    Output list: 
       0: field 
       1: mesh (Center of gravity as a mesh)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("topology::center_of_gravity")
    >>> op_way2 = core.operators.geo.center_of_gravity()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("topology::center_of_gravity")
        self._name = "topology::center_of_gravity"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecCenterOfGravity(self._op)
        self.outputs = _OutputSpecCenterOfGravity(self._op)

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

def center_of_gravity():
    """Operator's description:
    Internal name is "topology::center_of_gravity"
    Scripting name is "center_of_gravity"

    Description: Compute the center of gravity of a set of elements

    Input list: 
       0: mesh 
       1: mesh_scoping (Mesh scoping, if not set, all the elements of the mesh are considered.)
       2: field (Elemental or nodal ponderation used in computation.)

    Output list: 
       0: field 
       1: mesh (Center of gravity as a mesh)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("topology::center_of_gravity")
    >>> op_way2 = core.operators.geo.center_of_gravity()
    """
    return _CenterOfGravity()

#internal name: transform_cylindricalCS
#scripting name: to_cylindrical_cs
def _get_input_spec_to_cylindrical_cs(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "coordinate_system", type_names = ["field"], optional = True, document = """3-3 rotation matrix and origin coordinates must be set here to define a coordinate system.""")
    inputs_dict_to_cylindrical_cs = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_to_cylindrical_cs[pin]

def _get_output_spec_to_cylindrical_cs(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_to_cylindrical_cs = { 
        0 : outpin0
    }
    return outputs_dict_to_cylindrical_cs[pin]

class _InputSpecToCylindricalCs(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_to_cylindrical_cs(0), 0, op, -1) 
        self.coordinate_system = _Input(_get_input_spec_to_cylindrical_cs(1), 1, op, -1) 

class _OutputSpecToCylindricalCs(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_to_cylindrical_cs(0), 0, op) 

class _ToCylindricalCs(_Operator):
    """Operator's description:
    Internal name is "transform_cylindricalCS"
    Scripting name is "to_cylindrical_cs"

    Description: Transform a field (not defined with a cynlindrical coordinate system) to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: coordinate_system (3-3 rotation matrix and origin coordinates must be set here to define a coordinate system.)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("transform_cylindricalCS")
    >>> op_way2 = core.operators.geo.to_cylindrical_cs()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("transform_cylindricalCS")
        self._name = "transform_cylindricalCS"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecToCylindricalCs(self._op)
        self.outputs = _OutputSpecToCylindricalCs(self._op)

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

def to_cylindrical_cs():
    """Operator's description:
    Internal name is "transform_cylindricalCS"
    Scripting name is "to_cylindrical_cs"

    Description: Transform a field (not defined with a cynlindrical coordinate system) to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: coordinate_system (3-3 rotation matrix and origin coordinates must be set here to define a coordinate system.)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("transform_cylindricalCS")
    >>> op_way2 = core.operators.geo.to_cylindrical_cs()
    """
    return _ToCylindricalCs()

#internal name: rotate
#scripting name: rotate
def _get_input_spec_rotate(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "field_rotation_matrix", type_names = ["field"], optional = False, document = """3-3 rotation matrix""")
    inputs_dict_rotate = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_rotate[pin]

def _get_output_spec_rotate(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_rotate = { 
        0 : outpin0
    }
    return outputs_dict_rotate[pin]

class _InputSpecRotate(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_rotate(0), 0, op, -1) 
        self.field_rotation_matrix = _Input(_get_input_spec_rotate(1), 1, op, -1) 

class _OutputSpecRotate(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_rotate(0), 0, op) 

class _Rotate(_Operator):
    """Operator's description:
    Internal name is "rotate"
    Scripting name is "rotate"

    Description: Apply a transformation (rotation) matrix on field.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: field_rotation_matrix (3-3 rotation matrix)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("rotate")
    >>> op_way2 = core.operators.geo.rotate()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("rotate")
        self._name = "rotate"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecRotate(self._op)
        self.outputs = _OutputSpecRotate(self._op)

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

def rotate():
    """Operator's description:
    Internal name is "rotate"
    Scripting name is "rotate"

    Description: Apply a transformation (rotation) matrix on field.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: field_rotation_matrix (3-3 rotation matrix)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("rotate")
    >>> op_way2 = core.operators.geo.rotate()
    """
    return _Rotate()

#internal name: rotate_fc
#scripting name: rotate_fc
def _get_input_spec_rotate_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "coordinate_system", type_names = ["field"], optional = False, document = """3-3 rotation matrix""")
    inputs_dict_rotate_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_rotate_fc[pin]

def _get_output_spec_rotate_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_rotate_fc = { 
        0 : outpin0
    }
    return outputs_dict_rotate_fc[pin]

class _InputSpecRotateFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_rotate_fc(0), 0, op, -1) 
        self.coordinate_system = _Input(_get_input_spec_rotate_fc(1), 1, op, -1) 

class _OutputSpecRotateFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_rotate_fc(0), 0, op) 

class _RotateFc(_Operator):
    """Operator's description:
    Internal name is "rotate_fc"
    Scripting name is "rotate_fc"

    Description: Apply a transformation (rotation) matrix on all the fields of a fields container.

    Input list: 
       0: fields_container 
       1: coordinate_system (3-3 rotation matrix)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("rotate_fc")
    >>> op_way2 = core.operators.geo.rotate_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("rotate_fc")
        self._name = "rotate_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecRotateFc(self._op)
        self.outputs = _OutputSpecRotateFc(self._op)

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

def rotate_fc():
    """Operator's description:
    Internal name is "rotate_fc"
    Scripting name is "rotate_fc"

    Description: Apply a transformation (rotation) matrix on all the fields of a fields container.

    Input list: 
       0: fields_container 
       1: coordinate_system (3-3 rotation matrix)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("rotate_fc")
    >>> op_way2 = core.operators.geo.rotate_fc()
    """
    return _RotateFc()

#internal name: volumes_provider
#scripting name: elements_volumes_over_time
def _get_input_spec_elements_volumes_over_time(pin):
    inpin1 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "displacement", type_names = ["fields_container"], optional = True, document = """Displacement field's container. Must contain the mesh if mesh not specified in input.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """Mesh must be defined if the displacement field's container does not contain it, or if there is no displacement.""")
    inputs_dict_elements_volumes_over_time = { 
        1 : inpin1,
        2 : inpin2,
        7 : inpin7
    }
    return inputs_dict_elements_volumes_over_time[pin]

def _get_output_spec_elements_volumes_over_time(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elements_volumes_over_time = { 
        0 : outpin0
    }
    return outputs_dict_elements_volumes_over_time[pin]

class _InputSpecElementsVolumesOverTime(_Inputs):
    def __init__(self, op: _Operator):
        self.scoping = _Input(_get_input_spec_elements_volumes_over_time(1), 1, op, -1) 
        self.displacement = _Input(_get_input_spec_elements_volumes_over_time(2), 2, op, -1) 
        self.mesh = _Input(_get_input_spec_elements_volumes_over_time(7), 7, op, -1) 

class _OutputSpecElementsVolumesOverTime(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elements_volumes_over_time(0), 0, op) 

class _ElementsVolumesOverTime(_Operator):
    """Operator's description:
    Internal name is "volumes_provider"
    Scripting name is "elements_volumes_over_time"

    Description: Calculation of the volume of each element over time of a mesh for each specified time step.

    Input list: 
       1: scoping 
       2: displacement (Displacement field's container. Must contain the mesh if mesh not specified in input.)
       7: mesh (Mesh must be defined if the displacement field's container does not contain it, or if there is no displacement.)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("volumes_provider")
    >>> op_way2 = core.operators.geo.elements_volumes_over_time()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("volumes_provider")
        self._name = "volumes_provider"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecElementsVolumesOverTime(self._op)
        self.outputs = _OutputSpecElementsVolumesOverTime(self._op)

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

def elements_volumes_over_time():
    """Operator's description:
    Internal name is "volumes_provider"
    Scripting name is "elements_volumes_over_time"

    Description: Calculation of the volume of each element over time of a mesh for each specified time step.

    Input list: 
       1: scoping 
       2: displacement (Displacement field's container. Must contain the mesh if mesh not specified in input.)
       7: mesh (Mesh must be defined if the displacement field's container does not contain it, or if there is no displacement.)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("volumes_provider")
    >>> op_way2 = core.operators.geo.elements_volumes_over_time()
    """
    return _ElementsVolumesOverTime()

#internal name: surfaces_provider
#scripting name: elements_facets_surfaces_over_time
def _get_input_spec_elements_facets_surfaces_over_time(pin):
    inpin1 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "displacement", type_names = ["fields_container"], optional = True, document = """Displacement field's container.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """Mesh must be defined if the displacement field's container does not contain it, or if there is no displacement.""")
    inputs_dict_elements_facets_surfaces_over_time = { 
        1 : inpin1,
        2 : inpin2,
        7 : inpin7
    }
    return inputs_dict_elements_facets_surfaces_over_time[pin]

def _get_output_spec_elements_facets_surfaces_over_time(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """Surfaces field.""")
    outpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], document = """Mesh made of surface elements only.""")
    outputs_dict_elements_facets_surfaces_over_time = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_elements_facets_surfaces_over_time[pin]

class _InputSpecElementsFacetsSurfacesOverTime(_Inputs):
    def __init__(self, op: _Operator):
        self.scoping = _Input(_get_input_spec_elements_facets_surfaces_over_time(1), 1, op, -1) 
        self.displacement = _Input(_get_input_spec_elements_facets_surfaces_over_time(2), 2, op, -1) 
        self.mesh = _Input(_get_input_spec_elements_facets_surfaces_over_time(7), 7, op, -1) 

class _OutputSpecElementsFacetsSurfacesOverTime(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elements_facets_surfaces_over_time(0), 0, op) 
        self.mesh = _Output(_get_output_spec_elements_facets_surfaces_over_time(1), 1, op) 

class _ElementsFacetsSurfacesOverTime(_Operator):
    """Operator's description:
    Internal name is "surfaces_provider"
    Scripting name is "elements_facets_surfaces_over_time"

    Description: Calculation of the surface of each element's facet over time of a mesh for each specified time step. Moreover, it gives as output a new mesh made with only surface elements.

    Input list: 
       1: scoping 
       2: displacement (Displacement field's container.)
       7: mesh (Mesh must be defined if the displacement field's container does not contain it, or if there is no displacement.)

    Output list: 
       0: fields_container (Surfaces field.)
       1: mesh (Mesh made of surface elements only.)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("surfaces_provider")
    >>> op_way2 = core.operators.geo.elements_facets_surfaces_over_time()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("surfaces_provider")
        self._name = "surfaces_provider"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecElementsFacetsSurfacesOverTime(self._op)
        self.outputs = _OutputSpecElementsFacetsSurfacesOverTime(self._op)

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

def elements_facets_surfaces_over_time():
    """Operator's description:
    Internal name is "surfaces_provider"
    Scripting name is "elements_facets_surfaces_over_time"

    Description: Calculation of the surface of each element's facet over time of a mesh for each specified time step. Moreover, it gives as output a new mesh made with only surface elements.

    Input list: 
       1: scoping 
       2: displacement (Displacement field's container.)
       7: mesh (Mesh must be defined if the displacement field's container does not contain it, or if there is no displacement.)

    Output list: 
       0: fields_container (Surfaces field.)
       1: mesh (Mesh made of surface elements only.)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("surfaces_provider")
    >>> op_way2 = core.operators.geo.elements_facets_surfaces_over_time()
    """
    return _ElementsFacetsSurfacesOverTime()

#internal name: element::volume
#scripting name: elements_volume
def _get_input_spec_elements_volume(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inputs_dict_elements_volume = { 
        0 : inpin0
    }
    return inputs_dict_elements_volume[pin]

def _get_output_spec_elements_volume(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_elements_volume = { 
        0 : outpin0
    }
    return outputs_dict_elements_volume[pin]

class _InputSpecElementsVolume(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_elements_volume(0), 0, op, -1) 

class _OutputSpecElementsVolume(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_elements_volume(0), 0, op) 

class _ElementsVolume(_Operator):
    """Operator's description:
    Internal name is "element::volume"
    Scripting name is "elements_volume"

    Description: Compute the volume of each element of a mesh, using default shape functions.

    Input list: 
       0: mesh 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("element::volume")
    >>> op_way2 = core.operators.geo.elements_volume()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("element::volume")
        self._name = "element::volume"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecElementsVolume(self._op)
        self.outputs = _OutputSpecElementsVolume(self._op)

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

def elements_volume():
    """Operator's description:
    Internal name is "element::volume"
    Scripting name is "elements_volume"

    Description: Compute the volume of each element of a mesh, using default shape functions.

    Input list: 
       0: mesh 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("element::volume")
    >>> op_way2 = core.operators.geo.elements_volume()
    """
    return _ElementsVolume()

#internal name: element::nodal_contribution
#scripting name: element_nodal_contribution
def _get_input_spec_element_nodal_contribution(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """Integrate the input field over a specific scoping.""")
    inpin2 = _PinSpecification(name = "volume_fraction", type_names = ["bool"], optional = True, document = """if true, returns influence volume, if false, return influence volume fraction (i.e. integrated value of shape function for each node).""")
    inputs_dict_element_nodal_contribution = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_element_nodal_contribution[pin]

def _get_output_spec_element_nodal_contribution(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_element_nodal_contribution = { 
        0 : outpin0
    }
    return outputs_dict_element_nodal_contribution[pin]

class _InputSpecElementNodalContribution(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_element_nodal_contribution(0), 0, op, -1) 
        self.scoping = _Input(_get_input_spec_element_nodal_contribution(1), 1, op, -1) 
        self.volume_fraction = _Input(_get_input_spec_element_nodal_contribution(2), 2, op, -1) 

class _OutputSpecElementNodalContribution(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_element_nodal_contribution(0), 0, op) 

class _ElementNodalContribution(_Operator):
    """Operator's description:
    Internal name is "element::nodal_contribution"
    Scripting name is "element_nodal_contribution"

    Description: Compute the fraction of volume attributed to each node of each element.

    Input list: 
       0: mesh 
       1: scoping (Integrate the input field over a specific scoping.)
       2: volume_fraction (if true, returns influence volume, if false, return influence volume fraction (i.e. integrated value of shape function for each node).)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("element::nodal_contribution")
    >>> op_way2 = core.operators.geo.element_nodal_contribution()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("element::nodal_contribution")
        self._name = "element::nodal_contribution"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecElementNodalContribution(self._op)
        self.outputs = _OutputSpecElementNodalContribution(self._op)

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

def element_nodal_contribution():
    """Operator's description:
    Internal name is "element::nodal_contribution"
    Scripting name is "element_nodal_contribution"

    Description: Compute the fraction of volume attributed to each node of each element.

    Input list: 
       0: mesh 
       1: scoping (Integrate the input field over a specific scoping.)
       2: volume_fraction (if true, returns influence volume, if false, return influence volume fraction (i.e. integrated value of shape function for each node).)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("element::nodal_contribution")
    >>> op_way2 = core.operators.geo.element_nodal_contribution()
    """
    return _ElementNodalContribution()

#internal name: topology::moment_of_inertia
#scripting name: moment_of_inertia
def _get_input_spec_moment_of_inertia(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """Mesh scoping, if not set, all the elements of the mesh are considered.""")
    inpin2 = _PinSpecification(name = "field", type_names = ["field"], optional = True, document = """Elemental or nodal ponderation used in computation.""")
    inpin3 = _PinSpecification(name = "boolean", type_names = ["bool"], optional = True, document = """default true, compute inertia tensor at center of gravity.""")
    inputs_dict_moment_of_inertia = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    return inputs_dict_moment_of_inertia[pin]

def _get_output_spec_moment_of_inertia(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_moment_of_inertia = { 
        0 : outpin0
    }
    return outputs_dict_moment_of_inertia[pin]

class _InputSpecMomentOfInertia(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_moment_of_inertia(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_moment_of_inertia(1), 1, op, -1) 
        self.field = _Input(_get_input_spec_moment_of_inertia(2), 2, op, -1) 
        self.boolean = _Input(_get_input_spec_moment_of_inertia(3), 3, op, -1) 

class _OutputSpecMomentOfInertia(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_moment_of_inertia(0), 0, op) 

class _MomentOfInertia(_Operator):
    """Operator's description:
    Internal name is "topology::moment_of_inertia"
    Scripting name is "moment_of_inertia"

    Description: Compute the inertia tensor of a set of elements.

    Input list: 
       0: mesh 
       1: mesh_scoping (Mesh scoping, if not set, all the elements of the mesh are considered.)
       2: field (Elemental or nodal ponderation used in computation.)
       3: boolean (default true, compute inertia tensor at center of gravity.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("topology::moment_of_inertia")
    >>> op_way2 = core.operators.geo.moment_of_inertia()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("topology::moment_of_inertia")
        self._name = "topology::moment_of_inertia"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecMomentOfInertia(self._op)
        self.outputs = _OutputSpecMomentOfInertia(self._op)

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

def moment_of_inertia():
    """Operator's description:
    Internal name is "topology::moment_of_inertia"
    Scripting name is "moment_of_inertia"

    Description: Compute the inertia tensor of a set of elements.

    Input list: 
       0: mesh 
       1: mesh_scoping (Mesh scoping, if not set, all the elements of the mesh are considered.)
       2: field (Elemental or nodal ponderation used in computation.)
       3: boolean (default true, compute inertia tensor at center of gravity.)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("topology::moment_of_inertia")
    >>> op_way2 = core.operators.geo.moment_of_inertia()
    """
    return _MomentOfInertia()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from meshOperatorsCore.dll plugin, from "geo" category
"""

#internal name: normals_provider
#scripting name: normals
def _get_input_spec_normals(pin):
    inpin0 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "field", type_names = ["field"], optional = True, document = """""")
    inputs_dict_normals = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3
    }
    return inputs_dict_normals[pin]

def _get_output_spec_normals(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_normals = { 
        0 : outpin0
    }
    return outputs_dict_normals[pin]

class _InputSpecNormals(_Inputs):
    def __init__(self, op: _Operator):
        self.mesh = _Input(_get_input_spec_normals(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_normals(1), 1, op, -1) 
        self.field = _Input(_get_input_spec_normals(3), 3, op, -1) 

class _OutputSpecNormals(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_normals(0), 0, op) 

class _Normals(_Operator):
    """Operator's description:
    Internal name is "normals_provider"
    Scripting name is "normals"

    Description: compute the normals at the given nodes or element scoping based on the given mesh (first version, the element normal is only handled on the shell elements)

    Input list: 
       0: mesh 
       1: mesh_scoping 
       3: field 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("normals_provider")
    >>> op_way2 = core.operators.geo.normals()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("normals_provider")
        self._name = "normals_provider"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecNormals(self._op)
        self.outputs = _OutputSpecNormals(self._op)

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

def normals():
    """Operator's description:
    Internal name is "normals_provider"
    Scripting name is "normals"

    Description: compute the normals at the given nodes or element scoping based on the given mesh (first version, the element normal is only handled on the shell elements)

    Input list: 
       0: mesh 
       1: mesh_scoping 
       3: field 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("normals_provider")
    >>> op_way2 = core.operators.geo.normals()
    """
    return _Normals()

