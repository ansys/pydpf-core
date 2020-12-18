from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "result" category
"""

#internal name: EPPL1
#scripting name: plastic_strain_principal_1
def _get_input_spec_plastic_strain_principal_1(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain_principal_1 = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain_principal_1
    else:
        return inputs_dict_plastic_strain_principal_1[pin]

def _get_output_spec_plastic_strain_principal_1(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_principal_1 = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_principal_1
    else:
        return outputs_dict_plastic_strain_principal_1[pin]

class _InputSpecPlasticStrainPrincipal1(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_principal_1(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain_principal_1(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain_principal_1(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain_principal_1(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_principal_1(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_principal_1(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain_principal_1(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain_principal_1(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain_principal_1(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain_principal_1(17), 17, op, -1) 

class _OutputSpecPlasticStrainPrincipal1(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_principal_1(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_principal_1(0), 0, op) 

class _PlasticStrainPrincipal1(_Operator):
    """Operator's description:
    Internal name is "EPPL1"
    Scripting name is "plastic_strain_principal_1"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component plastic strains 1st principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPL1")
    >>> op_way2 = core.operators.result.plastic_strain_principal_1()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPPL1")
        self.inputs = _InputSpecPlasticStrainPrincipal1(self)
        self.outputs = _OutputSpecPlasticStrainPrincipal1(self)

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

def plastic_strain_principal_1():
    """Operator's description:
    Internal name is "EPPL1"
    Scripting name is "plastic_strain_principal_1"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component plastic strains 1st principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPL1")
    >>> op_way2 = core.operators.result.plastic_strain_principal_1()
    """
    return _PlasticStrainPrincipal1()

