from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "result" category
"""

#internal name: EPPL1
#scripting name: plastic_strain_principal_1
def _get_input_spec_plastic_strain_principal_1(pin):
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
    return inputs_dict_plastic_strain_principal_1[pin]

def _get_output_spec_plastic_strain_principal_1(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_principal_1 = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_principal_1[pin]

class _InputSpecPlasticStrainPrincipal1(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain_principal_1(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain_principal_1(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain_principal_1(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_principal_1(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_principal_1(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain_principal_1(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain_principal_1(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain_principal_1(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain_principal_1(17), 17, op, -1) 

class _OutputSpecPlasticStrainPrincipal1(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_principal_1(0), 0, op) 

class _PlasticStrainPrincipal1:
    """Operator's description:
Internal name is "EPPL1"
Scripting name is "plastic_strain_principal_1"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPPL1")
- using dpf.operators.result.plastic_strain_principal_1()

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
"""
    def __init__(self):
         self._name = "EPPL1"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainPrincipal1(self._op)
         self.outputs = _OutputSpecPlasticStrainPrincipal1(self._op)

def plastic_strain_principal_1():
    return _PlasticStrainPrincipal1()

#internal name: RigidTransformationProvider
#scripting name: rigid_transformation
def _get_input_spec_rigid_transformation(pin):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inputs_dict_rigid_transformation = { 
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_rigid_transformation[pin]

def _get_output_spec_rigid_transformation(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_rigid_transformation = { 
        0 : outpin0
    }
    return outputs_dict_rigid_transformation[pin]

class _InputSpecRigidTransformation(_Inputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Input(_get_input_spec_rigid_transformation(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_rigid_transformation(4), 4, op, -1) 

class _OutputSpecRigidTransformation(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_rigid_transformation(0), 0, op) 

class _RigidTransformation:
    """Operator's description:
Internal name is "RigidTransformationProvider"
Scripting name is "rigid_transformation"

This operator can be instantiated in both following ways:
- using dpf.Operator("RigidTransformationProvider")
- using dpf.operators.result.rigid_transformation()

Input list: 
   3: streams_container (streams (result file container) (optional))
   4: data_sources (if the stream is null then we need to get the file path from the data sources)
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "RigidTransformationProvider"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecRigidTransformation(self._op)
         self.outputs = _OutputSpecRigidTransformation(self._op)

def rigid_transformation():
    return _RigidTransformation()

#internal name: EPELY
#scripting name: elastic_strain_Y
def _get_input_spec_elastic_strain_Y(pin):
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
    return inputs_dict_elastic_strain_Y[pin]