#internal name: EPPL3
#scripting name: plastic_strain_principal_3
def _get_input_spec_plastic_strain_principal_3(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain_principal_3 = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain_principal_3
    else:
        return inputs_dict_plastic_strain_principal_3[pin]

def _get_output_spec_plastic_strain_principal_3(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_principal_3 = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_principal_3
    else:
        return outputs_dict_plastic_strain_principal_3[pin]

class _InputSpecPlasticStrainPrincipal3(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_principal_3(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain_principal_3(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain_principal_3(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain_principal_3(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_principal_3(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_principal_3(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain_principal_3(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain_principal_3(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain_principal_3(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain_principal_3(17), 17, op, -1) 

class _OutputSpecPlasticStrainPrincipal3(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_principal_3(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_principal_3(0), 0, op) 

class _PlasticStrainPrincipal3(_Operator):
    """Operator's description:
    Internal name is "EPPL3"
    Scripting name is "plastic_strain_principal_3"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component plastic strains 3rd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPL3")
    >>> op_way2 = core.operators.result.plastic_strain_principal_3()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPPL3")
        self.inputs = _InputSpecPlasticStrainPrincipal3(self)
        self.outputs = _OutputSpecPlasticStrainPrincipal3(self)

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

def plastic_strain_principal_3():
    """Operator's description:
    Internal name is "EPPL3"
    Scripting name is "plastic_strain_principal_3"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component plastic strains 3rd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPL3")
    >>> op_way2 = core.operators.result.plastic_strain_principal_3()
    """
    return _PlasticStrainPrincipal3()

#internal name: RigidTransformationProvider
#scripting name: rigid_transformation
def _get_input_spec_rigid_transformation(pin = None):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inputs_dict_rigid_transformation = { 
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_rigid_transformation
    else:
        return inputs_dict_rigid_transformation[pin]

def _get_output_spec_rigid_transformation(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_rigid_transformation = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_rigid_transformation
    else:
        return outputs_dict_rigid_transformation[pin]

class _InputSpecRigidTransformation(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_rigid_transformation(), op)
        self.streams_container = Input(_get_input_spec_rigid_transformation(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_rigid_transformation(4), 4, op, -1) 

class _OutputSpecRigidTransformation(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_rigid_transformation(), op)
        self.fields_container = Output(_get_output_spec_rigid_transformation(0), 0, op) 

class _RigidTransformation(_Operator):
    """Operator's description:
    Internal name is "RigidTransformationProvider"
    Scripting name is "rigid_transformation"

    Description: Extracts rigid body motions from a displacement in input.

    Input list: 
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("RigidTransformationProvider")
    >>> op_way2 = core.operators.result.rigid_transformation()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("RigidTransformationProvider")
        self.inputs = _InputSpecRigidTransformation(self)
        self.outputs = _OutputSpecRigidTransformation(self)

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

def rigid_transformation():
    """Operator's description:
    Internal name is "RigidTransformationProvider"
    Scripting name is "rigid_transformation"

    Description: Extracts rigid body motions from a displacement in input.

    Input list: 
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("RigidTransformationProvider")
    >>> op_way2 = core.operators.result.rigid_transformation()
    """
    return _RigidTransformation()

#internal name: EPELY
#scripting name: elastic_strain_Y
def _get_input_spec_elastic_strain_Y(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain_Y = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain_Y
    else:
        return inputs_dict_elastic_strain_Y[pin]

def _get_output_spec_elastic_strain_Y(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_Y = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_Y
    else:
        return outputs_dict_elastic_strain_Y[pin]

class _InputSpecElasticStrainY(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_Y(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain_Y(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain_Y(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain_Y(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_Y(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain_Y(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain_Y(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain_Y(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain_Y(17), 17, op, -1) 

class _OutputSpecElasticStrainY(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_Y(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_Y(0), 0, op) 

class _ElasticStrainY(_Operator):
    """Operator's description:
    Internal name is "EPELY"
    Scripting name is "elastic_strain_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains YY normal component (11 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELY")
    >>> op_way2 = core.operators.result.elastic_strain_Y()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPELY")
        self.inputs = _InputSpecElasticStrainY(self)
        self.outputs = _OutputSpecElasticStrainY(self)

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

def elastic_strain_Y():
    """Operator's description:
    Internal name is "EPELY"
    Scripting name is "elastic_strain_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains YY normal component (11 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELY")
    >>> op_way2 = core.operators.result.elastic_strain_Y()
    """
    return _ElasticStrainY()

#internal name: ElementalMass
#scripting name: elemental_mass
def _get_input_spec_elemental_mass(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elemental_mass = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elemental_mass
    else:
        return inputs_dict_elemental_mass[pin]

def _get_output_spec_elemental_mass(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_mass = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_mass
    else:
        return outputs_dict_elemental_mass[pin]

class _InputSpecElementalMass(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_mass(), op)
        self.time_scoping = Input(_get_input_spec_elemental_mass(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elemental_mass(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elemental_mass(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elemental_mass(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elemental_mass(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elemental_mass(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elemental_mass(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elemental_mass(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elemental_mass(17), 17, op, -1) 

class _OutputSpecElementalMass(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_mass(), op)
        self.fields_container = Output(_get_output_spec_elemental_mass(0), 0, op) 

class _ElementalMass(_Operator):
    """Operator's description:
    Internal name is "ElementalMass"
    Scripting name is "elemental_mass"

    Description: Load the appropriate operator based on the data sources and read/compute element mass. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ElementalMass")
    >>> op_way2 = core.operators.result.elemental_mass()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ElementalMass")
        self.inputs = _InputSpecElementalMass(self)
        self.outputs = _OutputSpecElementalMass(self)

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

def elemental_mass():
    """Operator's description:
    Internal name is "ElementalMass"
    Scripting name is "elemental_mass"

    Description: Load the appropriate operator based on the data sources and read/compute element mass. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ElementalMass")
    >>> op_way2 = core.operators.result.elemental_mass()
    """
    return _ElementalMass()

#internal name: TF
#scripting name: heat_flux
def _get_input_spec_heat_flux(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_heat_flux = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_heat_flux
    else:
        return inputs_dict_heat_flux[pin]

def _get_output_spec_heat_flux(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_heat_flux = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_heat_flux
    else:
        return outputs_dict_heat_flux[pin]

class _InputSpecHeatFlux(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_heat_flux(), op)
        self.time_scoping = Input(_get_input_spec_heat_flux(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_heat_flux(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_heat_flux(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_heat_flux(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_heat_flux(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_heat_flux(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_heat_flux(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_heat_flux(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_heat_flux(17), 17, op, -1) 

class _OutputSpecHeatFlux(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_heat_flux(), op)
        self.fields_container = Output(_get_output_spec_heat_flux(0), 0, op) 

class _HeatFlux(_Operator):
    """Operator's description:
    Internal name is "TF"
    Scripting name is "heat_flux"

    Description: Load the appropriate operator based on the data sources and read/compute heat flux. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TF")
    >>> op_way2 = core.operators.result.heat_flux()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("TF")
        self.inputs = _InputSpecHeatFlux(self)
        self.outputs = _OutputSpecHeatFlux(self)

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

def heat_flux():
    """Operator's description:
    Internal name is "TF"
    Scripting name is "heat_flux"

    Description: Load the appropriate operator based on the data sources and read/compute heat flux. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TF")
    >>> op_way2 = core.operators.result.heat_flux()
    """
    return _HeatFlux()

#internal name: ENG_CO
#scripting name: co_energy
def _get_input_spec_co_energy(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_co_energy = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_co_energy
    else:
        return inputs_dict_co_energy[pin]

def _get_output_spec_co_energy(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_co_energy = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_co_energy
    else:
        return outputs_dict_co_energy[pin]

class _InputSpecCoEnergy(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_co_energy(), op)
        self.time_scoping = Input(_get_input_spec_co_energy(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_co_energy(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_co_energy(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_co_energy(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_co_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_co_energy(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_co_energy(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_co_energy(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_co_energy(17), 17, op, -1) 

class _OutputSpecCoEnergy(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_co_energy(), op)
        self.fields_container = Output(_get_output_spec_co_energy(0), 0, op) 

class _CoEnergy(_Operator):
    """Operator's description:
    Internal name is "ENG_CO"
    Scripting name is "co_energy"

    Description: Load the appropriate operator based on the data sources and read/compute co-energy (magnetics). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_CO")
    >>> op_way2 = core.operators.result.co_energy()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENG_CO")
        self.inputs = _InputSpecCoEnergy(self)
        self.outputs = _OutputSpecCoEnergy(self)

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

def co_energy():
    """Operator's description:
    Internal name is "ENG_CO"
    Scripting name is "co_energy"

    Description: Load the appropriate operator based on the data sources and read/compute co-energy (magnetics). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_CO")
    >>> op_way2 = core.operators.result.co_energy()
    """
    return _CoEnergy()

#internal name: EPELZ
#scripting name: elastic_strain_Z
def _get_input_spec_elastic_strain_Z(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain_Z = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain_Z
    else:
        return inputs_dict_elastic_strain_Z[pin]

def _get_output_spec_elastic_strain_Z(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_Z = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_Z
    else:
        return outputs_dict_elastic_strain_Z[pin]

class _InputSpecElasticStrainZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_Z(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain_Z(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain_Z(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain_Z(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_Z(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain_Z(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain_Z(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain_Z(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain_Z(17), 17, op, -1) 

class _OutputSpecElasticStrainZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_Z(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_Z(0), 0, op) 

class _ElasticStrainZ(_Operator):
    """Operator's description:
    Internal name is "EPELZ"
    Scripting name is "elastic_strain_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains ZZ normal component (22 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELZ")
    >>> op_way2 = core.operators.result.elastic_strain_Z()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPELZ")
        self.inputs = _InputSpecElasticStrainZ(self)
        self.outputs = _OutputSpecElasticStrainZ(self)

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

def elastic_strain_Z():
    """Operator's description:
    Internal name is "EPELZ"
    Scripting name is "elastic_strain_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains ZZ normal component (22 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELZ")
    >>> op_way2 = core.operators.result.elastic_strain_Z()
    """
    return _ElasticStrainZ()

#internal name: S
#scripting name: stress
def _get_input_spec_stress(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress
    else:
        return inputs_dict_stress[pin]

def _get_output_spec_stress(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress
    else:
        return outputs_dict_stress[pin]

class _InputSpecStress(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress(), op)
        self.time_scoping = Input(_get_input_spec_stress(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress(17), 17, op, -1) 

class _OutputSpecStress(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress(), op)
        self.fields_container = Output(_get_output_spec_stress(0), 0, op) 

class _Stress(_Operator):
    """Operator's description:
    Internal name is "S"
    Scripting name is "stress"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal component stresses. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("S")
    >>> op_way2 = core.operators.result.stress()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("S")
        self.inputs = _InputSpecStress(self)
        self.outputs = _OutputSpecStress(self)

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

def stress():
    """Operator's description:
    Internal name is "S"
    Scripting name is "stress"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal component stresses. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("S")
    >>> op_way2 = core.operators.result.stress()
    """
    return _Stress()

#internal name: SX
#scripting name: stress_X
def _get_input_spec_stress_X(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_X = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_X
    else:
        return inputs_dict_stress_X[pin]

def _get_output_spec_stress_X(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_X = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_X
    else:
        return outputs_dict_stress_X[pin]

class _InputSpecStressX(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_X(), op)
        self.time_scoping = Input(_get_input_spec_stress_X(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_X(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_X(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_X(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_X(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_X(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_X(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_X(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_X(17), 17, op, -1) 

class _OutputSpecStressX(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_X(), op)
        self.fields_container = Output(_get_output_spec_stress_X(0), 0, op) 

class _StressX(_Operator):
    """Operator's description:
    Internal name is "SX"
    Scripting name is "stress_X"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses XX normal component (00 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SX")
    >>> op_way2 = core.operators.result.stress_X()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("SX")
        self.inputs = _InputSpecStressX(self)
        self.outputs = _OutputSpecStressX(self)

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

def stress_X():
    """Operator's description:
    Internal name is "SX"
    Scripting name is "stress_X"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses XX normal component (00 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SX")
    >>> op_way2 = core.operators.result.stress_X()
    """
    return _StressX()

#internal name: SY
#scripting name: stress_Y
def _get_input_spec_stress_Y(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_Y = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_Y
    else:
        return inputs_dict_stress_Y[pin]

def _get_output_spec_stress_Y(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_Y = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_Y
    else:
        return outputs_dict_stress_Y[pin]

class _InputSpecStressY(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_Y(), op)
        self.time_scoping = Input(_get_input_spec_stress_Y(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_Y(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_Y(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_Y(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_Y(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_Y(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_Y(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_Y(17), 17, op, -1) 

class _OutputSpecStressY(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_Y(), op)
        self.fields_container = Output(_get_output_spec_stress_Y(0), 0, op) 

class _StressY(_Operator):
    """Operator's description:
    Internal name is "SY"
    Scripting name is "stress_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses YY normal component (11 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SY")
    >>> op_way2 = core.operators.result.stress_Y()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("SY")
        self.inputs = _InputSpecStressY(self)
        self.outputs = _OutputSpecStressY(self)

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

def stress_Y():
    """Operator's description:
    Internal name is "SY"
    Scripting name is "stress_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses YY normal component (11 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SY")
    >>> op_way2 = core.operators.result.stress_Y()
    """
    return _StressY()

#internal name: SZ
#scripting name: stress_Z
def _get_input_spec_stress_Z(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_Z = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_Z
    else:
        return inputs_dict_stress_Z[pin]

def _get_output_spec_stress_Z(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_Z = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_Z
    else:
        return outputs_dict_stress_Z[pin]

class _InputSpecStressZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_Z(), op)
        self.time_scoping = Input(_get_input_spec_stress_Z(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_Z(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_Z(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_Z(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_Z(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_Z(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_Z(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_Z(17), 17, op, -1) 

class _OutputSpecStressZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_Z(), op)
        self.fields_container = Output(_get_output_spec_stress_Z(0), 0, op) 

class _StressZ(_Operator):
    """Operator's description:
    Internal name is "SZ"
    Scripting name is "stress_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses ZZ normal component (22 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SZ")
    >>> op_way2 = core.operators.result.stress_Z()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("SZ")
        self.inputs = _InputSpecStressZ(self)
        self.outputs = _OutputSpecStressZ(self)

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

def stress_Z():
    """Operator's description:
    Internal name is "SZ"
    Scripting name is "stress_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses ZZ normal component (22 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SZ")
    >>> op_way2 = core.operators.result.stress_Z()
    """
    return _StressZ()

#internal name: SXY
#scripting name: stress_XY
def _get_input_spec_stress_XY(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_XY = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_XY
    else:
        return inputs_dict_stress_XY[pin]

def _get_output_spec_stress_XY(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_XY = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_XY
    else:
        return outputs_dict_stress_XY[pin]

class _InputSpecStressXY(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_XY(), op)
        self.time_scoping = Input(_get_input_spec_stress_XY(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_XY(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_XY(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_XY(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_XY(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_XY(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_XY(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_XY(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_XY(17), 17, op, -1) 

class _OutputSpecStressXY(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_XY(), op)
        self.fields_container = Output(_get_output_spec_stress_XY(0), 0, op) 

class _StressXY(_Operator):
    """Operator's description:
    Internal name is "SXY"
    Scripting name is "stress_XY"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses XY shear component (01 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SXY")
    >>> op_way2 = core.operators.result.stress_XY()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("SXY")
        self.inputs = _InputSpecStressXY(self)
        self.outputs = _OutputSpecStressXY(self)

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

def stress_XY():
    """Operator's description:
    Internal name is "SXY"
    Scripting name is "stress_XY"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses XY shear component (01 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SXY")
    >>> op_way2 = core.operators.result.stress_XY()
    """
    return _StressXY()

#internal name: SYZ
#scripting name: stress_YZ
def _get_input_spec_stress_YZ(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_YZ = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_YZ
    else:
        return inputs_dict_stress_YZ[pin]

def _get_output_spec_stress_YZ(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_YZ = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_YZ
    else:
        return outputs_dict_stress_YZ[pin]

class _InputSpecStressYZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_YZ(), op)
        self.time_scoping = Input(_get_input_spec_stress_YZ(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_YZ(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_YZ(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_YZ(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_YZ(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_YZ(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_YZ(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_YZ(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_YZ(17), 17, op, -1) 

class _OutputSpecStressYZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_YZ(), op)
        self.fields_container = Output(_get_output_spec_stress_YZ(0), 0, op) 

class _StressYZ(_Operator):
    """Operator's description:
    Internal name is "SYZ"
    Scripting name is "stress_YZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses YZ shear component (12 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SYZ")
    >>> op_way2 = core.operators.result.stress_YZ()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("SYZ")
        self.inputs = _InputSpecStressYZ(self)
        self.outputs = _OutputSpecStressYZ(self)

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

def stress_YZ():
    """Operator's description:
    Internal name is "SYZ"
    Scripting name is "stress_YZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses YZ shear component (12 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SYZ")
    >>> op_way2 = core.operators.result.stress_YZ()
    """
    return _StressYZ()

#internal name: ModalBasis
#scripting name: modal_basis
def _get_input_spec_modal_basis(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_modal_basis = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_modal_basis
    else:
        return inputs_dict_modal_basis[pin]

def _get_output_spec_modal_basis(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_modal_basis = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_modal_basis
    else:
        return outputs_dict_modal_basis[pin]

class _InputSpecModalBasis(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_modal_basis(), op)
        self.time_scoping = Input(_get_input_spec_modal_basis(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_modal_basis(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_modal_basis(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_modal_basis(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_modal_basis(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_modal_basis(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_modal_basis(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_modal_basis(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_modal_basis(17), 17, op, -1) 

class _OutputSpecModalBasis(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_modal_basis(), op)
        self.fields_container = Output(_get_output_spec_modal_basis(0), 0, op) 

class _ModalBasis(_Operator):
    """Operator's description:
    Internal name is "ModalBasis"
    Scripting name is "modal_basis"

    Description: Load the appropriate operator based on the data sources and read/compute modal basis. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ModalBasis")
    >>> op_way2 = core.operators.result.modal_basis()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ModalBasis")
        self.inputs = _InputSpecModalBasis(self)
        self.outputs = _OutputSpecModalBasis(self)

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

def modal_basis():
    """Operator's description:
    Internal name is "ModalBasis"
    Scripting name is "modal_basis"

    Description: Load the appropriate operator based on the data sources and read/compute modal basis. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ModalBasis")
    >>> op_way2 = core.operators.result.modal_basis()
    """
    return _ModalBasis()

#internal name: SXZ
#scripting name: stress_XZ
def _get_input_spec_stress_XZ(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_XZ = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_XZ
    else:
        return inputs_dict_stress_XZ[pin]

def _get_output_spec_stress_XZ(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_XZ = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_XZ
    else:
        return outputs_dict_stress_XZ[pin]

class _InputSpecStressXZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_XZ(), op)
        self.time_scoping = Input(_get_input_spec_stress_XZ(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_XZ(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_XZ(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_XZ(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_XZ(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_XZ(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_XZ(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_XZ(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_XZ(17), 17, op, -1) 

class _OutputSpecStressXZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_XZ(), op)
        self.fields_container = Output(_get_output_spec_stress_XZ(0), 0, op) 

class _StressXZ(_Operator):
    """Operator's description:
    Internal name is "SXZ"
    Scripting name is "stress_XZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses XZ shear component (02 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SXZ")
    >>> op_way2 = core.operators.result.stress_XZ()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("SXZ")
        self.inputs = _InputSpecStressXZ(self)
        self.outputs = _OutputSpecStressXZ(self)

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

def stress_XZ():
    """Operator's description:
    Internal name is "SXZ"
    Scripting name is "stress_XZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component stresses XZ shear component (02 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("SXZ")
    >>> op_way2 = core.operators.result.stress_XZ()
    """
    return _StressXZ()

#internal name: S1
#scripting name: stress_principal_1
def _get_input_spec_stress_principal_1(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_principal_1 = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_principal_1
    else:
        return inputs_dict_stress_principal_1[pin]

def _get_output_spec_stress_principal_1(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_principal_1 = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_principal_1
    else:
        return outputs_dict_stress_principal_1[pin]

class _InputSpecStressPrincipal1(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_principal_1(), op)
        self.time_scoping = Input(_get_input_spec_stress_principal_1(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_principal_1(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_principal_1(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_principal_1(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_principal_1(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_principal_1(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_principal_1(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_principal_1(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_principal_1(17), 17, op, -1) 

class _OutputSpecStressPrincipal1(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_principal_1(), op)
        self.fields_container = Output(_get_output_spec_stress_principal_1(0), 0, op) 

class _StressPrincipal1(_Operator):
    """Operator's description:
    Internal name is "S1"
    Scripting name is "stress_principal_1"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component stresses 1st principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("S1")
    >>> op_way2 = core.operators.result.stress_principal_1()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("S1")
        self.inputs = _InputSpecStressPrincipal1(self)
        self.outputs = _OutputSpecStressPrincipal1(self)

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

def stress_principal_1():
    """Operator's description:
    Internal name is "S1"
    Scripting name is "stress_principal_1"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component stresses 1st principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("S1")
    >>> op_way2 = core.operators.result.stress_principal_1()
    """
    return _StressPrincipal1()

#internal name: S2
#scripting name: stress_principal_2
def _get_input_spec_stress_principal_2(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_principal_2 = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_principal_2
    else:
        return inputs_dict_stress_principal_2[pin]

def _get_output_spec_stress_principal_2(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_principal_2 = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_principal_2
    else:
        return outputs_dict_stress_principal_2[pin]

class _InputSpecStressPrincipal2(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_principal_2(), op)
        self.time_scoping = Input(_get_input_spec_stress_principal_2(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_principal_2(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_principal_2(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_principal_2(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_principal_2(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_principal_2(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_principal_2(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_principal_2(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_principal_2(17), 17, op, -1) 

class _OutputSpecStressPrincipal2(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_principal_2(), op)
        self.fields_container = Output(_get_output_spec_stress_principal_2(0), 0, op) 

class _StressPrincipal2(_Operator):
    """Operator's description:
    Internal name is "S2"
    Scripting name is "stress_principal_2"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component stresses 2nd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("S2")
    >>> op_way2 = core.operators.result.stress_principal_2()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("S2")
        self.inputs = _InputSpecStressPrincipal2(self)
        self.outputs = _OutputSpecStressPrincipal2(self)

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

def stress_principal_2():
    """Operator's description:
    Internal name is "S2"
    Scripting name is "stress_principal_2"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component stresses 2nd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("S2")
    >>> op_way2 = core.operators.result.stress_principal_2()
    """
    return _StressPrincipal2()

#internal name: S3
#scripting name: stress_principal_3
def _get_input_spec_stress_principal_3(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_principal_3 = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_principal_3
    else:
        return inputs_dict_stress_principal_3[pin]

def _get_output_spec_stress_principal_3(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_principal_3 = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_principal_3
    else:
        return outputs_dict_stress_principal_3[pin]

class _InputSpecStressPrincipal3(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_principal_3(), op)
        self.time_scoping = Input(_get_input_spec_stress_principal_3(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_principal_3(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_principal_3(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_principal_3(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_principal_3(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_principal_3(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_principal_3(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_principal_3(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_principal_3(17), 17, op, -1) 

class _OutputSpecStressPrincipal3(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_principal_3(), op)
        self.fields_container = Output(_get_output_spec_stress_principal_3(0), 0, op) 

class _StressPrincipal3(_Operator):
    """Operator's description:
    Internal name is "S3"
    Scripting name is "stress_principal_3"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component stresses 3rd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("S3")
    >>> op_way2 = core.operators.result.stress_principal_3()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("S3")
        self.inputs = _InputSpecStressPrincipal3(self)
        self.outputs = _OutputSpecStressPrincipal3(self)

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

def stress_principal_3():
    """Operator's description:
    Internal name is "S3"
    Scripting name is "stress_principal_3"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component stresses 3rd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("S3")
    >>> op_way2 = core.operators.result.stress_principal_3()
    """
    return _StressPrincipal3()

#internal name: EPEL
#scripting name: elastic_strain
def _get_input_spec_elastic_strain(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain
    else:
        return inputs_dict_elastic_strain[pin]

def _get_output_spec_elastic_strain(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain
    else:
        return outputs_dict_elastic_strain[pin]

class _InputSpecElasticStrain(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain(17), 17, op, -1) 

class _OutputSpecElasticStrain(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain(0), 0, op) 

class _ElasticStrain(_Operator):
    """Operator's description:
    Internal name is "EPEL"
    Scripting name is "elastic_strain"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPEL")
    >>> op_way2 = core.operators.result.elastic_strain()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPEL")
        self.inputs = _InputSpecElasticStrain(self)
        self.outputs = _OutputSpecElasticStrain(self)

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

def elastic_strain():
    """Operator's description:
    Internal name is "EPEL"
    Scripting name is "elastic_strain"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPEL")
    >>> op_way2 = core.operators.result.elastic_strain()
    """
    return _ElasticStrain()

#internal name: EPELX
#scripting name: elastic_strain_X
def _get_input_spec_elastic_strain_X(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain_X = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain_X
    else:
        return inputs_dict_elastic_strain_X[pin]

def _get_output_spec_elastic_strain_X(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_X = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_X
    else:
        return outputs_dict_elastic_strain_X[pin]

class _InputSpecElasticStrainX(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_X(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain_X(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain_X(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain_X(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_X(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_X(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain_X(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain_X(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain_X(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain_X(17), 17, op, -1) 

class _OutputSpecElasticStrainX(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_X(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_X(0), 0, op) 

class _ElasticStrainX(_Operator):
    """Operator's description:
    Internal name is "EPELX"
    Scripting name is "elastic_strain_X"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains XX normal component (00 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELX")
    >>> op_way2 = core.operators.result.elastic_strain_X()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPELX")
        self.inputs = _InputSpecElasticStrainX(self)
        self.outputs = _OutputSpecElasticStrainX(self)

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

def elastic_strain_X():
    """Operator's description:
    Internal name is "EPELX"
    Scripting name is "elastic_strain_X"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains XX normal component (00 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELX")
    >>> op_way2 = core.operators.result.elastic_strain_X()
    """
    return _ElasticStrainX()

#internal name: EPELXY
#scripting name: elastic_strain_XY
def _get_input_spec_elastic_strain_XY(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain_XY = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain_XY
    else:
        return inputs_dict_elastic_strain_XY[pin]

def _get_output_spec_elastic_strain_XY(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_XY = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_XY
    else:
        return outputs_dict_elastic_strain_XY[pin]

class _InputSpecElasticStrainXY(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_XY(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain_XY(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain_XY(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain_XY(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_XY(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_XY(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain_XY(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain_XY(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain_XY(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain_XY(17), 17, op, -1) 

class _OutputSpecElasticStrainXY(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_XY(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_XY(0), 0, op) 

class _ElasticStrainXY(_Operator):
    """Operator's description:
    Internal name is "EPELXY"
    Scripting name is "elastic_strain_XY"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains XY shear component (01 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELXY")
    >>> op_way2 = core.operators.result.elastic_strain_XY()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPELXY")
        self.inputs = _InputSpecElasticStrainXY(self)
        self.outputs = _OutputSpecElasticStrainXY(self)

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

def elastic_strain_XY():
    """Operator's description:
    Internal name is "EPELXY"
    Scripting name is "elastic_strain_XY"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains XY shear component (01 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELXY")
    >>> op_way2 = core.operators.result.elastic_strain_XY()
    """
    return _ElasticStrainXY()

#internal name: EPELYZ
#scripting name: elastic_strain_YZ
def _get_input_spec_elastic_strain_YZ(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain_YZ = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain_YZ
    else:
        return inputs_dict_elastic_strain_YZ[pin]

def _get_output_spec_elastic_strain_YZ(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_YZ = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_YZ
    else:
        return outputs_dict_elastic_strain_YZ[pin]

class _InputSpecElasticStrainYZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_YZ(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain_YZ(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain_YZ(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain_YZ(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_YZ(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_YZ(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain_YZ(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain_YZ(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain_YZ(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain_YZ(17), 17, op, -1) 

class _OutputSpecElasticStrainYZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_YZ(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_YZ(0), 0, op) 

class _ElasticStrainYZ(_Operator):
    """Operator's description:
    Internal name is "EPELYZ"
    Scripting name is "elastic_strain_YZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains YZ shear component (12 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELYZ")
    >>> op_way2 = core.operators.result.elastic_strain_YZ()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPELYZ")
        self.inputs = _InputSpecElasticStrainYZ(self)
        self.outputs = _OutputSpecElasticStrainYZ(self)

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

def elastic_strain_YZ():
    """Operator's description:
    Internal name is "EPELYZ"
    Scripting name is "elastic_strain_YZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains YZ shear component (12 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELYZ")
    >>> op_way2 = core.operators.result.elastic_strain_YZ()
    """
    return _ElasticStrainYZ()

#internal name: EPELXZ
#scripting name: elastic_strain_XZ
def _get_input_spec_elastic_strain_XZ(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain_XZ = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain_XZ
    else:
        return inputs_dict_elastic_strain_XZ[pin]

def _get_output_spec_elastic_strain_XZ(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_XZ = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_XZ
    else:
        return outputs_dict_elastic_strain_XZ[pin]

class _InputSpecElasticStrainXZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_XZ(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain_XZ(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain_XZ(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain_XZ(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_XZ(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_XZ(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain_XZ(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain_XZ(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain_XZ(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain_XZ(17), 17, op, -1) 

class _OutputSpecElasticStrainXZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_XZ(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_XZ(0), 0, op) 

class _ElasticStrainXZ(_Operator):
    """Operator's description:
    Internal name is "EPELXZ"
    Scripting name is "elastic_strain_XZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains XZ shear component (02 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELXZ")
    >>> op_way2 = core.operators.result.elastic_strain_XZ()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPELXZ")
        self.inputs = _InputSpecElasticStrainXZ(self)
        self.outputs = _OutputSpecElasticStrainXZ(self)

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

def elastic_strain_XZ():
    """Operator's description:
    Internal name is "EPELXZ"
    Scripting name is "elastic_strain_XZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component elastic strains XZ shear component (02 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPELXZ")
    >>> op_way2 = core.operators.result.elastic_strain_XZ()
    """
    return _ElasticStrainXZ()

#internal name: EPEL1
#scripting name: elastic_strain_principal_1
def _get_input_spec_elastic_strain_principal_1(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain_principal_1 = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain_principal_1
    else:
        return inputs_dict_elastic_strain_principal_1[pin]

def _get_output_spec_elastic_strain_principal_1(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_principal_1 = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_principal_1
    else:
        return outputs_dict_elastic_strain_principal_1[pin]

class _InputSpecElasticStrainPrincipal1(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_principal_1(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain_principal_1(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain_principal_1(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain_principal_1(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_principal_1(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_principal_1(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain_principal_1(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain_principal_1(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain_principal_1(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain_principal_1(17), 17, op, -1) 

class _OutputSpecElasticStrainPrincipal1(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_principal_1(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_principal_1(0), 0, op) 

class _ElasticStrainPrincipal1(_Operator):
    """Operator's description:
    Internal name is "EPEL1"
    Scripting name is "elastic_strain_principal_1"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component elastic strains 1st principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPEL1")
    >>> op_way2 = core.operators.result.elastic_strain_principal_1()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPEL1")
        self.inputs = _InputSpecElasticStrainPrincipal1(self)
        self.outputs = _OutputSpecElasticStrainPrincipal1(self)

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

def elastic_strain_principal_1():
    """Operator's description:
    Internal name is "EPEL1"
    Scripting name is "elastic_strain_principal_1"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component elastic strains 1st principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPEL1")
    >>> op_way2 = core.operators.result.elastic_strain_principal_1()
    """
    return _ElasticStrainPrincipal1()

#internal name: EPEL2
#scripting name: elastic_strain_principal_2
def _get_input_spec_elastic_strain_principal_2(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain_principal_2 = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain_principal_2
    else:
        return inputs_dict_elastic_strain_principal_2[pin]

def _get_output_spec_elastic_strain_principal_2(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_principal_2 = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_principal_2
    else:
        return outputs_dict_elastic_strain_principal_2[pin]

class _InputSpecElasticStrainPrincipal2(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_principal_2(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain_principal_2(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain_principal_2(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain_principal_2(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_principal_2(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_principal_2(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain_principal_2(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain_principal_2(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain_principal_2(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain_principal_2(17), 17, op, -1) 

class _OutputSpecElasticStrainPrincipal2(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_principal_2(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_principal_2(0), 0, op) 

class _ElasticStrainPrincipal2(_Operator):
    """Operator's description:
    Internal name is "EPEL2"
    Scripting name is "elastic_strain_principal_2"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component elastic strains 2nd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPEL2")
    >>> op_way2 = core.operators.result.elastic_strain_principal_2()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPEL2")
        self.inputs = _InputSpecElasticStrainPrincipal2(self)
        self.outputs = _OutputSpecElasticStrainPrincipal2(self)

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

def elastic_strain_principal_2():
    """Operator's description:
    Internal name is "EPEL2"
    Scripting name is "elastic_strain_principal_2"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component elastic strains 2nd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPEL2")
    >>> op_way2 = core.operators.result.elastic_strain_principal_2()
    """
    return _ElasticStrainPrincipal2()

#internal name: EPEL3
#scripting name: elastic_strain_principal_3
def _get_input_spec_elastic_strain_principal_3(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain_principal_3 = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain_principal_3
    else:
        return inputs_dict_elastic_strain_principal_3[pin]

def _get_output_spec_elastic_strain_principal_3(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_principal_3 = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_principal_3
    else:
        return outputs_dict_elastic_strain_principal_3[pin]

class _InputSpecElasticStrainPrincipal3(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_principal_3(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain_principal_3(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain_principal_3(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain_principal_3(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_principal_3(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_principal_3(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain_principal_3(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain_principal_3(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain_principal_3(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain_principal_3(17), 17, op, -1) 

class _OutputSpecElasticStrainPrincipal3(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_principal_3(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_principal_3(0), 0, op) 

class _ElasticStrainPrincipal3(_Operator):
    """Operator's description:
    Internal name is "EPEL3"
    Scripting name is "elastic_strain_principal_3"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component elastic strains 3rd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPEL3")
    >>> op_way2 = core.operators.result.elastic_strain_principal_3()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPEL3")
        self.inputs = _InputSpecElasticStrainPrincipal3(self)
        self.outputs = _OutputSpecElasticStrainPrincipal3(self)

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

def elastic_strain_principal_3():
    """Operator's description:
    Internal name is "EPEL3"
    Scripting name is "elastic_strain_principal_3"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component elastic strains 3rd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPEL3")
    >>> op_way2 = core.operators.result.elastic_strain_principal_3()
    """
    return _ElasticStrainPrincipal3()

#internal name: EPPL
#scripting name: plastic_strain
def _get_input_spec_plastic_strain(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain
    else:
        return inputs_dict_plastic_strain[pin]

def _get_output_spec_plastic_strain(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain
    else:
        return outputs_dict_plastic_strain[pin]

class _InputSpecPlasticStrain(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain(17), 17, op, -1) 

class _OutputSpecPlasticStrain(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain(0), 0, op) 

class _PlasticStrain(_Operator):
    """Operator's description:
    Internal name is "EPPL"
    Scripting name is "plastic_strain"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPL")
    >>> op_way2 = core.operators.result.plastic_strain()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPPL")
        self.inputs = _InputSpecPlasticStrain(self)
        self.outputs = _OutputSpecPlasticStrain(self)

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

def plastic_strain():
    """Operator's description:
    Internal name is "EPPL"
    Scripting name is "plastic_strain"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPL")
    >>> op_way2 = core.operators.result.plastic_strain()
    """
    return _PlasticStrain()

#internal name: EPPLX
#scripting name: plastic_strain_X
def _get_input_spec_plastic_strain_X(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain_X = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain_X
    else:
        return inputs_dict_plastic_strain_X[pin]

def _get_output_spec_plastic_strain_X(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_X = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_X
    else:
        return outputs_dict_plastic_strain_X[pin]

class _InputSpecPlasticStrainX(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_X(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain_X(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain_X(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain_X(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_X(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_X(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain_X(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain_X(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain_X(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain_X(17), 17, op, -1) 

class _OutputSpecPlasticStrainX(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_X(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_X(0), 0, op) 

class _PlasticStrainX(_Operator):
    """Operator's description:
    Internal name is "EPPLX"
    Scripting name is "plastic_strain_X"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains XX normal component (00 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLX")
    >>> op_way2 = core.operators.result.plastic_strain_X()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPPLX")
        self.inputs = _InputSpecPlasticStrainX(self)
        self.outputs = _OutputSpecPlasticStrainX(self)

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

def plastic_strain_X():
    """Operator's description:
    Internal name is "EPPLX"
    Scripting name is "plastic_strain_X"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains XX normal component (00 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLX")
    >>> op_way2 = core.operators.result.plastic_strain_X()
    """
    return _PlasticStrainX()

#internal name: EPPLY
#scripting name: plastic_strain_Y
def _get_input_spec_plastic_strain_Y(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain_Y = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain_Y
    else:
        return inputs_dict_plastic_strain_Y[pin]

def _get_output_spec_plastic_strain_Y(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_Y = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_Y
    else:
        return outputs_dict_plastic_strain_Y[pin]

class _InputSpecPlasticStrainY(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_Y(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain_Y(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain_Y(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain_Y(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_Y(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain_Y(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain_Y(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain_Y(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain_Y(17), 17, op, -1) 

class _OutputSpecPlasticStrainY(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_Y(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_Y(0), 0, op) 

class _PlasticStrainY(_Operator):
    """Operator's description:
    Internal name is "EPPLY"
    Scripting name is "plastic_strain_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains YY normal component (11 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLY")
    >>> op_way2 = core.operators.result.plastic_strain_Y()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPPLY")
        self.inputs = _InputSpecPlasticStrainY(self)
        self.outputs = _OutputSpecPlasticStrainY(self)

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

def plastic_strain_Y():
    """Operator's description:
    Internal name is "EPPLY"
    Scripting name is "plastic_strain_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains YY normal component (11 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLY")
    >>> op_way2 = core.operators.result.plastic_strain_Y()
    """
    return _PlasticStrainY()

#internal name: EPPLZ
#scripting name: plastic_strain_Z
def _get_input_spec_plastic_strain_Z(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain_Z = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain_Z
    else:
        return inputs_dict_plastic_strain_Z[pin]

def _get_output_spec_plastic_strain_Z(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_Z = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_Z
    else:
        return outputs_dict_plastic_strain_Z[pin]

class _InputSpecPlasticStrainZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_Z(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain_Z(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain_Z(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain_Z(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_Z(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain_Z(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain_Z(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain_Z(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain_Z(17), 17, op, -1) 

class _OutputSpecPlasticStrainZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_Z(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_Z(0), 0, op) 

class _PlasticStrainZ(_Operator):
    """Operator's description:
    Internal name is "EPPLZ"
    Scripting name is "plastic_strain_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains ZZ normal component (22 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLZ")
    >>> op_way2 = core.operators.result.plastic_strain_Z()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPPLZ")
        self.inputs = _InputSpecPlasticStrainZ(self)
        self.outputs = _OutputSpecPlasticStrainZ(self)

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

def plastic_strain_Z():
    """Operator's description:
    Internal name is "EPPLZ"
    Scripting name is "plastic_strain_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains ZZ normal component (22 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLZ")
    >>> op_way2 = core.operators.result.plastic_strain_Z()
    """
    return _PlasticStrainZ()

#internal name: ENL_HPRES
#scripting name: hydrostatic_pressure
def _get_input_spec_hydrostatic_pressure(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_hydrostatic_pressure = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_hydrostatic_pressure
    else:
        return inputs_dict_hydrostatic_pressure[pin]

def _get_output_spec_hydrostatic_pressure(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_hydrostatic_pressure = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_hydrostatic_pressure
    else:
        return outputs_dict_hydrostatic_pressure[pin]

class _InputSpecHydrostaticPressure(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_hydrostatic_pressure(), op)
        self.time_scoping = Input(_get_input_spec_hydrostatic_pressure(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_hydrostatic_pressure(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_hydrostatic_pressure(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_hydrostatic_pressure(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_hydrostatic_pressure(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_hydrostatic_pressure(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_hydrostatic_pressure(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_hydrostatic_pressure(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_hydrostatic_pressure(17), 17, op, -1) 

class _OutputSpecHydrostaticPressure(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_hydrostatic_pressure(), op)
        self.fields_container = Output(_get_output_spec_hydrostatic_pressure(0), 0, op) 

class _HydrostaticPressure(_Operator):
    """Operator's description:
    Internal name is "ENL_HPRES"
    Scripting name is "hydrostatic_pressure"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal hydrostatic pressure. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_HPRES")
    >>> op_way2 = core.operators.result.hydrostatic_pressure()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENL_HPRES")
        self.inputs = _InputSpecHydrostaticPressure(self)
        self.outputs = _OutputSpecHydrostaticPressure(self)

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

def hydrostatic_pressure():
    """Operator's description:
    Internal name is "ENL_HPRES"
    Scripting name is "hydrostatic_pressure"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal hydrostatic pressure. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_HPRES")
    >>> op_way2 = core.operators.result.hydrostatic_pressure()
    """
    return _HydrostaticPressure()

#internal name: EPPLXY
#scripting name: plastic_strain_XY
def _get_input_spec_plastic_strain_XY(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain_XY = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain_XY
    else:
        return inputs_dict_plastic_strain_XY[pin]

def _get_output_spec_plastic_strain_XY(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_XY = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_XY
    else:
        return outputs_dict_plastic_strain_XY[pin]

class _InputSpecPlasticStrainXY(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_XY(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain_XY(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain_XY(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain_XY(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_XY(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_XY(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain_XY(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain_XY(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain_XY(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain_XY(17), 17, op, -1) 

class _OutputSpecPlasticStrainXY(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_XY(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_XY(0), 0, op) 

class _PlasticStrainXY(_Operator):
    """Operator's description:
    Internal name is "EPPLXY"
    Scripting name is "plastic_strain_XY"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains XY shear component (01 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLXY")
    >>> op_way2 = core.operators.result.plastic_strain_XY()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPPLXY")
        self.inputs = _InputSpecPlasticStrainXY(self)
        self.outputs = _OutputSpecPlasticStrainXY(self)

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

def plastic_strain_XY():
    """Operator's description:
    Internal name is "EPPLXY"
    Scripting name is "plastic_strain_XY"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains XY shear component (01 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLXY")
    >>> op_way2 = core.operators.result.plastic_strain_XY()
    """
    return _PlasticStrainXY()

#internal name: EPPLYZ
#scripting name: plastic_strain_YZ
def _get_input_spec_plastic_strain_YZ(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain_YZ = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain_YZ
    else:
        return inputs_dict_plastic_strain_YZ[pin]

def _get_output_spec_plastic_strain_YZ(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_YZ = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_YZ
    else:
        return outputs_dict_plastic_strain_YZ[pin]

class _InputSpecPlasticStrainYZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_YZ(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain_YZ(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain_YZ(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain_YZ(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_YZ(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_YZ(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain_YZ(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain_YZ(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain_YZ(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain_YZ(17), 17, op, -1) 

class _OutputSpecPlasticStrainYZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_YZ(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_YZ(0), 0, op) 

class _PlasticStrainYZ(_Operator):
    """Operator's description:
    Internal name is "EPPLYZ"
    Scripting name is "plastic_strain_YZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains YZ shear component (12 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLYZ")
    >>> op_way2 = core.operators.result.plastic_strain_YZ()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPPLYZ")
        self.inputs = _InputSpecPlasticStrainYZ(self)
        self.outputs = _OutputSpecPlasticStrainYZ(self)

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

def plastic_strain_YZ():
    """Operator's description:
    Internal name is "EPPLYZ"
    Scripting name is "plastic_strain_YZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains YZ shear component (12 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLYZ")
    >>> op_way2 = core.operators.result.plastic_strain_YZ()
    """
    return _PlasticStrainYZ()

#internal name: EPPLXZ
#scripting name: plastic_strain_XZ
def _get_input_spec_plastic_strain_XZ(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain_XZ = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain_XZ
    else:
        return inputs_dict_plastic_strain_XZ[pin]

def _get_output_spec_plastic_strain_XZ(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_XZ = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_XZ
    else:
        return outputs_dict_plastic_strain_XZ[pin]

class _InputSpecPlasticStrainXZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_XZ(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain_XZ(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain_XZ(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain_XZ(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_XZ(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_XZ(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain_XZ(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain_XZ(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain_XZ(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain_XZ(17), 17, op, -1) 

class _OutputSpecPlasticStrainXZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_XZ(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_XZ(0), 0, op) 

class _PlasticStrainXZ(_Operator):
    """Operator's description:
    Internal name is "EPPLXZ"
    Scripting name is "plastic_strain_XZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains XZ shear component (02 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLXZ")
    >>> op_way2 = core.operators.result.plastic_strain_XZ()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPPLXZ")
        self.inputs = _InputSpecPlasticStrainXZ(self)
        self.outputs = _OutputSpecPlasticStrainXZ(self)

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

def plastic_strain_XZ():
    """Operator's description:
    Internal name is "EPPLXZ"
    Scripting name is "plastic_strain_XZ"

    Description:  Load the appropriate operator based on the data sources and read/compute element nodal component plastic strains XZ shear component (02 component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPLXZ")
    >>> op_way2 = core.operators.result.plastic_strain_XZ()
    """
    return _PlasticStrainXZ()

#internal name: EPPL2
#scripting name: plastic_strain_principal_2
def _get_input_spec_plastic_strain_principal_2(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain_principal_2 = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain_principal_2
    else:
        return inputs_dict_plastic_strain_principal_2[pin]

def _get_output_spec_plastic_strain_principal_2(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_principal_2 = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_principal_2
    else:
        return outputs_dict_plastic_strain_principal_2[pin]

class _InputSpecPlasticStrainPrincipal2(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_principal_2(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain_principal_2(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain_principal_2(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain_principal_2(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_principal_2(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_principal_2(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain_principal_2(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain_principal_2(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain_principal_2(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain_principal_2(17), 17, op, -1) 

class _OutputSpecPlasticStrainPrincipal2(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_principal_2(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_principal_2(0), 0, op) 

class _PlasticStrainPrincipal2(_Operator):
    """Operator's description:
    Internal name is "EPPL2"
    Scripting name is "plastic_strain_principal_2"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component plastic strains 2nd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPL2")
    >>> op_way2 = core.operators.result.plastic_strain_principal_2()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EPPL2")
        self.inputs = _InputSpecPlasticStrainPrincipal2(self)
        self.outputs = _OutputSpecPlasticStrainPrincipal2(self)

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

def plastic_strain_principal_2():
    """Operator's description:
    Internal name is "EPPL2"
    Scripting name is "plastic_strain_principal_2"

    Description:  Load the appropriate operator based on the data sources, reads/computes the result and find its eigen values (element nodal component plastic strains 2nd principal component).

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EPPL2")
    >>> op_way2 = core.operators.result.plastic_strain_principal_2()
    """
    return _PlasticStrainPrincipal2()

#internal name: A
#scripting name: acceleration
def _get_input_spec_acceleration(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_acceleration = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_acceleration
    else:
        return inputs_dict_acceleration[pin]

def _get_output_spec_acceleration(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_acceleration = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_acceleration
    else:
        return outputs_dict_acceleration[pin]

class _InputSpecAcceleration(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_acceleration(), op)
        self.time_scoping = Input(_get_input_spec_acceleration(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_acceleration(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_acceleration(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_acceleration(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_acceleration(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_acceleration(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_acceleration(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_acceleration(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_acceleration(17), 17, op, -1) 

class _OutputSpecAcceleration(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_acceleration(), op)
        self.fields_container = Output(_get_output_spec_acceleration(0), 0, op) 

class _Acceleration(_Operator):
    """Operator's description:
    Internal name is "A"
    Scripting name is "acceleration"

    Description: Load the appropriate operator based on the data sources and read/compute nodal accelerations. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("A")
    >>> op_way2 = core.operators.result.acceleration()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("A")
        self.inputs = _InputSpecAcceleration(self)
        self.outputs = _OutputSpecAcceleration(self)

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

def acceleration():
    """Operator's description:
    Internal name is "A"
    Scripting name is "acceleration"

    Description: Load the appropriate operator based on the data sources and read/compute nodal accelerations. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("A")
    >>> op_way2 = core.operators.result.acceleration()
    """
    return _Acceleration()

#internal name: AX
#scripting name: acceleration_X
def _get_input_spec_acceleration_X(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_acceleration_X = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_acceleration_X
    else:
        return inputs_dict_acceleration_X[pin]

def _get_output_spec_acceleration_X(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_acceleration_X = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_acceleration_X
    else:
        return outputs_dict_acceleration_X[pin]

class _InputSpecAccelerationX(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_acceleration_X(), op)
        self.time_scoping = Input(_get_input_spec_acceleration_X(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_acceleration_X(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_acceleration_X(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_acceleration_X(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_acceleration_X(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_acceleration_X(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_acceleration_X(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_acceleration_X(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_acceleration_X(17), 17, op, -1) 

class _OutputSpecAccelerationX(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_acceleration_X(), op)
        self.fields_container = Output(_get_output_spec_acceleration_X(0), 0, op) 

class _AccelerationX(_Operator):
    """Operator's description:
    Internal name is "AX"
    Scripting name is "acceleration_X"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal accelerations X component of the vector (1st component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("AX")
    >>> op_way2 = core.operators.result.acceleration_X()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("AX")
        self.inputs = _InputSpecAccelerationX(self)
        self.outputs = _OutputSpecAccelerationX(self)

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

def acceleration_X():
    """Operator's description:
    Internal name is "AX"
    Scripting name is "acceleration_X"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal accelerations X component of the vector (1st component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("AX")
    >>> op_way2 = core.operators.result.acceleration_X()
    """
    return _AccelerationX()

#internal name: AY
#scripting name: acceleration_Y
def _get_input_spec_acceleration_Y(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_acceleration_Y = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_acceleration_Y
    else:
        return inputs_dict_acceleration_Y[pin]

def _get_output_spec_acceleration_Y(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_acceleration_Y = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_acceleration_Y
    else:
        return outputs_dict_acceleration_Y[pin]

class _InputSpecAccelerationY(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_acceleration_Y(), op)
        self.time_scoping = Input(_get_input_spec_acceleration_Y(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_acceleration_Y(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_acceleration_Y(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_acceleration_Y(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_acceleration_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_acceleration_Y(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_acceleration_Y(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_acceleration_Y(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_acceleration_Y(17), 17, op, -1) 

class _OutputSpecAccelerationY(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_acceleration_Y(), op)
        self.fields_container = Output(_get_output_spec_acceleration_Y(0), 0, op) 

class _AccelerationY(_Operator):
    """Operator's description:
    Internal name is "AY"
    Scripting name is "acceleration_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal accelerations Y component of the vector (2nd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("AY")
    >>> op_way2 = core.operators.result.acceleration_Y()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("AY")
        self.inputs = _InputSpecAccelerationY(self)
        self.outputs = _OutputSpecAccelerationY(self)

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

def acceleration_Y():
    """Operator's description:
    Internal name is "AY"
    Scripting name is "acceleration_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal accelerations Y component of the vector (2nd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("AY")
    >>> op_way2 = core.operators.result.acceleration_Y()
    """
    return _AccelerationY()

#internal name: centroids
#scripting name: element_centroids
def _get_input_spec_element_centroids(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_element_centroids = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_element_centroids
    else:
        return inputs_dict_element_centroids[pin]

def _get_output_spec_element_centroids(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_element_centroids = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_element_centroids
    else:
        return outputs_dict_element_centroids[pin]

class _InputSpecElementCentroids(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_element_centroids(), op)
        self.time_scoping = Input(_get_input_spec_element_centroids(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_element_centroids(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_element_centroids(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_element_centroids(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_element_centroids(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_element_centroids(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_element_centroids(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_element_centroids(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_element_centroids(17), 17, op, -1) 

class _OutputSpecElementCentroids(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_element_centroids(), op)
        self.fields_container = Output(_get_output_spec_element_centroids(0), 0, op) 

class _ElementCentroids(_Operator):
    """Operator's description:
    Internal name is "centroids"
    Scripting name is "element_centroids"

    Description: Load the appropriate operator based on the data sources and read/compute coordinate of the elemental centroids. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("centroids")
    >>> op_way2 = core.operators.result.element_centroids()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("centroids")
        self.inputs = _InputSpecElementCentroids(self)
        self.outputs = _OutputSpecElementCentroids(self)

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

def element_centroids():
    """Operator's description:
    Internal name is "centroids"
    Scripting name is "element_centroids"

    Description: Load the appropriate operator based on the data sources and read/compute coordinate of the elemental centroids. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("centroids")
    >>> op_way2 = core.operators.result.element_centroids()
    """
    return _ElementCentroids()

#internal name: AZ
#scripting name: acceleration_Z
def _get_input_spec_acceleration_Z(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_acceleration_Z = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_acceleration_Z
    else:
        return inputs_dict_acceleration_Z[pin]

def _get_output_spec_acceleration_Z(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_acceleration_Z = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_acceleration_Z
    else:
        return outputs_dict_acceleration_Z[pin]

class _InputSpecAccelerationZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_acceleration_Z(), op)
        self.time_scoping = Input(_get_input_spec_acceleration_Z(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_acceleration_Z(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_acceleration_Z(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_acceleration_Z(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_acceleration_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_acceleration_Z(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_acceleration_Z(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_acceleration_Z(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_acceleration_Z(17), 17, op, -1) 

class _OutputSpecAccelerationZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_acceleration_Z(), op)
        self.fields_container = Output(_get_output_spec_acceleration_Z(0), 0, op) 

class _AccelerationZ(_Operator):
    """Operator's description:
    Internal name is "AZ"
    Scripting name is "acceleration_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal accelerations Z component of the vector (3rd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("AZ")
    >>> op_way2 = core.operators.result.acceleration_Z()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("AZ")
        self.inputs = _InputSpecAccelerationZ(self)
        self.outputs = _OutputSpecAccelerationZ(self)

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

def acceleration_Z():
    """Operator's description:
    Internal name is "AZ"
    Scripting name is "acceleration_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal accelerations Z component of the vector (3rd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("AZ")
    >>> op_way2 = core.operators.result.acceleration_Z()
    """
    return _AccelerationZ()

#internal name: RF
#scripting name: reaction_force
def _get_input_spec_reaction_force(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_reaction_force = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_reaction_force
    else:
        return inputs_dict_reaction_force[pin]

def _get_output_spec_reaction_force(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_reaction_force = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_reaction_force
    else:
        return outputs_dict_reaction_force[pin]

class _InputSpecReactionForce(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_reaction_force(), op)
        self.time_scoping = Input(_get_input_spec_reaction_force(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_reaction_force(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_reaction_force(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_reaction_force(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_reaction_force(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_reaction_force(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_reaction_force(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_reaction_force(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_reaction_force(17), 17, op, -1) 

class _OutputSpecReactionForce(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_reaction_force(), op)
        self.fields_container = Output(_get_output_spec_reaction_force(0), 0, op) 

class _ReactionForce(_Operator):
    """Operator's description:
    Internal name is "RF"
    Scripting name is "reaction_force"

    Description: Load the appropriate operator based on the data sources and read/compute nodal reaction forces. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("RF")
    >>> op_way2 = core.operators.result.reaction_force()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("RF")
        self.inputs = _InputSpecReactionForce(self)
        self.outputs = _OutputSpecReactionForce(self)

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

def reaction_force():
    """Operator's description:
    Internal name is "RF"
    Scripting name is "reaction_force"

    Description: Load the appropriate operator based on the data sources and read/compute nodal reaction forces. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("RF")
    >>> op_way2 = core.operators.result.reaction_force()
    """
    return _ReactionForce()

#internal name: V
#scripting name: velocity
def _get_input_spec_velocity(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_velocity = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_velocity
    else:
        return inputs_dict_velocity[pin]

def _get_output_spec_velocity(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_velocity = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_velocity
    else:
        return outputs_dict_velocity[pin]

class _InputSpecVelocity(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_velocity(), op)
        self.time_scoping = Input(_get_input_spec_velocity(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_velocity(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_velocity(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_velocity(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_velocity(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_velocity(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_velocity(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_velocity(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_velocity(17), 17, op, -1) 

class _OutputSpecVelocity(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_velocity(), op)
        self.fields_container = Output(_get_output_spec_velocity(0), 0, op) 

class _Velocity(_Operator):
    """Operator's description:
    Internal name is "V"
    Scripting name is "velocity"

    Description: Load the appropriate operator based on the data sources and read/compute nodal velocities. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("V")
    >>> op_way2 = core.operators.result.velocity()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("V")
        self.inputs = _InputSpecVelocity(self)
        self.outputs = _OutputSpecVelocity(self)

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

def velocity():
    """Operator's description:
    Internal name is "V"
    Scripting name is "velocity"

    Description: Load the appropriate operator based on the data sources and read/compute nodal velocities. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("V")
    >>> op_way2 = core.operators.result.velocity()
    """
    return _Velocity()

#internal name: VX
#scripting name: velocity_X
def _get_input_spec_velocity_X(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_velocity_X = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_velocity_X
    else:
        return inputs_dict_velocity_X[pin]

def _get_output_spec_velocity_X(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_velocity_X = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_velocity_X
    else:
        return outputs_dict_velocity_X[pin]

class _InputSpecVelocityX(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_velocity_X(), op)
        self.time_scoping = Input(_get_input_spec_velocity_X(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_velocity_X(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_velocity_X(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_velocity_X(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_velocity_X(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_velocity_X(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_velocity_X(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_velocity_X(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_velocity_X(17), 17, op, -1) 

class _OutputSpecVelocityX(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_velocity_X(), op)
        self.fields_container = Output(_get_output_spec_velocity_X(0), 0, op) 

class _VelocityX(_Operator):
    """Operator's description:
    Internal name is "VX"
    Scripting name is "velocity_X"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal velocities X component of the vector (1st component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("VX")
    >>> op_way2 = core.operators.result.velocity_X()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("VX")
        self.inputs = _InputSpecVelocityX(self)
        self.outputs = _OutputSpecVelocityX(self)

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

def velocity_X():
    """Operator's description:
    Internal name is "VX"
    Scripting name is "velocity_X"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal velocities X component of the vector (1st component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("VX")
    >>> op_way2 = core.operators.result.velocity_X()
    """
    return _VelocityX()

#internal name: VY
#scripting name: velocity_Y
def _get_input_spec_velocity_Y(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_velocity_Y = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_velocity_Y
    else:
        return inputs_dict_velocity_Y[pin]

def _get_output_spec_velocity_Y(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_velocity_Y = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_velocity_Y
    else:
        return outputs_dict_velocity_Y[pin]

class _InputSpecVelocityY(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_velocity_Y(), op)
        self.time_scoping = Input(_get_input_spec_velocity_Y(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_velocity_Y(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_velocity_Y(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_velocity_Y(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_velocity_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_velocity_Y(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_velocity_Y(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_velocity_Y(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_velocity_Y(17), 17, op, -1) 

class _OutputSpecVelocityY(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_velocity_Y(), op)
        self.fields_container = Output(_get_output_spec_velocity_Y(0), 0, op) 

class _VelocityY(_Operator):
    """Operator's description:
    Internal name is "VY"
    Scripting name is "velocity_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal velocities Y component of the vector (2nd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("VY")
    >>> op_way2 = core.operators.result.velocity_Y()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("VY")
        self.inputs = _InputSpecVelocityY(self)
        self.outputs = _OutputSpecVelocityY(self)

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

def velocity_Y():
    """Operator's description:
    Internal name is "VY"
    Scripting name is "velocity_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal velocities Y component of the vector (2nd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("VY")
    >>> op_way2 = core.operators.result.velocity_Y()
    """
    return _VelocityY()

#internal name: VZ
#scripting name: velocity_Z
def _get_input_spec_velocity_Z(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_velocity_Z = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_velocity_Z
    else:
        return inputs_dict_velocity_Z[pin]

def _get_output_spec_velocity_Z(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_velocity_Z = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_velocity_Z
    else:
        return outputs_dict_velocity_Z[pin]

class _InputSpecVelocityZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_velocity_Z(), op)
        self.time_scoping = Input(_get_input_spec_velocity_Z(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_velocity_Z(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_velocity_Z(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_velocity_Z(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_velocity_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_velocity_Z(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_velocity_Z(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_velocity_Z(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_velocity_Z(17), 17, op, -1) 

class _OutputSpecVelocityZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_velocity_Z(), op)
        self.fields_container = Output(_get_output_spec_velocity_Z(0), 0, op) 

class _VelocityZ(_Operator):
    """Operator's description:
    Internal name is "VZ"
    Scripting name is "velocity_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal velocities Z component of the vector (3rd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("VZ")
    >>> op_way2 = core.operators.result.velocity_Z()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("VZ")
        self.inputs = _InputSpecVelocityZ(self)
        self.outputs = _OutputSpecVelocityZ(self)

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

def velocity_Z():
    """Operator's description:
    Internal name is "VZ"
    Scripting name is "velocity_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal velocities Z component of the vector (3rd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("VZ")
    >>> op_way2 = core.operators.result.velocity_Z()
    """
    return _VelocityZ()

#internal name: U
#scripting name: displacement
def _get_input_spec_displacement(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_displacement = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_displacement
    else:
        return inputs_dict_displacement[pin]

def _get_output_spec_displacement(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_displacement = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_displacement
    else:
        return outputs_dict_displacement[pin]

class _InputSpecDisplacement(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_displacement(), op)
        self.time_scoping = Input(_get_input_spec_displacement(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_displacement(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_displacement(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_displacement(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_displacement(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_displacement(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_displacement(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_displacement(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_displacement(17), 17, op, -1) 

class _OutputSpecDisplacement(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_displacement(), op)
        self.fields_container = Output(_get_output_spec_displacement(0), 0, op) 

class _Displacement(_Operator):
    """Operator's description:
    Internal name is "U"
    Scripting name is "displacement"

    Description: Load the appropriate operator based on the data sources and read/compute nodal displacements. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("U")
    >>> op_way2 = core.operators.result.displacement()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("U")
        self.inputs = _InputSpecDisplacement(self)
        self.outputs = _OutputSpecDisplacement(self)

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

def displacement():
    """Operator's description:
    Internal name is "U"
    Scripting name is "displacement"

    Description: Load the appropriate operator based on the data sources and read/compute nodal displacements. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("U")
    >>> op_way2 = core.operators.result.displacement()
    """
    return _Displacement()

#internal name: UX
#scripting name: displacement_X
def _get_input_spec_displacement_X(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_displacement_X = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_displacement_X
    else:
        return inputs_dict_displacement_X[pin]

def _get_output_spec_displacement_X(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_displacement_X = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_displacement_X
    else:
        return outputs_dict_displacement_X[pin]

class _InputSpecDisplacementX(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_displacement_X(), op)
        self.time_scoping = Input(_get_input_spec_displacement_X(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_displacement_X(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_displacement_X(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_displacement_X(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_displacement_X(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_displacement_X(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_displacement_X(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_displacement_X(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_displacement_X(17), 17, op, -1) 

class _OutputSpecDisplacementX(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_displacement_X(), op)
        self.fields_container = Output(_get_output_spec_displacement_X(0), 0, op) 

class _DisplacementX(_Operator):
    """Operator's description:
    Internal name is "UX"
    Scripting name is "displacement_X"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal displacements X component of the vector (1st component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("UX")
    >>> op_way2 = core.operators.result.displacement_X()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("UX")
        self.inputs = _InputSpecDisplacementX(self)
        self.outputs = _OutputSpecDisplacementX(self)

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

def displacement_X():
    """Operator's description:
    Internal name is "UX"
    Scripting name is "displacement_X"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal displacements X component of the vector (1st component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("UX")
    >>> op_way2 = core.operators.result.displacement_X()
    """
    return _DisplacementX()

#internal name: UY
#scripting name: displacement_Y
def _get_input_spec_displacement_Y(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_displacement_Y = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_displacement_Y
    else:
        return inputs_dict_displacement_Y[pin]

def _get_output_spec_displacement_Y(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_displacement_Y = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_displacement_Y
    else:
        return outputs_dict_displacement_Y[pin]

class _InputSpecDisplacementY(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_displacement_Y(), op)
        self.time_scoping = Input(_get_input_spec_displacement_Y(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_displacement_Y(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_displacement_Y(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_displacement_Y(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_displacement_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_displacement_Y(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_displacement_Y(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_displacement_Y(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_displacement_Y(17), 17, op, -1) 

class _OutputSpecDisplacementY(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_displacement_Y(), op)
        self.fields_container = Output(_get_output_spec_displacement_Y(0), 0, op) 

class _DisplacementY(_Operator):
    """Operator's description:
    Internal name is "UY"
    Scripting name is "displacement_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal displacements Y component of the vector (2nd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("UY")
    >>> op_way2 = core.operators.result.displacement_Y()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("UY")
        self.inputs = _InputSpecDisplacementY(self)
        self.outputs = _OutputSpecDisplacementY(self)

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

def displacement_Y():
    """Operator's description:
    Internal name is "UY"
    Scripting name is "displacement_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal displacements Y component of the vector (2nd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("UY")
    >>> op_way2 = core.operators.result.displacement_Y()
    """
    return _DisplacementY()

#internal name: UZ
#scripting name: displacement_Z
def _get_input_spec_displacement_Z(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_displacement_Z = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_displacement_Z
    else:
        return inputs_dict_displacement_Z[pin]

def _get_output_spec_displacement_Z(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_displacement_Z = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_displacement_Z
    else:
        return outputs_dict_displacement_Z[pin]

class _InputSpecDisplacementZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_displacement_Z(), op)
        self.time_scoping = Input(_get_input_spec_displacement_Z(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_displacement_Z(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_displacement_Z(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_displacement_Z(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_displacement_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_displacement_Z(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_displacement_Z(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_displacement_Z(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_displacement_Z(17), 17, op, -1) 

class _OutputSpecDisplacementZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_displacement_Z(), op)
        self.fields_container = Output(_get_output_spec_displacement_Z(0), 0, op) 

class _DisplacementZ(_Operator):
    """Operator's description:
    Internal name is "UZ"
    Scripting name is "displacement_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal displacements Z component of the vector (3rd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("UZ")
    >>> op_way2 = core.operators.result.displacement_Z()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("UZ")
        self.inputs = _InputSpecDisplacementZ(self)
        self.outputs = _OutputSpecDisplacementZ(self)

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

def displacement_Z():
    """Operator's description:
    Internal name is "UZ"
    Scripting name is "displacement_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute nodal displacements Z component of the vector (3rd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("UZ")
    >>> op_way2 = core.operators.result.displacement_Z()
    """
    return _DisplacementZ()

#internal name: TFX
#scripting name: heat_flux_X
def _get_input_spec_heat_flux_X(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_heat_flux_X = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_heat_flux_X
    else:
        return inputs_dict_heat_flux_X[pin]

def _get_output_spec_heat_flux_X(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_heat_flux_X = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_heat_flux_X
    else:
        return outputs_dict_heat_flux_X[pin]

class _InputSpecHeatFluxX(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_heat_flux_X(), op)
        self.time_scoping = Input(_get_input_spec_heat_flux_X(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_heat_flux_X(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_heat_flux_X(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_heat_flux_X(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_heat_flux_X(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_heat_flux_X(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_heat_flux_X(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_heat_flux_X(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_heat_flux_X(17), 17, op, -1) 

class _OutputSpecHeatFluxX(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_heat_flux_X(), op)
        self.fields_container = Output(_get_output_spec_heat_flux_X(0), 0, op) 

class _HeatFluxX(_Operator):
    """Operator's description:
    Internal name is "TFX"
    Scripting name is "heat_flux_X"

    Description:  Load the appropriate operator based on the data sources and read/compute heat flux X component of the vector (1st component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TFX")
    >>> op_way2 = core.operators.result.heat_flux_X()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("TFX")
        self.inputs = _InputSpecHeatFluxX(self)
        self.outputs = _OutputSpecHeatFluxX(self)

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

def heat_flux_X():
    """Operator's description:
    Internal name is "TFX"
    Scripting name is "heat_flux_X"

    Description:  Load the appropriate operator based on the data sources and read/compute heat flux X component of the vector (1st component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TFX")
    >>> op_way2 = core.operators.result.heat_flux_X()
    """
    return _HeatFluxX()

#internal name: EF
#scripting name: electric_field
def _get_input_spec_electric_field(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_electric_field = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_electric_field
    else:
        return inputs_dict_electric_field[pin]

def _get_output_spec_electric_field(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_electric_field = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_electric_field
    else:
        return outputs_dict_electric_field[pin]

class _InputSpecElectricField(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_electric_field(), op)
        self.time_scoping = Input(_get_input_spec_electric_field(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_electric_field(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_electric_field(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_electric_field(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_electric_field(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_electric_field(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_electric_field(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_electric_field(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_electric_field(17), 17, op, -1) 

class _OutputSpecElectricField(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_electric_field(), op)
        self.fields_container = Output(_get_output_spec_electric_field(0), 0, op) 

class _ElectricField(_Operator):
    """Operator's description:
    Internal name is "EF"
    Scripting name is "electric_field"

    Description: Load the appropriate operator based on the data sources and read/compute electric field. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EF")
    >>> op_way2 = core.operators.result.electric_field()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("EF")
        self.inputs = _InputSpecElectricField(self)
        self.outputs = _OutputSpecElectricField(self)

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

def electric_field():
    """Operator's description:
    Internal name is "EF"
    Scripting name is "electric_field"

    Description: Load the appropriate operator based on the data sources and read/compute electric field. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("EF")
    >>> op_way2 = core.operators.result.electric_field()
    """
    return _ElectricField()

#internal name: TFY
#scripting name: heat_flux_Y
def _get_input_spec_heat_flux_Y(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_heat_flux_Y = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_heat_flux_Y
    else:
        return inputs_dict_heat_flux_Y[pin]

def _get_output_spec_heat_flux_Y(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_heat_flux_Y = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_heat_flux_Y
    else:
        return outputs_dict_heat_flux_Y[pin]

class _InputSpecHeatFluxY(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_heat_flux_Y(), op)
        self.time_scoping = Input(_get_input_spec_heat_flux_Y(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_heat_flux_Y(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_heat_flux_Y(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_heat_flux_Y(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_heat_flux_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_heat_flux_Y(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_heat_flux_Y(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_heat_flux_Y(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_heat_flux_Y(17), 17, op, -1) 

class _OutputSpecHeatFluxY(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_heat_flux_Y(), op)
        self.fields_container = Output(_get_output_spec_heat_flux_Y(0), 0, op) 

class _HeatFluxY(_Operator):
    """Operator's description:
    Internal name is "TFY"
    Scripting name is "heat_flux_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute heat flux Y component of the vector (2nd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TFY")
    >>> op_way2 = core.operators.result.heat_flux_Y()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("TFY")
        self.inputs = _InputSpecHeatFluxY(self)
        self.outputs = _OutputSpecHeatFluxY(self)

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

def heat_flux_Y():
    """Operator's description:
    Internal name is "TFY"
    Scripting name is "heat_flux_Y"

    Description:  Load the appropriate operator based on the data sources and read/compute heat flux Y component of the vector (2nd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TFY")
    >>> op_way2 = core.operators.result.heat_flux_Y()
    """
    return _HeatFluxY()

#internal name: TFZ
#scripting name: heat_flux_Z
def _get_input_spec_heat_flux_Z(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources // if stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """requested location, default is Nodal""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_heat_flux_Z = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_heat_flux_Z
    else:
        return inputs_dict_heat_flux_Z[pin]

def _get_output_spec_heat_flux_Z(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_heat_flux_Z = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_heat_flux_Z
    else:
        return outputs_dict_heat_flux_Z[pin]

class _InputSpecHeatFluxZ(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_heat_flux_Z(), op)
        self.time_scoping = Input(_get_input_spec_heat_flux_Z(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_heat_flux_Z(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_heat_flux_Z(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_heat_flux_Z(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_heat_flux_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_heat_flux_Z(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_heat_flux_Z(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_heat_flux_Z(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_heat_flux_Z(17), 17, op, -1) 

class _OutputSpecHeatFluxZ(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_heat_flux_Z(), op)
        self.fields_container = Output(_get_output_spec_heat_flux_Z(0), 0, op) 

class _HeatFluxZ(_Operator):
    """Operator's description:
    Internal name is "TFZ"
    Scripting name is "heat_flux_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute heat flux Z component of the vector (3rd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TFZ")
    >>> op_way2 = core.operators.result.heat_flux_Z()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("TFZ")
        self.inputs = _InputSpecHeatFluxZ(self)
        self.outputs = _OutputSpecHeatFluxZ(self)

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

def heat_flux_Z():
    """Operator's description:
    Internal name is "TFZ"
    Scripting name is "heat_flux_Z"

    Description:  Load the appropriate operator based on the data sources and read/compute heat flux Z component of the vector (3rd component). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (data sources // if stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location (requested location, default is Nodal)
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TFZ")
    >>> op_way2 = core.operators.result.heat_flux_Z()
    """
    return _HeatFluxZ()

#internal name: ENF
#scripting name: element_nodal_forces
def _get_input_spec_element_nodal_forces(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_element_nodal_forces = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_element_nodal_forces
    else:
        return inputs_dict_element_nodal_forces[pin]

def _get_output_spec_element_nodal_forces(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_element_nodal_forces = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_element_nodal_forces
    else:
        return outputs_dict_element_nodal_forces[pin]

class _InputSpecElementNodalForces(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_element_nodal_forces(), op)
        self.time_scoping = Input(_get_input_spec_element_nodal_forces(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_element_nodal_forces(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_element_nodal_forces(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_element_nodal_forces(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_element_nodal_forces(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_element_nodal_forces(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_element_nodal_forces(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_element_nodal_forces(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_element_nodal_forces(17), 17, op, -1) 

class _OutputSpecElementNodalForces(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_element_nodal_forces(), op)
        self.fields_container = Output(_get_output_spec_element_nodal_forces(0), 0, op) 

class _ElementNodalForces(_Operator):
    """Operator's description:
    Internal name is "ENF"
    Scripting name is "element_nodal_forces"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal forces. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENF")
    >>> op_way2 = core.operators.result.element_nodal_forces()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENF")
        self.inputs = _InputSpecElementNodalForces(self)
        self.outputs = _OutputSpecElementNodalForces(self)

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

def element_nodal_forces():
    """Operator's description:
    Internal name is "ENF"
    Scripting name is "element_nodal_forces"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal forces. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENF")
    >>> op_way2 = core.operators.result.element_nodal_forces()
    """
    return _ElementNodalForces()

#internal name: BFE
#scripting name: structural_temperature
def _get_input_spec_structural_temperature(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_structural_temperature = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_structural_temperature
    else:
        return inputs_dict_structural_temperature[pin]

def _get_output_spec_structural_temperature(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_structural_temperature = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_structural_temperature
    else:
        return outputs_dict_structural_temperature[pin]

class _InputSpecStructuralTemperature(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_structural_temperature(), op)
        self.time_scoping = Input(_get_input_spec_structural_temperature(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_structural_temperature(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_structural_temperature(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_structural_temperature(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_structural_temperature(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_structural_temperature(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_structural_temperature(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_structural_temperature(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_structural_temperature(17), 17, op, -1) 

class _OutputSpecStructuralTemperature(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_structural_temperature(), op)
        self.fields_container = Output(_get_output_spec_structural_temperature(0), 0, op) 

class _StructuralTemperature(_Operator):
    """Operator's description:
    Internal name is "BFE"
    Scripting name is "structural_temperature"

    Description: Load the appropriate operator based on the data sources and read/compute element structural nodal temperatures. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("BFE")
    >>> op_way2 = core.operators.result.structural_temperature()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("BFE")
        self.inputs = _InputSpecStructuralTemperature(self)
        self.outputs = _OutputSpecStructuralTemperature(self)

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

def structural_temperature():
    """Operator's description:
    Internal name is "BFE"
    Scripting name is "structural_temperature"

    Description: Load the appropriate operator based on the data sources and read/compute element structural nodal temperatures. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("BFE")
    >>> op_way2 = core.operators.result.structural_temperature()
    """
    return _StructuralTemperature()

#internal name: ENG_INC
#scripting name: incremental_energy
def _get_input_spec_incremental_energy(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_incremental_energy = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_incremental_energy
    else:
        return inputs_dict_incremental_energy[pin]

def _get_output_spec_incremental_energy(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_incremental_energy = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_incremental_energy
    else:
        return outputs_dict_incremental_energy[pin]

class _InputSpecIncrementalEnergy(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_incremental_energy(), op)
        self.time_scoping = Input(_get_input_spec_incremental_energy(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_incremental_energy(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_incremental_energy(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_incremental_energy(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_incremental_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_incremental_energy(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_incremental_energy(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_incremental_energy(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_incremental_energy(17), 17, op, -1) 

class _OutputSpecIncrementalEnergy(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_incremental_energy(), op)
        self.fields_container = Output(_get_output_spec_incremental_energy(0), 0, op) 

class _IncrementalEnergy(_Operator):
    """Operator's description:
    Internal name is "ENG_INC"
    Scripting name is "incremental_energy"

    Description: Load the appropriate operator based on the data sources and read/compute incremental energy (magnetics). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_INC")
    >>> op_way2 = core.operators.result.incremental_energy()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENG_INC")
        self.inputs = _InputSpecIncrementalEnergy(self)
        self.outputs = _OutputSpecIncrementalEnergy(self)

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

def incremental_energy():
    """Operator's description:
    Internal name is "ENG_INC"
    Scripting name is "incremental_energy"

    Description: Load the appropriate operator based on the data sources and read/compute incremental energy (magnetics). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_INC")
    >>> op_way2 = core.operators.result.incremental_energy()
    """
    return _IncrementalEnergy()

#internal name: ENG_SE
#scripting name: stiffness_matrix_energy
def _get_input_spec_stiffness_matrix_energy(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stiffness_matrix_energy = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stiffness_matrix_energy
    else:
        return inputs_dict_stiffness_matrix_energy[pin]

def _get_output_spec_stiffness_matrix_energy(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stiffness_matrix_energy = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stiffness_matrix_energy
    else:
        return outputs_dict_stiffness_matrix_energy[pin]

class _InputSpecStiffnessMatrixEnergy(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stiffness_matrix_energy(), op)
        self.time_scoping = Input(_get_input_spec_stiffness_matrix_energy(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stiffness_matrix_energy(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stiffness_matrix_energy(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stiffness_matrix_energy(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stiffness_matrix_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stiffness_matrix_energy(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stiffness_matrix_energy(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stiffness_matrix_energy(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stiffness_matrix_energy(17), 17, op, -1) 

class _OutputSpecStiffnessMatrixEnergy(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stiffness_matrix_energy(), op)
        self.fields_container = Output(_get_output_spec_stiffness_matrix_energy(0), 0, op) 

class _StiffnessMatrixEnergy(_Operator):
    """Operator's description:
    Internal name is "ENG_SE"
    Scripting name is "stiffness_matrix_energy"

    Description: Load the appropriate operator based on the data sources and read/compute element energy associated with the stiffness matrix. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_SE")
    >>> op_way2 = core.operators.result.stiffness_matrix_energy()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENG_SE")
        self.inputs = _InputSpecStiffnessMatrixEnergy(self)
        self.outputs = _OutputSpecStiffnessMatrixEnergy(self)

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

def stiffness_matrix_energy():
    """Operator's description:
    Internal name is "ENG_SE"
    Scripting name is "stiffness_matrix_energy"

    Description: Load the appropriate operator based on the data sources and read/compute element energy associated with the stiffness matrix. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_SE")
    >>> op_way2 = core.operators.result.stiffness_matrix_energy()
    """
    return _StiffnessMatrixEnergy()

#internal name: ETH
#scripting name: thermal_strain
def _get_input_spec_thermal_strain(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_thermal_strain = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_thermal_strain
    else:
        return inputs_dict_thermal_strain[pin]

def _get_output_spec_thermal_strain(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_thermal_strain = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_thermal_strain
    else:
        return outputs_dict_thermal_strain[pin]

class _InputSpecThermalStrain(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_thermal_strain(), op)
        self.time_scoping = Input(_get_input_spec_thermal_strain(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_thermal_strain(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_thermal_strain(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_thermal_strain(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_thermal_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_thermal_strain(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_thermal_strain(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_thermal_strain(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_thermal_strain(17), 17, op, -1) 

class _OutputSpecThermalStrain(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_thermal_strain(), op)
        self.fields_container = Output(_get_output_spec_thermal_strain(0), 0, op) 

class _ThermalStrain(_Operator):
    """Operator's description:
    Internal name is "ETH"
    Scripting name is "thermal_strain"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal component thermal strains. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ETH")
    >>> op_way2 = core.operators.result.thermal_strain()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ETH")
        self.inputs = _InputSpecThermalStrain(self)
        self.outputs = _OutputSpecThermalStrain(self)

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

def thermal_strain():
    """Operator's description:
    Internal name is "ETH"
    Scripting name is "thermal_strain"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal component thermal strains. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ETH")
    >>> op_way2 = core.operators.result.thermal_strain()
    """
    return _ThermalStrain()

#internal name: ENL_SEPL
#scripting name: eqv_stress_parameter
def _get_input_spec_eqv_stress_parameter(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_eqv_stress_parameter = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_eqv_stress_parameter
    else:
        return inputs_dict_eqv_stress_parameter[pin]

def _get_output_spec_eqv_stress_parameter(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_eqv_stress_parameter = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_eqv_stress_parameter
    else:
        return outputs_dict_eqv_stress_parameter[pin]

class _InputSpecEqvStressParameter(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_eqv_stress_parameter(), op)
        self.time_scoping = Input(_get_input_spec_eqv_stress_parameter(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_eqv_stress_parameter(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_eqv_stress_parameter(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_eqv_stress_parameter(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_eqv_stress_parameter(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_eqv_stress_parameter(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_eqv_stress_parameter(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_eqv_stress_parameter(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_eqv_stress_parameter(17), 17, op, -1) 

class _OutputSpecEqvStressParameter(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_eqv_stress_parameter(), op)
        self.fields_container = Output(_get_output_spec_eqv_stress_parameter(0), 0, op) 

class _EqvStressParameter(_Operator):
    """Operator's description:
    Internal name is "ENL_SEPL"
    Scripting name is "eqv_stress_parameter"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal equivalent stress parameter. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_SEPL")
    >>> op_way2 = core.operators.result.eqv_stress_parameter()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENL_SEPL")
        self.inputs = _InputSpecEqvStressParameter(self)
        self.outputs = _OutputSpecEqvStressParameter(self)

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

def eqv_stress_parameter():
    """Operator's description:
    Internal name is "ENL_SEPL"
    Scripting name is "eqv_stress_parameter"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal equivalent stress parameter. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_SEPL")
    >>> op_way2 = core.operators.result.eqv_stress_parameter()
    """
    return _EqvStressParameter()

#internal name: ENL_SRAT
#scripting name: stress_ratio
def _get_input_spec_stress_ratio(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_ratio = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_ratio
    else:
        return inputs_dict_stress_ratio[pin]

def _get_output_spec_stress_ratio(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_ratio = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_ratio
    else:
        return outputs_dict_stress_ratio[pin]

class _InputSpecStressRatio(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_ratio(), op)
        self.time_scoping = Input(_get_input_spec_stress_ratio(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_ratio(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_ratio(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_ratio(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_ratio(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_ratio(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_ratio(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_ratio(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_ratio(17), 17, op, -1) 

class _OutputSpecStressRatio(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_ratio(), op)
        self.fields_container = Output(_get_output_spec_stress_ratio(0), 0, op) 

class _StressRatio(_Operator):
    """Operator's description:
    Internal name is "ENL_SRAT"
    Scripting name is "stress_ratio"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal stress ratio. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_SRAT")
    >>> op_way2 = core.operators.result.stress_ratio()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENL_SRAT")
        self.inputs = _InputSpecStressRatio(self)
        self.outputs = _OutputSpecStressRatio(self)

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

def stress_ratio():
    """Operator's description:
    Internal name is "ENL_SRAT"
    Scripting name is "stress_ratio"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal stress ratio. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_SRAT")
    >>> op_way2 = core.operators.result.stress_ratio()
    """
    return _StressRatio()

#internal name: ENL_EPEQ
#scripting name: accu_eqv_plastic_strain
def _get_input_spec_accu_eqv_plastic_strain(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_accu_eqv_plastic_strain = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_accu_eqv_plastic_strain
    else:
        return inputs_dict_accu_eqv_plastic_strain[pin]

def _get_output_spec_accu_eqv_plastic_strain(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_accu_eqv_plastic_strain = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_accu_eqv_plastic_strain
    else:
        return outputs_dict_accu_eqv_plastic_strain[pin]

class _InputSpecAccuEqvPlasticStrain(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_accu_eqv_plastic_strain(), op)
        self.time_scoping = Input(_get_input_spec_accu_eqv_plastic_strain(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_accu_eqv_plastic_strain(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_accu_eqv_plastic_strain(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_accu_eqv_plastic_strain(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_accu_eqv_plastic_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_accu_eqv_plastic_strain(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_accu_eqv_plastic_strain(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_accu_eqv_plastic_strain(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_accu_eqv_plastic_strain(17), 17, op, -1) 

class _OutputSpecAccuEqvPlasticStrain(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_accu_eqv_plastic_strain(), op)
        self.fields_container = Output(_get_output_spec_accu_eqv_plastic_strain(0), 0, op) 

class _AccuEqvPlasticStrain(_Operator):
    """Operator's description:
    Internal name is "ENL_EPEQ"
    Scripting name is "accu_eqv_plastic_strain"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal accumulated equivalent plastic strain. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_EPEQ")
    >>> op_way2 = core.operators.result.accu_eqv_plastic_strain()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENL_EPEQ")
        self.inputs = _InputSpecAccuEqvPlasticStrain(self)
        self.outputs = _OutputSpecAccuEqvPlasticStrain(self)

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

def accu_eqv_plastic_strain():
    """Operator's description:
    Internal name is "ENL_EPEQ"
    Scripting name is "accu_eqv_plastic_strain"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal accumulated equivalent plastic strain. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_EPEQ")
    >>> op_way2 = core.operators.result.accu_eqv_plastic_strain()
    """
    return _AccuEqvPlasticStrain()

#internal name: ENL_PSV
#scripting name: plastic_state_variable
def _get_input_spec_plastic_state_variable(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_state_variable = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_state_variable
    else:
        return inputs_dict_plastic_state_variable[pin]

def _get_output_spec_plastic_state_variable(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_state_variable = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_state_variable
    else:
        return outputs_dict_plastic_state_variable[pin]

class _InputSpecPlasticStateVariable(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_state_variable(), op)
        self.time_scoping = Input(_get_input_spec_plastic_state_variable(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_state_variable(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_state_variable(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_state_variable(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_state_variable(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_state_variable(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_state_variable(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_state_variable(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_state_variable(17), 17, op, -1) 

class _OutputSpecPlasticStateVariable(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_state_variable(), op)
        self.fields_container = Output(_get_output_spec_plastic_state_variable(0), 0, op) 

class _PlasticStateVariable(_Operator):
    """Operator's description:
    Internal name is "ENL_PSV"
    Scripting name is "plastic_state_variable"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal plastic state variable. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_PSV")
    >>> op_way2 = core.operators.result.plastic_state_variable()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENL_PSV")
        self.inputs = _InputSpecPlasticStateVariable(self)
        self.outputs = _OutputSpecPlasticStateVariable(self)

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

def plastic_state_variable():
    """Operator's description:
    Internal name is "ENL_PSV"
    Scripting name is "plastic_state_variable"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal plastic state variable. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_PSV")
    >>> op_way2 = core.operators.result.plastic_state_variable()
    """
    return _PlasticStateVariable()

#internal name: ENL_CREQ
#scripting name: accu_eqv_creep_strain
def _get_input_spec_accu_eqv_creep_strain(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_accu_eqv_creep_strain = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_accu_eqv_creep_strain
    else:
        return inputs_dict_accu_eqv_creep_strain[pin]

def _get_output_spec_accu_eqv_creep_strain(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_accu_eqv_creep_strain = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_accu_eqv_creep_strain
    else:
        return outputs_dict_accu_eqv_creep_strain[pin]

class _InputSpecAccuEqvCreepStrain(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_accu_eqv_creep_strain(), op)
        self.time_scoping = Input(_get_input_spec_accu_eqv_creep_strain(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_accu_eqv_creep_strain(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_accu_eqv_creep_strain(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_accu_eqv_creep_strain(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_accu_eqv_creep_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_accu_eqv_creep_strain(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_accu_eqv_creep_strain(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_accu_eqv_creep_strain(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_accu_eqv_creep_strain(17), 17, op, -1) 

class _OutputSpecAccuEqvCreepStrain(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_accu_eqv_creep_strain(), op)
        self.fields_container = Output(_get_output_spec_accu_eqv_creep_strain(0), 0, op) 

class _AccuEqvCreepStrain(_Operator):
    """Operator's description:
    Internal name is "ENL_CREQ"
    Scripting name is "accu_eqv_creep_strain"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal accumulated equivalent creep strain. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_CREQ")
    >>> op_way2 = core.operators.result.accu_eqv_creep_strain()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENL_CREQ")
        self.inputs = _InputSpecAccuEqvCreepStrain(self)
        self.outputs = _OutputSpecAccuEqvCreepStrain(self)

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

def accu_eqv_creep_strain():
    """Operator's description:
    Internal name is "ENL_CREQ"
    Scripting name is "accu_eqv_creep_strain"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal accumulated equivalent creep strain. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_CREQ")
    >>> op_way2 = core.operators.result.accu_eqv_creep_strain()
    """
    return _AccuEqvCreepStrain()

#internal name: ENL_PLWK
#scripting name: plastic_strain_energy_density
def _get_input_spec_plastic_strain_energy_density(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_plastic_strain_energy_density = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_plastic_strain_energy_density
    else:
        return inputs_dict_plastic_strain_energy_density[pin]

def _get_output_spec_plastic_strain_energy_density(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_energy_density = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_energy_density
    else:
        return outputs_dict_plastic_strain_energy_density[pin]

class _InputSpecPlasticStrainEnergyDensity(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_energy_density(), op)
        self.time_scoping = Input(_get_input_spec_plastic_strain_energy_density(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_plastic_strain_energy_density(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_plastic_strain_energy_density(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_energy_density(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_energy_density(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_plastic_strain_energy_density(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_plastic_strain_energy_density(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_plastic_strain_energy_density(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_plastic_strain_energy_density(17), 17, op, -1) 

class _OutputSpecPlasticStrainEnergyDensity(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_energy_density(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_energy_density(0), 0, op) 

class _PlasticStrainEnergyDensity(_Operator):
    """Operator's description:
    Internal name is "ENL_PLWK"
    Scripting name is "plastic_strain_energy_density"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal plastic strain energy density. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_PLWK")
    >>> op_way2 = core.operators.result.plastic_strain_energy_density()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENL_PLWK")
        self.inputs = _InputSpecPlasticStrainEnergyDensity(self)
        self.outputs = _OutputSpecPlasticStrainEnergyDensity(self)

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

def plastic_strain_energy_density():
    """Operator's description:
    Internal name is "ENL_PLWK"
    Scripting name is "plastic_strain_energy_density"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal plastic strain energy density. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_PLWK")
    >>> op_way2 = core.operators.result.plastic_strain_energy_density()
    """
    return _PlasticStrainEnergyDensity()

#internal name: MaterialPropertyOfElement
#scripting name: material_property_of_element
def _get_input_spec_material_property_of_element(pin = None):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_material_property_of_element = { 
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_material_property_of_element
    else:
        return inputs_dict_material_property_of_element[pin]

def _get_output_spec_material_property_of_element(pin = None):
    outpin0 = _PinSpecification(name = "material_properties", type_names = ["field"], document = """material properties""")
    outputs_dict_material_property_of_element = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_material_property_of_element
    else:
        return outputs_dict_material_property_of_element[pin]

class _InputSpecMaterialPropertyOfElement(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_material_property_of_element(), op)
        self.streams_container = Input(_get_input_spec_material_property_of_element(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_material_property_of_element(4), 4, op, -1) 

class _OutputSpecMaterialPropertyOfElement(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_material_property_of_element(), op)
        self.material_properties = Output(_get_output_spec_material_property_of_element(0), 0, op) 

class _MaterialPropertyOfElement(_Operator):
    """Operator's description:
    Internal name is "MaterialPropertyOfElement"
    Scripting name is "material_property_of_element"

    Description:  Load the appropriate operator based on the data sources and get material properties

    Input list: 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: material_properties (material properties)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("MaterialPropertyOfElement")
    >>> op_way2 = core.operators.result.material_property_of_element()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("MaterialPropertyOfElement")
        self.inputs = _InputSpecMaterialPropertyOfElement(self)
        self.outputs = _OutputSpecMaterialPropertyOfElement(self)

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

def material_property_of_element():
    """Operator's description:
    Internal name is "MaterialPropertyOfElement"
    Scripting name is "material_property_of_element"

    Description:  Load the appropriate operator based on the data sources and get material properties

    Input list: 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: material_properties (material properties)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("MaterialPropertyOfElement")
    >>> op_way2 = core.operators.result.material_property_of_element()
    """
    return _MaterialPropertyOfElement()

#internal name: ENL_CRWK
#scripting name: creep_strain_energy_density
def _get_input_spec_creep_strain_energy_density(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_creep_strain_energy_density = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_creep_strain_energy_density
    else:
        return inputs_dict_creep_strain_energy_density[pin]

def _get_output_spec_creep_strain_energy_density(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_creep_strain_energy_density = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_creep_strain_energy_density
    else:
        return outputs_dict_creep_strain_energy_density[pin]

class _InputSpecCreepStrainEnergyDensity(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_creep_strain_energy_density(), op)
        self.time_scoping = Input(_get_input_spec_creep_strain_energy_density(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_creep_strain_energy_density(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_creep_strain_energy_density(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_creep_strain_energy_density(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_creep_strain_energy_density(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_creep_strain_energy_density(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_creep_strain_energy_density(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_creep_strain_energy_density(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_creep_strain_energy_density(17), 17, op, -1) 

class _OutputSpecCreepStrainEnergyDensity(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_creep_strain_energy_density(), op)
        self.fields_container = Output(_get_output_spec_creep_strain_energy_density(0), 0, op) 

class _CreepStrainEnergyDensity(_Operator):
    """Operator's description:
    Internal name is "ENL_CRWK"
    Scripting name is "creep_strain_energy_density"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal creep strain energy density. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_CRWK")
    >>> op_way2 = core.operators.result.creep_strain_energy_density()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENL_CRWK")
        self.inputs = _InputSpecCreepStrainEnergyDensity(self)
        self.outputs = _OutputSpecCreepStrainEnergyDensity(self)

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

def creep_strain_energy_density():
    """Operator's description:
    Internal name is "ENL_CRWK"
    Scripting name is "creep_strain_energy_density"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal creep strain energy density. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_CRWK")
    >>> op_way2 = core.operators.result.creep_strain_energy_density()
    """
    return _CreepStrainEnergyDensity()

#internal name: ENL_ELENG
#scripting name: elastic_strain_energy_density
def _get_input_spec_elastic_strain_energy_density(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elastic_strain_energy_density = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elastic_strain_energy_density
    else:
        return inputs_dict_elastic_strain_energy_density[pin]

def _get_output_spec_elastic_strain_energy_density(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_energy_density = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_energy_density
    else:
        return outputs_dict_elastic_strain_energy_density[pin]

class _InputSpecElasticStrainEnergyDensity(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_energy_density(), op)
        self.time_scoping = Input(_get_input_spec_elastic_strain_energy_density(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elastic_strain_energy_density(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elastic_strain_energy_density(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_energy_density(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_energy_density(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elastic_strain_energy_density(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elastic_strain_energy_density(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elastic_strain_energy_density(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elastic_strain_energy_density(17), 17, op, -1) 

class _OutputSpecElasticStrainEnergyDensity(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_energy_density(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_energy_density(0), 0, op) 

class _ElasticStrainEnergyDensity(_Operator):
    """Operator's description:
    Internal name is "ENL_ELENG"
    Scripting name is "elastic_strain_energy_density"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal elastic strain energy density. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_ELENG")
    >>> op_way2 = core.operators.result.elastic_strain_energy_density()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENL_ELENG")
        self.inputs = _InputSpecElasticStrainEnergyDensity(self)
        self.outputs = _OutputSpecElasticStrainEnergyDensity(self)

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

def elastic_strain_energy_density():
    """Operator's description:
    Internal name is "ENL_ELENG"
    Scripting name is "elastic_strain_energy_density"

    Description: Load the appropriate operator based on the data sources and read/compute element nodal elastic strain energy density. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENL_ELENG")
    >>> op_way2 = core.operators.result.elastic_strain_energy_density()
    """
    return _ElasticStrainEnergyDensity()

#internal name: ECT_STAT
#scripting name: contact_status
def _get_input_spec_contact_status(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_contact_status = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_contact_status
    else:
        return inputs_dict_contact_status[pin]

def _get_output_spec_contact_status(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_status = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_contact_status
    else:
        return outputs_dict_contact_status[pin]

class _InputSpecContactStatus(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_contact_status(), op)
        self.time_scoping = Input(_get_input_spec_contact_status(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_contact_status(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_contact_status(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_contact_status(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_contact_status(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_contact_status(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_contact_status(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_contact_status(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_contact_status(17), 17, op, -1) 

class _OutputSpecContactStatus(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_contact_status(), op)
        self.fields_container = Output(_get_output_spec_contact_status(0), 0, op) 

class _ContactStatus(_Operator):
    """Operator's description:
    Internal name is "ECT_STAT"
    Scripting name is "contact_status"

    Description: Load the appropriate operator based on the data sources and read/compute element contact status. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_STAT")
    >>> op_way2 = core.operators.result.contact_status()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ECT_STAT")
        self.inputs = _InputSpecContactStatus(self)
        self.outputs = _OutputSpecContactStatus(self)

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

def contact_status():
    """Operator's description:
    Internal name is "ECT_STAT"
    Scripting name is "contact_status"

    Description: Load the appropriate operator based on the data sources and read/compute element contact status. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_STAT")
    >>> op_way2 = core.operators.result.contact_status()
    """
    return _ContactStatus()

#internal name: ECT_PENE
#scripting name: contact_penetration
def _get_input_spec_contact_penetration(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_contact_penetration = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_contact_penetration
    else:
        return inputs_dict_contact_penetration[pin]

def _get_output_spec_contact_penetration(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_penetration = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_contact_penetration
    else:
        return outputs_dict_contact_penetration[pin]

class _InputSpecContactPenetration(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_contact_penetration(), op)
        self.time_scoping = Input(_get_input_spec_contact_penetration(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_contact_penetration(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_contact_penetration(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_contact_penetration(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_contact_penetration(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_contact_penetration(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_contact_penetration(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_contact_penetration(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_contact_penetration(17), 17, op, -1) 

class _OutputSpecContactPenetration(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_contact_penetration(), op)
        self.fields_container = Output(_get_output_spec_contact_penetration(0), 0, op) 

class _ContactPenetration(_Operator):
    """Operator's description:
    Internal name is "ECT_PENE"
    Scripting name is "contact_penetration"

    Description: Load the appropriate operator based on the data sources and read/compute element contact penetration. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_PENE")
    >>> op_way2 = core.operators.result.contact_penetration()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ECT_PENE")
        self.inputs = _InputSpecContactPenetration(self)
        self.outputs = _OutputSpecContactPenetration(self)

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

def contact_penetration():
    """Operator's description:
    Internal name is "ECT_PENE"
    Scripting name is "contact_penetration"

    Description: Load the appropriate operator based on the data sources and read/compute element contact penetration. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_PENE")
    >>> op_way2 = core.operators.result.contact_penetration()
    """
    return _ContactPenetration()

#internal name: ECT_PRES
#scripting name: contact_pressure
def _get_input_spec_contact_pressure(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_contact_pressure = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_contact_pressure
    else:
        return inputs_dict_contact_pressure[pin]

def _get_output_spec_contact_pressure(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_pressure = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_contact_pressure
    else:
        return outputs_dict_contact_pressure[pin]

class _InputSpecContactPressure(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_contact_pressure(), op)
        self.time_scoping = Input(_get_input_spec_contact_pressure(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_contact_pressure(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_contact_pressure(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_contact_pressure(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_contact_pressure(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_contact_pressure(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_contact_pressure(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_contact_pressure(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_contact_pressure(17), 17, op, -1) 

class _OutputSpecContactPressure(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_contact_pressure(), op)
        self.fields_container = Output(_get_output_spec_contact_pressure(0), 0, op) 

class _ContactPressure(_Operator):
    """Operator's description:
    Internal name is "ECT_PRES"
    Scripting name is "contact_pressure"

    Description: Load the appropriate operator based on the data sources and read/compute element contact pressure. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_PRES")
    >>> op_way2 = core.operators.result.contact_pressure()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ECT_PRES")
        self.inputs = _InputSpecContactPressure(self)
        self.outputs = _OutputSpecContactPressure(self)

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

def contact_pressure():
    """Operator's description:
    Internal name is "ECT_PRES"
    Scripting name is "contact_pressure"

    Description: Load the appropriate operator based on the data sources and read/compute element contact pressure. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_PRES")
    >>> op_way2 = core.operators.result.contact_pressure()
    """
    return _ContactPressure()

#internal name: ECT_SFRIC
#scripting name: contact_friction_stress
def _get_input_spec_contact_friction_stress(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_contact_friction_stress = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_contact_friction_stress
    else:
        return inputs_dict_contact_friction_stress[pin]

def _get_output_spec_contact_friction_stress(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_friction_stress = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_contact_friction_stress
    else:
        return outputs_dict_contact_friction_stress[pin]

class _InputSpecContactFrictionStress(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_contact_friction_stress(), op)
        self.time_scoping = Input(_get_input_spec_contact_friction_stress(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_contact_friction_stress(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_contact_friction_stress(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_contact_friction_stress(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_contact_friction_stress(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_contact_friction_stress(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_contact_friction_stress(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_contact_friction_stress(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_contact_friction_stress(17), 17, op, -1) 

class _OutputSpecContactFrictionStress(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_contact_friction_stress(), op)
        self.fields_container = Output(_get_output_spec_contact_friction_stress(0), 0, op) 

class _ContactFrictionStress(_Operator):
    """Operator's description:
    Internal name is "ECT_SFRIC"
    Scripting name is "contact_friction_stress"

    Description: Load the appropriate operator based on the data sources and read/compute element contact friction stress. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_SFRIC")
    >>> op_way2 = core.operators.result.contact_friction_stress()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ECT_SFRIC")
        self.inputs = _InputSpecContactFrictionStress(self)
        self.outputs = _OutputSpecContactFrictionStress(self)

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

def contact_friction_stress():
    """Operator's description:
    Internal name is "ECT_SFRIC"
    Scripting name is "contact_friction_stress"

    Description: Load the appropriate operator based on the data sources and read/compute element contact friction stress. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_SFRIC")
    >>> op_way2 = core.operators.result.contact_friction_stress()
    """
    return _ContactFrictionStress()

#internal name: ECT_STOT
#scripting name: contact_total_stress
def _get_input_spec_contact_total_stress(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_contact_total_stress = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_contact_total_stress
    else:
        return inputs_dict_contact_total_stress[pin]

def _get_output_spec_contact_total_stress(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_total_stress = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_contact_total_stress
    else:
        return outputs_dict_contact_total_stress[pin]

class _InputSpecContactTotalStress(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_contact_total_stress(), op)
        self.time_scoping = Input(_get_input_spec_contact_total_stress(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_contact_total_stress(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_contact_total_stress(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_contact_total_stress(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_contact_total_stress(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_contact_total_stress(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_contact_total_stress(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_contact_total_stress(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_contact_total_stress(17), 17, op, -1) 

class _OutputSpecContactTotalStress(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_contact_total_stress(), op)
        self.fields_container = Output(_get_output_spec_contact_total_stress(0), 0, op) 

class _ContactTotalStress(_Operator):
    """Operator's description:
    Internal name is "ECT_STOT"
    Scripting name is "contact_total_stress"

    Description: Load the appropriate operator based on the data sources and read/compute element contact total stress (pressure plus friction). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_STOT")
    >>> op_way2 = core.operators.result.contact_total_stress()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ECT_STOT")
        self.inputs = _InputSpecContactTotalStress(self)
        self.outputs = _OutputSpecContactTotalStress(self)

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

def contact_total_stress():
    """Operator's description:
    Internal name is "ECT_STOT"
    Scripting name is "contact_total_stress"

    Description: Load the appropriate operator based on the data sources and read/compute element contact total stress (pressure plus friction). Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_STOT")
    >>> op_way2 = core.operators.result.contact_total_stress()
    """
    return _ContactTotalStress()

#internal name: ECT_SLIDE
#scripting name: contact_sliding_distance
def _get_input_spec_contact_sliding_distance(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_contact_sliding_distance = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_contact_sliding_distance
    else:
        return inputs_dict_contact_sliding_distance[pin]

def _get_output_spec_contact_sliding_distance(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_sliding_distance = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_contact_sliding_distance
    else:
        return outputs_dict_contact_sliding_distance[pin]

class _InputSpecContactSlidingDistance(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_contact_sliding_distance(), op)
        self.time_scoping = Input(_get_input_spec_contact_sliding_distance(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_contact_sliding_distance(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_contact_sliding_distance(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_contact_sliding_distance(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_contact_sliding_distance(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_contact_sliding_distance(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_contact_sliding_distance(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_contact_sliding_distance(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_contact_sliding_distance(17), 17, op, -1) 

class _OutputSpecContactSlidingDistance(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_contact_sliding_distance(), op)
        self.fields_container = Output(_get_output_spec_contact_sliding_distance(0), 0, op) 

class _ContactSlidingDistance(_Operator):
    """Operator's description:
    Internal name is "ECT_SLIDE"
    Scripting name is "contact_sliding_distance"

    Description: Load the appropriate operator based on the data sources and read/compute element contact sliding distance. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_SLIDE")
    >>> op_way2 = core.operators.result.contact_sliding_distance()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ECT_SLIDE")
        self.inputs = _InputSpecContactSlidingDistance(self)
        self.outputs = _OutputSpecContactSlidingDistance(self)

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

def contact_sliding_distance():
    """Operator's description:
    Internal name is "ECT_SLIDE"
    Scripting name is "contact_sliding_distance"

    Description: Load the appropriate operator based on the data sources and read/compute element contact sliding distance. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_SLIDE")
    >>> op_way2 = core.operators.result.contact_sliding_distance()
    """
    return _ContactSlidingDistance()

#internal name: ECT_GAP
#scripting name: contact_gap_distance
def _get_input_spec_contact_gap_distance(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_contact_gap_distance = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_contact_gap_distance
    else:
        return inputs_dict_contact_gap_distance[pin]

def _get_output_spec_contact_gap_distance(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_gap_distance = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_contact_gap_distance
    else:
        return outputs_dict_contact_gap_distance[pin]

class _InputSpecContactGapDistance(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_contact_gap_distance(), op)
        self.time_scoping = Input(_get_input_spec_contact_gap_distance(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_contact_gap_distance(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_contact_gap_distance(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_contact_gap_distance(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_contact_gap_distance(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_contact_gap_distance(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_contact_gap_distance(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_contact_gap_distance(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_contact_gap_distance(17), 17, op, -1) 

class _OutputSpecContactGapDistance(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_contact_gap_distance(), op)
        self.fields_container = Output(_get_output_spec_contact_gap_distance(0), 0, op) 

class _ContactGapDistance(_Operator):
    """Operator's description:
    Internal name is "ECT_GAP"
    Scripting name is "contact_gap_distance"

    Description: Load the appropriate operator based on the data sources and read/compute element contact gap distance. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_GAP")
    >>> op_way2 = core.operators.result.contact_gap_distance()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ECT_GAP")
        self.inputs = _InputSpecContactGapDistance(self)
        self.outputs = _OutputSpecContactGapDistance(self)

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

def contact_gap_distance():
    """Operator's description:
    Internal name is "ECT_GAP"
    Scripting name is "contact_gap_distance"

    Description: Load the appropriate operator based on the data sources and read/compute element contact gap distance. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_GAP")
    >>> op_way2 = core.operators.result.contact_gap_distance()
    """
    return _ContactGapDistance()

#internal name: ECT_FLUX
#scripting name: contact_surface_heat_flux
def _get_input_spec_contact_surface_heat_flux(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_contact_surface_heat_flux = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_contact_surface_heat_flux
    else:
        return inputs_dict_contact_surface_heat_flux[pin]

def _get_output_spec_contact_surface_heat_flux(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_surface_heat_flux = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_contact_surface_heat_flux
    else:
        return outputs_dict_contact_surface_heat_flux[pin]

class _InputSpecContactSurfaceHeatFlux(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_contact_surface_heat_flux(), op)
        self.time_scoping = Input(_get_input_spec_contact_surface_heat_flux(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_contact_surface_heat_flux(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_contact_surface_heat_flux(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_contact_surface_heat_flux(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_contact_surface_heat_flux(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_contact_surface_heat_flux(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_contact_surface_heat_flux(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_contact_surface_heat_flux(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_contact_surface_heat_flux(17), 17, op, -1) 

class _OutputSpecContactSurfaceHeatFlux(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_contact_surface_heat_flux(), op)
        self.fields_container = Output(_get_output_spec_contact_surface_heat_flux(0), 0, op) 

class _ContactSurfaceHeatFlux(_Operator):
    """Operator's description:
    Internal name is "ECT_FLUX"
    Scripting name is "contact_surface_heat_flux"

    Description: Load the appropriate operator based on the data sources and read/compute element total heat flux at contact surface. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_FLUX")
    >>> op_way2 = core.operators.result.contact_surface_heat_flux()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ECT_FLUX")
        self.inputs = _InputSpecContactSurfaceHeatFlux(self)
        self.outputs = _OutputSpecContactSurfaceHeatFlux(self)

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

def contact_surface_heat_flux():
    """Operator's description:
    Internal name is "ECT_FLUX"
    Scripting name is "contact_surface_heat_flux"

    Description: Load the appropriate operator based on the data sources and read/compute element total heat flux at contact surface. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_FLUX")
    >>> op_way2 = core.operators.result.contact_surface_heat_flux()
    """
    return _ContactSurfaceHeatFlux()

#internal name: ECT_CNOS
#scripting name: num_surface_status_changes
def _get_input_spec_num_surface_status_changes(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_num_surface_status_changes = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_num_surface_status_changes
    else:
        return inputs_dict_num_surface_status_changes[pin]

def _get_output_spec_num_surface_status_changes(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_num_surface_status_changes = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_num_surface_status_changes
    else:
        return outputs_dict_num_surface_status_changes[pin]

class _InputSpecNumSurfaceStatusChanges(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_num_surface_status_changes(), op)
        self.time_scoping = Input(_get_input_spec_num_surface_status_changes(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_num_surface_status_changes(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_num_surface_status_changes(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_num_surface_status_changes(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_num_surface_status_changes(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_num_surface_status_changes(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_num_surface_status_changes(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_num_surface_status_changes(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_num_surface_status_changes(17), 17, op, -1) 

class _OutputSpecNumSurfaceStatusChanges(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_num_surface_status_changes(), op)
        self.fields_container = Output(_get_output_spec_num_surface_status_changes(0), 0, op) 

class _NumSurfaceStatusChanges(_Operator):
    """Operator's description:
    Internal name is "ECT_CNOS"
    Scripting name is "num_surface_status_changes"

    Description: Load the appropriate operator based on the data sources and read/compute element total number of contact status changes during substep. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_CNOS")
    >>> op_way2 = core.operators.result.num_surface_status_changes()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ECT_CNOS")
        self.inputs = _InputSpecNumSurfaceStatusChanges(self)
        self.outputs = _OutputSpecNumSurfaceStatusChanges(self)

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

def num_surface_status_changes():
    """Operator's description:
    Internal name is "ECT_CNOS"
    Scripting name is "num_surface_status_changes"

    Description: Load the appropriate operator based on the data sources and read/compute element total number of contact status changes during substep. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_CNOS")
    >>> op_way2 = core.operators.result.num_surface_status_changes()
    """
    return _NumSurfaceStatusChanges()

#internal name: ECT_FRES
#scripting name: contact_fluid_penetration_pressure
def _get_input_spec_contact_fluid_penetration_pressure(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_contact_fluid_penetration_pressure = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_contact_fluid_penetration_pressure
    else:
        return inputs_dict_contact_fluid_penetration_pressure[pin]

def _get_output_spec_contact_fluid_penetration_pressure(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_fluid_penetration_pressure = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_contact_fluid_penetration_pressure
    else:
        return outputs_dict_contact_fluid_penetration_pressure[pin]

class _InputSpecContactFluidPenetrationPressure(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_contact_fluid_penetration_pressure(), op)
        self.time_scoping = Input(_get_input_spec_contact_fluid_penetration_pressure(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_contact_fluid_penetration_pressure(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_contact_fluid_penetration_pressure(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_contact_fluid_penetration_pressure(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_contact_fluid_penetration_pressure(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_contact_fluid_penetration_pressure(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_contact_fluid_penetration_pressure(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_contact_fluid_penetration_pressure(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_contact_fluid_penetration_pressure(17), 17, op, -1) 

class _OutputSpecContactFluidPenetrationPressure(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_contact_fluid_penetration_pressure(), op)
        self.fields_container = Output(_get_output_spec_contact_fluid_penetration_pressure(0), 0, op) 

class _ContactFluidPenetrationPressure(_Operator):
    """Operator's description:
    Internal name is "ECT_FRES"
    Scripting name is "contact_fluid_penetration_pressure"

    Description: Load the appropriate operator based on the data sources and read/compute element actual applied fluid penetration pressure. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_FRES")
    >>> op_way2 = core.operators.result.contact_fluid_penetration_pressure()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ECT_FRES")
        self.inputs = _InputSpecContactFluidPenetrationPressure(self)
        self.outputs = _OutputSpecContactFluidPenetrationPressure(self)

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

def contact_fluid_penetration_pressure():
    """Operator's description:
    Internal name is "ECT_FRES"
    Scripting name is "contact_fluid_penetration_pressure"

    Description: Load the appropriate operator based on the data sources and read/compute element actual applied fluid penetration pressure. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ECT_FRES")
    >>> op_way2 = core.operators.result.contact_fluid_penetration_pressure()
    """
    return _ContactFluidPenetrationPressure()

#internal name: ENG_VOL
#scripting name: elemental_volume
def _get_input_spec_elemental_volume(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_elemental_volume = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_elemental_volume
    else:
        return inputs_dict_elemental_volume[pin]

def _get_output_spec_elemental_volume(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_volume = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_volume
    else:
        return outputs_dict_elemental_volume[pin]

class _InputSpecElementalVolume(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_volume(), op)
        self.time_scoping = Input(_get_input_spec_elemental_volume(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_elemental_volume(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_elemental_volume(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elemental_volume(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elemental_volume(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_elemental_volume(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_elemental_volume(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_elemental_volume(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_elemental_volume(17), 17, op, -1) 

class _OutputSpecElementalVolume(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_volume(), op)
        self.fields_container = Output(_get_output_spec_elemental_volume(0), 0, op) 

class _ElementalVolume(_Operator):
    """Operator's description:
    Internal name is "ENG_VOL"
    Scripting name is "elemental_volume"

    Description: Load the appropriate operator based on the data sources and read/compute element volume. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_VOL")
    >>> op_way2 = core.operators.result.elemental_volume()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENG_VOL")
        self.inputs = _InputSpecElementalVolume(self)
        self.outputs = _OutputSpecElementalVolume(self)

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

def elemental_volume():
    """Operator's description:
    Internal name is "ENG_VOL"
    Scripting name is "elemental_volume"

    Description: Load the appropriate operator based on the data sources and read/compute element volume. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_VOL")
    >>> op_way2 = core.operators.result.elemental_volume()
    """
    return _ElementalVolume()

#internal name: ENG_AHO
#scripting name: artificial_hourglass_energy
def _get_input_spec_artificial_hourglass_energy(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_artificial_hourglass_energy = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_artificial_hourglass_energy
    else:
        return inputs_dict_artificial_hourglass_energy[pin]

def _get_output_spec_artificial_hourglass_energy(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_artificial_hourglass_energy = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_artificial_hourglass_energy
    else:
        return outputs_dict_artificial_hourglass_energy[pin]

class _InputSpecArtificialHourglassEnergy(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_artificial_hourglass_energy(), op)
        self.time_scoping = Input(_get_input_spec_artificial_hourglass_energy(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_artificial_hourglass_energy(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_artificial_hourglass_energy(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_artificial_hourglass_energy(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_artificial_hourglass_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_artificial_hourglass_energy(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_artificial_hourglass_energy(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_artificial_hourglass_energy(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_artificial_hourglass_energy(17), 17, op, -1) 

class _OutputSpecArtificialHourglassEnergy(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_artificial_hourglass_energy(), op)
        self.fields_container = Output(_get_output_spec_artificial_hourglass_energy(0), 0, op) 

class _ArtificialHourglassEnergy(_Operator):
    """Operator's description:
    Internal name is "ENG_AHO"
    Scripting name is "artificial_hourglass_energy"

    Description: Load the appropriate operator based on the data sources and read/compute artificial hourglass energy. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_AHO")
    >>> op_way2 = core.operators.result.artificial_hourglass_energy()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENG_AHO")
        self.inputs = _InputSpecArtificialHourglassEnergy(self)
        self.outputs = _OutputSpecArtificialHourglassEnergy(self)

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

def artificial_hourglass_energy():
    """Operator's description:
    Internal name is "ENG_AHO"
    Scripting name is "artificial_hourglass_energy"

    Description: Load the appropriate operator based on the data sources and read/compute artificial hourglass energy. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_AHO")
    >>> op_way2 = core.operators.result.artificial_hourglass_energy()
    """
    return _ArtificialHourglassEnergy()

#internal name: ENG_KE
#scripting name: kinetic_energy
def _get_input_spec_kinetic_energy(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_kinetic_energy = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_kinetic_energy
    else:
        return inputs_dict_kinetic_energy[pin]

def _get_output_spec_kinetic_energy(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_kinetic_energy = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_kinetic_energy
    else:
        return outputs_dict_kinetic_energy[pin]

class _InputSpecKineticEnergy(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_kinetic_energy(), op)
        self.time_scoping = Input(_get_input_spec_kinetic_energy(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_kinetic_energy(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_kinetic_energy(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_kinetic_energy(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_kinetic_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_kinetic_energy(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_kinetic_energy(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_kinetic_energy(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_kinetic_energy(17), 17, op, -1) 

class _OutputSpecKineticEnergy(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_kinetic_energy(), op)
        self.fields_container = Output(_get_output_spec_kinetic_energy(0), 0, op) 

class _KineticEnergy(_Operator):
    """Operator's description:
    Internal name is "ENG_KE"
    Scripting name is "kinetic_energy"

    Description: Load the appropriate operator based on the data sources and read/compute kinetic energy. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_KE")
    >>> op_way2 = core.operators.result.kinetic_energy()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENG_KE")
        self.inputs = _InputSpecKineticEnergy(self)
        self.outputs = _OutputSpecKineticEnergy(self)

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

def kinetic_energy():
    """Operator's description:
    Internal name is "ENG_KE"
    Scripting name is "kinetic_energy"

    Description: Load the appropriate operator based on the data sources and read/compute kinetic energy. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_KE")
    >>> op_way2 = core.operators.result.kinetic_energy()
    """
    return _KineticEnergy()

#internal name: ENG_TH
#scripting name: thermal_dissipation_energy
def _get_input_spec_thermal_dissipation_energy(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_thermal_dissipation_energy = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_thermal_dissipation_energy
    else:
        return inputs_dict_thermal_dissipation_energy[pin]

def _get_output_spec_thermal_dissipation_energy(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_thermal_dissipation_energy = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_thermal_dissipation_energy
    else:
        return outputs_dict_thermal_dissipation_energy[pin]

class _InputSpecThermalDissipationEnergy(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_thermal_dissipation_energy(), op)
        self.time_scoping = Input(_get_input_spec_thermal_dissipation_energy(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_thermal_dissipation_energy(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_thermal_dissipation_energy(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_thermal_dissipation_energy(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_thermal_dissipation_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_thermal_dissipation_energy(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_thermal_dissipation_energy(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_thermal_dissipation_energy(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_thermal_dissipation_energy(17), 17, op, -1) 

class _OutputSpecThermalDissipationEnergy(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_thermal_dissipation_energy(), op)
        self.fields_container = Output(_get_output_spec_thermal_dissipation_energy(0), 0, op) 

class _ThermalDissipationEnergy(_Operator):
    """Operator's description:
    Internal name is "ENG_TH"
    Scripting name is "thermal_dissipation_energy"

    Description: Load the appropriate operator based on the data sources and read/compute thermal dissipation energy. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_TH")
    >>> op_way2 = core.operators.result.thermal_dissipation_energy()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENG_TH")
        self.inputs = _InputSpecThermalDissipationEnergy(self)
        self.outputs = _OutputSpecThermalDissipationEnergy(self)

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

def thermal_dissipation_energy():
    """Operator's description:
    Internal name is "ENG_TH"
    Scripting name is "thermal_dissipation_energy"

    Description: Load the appropriate operator based on the data sources and read/compute thermal dissipation energy. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENG_TH")
    >>> op_way2 = core.operators.result.thermal_dissipation_energy()
    """
    return _ThermalDissipationEnergy()

#internal name: F
#scripting name: nodal_force
def _get_input_spec_nodal_force(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_nodal_force = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_nodal_force
    else:
        return inputs_dict_nodal_force[pin]

def _get_output_spec_nodal_force(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_force = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_force
    else:
        return outputs_dict_nodal_force[pin]

class _InputSpecNodalForce(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_force(), op)
        self.time_scoping = Input(_get_input_spec_nodal_force(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_force(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_force(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_force(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_force(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_nodal_force(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_force(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_nodal_force(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_nodal_force(17), 17, op, -1) 

class _OutputSpecNodalForce(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_force(), op)
        self.fields_container = Output(_get_output_spec_nodal_force(0), 0, op) 

class _NodalForce(_Operator):
    """Operator's description:
    Internal name is "F"
    Scripting name is "nodal_force"

    Description: Load the appropriate operator based on the data sources and read/compute nodal forces. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("F")
    >>> op_way2 = core.operators.result.nodal_force()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("F")
        self.inputs = _InputSpecNodalForce(self)
        self.outputs = _OutputSpecNodalForce(self)

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

def nodal_force():
    """Operator's description:
    Internal name is "F"
    Scripting name is "nodal_force"

    Description: Load the appropriate operator based on the data sources and read/compute nodal forces. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("F")
    >>> op_way2 = core.operators.result.nodal_force()
    """
    return _NodalForce()

#internal name: M
#scripting name: nodal_moment
def _get_input_spec_nodal_moment(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_nodal_moment = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_nodal_moment
    else:
        return inputs_dict_nodal_moment[pin]

def _get_output_spec_nodal_moment(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_moment = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_moment
    else:
        return outputs_dict_nodal_moment[pin]

class _InputSpecNodalMoment(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_moment(), op)
        self.time_scoping = Input(_get_input_spec_nodal_moment(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_moment(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_moment(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_moment(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_moment(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_nodal_moment(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_moment(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_nodal_moment(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_nodal_moment(17), 17, op, -1) 

class _OutputSpecNodalMoment(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_moment(), op)
        self.fields_container = Output(_get_output_spec_nodal_moment(0), 0, op) 

class _NodalMoment(_Operator):
    """Operator's description:
    Internal name is "M"
    Scripting name is "nodal_moment"

    Description: Load the appropriate operator based on the data sources and read/compute nodal moment. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("M")
    >>> op_way2 = core.operators.result.nodal_moment()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("M")
        self.inputs = _InputSpecNodalMoment(self)
        self.outputs = _OutputSpecNodalMoment(self)

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

def nodal_moment():
    """Operator's description:
    Internal name is "M"
    Scripting name is "nodal_moment"

    Description: Load the appropriate operator based on the data sources and read/compute nodal moment. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("M")
    >>> op_way2 = core.operators.result.nodal_moment()
    """
    return _NodalMoment()

#internal name: TEMP
#scripting name: temperature
def _get_input_spec_temperature(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_temperature = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_temperature
    else:
        return inputs_dict_temperature[pin]

def _get_output_spec_temperature(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_temperature = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_temperature
    else:
        return outputs_dict_temperature[pin]

class _InputSpecTemperature(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_temperature(), op)
        self.time_scoping = Input(_get_input_spec_temperature(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_temperature(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_temperature(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_temperature(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_temperature(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_temperature(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_temperature(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_temperature(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_temperature(17), 17, op, -1) 

class _OutputSpecTemperature(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_temperature(), op)
        self.fields_container = Output(_get_output_spec_temperature(0), 0, op) 

class _Temperature(_Operator):
    """Operator's description:
    Internal name is "TEMP"
    Scripting name is "temperature"

    Description: Load the appropriate operator based on the data sources and read/compute temperature field. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TEMP")
    >>> op_way2 = core.operators.result.temperature()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("TEMP")
        self.inputs = _InputSpecTemperature(self)
        self.outputs = _OutputSpecTemperature(self)

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

def temperature():
    """Operator's description:
    Internal name is "TEMP"
    Scripting name is "temperature"

    Description: Load the appropriate operator based on the data sources and read/compute temperature field. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TEMP")
    >>> op_way2 = core.operators.result.temperature()
    """
    return _Temperature()

#internal name: UTOT
#scripting name: raw_displacement
def _get_input_spec_raw_displacement(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_raw_displacement = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_raw_displacement
    else:
        return inputs_dict_raw_displacement[pin]

def _get_output_spec_raw_displacement(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_raw_displacement = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_raw_displacement
    else:
        return outputs_dict_raw_displacement[pin]

class _InputSpecRawDisplacement(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_raw_displacement(), op)
        self.time_scoping = Input(_get_input_spec_raw_displacement(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_raw_displacement(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_raw_displacement(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_raw_displacement(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_raw_displacement(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_raw_displacement(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_raw_displacement(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_raw_displacement(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_raw_displacement(17), 17, op, -1) 

class _OutputSpecRawDisplacement(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_raw_displacement(), op)
        self.fields_container = Output(_get_output_spec_raw_displacement(0), 0, op) 

class _RawDisplacement(_Operator):
    """Operator's description:
    Internal name is "UTOT"
    Scripting name is "raw_displacement"

    Description: Load the appropriate operator based on the data sources and read/compute U vector from the finite element problem KU=F. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("UTOT")
    >>> op_way2 = core.operators.result.raw_displacement()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("UTOT")
        self.inputs = _InputSpecRawDisplacement(self)
        self.outputs = _OutputSpecRawDisplacement(self)

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

def raw_displacement():
    """Operator's description:
    Internal name is "UTOT"
    Scripting name is "raw_displacement"

    Description: Load the appropriate operator based on the data sources and read/compute U vector from the finite element problem KU=F. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("UTOT")
    >>> op_way2 = core.operators.result.raw_displacement()
    """
    return _RawDisplacement()

#internal name: RFTOT
#scripting name: raw_reaction_force
def _get_input_spec_raw_reaction_force(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_raw_reaction_force = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_raw_reaction_force
    else:
        return inputs_dict_raw_reaction_force[pin]

def _get_output_spec_raw_reaction_force(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_raw_reaction_force = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_raw_reaction_force
    else:
        return outputs_dict_raw_reaction_force[pin]

class _InputSpecRawReactionForce(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_raw_reaction_force(), op)
        self.time_scoping = Input(_get_input_spec_raw_reaction_force(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_raw_reaction_force(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_raw_reaction_force(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_raw_reaction_force(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_raw_reaction_force(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_raw_reaction_force(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_raw_reaction_force(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_raw_reaction_force(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_raw_reaction_force(17), 17, op, -1) 

class _OutputSpecRawReactionForce(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_raw_reaction_force(), op)
        self.fields_container = Output(_get_output_spec_raw_reaction_force(0), 0, op) 

class _RawReactionForce(_Operator):
    """Operator's description:
    Internal name is "RFTOT"
    Scripting name is "raw_reaction_force"

    Description: Load the appropriate operator based on the data sources and read/compute F vector from the finite element problem KU=F. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("RFTOT")
    >>> op_way2 = core.operators.result.raw_reaction_force()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("RFTOT")
        self.inputs = _InputSpecRawReactionForce(self)
        self.outputs = _OutputSpecRawReactionForce(self)

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

def raw_reaction_force():
    """Operator's description:
    Internal name is "RFTOT"
    Scripting name is "raw_reaction_force"

    Description: Load the appropriate operator based on the data sources and read/compute F vector from the finite element problem KU=F. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("RFTOT")
    >>> op_way2 = core.operators.result.raw_reaction_force()
    """
    return _RawReactionForce()

#internal name: VOLT
#scripting name: electric_potential
def _get_input_spec_electric_potential(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_electric_potential = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_electric_potential
    else:
        return inputs_dict_electric_potential[pin]

def _get_output_spec_electric_potential(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_electric_potential = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_electric_potential
    else:
        return outputs_dict_electric_potential[pin]

class _InputSpecElectricPotential(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_electric_potential(), op)
        self.time_scoping = Input(_get_input_spec_electric_potential(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_electric_potential(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_electric_potential(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_electric_potential(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_electric_potential(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_electric_potential(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_electric_potential(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_electric_potential(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_electric_potential(17), 17, op, -1) 

class _OutputSpecElectricPotential(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_electric_potential(), op)
        self.fields_container = Output(_get_output_spec_electric_potential(0), 0, op) 

class _ElectricPotential(_Operator):
    """Operator's description:
    Internal name is "VOLT"
    Scripting name is "electric_potential"

    Description: Load the appropriate operator based on the data sources and read/compute electric Potential. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("VOLT")
    >>> op_way2 = core.operators.result.electric_potential()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("VOLT")
        self.inputs = _InputSpecElectricPotential(self)
        self.outputs = _OutputSpecElectricPotential(self)

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

def electric_potential():
    """Operator's description:
    Internal name is "VOLT"
    Scripting name is "electric_potential"

    Description: Load the appropriate operator based on the data sources and read/compute electric Potential. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("VOLT")
    >>> op_way2 = core.operators.result.electric_potential()
    """
    return _ElectricPotential()

#internal name: thickness
#scripting name: thickness
def _get_input_spec_thickness(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """Fields container already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_thickness = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_thickness
    else:
        return inputs_dict_thickness[pin]

def _get_output_spec_thickness(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_thickness = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_thickness
    else:
        return outputs_dict_thickness[pin]

class _InputSpecThickness(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_thickness(), op)
        self.time_scoping = Input(_get_input_spec_thickness(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_thickness(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_thickness(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_thickness(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_thickness(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_thickness(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_thickness(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_thickness(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_thickness(17), 17, op, -1) 

class _OutputSpecThickness(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_thickness(), op)
        self.fields_container = Output(_get_output_spec_thickness(0), 0, op) 

class _Thickness(_Operator):
    """Operator's description:
    Internal name is "thickness"
    Scripting name is "thickness"

    Description: Load the appropriate operator based on the data sources and read/compute thickness. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("thickness")
    >>> op_way2 = core.operators.result.thickness()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("thickness")
        self.inputs = _InputSpecThickness(self)
        self.outputs = _OutputSpecThickness(self)

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

def thickness():
    """Operator's description:
    Internal name is "thickness"
    Scripting name is "thickness"

    Description: Load the appropriate operator based on the data sources and read/compute thickness. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (Fields container already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("thickness")
    >>> op_way2 = core.operators.result.thickness()
    """
    return _Thickness()

#internal name: S_eqv
#scripting name: stress_von_mises
def _get_input_spec_stress_von_mises(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order)""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """""")
    inpin17 = _PinSpecification(name = "domain_id", type_names = ["int32"], optional = True, document = """""")
    inputs_dict_stress_von_mises = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        17 : inpin17
    }
    if pin is None:
        return inputs_dict_stress_von_mises
    else:
        return inputs_dict_stress_von_mises[pin]

def _get_output_spec_stress_von_mises(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_von_mises = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_von_mises
    else:
        return outputs_dict_stress_von_mises[pin]

class _InputSpecStressVonMises(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_von_mises(), op)
        self.time_scoping = Input(_get_input_spec_stress_von_mises(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_stress_von_mises(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_stress_von_mises(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_von_mises(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_von_mises(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_stress_von_mises(5), 5, op, -1) 
        self.mesh = Input(_get_input_spec_stress_von_mises(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_stress_von_mises(9), 9, op, -1) 
        self.domain_id = Input(_get_input_spec_stress_von_mises(17), 17, op, -1) 

class _OutputSpecStressVonMises(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_von_mises(), op)
        self.fields_container = Output(_get_output_spec_stress_von_mises(0), 0, op) 

class _StressVonMises(_Operator):
    """Operator's description:
    Internal name is "S_eqv"
    Scripting name is "stress_von_mises"

    Description: Reads/computes element nodal component stresses, average it one nodes and computes its element nodal component stresses nodal / elemental Mises equivalent

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("S_eqv")
    >>> op_way2 = core.operators.result.stress_von_mises()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("S_eqv")
        self.inputs = _InputSpecStressVonMises(self)
        self.outputs = _OutputSpecStressVonMises(self)

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

def stress_von_mises():
    """Operator's description:
    Internal name is "S_eqv"
    Scripting name is "stress_von_mises"

    Description: Reads/computes element nodal component stresses, average it one nodes and computes its element nodal component stresses nodal / elemental Mises equivalent

    Input list: 
       0: time_scoping 
       1: mesh_scoping (mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order))
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: mesh 
       9: requested_location 
       17: domain_id 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("S_eqv")
    >>> op_way2 = core.operators.result.stress_von_mises()
    """
    return _StressVonMises()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "result" category
"""

#internal name: cyclic_expansion
#scripting name: cyclic_expansion
def _get_input_spec_cyclic_expansion(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field container with the base and duplicate sectors""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = False, document = """""")
    inputs_dict_cyclic_expansion = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        16 : inpin16
    }
    if pin is None:
        return inputs_dict_cyclic_expansion
    else:
        return inputs_dict_cyclic_expansion[pin]

def _get_output_spec_cyclic_expansion(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_cyclic_expansion = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cyclic_expansion
    else:
        return outputs_dict_cyclic_expansion[pin]

class _InputSpecCyclicExpansion(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cyclic_expansion(), op)
        self.time_scoping = Input(_get_input_spec_cyclic_expansion(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_cyclic_expansion(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_cyclic_expansion(2), 2, op, -1) 
        self.cyclic_support = Input(_get_input_spec_cyclic_expansion(16), 16, op, -1) 

class _OutputSpecCyclicExpansion(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cyclic_expansion(), op)
        self.fields_container = Output(_get_output_spec_cyclic_expansion(0), 0, op) 

class _CyclicExpansion(_Operator):
    """Operator's description:
    Internal name is "cyclic_expansion"
    Scripting name is "cyclic_expansion"

    Description: Expand cyclic results from a fieldsContainer for given sets, sectors and scoping (optionals).


    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (field container with the base and duplicate sectors)
       16: cyclic_support 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cyclic_expansion")
    >>> op_way2 = core.operators.result.cyclic_expansion()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cyclic_expansion")
        self.inputs = _InputSpecCyclicExpansion(self)
        self.outputs = _OutputSpecCyclicExpansion(self)

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

def cyclic_expansion():
    """Operator's description:
    Internal name is "cyclic_expansion"
    Scripting name is "cyclic_expansion"

    Description: Expand cyclic results from a fieldsContainer for given sets, sectors and scoping (optionals).


    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (field container with the base and duplicate sectors)
       16: cyclic_support 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cyclic_expansion")
    >>> op_way2 = core.operators.result.cyclic_expansion()
    """
    return _CyclicExpansion()

#internal name: ERP
#scripting name: equivalent_radiated_power
def _get_input_spec_equivalent_radiated_power(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "meshed_region", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin have to be boundary or skin mesh""")
    inpin2 = _PinSpecification(name = "int32", type_names = ["int32"], optional = True, document = """load step number, if it's specified, the ERP is computed only on the substeps of this step""")
    inputs_dict_equivalent_radiated_power = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    if pin is None:
        return inputs_dict_equivalent_radiated_power
    else:
        return inputs_dict_equivalent_radiated_power[pin]

def _get_output_spec_equivalent_radiated_power(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_equivalent_radiated_power = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_equivalent_radiated_power
    else:
        return outputs_dict_equivalent_radiated_power[pin]

class _InputSpecEquivalentRadiatedPower(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_equivalent_radiated_power(), op)
        self.fields_container = Input(_get_input_spec_equivalent_radiated_power(0), 0, op, -1) 
        self.meshed_region = Input(_get_input_spec_equivalent_radiated_power(1), 1, op, -1) 
        self.int32 = Input(_get_input_spec_equivalent_radiated_power(2), 2, op, -1) 

class _OutputSpecEquivalentRadiatedPower(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_equivalent_radiated_power(), op)
        self.field = Output(_get_output_spec_equivalent_radiated_power(0), 0, op) 

class _EquivalentRadiatedPower(_Operator):
    """Operator's description:
    Internal name is "ERP"
    Scripting name is "equivalent_radiated_power"

    Description: Compute the Equivalent Radiated Power (ERP)

    Input list: 
       0: fields_container 
       1: meshed_region (the mesh region in this pin have to be boundary or skin mesh)
       2: int32 (load step number, if it's specified, the ERP is computed only on the substeps of this step)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ERP")
    >>> op_way2 = core.operators.result.equivalent_radiated_power()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ERP")
        self.inputs = _InputSpecEquivalentRadiatedPower(self)
        self.outputs = _OutputSpecEquivalentRadiatedPower(self)

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

def equivalent_radiated_power():
    """Operator's description:
    Internal name is "ERP"
    Scripting name is "equivalent_radiated_power"

    Description: Compute the Equivalent Radiated Power (ERP)

    Input list: 
       0: fields_container 
       1: meshed_region (the mesh region in this pin have to be boundary or skin mesh)
       2: int32 (load step number, if it's specified, the ERP is computed only on the substeps of this step)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ERP")
    >>> op_way2 = core.operators.result.equivalent_radiated_power()
    """
    return _EquivalentRadiatedPower()

#internal name: torque
#scripting name: torque
def _get_input_spec_torque(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """fields_container""")
    inputs_dict_torque = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_torque
    else:
        return inputs_dict_torque[pin]

def _get_output_spec_torque(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_torque = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_torque
    else:
        return outputs_dict_torque[pin]

class _InputSpecTorque(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_torque(), op)
        self.fields_container = Input(_get_input_spec_torque(0), 0, op, -1) 

class _OutputSpecTorque(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_torque(), op)
        self.fields_container = Output(_get_output_spec_torque(0), 0, op) 

class _Torque(_Operator):
    """Operator's description:
    Internal name is "torque"
    Scripting name is "torque"

    Description: Compute torque of a force based on a 3D point.


    Input list: 
       0: fields_container (fields_container)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("torque")
    >>> op_way2 = core.operators.result.torque()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("torque")
        self.inputs = _InputSpecTorque(self)
        self.outputs = _OutputSpecTorque(self)

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

def torque():
    """Operator's description:
    Internal name is "torque"
    Scripting name is "torque"

    Description: Compute torque of a force based on a 3D point.


    Input list: 
       0: fields_container (fields_container)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("torque")
    >>> op_way2 = core.operators.result.torque()
    """
    return _Torque()

#internal name: cyclic_expansion_mesh
#scripting name: cyclic_mesh_expansion
def _get_input_spec_cyclic_mesh_expansion(pin = None):
    inpin7 = _PinSpecification(name = "sector_meshed_region", type_names = ["meshed_region"], optional = True, document = """""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = False, document = """""")
    inputs_dict_cyclic_mesh_expansion = { 
        7 : inpin7,
        16 : inpin16
    }
    if pin is None:
        return inputs_dict_cyclic_mesh_expansion
    else:
        return inputs_dict_cyclic_mesh_expansion[pin]

def _get_output_spec_cyclic_mesh_expansion(pin = None):
    outpin0 = _PinSpecification(name = "meshed_region", type_names = ["meshed_region"], document = """expanded meshed region.""")
    outpin1 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], document = """input cyclic support modified in place containing the new expanded meshed region.""")
    outputs_dict_cyclic_mesh_expansion = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_cyclic_mesh_expansion
    else:
        return outputs_dict_cyclic_mesh_expansion[pin]

class _InputSpecCyclicMeshExpansion(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cyclic_mesh_expansion(), op)
        self.sector_meshed_region = Input(_get_input_spec_cyclic_mesh_expansion(7), 7, op, -1) 
        self.cyclic_support = Input(_get_input_spec_cyclic_mesh_expansion(16), 16, op, -1) 

class _OutputSpecCyclicMeshExpansion(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cyclic_mesh_expansion(), op)
        self.meshed_region = Output(_get_output_spec_cyclic_mesh_expansion(0), 0, op) 
        self.cyclic_support = Output(_get_output_spec_cyclic_mesh_expansion(1), 1, op) 

class _CyclicMeshExpansion(_Operator):
    """Operator's description:
    Internal name is "cyclic_expansion_mesh"
    Scripting name is "cyclic_mesh_expansion"

    Description: Read the cyclic support.

    Input list: 
       7: sector_meshed_region 
       16: cyclic_support 

    Output list: 
       0: meshed_region (expanded meshed region.)
       1: cyclic_support (input cyclic support modified in place containing the new expanded meshed region.)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cyclic_expansion_mesh")
    >>> op_way2 = core.operators.result.cyclic_mesh_expansion()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cyclic_expansion_mesh")
        self.inputs = _InputSpecCyclicMeshExpansion(self)
        self.outputs = _OutputSpecCyclicMeshExpansion(self)

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

def cyclic_mesh_expansion():
    """Operator's description:
    Internal name is "cyclic_expansion_mesh"
    Scripting name is "cyclic_mesh_expansion"

    Description: Read the cyclic support.

    Input list: 
       7: sector_meshed_region 
       16: cyclic_support 

    Output list: 
       0: meshed_region (expanded meshed region.)
       1: cyclic_support (input cyclic support modified in place containing the new expanded meshed region.)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cyclic_expansion_mesh")
    >>> op_way2 = core.operators.result.cyclic_mesh_expansion()
    """
    return _CyclicMeshExpansion()

#internal name: cyclic_analytic_usum_max
#scripting name: cyclic_analytic_usum_max
def _get_input_spec_cyclic_analytic_usum_max(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field container with the base and duplicate sectors""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = False, document = """""")
    inputs_dict_cyclic_analytic_usum_max = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        16 : inpin16
    }
    if pin is None:
        return inputs_dict_cyclic_analytic_usum_max
    else:
        return inputs_dict_cyclic_analytic_usum_max[pin]

def _get_output_spec_cyclic_analytic_usum_max(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_cyclic_analytic_usum_max = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cyclic_analytic_usum_max
    else:
        return outputs_dict_cyclic_analytic_usum_max[pin]

class _InputSpecCyclicAnalyticUsumMax(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cyclic_analytic_usum_max(), op)
        self.time_scoping = Input(_get_input_spec_cyclic_analytic_usum_max(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_cyclic_analytic_usum_max(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_cyclic_analytic_usum_max(2), 2, op, -1) 
        self.cyclic_support = Input(_get_input_spec_cyclic_analytic_usum_max(16), 16, op, -1) 

class _OutputSpecCyclicAnalyticUsumMax(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cyclic_analytic_usum_max(), op)
        self.fields_container = Output(_get_output_spec_cyclic_analytic_usum_max(0), 0, op) 

class _CyclicAnalyticUsumMax(_Operator):
    """Operator's description:
    Internal name is "cyclic_analytic_usum_max"
    Scripting name is "cyclic_analytic_usum_max"

    Description: Compute the maximum of the total deformation that can be expected on 360 degrees

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (field container with the base and duplicate sectors)
       16: cyclic_support 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cyclic_analytic_usum_max")
    >>> op_way2 = core.operators.result.cyclic_analytic_usum_max()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cyclic_analytic_usum_max")
        self.inputs = _InputSpecCyclicAnalyticUsumMax(self)
        self.outputs = _OutputSpecCyclicAnalyticUsumMax(self)

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

def cyclic_analytic_usum_max():
    """Operator's description:
    Internal name is "cyclic_analytic_usum_max"
    Scripting name is "cyclic_analytic_usum_max"

    Description: Compute the maximum of the total deformation that can be expected on 360 degrees

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (field container with the base and duplicate sectors)
       16: cyclic_support 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cyclic_analytic_usum_max")
    >>> op_way2 = core.operators.result.cyclic_analytic_usum_max()
    """
    return _CyclicAnalyticUsumMax()

#internal name: cyclic_analytic_stress_eqv_max
#scripting name: cyclic_analytic_seqv_max
def _get_input_spec_cyclic_analytic_seqv_max(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field container with the base and duplicate sectors""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = False, document = """""")
    inputs_dict_cyclic_analytic_seqv_max = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        16 : inpin16
    }
    if pin is None:
        return inputs_dict_cyclic_analytic_seqv_max
    else:
        return inputs_dict_cyclic_analytic_seqv_max[pin]

def _get_output_spec_cyclic_analytic_seqv_max(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_cyclic_analytic_seqv_max = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cyclic_analytic_seqv_max
    else:
        return outputs_dict_cyclic_analytic_seqv_max[pin]

class _InputSpecCyclicAnalyticSeqvMax(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cyclic_analytic_seqv_max(), op)
        self.time_scoping = Input(_get_input_spec_cyclic_analytic_seqv_max(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_cyclic_analytic_seqv_max(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_cyclic_analytic_seqv_max(2), 2, op, -1) 
        self.cyclic_support = Input(_get_input_spec_cyclic_analytic_seqv_max(16), 16, op, -1) 

class _OutputSpecCyclicAnalyticSeqvMax(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cyclic_analytic_seqv_max(), op)
        self.fields_container = Output(_get_output_spec_cyclic_analytic_seqv_max(0), 0, op) 

class _CyclicAnalyticSeqvMax(_Operator):
    """Operator's description:
    Internal name is "cyclic_analytic_stress_eqv_max"
    Scripting name is "cyclic_analytic_seqv_max"

    Description: Compute the maximum of the Von Mises equivalent stress that can be expected on 360 degrees

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (field container with the base and duplicate sectors)
       16: cyclic_support 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cyclic_analytic_stress_eqv_max")
    >>> op_way2 = core.operators.result.cyclic_analytic_seqv_max()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cyclic_analytic_stress_eqv_max")
        self.inputs = _InputSpecCyclicAnalyticSeqvMax(self)
        self.outputs = _OutputSpecCyclicAnalyticSeqvMax(self)

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

def cyclic_analytic_seqv_max():
    """Operator's description:
    Internal name is "cyclic_analytic_stress_eqv_max"
    Scripting name is "cyclic_analytic_seqv_max"

    Description: Compute the maximum of the Von Mises equivalent stress that can be expected on 360 degrees

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (field container with the base and duplicate sectors)
       16: cyclic_support 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cyclic_analytic_stress_eqv_max")
    >>> op_way2 = core.operators.result.cyclic_analytic_seqv_max()
    """
    return _CyclicAnalyticSeqvMax()

#internal name: recombine_harmonic_indeces_cyclic
#scripting name: recombine_harmonic_indeces_cyclic
def _get_input_spec_recombine_harmonic_indeces_cyclic(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_recombine_harmonic_indeces_cyclic = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_recombine_harmonic_indeces_cyclic
    else:
        return inputs_dict_recombine_harmonic_indeces_cyclic[pin]

def _get_output_spec_recombine_harmonic_indeces_cyclic(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_recombine_harmonic_indeces_cyclic = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_recombine_harmonic_indeces_cyclic
    else:
        return outputs_dict_recombine_harmonic_indeces_cyclic[pin]

class _InputSpecRecombineHarmonicIndecesCyclic(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_recombine_harmonic_indeces_cyclic(), op)
        self.fields_container = Input(_get_input_spec_recombine_harmonic_indeces_cyclic(0), 0, op, -1) 

class _OutputSpecRecombineHarmonicIndecesCyclic(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_recombine_harmonic_indeces_cyclic(), op)
        self.fields_container = Output(_get_output_spec_recombine_harmonic_indeces_cyclic(0), 0, op) 

class _RecombineHarmonicIndecesCyclic(_Operator):
    """Operator's description:
    Internal name is "recombine_harmonic_indeces_cyclic"
    Scripting name is "recombine_harmonic_indeces_cyclic"

    Description: Add the fields corresponding to different load steps with the same frequencies to compute the response.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("recombine_harmonic_indeces_cyclic")
    >>> op_way2 = core.operators.result.recombine_harmonic_indeces_cyclic()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("recombine_harmonic_indeces_cyclic")
        self.inputs = _InputSpecRecombineHarmonicIndecesCyclic(self)
        self.outputs = _OutputSpecRecombineHarmonicIndecesCyclic(self)

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

def recombine_harmonic_indeces_cyclic():
    """Operator's description:
    Internal name is "recombine_harmonic_indeces_cyclic"
    Scripting name is "recombine_harmonic_indeces_cyclic"

    Description: Add the fields corresponding to different load steps with the same frequencies to compute the response.

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("recombine_harmonic_indeces_cyclic")
    >>> op_way2 = core.operators.result.recombine_harmonic_indeces_cyclic()
    """
    return _RecombineHarmonicIndecesCyclic()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from mapdlOperatorsCore.dll plugin, from "result" category
"""

#internal name: mapdl::rst::NPEL
#scripting name: nodal_averaged_elastic_strains
def _get_input_spec_nodal_averaged_elastic_strains(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nodal_averaged_elastic_strains = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_nodal_averaged_elastic_strains
    else:
        return inputs_dict_nodal_averaged_elastic_strains[pin]

def _get_output_spec_nodal_averaged_elastic_strains(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_elastic_strains = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_averaged_elastic_strains
    else:
        return outputs_dict_nodal_averaged_elastic_strains[pin]

class _InputSpecNodalAveragedElasticStrains(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_averaged_elastic_strains(), op)
        self.time_scoping = Input(_get_input_spec_nodal_averaged_elastic_strains(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_averaged_elastic_strains(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_averaged_elastic_strains(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_averaged_elastic_strains(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_averaged_elastic_strains(4), 4, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_averaged_elastic_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedElasticStrains(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_averaged_elastic_strains(), op)
        self.fields_container = Output(_get_output_spec_nodal_averaged_elastic_strains(0), 0, op) 

class _NodalAveragedElasticStrains(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::NPEL"
    Scripting name is "nodal_averaged_elastic_strains"

    Description: Read nodal averaged elastic strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NPEL")
    >>> op_way2 = core.operators.result.nodal_averaged_elastic_strains()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::NPEL")
        self.inputs = _InputSpecNodalAveragedElasticStrains(self)
        self.outputs = _OutputSpecNodalAveragedElasticStrains(self)

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

def nodal_averaged_elastic_strains():
    """Operator's description:
    Internal name is "mapdl::rst::NPEL"
    Scripting name is "nodal_averaged_elastic_strains"

    Description: Read nodal averaged elastic strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NPEL")
    >>> op_way2 = core.operators.result.nodal_averaged_elastic_strains()
    """
    return _NodalAveragedElasticStrains()

#internal name: RigidBodyAddition
#scripting name: add_rigid_body_motion
def _get_input_spec_add_rigid_body_motion(pin = None):
    inpin0 = _PinSpecification(name = "displacement_field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "translation_field", type_names = ["field"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "rotation_field", type_names = ["field"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "center_field", type_names = ["field"], optional = False, document = """""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """default is the mesh in the support""")
    inputs_dict_add_rigid_body_motion = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_add_rigid_body_motion
    else:
        return inputs_dict_add_rigid_body_motion[pin]

def _get_output_spec_add_rigid_body_motion(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_add_rigid_body_motion = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_add_rigid_body_motion
    else:
        return outputs_dict_add_rigid_body_motion[pin]

class _InputSpecAddRigidBodyMotion(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_add_rigid_body_motion(), op)
        self.displacement_field = Input(_get_input_spec_add_rigid_body_motion(0), 0, op, -1) 
        self.translation_field = Input(_get_input_spec_add_rigid_body_motion(1), 1, op, -1) 
        self.rotation_field = Input(_get_input_spec_add_rigid_body_motion(2), 2, op, -1) 
        self.center_field = Input(_get_input_spec_add_rigid_body_motion(3), 3, op, -1) 
        self.mesh = Input(_get_input_spec_add_rigid_body_motion(7), 7, op, -1) 

class _OutputSpecAddRigidBodyMotion(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_add_rigid_body_motion(), op)
        self.field = Output(_get_output_spec_add_rigid_body_motion(0), 0, op) 

class _AddRigidBodyMotion(_Operator):
    """Operator's description:
    Internal name is "RigidBodyAddition"
    Scripting name is "add_rigid_body_motion"

    Description: Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem

    Input list: 
       0: displacement_field 
       1: translation_field 
       2: rotation_field 
       3: center_field 
       7: mesh (default is the mesh in the support)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("RigidBodyAddition")
    >>> op_way2 = core.operators.result.add_rigid_body_motion()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("RigidBodyAddition")
        self.inputs = _InputSpecAddRigidBodyMotion(self)
        self.outputs = _OutputSpecAddRigidBodyMotion(self)

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

def add_rigid_body_motion():
    """Operator's description:
    Internal name is "RigidBodyAddition"
    Scripting name is "add_rigid_body_motion"

    Description: Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem

    Input list: 
       0: displacement_field 
       1: translation_field 
       2: rotation_field 
       3: center_field 
       7: mesh (default is the mesh in the support)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("RigidBodyAddition")
    >>> op_way2 = core.operators.result.add_rigid_body_motion()
    """
    return _AddRigidBodyMotion()

#internal name: mapdl::rst::NPEL_EQV
#scripting name: nodal_averaged_equivalent_elastic_strain
def _get_input_spec_nodal_averaged_equivalent_elastic_strain(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nodal_averaged_equivalent_elastic_strain = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_nodal_averaged_equivalent_elastic_strain
    else:
        return inputs_dict_nodal_averaged_equivalent_elastic_strain[pin]

def _get_output_spec_nodal_averaged_equivalent_elastic_strain(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_equivalent_elastic_strain = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_averaged_equivalent_elastic_strain
    else:
        return outputs_dict_nodal_averaged_equivalent_elastic_strain[pin]

class _InputSpecNodalAveragedEquivalentElasticStrain(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_averaged_equivalent_elastic_strain(), op)
        self.time_scoping = Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(4), 4, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(7), 7, op, -1) 

class _OutputSpecNodalAveragedEquivalentElasticStrain(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_averaged_equivalent_elastic_strain(), op)
        self.fields_container = Output(_get_output_spec_nodal_averaged_equivalent_elastic_strain(0), 0, op) 

class _NodalAveragedEquivalentElasticStrain(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::NPEL_EQV"
    Scripting name is "nodal_averaged_equivalent_elastic_strain"

    Description: Read nodal averaged equivalent elastic strain as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NPEL_EQV")
    >>> op_way2 = core.operators.result.nodal_averaged_equivalent_elastic_strain()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::NPEL_EQV")
        self.inputs = _InputSpecNodalAveragedEquivalentElasticStrain(self)
        self.outputs = _OutputSpecNodalAveragedEquivalentElasticStrain(self)

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

def nodal_averaged_equivalent_elastic_strain():
    """Operator's description:
    Internal name is "mapdl::rst::NPEL_EQV"
    Scripting name is "nodal_averaged_equivalent_elastic_strain"

    Description: Read nodal averaged equivalent elastic strain as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NPEL_EQV")
    >>> op_way2 = core.operators.result.nodal_averaged_equivalent_elastic_strain()
    """
    return _NodalAveragedEquivalentElasticStrain()

from . import mapdl #mapdl.run

#internal name: mapdl::rst::V_cyclic
#scripting name: cyclic_expanded_velocity
def _get_input_spec_cyclic_expanded_velocity(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "sector_mesh", type_names = ["meshed_region"], optional = True, document = """mesh of the base sector (can be a skin).""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """location needed in output""")
    inpin14 = _PinSpecification(name = "read_cyclic", type_names = ["int32"], optional = True, document = """if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1)""")
    inpin15 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], optional = True, document = """mesh expanded.""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = True, document = """""")
    inpin18 = _PinSpecification(name = "sectors_to_expand", type_names = ["scoping","scopings_container"], optional = True, document = """sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.""")
    inpin19 = _PinSpecification(name = "phi", type_names = ["double"], optional = True, document = """angle phi (default value 0.0)""")
    inpin20 = _PinSpecification(name = "filter_degenerated_elements", type_names = ["bool"], optional = True, document = """if it's set to true, results are filtered to handle degenerated elements (default is true)""")
    inputs_dict_cyclic_expanded_velocity = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        14 : inpin14,
        15 : inpin15,
        16 : inpin16,
        18 : inpin18,
        19 : inpin19,
        20 : inpin20
    }
    if pin is None:
        return inputs_dict_cyclic_expanded_velocity
    else:
        return inputs_dict_cyclic_expanded_velocity[pin]

def _get_output_spec_cyclic_expanded_velocity(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outpin1 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], document = """""")
    outputs_dict_cyclic_expanded_velocity = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_cyclic_expanded_velocity
    else:
        return outputs_dict_cyclic_expanded_velocity[pin]

class _InputSpecCyclicExpandedVelocity(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cyclic_expanded_velocity(), op)
        self.time_scoping = Input(_get_input_spec_cyclic_expanded_velocity(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_cyclic_expanded_velocity(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_cyclic_expanded_velocity(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_cyclic_expanded_velocity(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_cyclic_expanded_velocity(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_cyclic_expanded_velocity(5), 5, op, -1) 
        self.sector_mesh = Input(_get_input_spec_cyclic_expanded_velocity(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_cyclic_expanded_velocity(9), 9, op, -1) 
        self.read_cyclic = Input(_get_input_spec_cyclic_expanded_velocity(14), 14, op, -1) 
        self.expanded_meshed_region = Input(_get_input_spec_cyclic_expanded_velocity(15), 15, op, -1) 
        self.cyclic_support = Input(_get_input_spec_cyclic_expanded_velocity(16), 16, op, -1) 
        self.sectors_to_expand = Input(_get_input_spec_cyclic_expanded_velocity(18), 18, op, -1) 
        self.phi = Input(_get_input_spec_cyclic_expanded_velocity(19), 19, op, -1) 
        self.filter_degenerated_elements = Input(_get_input_spec_cyclic_expanded_velocity(20), 20, op, -1) 

class _OutputSpecCyclicExpandedVelocity(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cyclic_expanded_velocity(), op)
        self.fields_container = Output(_get_output_spec_cyclic_expanded_velocity(0), 0, op) 
        self.expanded_meshed_region = Output(_get_output_spec_cyclic_expanded_velocity(1), 1, op) 

class _CyclicExpandedVelocity(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::V_cyclic"
    Scripting name is "cyclic_expanded_velocity"

    Description: Read velocity from an rst file and expand it with cyclic symmetry.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (angle phi (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: fields_container (FieldsContainer filled in)
       1: expanded_meshed_region 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::V_cyclic")
    >>> op_way2 = core.operators.result.cyclic_expanded_velocity()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::V_cyclic")
        self.inputs = _InputSpecCyclicExpandedVelocity(self)
        self.outputs = _OutputSpecCyclicExpandedVelocity(self)

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

def cyclic_expanded_velocity():
    """Operator's description:
    Internal name is "mapdl::rst::V_cyclic"
    Scripting name is "cyclic_expanded_velocity"

    Description: Read velocity from an rst file and expand it with cyclic symmetry.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (angle phi (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: fields_container (FieldsContainer filled in)
       1: expanded_meshed_region 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::V_cyclic")
    >>> op_way2 = core.operators.result.cyclic_expanded_velocity()
    """
    return _CyclicExpandedVelocity()

#internal name: mapdl::rst::EPEL_cyclic
#scripting name: cyclic_expanded_el_strain
def _get_input_spec_cyclic_expanded_el_strain(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "sector_mesh", type_names = ["meshed_region"], optional = True, document = """mesh of the base sector (can be a skin).""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """location needed in output""")
    inpin14 = _PinSpecification(name = "read_cyclic", type_names = ["int32"], optional = True, document = """if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1)""")
    inpin15 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], optional = True, document = """mesh expanded.""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = True, document = """""")
    inpin18 = _PinSpecification(name = "sectors_to_expand", type_names = ["scoping","scopings_container"], optional = True, document = """sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.""")
    inpin19 = _PinSpecification(name = "phi", type_names = ["double"], optional = True, document = """phi angle (default value 0.0)""")
    inpin20 = _PinSpecification(name = "filter_degenerated_elements", type_names = ["bool"], optional = True, document = """if it's set to true, results are filtered to handle degenerated elements (default is true)""")
    inputs_dict_cyclic_expanded_el_strain = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        14 : inpin14,
        15 : inpin15,
        16 : inpin16,
        18 : inpin18,
        19 : inpin19,
        20 : inpin20
    }
    if pin is None:
        return inputs_dict_cyclic_expanded_el_strain
    else:
        return inputs_dict_cyclic_expanded_el_strain[pin]

def _get_output_spec_cyclic_expanded_el_strain(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outpin1 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], document = """""")
    outputs_dict_cyclic_expanded_el_strain = { 
        0 : outpin0,
        1 : outpin1
    }
    if pin is None:
        return outputs_dict_cyclic_expanded_el_strain
    else:
        return outputs_dict_cyclic_expanded_el_strain[pin]

class _InputSpecCyclicExpandedElStrain(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cyclic_expanded_el_strain(), op)
        self.time_scoping = Input(_get_input_spec_cyclic_expanded_el_strain(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_cyclic_expanded_el_strain(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_cyclic_expanded_el_strain(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_cyclic_expanded_el_strain(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_cyclic_expanded_el_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_cyclic_expanded_el_strain(5), 5, op, -1) 
        self.sector_mesh = Input(_get_input_spec_cyclic_expanded_el_strain(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_cyclic_expanded_el_strain(9), 9, op, -1) 
        self.read_cyclic = Input(_get_input_spec_cyclic_expanded_el_strain(14), 14, op, -1) 
        self.expanded_meshed_region = Input(_get_input_spec_cyclic_expanded_el_strain(15), 15, op, -1) 
        self.cyclic_support = Input(_get_input_spec_cyclic_expanded_el_strain(16), 16, op, -1) 
        self.sectors_to_expand = Input(_get_input_spec_cyclic_expanded_el_strain(18), 18, op, -1) 
        self.phi = Input(_get_input_spec_cyclic_expanded_el_strain(19), 19, op, -1) 
        self.filter_degenerated_elements = Input(_get_input_spec_cyclic_expanded_el_strain(20), 20, op, -1) 

class _OutputSpecCyclicExpandedElStrain(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cyclic_expanded_el_strain(), op)
        self.fields_container = Output(_get_output_spec_cyclic_expanded_el_strain(0), 0, op) 
        self.expanded_meshed_region = Output(_get_output_spec_cyclic_expanded_el_strain(1), 1, op) 

class _CyclicExpandedElStrain(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::EPEL_cyclic"
    Scripting name is "cyclic_expanded_el_strain"

    Description: Read mapdl::rst::EPEL from an rst file and expand it with cyclic symmetry.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (phi angle (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: fields_container (FieldsContainer filled in)
       1: expanded_meshed_region 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::EPEL_cyclic")
    >>> op_way2 = core.operators.result.cyclic_expanded_el_strain()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::EPEL_cyclic")
        self.inputs = _InputSpecCyclicExpandedElStrain(self)
        self.outputs = _OutputSpecCyclicExpandedElStrain(self)

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

def cyclic_expanded_el_strain():
    """Operator's description:
    Internal name is "mapdl::rst::EPEL_cyclic"
    Scripting name is "cyclic_expanded_el_strain"

    Description: Read mapdl::rst::EPEL from an rst file and expand it with cyclic symmetry.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (phi angle (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: fields_container (FieldsContainer filled in)
       1: expanded_meshed_region 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::EPEL_cyclic")
    >>> op_way2 = core.operators.result.cyclic_expanded_el_strain()
    """
    return _CyclicExpandedElStrain()

#internal name: mapdl::rst::NTH_SWL
#scripting name: nodal_averaged_thermal_swelling_strains
def _get_input_spec_nodal_averaged_thermal_swelling_strains(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nodal_averaged_thermal_swelling_strains = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_nodal_averaged_thermal_swelling_strains
    else:
        return inputs_dict_nodal_averaged_thermal_swelling_strains[pin]

def _get_output_spec_nodal_averaged_thermal_swelling_strains(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_thermal_swelling_strains = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_averaged_thermal_swelling_strains
    else:
        return outputs_dict_nodal_averaged_thermal_swelling_strains[pin]

class _InputSpecNodalAveragedThermalSwellingStrains(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_averaged_thermal_swelling_strains(), op)
        self.time_scoping = Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(4), 4, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedThermalSwellingStrains(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_averaged_thermal_swelling_strains(), op)
        self.fields_container = Output(_get_output_spec_nodal_averaged_thermal_swelling_strains(0), 0, op) 

class _NodalAveragedThermalSwellingStrains(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::NTH_SWL"
    Scripting name is "nodal_averaged_thermal_swelling_strains"

    Description: Read nodal averaged thermal swelling strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NTH_SWL")
    >>> op_way2 = core.operators.result.nodal_averaged_thermal_swelling_strains()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::NTH_SWL")
        self.inputs = _InputSpecNodalAveragedThermalSwellingStrains(self)
        self.outputs = _OutputSpecNodalAveragedThermalSwellingStrains(self)

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

def nodal_averaged_thermal_swelling_strains():
    """Operator's description:
    Internal name is "mapdl::rst::NTH_SWL"
    Scripting name is "nodal_averaged_thermal_swelling_strains"

    Description: Read nodal averaged thermal swelling strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NTH_SWL")
    >>> op_way2 = core.operators.result.nodal_averaged_thermal_swelling_strains()
    """
    return _NodalAveragedThermalSwellingStrains()

#internal name: mapdl::rst::NS
#scripting name: nodal_averaged_stresses
def _get_input_spec_nodal_averaged_stresses(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nodal_averaged_stresses = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_nodal_averaged_stresses
    else:
        return inputs_dict_nodal_averaged_stresses[pin]

def _get_output_spec_nodal_averaged_stresses(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_stresses = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_averaged_stresses
    else:
        return outputs_dict_nodal_averaged_stresses[pin]

class _InputSpecNodalAveragedStresses(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_averaged_stresses(), op)
        self.time_scoping = Input(_get_input_spec_nodal_averaged_stresses(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_averaged_stresses(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_averaged_stresses(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_averaged_stresses(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_averaged_stresses(4), 4, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_averaged_stresses(7), 7, op, -1) 

class _OutputSpecNodalAveragedStresses(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_averaged_stresses(), op)
        self.fields_container = Output(_get_output_spec_nodal_averaged_stresses(0), 0, op) 

class _NodalAveragedStresses(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::NS"
    Scripting name is "nodal_averaged_stresses"

    Description: Read nodal averaged stresses as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NS")
    >>> op_way2 = core.operators.result.nodal_averaged_stresses()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::NS")
        self.inputs = _InputSpecNodalAveragedStresses(self)
        self.outputs = _OutputSpecNodalAveragedStresses(self)

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

def nodal_averaged_stresses():
    """Operator's description:
    Internal name is "mapdl::rst::NS"
    Scripting name is "nodal_averaged_stresses"

    Description: Read nodal averaged stresses as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NS")
    >>> op_way2 = core.operators.result.nodal_averaged_stresses()
    """
    return _NodalAveragedStresses()

#internal name: mapdl::rst::NTH
#scripting name: nodal_averaged_thermal_strains
def _get_input_spec_nodal_averaged_thermal_strains(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nodal_averaged_thermal_strains = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_nodal_averaged_thermal_strains
    else:
        return inputs_dict_nodal_averaged_thermal_strains[pin]

def _get_output_spec_nodal_averaged_thermal_strains(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_thermal_strains = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_averaged_thermal_strains
    else:
        return outputs_dict_nodal_averaged_thermal_strains[pin]

class _InputSpecNodalAveragedThermalStrains(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_averaged_thermal_strains(), op)
        self.time_scoping = Input(_get_input_spec_nodal_averaged_thermal_strains(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_averaged_thermal_strains(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_averaged_thermal_strains(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_averaged_thermal_strains(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_averaged_thermal_strains(4), 4, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_averaged_thermal_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedThermalStrains(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_averaged_thermal_strains(), op)
        self.fields_container = Output(_get_output_spec_nodal_averaged_thermal_strains(0), 0, op) 

class _NodalAveragedThermalStrains(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::NTH"
    Scripting name is "nodal_averaged_thermal_strains"

    Description: Read nodal averaged thermal strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NTH")
    >>> op_way2 = core.operators.result.nodal_averaged_thermal_strains()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::NTH")
        self.inputs = _InputSpecNodalAveragedThermalStrains(self)
        self.outputs = _OutputSpecNodalAveragedThermalStrains(self)

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

def nodal_averaged_thermal_strains():
    """Operator's description:
    Internal name is "mapdl::rst::NTH"
    Scripting name is "nodal_averaged_thermal_strains"

    Description: Read nodal averaged thermal strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NTH")
    >>> op_way2 = core.operators.result.nodal_averaged_thermal_strains()
    """
    return _NodalAveragedThermalStrains()

#internal name: mapdl::rst::NPPL
#scripting name: nodal_averaged_plastic_strains
def _get_input_spec_nodal_averaged_plastic_strains(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nodal_averaged_plastic_strains = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_nodal_averaged_plastic_strains
    else:
        return inputs_dict_nodal_averaged_plastic_strains[pin]

def _get_output_spec_nodal_averaged_plastic_strains(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_plastic_strains = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_averaged_plastic_strains
    else:
        return outputs_dict_nodal_averaged_plastic_strains[pin]

class _InputSpecNodalAveragedPlasticStrains(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_averaged_plastic_strains(), op)
        self.time_scoping = Input(_get_input_spec_nodal_averaged_plastic_strains(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_averaged_plastic_strains(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_averaged_plastic_strains(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_averaged_plastic_strains(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_averaged_plastic_strains(4), 4, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_averaged_plastic_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedPlasticStrains(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_averaged_plastic_strains(), op)
        self.fields_container = Output(_get_output_spec_nodal_averaged_plastic_strains(0), 0, op) 

class _NodalAveragedPlasticStrains(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::NPPL"
    Scripting name is "nodal_averaged_plastic_strains"

    Description: Read nodal averaged plastic strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NPPL")
    >>> op_way2 = core.operators.result.nodal_averaged_plastic_strains()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::NPPL")
        self.inputs = _InputSpecNodalAveragedPlasticStrains(self)
        self.outputs = _OutputSpecNodalAveragedPlasticStrains(self)

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

def nodal_averaged_plastic_strains():
    """Operator's description:
    Internal name is "mapdl::rst::NPPL"
    Scripting name is "nodal_averaged_plastic_strains"

    Description: Read nodal averaged plastic strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NPPL")
    >>> op_way2 = core.operators.result.nodal_averaged_plastic_strains()
    """
    return _NodalAveragedPlasticStrains()

#internal name: mapdl::rst::NCR
#scripting name: nodal_averaged_creep_strains
def _get_input_spec_nodal_averaged_creep_strains(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nodal_averaged_creep_strains = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_nodal_averaged_creep_strains
    else:
        return inputs_dict_nodal_averaged_creep_strains[pin]

def _get_output_spec_nodal_averaged_creep_strains(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_creep_strains = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_averaged_creep_strains
    else:
        return outputs_dict_nodal_averaged_creep_strains[pin]

class _InputSpecNodalAveragedCreepStrains(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_averaged_creep_strains(), op)
        self.time_scoping = Input(_get_input_spec_nodal_averaged_creep_strains(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_averaged_creep_strains(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_averaged_creep_strains(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_averaged_creep_strains(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_averaged_creep_strains(4), 4, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_averaged_creep_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedCreepStrains(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_averaged_creep_strains(), op)
        self.fields_container = Output(_get_output_spec_nodal_averaged_creep_strains(0), 0, op) 

class _NodalAveragedCreepStrains(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::NCR"
    Scripting name is "nodal_averaged_creep_strains"

    Description: Read nodal averaged creep strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NCR")
    >>> op_way2 = core.operators.result.nodal_averaged_creep_strains()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::NCR")
        self.inputs = _InputSpecNodalAveragedCreepStrains(self)
        self.outputs = _OutputSpecNodalAveragedCreepStrains(self)

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

def nodal_averaged_creep_strains():
    """Operator's description:
    Internal name is "mapdl::rst::NCR"
    Scripting name is "nodal_averaged_creep_strains"

    Description: Read nodal averaged creep strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NCR")
    >>> op_way2 = core.operators.result.nodal_averaged_creep_strains()
    """
    return _NodalAveragedCreepStrains()

#internal name: mapdl::rst::NTH_EQV
#scripting name: nodal_averaged_equivalent_thermal_strains
def _get_input_spec_nodal_averaged_equivalent_thermal_strains(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nodal_averaged_equivalent_thermal_strains = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_nodal_averaged_equivalent_thermal_strains
    else:
        return inputs_dict_nodal_averaged_equivalent_thermal_strains[pin]

def _get_output_spec_nodal_averaged_equivalent_thermal_strains(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_equivalent_thermal_strains = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_averaged_equivalent_thermal_strains
    else:
        return outputs_dict_nodal_averaged_equivalent_thermal_strains[pin]

class _InputSpecNodalAveragedEquivalentThermalStrains(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_averaged_equivalent_thermal_strains(), op)
        self.time_scoping = Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(4), 4, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedEquivalentThermalStrains(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_averaged_equivalent_thermal_strains(), op)
        self.fields_container = Output(_get_output_spec_nodal_averaged_equivalent_thermal_strains(0), 0, op) 

class _NodalAveragedEquivalentThermalStrains(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::NTH_EQV"
    Scripting name is "nodal_averaged_equivalent_thermal_strains"

    Description: Read nodal averaged equivalent thermal strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NTH_EQV")
    >>> op_way2 = core.operators.result.nodal_averaged_equivalent_thermal_strains()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::NTH_EQV")
        self.inputs = _InputSpecNodalAveragedEquivalentThermalStrains(self)
        self.outputs = _OutputSpecNodalAveragedEquivalentThermalStrains(self)

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

def nodal_averaged_equivalent_thermal_strains():
    """Operator's description:
    Internal name is "mapdl::rst::NTH_EQV"
    Scripting name is "nodal_averaged_equivalent_thermal_strains"

    Description: Read nodal averaged equivalent thermal strains as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NTH_EQV")
    >>> op_way2 = core.operators.result.nodal_averaged_equivalent_thermal_strains()
    """
    return _NodalAveragedEquivalentThermalStrains()

#internal name: mapdl::rst::NPPL_EQV
#scripting name: nodal_averaged_equivalent_plastic_strain
def _get_input_spec_nodal_averaged_equivalent_plastic_strain(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nodal_averaged_equivalent_plastic_strain = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_nodal_averaged_equivalent_plastic_strain
    else:
        return inputs_dict_nodal_averaged_equivalent_plastic_strain[pin]

def _get_output_spec_nodal_averaged_equivalent_plastic_strain(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_equivalent_plastic_strain = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_averaged_equivalent_plastic_strain
    else:
        return outputs_dict_nodal_averaged_equivalent_plastic_strain[pin]

class _InputSpecNodalAveragedEquivalentPlasticStrain(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_averaged_equivalent_plastic_strain(), op)
        self.time_scoping = Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(4), 4, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(7), 7, op, -1) 

class _OutputSpecNodalAveragedEquivalentPlasticStrain(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_averaged_equivalent_plastic_strain(), op)
        self.fields_container = Output(_get_output_spec_nodal_averaged_equivalent_plastic_strain(0), 0, op) 

class _NodalAveragedEquivalentPlasticStrain(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::NPPL_EQV"
    Scripting name is "nodal_averaged_equivalent_plastic_strain"

    Description: Read nodal averaged equivalent plastic strain as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NPPL_EQV")
    >>> op_way2 = core.operators.result.nodal_averaged_equivalent_plastic_strain()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::NPPL_EQV")
        self.inputs = _InputSpecNodalAveragedEquivalentPlasticStrain(self)
        self.outputs = _OutputSpecNodalAveragedEquivalentPlasticStrain(self)

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

def nodal_averaged_equivalent_plastic_strain():
    """Operator's description:
    Internal name is "mapdl::rst::NPPL_EQV"
    Scripting name is "nodal_averaged_equivalent_plastic_strain"

    Description: Read nodal averaged equivalent plastic strain as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NPPL_EQV")
    >>> op_way2 = core.operators.result.nodal_averaged_equivalent_plastic_strain()
    """
    return _NodalAveragedEquivalentPlasticStrain()

#internal name: mapdl::rst::NCR_EQV
#scripting name: nodal_averaged_equivalent_creep_strain
def _get_input_spec_nodal_averaged_equivalent_creep_strain(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nodal_averaged_equivalent_creep_strain = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_nodal_averaged_equivalent_creep_strain
    else:
        return inputs_dict_nodal_averaged_equivalent_creep_strain[pin]

def _get_output_spec_nodal_averaged_equivalent_creep_strain(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_equivalent_creep_strain = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_averaged_equivalent_creep_strain
    else:
        return outputs_dict_nodal_averaged_equivalent_creep_strain[pin]

class _InputSpecNodalAveragedEquivalentCreepStrain(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_averaged_equivalent_creep_strain(), op)
        self.time_scoping = Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(4), 4, op, -1) 
        self.mesh = Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(7), 7, op, -1) 

class _OutputSpecNodalAveragedEquivalentCreepStrain(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_averaged_equivalent_creep_strain(), op)
        self.fields_container = Output(_get_output_spec_nodal_averaged_equivalent_creep_strain(0), 0, op) 

class _NodalAveragedEquivalentCreepStrain(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::NCR_EQV"
    Scripting name is "nodal_averaged_equivalent_creep_strain"

    Description: Read nodal averaged equivalent creep strain as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NCR_EQV")
    >>> op_way2 = core.operators.result.nodal_averaged_equivalent_creep_strain()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::NCR_EQV")
        self.inputs = _InputSpecNodalAveragedEquivalentCreepStrain(self)
        self.outputs = _OutputSpecNodalAveragedEquivalentCreepStrain(self)

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

def nodal_averaged_equivalent_creep_strain():
    """Operator's description:
    Internal name is "mapdl::rst::NCR_EQV"
    Scripting name is "nodal_averaged_equivalent_creep_strain"

    Description: Read nodal averaged equivalent creep strain as averaged nodal result from rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: mesh 

    Output list: 
       0: fields_container (FieldsContainer filled in)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::NCR_EQV")
    >>> op_way2 = core.operators.result.nodal_averaged_equivalent_creep_strain()
    """
    return _NodalAveragedEquivalentCreepStrain()

#internal name: mapdl::rst::coords_and_euler_nodes
#scripting name: euler_nodes
def _get_input_spec_euler_nodes(pin = None):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inpin6 = _PinSpecification(name = "coord_and_euler", type_names = ["bool"], optional = False, document = """if true, then the field has ncomp=6 with 3 oords and 3 euler angles, else there is only the euler angles (default is true)""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_euler_nodes = { 
        3 : inpin3,
        4 : inpin4,
        6 : inpin6,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_euler_nodes
    else:
        return inputs_dict_euler_nodes[pin]

def _get_output_spec_euler_nodes(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_euler_nodes = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_euler_nodes
    else:
        return outputs_dict_euler_nodes[pin]

class _InputSpecEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_euler_nodes(), op)
        self.streams_container = Input(_get_input_spec_euler_nodes(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_euler_nodes(4), 4, op, -1) 
        self.coord_and_euler = Input(_get_input_spec_euler_nodes(6), 6, op, -1) 
        self.mesh = Input(_get_input_spec_euler_nodes(7), 7, op, -1) 

class _OutputSpecEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_euler_nodes(), op)
        self.fields_container = Output(_get_output_spec_euler_nodes(0), 0, op) 

class _EulerNodes(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::coords_and_euler_nodes"
    Scripting name is "euler_nodes"

    Description: read a field made of 3 coordinates and 3 Euler angles (6 dofs) by node from the rst file.

    Input list: 
       3: streams_container 
       4: data_sources 
       6: coord_and_euler (if true, then the field has ncomp=6 with 3 oords and 3 euler angles, else there is only the euler angles (default is true))
       7: mesh 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::coords_and_euler_nodes")
    >>> op_way2 = core.operators.result.euler_nodes()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::coords_and_euler_nodes")
        self.inputs = _InputSpecEulerNodes(self)
        self.outputs = _OutputSpecEulerNodes(self)

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

def euler_nodes():
    """Operator's description:
    Internal name is "mapdl::rst::coords_and_euler_nodes"
    Scripting name is "euler_nodes"

    Description: read a field made of 3 coordinates and 3 Euler angles (6 dofs) by node from the rst file.

    Input list: 
       3: streams_container 
       4: data_sources 
       6: coord_and_euler (if true, then the field has ncomp=6 with 3 oords and 3 euler angles, else there is only the euler angles (default is true))
       7: mesh 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::coords_and_euler_nodes")
    >>> op_way2 = core.operators.result.euler_nodes()
    """
    return _EulerNodes()

from . import mapdl #mapdl.nmisc

#internal name: ENF_rotation_by_euler_nodes
#scripting name: enf_rotation_by_euler_nodes
def _get_input_spec_enf_rotation_by_euler_nodes(pin = None):
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_enf_rotation_by_euler_nodes = { 
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_enf_rotation_by_euler_nodes
    else:
        return inputs_dict_enf_rotation_by_euler_nodes[pin]

def _get_output_spec_enf_rotation_by_euler_nodes(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_enf_rotation_by_euler_nodes = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_enf_rotation_by_euler_nodes
    else:
        return outputs_dict_enf_rotation_by_euler_nodes[pin]

class _InputSpecEnfRotationByEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_enf_rotation_by_euler_nodes(), op)
        self.fields_container = Input(_get_input_spec_enf_rotation_by_euler_nodes(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_enf_rotation_by_euler_nodes(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_enf_rotation_by_euler_nodes(4), 4, op, -1) 

class _OutputSpecEnfRotationByEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_enf_rotation_by_euler_nodes(), op)
        self.fields_container = Output(_get_output_spec_enf_rotation_by_euler_nodes(0), 0, op) 

class _EnfRotationByEulerNodes(_Operator):
    """Operator's description:
    Internal name is "ENF_rotation_by_euler_nodes"
    Scripting name is "enf_rotation_by_euler_nodes"

    Description: read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

    Input list: 
       2: fields_container 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENF_rotation_by_euler_nodes")
    >>> op_way2 = core.operators.result.enf_rotation_by_euler_nodes()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ENF_rotation_by_euler_nodes")
        self.inputs = _InputSpecEnfRotationByEulerNodes(self)
        self.outputs = _OutputSpecEnfRotationByEulerNodes(self)

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

def enf_rotation_by_euler_nodes():
    """Operator's description:
    Internal name is "ENF_rotation_by_euler_nodes"
    Scripting name is "enf_rotation_by_euler_nodes"

    Description: read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

    Input list: 
       2: fields_container 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ENF_rotation_by_euler_nodes")
    >>> op_way2 = core.operators.result.enf_rotation_by_euler_nodes()
    """
    return _EnfRotationByEulerNodes()

#internal name: cms_matrices_provider
#scripting name: cms_matrices_provider
def _get_input_spec_cms_matrices_provider(pin = None):
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """Data_sources (must contain at list one subfile).""")
    inputs_dict_cms_matrices_provider = { 
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_cms_matrices_provider
    else:
        return inputs_dict_cms_matrices_provider[pin]

def _get_output_spec_cms_matrices_provider(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """Fields container containing in this order : stiffness, damping, mass matrices, and then load vector.""")
    outputs_dict_cms_matrices_provider = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_cms_matrices_provider
    else:
        return outputs_dict_cms_matrices_provider[pin]

class _InputSpecCmsMatricesProvider(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cms_matrices_provider(), op)
        self.data_sources = Input(_get_input_spec_cms_matrices_provider(4), 4, op, -1) 

class _OutputSpecCmsMatricesProvider(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cms_matrices_provider(), op)
        self.fields_container = Output(_get_output_spec_cms_matrices_provider(0), 0, op) 

class _CmsMatricesProvider(_Operator):
    """Operator's description:
    Internal name is "cms_matrices_provider"
    Scripting name is "cms_matrices_provider"

    Description: Read reducted matrices for cms elements. Extract stiffness, damping, mass matrices and load vector from a subfile.

    Input list: 
       4: data_sources (Data_sources (must contain at list one subfile).)

    Output list: 
       0: fields_container (Fields container containing in this order : stiffness, damping, mass matrices, and then load vector.)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cms_matrices_provider")
    >>> op_way2 = core.operators.result.cms_matrices_provider()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("cms_matrices_provider")
        self.inputs = _InputSpecCmsMatricesProvider(self)
        self.outputs = _OutputSpecCmsMatricesProvider(self)

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

def cms_matrices_provider():
    """Operator's description:
    Internal name is "cms_matrices_provider"
    Scripting name is "cms_matrices_provider"

    Description: Read reducted matrices for cms elements. Extract stiffness, damping, mass matrices and load vector from a subfile.

    Input list: 
       4: data_sources (Data_sources (must contain at list one subfile).)

    Output list: 
       0: fields_container (Fields container containing in this order : stiffness, damping, mass matrices, and then load vector.)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("cms_matrices_provider")
    >>> op_way2 = core.operators.result.cms_matrices_provider()
    """
    return _CmsMatricesProvider()

from . import mapdl #mapdl.smisc

#internal name: mapdl::rst::RotateNodalFCByEulerNodes
#scripting name: nodal_rotation_by_euler_nodes
def _get_input_spec_nodal_rotation_by_euler_nodes(pin = None):
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_nodal_rotation_by_euler_nodes = { 
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_nodal_rotation_by_euler_nodes
    else:
        return inputs_dict_nodal_rotation_by_euler_nodes[pin]

def _get_output_spec_nodal_rotation_by_euler_nodes(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_rotation_by_euler_nodes = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_rotation_by_euler_nodes
    else:
        return outputs_dict_nodal_rotation_by_euler_nodes[pin]

class _InputSpecNodalRotationByEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_rotation_by_euler_nodes(), op)
        self.fields_container = Input(_get_input_spec_nodal_rotation_by_euler_nodes(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_nodal_rotation_by_euler_nodes(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_nodal_rotation_by_euler_nodes(4), 4, op, -1) 

class _OutputSpecNodalRotationByEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_rotation_by_euler_nodes(), op)
        self.fields_container = Output(_get_output_spec_nodal_rotation_by_euler_nodes(0), 0, op) 

class _NodalRotationByEulerNodes(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::RotateNodalFCByEulerNodes"
    Scripting name is "nodal_rotation_by_euler_nodes"

    Description: read Euler angles on nodes from the rst file and rotate the fields in the fieldsContainer.

    Input list: 
       2: fields_container 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::RotateNodalFCByEulerNodes")
    >>> op_way2 = core.operators.result.nodal_rotation_by_euler_nodes()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::RotateNodalFCByEulerNodes")
        self.inputs = _InputSpecNodalRotationByEulerNodes(self)
        self.outputs = _OutputSpecNodalRotationByEulerNodes(self)

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

def nodal_rotation_by_euler_nodes():
    """Operator's description:
    Internal name is "mapdl::rst::RotateNodalFCByEulerNodes"
    Scripting name is "nodal_rotation_by_euler_nodes"

    Description: read Euler angles on nodes from the rst file and rotate the fields in the fieldsContainer.

    Input list: 
       2: fields_container 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::RotateNodalFCByEulerNodes")
    >>> op_way2 = core.operators.result.nodal_rotation_by_euler_nodes()
    """
    return _NodalRotationByEulerNodes()

#internal name: mapdl::rst::S_rotation_by_euler_nodes
#scripting name: stress_rotation_by_euler_nodes
def _get_input_spec_stress_rotation_by_euler_nodes(pin = None):
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_stress_rotation_by_euler_nodes = { 
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_stress_rotation_by_euler_nodes
    else:
        return inputs_dict_stress_rotation_by_euler_nodes[pin]

def _get_output_spec_stress_rotation_by_euler_nodes(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_rotation_by_euler_nodes = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_stress_rotation_by_euler_nodes
    else:
        return outputs_dict_stress_rotation_by_euler_nodes[pin]

class _InputSpecStressRotationByEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_stress_rotation_by_euler_nodes(), op)
        self.fields_container = Input(_get_input_spec_stress_rotation_by_euler_nodes(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_stress_rotation_by_euler_nodes(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_stress_rotation_by_euler_nodes(4), 4, op, -1) 

class _OutputSpecStressRotationByEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_stress_rotation_by_euler_nodes(), op)
        self.fields_container = Output(_get_output_spec_stress_rotation_by_euler_nodes(0), 0, op) 

class _StressRotationByEulerNodes(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::S_rotation_by_euler_nodes"
    Scripting name is "stress_rotation_by_euler_nodes"

    Description: read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

    Input list: 
       2: fields_container 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::S_rotation_by_euler_nodes")
    >>> op_way2 = core.operators.result.stress_rotation_by_euler_nodes()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::S_rotation_by_euler_nodes")
        self.inputs = _InputSpecStressRotationByEulerNodes(self)
        self.outputs = _OutputSpecStressRotationByEulerNodes(self)

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

def stress_rotation_by_euler_nodes():
    """Operator's description:
    Internal name is "mapdl::rst::S_rotation_by_euler_nodes"
    Scripting name is "stress_rotation_by_euler_nodes"

    Description: read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

    Input list: 
       2: fields_container 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::S_rotation_by_euler_nodes")
    >>> op_way2 = core.operators.result.stress_rotation_by_euler_nodes()
    """
    return _StressRotationByEulerNodes()

#internal name: mapdl::rst::EPEL_rotation_by_euler_nodes
#scripting name: elastic_strain_rotation_by_euler_nodes
def _get_input_spec_elastic_strain_rotation_by_euler_nodes(pin = None):
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_elastic_strain_rotation_by_euler_nodes = { 
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_elastic_strain_rotation_by_euler_nodes
    else:
        return inputs_dict_elastic_strain_rotation_by_euler_nodes[pin]

def _get_output_spec_elastic_strain_rotation_by_euler_nodes(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_rotation_by_euler_nodes = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elastic_strain_rotation_by_euler_nodes
    else:
        return outputs_dict_elastic_strain_rotation_by_euler_nodes[pin]

class _InputSpecElasticStrainRotationByEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elastic_strain_rotation_by_euler_nodes(), op)
        self.fields_container = Input(_get_input_spec_elastic_strain_rotation_by_euler_nodes(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_elastic_strain_rotation_by_euler_nodes(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_elastic_strain_rotation_by_euler_nodes(4), 4, op, -1) 

class _OutputSpecElasticStrainRotationByEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elastic_strain_rotation_by_euler_nodes(), op)
        self.fields_container = Output(_get_output_spec_elastic_strain_rotation_by_euler_nodes(0), 0, op) 

class _ElasticStrainRotationByEulerNodes(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::EPEL_rotation_by_euler_nodes"
    Scripting name is "elastic_strain_rotation_by_euler_nodes"

    Description: read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

    Input list: 
       2: fields_container 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::EPEL_rotation_by_euler_nodes")
    >>> op_way2 = core.operators.result.elastic_strain_rotation_by_euler_nodes()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::EPEL_rotation_by_euler_nodes")
        self.inputs = _InputSpecElasticStrainRotationByEulerNodes(self)
        self.outputs = _OutputSpecElasticStrainRotationByEulerNodes(self)

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

def elastic_strain_rotation_by_euler_nodes():
    """Operator's description:
    Internal name is "mapdl::rst::EPEL_rotation_by_euler_nodes"
    Scripting name is "elastic_strain_rotation_by_euler_nodes"

    Description: read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

    Input list: 
       2: fields_container 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::EPEL_rotation_by_euler_nodes")
    >>> op_way2 = core.operators.result.elastic_strain_rotation_by_euler_nodes()
    """
    return _ElasticStrainRotationByEulerNodes()

#internal name: mapdl::rst::EPPL_rotation_by_euler_nodes
#scripting name: plastic_strain_rotation_by_euler_nodes
def _get_input_spec_plastic_strain_rotation_by_euler_nodes(pin = None):
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_plastic_strain_rotation_by_euler_nodes = { 
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_plastic_strain_rotation_by_euler_nodes
    else:
        return inputs_dict_plastic_strain_rotation_by_euler_nodes[pin]

def _get_output_spec_plastic_strain_rotation_by_euler_nodes(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_rotation_by_euler_nodes = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_plastic_strain_rotation_by_euler_nodes
    else:
        return outputs_dict_plastic_strain_rotation_by_euler_nodes[pin]

class _InputSpecPlasticStrainRotationByEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_plastic_strain_rotation_by_euler_nodes(), op)
        self.fields_container = Input(_get_input_spec_plastic_strain_rotation_by_euler_nodes(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_plastic_strain_rotation_by_euler_nodes(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_plastic_strain_rotation_by_euler_nodes(4), 4, op, -1) 

class _OutputSpecPlasticStrainRotationByEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_plastic_strain_rotation_by_euler_nodes(), op)
        self.fields_container = Output(_get_output_spec_plastic_strain_rotation_by_euler_nodes(0), 0, op) 

class _PlasticStrainRotationByEulerNodes(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::EPPL_rotation_by_euler_nodes"
    Scripting name is "plastic_strain_rotation_by_euler_nodes"

    Description: read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

    Input list: 
       2: fields_container 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::EPPL_rotation_by_euler_nodes")
    >>> op_way2 = core.operators.result.plastic_strain_rotation_by_euler_nodes()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::EPPL_rotation_by_euler_nodes")
        self.inputs = _InputSpecPlasticStrainRotationByEulerNodes(self)
        self.outputs = _OutputSpecPlasticStrainRotationByEulerNodes(self)

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

def plastic_strain_rotation_by_euler_nodes():
    """Operator's description:
    Internal name is "mapdl::rst::EPPL_rotation_by_euler_nodes"
    Scripting name is "plastic_strain_rotation_by_euler_nodes"

    Description: read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

    Input list: 
       2: fields_container 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::EPPL_rotation_by_euler_nodes")
    >>> op_way2 = core.operators.result.plastic_strain_rotation_by_euler_nodes()
    """
    return _PlasticStrainRotationByEulerNodes()

from . import mapdl #mapdl.pres_to_field

from . import mapdl #mapdl.prns_to_field

#internal name: ExtractRigidBodyMotion
#scripting name: remove_rigid_body_motion
def _get_input_spec_remove_rigid_body_motion(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "reference_node_id", type_names = ["int32"], optional = True, document = """Id of the reference entity (node).""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """default is the mesh in the support""")
    inputs_dict_remove_rigid_body_motion = { 
        0 : inpin0,
        1 : inpin1,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_remove_rigid_body_motion
    else:
        return inputs_dict_remove_rigid_body_motion[pin]

def _get_output_spec_remove_rigid_body_motion(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_remove_rigid_body_motion = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_remove_rigid_body_motion
    else:
        return outputs_dict_remove_rigid_body_motion[pin]

class _InputSpecRemoveRigidBodyMotion(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_remove_rigid_body_motion(), op)
        self.field = Input(_get_input_spec_remove_rigid_body_motion(0), 0, op, -1) 
        self.reference_node_id = Input(_get_input_spec_remove_rigid_body_motion(1), 1, op, -1) 
        self.mesh = Input(_get_input_spec_remove_rigid_body_motion(7), 7, op, -1) 

class _OutputSpecRemoveRigidBodyMotion(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_remove_rigid_body_motion(), op)
        self.field = Output(_get_output_spec_remove_rigid_body_motion(0), 0, op) 

class _RemoveRigidBodyMotion(_Operator):
    """Operator's description:
    Internal name is "ExtractRigidBodyMotion"
    Scripting name is "remove_rigid_body_motion"

    Description: Removes rigid body mode from a total displacement field by minimization. Use a reference point in order to substract its displacement to the result displacement field.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: reference_node_id (Id of the reference entity (node).)
       7: mesh (default is the mesh in the support)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ExtractRigidBodyMotion")
    >>> op_way2 = core.operators.result.remove_rigid_body_motion()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ExtractRigidBodyMotion")
        self.inputs = _InputSpecRemoveRigidBodyMotion(self)
        self.outputs = _OutputSpecRemoveRigidBodyMotion(self)

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

def remove_rigid_body_motion():
    """Operator's description:
    Internal name is "ExtractRigidBodyMotion"
    Scripting name is "remove_rigid_body_motion"

    Description: Removes rigid body mode from a total displacement field by minimization. Use a reference point in order to substract its displacement to the result displacement field.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: reference_node_id (Id of the reference entity (node).)
       7: mesh (default is the mesh in the support)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ExtractRigidBodyMotion")
    >>> op_way2 = core.operators.result.remove_rigid_body_motion()
    """
    return _RemoveRigidBodyMotion()

#internal name: ExtractRigidBodyMotion_fc
#scripting name: remove_rigid_body_motion_fc
def _get_input_spec_remove_rigid_body_motion_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "reference_node_id", type_names = ["int32"], optional = True, document = """Id of the reference entity (node).""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """default is the mesh in the support""")
    inputs_dict_remove_rigid_body_motion_fc = { 
        0 : inpin0,
        1 : inpin1,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_remove_rigid_body_motion_fc
    else:
        return inputs_dict_remove_rigid_body_motion_fc[pin]

def _get_output_spec_remove_rigid_body_motion_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_remove_rigid_body_motion_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_remove_rigid_body_motion_fc
    else:
        return outputs_dict_remove_rigid_body_motion_fc[pin]

class _InputSpecRemoveRigidBodyMotionFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_remove_rigid_body_motion_fc(), op)
        self.fields_container = Input(_get_input_spec_remove_rigid_body_motion_fc(0), 0, op, -1) 
        self.reference_node_id = Input(_get_input_spec_remove_rigid_body_motion_fc(1), 1, op, -1) 
        self.mesh = Input(_get_input_spec_remove_rigid_body_motion_fc(7), 7, op, -1) 

class _OutputSpecRemoveRigidBodyMotionFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_remove_rigid_body_motion_fc(), op)
        self.fields_container = Output(_get_output_spec_remove_rigid_body_motion_fc(0), 0, op) 

class _RemoveRigidBodyMotionFc(_Operator):
    """Operator's description:
    Internal name is "ExtractRigidBodyMotion_fc"
    Scripting name is "remove_rigid_body_motion_fc"

    Description: Removes rigid body mode from a total displacement field by minimization. Use a reference point in order to substract its displacement to the result displacement field.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: reference_node_id (Id of the reference entity (node).)
       7: mesh (default is the mesh in the support)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ExtractRigidBodyMotion_fc")
    >>> op_way2 = core.operators.result.remove_rigid_body_motion_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ExtractRigidBodyMotion_fc")
        self.inputs = _InputSpecRemoveRigidBodyMotionFc(self)
        self.outputs = _OutputSpecRemoveRigidBodyMotionFc(self)

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

def remove_rigid_body_motion_fc():
    """Operator's description:
    Internal name is "ExtractRigidBodyMotion_fc"
    Scripting name is "remove_rigid_body_motion_fc"

    Description: Removes rigid body mode from a total displacement field by minimization. Use a reference point in order to substract its displacement to the result displacement field.

    Input list: 
       0: fields_container (field or fields container with only one field is expected)
       1: reference_node_id (Id of the reference entity (node).)
       7: mesh (default is the mesh in the support)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ExtractRigidBodyMotion_fc")
    >>> op_way2 = core.operators.result.remove_rigid_body_motion_fc()
    """
    return _RemoveRigidBodyMotionFc()

#internal name: RigidBodyAddition_fc
#scripting name: add_rigid_body_motion_fc
def _get_input_spec_add_rigid_body_motion_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "translation_field", type_names = ["field"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "rotation_field", type_names = ["field"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "center_field", type_names = ["field"], optional = False, document = """""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """default is the mesh in the support""")
    inputs_dict_add_rigid_body_motion_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        7 : inpin7
    }
    if pin is None:
        return inputs_dict_add_rigid_body_motion_fc
    else:
        return inputs_dict_add_rigid_body_motion_fc[pin]

def _get_output_spec_add_rigid_body_motion_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_add_rigid_body_motion_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_add_rigid_body_motion_fc
    else:
        return outputs_dict_add_rigid_body_motion_fc[pin]

class _InputSpecAddRigidBodyMotionFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_add_rigid_body_motion_fc(), op)
        self.fields_container = Input(_get_input_spec_add_rigid_body_motion_fc(0), 0, op, -1) 
        self.translation_field = Input(_get_input_spec_add_rigid_body_motion_fc(1), 1, op, -1) 
        self.rotation_field = Input(_get_input_spec_add_rigid_body_motion_fc(2), 2, op, -1) 
        self.center_field = Input(_get_input_spec_add_rigid_body_motion_fc(3), 3, op, -1) 
        self.mesh = Input(_get_input_spec_add_rigid_body_motion_fc(7), 7, op, -1) 

class _OutputSpecAddRigidBodyMotionFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_add_rigid_body_motion_fc(), op)
        self.fields_container = Output(_get_output_spec_add_rigid_body_motion_fc(0), 0, op) 

class _AddRigidBodyMotionFc(_Operator):
    """Operator's description:
    Internal name is "RigidBodyAddition_fc"
    Scripting name is "add_rigid_body_motion_fc"

    Description: Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem

    Input list: 
       0: fields_container 
       1: translation_field 
       2: rotation_field 
       3: center_field 
       7: mesh (default is the mesh in the support)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("RigidBodyAddition_fc")
    >>> op_way2 = core.operators.result.add_rigid_body_motion_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("RigidBodyAddition_fc")
        self.inputs = _InputSpecAddRigidBodyMotionFc(self)
        self.outputs = _OutputSpecAddRigidBodyMotionFc(self)

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

def add_rigid_body_motion_fc():
    """Operator's description:
    Internal name is "RigidBodyAddition_fc"
    Scripting name is "add_rigid_body_motion_fc"

    Description: Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem

    Input list: 
       0: fields_container 
       1: translation_field 
       2: rotation_field 
       3: center_field 
       7: mesh (default is the mesh in the support)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("RigidBodyAddition_fc")
    >>> op_way2 = core.operators.result.add_rigid_body_motion_fc()
    """
    return _AddRigidBodyMotionFc()

#internal name: mapdl::rst::U_cyclic
#scripting name: cyclic_expanded_displacement
def _get_input_spec_cyclic_expanded_displacement(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "sector_mesh", type_names = ["meshed_region"], optional = True, document = """mesh of the base sector (can be a skin).""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """location needed in output""")
    inpin12 = _PinSpecification(name = "freq", type_names = ["double"], optional = False, document = """""")
    inpin14 = _PinSpecification(name = "read_cyclic", type_names = ["int32"], optional = True, document = """if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1)""")
    inpin15 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], optional = True, document = """mesh expanded.""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = True, document = """""")
    inpin18 = _PinSpecification(name = "sectors_to_expand", type_names = ["scoping","scopings_container"], optional = True, document = """sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.""")
    inpin19 = _PinSpecification(name = "phi", type_names = ["double"], optional = True, document = """angle phi (default value 0.0)""")
    inpin20 = _PinSpecification(name = "filter_degenerated_elements", type_names = ["bool"], optional = True, document = """if it's set to true, results are filtered to handle degenerated elements (default is true)""")
    inputs_dict_cyclic_expanded_displacement = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        12 : inpin12,
        14 : inpin14,
        15 : inpin15,
        16 : inpin16,
        18 : inpin18,
        19 : inpin19,
        20 : inpin20
    }
    if pin is None:
        return inputs_dict_cyclic_expanded_displacement
    else:
        return inputs_dict_cyclic_expanded_displacement[pin]

def _get_output_spec_cyclic_expanded_displacement(pin = None):
    outpin0 = _PinSpecification(name = "static_matrix", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outpin1 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], document = """""")
    outpin2 = _PinSpecification(name = "inertia_matrix", type_names = ["fields_container"], document = """""")
    outpin3 = _PinSpecification(name = "remote_point_id", type_names = ["int32"], document = """""")
    outputs_dict_cyclic_expanded_displacement = { 
        0 : outpin0,
        1 : outpin1,
        2 : outpin2,
        3 : outpin3
    }
    if pin is None:
        return outputs_dict_cyclic_expanded_displacement
    else:
        return outputs_dict_cyclic_expanded_displacement[pin]

class _InputSpecCyclicExpandedDisplacement(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cyclic_expanded_displacement(), op)
        self.time_scoping = Input(_get_input_spec_cyclic_expanded_displacement(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_cyclic_expanded_displacement(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_cyclic_expanded_displacement(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_cyclic_expanded_displacement(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_cyclic_expanded_displacement(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_cyclic_expanded_displacement(5), 5, op, -1) 
        self.sector_mesh = Input(_get_input_spec_cyclic_expanded_displacement(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_cyclic_expanded_displacement(9), 9, op, -1) 
        self.freq = Input(_get_input_spec_cyclic_expanded_displacement(12), 12, op, -1) 
        self.read_cyclic = Input(_get_input_spec_cyclic_expanded_displacement(14), 14, op, -1) 
        self.expanded_meshed_region = Input(_get_input_spec_cyclic_expanded_displacement(15), 15, op, -1) 
        self.cyclic_support = Input(_get_input_spec_cyclic_expanded_displacement(16), 16, op, -1) 
        self.sectors_to_expand = Input(_get_input_spec_cyclic_expanded_displacement(18), 18, op, -1) 
        self.phi = Input(_get_input_spec_cyclic_expanded_displacement(19), 19, op, -1) 
        self.filter_degenerated_elements = Input(_get_input_spec_cyclic_expanded_displacement(20), 20, op, -1) 

class _OutputSpecCyclicExpandedDisplacement(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cyclic_expanded_displacement(), op)
        self.static_matrix = Output(_get_output_spec_cyclic_expanded_displacement(0), 0, op) 
        self.expanded_meshed_region = Output(_get_output_spec_cyclic_expanded_displacement(1), 1, op) 
        self.inertia_matrix = Output(_get_output_spec_cyclic_expanded_displacement(2), 2, op) 
        self.remote_point_id = Output(_get_output_spec_cyclic_expanded_displacement(3), 3, op) 

class _CyclicExpandedDisplacement(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::U_cyclic"
    Scripting name is "cyclic_expanded_displacement"

    Description: Read displacements from an rst file and expand it with cyclic symmetry.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       12: freq 
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (angle phi (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: static_matrix (FieldsContainer filled in)
       1: expanded_meshed_region 
       2: inertia_matrix 
       3: remote_point_id 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::U_cyclic")
    >>> op_way2 = core.operators.result.cyclic_expanded_displacement()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::U_cyclic")
        self.inputs = _InputSpecCyclicExpandedDisplacement(self)
        self.outputs = _OutputSpecCyclicExpandedDisplacement(self)

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

def cyclic_expanded_displacement():
    """Operator's description:
    Internal name is "mapdl::rst::U_cyclic"
    Scripting name is "cyclic_expanded_displacement"

    Description: Read displacements from an rst file and expand it with cyclic symmetry.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       12: freq 
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (angle phi (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: static_matrix (FieldsContainer filled in)
       1: expanded_meshed_region 
       2: inertia_matrix 
       3: remote_point_id 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::U_cyclic")
    >>> op_way2 = core.operators.result.cyclic_expanded_displacement()
    """
    return _CyclicExpandedDisplacement()

#internal name: mapdl::rst::A_cyclic
#scripting name: cyclic_expanded_acceleration
def _get_input_spec_cyclic_expanded_acceleration(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "sector_mesh", type_names = ["meshed_region"], optional = True, document = """mesh of the base sector (can be a skin).""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """location needed in output""")
    inpin12 = _PinSpecification(name = "freq", type_names = ["double"], optional = False, document = """""")
    inpin14 = _PinSpecification(name = "read_cyclic", type_names = ["int32"], optional = True, document = """if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1)""")
    inpin15 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], optional = True, document = """mesh expanded.""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = True, document = """""")
    inpin18 = _PinSpecification(name = "sectors_to_expand", type_names = ["scoping","scopings_container"], optional = True, document = """sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.""")
    inpin19 = _PinSpecification(name = "phi", type_names = ["double"], optional = True, document = """angle phi (default value 0.0)""")
    inpin20 = _PinSpecification(name = "filter_degenerated_elements", type_names = ["bool"], optional = True, document = """if it's set to true, results are filtered to handle degenerated elements (default is true)""")
    inputs_dict_cyclic_expanded_acceleration = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        12 : inpin12,
        14 : inpin14,
        15 : inpin15,
        16 : inpin16,
        18 : inpin18,
        19 : inpin19,
        20 : inpin20
    }
    if pin is None:
        return inputs_dict_cyclic_expanded_acceleration
    else:
        return inputs_dict_cyclic_expanded_acceleration[pin]

def _get_output_spec_cyclic_expanded_acceleration(pin = None):
    outpin0 = _PinSpecification(name = "static_matrix", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outpin1 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], document = """""")
    outpin2 = _PinSpecification(name = "inertia_matrix", type_names = ["fields_container"], document = """""")
    outpin3 = _PinSpecification(name = "remote_point_id", type_names = ["int32"], document = """""")
    outputs_dict_cyclic_expanded_acceleration = { 
        0 : outpin0,
        1 : outpin1,
        2 : outpin2,
        3 : outpin3
    }
    if pin is None:
        return outputs_dict_cyclic_expanded_acceleration
    else:
        return outputs_dict_cyclic_expanded_acceleration[pin]

class _InputSpecCyclicExpandedAcceleration(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cyclic_expanded_acceleration(), op)
        self.time_scoping = Input(_get_input_spec_cyclic_expanded_acceleration(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_cyclic_expanded_acceleration(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_cyclic_expanded_acceleration(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_cyclic_expanded_acceleration(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_cyclic_expanded_acceleration(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_cyclic_expanded_acceleration(5), 5, op, -1) 
        self.sector_mesh = Input(_get_input_spec_cyclic_expanded_acceleration(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_cyclic_expanded_acceleration(9), 9, op, -1) 
        self.freq = Input(_get_input_spec_cyclic_expanded_acceleration(12), 12, op, -1) 
        self.read_cyclic = Input(_get_input_spec_cyclic_expanded_acceleration(14), 14, op, -1) 
        self.expanded_meshed_region = Input(_get_input_spec_cyclic_expanded_acceleration(15), 15, op, -1) 
        self.cyclic_support = Input(_get_input_spec_cyclic_expanded_acceleration(16), 16, op, -1) 
        self.sectors_to_expand = Input(_get_input_spec_cyclic_expanded_acceleration(18), 18, op, -1) 
        self.phi = Input(_get_input_spec_cyclic_expanded_acceleration(19), 19, op, -1) 
        self.filter_degenerated_elements = Input(_get_input_spec_cyclic_expanded_acceleration(20), 20, op, -1) 

class _OutputSpecCyclicExpandedAcceleration(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cyclic_expanded_acceleration(), op)
        self.static_matrix = Output(_get_output_spec_cyclic_expanded_acceleration(0), 0, op) 
        self.expanded_meshed_region = Output(_get_output_spec_cyclic_expanded_acceleration(1), 1, op) 
        self.inertia_matrix = Output(_get_output_spec_cyclic_expanded_acceleration(2), 2, op) 
        self.remote_point_id = Output(_get_output_spec_cyclic_expanded_acceleration(3), 3, op) 

class _CyclicExpandedAcceleration(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::A_cyclic"
    Scripting name is "cyclic_expanded_acceleration"

    Description: Read acceleration from an rst file and expand it with cyclic symmetry.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       12: freq 
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (angle phi (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: static_matrix (FieldsContainer filled in)
       1: expanded_meshed_region 
       2: inertia_matrix 
       3: remote_point_id 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::A_cyclic")
    >>> op_way2 = core.operators.result.cyclic_expanded_acceleration()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::A_cyclic")
        self.inputs = _InputSpecCyclicExpandedAcceleration(self)
        self.outputs = _OutputSpecCyclicExpandedAcceleration(self)

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

def cyclic_expanded_acceleration():
    """Operator's description:
    Internal name is "mapdl::rst::A_cyclic"
    Scripting name is "cyclic_expanded_acceleration"

    Description: Read acceleration from an rst file and expand it with cyclic symmetry.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       12: freq 
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (angle phi (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: static_matrix (FieldsContainer filled in)
       1: expanded_meshed_region 
       2: inertia_matrix 
       3: remote_point_id 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::A_cyclic")
    >>> op_way2 = core.operators.result.cyclic_expanded_acceleration()
    """
    return _CyclicExpandedAcceleration()

#internal name: mapdl::rst::S_cyclic
#scripting name: cyclic_expanded_stress
def _get_input_spec_cyclic_expanded_stress(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "sector_mesh", type_names = ["meshed_region"], optional = True, document = """mesh of the base sector (can be a skin).""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """location needed in output""")
    inpin12 = _PinSpecification(name = "freq", type_names = ["double"], optional = False, document = """""")
    inpin14 = _PinSpecification(name = "read_cyclic", type_names = ["int32"], optional = True, document = """if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1)""")
    inpin15 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], optional = True, document = """mesh expanded.""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = True, document = """""")
    inpin18 = _PinSpecification(name = "sectors_to_expand", type_names = ["scoping","scopings_container"], optional = True, document = """sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.""")
    inpin19 = _PinSpecification(name = "phi", type_names = ["double"], optional = True, document = """phi angle (default value 0.0)""")
    inpin20 = _PinSpecification(name = "filter_degenerated_elements", type_names = ["bool"], optional = True, document = """if it's set to true, results are filtered to handle degenerated elements (default is true)""")
    inputs_dict_cyclic_expanded_stress = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        12 : inpin12,
        14 : inpin14,
        15 : inpin15,
        16 : inpin16,
        18 : inpin18,
        19 : inpin19,
        20 : inpin20
    }
    if pin is None:
        return inputs_dict_cyclic_expanded_stress
    else:
        return inputs_dict_cyclic_expanded_stress[pin]

def _get_output_spec_cyclic_expanded_stress(pin = None):
    outpin0 = _PinSpecification(name = "static_matrix", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outpin1 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], document = """""")
    outpin2 = _PinSpecification(name = "inertia_matrix", type_names = ["fields_container"], document = """""")
    outpin3 = _PinSpecification(name = "remote_point_id", type_names = ["int32"], document = """""")
    outputs_dict_cyclic_expanded_stress = { 
        0 : outpin0,
        1 : outpin1,
        2 : outpin2,
        3 : outpin3
    }
    if pin is None:
        return outputs_dict_cyclic_expanded_stress
    else:
        return outputs_dict_cyclic_expanded_stress[pin]

class _InputSpecCyclicExpandedStress(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cyclic_expanded_stress(), op)
        self.time_scoping = Input(_get_input_spec_cyclic_expanded_stress(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_cyclic_expanded_stress(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_cyclic_expanded_stress(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_cyclic_expanded_stress(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_cyclic_expanded_stress(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_cyclic_expanded_stress(5), 5, op, -1) 
        self.sector_mesh = Input(_get_input_spec_cyclic_expanded_stress(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_cyclic_expanded_stress(9), 9, op, -1) 
        self.freq = Input(_get_input_spec_cyclic_expanded_stress(12), 12, op, -1) 
        self.read_cyclic = Input(_get_input_spec_cyclic_expanded_stress(14), 14, op, -1) 
        self.expanded_meshed_region = Input(_get_input_spec_cyclic_expanded_stress(15), 15, op, -1) 
        self.cyclic_support = Input(_get_input_spec_cyclic_expanded_stress(16), 16, op, -1) 
        self.sectors_to_expand = Input(_get_input_spec_cyclic_expanded_stress(18), 18, op, -1) 
        self.phi = Input(_get_input_spec_cyclic_expanded_stress(19), 19, op, -1) 
        self.filter_degenerated_elements = Input(_get_input_spec_cyclic_expanded_stress(20), 20, op, -1) 

class _OutputSpecCyclicExpandedStress(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cyclic_expanded_stress(), op)
        self.static_matrix = Output(_get_output_spec_cyclic_expanded_stress(0), 0, op) 
        self.expanded_meshed_region = Output(_get_output_spec_cyclic_expanded_stress(1), 1, op) 
        self.inertia_matrix = Output(_get_output_spec_cyclic_expanded_stress(2), 2, op) 
        self.remote_point_id = Output(_get_output_spec_cyclic_expanded_stress(3), 3, op) 

class _CyclicExpandedStress(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::S_cyclic"
    Scripting name is "cyclic_expanded_stress"

    Description: Read mapdl::rst::S from an rst file and expand it with cyclic symmetry.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       12: freq 
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (phi angle (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: static_matrix (FieldsContainer filled in)
       1: expanded_meshed_region 
       2: inertia_matrix 
       3: remote_point_id 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::S_cyclic")
    >>> op_way2 = core.operators.result.cyclic_expanded_stress()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::S_cyclic")
        self.inputs = _InputSpecCyclicExpandedStress(self)
        self.outputs = _OutputSpecCyclicExpandedStress(self)

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

def cyclic_expanded_stress():
    """Operator's description:
    Internal name is "mapdl::rst::S_cyclic"
    Scripting name is "cyclic_expanded_stress"

    Description: Read mapdl::rst::S from an rst file and expand it with cyclic symmetry.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       12: freq 
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (phi angle (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: static_matrix (FieldsContainer filled in)
       1: expanded_meshed_region 
       2: inertia_matrix 
       3: remote_point_id 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::S_cyclic")
    >>> op_way2 = core.operators.result.cyclic_expanded_stress()
    """
    return _CyclicExpandedStress()

#internal name: mapdl::rst::ENG_VOL_cyclic
#scripting name: cyclic_volume
def _get_input_spec_cyclic_volume(pin = None):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin5 = _PinSpecification(name = "bool_rotate_to_global", type_names = ["bool"], optional = True, document = """if true the field is roated to global coordinate system (default true)""")
    inpin7 = _PinSpecification(name = "sector_mesh", type_names = ["meshed_region"], optional = True, document = """mesh of the base sector (can be a skin).""")
    inpin9 = _PinSpecification(name = "requested_location", type_names = ["string"], optional = True, document = """location needed in output""")
    inpin12 = _PinSpecification(name = "freq", type_names = ["double"], optional = False, document = """""")
    inpin14 = _PinSpecification(name = "read_cyclic", type_names = ["int32"], optional = True, document = """if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1)""")
    inpin15 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], optional = True, document = """mesh expanded.""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = True, document = """""")
    inpin18 = _PinSpecification(name = "sectors_to_expand", type_names = ["scoping","scopings_container"], optional = True, document = """sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.""")
    inpin19 = _PinSpecification(name = "phi", type_names = ["double"], optional = True, document = """phi angle (default value 0.0)""")
    inpin20 = _PinSpecification(name = "filter_degenerated_elements", type_names = ["bool"], optional = True, document = """if it's set to true, results are filtered to handle degenerated elements (default is true)""")
    inputs_dict_cyclic_volume = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        5 : inpin5,
        7 : inpin7,
        9 : inpin9,
        12 : inpin12,
        14 : inpin14,
        15 : inpin15,
        16 : inpin16,
        18 : inpin18,
        19 : inpin19,
        20 : inpin20
    }
    if pin is None:
        return inputs_dict_cyclic_volume
    else:
        return inputs_dict_cyclic_volume[pin]

def _get_output_spec_cyclic_volume(pin = None):
    outpin0 = _PinSpecification(name = "static_matrix", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outpin1 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], document = """""")
    outpin2 = _PinSpecification(name = "inertia_matrix", type_names = ["fields_container"], document = """""")
    outpin3 = _PinSpecification(name = "remote_point_id", type_names = ["int32"], document = """""")
    outputs_dict_cyclic_volume = { 
        0 : outpin0,
        1 : outpin1,
        2 : outpin2,
        3 : outpin3
    }
    if pin is None:
        return outputs_dict_cyclic_volume
    else:
        return outputs_dict_cyclic_volume[pin]

class _InputSpecCyclicVolume(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_cyclic_volume(), op)
        self.time_scoping = Input(_get_input_spec_cyclic_volume(0), 0, op, -1) 
        self.mesh_scoping = Input(_get_input_spec_cyclic_volume(1), 1, op, -1) 
        self.fields_container = Input(_get_input_spec_cyclic_volume(2), 2, op, -1) 
        self.streams_container = Input(_get_input_spec_cyclic_volume(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_cyclic_volume(4), 4, op, -1) 
        self.bool_rotate_to_global = Input(_get_input_spec_cyclic_volume(5), 5, op, -1) 
        self.sector_mesh = Input(_get_input_spec_cyclic_volume(7), 7, op, -1) 
        self.requested_location = Input(_get_input_spec_cyclic_volume(9), 9, op, -1) 
        self.freq = Input(_get_input_spec_cyclic_volume(12), 12, op, -1) 
        self.read_cyclic = Input(_get_input_spec_cyclic_volume(14), 14, op, -1) 
        self.expanded_meshed_region = Input(_get_input_spec_cyclic_volume(15), 15, op, -1) 
        self.cyclic_support = Input(_get_input_spec_cyclic_volume(16), 16, op, -1) 
        self.sectors_to_expand = Input(_get_input_spec_cyclic_volume(18), 18, op, -1) 
        self.phi = Input(_get_input_spec_cyclic_volume(19), 19, op, -1) 
        self.filter_degenerated_elements = Input(_get_input_spec_cyclic_volume(20), 20, op, -1) 

class _OutputSpecCyclicVolume(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_cyclic_volume(), op)
        self.static_matrix = Output(_get_output_spec_cyclic_volume(0), 0, op) 
        self.expanded_meshed_region = Output(_get_output_spec_cyclic_volume(1), 1, op) 
        self.inertia_matrix = Output(_get_output_spec_cyclic_volume(2), 2, op) 
        self.remote_point_id = Output(_get_output_spec_cyclic_volume(3), 3, op) 

class _CyclicVolume(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::ENG_VOL_cyclic"
    Scripting name is "cyclic_volume"

    Description: Read mapdl::rst::ENG_VOL from an rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       12: freq 
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (phi angle (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: static_matrix (FieldsContainer filled in)
       1: expanded_meshed_region 
       2: inertia_matrix 
       3: remote_point_id 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::ENG_VOL_cyclic")
    >>> op_way2 = core.operators.result.cyclic_volume()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::ENG_VOL_cyclic")
        self.inputs = _InputSpecCyclicVolume(self)
        self.outputs = _OutputSpecCyclicVolume(self)

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

def cyclic_volume():
    """Operator's description:
    Internal name is "mapdl::rst::ENG_VOL_cyclic"
    Scripting name is "cyclic_volume"

    Description: Read mapdl::rst::ENG_VOL from an rst file.

    Input list: 
       0: time_scoping 
       1: mesh_scoping 
       2: fields_container (FieldsContainer already allocated modified inplace)
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       5: bool_rotate_to_global (if true the field is roated to global coordinate system (default true))
       7: sector_mesh (mesh of the base sector (can be a skin).)
       9: requested_location (location needed in output)
       12: freq 
       14: read_cyclic (if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done (default is 1))
       15: expanded_meshed_region (mesh expanded.)
       16: cyclic_support 
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)
       19: phi (phi angle (default value 0.0))
       20: filter_degenerated_elements (if it's set to true, results are filtered to handle degenerated elements (default is true))

    Output list: 
       0: static_matrix (FieldsContainer filled in)
       1: expanded_meshed_region 
       2: inertia_matrix 
       3: remote_point_id 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::ENG_VOL_cyclic")
    >>> op_way2 = core.operators.result.cyclic_volume()
    """
    return _CyclicVolume()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from meshOperatorsCore.dll plugin, from "result" category
"""

#internal name: vtk::vtk::FieldProvider
#scripting name: to_field
def _get_input_spec_to_field(pin = None):
    inpin3 = _PinSpecification(name = "streams", type_names = ["streams_container"], optional = True, document = """streams""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = True, document = """data_sources""")
    inputs_dict_to_field = { 
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_to_field
    else:
        return inputs_dict_to_field[pin]

def _get_output_spec_to_field(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """fields_container""")
    outputs_dict_to_field = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_to_field
    else:
        return outputs_dict_to_field[pin]

class _InputSpecToField(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_to_field(), op)
        self.streams = Input(_get_input_spec_to_field(3), 3, op, -1) 
        self.data_sources = Input(_get_input_spec_to_field(4), 4, op, -1) 

class _OutputSpecToField(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_to_field(), op)
        self.fields_container = Output(_get_output_spec_to_field(0), 0, op) 

class _ToField(_Operator):
    """Operator's description:
    Internal name is "vtk::vtk::FieldProvider"
    Scripting name is "to_field"

    Description: Write a field based on a vtk file.

    Input list: 
       3: streams (streams)
       4: data_sources (data_sources)

    Output list: 
       0: fields_container (fields_container)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("vtk::vtk::FieldProvider")
    >>> op_way2 = core.operators.result.to_field()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("vtk::vtk::FieldProvider")
        self.inputs = _InputSpecToField(self)
        self.outputs = _OutputSpecToField(self)

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

def to_field():
    """Operator's description:
    Internal name is "vtk::vtk::FieldProvider"
    Scripting name is "to_field"

    Description: Write a field based on a vtk file.

    Input list: 
       3: streams (streams)
       4: data_sources (data_sources)

    Output list: 
       0: fields_container (fields_container)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("vtk::vtk::FieldProvider")
    >>> op_way2 = core.operators.result.to_field()
    """
    return _ToField()