def _get_output_spec_elastic_strain_Y(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_Y = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_Y[pin]

class _InputSpecElasticStrainY(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain_Y(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain_Y(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain_Y(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_Y(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain_Y(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain_Y(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain_Y(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain_Y(17), 17, op, -1) 

class _OutputSpecElasticStrainY(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_Y(0), 0, op) 

class _ElasticStrainY:
    """Operator's description:
Internal name is "EPELY"
Scripting name is "elastic_strain_Y"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPELY")
- using dpf.operators.result.elastic_strain_Y()

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
"""
    def __init__(self):
         self._name = "EPELY"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainY(self._op)
         self.outputs = _OutputSpecElasticStrainY(self._op)

def elastic_strain_Y():
    return _ElasticStrainY()

#internal name: ElementalMass
#scripting name: elemental_mass
def _get_input_spec_elemental_mass(pin):
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
    return inputs_dict_elemental_mass[pin]

def _get_output_spec_elemental_mass(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_mass = { 
        0 : outpin0
    }
    return outputs_dict_elemental_mass[pin]

class _InputSpecElementalMass(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elemental_mass(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elemental_mass(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elemental_mass(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elemental_mass(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elemental_mass(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elemental_mass(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elemental_mass(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elemental_mass(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elemental_mass(17), 17, op, -1) 

class _OutputSpecElementalMass(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elemental_mass(0), 0, op) 

class _ElementalMass:
    """Operator's description:
Internal name is "ElementalMass"
Scripting name is "elemental_mass"

This operator can be instantiated in both following ways:
- using dpf.Operator("ElementalMass")
- using dpf.operators.result.elemental_mass()

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
"""
    def __init__(self):
         self._name = "ElementalMass"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalMass(self._op)
         self.outputs = _OutputSpecElementalMass(self._op)

def elemental_mass():
    return _ElementalMass()

#internal name: ENG_CO
#scripting name: co_energy
def _get_input_spec_co_energy(pin):
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
    return inputs_dict_co_energy[pin]

def _get_output_spec_co_energy(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_co_energy = { 
        0 : outpin0
    }
    return outputs_dict_co_energy[pin]

class _InputSpecCoEnergy(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_co_energy(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_co_energy(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_co_energy(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_co_energy(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_co_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_co_energy(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_co_energy(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_co_energy(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_co_energy(17), 17, op, -1) 

class _OutputSpecCoEnergy(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_co_energy(0), 0, op) 

class _CoEnergy:
    """Operator's description:
Internal name is "ENG_CO"
Scripting name is "co_energy"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENG_CO")
- using dpf.operators.result.co_energy()

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
"""
    def __init__(self):
         self._name = "ENG_CO"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCoEnergy(self._op)
         self.outputs = _OutputSpecCoEnergy(self._op)

def co_energy():
    return _CoEnergy()

#internal name: EPELZ
#scripting name: elastic_strain_Z
def _get_input_spec_elastic_strain_Z(pin):
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
    return inputs_dict_elastic_strain_Z[pin]

def _get_output_spec_elastic_strain_Z(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_Z = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_Z[pin]

class _InputSpecElasticStrainZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain_Z(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain_Z(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain_Z(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_Z(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain_Z(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain_Z(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain_Z(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain_Z(17), 17, op, -1) 

class _OutputSpecElasticStrainZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_Z(0), 0, op) 

class _ElasticStrainZ:
    """Operator's description:
Internal name is "EPELZ"
Scripting name is "elastic_strain_Z"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPELZ")
- using dpf.operators.result.elastic_strain_Z()

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
"""
    def __init__(self):
         self._name = "EPELZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainZ(self._op)
         self.outputs = _OutputSpecElasticStrainZ(self._op)

def elastic_strain_Z():
    return _ElasticStrainZ()

#internal name: S
#scripting name: stress
def _get_input_spec_stress(pin):
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
    return inputs_dict_stress[pin]

def _get_output_spec_stress(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress = { 
        0 : outpin0
    }
    return outputs_dict_stress[pin]

class _InputSpecStress(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress(17), 17, op, -1) 

class _OutputSpecStress(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress(0), 0, op) 

class _Stress:
    """Operator's description:
Internal name is "S"
Scripting name is "stress"

This operator can be instantiated in both following ways:
- using dpf.Operator("S")
- using dpf.operators.result.stress()

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
"""
    def __init__(self):
         self._name = "S"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStress(self._op)
         self.outputs = _OutputSpecStress(self._op)

def stress():
    return _Stress()

#internal name: SX
#scripting name: stress_X
def _get_input_spec_stress_X(pin):
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
    return inputs_dict_stress_X[pin]

def _get_output_spec_stress_X(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_X = { 
        0 : outpin0
    }
    return outputs_dict_stress_X[pin]

class _InputSpecStressX(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_X(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_X(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_X(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_X(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_X(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_X(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_X(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_X(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_X(17), 17, op, -1) 

class _OutputSpecStressX(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_X(0), 0, op) 

class _StressX:
    """Operator's description:
Internal name is "SX"
Scripting name is "stress_X"

This operator can be instantiated in both following ways:
- using dpf.Operator("SX")
- using dpf.operators.result.stress_X()

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
"""
    def __init__(self):
         self._name = "SX"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressX(self._op)
         self.outputs = _OutputSpecStressX(self._op)

def stress_X():
    return _StressX()

#internal name: SY
#scripting name: stress_Y
def _get_input_spec_stress_Y(pin):
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
    return inputs_dict_stress_Y[pin]

def _get_output_spec_stress_Y(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_Y = { 
        0 : outpin0
    }
    return outputs_dict_stress_Y[pin]

class _InputSpecStressY(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_Y(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_Y(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_Y(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_Y(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_Y(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_Y(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_Y(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_Y(17), 17, op, -1) 

class _OutputSpecStressY(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_Y(0), 0, op) 

class _StressY:
    """Operator's description:
Internal name is "SY"
Scripting name is "stress_Y"

This operator can be instantiated in both following ways:
- using dpf.Operator("SY")
- using dpf.operators.result.stress_Y()

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
"""
    def __init__(self):
         self._name = "SY"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressY(self._op)
         self.outputs = _OutputSpecStressY(self._op)

def stress_Y():
    return _StressY()

#internal name: SZ
#scripting name: stress_Z
def _get_input_spec_stress_Z(pin):
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
    return inputs_dict_stress_Z[pin]

def _get_output_spec_stress_Z(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_Z = { 
        0 : outpin0
    }
    return outputs_dict_stress_Z[pin]

class _InputSpecStressZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_Z(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_Z(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_Z(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_Z(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_Z(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_Z(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_Z(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_Z(17), 17, op, -1) 

class _OutputSpecStressZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_Z(0), 0, op) 

class _StressZ:
    """Operator's description:
Internal name is "SZ"
Scripting name is "stress_Z"

This operator can be instantiated in both following ways:
- using dpf.Operator("SZ")
- using dpf.operators.result.stress_Z()

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
"""
    def __init__(self):
         self._name = "SZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressZ(self._op)
         self.outputs = _OutputSpecStressZ(self._op)

def stress_Z():
    return _StressZ()

#internal name: SXY
#scripting name: stress_XY
def _get_input_spec_stress_XY(pin):
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
    return inputs_dict_stress_XY[pin]

def _get_output_spec_stress_XY(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_XY = { 
        0 : outpin0
    }
    return outputs_dict_stress_XY[pin]

class _InputSpecStressXY(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_XY(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_XY(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_XY(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_XY(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_XY(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_XY(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_XY(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_XY(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_XY(17), 17, op, -1) 

class _OutputSpecStressXY(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_XY(0), 0, op) 

class _StressXY:
    """Operator's description:
Internal name is "SXY"
Scripting name is "stress_XY"

This operator can be instantiated in both following ways:
- using dpf.Operator("SXY")
- using dpf.operators.result.stress_XY()

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
"""
    def __init__(self):
         self._name = "SXY"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressXY(self._op)
         self.outputs = _OutputSpecStressXY(self._op)

def stress_XY():
    return _StressXY()

#internal name: SYZ
#scripting name: stress_YZ
def _get_input_spec_stress_YZ(pin):
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
    return inputs_dict_stress_YZ[pin]

def _get_output_spec_stress_YZ(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_YZ = { 
        0 : outpin0
    }
    return outputs_dict_stress_YZ[pin]

class _InputSpecStressYZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_YZ(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_YZ(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_YZ(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_YZ(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_YZ(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_YZ(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_YZ(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_YZ(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_YZ(17), 17, op, -1) 

class _OutputSpecStressYZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_YZ(0), 0, op) 

class _StressYZ:
    """Operator's description:
Internal name is "SYZ"
Scripting name is "stress_YZ"

This operator can be instantiated in both following ways:
- using dpf.Operator("SYZ")
- using dpf.operators.result.stress_YZ()

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
"""
    def __init__(self):
         self._name = "SYZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressYZ(self._op)
         self.outputs = _OutputSpecStressYZ(self._op)

def stress_YZ():
    return _StressYZ()

#internal name: ModalBasis
#scripting name: modal_basis
def _get_input_spec_modal_basis(pin):
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
    return inputs_dict_modal_basis[pin]

def _get_output_spec_modal_basis(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_modal_basis = { 
        0 : outpin0
    }
    return outputs_dict_modal_basis[pin]

class _InputSpecModalBasis(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_modal_basis(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_modal_basis(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_modal_basis(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_modal_basis(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_modal_basis(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_modal_basis(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_modal_basis(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_modal_basis(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_modal_basis(17), 17, op, -1) 

class _OutputSpecModalBasis(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_modal_basis(0), 0, op) 

class _ModalBasis:
    """Operator's description:
Internal name is "ModalBasis"
Scripting name is "modal_basis"

This operator can be instantiated in both following ways:
- using dpf.Operator("ModalBasis")
- using dpf.operators.result.modal_basis()

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
"""
    def __init__(self):
         self._name = "ModalBasis"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecModalBasis(self._op)
         self.outputs = _OutputSpecModalBasis(self._op)

def modal_basis():
    return _ModalBasis()

#internal name: SXZ
#scripting name: stress_XZ
def _get_input_spec_stress_XZ(pin):
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
    return inputs_dict_stress_XZ[pin]

def _get_output_spec_stress_XZ(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_XZ = { 
        0 : outpin0
    }
    return outputs_dict_stress_XZ[pin]

class _InputSpecStressXZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_XZ(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_XZ(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_XZ(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_XZ(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_XZ(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_XZ(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_XZ(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_XZ(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_XZ(17), 17, op, -1) 

class _OutputSpecStressXZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_XZ(0), 0, op) 

class _StressXZ:
    """Operator's description:
Internal name is "SXZ"
Scripting name is "stress_XZ"

This operator can be instantiated in both following ways:
- using dpf.Operator("SXZ")
- using dpf.operators.result.stress_XZ()

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
"""
    def __init__(self):
         self._name = "SXZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressXZ(self._op)
         self.outputs = _OutputSpecStressXZ(self._op)

def stress_XZ():
    return _StressXZ()

#internal name: S1
#scripting name: stress_principal_1
def _get_input_spec_stress_principal_1(pin):
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
    return inputs_dict_stress_principal_1[pin]

def _get_output_spec_stress_principal_1(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_principal_1 = { 
        0 : outpin0
    }
    return outputs_dict_stress_principal_1[pin]

class _InputSpecStressPrincipal1(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_principal_1(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_principal_1(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_principal_1(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_principal_1(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_principal_1(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_principal_1(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_principal_1(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_principal_1(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_principal_1(17), 17, op, -1) 

class _OutputSpecStressPrincipal1(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_principal_1(0), 0, op) 

class _StressPrincipal1:
    """Operator's description:
Internal name is "S1"
Scripting name is "stress_principal_1"

This operator can be instantiated in both following ways:
- using dpf.Operator("S1")
- using dpf.operators.result.stress_principal_1()

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
"""
    def __init__(self):
         self._name = "S1"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressPrincipal1(self._op)
         self.outputs = _OutputSpecStressPrincipal1(self._op)

def stress_principal_1():
    return _StressPrincipal1()

#internal name: S2
#scripting name: stress_principal_2
def _get_input_spec_stress_principal_2(pin):
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
    return inputs_dict_stress_principal_2[pin]

def _get_output_spec_stress_principal_2(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_principal_2 = { 
        0 : outpin0
    }
    return outputs_dict_stress_principal_2[pin]

class _InputSpecStressPrincipal2(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_principal_2(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_principal_2(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_principal_2(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_principal_2(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_principal_2(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_principal_2(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_principal_2(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_principal_2(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_principal_2(17), 17, op, -1) 

class _OutputSpecStressPrincipal2(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_principal_2(0), 0, op) 

class _StressPrincipal2:
    """Operator's description:
Internal name is "S2"
Scripting name is "stress_principal_2"

This operator can be instantiated in both following ways:
- using dpf.Operator("S2")
- using dpf.operators.result.stress_principal_2()

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
"""
    def __init__(self):
         self._name = "S2"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressPrincipal2(self._op)
         self.outputs = _OutputSpecStressPrincipal2(self._op)

def stress_principal_2():
    return _StressPrincipal2()

#internal name: S3
#scripting name: stress_principal_3
def _get_input_spec_stress_principal_3(pin):
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
    return inputs_dict_stress_principal_3[pin]

def _get_output_spec_stress_principal_3(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_principal_3 = { 
        0 : outpin0
    }
    return outputs_dict_stress_principal_3[pin]

class _InputSpecStressPrincipal3(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_principal_3(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_principal_3(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_principal_3(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_principal_3(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_principal_3(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_principal_3(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_principal_3(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_principal_3(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_principal_3(17), 17, op, -1) 

class _OutputSpecStressPrincipal3(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_principal_3(0), 0, op) 

class _StressPrincipal3:
    """Operator's description:
Internal name is "S3"
Scripting name is "stress_principal_3"

This operator can be instantiated in both following ways:
- using dpf.Operator("S3")
- using dpf.operators.result.stress_principal_3()

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
"""
    def __init__(self):
         self._name = "S3"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressPrincipal3(self._op)
         self.outputs = _OutputSpecStressPrincipal3(self._op)

def stress_principal_3():
    return _StressPrincipal3()

#internal name: EPEL
#scripting name: elastic_strain
def _get_input_spec_elastic_strain(pin):
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
    return inputs_dict_elastic_strain[pin]

def _get_output_spec_elastic_strain(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain[pin]

class _InputSpecElasticStrain(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain(17), 17, op, -1) 

class _OutputSpecElasticStrain(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain(0), 0, op) 

class _ElasticStrain:
    """Operator's description:
Internal name is "EPEL"
Scripting name is "elastic_strain"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPEL")
- using dpf.operators.result.elastic_strain()

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
"""
    def __init__(self):
         self._name = "EPEL"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrain(self._op)
         self.outputs = _OutputSpecElasticStrain(self._op)

def elastic_strain():
    return _ElasticStrain()

#internal name: EPELX
#scripting name: elastic_strain_X
def _get_input_spec_elastic_strain_X(pin):
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
    return inputs_dict_elastic_strain_X[pin]

def _get_output_spec_elastic_strain_X(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_X = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_X[pin]

class _InputSpecElasticStrainX(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain_X(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain_X(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain_X(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_X(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_X(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain_X(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain_X(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain_X(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain_X(17), 17, op, -1) 

class _OutputSpecElasticStrainX(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_X(0), 0, op) 

class _ElasticStrainX:
    """Operator's description:
Internal name is "EPELX"
Scripting name is "elastic_strain_X"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPELX")
- using dpf.operators.result.elastic_strain_X()

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
"""
    def __init__(self):
         self._name = "EPELX"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainX(self._op)
         self.outputs = _OutputSpecElasticStrainX(self._op)

def elastic_strain_X():
    return _ElasticStrainX()

#internal name: EPELXY
#scripting name: elastic_strain_XY
def _get_input_spec_elastic_strain_XY(pin):
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
    return inputs_dict_elastic_strain_XY[pin]

def _get_output_spec_elastic_strain_XY(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_XY = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_XY[pin]

class _InputSpecElasticStrainXY(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain_XY(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain_XY(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain_XY(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_XY(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_XY(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain_XY(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain_XY(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain_XY(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain_XY(17), 17, op, -1) 

class _OutputSpecElasticStrainXY(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_XY(0), 0, op) 

class _ElasticStrainXY:
    """Operator's description:
Internal name is "EPELXY"
Scripting name is "elastic_strain_XY"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPELXY")
- using dpf.operators.result.elastic_strain_XY()

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
"""
    def __init__(self):
         self._name = "EPELXY"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainXY(self._op)
         self.outputs = _OutputSpecElasticStrainXY(self._op)

def elastic_strain_XY():
    return _ElasticStrainXY()

#internal name: EPELYZ
#scripting name: elastic_strain_YZ
def _get_input_spec_elastic_strain_YZ(pin):
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
    return inputs_dict_elastic_strain_YZ[pin]

def _get_output_spec_elastic_strain_YZ(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_YZ = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_YZ[pin]

class _InputSpecElasticStrainYZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain_YZ(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain_YZ(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain_YZ(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_YZ(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_YZ(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain_YZ(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain_YZ(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain_YZ(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain_YZ(17), 17, op, -1) 

class _OutputSpecElasticStrainYZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_YZ(0), 0, op) 

class _ElasticStrainYZ:
    """Operator's description:
Internal name is "EPELYZ"
Scripting name is "elastic_strain_YZ"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPELYZ")
- using dpf.operators.result.elastic_strain_YZ()

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
"""
    def __init__(self):
         self._name = "EPELYZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainYZ(self._op)
         self.outputs = _OutputSpecElasticStrainYZ(self._op)

def elastic_strain_YZ():
    return _ElasticStrainYZ()

#internal name: EPELXZ
#scripting name: elastic_strain_XZ
def _get_input_spec_elastic_strain_XZ(pin):
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
    return inputs_dict_elastic_strain_XZ[pin]

def _get_output_spec_elastic_strain_XZ(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_XZ = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_XZ[pin]

class _InputSpecElasticStrainXZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain_XZ(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain_XZ(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain_XZ(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_XZ(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_XZ(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain_XZ(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain_XZ(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain_XZ(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain_XZ(17), 17, op, -1) 

class _OutputSpecElasticStrainXZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_XZ(0), 0, op) 

class _ElasticStrainXZ:
    """Operator's description:
Internal name is "EPELXZ"
Scripting name is "elastic_strain_XZ"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPELXZ")
- using dpf.operators.result.elastic_strain_XZ()

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
"""
    def __init__(self):
         self._name = "EPELXZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainXZ(self._op)
         self.outputs = _OutputSpecElasticStrainXZ(self._op)

def elastic_strain_XZ():
    return _ElasticStrainXZ()

#internal name: EPEL1
#scripting name: elastic_strain_principal_1
def _get_input_spec_elastic_strain_principal_1(pin):
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
    return inputs_dict_elastic_strain_principal_1[pin]

def _get_output_spec_elastic_strain_principal_1(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_principal_1 = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_principal_1[pin]

class _InputSpecElasticStrainPrincipal1(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain_principal_1(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain_principal_1(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain_principal_1(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_principal_1(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_principal_1(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain_principal_1(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain_principal_1(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain_principal_1(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain_principal_1(17), 17, op, -1) 

class _OutputSpecElasticStrainPrincipal1(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_principal_1(0), 0, op) 

class _ElasticStrainPrincipal1:
    """Operator's description:
Internal name is "EPEL1"
Scripting name is "elastic_strain_principal_1"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPEL1")
- using dpf.operators.result.elastic_strain_principal_1()

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
"""
    def __init__(self):
         self._name = "EPEL1"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainPrincipal1(self._op)
         self.outputs = _OutputSpecElasticStrainPrincipal1(self._op)

def elastic_strain_principal_1():
    return _ElasticStrainPrincipal1()

#internal name: EPEL2
#scripting name: elastic_strain_principal_2
def _get_input_spec_elastic_strain_principal_2(pin):
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
    return inputs_dict_elastic_strain_principal_2[pin]

def _get_output_spec_elastic_strain_principal_2(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_principal_2 = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_principal_2[pin]

class _InputSpecElasticStrainPrincipal2(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain_principal_2(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain_principal_2(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain_principal_2(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_principal_2(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_principal_2(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain_principal_2(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain_principal_2(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain_principal_2(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain_principal_2(17), 17, op, -1) 

class _OutputSpecElasticStrainPrincipal2(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_principal_2(0), 0, op) 

class _ElasticStrainPrincipal2:
    """Operator's description:
Internal name is "EPEL2"
Scripting name is "elastic_strain_principal_2"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPEL2")
- using dpf.operators.result.elastic_strain_principal_2()

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
"""
    def __init__(self):
         self._name = "EPEL2"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainPrincipal2(self._op)
         self.outputs = _OutputSpecElasticStrainPrincipal2(self._op)

def elastic_strain_principal_2():
    return _ElasticStrainPrincipal2()

#internal name: EPEL3
#scripting name: elastic_strain_principal_3
def _get_input_spec_elastic_strain_principal_3(pin):
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
    return inputs_dict_elastic_strain_principal_3[pin]

def _get_output_spec_elastic_strain_principal_3(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_principal_3 = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_principal_3[pin]

class _InputSpecElasticStrainPrincipal3(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain_principal_3(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain_principal_3(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain_principal_3(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_principal_3(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_principal_3(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain_principal_3(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain_principal_3(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain_principal_3(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain_principal_3(17), 17, op, -1) 

class _OutputSpecElasticStrainPrincipal3(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_principal_3(0), 0, op) 

class _ElasticStrainPrincipal3:
    """Operator's description:
Internal name is "EPEL3"
Scripting name is "elastic_strain_principal_3"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPEL3")
- using dpf.operators.result.elastic_strain_principal_3()

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
"""
    def __init__(self):
         self._name = "EPEL3"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainPrincipal3(self._op)
         self.outputs = _OutputSpecElasticStrainPrincipal3(self._op)

def elastic_strain_principal_3():
    return _ElasticStrainPrincipal3()

#internal name: EPPL
#scripting name: plastic_strain
def _get_input_spec_plastic_strain(pin):
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
    return inputs_dict_plastic_strain[pin]

def _get_output_spec_plastic_strain(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain[pin]

class _InputSpecPlasticStrain(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain(17), 17, op, -1) 

class _OutputSpecPlasticStrain(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain(0), 0, op) 

class _PlasticStrain:
    """Operator's description:
Internal name is "EPPL"
Scripting name is "plastic_strain"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPPL")
- using dpf.operators.result.plastic_strain()

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
"""
    def __init__(self):
         self._name = "EPPL"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrain(self._op)
         self.outputs = _OutputSpecPlasticStrain(self._op)

def plastic_strain():
    return _PlasticStrain()

#internal name: EPPLX
#scripting name: plastic_strain_X
def _get_input_spec_plastic_strain_X(pin):
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
    return inputs_dict_plastic_strain_X[pin]

def _get_output_spec_plastic_strain_X(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_X = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_X[pin]

class _InputSpecPlasticStrainX(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain_X(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain_X(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain_X(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_X(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_X(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain_X(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain_X(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain_X(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain_X(17), 17, op, -1) 

class _OutputSpecPlasticStrainX(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_X(0), 0, op) 

class _PlasticStrainX:
    """Operator's description:
Internal name is "EPPLX"
Scripting name is "plastic_strain_X"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPPLX")
- using dpf.operators.result.plastic_strain_X()

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
"""
    def __init__(self):
         self._name = "EPPLX"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainX(self._op)
         self.outputs = _OutputSpecPlasticStrainX(self._op)

def plastic_strain_X():
    return _PlasticStrainX()

#internal name: EPPLY
#scripting name: plastic_strain_Y
def _get_input_spec_plastic_strain_Y(pin):
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
    return inputs_dict_plastic_strain_Y[pin]

def _get_output_spec_plastic_strain_Y(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_Y = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_Y[pin]

class _InputSpecPlasticStrainY(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain_Y(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain_Y(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain_Y(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_Y(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain_Y(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain_Y(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain_Y(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain_Y(17), 17, op, -1) 

class _OutputSpecPlasticStrainY(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_Y(0), 0, op) 

class _PlasticStrainY:
    """Operator's description:
Internal name is "EPPLY"
Scripting name is "plastic_strain_Y"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPPLY")
- using dpf.operators.result.plastic_strain_Y()

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
"""
    def __init__(self):
         self._name = "EPPLY"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainY(self._op)
         self.outputs = _OutputSpecPlasticStrainY(self._op)

def plastic_strain_Y():
    return _PlasticStrainY()

#internal name: EPPLZ
#scripting name: plastic_strain_Z
def _get_input_spec_plastic_strain_Z(pin):
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
    return inputs_dict_plastic_strain_Z[pin]

def _get_output_spec_plastic_strain_Z(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_Z = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_Z[pin]

class _InputSpecPlasticStrainZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain_Z(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain_Z(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain_Z(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_Z(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain_Z(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain_Z(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain_Z(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain_Z(17), 17, op, -1) 

class _OutputSpecPlasticStrainZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_Z(0), 0, op) 

class _PlasticStrainZ:
    """Operator's description:
Internal name is "EPPLZ"
Scripting name is "plastic_strain_Z"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPPLZ")
- using dpf.operators.result.plastic_strain_Z()

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
"""
    def __init__(self):
         self._name = "EPPLZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainZ(self._op)
         self.outputs = _OutputSpecPlasticStrainZ(self._op)

def plastic_strain_Z():
    return _PlasticStrainZ()

#internal name: ENL_HPRES
#scripting name: hydrostatic_pressure
def _get_input_spec_hydrostatic_pressure(pin):
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
    return inputs_dict_hydrostatic_pressure[pin]

def _get_output_spec_hydrostatic_pressure(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_hydrostatic_pressure = { 
        0 : outpin0
    }
    return outputs_dict_hydrostatic_pressure[pin]

class _InputSpecHydrostaticPressure(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_hydrostatic_pressure(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_hydrostatic_pressure(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_hydrostatic_pressure(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_hydrostatic_pressure(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_hydrostatic_pressure(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_hydrostatic_pressure(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_hydrostatic_pressure(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_hydrostatic_pressure(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_hydrostatic_pressure(17), 17, op, -1) 

class _OutputSpecHydrostaticPressure(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_hydrostatic_pressure(0), 0, op) 

class _HydrostaticPressure:
    """Operator's description:
Internal name is "ENL_HPRES"
Scripting name is "hydrostatic_pressure"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENL_HPRES")
- using dpf.operators.result.hydrostatic_pressure()

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
"""
    def __init__(self):
         self._name = "ENL_HPRES"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecHydrostaticPressure(self._op)
         self.outputs = _OutputSpecHydrostaticPressure(self._op)

def hydrostatic_pressure():
    return _HydrostaticPressure()

#internal name: EPPLXY
#scripting name: plastic_strain_XY
def _get_input_spec_plastic_strain_XY(pin):
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
    return inputs_dict_plastic_strain_XY[pin]

def _get_output_spec_plastic_strain_XY(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_XY = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_XY[pin]

class _InputSpecPlasticStrainXY(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain_XY(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain_XY(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain_XY(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_XY(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_XY(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain_XY(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain_XY(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain_XY(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain_XY(17), 17, op, -1) 

class _OutputSpecPlasticStrainXY(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_XY(0), 0, op) 

class _PlasticStrainXY:
    """Operator's description:
Internal name is "EPPLXY"
Scripting name is "plastic_strain_XY"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPPLXY")
- using dpf.operators.result.plastic_strain_XY()

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
"""
    def __init__(self):
         self._name = "EPPLXY"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainXY(self._op)
         self.outputs = _OutputSpecPlasticStrainXY(self._op)

def plastic_strain_XY():
    return _PlasticStrainXY()

#internal name: EPPLYZ
#scripting name: plastic_strain_YZ
def _get_input_spec_plastic_strain_YZ(pin):
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
    return inputs_dict_plastic_strain_YZ[pin]

def _get_output_spec_plastic_strain_YZ(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_YZ = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_YZ[pin]

class _InputSpecPlasticStrainYZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain_YZ(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain_YZ(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain_YZ(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_YZ(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_YZ(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain_YZ(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain_YZ(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain_YZ(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain_YZ(17), 17, op, -1) 

class _OutputSpecPlasticStrainYZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_YZ(0), 0, op) 

class _PlasticStrainYZ:
    """Operator's description:
Internal name is "EPPLYZ"
Scripting name is "plastic_strain_YZ"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPPLYZ")
- using dpf.operators.result.plastic_strain_YZ()

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
"""
    def __init__(self):
         self._name = "EPPLYZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainYZ(self._op)
         self.outputs = _OutputSpecPlasticStrainYZ(self._op)

def plastic_strain_YZ():
    return _PlasticStrainYZ()

#internal name: EPPLXZ
#scripting name: plastic_strain_XZ
def _get_input_spec_plastic_strain_XZ(pin):
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
    return inputs_dict_plastic_strain_XZ[pin]

def _get_output_spec_plastic_strain_XZ(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_XZ = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_XZ[pin]

class _InputSpecPlasticStrainXZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain_XZ(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain_XZ(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain_XZ(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_XZ(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_XZ(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain_XZ(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain_XZ(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain_XZ(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain_XZ(17), 17, op, -1) 

class _OutputSpecPlasticStrainXZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_XZ(0), 0, op) 

class _PlasticStrainXZ:
    """Operator's description:
Internal name is "EPPLXZ"
Scripting name is "plastic_strain_XZ"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPPLXZ")
- using dpf.operators.result.plastic_strain_XZ()

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
"""
    def __init__(self):
         self._name = "EPPLXZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainXZ(self._op)
         self.outputs = _OutputSpecPlasticStrainXZ(self._op)

def plastic_strain_XZ():
    return _PlasticStrainXZ()

#internal name: EPPL2
#scripting name: plastic_strain_principal_2
def _get_input_spec_plastic_strain_principal_2(pin):
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
    return inputs_dict_plastic_strain_principal_2[pin]

def _get_output_spec_plastic_strain_principal_2(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_principal_2 = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_principal_2[pin]

class _InputSpecPlasticStrainPrincipal2(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain_principal_2(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain_principal_2(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain_principal_2(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_principal_2(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_principal_2(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain_principal_2(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain_principal_2(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain_principal_2(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain_principal_2(17), 17, op, -1) 

class _OutputSpecPlasticStrainPrincipal2(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_principal_2(0), 0, op) 

class _PlasticStrainPrincipal2:
    """Operator's description:
Internal name is "EPPL2"
Scripting name is "plastic_strain_principal_2"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPPL2")
- using dpf.operators.result.plastic_strain_principal_2()

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
"""
    def __init__(self):
         self._name = "EPPL2"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainPrincipal2(self._op)
         self.outputs = _OutputSpecPlasticStrainPrincipal2(self._op)

def plastic_strain_principal_2():
    return _PlasticStrainPrincipal2()

#internal name: EPPL3
#scripting name: plastic_strain_principal_3
def _get_input_spec_plastic_strain_principal_3(pin):
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
    return inputs_dict_plastic_strain_principal_3[pin]

def _get_output_spec_plastic_strain_principal_3(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_principal_3 = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_principal_3[pin]

class _InputSpecPlasticStrainPrincipal3(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain_principal_3(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain_principal_3(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain_principal_3(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_principal_3(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_principal_3(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain_principal_3(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain_principal_3(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain_principal_3(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain_principal_3(17), 17, op, -1) 

class _OutputSpecPlasticStrainPrincipal3(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_principal_3(0), 0, op) 

class _PlasticStrainPrincipal3:
    """Operator's description:
Internal name is "EPPL3"
Scripting name is "plastic_strain_principal_3"

This operator can be instantiated in both following ways:
- using dpf.Operator("EPPL3")
- using dpf.operators.result.plastic_strain_principal_3()

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
"""
    def __init__(self):
         self._name = "EPPL3"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainPrincipal3(self._op)
         self.outputs = _OutputSpecPlasticStrainPrincipal3(self._op)

def plastic_strain_principal_3():
    return _PlasticStrainPrincipal3()

#internal name: A
#scripting name: acceleration
def _get_input_spec_acceleration(pin):
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
    return inputs_dict_acceleration[pin]

def _get_output_spec_acceleration(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_acceleration = { 
        0 : outpin0
    }
    return outputs_dict_acceleration[pin]

class _InputSpecAcceleration(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_acceleration(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_acceleration(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_acceleration(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_acceleration(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_acceleration(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_acceleration(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_acceleration(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_acceleration(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_acceleration(17), 17, op, -1) 

class _OutputSpecAcceleration(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_acceleration(0), 0, op) 

class _Acceleration:
    """Operator's description:
Internal name is "A"
Scripting name is "acceleration"

This operator can be instantiated in both following ways:
- using dpf.Operator("A")
- using dpf.operators.result.acceleration()

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
"""
    def __init__(self):
         self._name = "A"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAcceleration(self._op)
         self.outputs = _OutputSpecAcceleration(self._op)

def acceleration():
    return _Acceleration()

#internal name: AX
#scripting name: acceleration_X
def _get_input_spec_acceleration_X(pin):
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
    return inputs_dict_acceleration_X[pin]

def _get_output_spec_acceleration_X(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_acceleration_X = { 
        0 : outpin0
    }
    return outputs_dict_acceleration_X[pin]

class _InputSpecAccelerationX(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_acceleration_X(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_acceleration_X(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_acceleration_X(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_acceleration_X(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_acceleration_X(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_acceleration_X(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_acceleration_X(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_acceleration_X(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_acceleration_X(17), 17, op, -1) 

class _OutputSpecAccelerationX(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_acceleration_X(0), 0, op) 

class _AccelerationX:
    """Operator's description:
Internal name is "AX"
Scripting name is "acceleration_X"

This operator can be instantiated in both following ways:
- using dpf.Operator("AX")
- using dpf.operators.result.acceleration_X()

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
"""
    def __init__(self):
         self._name = "AX"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAccelerationX(self._op)
         self.outputs = _OutputSpecAccelerationX(self._op)

def acceleration_X():
    return _AccelerationX()

#internal name: AY
#scripting name: acceleration_Y
def _get_input_spec_acceleration_Y(pin):
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
    return inputs_dict_acceleration_Y[pin]

def _get_output_spec_acceleration_Y(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_acceleration_Y = { 
        0 : outpin0
    }
    return outputs_dict_acceleration_Y[pin]

class _InputSpecAccelerationY(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_acceleration_Y(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_acceleration_Y(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_acceleration_Y(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_acceleration_Y(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_acceleration_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_acceleration_Y(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_acceleration_Y(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_acceleration_Y(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_acceleration_Y(17), 17, op, -1) 

class _OutputSpecAccelerationY(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_acceleration_Y(0), 0, op) 

class _AccelerationY:
    """Operator's description:
Internal name is "AY"
Scripting name is "acceleration_Y"

This operator can be instantiated in both following ways:
- using dpf.Operator("AY")
- using dpf.operators.result.acceleration_Y()

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
"""
    def __init__(self):
         self._name = "AY"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAccelerationY(self._op)
         self.outputs = _OutputSpecAccelerationY(self._op)

def acceleration_Y():
    return _AccelerationY()

#internal name: AZ
#scripting name: acceleration_Z
def _get_input_spec_acceleration_Z(pin):
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
    return inputs_dict_acceleration_Z[pin]

def _get_output_spec_acceleration_Z(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_acceleration_Z = { 
        0 : outpin0
    }
    return outputs_dict_acceleration_Z[pin]

class _InputSpecAccelerationZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_acceleration_Z(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_acceleration_Z(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_acceleration_Z(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_acceleration_Z(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_acceleration_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_acceleration_Z(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_acceleration_Z(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_acceleration_Z(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_acceleration_Z(17), 17, op, -1) 

class _OutputSpecAccelerationZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_acceleration_Z(0), 0, op) 

class _AccelerationZ:
    """Operator's description:
Internal name is "AZ"
Scripting name is "acceleration_Z"

This operator can be instantiated in both following ways:
- using dpf.Operator("AZ")
- using dpf.operators.result.acceleration_Z()

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
"""
    def __init__(self):
         self._name = "AZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAccelerationZ(self._op)
         self.outputs = _OutputSpecAccelerationZ(self._op)

def acceleration_Z():
    return _AccelerationZ()

#internal name: RF
#scripting name: reaction_force
def _get_input_spec_reaction_force(pin):
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
    return inputs_dict_reaction_force[pin]

def _get_output_spec_reaction_force(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_reaction_force = { 
        0 : outpin0
    }
    return outputs_dict_reaction_force[pin]

class _InputSpecReactionForce(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_reaction_force(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_reaction_force(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_reaction_force(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_reaction_force(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_reaction_force(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_reaction_force(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_reaction_force(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_reaction_force(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_reaction_force(17), 17, op, -1) 

class _OutputSpecReactionForce(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_reaction_force(0), 0, op) 

class _ReactionForce:
    """Operator's description:
Internal name is "RF"
Scripting name is "reaction_force"

This operator can be instantiated in both following ways:
- using dpf.Operator("RF")
- using dpf.operators.result.reaction_force()

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
"""
    def __init__(self):
         self._name = "RF"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecReactionForce(self._op)
         self.outputs = _OutputSpecReactionForce(self._op)

def reaction_force():
    return _ReactionForce()

#internal name: V
#scripting name: velocity
def _get_input_spec_velocity(pin):
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
    return inputs_dict_velocity[pin]

def _get_output_spec_velocity(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_velocity = { 
        0 : outpin0
    }
    return outputs_dict_velocity[pin]

class _InputSpecVelocity(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_velocity(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_velocity(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_velocity(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_velocity(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_velocity(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_velocity(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_velocity(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_velocity(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_velocity(17), 17, op, -1) 

class _OutputSpecVelocity(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_velocity(0), 0, op) 

class _Velocity:
    """Operator's description:
Internal name is "V"
Scripting name is "velocity"

This operator can be instantiated in both following ways:
- using dpf.Operator("V")
- using dpf.operators.result.velocity()

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
"""
    def __init__(self):
         self._name = "V"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecVelocity(self._op)
         self.outputs = _OutputSpecVelocity(self._op)

def velocity():
    return _Velocity()

#internal name: VX
#scripting name: velocity_X
def _get_input_spec_velocity_X(pin):
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
    return inputs_dict_velocity_X[pin]

def _get_output_spec_velocity_X(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_velocity_X = { 
        0 : outpin0
    }
    return outputs_dict_velocity_X[pin]

class _InputSpecVelocityX(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_velocity_X(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_velocity_X(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_velocity_X(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_velocity_X(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_velocity_X(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_velocity_X(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_velocity_X(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_velocity_X(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_velocity_X(17), 17, op, -1) 

class _OutputSpecVelocityX(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_velocity_X(0), 0, op) 

class _VelocityX:
    """Operator's description:
Internal name is "VX"
Scripting name is "velocity_X"

This operator can be instantiated in both following ways:
- using dpf.Operator("VX")
- using dpf.operators.result.velocity_X()

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
"""
    def __init__(self):
         self._name = "VX"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecVelocityX(self._op)
         self.outputs = _OutputSpecVelocityX(self._op)

def velocity_X():
    return _VelocityX()

#internal name: VY
#scripting name: velocity_Y
def _get_input_spec_velocity_Y(pin):
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
    return inputs_dict_velocity_Y[pin]

def _get_output_spec_velocity_Y(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_velocity_Y = { 
        0 : outpin0
    }
    return outputs_dict_velocity_Y[pin]

class _InputSpecVelocityY(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_velocity_Y(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_velocity_Y(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_velocity_Y(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_velocity_Y(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_velocity_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_velocity_Y(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_velocity_Y(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_velocity_Y(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_velocity_Y(17), 17, op, -1) 

class _OutputSpecVelocityY(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_velocity_Y(0), 0, op) 

class _VelocityY:
    """Operator's description:
Internal name is "VY"
Scripting name is "velocity_Y"

This operator can be instantiated in both following ways:
- using dpf.Operator("VY")
- using dpf.operators.result.velocity_Y()

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
"""
    def __init__(self):
         self._name = "VY"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecVelocityY(self._op)
         self.outputs = _OutputSpecVelocityY(self._op)

def velocity_Y():
    return _VelocityY()

#internal name: VZ
#scripting name: velocity_Z
def _get_input_spec_velocity_Z(pin):
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
    return inputs_dict_velocity_Z[pin]

def _get_output_spec_velocity_Z(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_velocity_Z = { 
        0 : outpin0
    }
    return outputs_dict_velocity_Z[pin]

class _InputSpecVelocityZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_velocity_Z(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_velocity_Z(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_velocity_Z(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_velocity_Z(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_velocity_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_velocity_Z(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_velocity_Z(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_velocity_Z(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_velocity_Z(17), 17, op, -1) 

class _OutputSpecVelocityZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_velocity_Z(0), 0, op) 

class _VelocityZ:
    """Operator's description:
Internal name is "VZ"
Scripting name is "velocity_Z"

This operator can be instantiated in both following ways:
- using dpf.Operator("VZ")
- using dpf.operators.result.velocity_Z()

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
"""
    def __init__(self):
         self._name = "VZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecVelocityZ(self._op)
         self.outputs = _OutputSpecVelocityZ(self._op)

def velocity_Z():
    return _VelocityZ()

#internal name: U
#scripting name: displacement
def _get_input_spec_displacement(pin):
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
    return inputs_dict_displacement[pin]

def _get_output_spec_displacement(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_displacement = { 
        0 : outpin0
    }
    return outputs_dict_displacement[pin]

class _InputSpecDisplacement(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_displacement(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_displacement(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_displacement(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_displacement(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_displacement(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_displacement(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_displacement(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_displacement(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_displacement(17), 17, op, -1) 

class _OutputSpecDisplacement(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_displacement(0), 0, op) 

class _Displacement:
    """Operator's description:
Internal name is "U"
Scripting name is "displacement"

This operator can be instantiated in both following ways:
- using dpf.Operator("U")
- using dpf.operators.result.displacement()

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
"""
    def __init__(self):
         self._name = "U"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecDisplacement(self._op)
         self.outputs = _OutputSpecDisplacement(self._op)

def displacement():
    return _Displacement()

#internal name: UX
#scripting name: displacement_X
def _get_input_spec_displacement_X(pin):
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
    return inputs_dict_displacement_X[pin]

def _get_output_spec_displacement_X(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_displacement_X = { 
        0 : outpin0
    }
    return outputs_dict_displacement_X[pin]

class _InputSpecDisplacementX(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_displacement_X(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_displacement_X(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_displacement_X(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_displacement_X(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_displacement_X(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_displacement_X(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_displacement_X(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_displacement_X(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_displacement_X(17), 17, op, -1) 

class _OutputSpecDisplacementX(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_displacement_X(0), 0, op) 

class _DisplacementX:
    """Operator's description:
Internal name is "UX"
Scripting name is "displacement_X"

This operator can be instantiated in both following ways:
- using dpf.Operator("UX")
- using dpf.operators.result.displacement_X()

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
"""
    def __init__(self):
         self._name = "UX"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecDisplacementX(self._op)
         self.outputs = _OutputSpecDisplacementX(self._op)

def displacement_X():
    return _DisplacementX()

#internal name: UY
#scripting name: displacement_Y
def _get_input_spec_displacement_Y(pin):
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
    return inputs_dict_displacement_Y[pin]

def _get_output_spec_displacement_Y(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_displacement_Y = { 
        0 : outpin0
    }
    return outputs_dict_displacement_Y[pin]

class _InputSpecDisplacementY(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_displacement_Y(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_displacement_Y(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_displacement_Y(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_displacement_Y(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_displacement_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_displacement_Y(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_displacement_Y(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_displacement_Y(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_displacement_Y(17), 17, op, -1) 

class _OutputSpecDisplacementY(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_displacement_Y(0), 0, op) 

class _DisplacementY:
    """Operator's description:
Internal name is "UY"
Scripting name is "displacement_Y"

This operator can be instantiated in both following ways:
- using dpf.Operator("UY")
- using dpf.operators.result.displacement_Y()

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
"""
    def __init__(self):
         self._name = "UY"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecDisplacementY(self._op)
         self.outputs = _OutputSpecDisplacementY(self._op)

def displacement_Y():
    return _DisplacementY()

#internal name: UZ
#scripting name: displacement_Z
def _get_input_spec_displacement_Z(pin):
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
    return inputs_dict_displacement_Z[pin]

def _get_output_spec_displacement_Z(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_displacement_Z = { 
        0 : outpin0
    }
    return outputs_dict_displacement_Z[pin]

class _InputSpecDisplacementZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_displacement_Z(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_displacement_Z(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_displacement_Z(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_displacement_Z(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_displacement_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_displacement_Z(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_displacement_Z(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_displacement_Z(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_displacement_Z(17), 17, op, -1) 

class _OutputSpecDisplacementZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_displacement_Z(0), 0, op) 

class _DisplacementZ:
    """Operator's description:
Internal name is "UZ"
Scripting name is "displacement_Z"

This operator can be instantiated in both following ways:
- using dpf.Operator("UZ")
- using dpf.operators.result.displacement_Z()

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
"""
    def __init__(self):
         self._name = "UZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecDisplacementZ(self._op)
         self.outputs = _OutputSpecDisplacementZ(self._op)

def displacement_Z():
    return _DisplacementZ()

#internal name: TF
#scripting name: heat_flux
def _get_input_spec_heat_flux(pin):
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
    return inputs_dict_heat_flux[pin]

def _get_output_spec_heat_flux(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_heat_flux = { 
        0 : outpin0
    }
    return outputs_dict_heat_flux[pin]

class _InputSpecHeatFlux(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_heat_flux(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_heat_flux(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_heat_flux(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_heat_flux(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_heat_flux(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_heat_flux(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_heat_flux(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_heat_flux(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_heat_flux(17), 17, op, -1) 

class _OutputSpecHeatFlux(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_heat_flux(0), 0, op) 

class _HeatFlux:
    """Operator's description:
Internal name is "TF"
Scripting name is "heat_flux"

This operator can be instantiated in both following ways:
- using dpf.Operator("TF")
- using dpf.operators.result.heat_flux()

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
"""
    def __init__(self):
         self._name = "TF"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecHeatFlux(self._op)
         self.outputs = _OutputSpecHeatFlux(self._op)

def heat_flux():
    return _HeatFlux()

#internal name: TFX
#scripting name: heat_flux_X
def _get_input_spec_heat_flux_X(pin):
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
    return inputs_dict_heat_flux_X[pin]

def _get_output_spec_heat_flux_X(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_heat_flux_X = { 
        0 : outpin0
    }
    return outputs_dict_heat_flux_X[pin]

class _InputSpecHeatFluxX(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_heat_flux_X(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_heat_flux_X(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_heat_flux_X(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_heat_flux_X(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_heat_flux_X(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_heat_flux_X(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_heat_flux_X(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_heat_flux_X(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_heat_flux_X(17), 17, op, -1) 

class _OutputSpecHeatFluxX(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_heat_flux_X(0), 0, op) 

class _HeatFluxX:
    """Operator's description:
Internal name is "TFX"
Scripting name is "heat_flux_X"

This operator can be instantiated in both following ways:
- using dpf.Operator("TFX")
- using dpf.operators.result.heat_flux_X()

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
"""
    def __init__(self):
         self._name = "TFX"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecHeatFluxX(self._op)
         self.outputs = _OutputSpecHeatFluxX(self._op)

def heat_flux_X():
    return _HeatFluxX()

#internal name: EF
#scripting name: electric_field
def _get_input_spec_electric_field(pin):
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
    return inputs_dict_electric_field[pin]

def _get_output_spec_electric_field(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_electric_field = { 
        0 : outpin0
    }
    return outputs_dict_electric_field[pin]

class _InputSpecElectricField(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_electric_field(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_electric_field(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_electric_field(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_electric_field(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_electric_field(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_electric_field(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_electric_field(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_electric_field(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_electric_field(17), 17, op, -1) 

class _OutputSpecElectricField(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_electric_field(0), 0, op) 

class _ElectricField:
    """Operator's description:
Internal name is "EF"
Scripting name is "electric_field"

This operator can be instantiated in both following ways:
- using dpf.Operator("EF")
- using dpf.operators.result.electric_field()

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
"""
    def __init__(self):
         self._name = "EF"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElectricField(self._op)
         self.outputs = _OutputSpecElectricField(self._op)

def electric_field():
    return _ElectricField()

#internal name: TFY
#scripting name: heat_flux_Y
def _get_input_spec_heat_flux_Y(pin):
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
    return inputs_dict_heat_flux_Y[pin]

def _get_output_spec_heat_flux_Y(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_heat_flux_Y = { 
        0 : outpin0
    }
    return outputs_dict_heat_flux_Y[pin]

class _InputSpecHeatFluxY(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_heat_flux_Y(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_heat_flux_Y(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_heat_flux_Y(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_heat_flux_Y(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_heat_flux_Y(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_heat_flux_Y(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_heat_flux_Y(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_heat_flux_Y(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_heat_flux_Y(17), 17, op, -1) 

class _OutputSpecHeatFluxY(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_heat_flux_Y(0), 0, op) 

class _HeatFluxY:
    """Operator's description:
Internal name is "TFY"
Scripting name is "heat_flux_Y"

This operator can be instantiated in both following ways:
- using dpf.Operator("TFY")
- using dpf.operators.result.heat_flux_Y()

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
"""
    def __init__(self):
         self._name = "TFY"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecHeatFluxY(self._op)
         self.outputs = _OutputSpecHeatFluxY(self._op)

def heat_flux_Y():
    return _HeatFluxY()

#internal name: TFZ
#scripting name: heat_flux_Z
def _get_input_spec_heat_flux_Z(pin):
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
    return inputs_dict_heat_flux_Z[pin]

def _get_output_spec_heat_flux_Z(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_heat_flux_Z = { 
        0 : outpin0
    }
    return outputs_dict_heat_flux_Z[pin]

class _InputSpecHeatFluxZ(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_heat_flux_Z(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_heat_flux_Z(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_heat_flux_Z(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_heat_flux_Z(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_heat_flux_Z(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_heat_flux_Z(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_heat_flux_Z(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_heat_flux_Z(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_heat_flux_Z(17), 17, op, -1) 

class _OutputSpecHeatFluxZ(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_heat_flux_Z(0), 0, op) 

class _HeatFluxZ:
    """Operator's description:
Internal name is "TFZ"
Scripting name is "heat_flux_Z"

This operator can be instantiated in both following ways:
- using dpf.Operator("TFZ")
- using dpf.operators.result.heat_flux_Z()

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
"""
    def __init__(self):
         self._name = "TFZ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecHeatFluxZ(self._op)
         self.outputs = _OutputSpecHeatFluxZ(self._op)

def heat_flux_Z():
    return _HeatFluxZ()

#internal name: ENF
#scripting name: element_nodal_forces
def _get_input_spec_element_nodal_forces(pin):
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
    return inputs_dict_element_nodal_forces[pin]

def _get_output_spec_element_nodal_forces(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_element_nodal_forces = { 
        0 : outpin0
    }
    return outputs_dict_element_nodal_forces[pin]

class _InputSpecElementNodalForces(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_element_nodal_forces(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_element_nodal_forces(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_element_nodal_forces(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_element_nodal_forces(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_element_nodal_forces(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_element_nodal_forces(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_element_nodal_forces(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_element_nodal_forces(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_element_nodal_forces(17), 17, op, -1) 

class _OutputSpecElementNodalForces(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_element_nodal_forces(0), 0, op) 

class _ElementNodalForces:
    """Operator's description:
Internal name is "ENF"
Scripting name is "element_nodal_forces"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENF")
- using dpf.operators.result.element_nodal_forces()

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
"""
    def __init__(self):
         self._name = "ENF"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementNodalForces(self._op)
         self.outputs = _OutputSpecElementNodalForces(self._op)

def element_nodal_forces():
    return _ElementNodalForces()

#internal name: BFE
#scripting name: structural_temperature
def _get_input_spec_structural_temperature(pin):
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
    return inputs_dict_structural_temperature[pin]

def _get_output_spec_structural_temperature(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_structural_temperature = { 
        0 : outpin0
    }
    return outputs_dict_structural_temperature[pin]

class _InputSpecStructuralTemperature(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_structural_temperature(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_structural_temperature(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_structural_temperature(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_structural_temperature(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_structural_temperature(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_structural_temperature(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_structural_temperature(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_structural_temperature(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_structural_temperature(17), 17, op, -1) 

class _OutputSpecStructuralTemperature(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_structural_temperature(0), 0, op) 

class _StructuralTemperature:
    """Operator's description:
Internal name is "BFE"
Scripting name is "structural_temperature"

This operator can be instantiated in both following ways:
- using dpf.Operator("BFE")
- using dpf.operators.result.structural_temperature()

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
"""
    def __init__(self):
         self._name = "BFE"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStructuralTemperature(self._op)
         self.outputs = _OutputSpecStructuralTemperature(self._op)

def structural_temperature():
    return _StructuralTemperature()

#internal name: ENG_INC
#scripting name: incremental_energy
def _get_input_spec_incremental_energy(pin):
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
    return inputs_dict_incremental_energy[pin]

def _get_output_spec_incremental_energy(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_incremental_energy = { 
        0 : outpin0
    }
    return outputs_dict_incremental_energy[pin]

class _InputSpecIncrementalEnergy(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_incremental_energy(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_incremental_energy(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_incremental_energy(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_incremental_energy(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_incremental_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_incremental_energy(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_incremental_energy(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_incremental_energy(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_incremental_energy(17), 17, op, -1) 

class _OutputSpecIncrementalEnergy(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_incremental_energy(0), 0, op) 

class _IncrementalEnergy:
    """Operator's description:
Internal name is "ENG_INC"
Scripting name is "incremental_energy"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENG_INC")
- using dpf.operators.result.incremental_energy()

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
"""
    def __init__(self):
         self._name = "ENG_INC"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecIncrementalEnergy(self._op)
         self.outputs = _OutputSpecIncrementalEnergy(self._op)

def incremental_energy():
    return _IncrementalEnergy()

#internal name: ENG_SE
#scripting name: stiffness_matrix_energy
def _get_input_spec_stiffness_matrix_energy(pin):
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
    return inputs_dict_stiffness_matrix_energy[pin]

def _get_output_spec_stiffness_matrix_energy(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stiffness_matrix_energy = { 
        0 : outpin0
    }
    return outputs_dict_stiffness_matrix_energy[pin]

class _InputSpecStiffnessMatrixEnergy(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stiffness_matrix_energy(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stiffness_matrix_energy(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stiffness_matrix_energy(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stiffness_matrix_energy(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stiffness_matrix_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stiffness_matrix_energy(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stiffness_matrix_energy(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stiffness_matrix_energy(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stiffness_matrix_energy(17), 17, op, -1) 

class _OutputSpecStiffnessMatrixEnergy(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stiffness_matrix_energy(0), 0, op) 

class _StiffnessMatrixEnergy:
    """Operator's description:
Internal name is "ENG_SE"
Scripting name is "stiffness_matrix_energy"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENG_SE")
- using dpf.operators.result.stiffness_matrix_energy()

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
"""
    def __init__(self):
         self._name = "ENG_SE"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStiffnessMatrixEnergy(self._op)
         self.outputs = _OutputSpecStiffnessMatrixEnergy(self._op)

def stiffness_matrix_energy():
    return _StiffnessMatrixEnergy()

#internal name: ETH
#scripting name: thermal_strain
def _get_input_spec_thermal_strain(pin):
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
    return inputs_dict_thermal_strain[pin]

def _get_output_spec_thermal_strain(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_thermal_strain = { 
        0 : outpin0
    }
    return outputs_dict_thermal_strain[pin]

class _InputSpecThermalStrain(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_thermal_strain(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_thermal_strain(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_thermal_strain(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_thermal_strain(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_thermal_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_thermal_strain(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_thermal_strain(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_thermal_strain(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_thermal_strain(17), 17, op, -1) 

class _OutputSpecThermalStrain(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_thermal_strain(0), 0, op) 

class _ThermalStrain:
    """Operator's description:
Internal name is "ETH"
Scripting name is "thermal_strain"

This operator can be instantiated in both following ways:
- using dpf.Operator("ETH")
- using dpf.operators.result.thermal_strain()

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
"""
    def __init__(self):
         self._name = "ETH"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecThermalStrain(self._op)
         self.outputs = _OutputSpecThermalStrain(self._op)

def thermal_strain():
    return _ThermalStrain()

#internal name: ENL_SEPL
#scripting name: eqv_stress_parameter
def _get_input_spec_eqv_stress_parameter(pin):
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
    return inputs_dict_eqv_stress_parameter[pin]

def _get_output_spec_eqv_stress_parameter(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_eqv_stress_parameter = { 
        0 : outpin0
    }
    return outputs_dict_eqv_stress_parameter[pin]

class _InputSpecEqvStressParameter(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_eqv_stress_parameter(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_eqv_stress_parameter(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_eqv_stress_parameter(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_eqv_stress_parameter(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_eqv_stress_parameter(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_eqv_stress_parameter(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_eqv_stress_parameter(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_eqv_stress_parameter(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_eqv_stress_parameter(17), 17, op, -1) 

class _OutputSpecEqvStressParameter(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_eqv_stress_parameter(0), 0, op) 

class _EqvStressParameter:
    """Operator's description:
Internal name is "ENL_SEPL"
Scripting name is "eqv_stress_parameter"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENL_SEPL")
- using dpf.operators.result.eqv_stress_parameter()

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
"""
    def __init__(self):
         self._name = "ENL_SEPL"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecEqvStressParameter(self._op)
         self.outputs = _OutputSpecEqvStressParameter(self._op)

def eqv_stress_parameter():
    return _EqvStressParameter()

#internal name: ENL_SRAT
#scripting name: stress_ratio
def _get_input_spec_stress_ratio(pin):
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
    return inputs_dict_stress_ratio[pin]

def _get_output_spec_stress_ratio(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_ratio = { 
        0 : outpin0
    }
    return outputs_dict_stress_ratio[pin]

class _InputSpecStressRatio(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_ratio(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_ratio(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_ratio(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_ratio(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_ratio(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_ratio(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_ratio(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_ratio(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_ratio(17), 17, op, -1) 

class _OutputSpecStressRatio(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_ratio(0), 0, op) 

class _StressRatio:
    """Operator's description:
Internal name is "ENL_SRAT"
Scripting name is "stress_ratio"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENL_SRAT")
- using dpf.operators.result.stress_ratio()

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
"""
    def __init__(self):
         self._name = "ENL_SRAT"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressRatio(self._op)
         self.outputs = _OutputSpecStressRatio(self._op)

def stress_ratio():
    return _StressRatio()

#internal name: ENL_EPEQ
#scripting name: accu_eqv_plastic_strain
def _get_input_spec_accu_eqv_plastic_strain(pin):
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
    return inputs_dict_accu_eqv_plastic_strain[pin]

def _get_output_spec_accu_eqv_plastic_strain(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_accu_eqv_plastic_strain = { 
        0 : outpin0
    }
    return outputs_dict_accu_eqv_plastic_strain[pin]

class _InputSpecAccuEqvPlasticStrain(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_accu_eqv_plastic_strain(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_accu_eqv_plastic_strain(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_accu_eqv_plastic_strain(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_accu_eqv_plastic_strain(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_accu_eqv_plastic_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_accu_eqv_plastic_strain(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_accu_eqv_plastic_strain(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_accu_eqv_plastic_strain(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_accu_eqv_plastic_strain(17), 17, op, -1) 

class _OutputSpecAccuEqvPlasticStrain(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_accu_eqv_plastic_strain(0), 0, op) 

class _AccuEqvPlasticStrain:
    """Operator's description:
Internal name is "ENL_EPEQ"
Scripting name is "accu_eqv_plastic_strain"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENL_EPEQ")
- using dpf.operators.result.accu_eqv_plastic_strain()

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
"""
    def __init__(self):
         self._name = "ENL_EPEQ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAccuEqvPlasticStrain(self._op)
         self.outputs = _OutputSpecAccuEqvPlasticStrain(self._op)

def accu_eqv_plastic_strain():
    return _AccuEqvPlasticStrain()

#internal name: ENL_PSV
#scripting name: plastic_state_variable
def _get_input_spec_plastic_state_variable(pin):
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
    return inputs_dict_plastic_state_variable[pin]

def _get_output_spec_plastic_state_variable(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_state_variable = { 
        0 : outpin0
    }
    return outputs_dict_plastic_state_variable[pin]

class _InputSpecPlasticStateVariable(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_state_variable(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_state_variable(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_state_variable(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_state_variable(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_state_variable(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_state_variable(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_state_variable(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_state_variable(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_state_variable(17), 17, op, -1) 

class _OutputSpecPlasticStateVariable(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_state_variable(0), 0, op) 

class _PlasticStateVariable:
    """Operator's description:
Internal name is "ENL_PSV"
Scripting name is "plastic_state_variable"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENL_PSV")
- using dpf.operators.result.plastic_state_variable()

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
"""
    def __init__(self):
         self._name = "ENL_PSV"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStateVariable(self._op)
         self.outputs = _OutputSpecPlasticStateVariable(self._op)

def plastic_state_variable():
    return _PlasticStateVariable()

#internal name: ENL_CREQ
#scripting name: accu_eqv_creep_strain
def _get_input_spec_accu_eqv_creep_strain(pin):
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
    return inputs_dict_accu_eqv_creep_strain[pin]

def _get_output_spec_accu_eqv_creep_strain(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_accu_eqv_creep_strain = { 
        0 : outpin0
    }
    return outputs_dict_accu_eqv_creep_strain[pin]

class _InputSpecAccuEqvCreepStrain(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_accu_eqv_creep_strain(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_accu_eqv_creep_strain(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_accu_eqv_creep_strain(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_accu_eqv_creep_strain(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_accu_eqv_creep_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_accu_eqv_creep_strain(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_accu_eqv_creep_strain(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_accu_eqv_creep_strain(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_accu_eqv_creep_strain(17), 17, op, -1) 

class _OutputSpecAccuEqvCreepStrain(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_accu_eqv_creep_strain(0), 0, op) 

class _AccuEqvCreepStrain:
    """Operator's description:
Internal name is "ENL_CREQ"
Scripting name is "accu_eqv_creep_strain"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENL_CREQ")
- using dpf.operators.result.accu_eqv_creep_strain()

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
"""
    def __init__(self):
         self._name = "ENL_CREQ"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAccuEqvCreepStrain(self._op)
         self.outputs = _OutputSpecAccuEqvCreepStrain(self._op)

def accu_eqv_creep_strain():
    return _AccuEqvCreepStrain()

#internal name: ENL_PLWK
#scripting name: plastic_strain_energy_density
def _get_input_spec_plastic_strain_energy_density(pin):
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
    return inputs_dict_plastic_strain_energy_density[pin]

def _get_output_spec_plastic_strain_energy_density(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_energy_density = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_energy_density[pin]

class _InputSpecPlasticStrainEnergyDensity(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_plastic_strain_energy_density(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_plastic_strain_energy_density(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_plastic_strain_energy_density(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_energy_density(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_energy_density(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_plastic_strain_energy_density(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_plastic_strain_energy_density(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_plastic_strain_energy_density(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_plastic_strain_energy_density(17), 17, op, -1) 

class _OutputSpecPlasticStrainEnergyDensity(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_energy_density(0), 0, op) 

class _PlasticStrainEnergyDensity:
    """Operator's description:
Internal name is "ENL_PLWK"
Scripting name is "plastic_strain_energy_density"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENL_PLWK")
- using dpf.operators.result.plastic_strain_energy_density()

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
"""
    def __init__(self):
         self._name = "ENL_PLWK"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainEnergyDensity(self._op)
         self.outputs = _OutputSpecPlasticStrainEnergyDensity(self._op)

def plastic_strain_energy_density():
    return _PlasticStrainEnergyDensity()

#internal name: MaterialPropertyOfElement
#scripting name: material_property_of_element
def _get_input_spec_material_property_of_element(pin):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_material_property_of_element = { 
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_material_property_of_element[pin]

def _get_output_spec_material_property_of_element(pin):
    outpin0 = _PinSpecification(name = "material_properties", type_names = ["field"], document = """material properties""")
    outputs_dict_material_property_of_element = { 
        0 : outpin0
    }
    return outputs_dict_material_property_of_element[pin]

class _InputSpecMaterialPropertyOfElement(_Inputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Input(_get_input_spec_material_property_of_element(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_material_property_of_element(4), 4, op, -1) 

class _OutputSpecMaterialPropertyOfElement(_Outputs):
    def __init__(self, op: _Operator):
        self.material_properties = _Output(_get_output_spec_material_property_of_element(0), 0, op) 

class _MaterialPropertyOfElement:
    """Operator's description:
Internal name is "MaterialPropertyOfElement"
Scripting name is "material_property_of_element"

This operator can be instantiated in both following ways:
- using dpf.Operator("MaterialPropertyOfElement")
- using dpf.operators.result.material_property_of_element()

Input list: 
   3: streams_container 
   4: data_sources 
Output list: 
   0: material_properties (material properties)
"""
    def __init__(self):
         self._name = "MaterialPropertyOfElement"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecMaterialPropertyOfElement(self._op)
         self.outputs = _OutputSpecMaterialPropertyOfElement(self._op)

def material_property_of_element():
    return _MaterialPropertyOfElement()

#internal name: ENL_CRWK
#scripting name: creep_strain_energy_density
def _get_input_spec_creep_strain_energy_density(pin):
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
    return inputs_dict_creep_strain_energy_density[pin]

def _get_output_spec_creep_strain_energy_density(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_creep_strain_energy_density = { 
        0 : outpin0
    }
    return outputs_dict_creep_strain_energy_density[pin]

class _InputSpecCreepStrainEnergyDensity(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_creep_strain_energy_density(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_creep_strain_energy_density(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_creep_strain_energy_density(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_creep_strain_energy_density(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_creep_strain_energy_density(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_creep_strain_energy_density(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_creep_strain_energy_density(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_creep_strain_energy_density(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_creep_strain_energy_density(17), 17, op, -1) 

class _OutputSpecCreepStrainEnergyDensity(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_creep_strain_energy_density(0), 0, op) 

class _CreepStrainEnergyDensity:
    """Operator's description:
Internal name is "ENL_CRWK"
Scripting name is "creep_strain_energy_density"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENL_CRWK")
- using dpf.operators.result.creep_strain_energy_density()

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
"""
    def __init__(self):
         self._name = "ENL_CRWK"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCreepStrainEnergyDensity(self._op)
         self.outputs = _OutputSpecCreepStrainEnergyDensity(self._op)

def creep_strain_energy_density():
    return _CreepStrainEnergyDensity()

#internal name: ENL_ELENG
#scripting name: elastic_strain_energy_density
def _get_input_spec_elastic_strain_energy_density(pin):
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
    return inputs_dict_elastic_strain_energy_density[pin]

def _get_output_spec_elastic_strain_energy_density(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_energy_density = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_energy_density[pin]

class _InputSpecElasticStrainEnergyDensity(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elastic_strain_energy_density(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elastic_strain_energy_density(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elastic_strain_energy_density(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_energy_density(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_energy_density(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elastic_strain_energy_density(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elastic_strain_energy_density(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elastic_strain_energy_density(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elastic_strain_energy_density(17), 17, op, -1) 

class _OutputSpecElasticStrainEnergyDensity(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_energy_density(0), 0, op) 

class _ElasticStrainEnergyDensity:
    """Operator's description:
Internal name is "ENL_ELENG"
Scripting name is "elastic_strain_energy_density"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENL_ELENG")
- using dpf.operators.result.elastic_strain_energy_density()

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
"""
    def __init__(self):
         self._name = "ENL_ELENG"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainEnergyDensity(self._op)
         self.outputs = _OutputSpecElasticStrainEnergyDensity(self._op)

def elastic_strain_energy_density():
    return _ElasticStrainEnergyDensity()

#internal name: ECT_STAT
#scripting name: contact_status
def _get_input_spec_contact_status(pin):
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
    return inputs_dict_contact_status[pin]

def _get_output_spec_contact_status(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_status = { 
        0 : outpin0
    }
    return outputs_dict_contact_status[pin]

class _InputSpecContactStatus(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_contact_status(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_contact_status(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_contact_status(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_contact_status(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_contact_status(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_contact_status(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_contact_status(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_contact_status(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_contact_status(17), 17, op, -1) 

class _OutputSpecContactStatus(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_contact_status(0), 0, op) 

class _ContactStatus:
    """Operator's description:
Internal name is "ECT_STAT"
Scripting name is "contact_status"

This operator can be instantiated in both following ways:
- using dpf.Operator("ECT_STAT")
- using dpf.operators.result.contact_status()

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
"""
    def __init__(self):
         self._name = "ECT_STAT"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecContactStatus(self._op)
         self.outputs = _OutputSpecContactStatus(self._op)

def contact_status():
    return _ContactStatus()

#internal name: ECT_PENE
#scripting name: contact_penetration
def _get_input_spec_contact_penetration(pin):
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
    return inputs_dict_contact_penetration[pin]

def _get_output_spec_contact_penetration(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_penetration = { 
        0 : outpin0
    }
    return outputs_dict_contact_penetration[pin]

class _InputSpecContactPenetration(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_contact_penetration(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_contact_penetration(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_contact_penetration(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_contact_penetration(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_contact_penetration(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_contact_penetration(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_contact_penetration(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_contact_penetration(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_contact_penetration(17), 17, op, -1) 

class _OutputSpecContactPenetration(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_contact_penetration(0), 0, op) 

class _ContactPenetration:
    """Operator's description:
Internal name is "ECT_PENE"
Scripting name is "contact_penetration"

This operator can be instantiated in both following ways:
- using dpf.Operator("ECT_PENE")
- using dpf.operators.result.contact_penetration()

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
"""
    def __init__(self):
         self._name = "ECT_PENE"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecContactPenetration(self._op)
         self.outputs = _OutputSpecContactPenetration(self._op)

def contact_penetration():
    return _ContactPenetration()

#internal name: ECT_PRES
#scripting name: contact_pressure
def _get_input_spec_contact_pressure(pin):
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
    return inputs_dict_contact_pressure[pin]

def _get_output_spec_contact_pressure(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_pressure = { 
        0 : outpin0
    }
    return outputs_dict_contact_pressure[pin]

class _InputSpecContactPressure(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_contact_pressure(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_contact_pressure(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_contact_pressure(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_contact_pressure(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_contact_pressure(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_contact_pressure(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_contact_pressure(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_contact_pressure(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_contact_pressure(17), 17, op, -1) 

class _OutputSpecContactPressure(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_contact_pressure(0), 0, op) 

class _ContactPressure:
    """Operator's description:
Internal name is "ECT_PRES"
Scripting name is "contact_pressure"

This operator can be instantiated in both following ways:
- using dpf.Operator("ECT_PRES")
- using dpf.operators.result.contact_pressure()

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
"""
    def __init__(self):
         self._name = "ECT_PRES"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecContactPressure(self._op)
         self.outputs = _OutputSpecContactPressure(self._op)

def contact_pressure():
    return _ContactPressure()

#internal name: ECT_SFRIC
#scripting name: contact_friction_stress
def _get_input_spec_contact_friction_stress(pin):
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
    return inputs_dict_contact_friction_stress[pin]

def _get_output_spec_contact_friction_stress(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_friction_stress = { 
        0 : outpin0
    }
    return outputs_dict_contact_friction_stress[pin]

class _InputSpecContactFrictionStress(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_contact_friction_stress(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_contact_friction_stress(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_contact_friction_stress(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_contact_friction_stress(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_contact_friction_stress(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_contact_friction_stress(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_contact_friction_stress(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_contact_friction_stress(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_contact_friction_stress(17), 17, op, -1) 

class _OutputSpecContactFrictionStress(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_contact_friction_stress(0), 0, op) 

class _ContactFrictionStress:
    """Operator's description:
Internal name is "ECT_SFRIC"
Scripting name is "contact_friction_stress"

This operator can be instantiated in both following ways:
- using dpf.Operator("ECT_SFRIC")
- using dpf.operators.result.contact_friction_stress()

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
"""
    def __init__(self):
         self._name = "ECT_SFRIC"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecContactFrictionStress(self._op)
         self.outputs = _OutputSpecContactFrictionStress(self._op)

def contact_friction_stress():
    return _ContactFrictionStress()

#internal name: ECT_STOT
#scripting name: contact_total_stress
def _get_input_spec_contact_total_stress(pin):
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
    return inputs_dict_contact_total_stress[pin]

def _get_output_spec_contact_total_stress(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_total_stress = { 
        0 : outpin0
    }
    return outputs_dict_contact_total_stress[pin]

class _InputSpecContactTotalStress(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_contact_total_stress(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_contact_total_stress(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_contact_total_stress(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_contact_total_stress(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_contact_total_stress(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_contact_total_stress(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_contact_total_stress(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_contact_total_stress(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_contact_total_stress(17), 17, op, -1) 

class _OutputSpecContactTotalStress(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_contact_total_stress(0), 0, op) 

class _ContactTotalStress:
    """Operator's description:
Internal name is "ECT_STOT"
Scripting name is "contact_total_stress"

This operator can be instantiated in both following ways:
- using dpf.Operator("ECT_STOT")
- using dpf.operators.result.contact_total_stress()

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
"""
    def __init__(self):
         self._name = "ECT_STOT"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecContactTotalStress(self._op)
         self.outputs = _OutputSpecContactTotalStress(self._op)

def contact_total_stress():
    return _ContactTotalStress()

#internal name: ECT_SLIDE
#scripting name: contact_sliding_distance
def _get_input_spec_contact_sliding_distance(pin):
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
    return inputs_dict_contact_sliding_distance[pin]

def _get_output_spec_contact_sliding_distance(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_sliding_distance = { 
        0 : outpin0
    }
    return outputs_dict_contact_sliding_distance[pin]

class _InputSpecContactSlidingDistance(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_contact_sliding_distance(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_contact_sliding_distance(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_contact_sliding_distance(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_contact_sliding_distance(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_contact_sliding_distance(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_contact_sliding_distance(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_contact_sliding_distance(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_contact_sliding_distance(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_contact_sliding_distance(17), 17, op, -1) 

class _OutputSpecContactSlidingDistance(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_contact_sliding_distance(0), 0, op) 

class _ContactSlidingDistance:
    """Operator's description:
Internal name is "ECT_SLIDE"
Scripting name is "contact_sliding_distance"

This operator can be instantiated in both following ways:
- using dpf.Operator("ECT_SLIDE")
- using dpf.operators.result.contact_sliding_distance()

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
"""
    def __init__(self):
         self._name = "ECT_SLIDE"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecContactSlidingDistance(self._op)
         self.outputs = _OutputSpecContactSlidingDistance(self._op)

def contact_sliding_distance():
    return _ContactSlidingDistance()

#internal name: ECT_GAP
#scripting name: contact_gap_distance
def _get_input_spec_contact_gap_distance(pin):
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
    return inputs_dict_contact_gap_distance[pin]

def _get_output_spec_contact_gap_distance(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_gap_distance = { 
        0 : outpin0
    }
    return outputs_dict_contact_gap_distance[pin]

class _InputSpecContactGapDistance(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_contact_gap_distance(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_contact_gap_distance(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_contact_gap_distance(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_contact_gap_distance(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_contact_gap_distance(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_contact_gap_distance(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_contact_gap_distance(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_contact_gap_distance(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_contact_gap_distance(17), 17, op, -1) 

class _OutputSpecContactGapDistance(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_contact_gap_distance(0), 0, op) 

class _ContactGapDistance:
    """Operator's description:
Internal name is "ECT_GAP"
Scripting name is "contact_gap_distance"

This operator can be instantiated in both following ways:
- using dpf.Operator("ECT_GAP")
- using dpf.operators.result.contact_gap_distance()

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
"""
    def __init__(self):
         self._name = "ECT_GAP"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecContactGapDistance(self._op)
         self.outputs = _OutputSpecContactGapDistance(self._op)

def contact_gap_distance():
    return _ContactGapDistance()

#internal name: ECT_FLUX
#scripting name: contact_surface_heat_flux
def _get_input_spec_contact_surface_heat_flux(pin):
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
    return inputs_dict_contact_surface_heat_flux[pin]

def _get_output_spec_contact_surface_heat_flux(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_surface_heat_flux = { 
        0 : outpin0
    }
    return outputs_dict_contact_surface_heat_flux[pin]

class _InputSpecContactSurfaceHeatFlux(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_contact_surface_heat_flux(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_contact_surface_heat_flux(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_contact_surface_heat_flux(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_contact_surface_heat_flux(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_contact_surface_heat_flux(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_contact_surface_heat_flux(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_contact_surface_heat_flux(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_contact_surface_heat_flux(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_contact_surface_heat_flux(17), 17, op, -1) 

class _OutputSpecContactSurfaceHeatFlux(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_contact_surface_heat_flux(0), 0, op) 

class _ContactSurfaceHeatFlux:
    """Operator's description:
Internal name is "ECT_FLUX"
Scripting name is "contact_surface_heat_flux"

This operator can be instantiated in both following ways:
- using dpf.Operator("ECT_FLUX")
- using dpf.operators.result.contact_surface_heat_flux()

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
"""
    def __init__(self):
         self._name = "ECT_FLUX"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecContactSurfaceHeatFlux(self._op)
         self.outputs = _OutputSpecContactSurfaceHeatFlux(self._op)

def contact_surface_heat_flux():
    return _ContactSurfaceHeatFlux()

#internal name: ECT_CNOS
#scripting name: num_surface_status_changes
def _get_input_spec_num_surface_status_changes(pin):
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
    return inputs_dict_num_surface_status_changes[pin]

def _get_output_spec_num_surface_status_changes(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_num_surface_status_changes = { 
        0 : outpin0
    }
    return outputs_dict_num_surface_status_changes[pin]

class _InputSpecNumSurfaceStatusChanges(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_num_surface_status_changes(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_num_surface_status_changes(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_num_surface_status_changes(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_num_surface_status_changes(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_num_surface_status_changes(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_num_surface_status_changes(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_num_surface_status_changes(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_num_surface_status_changes(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_num_surface_status_changes(17), 17, op, -1) 

class _OutputSpecNumSurfaceStatusChanges(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_num_surface_status_changes(0), 0, op) 

class _NumSurfaceStatusChanges:
    """Operator's description:
Internal name is "ECT_CNOS"
Scripting name is "num_surface_status_changes"

This operator can be instantiated in both following ways:
- using dpf.Operator("ECT_CNOS")
- using dpf.operators.result.num_surface_status_changes()

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
"""
    def __init__(self):
         self._name = "ECT_CNOS"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNumSurfaceStatusChanges(self._op)
         self.outputs = _OutputSpecNumSurfaceStatusChanges(self._op)

def num_surface_status_changes():
    return _NumSurfaceStatusChanges()

#internal name: ECT_FRES
#scripting name: contact_fluid_penetration_pressure
def _get_input_spec_contact_fluid_penetration_pressure(pin):
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
    return inputs_dict_contact_fluid_penetration_pressure[pin]

def _get_output_spec_contact_fluid_penetration_pressure(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_contact_fluid_penetration_pressure = { 
        0 : outpin0
    }
    return outputs_dict_contact_fluid_penetration_pressure[pin]

class _InputSpecContactFluidPenetrationPressure(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_contact_fluid_penetration_pressure(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_contact_fluid_penetration_pressure(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_contact_fluid_penetration_pressure(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_contact_fluid_penetration_pressure(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_contact_fluid_penetration_pressure(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_contact_fluid_penetration_pressure(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_contact_fluid_penetration_pressure(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_contact_fluid_penetration_pressure(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_contact_fluid_penetration_pressure(17), 17, op, -1) 

class _OutputSpecContactFluidPenetrationPressure(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_contact_fluid_penetration_pressure(0), 0, op) 

class _ContactFluidPenetrationPressure:
    """Operator's description:
Internal name is "ECT_FRES"
Scripting name is "contact_fluid_penetration_pressure"

This operator can be instantiated in both following ways:
- using dpf.Operator("ECT_FRES")
- using dpf.operators.result.contact_fluid_penetration_pressure()

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
"""
    def __init__(self):
         self._name = "ECT_FRES"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecContactFluidPenetrationPressure(self._op)
         self.outputs = _OutputSpecContactFluidPenetrationPressure(self._op)

def contact_fluid_penetration_pressure():
    return _ContactFluidPenetrationPressure()

#internal name: ENG_VOL
#scripting name: elemental_volume
def _get_input_spec_elemental_volume(pin):
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
    return inputs_dict_elemental_volume[pin]

def _get_output_spec_elemental_volume(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_volume = { 
        0 : outpin0
    }
    return outputs_dict_elemental_volume[pin]

class _InputSpecElementalVolume(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_elemental_volume(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_elemental_volume(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_elemental_volume(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elemental_volume(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elemental_volume(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_elemental_volume(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_elemental_volume(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_elemental_volume(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_elemental_volume(17), 17, op, -1) 

class _OutputSpecElementalVolume(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elemental_volume(0), 0, op) 

class _ElementalVolume:
    """Operator's description:
Internal name is "ENG_VOL"
Scripting name is "elemental_volume"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENG_VOL")
- using dpf.operators.result.elemental_volume()

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
"""
    def __init__(self):
         self._name = "ENG_VOL"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElementalVolume(self._op)
         self.outputs = _OutputSpecElementalVolume(self._op)

def elemental_volume():
    return _ElementalVolume()

#internal name: ENG_AHO
#scripting name: artificial_hourglass_energy
def _get_input_spec_artificial_hourglass_energy(pin):
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
    return inputs_dict_artificial_hourglass_energy[pin]

def _get_output_spec_artificial_hourglass_energy(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_artificial_hourglass_energy = { 
        0 : outpin0
    }
    return outputs_dict_artificial_hourglass_energy[pin]

class _InputSpecArtificialHourglassEnergy(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_artificial_hourglass_energy(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_artificial_hourglass_energy(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_artificial_hourglass_energy(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_artificial_hourglass_energy(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_artificial_hourglass_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_artificial_hourglass_energy(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_artificial_hourglass_energy(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_artificial_hourglass_energy(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_artificial_hourglass_energy(17), 17, op, -1) 

class _OutputSpecArtificialHourglassEnergy(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_artificial_hourglass_energy(0), 0, op) 

class _ArtificialHourglassEnergy:
    """Operator's description:
Internal name is "ENG_AHO"
Scripting name is "artificial_hourglass_energy"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENG_AHO")
- using dpf.operators.result.artificial_hourglass_energy()

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
"""
    def __init__(self):
         self._name = "ENG_AHO"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecArtificialHourglassEnergy(self._op)
         self.outputs = _OutputSpecArtificialHourglassEnergy(self._op)

def artificial_hourglass_energy():
    return _ArtificialHourglassEnergy()

#internal name: ENG_KE
#scripting name: kinetic_energy
def _get_input_spec_kinetic_energy(pin):
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
    return inputs_dict_kinetic_energy[pin]

def _get_output_spec_kinetic_energy(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_kinetic_energy = { 
        0 : outpin0
    }
    return outputs_dict_kinetic_energy[pin]

class _InputSpecKineticEnergy(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_kinetic_energy(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_kinetic_energy(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_kinetic_energy(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_kinetic_energy(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_kinetic_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_kinetic_energy(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_kinetic_energy(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_kinetic_energy(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_kinetic_energy(17), 17, op, -1) 

class _OutputSpecKineticEnergy(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_kinetic_energy(0), 0, op) 

class _KineticEnergy:
    """Operator's description:
Internal name is "ENG_KE"
Scripting name is "kinetic_energy"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENG_KE")
- using dpf.operators.result.kinetic_energy()

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
"""
    def __init__(self):
         self._name = "ENG_KE"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecKineticEnergy(self._op)
         self.outputs = _OutputSpecKineticEnergy(self._op)

def kinetic_energy():
    return _KineticEnergy()

#internal name: ENG_TH
#scripting name: thermal_dissipation_energy
def _get_input_spec_thermal_dissipation_energy(pin):
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
    return inputs_dict_thermal_dissipation_energy[pin]

def _get_output_spec_thermal_dissipation_energy(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_thermal_dissipation_energy = { 
        0 : outpin0
    }
    return outputs_dict_thermal_dissipation_energy[pin]

class _InputSpecThermalDissipationEnergy(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_thermal_dissipation_energy(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_thermal_dissipation_energy(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_thermal_dissipation_energy(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_thermal_dissipation_energy(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_thermal_dissipation_energy(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_thermal_dissipation_energy(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_thermal_dissipation_energy(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_thermal_dissipation_energy(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_thermal_dissipation_energy(17), 17, op, -1) 

class _OutputSpecThermalDissipationEnergy(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_thermal_dissipation_energy(0), 0, op) 

class _ThermalDissipationEnergy:
    """Operator's description:
Internal name is "ENG_TH"
Scripting name is "thermal_dissipation_energy"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENG_TH")
- using dpf.operators.result.thermal_dissipation_energy()

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
"""
    def __init__(self):
         self._name = "ENG_TH"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecThermalDissipationEnergy(self._op)
         self.outputs = _OutputSpecThermalDissipationEnergy(self._op)

def thermal_dissipation_energy():
    return _ThermalDissipationEnergy()

#internal name: F
#scripting name: nodal_force
def _get_input_spec_nodal_force(pin):
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
    return inputs_dict_nodal_force[pin]

def _get_output_spec_nodal_force(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_force = { 
        0 : outpin0
    }
    return outputs_dict_nodal_force[pin]

class _InputSpecNodalForce(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_force(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_force(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_force(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_force(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_force(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_nodal_force(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_force(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_nodal_force(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_nodal_force(17), 17, op, -1) 

class _OutputSpecNodalForce(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_force(0), 0, op) 

class _NodalForce:
    """Operator's description:
Internal name is "F"
Scripting name is "nodal_force"

This operator can be instantiated in both following ways:
- using dpf.Operator("F")
- using dpf.operators.result.nodal_force()

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
"""
    def __init__(self):
         self._name = "F"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalForce(self._op)
         self.outputs = _OutputSpecNodalForce(self._op)

def nodal_force():
    return _NodalForce()

#internal name: M
#scripting name: nodal_moment
def _get_input_spec_nodal_moment(pin):
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
    return inputs_dict_nodal_moment[pin]

def _get_output_spec_nodal_moment(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_moment = { 
        0 : outpin0
    }
    return outputs_dict_nodal_moment[pin]

class _InputSpecNodalMoment(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_moment(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_moment(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_moment(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_moment(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_moment(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_nodal_moment(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_moment(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_nodal_moment(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_nodal_moment(17), 17, op, -1) 

class _OutputSpecNodalMoment(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_moment(0), 0, op) 

class _NodalMoment:
    """Operator's description:
Internal name is "M"
Scripting name is "nodal_moment"

This operator can be instantiated in both following ways:
- using dpf.Operator("M")
- using dpf.operators.result.nodal_moment()

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
"""
    def __init__(self):
         self._name = "M"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalMoment(self._op)
         self.outputs = _OutputSpecNodalMoment(self._op)

def nodal_moment():
    return _NodalMoment()

#internal name: TEMP
#scripting name: temperature
def _get_input_spec_temperature(pin):
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
    return inputs_dict_temperature[pin]

def _get_output_spec_temperature(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_temperature = { 
        0 : outpin0
    }
    return outputs_dict_temperature[pin]

class _InputSpecTemperature(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_temperature(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_temperature(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_temperature(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_temperature(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_temperature(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_temperature(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_temperature(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_temperature(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_temperature(17), 17, op, -1) 

class _OutputSpecTemperature(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_temperature(0), 0, op) 

class _Temperature:
    """Operator's description:
Internal name is "TEMP"
Scripting name is "temperature"

This operator can be instantiated in both following ways:
- using dpf.Operator("TEMP")
- using dpf.operators.result.temperature()

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
"""
    def __init__(self):
         self._name = "TEMP"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecTemperature(self._op)
         self.outputs = _OutputSpecTemperature(self._op)

def temperature():
    return _Temperature()

#internal name: UTOT
#scripting name: raw_displacement
def _get_input_spec_raw_displacement(pin):
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
    return inputs_dict_raw_displacement[pin]

def _get_output_spec_raw_displacement(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_raw_displacement = { 
        0 : outpin0
    }
    return outputs_dict_raw_displacement[pin]

class _InputSpecRawDisplacement(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_raw_displacement(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_raw_displacement(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_raw_displacement(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_raw_displacement(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_raw_displacement(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_raw_displacement(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_raw_displacement(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_raw_displacement(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_raw_displacement(17), 17, op, -1) 

class _OutputSpecRawDisplacement(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_raw_displacement(0), 0, op) 

class _RawDisplacement:
    """Operator's description:
Internal name is "UTOT"
Scripting name is "raw_displacement"

This operator can be instantiated in both following ways:
- using dpf.Operator("UTOT")
- using dpf.operators.result.raw_displacement()

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
"""
    def __init__(self):
         self._name = "UTOT"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecRawDisplacement(self._op)
         self.outputs = _OutputSpecRawDisplacement(self._op)

def raw_displacement():
    return _RawDisplacement()

#internal name: RFTOT
#scripting name: raw_reaction_force
def _get_input_spec_raw_reaction_force(pin):
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
    return inputs_dict_raw_reaction_force[pin]

def _get_output_spec_raw_reaction_force(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_raw_reaction_force = { 
        0 : outpin0
    }
    return outputs_dict_raw_reaction_force[pin]

class _InputSpecRawReactionForce(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_raw_reaction_force(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_raw_reaction_force(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_raw_reaction_force(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_raw_reaction_force(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_raw_reaction_force(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_raw_reaction_force(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_raw_reaction_force(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_raw_reaction_force(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_raw_reaction_force(17), 17, op, -1) 

class _OutputSpecRawReactionForce(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_raw_reaction_force(0), 0, op) 

class _RawReactionForce:
    """Operator's description:
Internal name is "RFTOT"
Scripting name is "raw_reaction_force"

This operator can be instantiated in both following ways:
- using dpf.Operator("RFTOT")
- using dpf.operators.result.raw_reaction_force()

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
"""
    def __init__(self):
         self._name = "RFTOT"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecRawReactionForce(self._op)
         self.outputs = _OutputSpecRawReactionForce(self._op)

def raw_reaction_force():
    return _RawReactionForce()

#internal name: VOLT
#scripting name: electric_potential
def _get_input_spec_electric_potential(pin):
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
    return inputs_dict_electric_potential[pin]

def _get_output_spec_electric_potential(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_electric_potential = { 
        0 : outpin0
    }
    return outputs_dict_electric_potential[pin]

class _InputSpecElectricPotential(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_electric_potential(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_electric_potential(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_electric_potential(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_electric_potential(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_electric_potential(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_electric_potential(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_electric_potential(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_electric_potential(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_electric_potential(17), 17, op, -1) 

class _OutputSpecElectricPotential(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_electric_potential(0), 0, op) 

class _ElectricPotential:
    """Operator's description:
Internal name is "VOLT"
Scripting name is "electric_potential"

This operator can be instantiated in both following ways:
- using dpf.Operator("VOLT")
- using dpf.operators.result.electric_potential()

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
"""
    def __init__(self):
         self._name = "VOLT"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElectricPotential(self._op)
         self.outputs = _OutputSpecElectricPotential(self._op)

def electric_potential():
    return _ElectricPotential()

#internal name: S_eqv
#scripting name: stress_von_mises
def _get_input_spec_stress_von_mises(pin):
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
    return inputs_dict_stress_von_mises[pin]

def _get_output_spec_stress_von_mises(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_von_mises = { 
        0 : outpin0
    }
    return outputs_dict_stress_von_mises[pin]

class _InputSpecStressVonMises(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_stress_von_mises(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_stress_von_mises(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_stress_von_mises(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_von_mises(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_von_mises(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_stress_von_mises(5), 5, op, -1) 
        self.mesh = _Input(_get_input_spec_stress_von_mises(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_stress_von_mises(9), 9, op, -1) 
        self.domain_id = _Input(_get_input_spec_stress_von_mises(17), 17, op, -1) 

class _OutputSpecStressVonMises(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_von_mises(0), 0, op) 

class _StressVonMises:
    """Operator's description:
Internal name is "S_eqv"
Scripting name is "stress_von_mises"

This operator can be instantiated in both following ways:
- using dpf.Operator("S_eqv")
- using dpf.operators.result.stress_von_mises()

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
"""
    def __init__(self):
         self._name = "S_eqv"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressVonMises(self._op)
         self.outputs = _OutputSpecStressVonMises(self._op)

def stress_von_mises():
    return _StressVonMises()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "result" category
"""

#internal name: cyclic_expansion
#scripting name: cyclic_expansion
def _get_input_spec_cyclic_expansion(pin):
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
    return inputs_dict_cyclic_expansion[pin]

def _get_output_spec_cyclic_expansion(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_cyclic_expansion = { 
        0 : outpin0
    }
    return outputs_dict_cyclic_expansion[pin]

class _InputSpecCyclicExpansion(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_cyclic_expansion(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_cyclic_expansion(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_cyclic_expansion(2), 2, op, -1) 
        self.cyclic_support = _Input(_get_input_spec_cyclic_expansion(16), 16, op, -1) 

class _OutputSpecCyclicExpansion(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cyclic_expansion(0), 0, op) 

class _CyclicExpansion:
    """Operator's description:
Internal name is "cyclic_expansion"
Scripting name is "cyclic_expansion"

This operator can be instantiated in both following ways:
- using dpf.Operator("cyclic_expansion")
- using dpf.operators.result.cyclic_expansion()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (field container with the base and duplicate sectors)
   16: cyclic_support 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "cyclic_expansion"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCyclicExpansion(self._op)
         self.outputs = _OutputSpecCyclicExpansion(self._op)

def cyclic_expansion():
    return _CyclicExpansion()

#internal name: ERP
#scripting name: equivalent_radiated_power
def _get_input_spec_equivalent_radiated_power(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "meshed_region", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin have to be boundary or skin mesh""")
    inpin2 = _PinSpecification(name = "int32", type_names = ["int32"], optional = True, document = """load step number, if it's specified, the ERP is computed only on the substeps of this step""")
    inputs_dict_equivalent_radiated_power = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_equivalent_radiated_power[pin]

def _get_output_spec_equivalent_radiated_power(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_equivalent_radiated_power = { 
        0 : outpin0
    }
    return outputs_dict_equivalent_radiated_power[pin]

class _InputSpecEquivalentRadiatedPower(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_equivalent_radiated_power(0), 0, op, -1) 
        self.meshed_region = _Input(_get_input_spec_equivalent_radiated_power(1), 1, op, -1) 
        self.int32 = _Input(_get_input_spec_equivalent_radiated_power(2), 2, op, -1) 

class _OutputSpecEquivalentRadiatedPower(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_equivalent_radiated_power(0), 0, op) 

class _EquivalentRadiatedPower:
    """Operator's description:
Internal name is "ERP"
Scripting name is "equivalent_radiated_power"

This operator can be instantiated in both following ways:
- using dpf.Operator("ERP")
- using dpf.operators.result.equivalent_radiated_power()

Input list: 
   0: fields_container 
   1: meshed_region (the mesh region in this pin have to be boundary or skin mesh)
   2: int32 (load step number, if it's specified, the ERP is computed only on the substeps of this step)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "ERP"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecEquivalentRadiatedPower(self._op)
         self.outputs = _OutputSpecEquivalentRadiatedPower(self._op)

def equivalent_radiated_power():
    return _EquivalentRadiatedPower()

#internal name: torque
#scripting name: torque
def _get_input_spec_torque(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """fields_container""")
    inputs_dict_torque = { 
        0 : inpin0
    }
    return inputs_dict_torque[pin]

def _get_output_spec_torque(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_torque = { 
        0 : outpin0
    }
    return outputs_dict_torque[pin]

class _InputSpecTorque(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_torque(0), 0, op, -1) 

class _OutputSpecTorque(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_torque(0), 0, op) 

class _Torque:
    """Operator's description:
Internal name is "torque"
Scripting name is "torque"

This operator can be instantiated in both following ways:
- using dpf.Operator("torque")
- using dpf.operators.result.torque()

Input list: 
   0: fields_container (fields_container)
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "torque"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecTorque(self._op)
         self.outputs = _OutputSpecTorque(self._op)

def torque():
    return _Torque()

#internal name: cyclic_expansion_mesh
#scripting name: cyclic_mesh_expansion
def _get_input_spec_cyclic_mesh_expansion(pin):
    inpin7 = _PinSpecification(name = "sector_meshed_region", type_names = ["meshed_region"], optional = True, document = """""")
    inpin16 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], optional = False, document = """""")
    inputs_dict_cyclic_mesh_expansion = { 
        7 : inpin7,
        16 : inpin16
    }
    return inputs_dict_cyclic_mesh_expansion[pin]

def _get_output_spec_cyclic_mesh_expansion(pin):
    outpin0 = _PinSpecification(name = "meshed_region", type_names = ["meshed_region"], document = """expanded meshed region.""")
    outpin1 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], document = """input cyclic support modified in place containing the new expanded meshed region.""")
    outputs_dict_cyclic_mesh_expansion = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_cyclic_mesh_expansion[pin]

class _InputSpecCyclicMeshExpansion(_Inputs):
    def __init__(self, op: _Operator):
        self.sector_meshed_region = _Input(_get_input_spec_cyclic_mesh_expansion(7), 7, op, -1) 
        self.cyclic_support = _Input(_get_input_spec_cyclic_mesh_expansion(16), 16, op, -1) 

class _OutputSpecCyclicMeshExpansion(_Outputs):
    def __init__(self, op: _Operator):
        self.meshed_region = _Output(_get_output_spec_cyclic_mesh_expansion(0), 0, op) 
        self.cyclic_support = _Output(_get_output_spec_cyclic_mesh_expansion(1), 1, op) 

class _CyclicMeshExpansion:
    """Operator's description:
Internal name is "cyclic_expansion_mesh"
Scripting name is "cyclic_mesh_expansion"

This operator can be instantiated in both following ways:
- using dpf.Operator("cyclic_expansion_mesh")
- using dpf.operators.result.cyclic_mesh_expansion()

Input list: 
   7: sector_meshed_region 
   16: cyclic_support 
Output list: 
   0: meshed_region (expanded meshed region.)
   1: cyclic_support (input cyclic support modified in place containing the new expanded meshed region.)
"""
    def __init__(self):
         self._name = "cyclic_expansion_mesh"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCyclicMeshExpansion(self._op)
         self.outputs = _OutputSpecCyclicMeshExpansion(self._op)

def cyclic_mesh_expansion():
    return _CyclicMeshExpansion()

#internal name: cyclic_analytic_usum_max
#scripting name: cyclic_analytic_usum_max
def _get_input_spec_cyclic_analytic_usum_max(pin):
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
    return inputs_dict_cyclic_analytic_usum_max[pin]

def _get_output_spec_cyclic_analytic_usum_max(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_cyclic_analytic_usum_max = { 
        0 : outpin0
    }
    return outputs_dict_cyclic_analytic_usum_max[pin]

class _InputSpecCyclicAnalyticUsumMax(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_cyclic_analytic_usum_max(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_cyclic_analytic_usum_max(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_cyclic_analytic_usum_max(2), 2, op, -1) 
        self.cyclic_support = _Input(_get_input_spec_cyclic_analytic_usum_max(16), 16, op, -1) 

class _OutputSpecCyclicAnalyticUsumMax(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cyclic_analytic_usum_max(0), 0, op) 

class _CyclicAnalyticUsumMax:
    """Operator's description:
Internal name is "cyclic_analytic_usum_max"
Scripting name is "cyclic_analytic_usum_max"

This operator can be instantiated in both following ways:
- using dpf.Operator("cyclic_analytic_usum_max")
- using dpf.operators.result.cyclic_analytic_usum_max()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (field container with the base and duplicate sectors)
   16: cyclic_support 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "cyclic_analytic_usum_max"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCyclicAnalyticUsumMax(self._op)
         self.outputs = _OutputSpecCyclicAnalyticUsumMax(self._op)

def cyclic_analytic_usum_max():
    return _CyclicAnalyticUsumMax()

#internal name: cyclic_analytic_stress_eqv_max
#scripting name: cyclic_analytic_seqv_max
def _get_input_spec_cyclic_analytic_seqv_max(pin):
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
    return inputs_dict_cyclic_analytic_seqv_max[pin]

def _get_output_spec_cyclic_analytic_seqv_max(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_cyclic_analytic_seqv_max = { 
        0 : outpin0
    }
    return outputs_dict_cyclic_analytic_seqv_max[pin]

class _InputSpecCyclicAnalyticSeqvMax(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_cyclic_analytic_seqv_max(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_cyclic_analytic_seqv_max(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_cyclic_analytic_seqv_max(2), 2, op, -1) 
        self.cyclic_support = _Input(_get_input_spec_cyclic_analytic_seqv_max(16), 16, op, -1) 

class _OutputSpecCyclicAnalyticSeqvMax(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cyclic_analytic_seqv_max(0), 0, op) 

class _CyclicAnalyticSeqvMax:
    """Operator's description:
Internal name is "cyclic_analytic_stress_eqv_max"
Scripting name is "cyclic_analytic_seqv_max"

This operator can be instantiated in both following ways:
- using dpf.Operator("cyclic_analytic_stress_eqv_max")
- using dpf.operators.result.cyclic_analytic_seqv_max()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (field container with the base and duplicate sectors)
   16: cyclic_support 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "cyclic_analytic_stress_eqv_max"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCyclicAnalyticSeqvMax(self._op)
         self.outputs = _OutputSpecCyclicAnalyticSeqvMax(self._op)

def cyclic_analytic_seqv_max():
    return _CyclicAnalyticSeqvMax()

#internal name: recombine_harmonic_indeces_cyclic
#scripting name: recombine_harmonic_indeces_cyclic
def _get_input_spec_recombine_harmonic_indeces_cyclic(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_recombine_harmonic_indeces_cyclic = { 
        0 : inpin0
    }
    return inputs_dict_recombine_harmonic_indeces_cyclic[pin]

def _get_output_spec_recombine_harmonic_indeces_cyclic(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_recombine_harmonic_indeces_cyclic = { 
        0 : outpin0
    }
    return outputs_dict_recombine_harmonic_indeces_cyclic[pin]

class _InputSpecRecombineHarmonicIndecesCyclic(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_recombine_harmonic_indeces_cyclic(0), 0, op, -1) 

class _OutputSpecRecombineHarmonicIndecesCyclic(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_recombine_harmonic_indeces_cyclic(0), 0, op) 

class _RecombineHarmonicIndecesCyclic:
    """Operator's description:
Internal name is "recombine_harmonic_indeces_cyclic"
Scripting name is "recombine_harmonic_indeces_cyclic"

This operator can be instantiated in both following ways:
- using dpf.Operator("recombine_harmonic_indeces_cyclic")
- using dpf.operators.result.recombine_harmonic_indeces_cyclic()

Input list: 
   0: fields_container 
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "recombine_harmonic_indeces_cyclic"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecRecombineHarmonicIndecesCyclic(self._op)
         self.outputs = _OutputSpecRecombineHarmonicIndecesCyclic(self._op)

def recombine_harmonic_indeces_cyclic():
    return _RecombineHarmonicIndecesCyclic()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from mapdlOperatorsCore.dll plugin, from "result" category
"""

#internal name: mapdl::rst::NPEL
#scripting name: nodal_averaged_elastic_strains
def _get_input_spec_nodal_averaged_elastic_strains(pin):
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
    return inputs_dict_nodal_averaged_elastic_strains[pin]

def _get_output_spec_nodal_averaged_elastic_strains(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_elastic_strains = { 
        0 : outpin0
    }
    return outputs_dict_nodal_averaged_elastic_strains[pin]

class _InputSpecNodalAveragedElasticStrains(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_averaged_elastic_strains(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_averaged_elastic_strains(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_averaged_elastic_strains(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_averaged_elastic_strains(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_averaged_elastic_strains(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_averaged_elastic_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedElasticStrains(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_averaged_elastic_strains(0), 0, op) 

class _NodalAveragedElasticStrains:
    """Operator's description:
Internal name is "mapdl::rst::NPEL"
Scripting name is "nodal_averaged_elastic_strains"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::NPEL")
- using dpf.operators.result.nodal_averaged_elastic_strains()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::rst::NPEL"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalAveragedElasticStrains(self._op)
         self.outputs = _OutputSpecNodalAveragedElasticStrains(self._op)

def nodal_averaged_elastic_strains():
    return _NodalAveragedElasticStrains()

#internal name: RigidBodyAddition
#scripting name: add_rigid_body_motion
def _get_input_spec_add_rigid_body_motion(pin):
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
    return inputs_dict_add_rigid_body_motion[pin]

def _get_output_spec_add_rigid_body_motion(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_add_rigid_body_motion = { 
        0 : outpin0
    }
    return outputs_dict_add_rigid_body_motion[pin]

class _InputSpecAddRigidBodyMotion(_Inputs):
    def __init__(self, op: _Operator):
        self.displacement_field = _Input(_get_input_spec_add_rigid_body_motion(0), 0, op, -1) 
        self.translation_field = _Input(_get_input_spec_add_rigid_body_motion(1), 1, op, -1) 
        self.rotation_field = _Input(_get_input_spec_add_rigid_body_motion(2), 2, op, -1) 
        self.center_field = _Input(_get_input_spec_add_rigid_body_motion(3), 3, op, -1) 
        self.mesh = _Input(_get_input_spec_add_rigid_body_motion(7), 7, op, -1) 

class _OutputSpecAddRigidBodyMotion(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_add_rigid_body_motion(0), 0, op) 

class _AddRigidBodyMotion:
    """Operator's description:
Internal name is "RigidBodyAddition"
Scripting name is "add_rigid_body_motion"

This operator can be instantiated in both following ways:
- using dpf.Operator("RigidBodyAddition")
- using dpf.operators.result.add_rigid_body_motion()

Input list: 
   0: displacement_field 
   1: translation_field 
   2: rotation_field 
   3: center_field 
   7: mesh (default is the mesh in the support)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "RigidBodyAddition"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAddRigidBodyMotion(self._op)
         self.outputs = _OutputSpecAddRigidBodyMotion(self._op)

def add_rigid_body_motion():
    return _AddRigidBodyMotion()

#internal name: mapdl::rst::NPEL_EQV
#scripting name: nodal_averaged_equivalent_elastic_strain
def _get_input_spec_nodal_averaged_equivalent_elastic_strain(pin):
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
    return inputs_dict_nodal_averaged_equivalent_elastic_strain[pin]

def _get_output_spec_nodal_averaged_equivalent_elastic_strain(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_equivalent_elastic_strain = { 
        0 : outpin0
    }
    return outputs_dict_nodal_averaged_equivalent_elastic_strain[pin]

class _InputSpecNodalAveragedEquivalentElasticStrain(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_averaged_equivalent_elastic_strain(7), 7, op, -1) 

class _OutputSpecNodalAveragedEquivalentElasticStrain(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_averaged_equivalent_elastic_strain(0), 0, op) 

class _NodalAveragedEquivalentElasticStrain:
    """Operator's description:
Internal name is "mapdl::rst::NPEL_EQV"
Scripting name is "nodal_averaged_equivalent_elastic_strain"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::NPEL_EQV")
- using dpf.operators.result.nodal_averaged_equivalent_elastic_strain()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::rst::NPEL_EQV"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalAveragedEquivalentElasticStrain(self._op)
         self.outputs = _OutputSpecNodalAveragedEquivalentElasticStrain(self._op)

def nodal_averaged_equivalent_elastic_strain():
    return _NodalAveragedEquivalentElasticStrain()

from . import mapdl #mapdl.run

#internal name: mapdl::rst::V_cyclic
#scripting name: cyclic_expanded_velocity
def _get_input_spec_cyclic_expanded_velocity(pin):
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
    return inputs_dict_cyclic_expanded_velocity[pin]

def _get_output_spec_cyclic_expanded_velocity(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outpin1 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], document = """""")
    outputs_dict_cyclic_expanded_velocity = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_cyclic_expanded_velocity[pin]

class _InputSpecCyclicExpandedVelocity(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_cyclic_expanded_velocity(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_cyclic_expanded_velocity(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_cyclic_expanded_velocity(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_cyclic_expanded_velocity(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_cyclic_expanded_velocity(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_cyclic_expanded_velocity(5), 5, op, -1) 
        self.sector_mesh = _Input(_get_input_spec_cyclic_expanded_velocity(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_cyclic_expanded_velocity(9), 9, op, -1) 
        self.read_cyclic = _Input(_get_input_spec_cyclic_expanded_velocity(14), 14, op, -1) 
        self.expanded_meshed_region = _Input(_get_input_spec_cyclic_expanded_velocity(15), 15, op, -1) 
        self.cyclic_support = _Input(_get_input_spec_cyclic_expanded_velocity(16), 16, op, -1) 
        self.sectors_to_expand = _Input(_get_input_spec_cyclic_expanded_velocity(18), 18, op, -1) 
        self.phi = _Input(_get_input_spec_cyclic_expanded_velocity(19), 19, op, -1) 
        self.filter_degenerated_elements = _Input(_get_input_spec_cyclic_expanded_velocity(20), 20, op, -1) 

class _OutputSpecCyclicExpandedVelocity(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cyclic_expanded_velocity(0), 0, op) 
        self.expanded_meshed_region = _Output(_get_output_spec_cyclic_expanded_velocity(1), 1, op) 

class _CyclicExpandedVelocity:
    """Operator's description:
Internal name is "mapdl::rst::V_cyclic"
Scripting name is "cyclic_expanded_velocity"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::V_cyclic")
- using dpf.operators.result.cyclic_expanded_velocity()

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
"""
    def __init__(self):
         self._name = "mapdl::rst::V_cyclic"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCyclicExpandedVelocity(self._op)
         self.outputs = _OutputSpecCyclicExpandedVelocity(self._op)

def cyclic_expanded_velocity():
    return _CyclicExpandedVelocity()

#internal name: mapdl::rst::EPEL_cyclic
#scripting name: cyclic_expanded_el_strain
def _get_input_spec_cyclic_expanded_el_strain(pin):
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
    return inputs_dict_cyclic_expanded_el_strain[pin]

def _get_output_spec_cyclic_expanded_el_strain(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outpin1 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], document = """""")
    outputs_dict_cyclic_expanded_el_strain = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_cyclic_expanded_el_strain[pin]

class _InputSpecCyclicExpandedElStrain(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_cyclic_expanded_el_strain(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_cyclic_expanded_el_strain(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_cyclic_expanded_el_strain(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_cyclic_expanded_el_strain(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_cyclic_expanded_el_strain(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_cyclic_expanded_el_strain(5), 5, op, -1) 
        self.sector_mesh = _Input(_get_input_spec_cyclic_expanded_el_strain(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_cyclic_expanded_el_strain(9), 9, op, -1) 
        self.read_cyclic = _Input(_get_input_spec_cyclic_expanded_el_strain(14), 14, op, -1) 
        self.expanded_meshed_region = _Input(_get_input_spec_cyclic_expanded_el_strain(15), 15, op, -1) 
        self.cyclic_support = _Input(_get_input_spec_cyclic_expanded_el_strain(16), 16, op, -1) 
        self.sectors_to_expand = _Input(_get_input_spec_cyclic_expanded_el_strain(18), 18, op, -1) 
        self.phi = _Input(_get_input_spec_cyclic_expanded_el_strain(19), 19, op, -1) 
        self.filter_degenerated_elements = _Input(_get_input_spec_cyclic_expanded_el_strain(20), 20, op, -1) 

class _OutputSpecCyclicExpandedElStrain(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cyclic_expanded_el_strain(0), 0, op) 
        self.expanded_meshed_region = _Output(_get_output_spec_cyclic_expanded_el_strain(1), 1, op) 

class _CyclicExpandedElStrain:
    """Operator's description:
Internal name is "mapdl::rst::EPEL_cyclic"
Scripting name is "cyclic_expanded_el_strain"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::EPEL_cyclic")
- using dpf.operators.result.cyclic_expanded_el_strain()

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
"""
    def __init__(self):
         self._name = "mapdl::rst::EPEL_cyclic"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCyclicExpandedElStrain(self._op)
         self.outputs = _OutputSpecCyclicExpandedElStrain(self._op)

def cyclic_expanded_el_strain():
    return _CyclicExpandedElStrain()

#internal name: mapdl::rst::NTH_SWL
#scripting name: nodal_averaged_thermal_swelling_strains
def _get_input_spec_nodal_averaged_thermal_swelling_strains(pin):
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
    return inputs_dict_nodal_averaged_thermal_swelling_strains[pin]

def _get_output_spec_nodal_averaged_thermal_swelling_strains(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_thermal_swelling_strains = { 
        0 : outpin0
    }
    return outputs_dict_nodal_averaged_thermal_swelling_strains[pin]

class _InputSpecNodalAveragedThermalSwellingStrains(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_averaged_thermal_swelling_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedThermalSwellingStrains(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_averaged_thermal_swelling_strains(0), 0, op) 

class _NodalAveragedThermalSwellingStrains:
    """Operator's description:
Internal name is "mapdl::rst::NTH_SWL"
Scripting name is "nodal_averaged_thermal_swelling_strains"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::NTH_SWL")
- using dpf.operators.result.nodal_averaged_thermal_swelling_strains()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::rst::NTH_SWL"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalAveragedThermalSwellingStrains(self._op)
         self.outputs = _OutputSpecNodalAveragedThermalSwellingStrains(self._op)

def nodal_averaged_thermal_swelling_strains():
    return _NodalAveragedThermalSwellingStrains()

#internal name: mapdl::rst::NS
#scripting name: nodal_averaged_stresses
def _get_input_spec_nodal_averaged_stresses(pin):
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
    return inputs_dict_nodal_averaged_stresses[pin]

def _get_output_spec_nodal_averaged_stresses(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_stresses = { 
        0 : outpin0
    }
    return outputs_dict_nodal_averaged_stresses[pin]

class _InputSpecNodalAveragedStresses(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_averaged_stresses(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_averaged_stresses(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_averaged_stresses(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_averaged_stresses(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_averaged_stresses(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_averaged_stresses(7), 7, op, -1) 

class _OutputSpecNodalAveragedStresses(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_averaged_stresses(0), 0, op) 

class _NodalAveragedStresses:
    """Operator's description:
Internal name is "mapdl::rst::NS"
Scripting name is "nodal_averaged_stresses"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::NS")
- using dpf.operators.result.nodal_averaged_stresses()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::rst::NS"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalAveragedStresses(self._op)
         self.outputs = _OutputSpecNodalAveragedStresses(self._op)

def nodal_averaged_stresses():
    return _NodalAveragedStresses()

#internal name: mapdl::rst::NTH
#scripting name: nodal_averaged_thermal_strains
def _get_input_spec_nodal_averaged_thermal_strains(pin):
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
    return inputs_dict_nodal_averaged_thermal_strains[pin]

def _get_output_spec_nodal_averaged_thermal_strains(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_thermal_strains = { 
        0 : outpin0
    }
    return outputs_dict_nodal_averaged_thermal_strains[pin]

class _InputSpecNodalAveragedThermalStrains(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_averaged_thermal_strains(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_averaged_thermal_strains(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_averaged_thermal_strains(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_averaged_thermal_strains(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_averaged_thermal_strains(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_averaged_thermal_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedThermalStrains(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_averaged_thermal_strains(0), 0, op) 

class _NodalAveragedThermalStrains:
    """Operator's description:
Internal name is "mapdl::rst::NTH"
Scripting name is "nodal_averaged_thermal_strains"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::NTH")
- using dpf.operators.result.nodal_averaged_thermal_strains()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::rst::NTH"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalAveragedThermalStrains(self._op)
         self.outputs = _OutputSpecNodalAveragedThermalStrains(self._op)

def nodal_averaged_thermal_strains():
    return _NodalAveragedThermalStrains()

#internal name: mapdl::rst::NPPL
#scripting name: nodal_averaged_plastic_strains
def _get_input_spec_nodal_averaged_plastic_strains(pin):
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
    return inputs_dict_nodal_averaged_plastic_strains[pin]

def _get_output_spec_nodal_averaged_plastic_strains(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_plastic_strains = { 
        0 : outpin0
    }
    return outputs_dict_nodal_averaged_plastic_strains[pin]

class _InputSpecNodalAveragedPlasticStrains(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_averaged_plastic_strains(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_averaged_plastic_strains(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_averaged_plastic_strains(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_averaged_plastic_strains(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_averaged_plastic_strains(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_averaged_plastic_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedPlasticStrains(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_averaged_plastic_strains(0), 0, op) 

class _NodalAveragedPlasticStrains:
    """Operator's description:
Internal name is "mapdl::rst::NPPL"
Scripting name is "nodal_averaged_plastic_strains"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::NPPL")
- using dpf.operators.result.nodal_averaged_plastic_strains()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::rst::NPPL"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalAveragedPlasticStrains(self._op)
         self.outputs = _OutputSpecNodalAveragedPlasticStrains(self._op)

def nodal_averaged_plastic_strains():
    return _NodalAveragedPlasticStrains()

#internal name: mapdl::rst::NCR
#scripting name: nodal_averaged_creep_strains
def _get_input_spec_nodal_averaged_creep_strains(pin):
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
    return inputs_dict_nodal_averaged_creep_strains[pin]

def _get_output_spec_nodal_averaged_creep_strains(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_creep_strains = { 
        0 : outpin0
    }
    return outputs_dict_nodal_averaged_creep_strains[pin]

class _InputSpecNodalAveragedCreepStrains(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_averaged_creep_strains(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_averaged_creep_strains(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_averaged_creep_strains(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_averaged_creep_strains(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_averaged_creep_strains(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_averaged_creep_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedCreepStrains(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_averaged_creep_strains(0), 0, op) 

class _NodalAveragedCreepStrains:
    """Operator's description:
Internal name is "mapdl::rst::NCR"
Scripting name is "nodal_averaged_creep_strains"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::NCR")
- using dpf.operators.result.nodal_averaged_creep_strains()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::rst::NCR"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalAveragedCreepStrains(self._op)
         self.outputs = _OutputSpecNodalAveragedCreepStrains(self._op)

def nodal_averaged_creep_strains():
    return _NodalAveragedCreepStrains()

#internal name: mapdl::rst::NTH_EQV
#scripting name: nodal_averaged_equivalent_thermal_strains
def _get_input_spec_nodal_averaged_equivalent_thermal_strains(pin):
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
    return inputs_dict_nodal_averaged_equivalent_thermal_strains[pin]

def _get_output_spec_nodal_averaged_equivalent_thermal_strains(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_equivalent_thermal_strains = { 
        0 : outpin0
    }
    return outputs_dict_nodal_averaged_equivalent_thermal_strains[pin]

class _InputSpecNodalAveragedEquivalentThermalStrains(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_averaged_equivalent_thermal_strains(7), 7, op, -1) 

class _OutputSpecNodalAveragedEquivalentThermalStrains(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_averaged_equivalent_thermal_strains(0), 0, op) 

class _NodalAveragedEquivalentThermalStrains:
    """Operator's description:
Internal name is "mapdl::rst::NTH_EQV"
Scripting name is "nodal_averaged_equivalent_thermal_strains"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::NTH_EQV")
- using dpf.operators.result.nodal_averaged_equivalent_thermal_strains()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::rst::NTH_EQV"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalAveragedEquivalentThermalStrains(self._op)
         self.outputs = _OutputSpecNodalAveragedEquivalentThermalStrains(self._op)

def nodal_averaged_equivalent_thermal_strains():
    return _NodalAveragedEquivalentThermalStrains()

#internal name: mapdl::rst::NPPL_EQV
#scripting name: nodal_averaged_equivalent_plastic_strain
def _get_input_spec_nodal_averaged_equivalent_plastic_strain(pin):
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
    return inputs_dict_nodal_averaged_equivalent_plastic_strain[pin]

def _get_output_spec_nodal_averaged_equivalent_plastic_strain(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_equivalent_plastic_strain = { 
        0 : outpin0
    }
    return outputs_dict_nodal_averaged_equivalent_plastic_strain[pin]

class _InputSpecNodalAveragedEquivalentPlasticStrain(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_averaged_equivalent_plastic_strain(7), 7, op, -1) 

class _OutputSpecNodalAveragedEquivalentPlasticStrain(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_averaged_equivalent_plastic_strain(0), 0, op) 

class _NodalAveragedEquivalentPlasticStrain:
    """Operator's description:
Internal name is "mapdl::rst::NPPL_EQV"
Scripting name is "nodal_averaged_equivalent_plastic_strain"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::NPPL_EQV")
- using dpf.operators.result.nodal_averaged_equivalent_plastic_strain()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::rst::NPPL_EQV"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalAveragedEquivalentPlasticStrain(self._op)
         self.outputs = _OutputSpecNodalAveragedEquivalentPlasticStrain(self._op)

def nodal_averaged_equivalent_plastic_strain():
    return _NodalAveragedEquivalentPlasticStrain()

#internal name: mapdl::rst::NCR_EQV
#scripting name: nodal_averaged_equivalent_creep_strain
def _get_input_spec_nodal_averaged_equivalent_creep_strain(pin):
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
    return inputs_dict_nodal_averaged_equivalent_creep_strain[pin]

def _get_output_spec_nodal_averaged_equivalent_creep_strain(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nodal_averaged_equivalent_creep_strain = { 
        0 : outpin0
    }
    return outputs_dict_nodal_averaged_equivalent_creep_strain[pin]

class _InputSpecNodalAveragedEquivalentCreepStrain(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nodal_averaged_equivalent_creep_strain(7), 7, op, -1) 

class _OutputSpecNodalAveragedEquivalentCreepStrain(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_averaged_equivalent_creep_strain(0), 0, op) 

class _NodalAveragedEquivalentCreepStrain:
    """Operator's description:
Internal name is "mapdl::rst::NCR_EQV"
Scripting name is "nodal_averaged_equivalent_creep_strain"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::NCR_EQV")
- using dpf.operators.result.nodal_averaged_equivalent_creep_strain()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::rst::NCR_EQV"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalAveragedEquivalentCreepStrain(self._op)
         self.outputs = _OutputSpecNodalAveragedEquivalentCreepStrain(self._op)

def nodal_averaged_equivalent_creep_strain():
    return _NodalAveragedEquivalentCreepStrain()

#internal name: mapdl::rst::coords_and_euler_nodes
#scripting name: euler_nodes
def _get_input_spec_euler_nodes(pin):
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
    return inputs_dict_euler_nodes[pin]

def _get_output_spec_euler_nodes(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_euler_nodes = { 
        0 : outpin0
    }
    return outputs_dict_euler_nodes[pin]

class _InputSpecEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Input(_get_input_spec_euler_nodes(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_euler_nodes(4), 4, op, -1) 
        self.coord_and_euler = _Input(_get_input_spec_euler_nodes(6), 6, op, -1) 
        self.mesh = _Input(_get_input_spec_euler_nodes(7), 7, op, -1) 

class _OutputSpecEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_euler_nodes(0), 0, op) 

class _EulerNodes:
    """Operator's description:
Internal name is "mapdl::rst::coords_and_euler_nodes"
Scripting name is "euler_nodes"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::coords_and_euler_nodes")
- using dpf.operators.result.euler_nodes()

Input list: 
   3: streams_container 
   4: data_sources 
   6: coord_and_euler (if true, then the field has ncomp=6 with 3 oords and 3 euler angles, else there is only the euler angles (default is true))
   7: mesh 
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "mapdl::rst::coords_and_euler_nodes"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecEulerNodes(self._op)
         self.outputs = _OutputSpecEulerNodes(self._op)

def euler_nodes():
    return _EulerNodes()

from . import mapdl #mapdl.nmisc

#internal name: ENF_rotation_by_euler_nodes
#scripting name: enf_rotation_by_euler_nodes
def _get_input_spec_enf_rotation_by_euler_nodes(pin):
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_enf_rotation_by_euler_nodes = { 
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_enf_rotation_by_euler_nodes[pin]

def _get_output_spec_enf_rotation_by_euler_nodes(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_enf_rotation_by_euler_nodes = { 
        0 : outpin0
    }
    return outputs_dict_enf_rotation_by_euler_nodes[pin]

class _InputSpecEnfRotationByEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_enf_rotation_by_euler_nodes(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_enf_rotation_by_euler_nodes(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_enf_rotation_by_euler_nodes(4), 4, op, -1) 

class _OutputSpecEnfRotationByEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_enf_rotation_by_euler_nodes(0), 0, op) 

class _EnfRotationByEulerNodes:
    """Operator's description:
Internal name is "ENF_rotation_by_euler_nodes"
Scripting name is "enf_rotation_by_euler_nodes"

This operator can be instantiated in both following ways:
- using dpf.Operator("ENF_rotation_by_euler_nodes")
- using dpf.operators.result.enf_rotation_by_euler_nodes()

Input list: 
   2: fields_container 
   3: streams_container 
   4: data_sources 
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "ENF_rotation_by_euler_nodes"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecEnfRotationByEulerNodes(self._op)
         self.outputs = _OutputSpecEnfRotationByEulerNodes(self._op)

def enf_rotation_by_euler_nodes():
    return _EnfRotationByEulerNodes()

#internal name: cms_matrices_provider
#scripting name: cms_matrices_provider
def _get_input_spec_cms_matrices_provider(pin):
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """Data_sources (must contain at list one subfile).""")
    inputs_dict_cms_matrices_provider = { 
        4 : inpin4
    }
    return inputs_dict_cms_matrices_provider[pin]

def _get_output_spec_cms_matrices_provider(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """Fields container containing in this order : stiffness, damping, mass matrices, and then load vector.""")
    outputs_dict_cms_matrices_provider = { 
        0 : outpin0
    }
    return outputs_dict_cms_matrices_provider[pin]

class _InputSpecCmsMatricesProvider(_Inputs):
    def __init__(self, op: _Operator):
        self.data_sources = _Input(_get_input_spec_cms_matrices_provider(4), 4, op, -1) 

class _OutputSpecCmsMatricesProvider(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_cms_matrices_provider(0), 0, op) 

class _CmsMatricesProvider:
    """Operator's description:
Internal name is "cms_matrices_provider"
Scripting name is "cms_matrices_provider"

This operator can be instantiated in both following ways:
- using dpf.Operator("cms_matrices_provider")
- using dpf.operators.result.cms_matrices_provider()

Input list: 
   4: data_sources (Data_sources (must contain at list one subfile).)
Output list: 
   0: fields_container (Fields container containing in this order : stiffness, damping, mass matrices, and then load vector.)
"""
    def __init__(self):
         self._name = "cms_matrices_provider"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCmsMatricesProvider(self._op)
         self.outputs = _OutputSpecCmsMatricesProvider(self._op)

def cms_matrices_provider():
    return _CmsMatricesProvider()

from . import mapdl #mapdl.smisc

#internal name: mapdl::rst::RotateNodalFCByEulerNodes
#scripting name: nodal_rotation_by_euler_nodes
def _get_input_spec_nodal_rotation_by_euler_nodes(pin):
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_nodal_rotation_by_euler_nodes = { 
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_nodal_rotation_by_euler_nodes[pin]

def _get_output_spec_nodal_rotation_by_euler_nodes(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_rotation_by_euler_nodes = { 
        0 : outpin0
    }
    return outputs_dict_nodal_rotation_by_euler_nodes[pin]

class _InputSpecNodalRotationByEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_nodal_rotation_by_euler_nodes(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nodal_rotation_by_euler_nodes(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nodal_rotation_by_euler_nodes(4), 4, op, -1) 

class _OutputSpecNodalRotationByEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nodal_rotation_by_euler_nodes(0), 0, op) 

class _NodalRotationByEulerNodes:
    """Operator's description:
Internal name is "mapdl::rst::RotateNodalFCByEulerNodes"
Scripting name is "nodal_rotation_by_euler_nodes"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::RotateNodalFCByEulerNodes")
- using dpf.operators.result.nodal_rotation_by_euler_nodes()

Input list: 
   2: fields_container 
   3: streams_container 
   4: data_sources 
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "mapdl::rst::RotateNodalFCByEulerNodes"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNodalRotationByEulerNodes(self._op)
         self.outputs = _OutputSpecNodalRotationByEulerNodes(self._op)

def nodal_rotation_by_euler_nodes():
    return _NodalRotationByEulerNodes()

#internal name: mapdl::rst::S_rotation_by_euler_nodes
#scripting name: stress_rotation_by_euler_nodes
def _get_input_spec_stress_rotation_by_euler_nodes(pin):
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_stress_rotation_by_euler_nodes = { 
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_stress_rotation_by_euler_nodes[pin]

def _get_output_spec_stress_rotation_by_euler_nodes(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_stress_rotation_by_euler_nodes = { 
        0 : outpin0
    }
    return outputs_dict_stress_rotation_by_euler_nodes[pin]

class _InputSpecStressRotationByEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_stress_rotation_by_euler_nodes(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_stress_rotation_by_euler_nodes(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_stress_rotation_by_euler_nodes(4), 4, op, -1) 

class _OutputSpecStressRotationByEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_stress_rotation_by_euler_nodes(0), 0, op) 

class _StressRotationByEulerNodes:
    """Operator's description:
Internal name is "mapdl::rst::S_rotation_by_euler_nodes"
Scripting name is "stress_rotation_by_euler_nodes"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::S_rotation_by_euler_nodes")
- using dpf.operators.result.stress_rotation_by_euler_nodes()

Input list: 
   2: fields_container 
   3: streams_container 
   4: data_sources 
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "mapdl::rst::S_rotation_by_euler_nodes"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStressRotationByEulerNodes(self._op)
         self.outputs = _OutputSpecStressRotationByEulerNodes(self._op)

def stress_rotation_by_euler_nodes():
    return _StressRotationByEulerNodes()

#internal name: mapdl::rst::EPEL_rotation_by_euler_nodes
#scripting name: elastic_strain_rotation_by_euler_nodes
def _get_input_spec_elastic_strain_rotation_by_euler_nodes(pin):
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_elastic_strain_rotation_by_euler_nodes = { 
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_elastic_strain_rotation_by_euler_nodes[pin]

def _get_output_spec_elastic_strain_rotation_by_euler_nodes(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elastic_strain_rotation_by_euler_nodes = { 
        0 : outpin0
    }
    return outputs_dict_elastic_strain_rotation_by_euler_nodes[pin]

class _InputSpecElasticStrainRotationByEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_elastic_strain_rotation_by_euler_nodes(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_elastic_strain_rotation_by_euler_nodes(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_elastic_strain_rotation_by_euler_nodes(4), 4, op, -1) 

class _OutputSpecElasticStrainRotationByEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_elastic_strain_rotation_by_euler_nodes(0), 0, op) 

class _ElasticStrainRotationByEulerNodes:
    """Operator's description:
Internal name is "mapdl::rst::EPEL_rotation_by_euler_nodes"
Scripting name is "elastic_strain_rotation_by_euler_nodes"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::EPEL_rotation_by_euler_nodes")
- using dpf.operators.result.elastic_strain_rotation_by_euler_nodes()

Input list: 
   2: fields_container 
   3: streams_container 
   4: data_sources 
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "mapdl::rst::EPEL_rotation_by_euler_nodes"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecElasticStrainRotationByEulerNodes(self._op)
         self.outputs = _OutputSpecElasticStrainRotationByEulerNodes(self._op)

def elastic_strain_rotation_by_euler_nodes():
    return _ElasticStrainRotationByEulerNodes()

#internal name: mapdl::rst::EPPL_rotation_by_euler_nodes
#scripting name: plastic_strain_rotation_by_euler_nodes
def _get_input_spec_plastic_strain_rotation_by_euler_nodes(pin):
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_plastic_strain_rotation_by_euler_nodes = { 
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_plastic_strain_rotation_by_euler_nodes[pin]

def _get_output_spec_plastic_strain_rotation_by_euler_nodes(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_plastic_strain_rotation_by_euler_nodes = { 
        0 : outpin0
    }
    return outputs_dict_plastic_strain_rotation_by_euler_nodes[pin]

class _InputSpecPlasticStrainRotationByEulerNodes(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_plastic_strain_rotation_by_euler_nodes(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_plastic_strain_rotation_by_euler_nodes(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_plastic_strain_rotation_by_euler_nodes(4), 4, op, -1) 

class _OutputSpecPlasticStrainRotationByEulerNodes(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_plastic_strain_rotation_by_euler_nodes(0), 0, op) 

class _PlasticStrainRotationByEulerNodes:
    """Operator's description:
Internal name is "mapdl::rst::EPPL_rotation_by_euler_nodes"
Scripting name is "plastic_strain_rotation_by_euler_nodes"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::EPPL_rotation_by_euler_nodes")
- using dpf.operators.result.plastic_strain_rotation_by_euler_nodes()

Input list: 
   2: fields_container 
   3: streams_container 
   4: data_sources 
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "mapdl::rst::EPPL_rotation_by_euler_nodes"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPlasticStrainRotationByEulerNodes(self._op)
         self.outputs = _OutputSpecPlasticStrainRotationByEulerNodes(self._op)

def plastic_strain_rotation_by_euler_nodes():
    return _PlasticStrainRotationByEulerNodes()

from . import mapdl #mapdl.pres_to_field

from . import mapdl #mapdl.prns_to_field

#internal name: ExtractRigidBodyMotion
#scripting name: remove_rigid_body_motion
def _get_input_spec_remove_rigid_body_motion(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "reference_node_id", type_names = ["int32"], optional = True, document = """Id of the reference entity (node).""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """default is the mesh in the support""")
    inputs_dict_remove_rigid_body_motion = { 
        0 : inpin0,
        1 : inpin1,
        7 : inpin7
    }
    return inputs_dict_remove_rigid_body_motion[pin]

def _get_output_spec_remove_rigid_body_motion(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_remove_rigid_body_motion = { 
        0 : outpin0
    }
    return outputs_dict_remove_rigid_body_motion[pin]

class _InputSpecRemoveRigidBodyMotion(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_remove_rigid_body_motion(0), 0, op, -1) 
        self.reference_node_id = _Input(_get_input_spec_remove_rigid_body_motion(1), 1, op, -1) 
        self.mesh = _Input(_get_input_spec_remove_rigid_body_motion(7), 7, op, -1) 

class _OutputSpecRemoveRigidBodyMotion(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_remove_rigid_body_motion(0), 0, op) 

class _RemoveRigidBodyMotion:
    """Operator's description:
Internal name is "ExtractRigidBodyMotion"
Scripting name is "remove_rigid_body_motion"

This operator can be instantiated in both following ways:
- using dpf.Operator("ExtractRigidBodyMotion")
- using dpf.operators.result.remove_rigid_body_motion()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: reference_node_id (Id of the reference entity (node).)
   7: mesh (default is the mesh in the support)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "ExtractRigidBodyMotion"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecRemoveRigidBodyMotion(self._op)
         self.outputs = _OutputSpecRemoveRigidBodyMotion(self._op)

def remove_rigid_body_motion():
    return _RemoveRigidBodyMotion()

#internal name: ExtractRigidBodyMotion_fc
#scripting name: remove_rigid_body_motion_fc
def _get_input_spec_remove_rigid_body_motion_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "reference_node_id", type_names = ["int32"], optional = True, document = """Id of the reference entity (node).""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """default is the mesh in the support""")
    inputs_dict_remove_rigid_body_motion_fc = { 
        0 : inpin0,
        1 : inpin1,
        7 : inpin7
    }
    return inputs_dict_remove_rigid_body_motion_fc[pin]

def _get_output_spec_remove_rigid_body_motion_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_remove_rigid_body_motion_fc = { 
        0 : outpin0
    }
    return outputs_dict_remove_rigid_body_motion_fc[pin]

class _InputSpecRemoveRigidBodyMotionFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_remove_rigid_body_motion_fc(0), 0, op, -1) 
        self.reference_node_id = _Input(_get_input_spec_remove_rigid_body_motion_fc(1), 1, op, -1) 
        self.mesh = _Input(_get_input_spec_remove_rigid_body_motion_fc(7), 7, op, -1) 

class _OutputSpecRemoveRigidBodyMotionFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_remove_rigid_body_motion_fc(0), 0, op) 

class _RemoveRigidBodyMotionFc:
    """Operator's description:
Internal name is "ExtractRigidBodyMotion_fc"
Scripting name is "remove_rigid_body_motion_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("ExtractRigidBodyMotion_fc")
- using dpf.operators.result.remove_rigid_body_motion_fc()

Input list: 
   0: fields_container (field or fields container with only one field is expected)
   1: reference_node_id (Id of the reference entity (node).)
   7: mesh (default is the mesh in the support)
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "ExtractRigidBodyMotion_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecRemoveRigidBodyMotionFc(self._op)
         self.outputs = _OutputSpecRemoveRigidBodyMotionFc(self._op)

def remove_rigid_body_motion_fc():
    return _RemoveRigidBodyMotionFc()

#internal name: RigidBodyAddition_fc
#scripting name: add_rigid_body_motion_fc
def _get_input_spec_add_rigid_body_motion_fc(pin):
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
    return inputs_dict_add_rigid_body_motion_fc[pin]

def _get_output_spec_add_rigid_body_motion_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_add_rigid_body_motion_fc = { 
        0 : outpin0
    }
    return outputs_dict_add_rigid_body_motion_fc[pin]

class _InputSpecAddRigidBodyMotionFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_add_rigid_body_motion_fc(0), 0, op, -1) 
        self.translation_field = _Input(_get_input_spec_add_rigid_body_motion_fc(1), 1, op, -1) 
        self.rotation_field = _Input(_get_input_spec_add_rigid_body_motion_fc(2), 2, op, -1) 
        self.center_field = _Input(_get_input_spec_add_rigid_body_motion_fc(3), 3, op, -1) 
        self.mesh = _Input(_get_input_spec_add_rigid_body_motion_fc(7), 7, op, -1) 

class _OutputSpecAddRigidBodyMotionFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_add_rigid_body_motion_fc(0), 0, op) 

class _AddRigidBodyMotionFc:
    """Operator's description:
Internal name is "RigidBodyAddition_fc"
Scripting name is "add_rigid_body_motion_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("RigidBodyAddition_fc")
- using dpf.operators.result.add_rigid_body_motion_fc()

Input list: 
   0: fields_container 
   1: translation_field 
   2: rotation_field 
   3: center_field 
   7: mesh (default is the mesh in the support)
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "RigidBodyAddition_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecAddRigidBodyMotionFc(self._op)
         self.outputs = _OutputSpecAddRigidBodyMotionFc(self._op)

def add_rigid_body_motion_fc():
    return _AddRigidBodyMotionFc()

#internal name: mapdl::rst::U_cyclic
#scripting name: cyclic_expanded_displacement
def _get_input_spec_cyclic_expanded_displacement(pin):
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
    return inputs_dict_cyclic_expanded_displacement[pin]

def _get_output_spec_cyclic_expanded_displacement(pin):
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
    return outputs_dict_cyclic_expanded_displacement[pin]

class _InputSpecCyclicExpandedDisplacement(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_cyclic_expanded_displacement(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_cyclic_expanded_displacement(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_cyclic_expanded_displacement(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_cyclic_expanded_displacement(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_cyclic_expanded_displacement(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_cyclic_expanded_displacement(5), 5, op, -1) 
        self.sector_mesh = _Input(_get_input_spec_cyclic_expanded_displacement(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_cyclic_expanded_displacement(9), 9, op, -1) 
        self.freq = _Input(_get_input_spec_cyclic_expanded_displacement(12), 12, op, -1) 
        self.read_cyclic = _Input(_get_input_spec_cyclic_expanded_displacement(14), 14, op, -1) 
        self.expanded_meshed_region = _Input(_get_input_spec_cyclic_expanded_displacement(15), 15, op, -1) 
        self.cyclic_support = _Input(_get_input_spec_cyclic_expanded_displacement(16), 16, op, -1) 
        self.sectors_to_expand = _Input(_get_input_spec_cyclic_expanded_displacement(18), 18, op, -1) 
        self.phi = _Input(_get_input_spec_cyclic_expanded_displacement(19), 19, op, -1) 
        self.filter_degenerated_elements = _Input(_get_input_spec_cyclic_expanded_displacement(20), 20, op, -1) 

class _OutputSpecCyclicExpandedDisplacement(_Outputs):
    def __init__(self, op: _Operator):
        self.static_matrix = _Output(_get_output_spec_cyclic_expanded_displacement(0), 0, op) 
        self.expanded_meshed_region = _Output(_get_output_spec_cyclic_expanded_displacement(1), 1, op) 
        self.inertia_matrix = _Output(_get_output_spec_cyclic_expanded_displacement(2), 2, op) 
        self.remote_point_id = _Output(_get_output_spec_cyclic_expanded_displacement(3), 3, op) 

class _CyclicExpandedDisplacement:
    """Operator's description:
Internal name is "mapdl::rst::U_cyclic"
Scripting name is "cyclic_expanded_displacement"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::U_cyclic")
- using dpf.operators.result.cyclic_expanded_displacement()

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
"""
    def __init__(self):
         self._name = "mapdl::rst::U_cyclic"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCyclicExpandedDisplacement(self._op)
         self.outputs = _OutputSpecCyclicExpandedDisplacement(self._op)

def cyclic_expanded_displacement():
    return _CyclicExpandedDisplacement()

#internal name: mapdl::rst::A_cyclic
#scripting name: cyclic_expanded_acceleration
def _get_input_spec_cyclic_expanded_acceleration(pin):
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
    return inputs_dict_cyclic_expanded_acceleration[pin]

def _get_output_spec_cyclic_expanded_acceleration(pin):
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
    return outputs_dict_cyclic_expanded_acceleration[pin]

class _InputSpecCyclicExpandedAcceleration(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_cyclic_expanded_acceleration(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_cyclic_expanded_acceleration(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_cyclic_expanded_acceleration(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_cyclic_expanded_acceleration(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_cyclic_expanded_acceleration(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_cyclic_expanded_acceleration(5), 5, op, -1) 
        self.sector_mesh = _Input(_get_input_spec_cyclic_expanded_acceleration(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_cyclic_expanded_acceleration(9), 9, op, -1) 
        self.freq = _Input(_get_input_spec_cyclic_expanded_acceleration(12), 12, op, -1) 
        self.read_cyclic = _Input(_get_input_spec_cyclic_expanded_acceleration(14), 14, op, -1) 
        self.expanded_meshed_region = _Input(_get_input_spec_cyclic_expanded_acceleration(15), 15, op, -1) 
        self.cyclic_support = _Input(_get_input_spec_cyclic_expanded_acceleration(16), 16, op, -1) 
        self.sectors_to_expand = _Input(_get_input_spec_cyclic_expanded_acceleration(18), 18, op, -1) 
        self.phi = _Input(_get_input_spec_cyclic_expanded_acceleration(19), 19, op, -1) 
        self.filter_degenerated_elements = _Input(_get_input_spec_cyclic_expanded_acceleration(20), 20, op, -1) 

class _OutputSpecCyclicExpandedAcceleration(_Outputs):
    def __init__(self, op: _Operator):
        self.static_matrix = _Output(_get_output_spec_cyclic_expanded_acceleration(0), 0, op) 
        self.expanded_meshed_region = _Output(_get_output_spec_cyclic_expanded_acceleration(1), 1, op) 
        self.inertia_matrix = _Output(_get_output_spec_cyclic_expanded_acceleration(2), 2, op) 
        self.remote_point_id = _Output(_get_output_spec_cyclic_expanded_acceleration(3), 3, op) 

class _CyclicExpandedAcceleration:
    """Operator's description:
Internal name is "mapdl::rst::A_cyclic"
Scripting name is "cyclic_expanded_acceleration"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::A_cyclic")
- using dpf.operators.result.cyclic_expanded_acceleration()

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
"""
    def __init__(self):
         self._name = "mapdl::rst::A_cyclic"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCyclicExpandedAcceleration(self._op)
         self.outputs = _OutputSpecCyclicExpandedAcceleration(self._op)

def cyclic_expanded_acceleration():
    return _CyclicExpandedAcceleration()

#internal name: mapdl::rst::S_cyclic
#scripting name: cyclic_expanded_stress
def _get_input_spec_cyclic_expanded_stress(pin):
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
    return inputs_dict_cyclic_expanded_stress[pin]

def _get_output_spec_cyclic_expanded_stress(pin):
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
    return outputs_dict_cyclic_expanded_stress[pin]

class _InputSpecCyclicExpandedStress(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_cyclic_expanded_stress(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_cyclic_expanded_stress(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_cyclic_expanded_stress(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_cyclic_expanded_stress(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_cyclic_expanded_stress(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_cyclic_expanded_stress(5), 5, op, -1) 
        self.sector_mesh = _Input(_get_input_spec_cyclic_expanded_stress(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_cyclic_expanded_stress(9), 9, op, -1) 
        self.freq = _Input(_get_input_spec_cyclic_expanded_stress(12), 12, op, -1) 
        self.read_cyclic = _Input(_get_input_spec_cyclic_expanded_stress(14), 14, op, -1) 
        self.expanded_meshed_region = _Input(_get_input_spec_cyclic_expanded_stress(15), 15, op, -1) 
        self.cyclic_support = _Input(_get_input_spec_cyclic_expanded_stress(16), 16, op, -1) 
        self.sectors_to_expand = _Input(_get_input_spec_cyclic_expanded_stress(18), 18, op, -1) 
        self.phi = _Input(_get_input_spec_cyclic_expanded_stress(19), 19, op, -1) 
        self.filter_degenerated_elements = _Input(_get_input_spec_cyclic_expanded_stress(20), 20, op, -1) 

class _OutputSpecCyclicExpandedStress(_Outputs):
    def __init__(self, op: _Operator):
        self.static_matrix = _Output(_get_output_spec_cyclic_expanded_stress(0), 0, op) 
        self.expanded_meshed_region = _Output(_get_output_spec_cyclic_expanded_stress(1), 1, op) 
        self.inertia_matrix = _Output(_get_output_spec_cyclic_expanded_stress(2), 2, op) 
        self.remote_point_id = _Output(_get_output_spec_cyclic_expanded_stress(3), 3, op) 

class _CyclicExpandedStress:
    """Operator's description:
Internal name is "mapdl::rst::S_cyclic"
Scripting name is "cyclic_expanded_stress"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::S_cyclic")
- using dpf.operators.result.cyclic_expanded_stress()

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
"""
    def __init__(self):
         self._name = "mapdl::rst::S_cyclic"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCyclicExpandedStress(self._op)
         self.outputs = _OutputSpecCyclicExpandedStress(self._op)

def cyclic_expanded_stress():
    return _CyclicExpandedStress()

#internal name: mapdl::rst::ENG_VOL_cyclic
#scripting name: cyclic_volume
def _get_input_spec_cyclic_volume(pin):
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
    return inputs_dict_cyclic_volume[pin]

def _get_output_spec_cyclic_volume(pin):
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
    return outputs_dict_cyclic_volume[pin]

class _InputSpecCyclicVolume(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_cyclic_volume(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_cyclic_volume(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_cyclic_volume(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_cyclic_volume(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_cyclic_volume(4), 4, op, -1) 
        self.bool_rotate_to_global = _Input(_get_input_spec_cyclic_volume(5), 5, op, -1) 
        self.sector_mesh = _Input(_get_input_spec_cyclic_volume(7), 7, op, -1) 
        self.requested_location = _Input(_get_input_spec_cyclic_volume(9), 9, op, -1) 
        self.freq = _Input(_get_input_spec_cyclic_volume(12), 12, op, -1) 
        self.read_cyclic = _Input(_get_input_spec_cyclic_volume(14), 14, op, -1) 
        self.expanded_meshed_region = _Input(_get_input_spec_cyclic_volume(15), 15, op, -1) 
        self.cyclic_support = _Input(_get_input_spec_cyclic_volume(16), 16, op, -1) 
        self.sectors_to_expand = _Input(_get_input_spec_cyclic_volume(18), 18, op, -1) 
        self.phi = _Input(_get_input_spec_cyclic_volume(19), 19, op, -1) 
        self.filter_degenerated_elements = _Input(_get_input_spec_cyclic_volume(20), 20, op, -1) 

class _OutputSpecCyclicVolume(_Outputs):
    def __init__(self, op: _Operator):
        self.static_matrix = _Output(_get_output_spec_cyclic_volume(0), 0, op) 
        self.expanded_meshed_region = _Output(_get_output_spec_cyclic_volume(1), 1, op) 
        self.inertia_matrix = _Output(_get_output_spec_cyclic_volume(2), 2, op) 
        self.remote_point_id = _Output(_get_output_spec_cyclic_volume(3), 3, op) 

class _CyclicVolume:
    """Operator's description:
Internal name is "mapdl::rst::ENG_VOL_cyclic"
Scripting name is "cyclic_volume"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::rst::ENG_VOL_cyclic")
- using dpf.operators.result.cyclic_volume()

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
"""
    def __init__(self):
         self._name = "mapdl::rst::ENG_VOL_cyclic"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecCyclicVolume(self._op)
         self.outputs = _OutputSpecCyclicVolume(self._op)

def cyclic_volume():
    return _CyclicVolume()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from meshOperatorsCore.dll plugin, from "result" category
"""

#internal name: vtk::vtk::FieldProvider
#scripting name: to_field
def _get_input_spec_to_field(pin):
    inpin3 = _PinSpecification(name = "streams", type_names = ["streams_container"], optional = True, document = """streams""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = True, document = """data_sources""")
    inputs_dict_to_field = { 
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_to_field[pin]

def _get_output_spec_to_field(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """fields_container""")
    outputs_dict_to_field = { 
        0 : outpin0
    }
    return outputs_dict_to_field[pin]

class _InputSpecToField(_Inputs):
    def __init__(self, op: _Operator):
        self.streams = _Input(_get_input_spec_to_field(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_to_field(4), 4, op, -1) 

class _OutputSpecToField(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_to_field(0), 0, op) 

class _ToField:
    """Operator's description:
Internal name is "vtk::vtk::FieldProvider"
Scripting name is "to_field"

This operator can be instantiated in both following ways:
- using dpf.Operator("vtk::vtk::FieldProvider")
- using dpf.operators.result.to_field()

Input list: 
   3: streams (streams)
   4: data_sources (data_sources)
Output list: 
   0: fields_container (fields_container)
"""
    def __init__(self):
         self._name = "vtk::vtk::FieldProvider"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecToField(self._op)
         self.outputs = _OutputSpecToField(self._op)

def to_field():
    return _ToField()

