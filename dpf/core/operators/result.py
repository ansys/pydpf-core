"""
Result Operators
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native.dll plugin, from "result" category
"""

#internal name: EPPL1
#scripting name: plastic_strain_principal_1
class _InputsPlasticStrainPrincipal1(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_principal_1._spec().inputs, op)
        self.time_scoping = Input(plastic_strain_principal_1._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain_principal_1._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain_principal_1._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_principal_1._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_principal_1._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain_principal_1._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain_principal_1._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain_principal_1._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain_principal_1._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrainPrincipal1(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_principal_1._spec().outputs, op)
        self.fields_container = Output(plastic_strain_principal_1._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_principal_1(Operator):
    """Read/compute element nodal component plastic strains 1st principal component by calling the readers defined by the datasources and computing its eigen values.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_principal_1()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="EPPL1", config = config, server = server)
        self.inputs = _InputsPlasticStrainPrincipal1(self)
        self.outputs = _OutputsPlasticStrainPrincipal1(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component plastic strains 1st principal component by calling the readers defined by the datasources and computing its eigen values.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document=""""""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPPL1")

#internal name: EPPL3
#scripting name: plastic_strain_principal_3
class _InputsPlasticStrainPrincipal3(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_principal_3._spec().inputs, op)
        self.time_scoping = Input(plastic_strain_principal_3._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain_principal_3._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain_principal_3._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_principal_3._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_principal_3._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain_principal_3._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain_principal_3._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain_principal_3._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain_principal_3._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrainPrincipal3(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_principal_3._spec().outputs, op)
        self.fields_container = Output(plastic_strain_principal_3._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_principal_3(Operator):
    """Read/compute element nodal component plastic strains 3rd principal component by calling the readers defined by the datasources and computing its eigen values.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_principal_3()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="EPPL3", config = config, server = server)
        self.inputs = _InputsPlasticStrainPrincipal3(self)
        self.outputs = _OutputsPlasticStrainPrincipal3(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component plastic strains 3rd principal component by calling the readers defined by the datasources and computing its eigen values.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document=""""""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPPL3")

#internal name: RigidTransformationProvider
#scripting name: rigid_transformation
class _InputsRigidTransformation(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(rigid_transformation._spec().inputs, op)
        self.streams_container = Input(rigid_transformation._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(rigid_transformation._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsRigidTransformation(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(rigid_transformation._spec().outputs, op)
        self.fields_container = Output(rigid_transformation._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class rigid_transformation(Operator):
    """Extracts rigid body motions from a displacement in input.

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.rigid_transformation()

    """
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="RigidTransformationProvider", config = config, server = server)
        self.inputs = _InputsRigidTransformation(self)
        self.outputs = _OutputsRigidTransformation(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts rigid body motions from a displacement in input.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container) (optional)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "RigidTransformationProvider")

#internal name: EPELY
#scripting name: elastic_strain_Y
class _InputsElasticStrainY(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_Y._spec().inputs, op)
        self.time_scoping = Input(elastic_strain_Y._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain_Y._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain_Y._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_Y._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_Y._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain_Y._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain_Y._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain_Y._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain_Y._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrainY(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_Y._spec().outputs, op)
        self.fields_container = Output(elastic_strain_Y._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_Y(Operator):
    """Read/compute element nodal component elastic strains YY normal component (11 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_Y()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPELY", config = config, server = server)
        self.inputs = _InputsElasticStrainY(self)
        self.outputs = _OutputsElasticStrainY(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component elastic strains YY normal component (11 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPELY")

#internal name: M
#scripting name: nodal_moment
class _InputsNodalMoment(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_moment._spec().inputs, op)
        self.time_scoping = Input(nodal_moment._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_moment._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_moment._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_moment._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_moment._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(nodal_moment._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(nodal_moment._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(nodal_moment._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsNodalMoment(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_moment._spec().outputs, op)
        self.fields_container = Output(nodal_moment._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_moment(Operator):
    """Read/compute nodal moment by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_moment()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="M", config = config, server = server)
        self.inputs = _InputsNodalMoment(self)
        self.outputs = _OutputsNodalMoment(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal moment by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "M")

#internal name: ElementalMass
#scripting name: elemental_mass
class _InputsElementalMass(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_mass._spec().inputs, op)
        self.time_scoping = Input(elemental_mass._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elemental_mass._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elemental_mass._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elemental_mass._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elemental_mass._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elemental_mass._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elemental_mass._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(elemental_mass._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElementalMass(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_mass._spec().outputs, op)
        self.fields_container = Output(elemental_mass._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elemental_mass(Operator):
    """Read/compute element mass by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elemental_mass()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="ElementalMass", config = config, server = server)
        self.inputs = _InputsElementalMass(self)
        self.outputs = _OutputsElementalMass(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element mass by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ElementalMass")

#internal name: TF
#scripting name: heat_flux
class _InputsHeatFlux(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(heat_flux._spec().inputs, op)
        self.time_scoping = Input(heat_flux._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(heat_flux._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(heat_flux._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(heat_flux._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(heat_flux._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(heat_flux._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(heat_flux._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(heat_flux._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(heat_flux._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsHeatFlux(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(heat_flux._spec().outputs, op)
        self.fields_container = Output(heat_flux._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class heat_flux(Operator):
    """Read/compute heat flux by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.heat_flux()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="TF", config = config, server = server)
        self.inputs = _InputsHeatFlux(self)
        self.outputs = _OutputsHeatFlux(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute heat flux by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "TF")

#internal name: ENG_CO
#scripting name: co_energy
class _InputsCoEnergy(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(co_energy._spec().inputs, op)
        self.time_scoping = Input(co_energy._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(co_energy._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(co_energy._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(co_energy._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(co_energy._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(co_energy._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(co_energy._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(co_energy._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsCoEnergy(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(co_energy._spec().outputs, op)
        self.fields_container = Output(co_energy._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class co_energy(Operator):
    """Read/compute co-energy (magnetics) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.co_energy()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="ENG_CO", config = config, server = server)
        self.inputs = _InputsCoEnergy(self)
        self.outputs = _OutputsCoEnergy(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute co-energy (magnetics) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENG_CO")

#internal name: EPPL2
#scripting name: plastic_strain_principal_2
class _InputsPlasticStrainPrincipal2(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_principal_2._spec().inputs, op)
        self.time_scoping = Input(plastic_strain_principal_2._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain_principal_2._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain_principal_2._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_principal_2._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_principal_2._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain_principal_2._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain_principal_2._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain_principal_2._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain_principal_2._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrainPrincipal2(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_principal_2._spec().outputs, op)
        self.fields_container = Output(plastic_strain_principal_2._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_principal_2(Operator):
    """Read/compute element nodal component plastic strains 2nd principal component by calling the readers defined by the datasources and computing its eigen values.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_principal_2()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="EPPL2", config = config, server = server)
        self.inputs = _InputsPlasticStrainPrincipal2(self)
        self.outputs = _OutputsPlasticStrainPrincipal2(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component plastic strains 2nd principal component by calling the readers defined by the datasources and computing its eigen values.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document=""""""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPPL2")

#internal name: EPELZ
#scripting name: elastic_strain_Z
class _InputsElasticStrainZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_Z._spec().inputs, op)
        self.time_scoping = Input(elastic_strain_Z._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain_Z._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain_Z._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_Z._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_Z._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain_Z._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain_Z._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain_Z._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain_Z._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrainZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_Z._spec().outputs, op)
        self.fields_container = Output(elastic_strain_Z._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_Z(Operator):
    """Read/compute element nodal component elastic strains ZZ normal component (22 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_Z()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPELZ", config = config, server = server)
        self.inputs = _InputsElasticStrainZ(self)
        self.outputs = _OutputsElasticStrainZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component elastic strains ZZ normal component (22 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPELZ")

#internal name: S
#scripting name: stress
class _InputsStress(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress._spec().inputs, op)
        self.time_scoping = Input(stress._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStress(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress._spec().outputs, op)
        self.fields_container = Output(stress._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress(Operator):
    """Read/compute element nodal component stresses by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="S", config = config, server = server)
        self.inputs = _InputsStress(self)
        self.outputs = _OutputsStress(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component stresses by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "S")

#internal name: SX
#scripting name: stress_X
class _InputsStressX(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_X._spec().inputs, op)
        self.time_scoping = Input(stress_X._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_X._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_X._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_X._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_X._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_X._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_X._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_X._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_X._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressX(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_X._spec().outputs, op)
        self.fields_container = Output(stress_X._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_X(Operator):
    """Read/compute element nodal component stresses XX normal component (00 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_X()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="SX", config = config, server = server)
        self.inputs = _InputsStressX(self)
        self.outputs = _OutputsStressX(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component stresses XX normal component (00 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "SX")

#internal name: SY
#scripting name: stress_Y
class _InputsStressY(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_Y._spec().inputs, op)
        self.time_scoping = Input(stress_Y._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_Y._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_Y._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_Y._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_Y._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_Y._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_Y._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_Y._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_Y._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressY(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_Y._spec().outputs, op)
        self.fields_container = Output(stress_Y._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_Y(Operator):
    """Read/compute element nodal component stresses YY normal component (11 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_Y()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="SY", config = config, server = server)
        self.inputs = _InputsStressY(self)
        self.outputs = _OutputsStressY(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component stresses YY normal component (11 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "SY")

#internal name: SZ
#scripting name: stress_Z
class _InputsStressZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_Z._spec().inputs, op)
        self.time_scoping = Input(stress_Z._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_Z._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_Z._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_Z._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_Z._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_Z._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_Z._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_Z._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_Z._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_Z._spec().outputs, op)
        self.fields_container = Output(stress_Z._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_Z(Operator):
    """Read/compute element nodal component stresses ZZ normal component (22 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_Z()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="SZ", config = config, server = server)
        self.inputs = _InputsStressZ(self)
        self.outputs = _OutputsStressZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component stresses ZZ normal component (22 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "SZ")

#internal name: SXY
#scripting name: stress_XY
class _InputsStressXY(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_XY._spec().inputs, op)
        self.time_scoping = Input(stress_XY._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_XY._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_XY._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_XY._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_XY._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_XY._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_XY._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_XY._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_XY._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressXY(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_XY._spec().outputs, op)
        self.fields_container = Output(stress_XY._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_XY(Operator):
    """Read/compute element nodal component stresses XY shear component (01 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_XY()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="SXY", config = config, server = server)
        self.inputs = _InputsStressXY(self)
        self.outputs = _OutputsStressXY(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component stresses XY shear component (01 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "SXY")

#internal name: SYZ
#scripting name: stress_YZ
class _InputsStressYZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_YZ._spec().inputs, op)
        self.time_scoping = Input(stress_YZ._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_YZ._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_YZ._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_YZ._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_YZ._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_YZ._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_YZ._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_YZ._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_YZ._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressYZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_YZ._spec().outputs, op)
        self.fields_container = Output(stress_YZ._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_YZ(Operator):
    """Read/compute element nodal component stresses YZ shear component (12 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_YZ()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="SYZ", config = config, server = server)
        self.inputs = _InputsStressYZ(self)
        self.outputs = _OutputsStressYZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component stresses YZ shear component (12 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "SYZ")

#internal name: ModalBasis
#scripting name: modal_basis
class _InputsModalBasis(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(modal_basis._spec().inputs, op)
        self.time_scoping = Input(modal_basis._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(modal_basis._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(modal_basis._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(modal_basis._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(modal_basis._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(modal_basis._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(modal_basis._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(modal_basis._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsModalBasis(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(modal_basis._spec().outputs, op)
        self.fields_container = Output(modal_basis._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class modal_basis(Operator):
    """Read/compute modal basis by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.modal_basis()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="ModalBasis", config = config, server = server)
        self.inputs = _InputsModalBasis(self)
        self.outputs = _OutputsModalBasis(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute modal basis by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ModalBasis")

#internal name: SXZ
#scripting name: stress_XZ
class _InputsStressXZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_XZ._spec().inputs, op)
        self.time_scoping = Input(stress_XZ._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_XZ._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_XZ._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_XZ._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_XZ._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_XZ._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_XZ._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_XZ._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_XZ._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressXZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_XZ._spec().outputs, op)
        self.fields_container = Output(stress_XZ._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_XZ(Operator):
    """Read/compute element nodal component stresses XZ shear component (02 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_XZ()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="SXZ", config = config, server = server)
        self.inputs = _InputsStressXZ(self)
        self.outputs = _OutputsStressXZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component stresses XZ shear component (02 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "SXZ")

#internal name: S1
#scripting name: stress_principal_1
class _InputsStressPrincipal1(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_principal_1._spec().inputs, op)
        self.time_scoping = Input(stress_principal_1._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_principal_1._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_principal_1._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_principal_1._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_principal_1._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_principal_1._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_principal_1._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_principal_1._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_principal_1._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressPrincipal1(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_principal_1._spec().outputs, op)
        self.fields_container = Output(stress_principal_1._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_principal_1(Operator):
    """Read/compute element nodal component stresses 1st principal component by calling the readers defined by the datasources and computing its eigen values.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_principal_1()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="S1", config = config, server = server)
        self.inputs = _InputsStressPrincipal1(self)
        self.outputs = _OutputsStressPrincipal1(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component stresses 1st principal component by calling the readers defined by the datasources and computing its eigen values.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document=""""""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "S1")

#internal name: S2
#scripting name: stress_principal_2
class _InputsStressPrincipal2(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_principal_2._spec().inputs, op)
        self.time_scoping = Input(stress_principal_2._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_principal_2._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_principal_2._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_principal_2._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_principal_2._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_principal_2._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_principal_2._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_principal_2._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_principal_2._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressPrincipal2(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_principal_2._spec().outputs, op)
        self.fields_container = Output(stress_principal_2._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_principal_2(Operator):
    """Read/compute element nodal component stresses 2nd principal component by calling the readers defined by the datasources and computing its eigen values.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_principal_2()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="S2", config = config, server = server)
        self.inputs = _InputsStressPrincipal2(self)
        self.outputs = _OutputsStressPrincipal2(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component stresses 2nd principal component by calling the readers defined by the datasources and computing its eigen values.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document=""""""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "S2")

#internal name: S3
#scripting name: stress_principal_3
class _InputsStressPrincipal3(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_principal_3._spec().inputs, op)
        self.time_scoping = Input(stress_principal_3._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_principal_3._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_principal_3._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_principal_3._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_principal_3._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_principal_3._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_principal_3._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_principal_3._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_principal_3._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressPrincipal3(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_principal_3._spec().outputs, op)
        self.fields_container = Output(stress_principal_3._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_principal_3(Operator):
    """Read/compute element nodal component stresses 3rd principal component by calling the readers defined by the datasources and computing its eigen values.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_principal_3()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="S3", config = config, server = server)
        self.inputs = _InputsStressPrincipal3(self)
        self.outputs = _OutputsStressPrincipal3(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component stresses 3rd principal component by calling the readers defined by the datasources and computing its eigen values.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document=""""""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "S3")

#internal name: EPEL
#scripting name: elastic_strain
class _InputsElasticStrain(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain._spec().inputs, op)
        self.time_scoping = Input(elastic_strain._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrain(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain._spec().outputs, op)
        self.fields_container = Output(elastic_strain._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain(Operator):
    """Read/compute element nodal component elastic strains by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPEL", config = config, server = server)
        self.inputs = _InputsElasticStrain(self)
        self.outputs = _OutputsElasticStrain(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component elastic strains by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPEL")

#internal name: EPELX
#scripting name: elastic_strain_X
class _InputsElasticStrainX(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_X._spec().inputs, op)
        self.time_scoping = Input(elastic_strain_X._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain_X._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain_X._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_X._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_X._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain_X._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain_X._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain_X._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain_X._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrainX(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_X._spec().outputs, op)
        self.fields_container = Output(elastic_strain_X._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_X(Operator):
    """Read/compute element nodal component elastic strains XX normal component (00 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_X()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPELX", config = config, server = server)
        self.inputs = _InputsElasticStrainX(self)
        self.outputs = _OutputsElasticStrainX(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component elastic strains XX normal component (00 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPELX")

#internal name: EPELXY
#scripting name: elastic_strain_XY
class _InputsElasticStrainXY(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_XY._spec().inputs, op)
        self.time_scoping = Input(elastic_strain_XY._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain_XY._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain_XY._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_XY._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_XY._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain_XY._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain_XY._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain_XY._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain_XY._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrainXY(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_XY._spec().outputs, op)
        self.fields_container = Output(elastic_strain_XY._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_XY(Operator):
    """Read/compute element nodal component elastic strains XY shear component (01 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_XY()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPELXY", config = config, server = server)
        self.inputs = _InputsElasticStrainXY(self)
        self.outputs = _OutputsElasticStrainXY(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component elastic strains XY shear component (01 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPELXY")

#internal name: EPELYZ
#scripting name: elastic_strain_YZ
class _InputsElasticStrainYZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_YZ._spec().inputs, op)
        self.time_scoping = Input(elastic_strain_YZ._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain_YZ._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain_YZ._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_YZ._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_YZ._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain_YZ._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain_YZ._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain_YZ._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain_YZ._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrainYZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_YZ._spec().outputs, op)
        self.fields_container = Output(elastic_strain_YZ._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_YZ(Operator):
    """Read/compute element nodal component elastic strains YZ shear component (12 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_YZ()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPELYZ", config = config, server = server)
        self.inputs = _InputsElasticStrainYZ(self)
        self.outputs = _OutputsElasticStrainYZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component elastic strains YZ shear component (12 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPELYZ")

#internal name: EPELXZ
#scripting name: elastic_strain_XZ
class _InputsElasticStrainXZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_XZ._spec().inputs, op)
        self.time_scoping = Input(elastic_strain_XZ._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain_XZ._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain_XZ._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_XZ._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_XZ._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain_XZ._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain_XZ._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain_XZ._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain_XZ._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrainXZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_XZ._spec().outputs, op)
        self.fields_container = Output(elastic_strain_XZ._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_XZ(Operator):
    """Read/compute element nodal component elastic strains XZ shear component (02 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_XZ()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPELXZ", config = config, server = server)
        self.inputs = _InputsElasticStrainXZ(self)
        self.outputs = _OutputsElasticStrainXZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component elastic strains XZ shear component (02 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPELXZ")

#internal name: EPEL1
#scripting name: elastic_strain_principal_1
class _InputsElasticStrainPrincipal1(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_principal_1._spec().inputs, op)
        self.time_scoping = Input(elastic_strain_principal_1._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain_principal_1._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain_principal_1._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_principal_1._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_principal_1._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain_principal_1._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain_principal_1._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain_principal_1._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain_principal_1._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrainPrincipal1(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_principal_1._spec().outputs, op)
        self.fields_container = Output(elastic_strain_principal_1._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_principal_1(Operator):
    """Read/compute element nodal component elastic strains 1st principal component by calling the readers defined by the datasources and computing its eigen values.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_principal_1()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="EPEL1", config = config, server = server)
        self.inputs = _InputsElasticStrainPrincipal1(self)
        self.outputs = _OutputsElasticStrainPrincipal1(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component elastic strains 1st principal component by calling the readers defined by the datasources and computing its eigen values.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document=""""""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPEL1")

#internal name: EPEL2
#scripting name: elastic_strain_principal_2
class _InputsElasticStrainPrincipal2(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_principal_2._spec().inputs, op)
        self.time_scoping = Input(elastic_strain_principal_2._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain_principal_2._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain_principal_2._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_principal_2._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_principal_2._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain_principal_2._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain_principal_2._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain_principal_2._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain_principal_2._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrainPrincipal2(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_principal_2._spec().outputs, op)
        self.fields_container = Output(elastic_strain_principal_2._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_principal_2(Operator):
    """Read/compute element nodal component elastic strains 2nd principal component by calling the readers defined by the datasources and computing its eigen values.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_principal_2()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="EPEL2", config = config, server = server)
        self.inputs = _InputsElasticStrainPrincipal2(self)
        self.outputs = _OutputsElasticStrainPrincipal2(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component elastic strains 2nd principal component by calling the readers defined by the datasources and computing its eigen values.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document=""""""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPEL2")

#internal name: EPEL3
#scripting name: elastic_strain_principal_3
class _InputsElasticStrainPrincipal3(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_principal_3._spec().inputs, op)
        self.time_scoping = Input(elastic_strain_principal_3._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain_principal_3._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain_principal_3._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_principal_3._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_principal_3._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain_principal_3._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain_principal_3._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain_principal_3._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain_principal_3._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrainPrincipal3(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_principal_3._spec().outputs, op)
        self.fields_container = Output(elastic_strain_principal_3._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_principal_3(Operator):
    """Read/compute element nodal component elastic strains 3rd principal component by calling the readers defined by the datasources and computing its eigen values.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_principal_3()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="EPEL3", config = config, server = server)
        self.inputs = _InputsElasticStrainPrincipal3(self)
        self.outputs = _OutputsElasticStrainPrincipal3(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component elastic strains 3rd principal component by calling the readers defined by the datasources and computing its eigen values.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document=""""""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPEL3")

#internal name: EPPL
#scripting name: plastic_strain
class _InputsPlasticStrain(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain._spec().inputs, op)
        self.time_scoping = Input(plastic_strain._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrain(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain._spec().outputs, op)
        self.fields_container = Output(plastic_strain._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain(Operator):
    """Read/compute element nodal component plastic strains by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPPL", config = config, server = server)
        self.inputs = _InputsPlasticStrain(self)
        self.outputs = _OutputsPlasticStrain(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component plastic strains by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPPL")

#internal name: EPPLX
#scripting name: plastic_strain_X
class _InputsPlasticStrainX(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_X._spec().inputs, op)
        self.time_scoping = Input(plastic_strain_X._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain_X._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain_X._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_X._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_X._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain_X._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain_X._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain_X._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain_X._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrainX(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_X._spec().outputs, op)
        self.fields_container = Output(plastic_strain_X._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_X(Operator):
    """Read/compute element nodal component plastic strains XX normal component (00 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_X()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPPLX", config = config, server = server)
        self.inputs = _InputsPlasticStrainX(self)
        self.outputs = _OutputsPlasticStrainX(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component plastic strains XX normal component (00 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPPLX")

#internal name: EPPLY
#scripting name: plastic_strain_Y
class _InputsPlasticStrainY(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_Y._spec().inputs, op)
        self.time_scoping = Input(plastic_strain_Y._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain_Y._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain_Y._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_Y._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_Y._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain_Y._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain_Y._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain_Y._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain_Y._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrainY(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_Y._spec().outputs, op)
        self.fields_container = Output(plastic_strain_Y._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_Y(Operator):
    """Read/compute element nodal component plastic strains YY normal component (11 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_Y()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPPLY", config = config, server = server)
        self.inputs = _InputsPlasticStrainY(self)
        self.outputs = _OutputsPlasticStrainY(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component plastic strains YY normal component (11 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPPLY")

#internal name: EPPLZ
#scripting name: plastic_strain_Z
class _InputsPlasticStrainZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_Z._spec().inputs, op)
        self.time_scoping = Input(plastic_strain_Z._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain_Z._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain_Z._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_Z._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_Z._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain_Z._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain_Z._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain_Z._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain_Z._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrainZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_Z._spec().outputs, op)
        self.fields_container = Output(plastic_strain_Z._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_Z(Operator):
    """Read/compute element nodal component plastic strains ZZ normal component (22 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_Z()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPPLZ", config = config, server = server)
        self.inputs = _InputsPlasticStrainZ(self)
        self.outputs = _OutputsPlasticStrainZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component plastic strains ZZ normal component (22 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPPLZ")

#internal name: ENL_HPRES
#scripting name: hydrostatic_pressure
class _InputsHydrostaticPressure(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(hydrostatic_pressure._spec().inputs, op)
        self.time_scoping = Input(hydrostatic_pressure._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(hydrostatic_pressure._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(hydrostatic_pressure._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(hydrostatic_pressure._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(hydrostatic_pressure._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(hydrostatic_pressure._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(hydrostatic_pressure._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(hydrostatic_pressure._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(hydrostatic_pressure._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsHydrostaticPressure(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(hydrostatic_pressure._spec().outputs, op)
        self.fields_container = Output(hydrostatic_pressure._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class hydrostatic_pressure(Operator):
    """Read/compute element nodal hydrostatic pressure by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.hydrostatic_pressure()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ENL_HPRES", config = config, server = server)
        self.inputs = _InputsHydrostaticPressure(self)
        self.outputs = _OutputsHydrostaticPressure(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal hydrostatic pressure by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENL_HPRES")

#internal name: EPPLXY
#scripting name: plastic_strain_XY
class _InputsPlasticStrainXY(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_XY._spec().inputs, op)
        self.time_scoping = Input(plastic_strain_XY._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain_XY._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain_XY._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_XY._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_XY._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain_XY._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain_XY._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain_XY._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain_XY._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrainXY(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_XY._spec().outputs, op)
        self.fields_container = Output(plastic_strain_XY._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_XY(Operator):
    """Read/compute element nodal component plastic strains XY shear component (01 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_XY()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPPLXY", config = config, server = server)
        self.inputs = _InputsPlasticStrainXY(self)
        self.outputs = _OutputsPlasticStrainXY(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component plastic strains XY shear component (01 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPPLXY")

#internal name: EPPLYZ
#scripting name: plastic_strain_YZ
class _InputsPlasticStrainYZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_YZ._spec().inputs, op)
        self.time_scoping = Input(plastic_strain_YZ._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain_YZ._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain_YZ._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_YZ._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_YZ._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain_YZ._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain_YZ._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain_YZ._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain_YZ._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrainYZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_YZ._spec().outputs, op)
        self.fields_container = Output(plastic_strain_YZ._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_YZ(Operator):
    """Read/compute element nodal component plastic strains YZ shear component (12 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_YZ()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPPLYZ", config = config, server = server)
        self.inputs = _InputsPlasticStrainYZ(self)
        self.outputs = _OutputsPlasticStrainYZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component plastic strains YZ shear component (12 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPPLYZ")

#internal name: EPPLXZ
#scripting name: plastic_strain_XZ
class _InputsPlasticStrainXZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_XZ._spec().inputs, op)
        self.time_scoping = Input(plastic_strain_XZ._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain_XZ._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain_XZ._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_XZ._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_XZ._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain_XZ._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain_XZ._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain_XZ._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain_XZ._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrainXZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_XZ._spec().outputs, op)
        self.fields_container = Output(plastic_strain_XZ._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_XZ(Operator):
    """Read/compute element nodal component plastic strains XZ shear component (02 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_XZ()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EPPLXZ", config = config, server = server)
        self.inputs = _InputsPlasticStrainXZ(self)
        self.outputs = _OutputsPlasticStrainXZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component plastic strains XZ shear component (02 component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EPPLXZ")

#internal name: A
#scripting name: acceleration
class _InputsAcceleration(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(acceleration._spec().inputs, op)
        self.time_scoping = Input(acceleration._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(acceleration._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(acceleration._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(acceleration._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(acceleration._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(acceleration._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(acceleration._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(acceleration._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsAcceleration(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(acceleration._spec().outputs, op)
        self.fields_container = Output(acceleration._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class acceleration(Operator):
    """Read/compute nodal accelerations by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.acceleration()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="A", config = config, server = server)
        self.inputs = _InputsAcceleration(self)
        self.outputs = _OutputsAcceleration(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal accelerations by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "A")

#internal name: AX
#scripting name: acceleration_X
class _InputsAccelerationX(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(acceleration_X._spec().inputs, op)
        self.time_scoping = Input(acceleration_X._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(acceleration_X._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(acceleration_X._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(acceleration_X._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(acceleration_X._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(acceleration_X._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(acceleration_X._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(acceleration_X._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsAccelerationX(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(acceleration_X._spec().outputs, op)
        self.fields_container = Output(acceleration_X._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class acceleration_X(Operator):
    """Read/compute nodal accelerations X component of the vector (1st component) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.acceleration_X()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="AX", config = config, server = server)
        self.inputs = _InputsAccelerationX(self)
        self.outputs = _OutputsAccelerationX(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal accelerations X component of the vector (1st component) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "AX")

#internal name: AY
#scripting name: acceleration_Y
class _InputsAccelerationY(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(acceleration_Y._spec().inputs, op)
        self.time_scoping = Input(acceleration_Y._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(acceleration_Y._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(acceleration_Y._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(acceleration_Y._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(acceleration_Y._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(acceleration_Y._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(acceleration_Y._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(acceleration_Y._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsAccelerationY(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(acceleration_Y._spec().outputs, op)
        self.fields_container = Output(acceleration_Y._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class acceleration_Y(Operator):
    """Read/compute nodal accelerations Y component of the vector (2nd component) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.acceleration_Y()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="AY", config = config, server = server)
        self.inputs = _InputsAccelerationY(self)
        self.outputs = _OutputsAccelerationY(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal accelerations Y component of the vector (2nd component) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "AY")

#internal name: centroids
#scripting name: element_centroids
class _InputsElementCentroids(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(element_centroids._spec().inputs, op)
        self.time_scoping = Input(element_centroids._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(element_centroids._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(element_centroids._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(element_centroids._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(element_centroids._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(element_centroids._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(element_centroids._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(element_centroids._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElementCentroids(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(element_centroids._spec().outputs, op)
        self.fields_container = Output(element_centroids._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class element_centroids(Operator):
    """Read/compute coordinate of the elemental centroids by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.element_centroids()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="centroids", config = config, server = server)
        self.inputs = _InputsElementCentroids(self)
        self.outputs = _OutputsElementCentroids(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute coordinate of the elemental centroids by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "centroids")

#internal name: AZ
#scripting name: acceleration_Z
class _InputsAccelerationZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(acceleration_Z._spec().inputs, op)
        self.time_scoping = Input(acceleration_Z._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(acceleration_Z._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(acceleration_Z._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(acceleration_Z._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(acceleration_Z._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(acceleration_Z._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(acceleration_Z._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(acceleration_Z._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsAccelerationZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(acceleration_Z._spec().outputs, op)
        self.fields_container = Output(acceleration_Z._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class acceleration_Z(Operator):
    """Read/compute nodal accelerations Z component of the vector (3rd component) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.acceleration_Z()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="AZ", config = config, server = server)
        self.inputs = _InputsAccelerationZ(self)
        self.outputs = _OutputsAccelerationZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal accelerations Z component of the vector (3rd component) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "AZ")

#internal name: RF
#scripting name: reaction_force
class _InputsReactionForce(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(reaction_force._spec().inputs, op)
        self.time_scoping = Input(reaction_force._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(reaction_force._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(reaction_force._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(reaction_force._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(reaction_force._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(reaction_force._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(reaction_force._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(reaction_force._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsReactionForce(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(reaction_force._spec().outputs, op)
        self.fields_container = Output(reaction_force._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class reaction_force(Operator):
    """Read/compute nodal reaction forces by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.reaction_force()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="RF", config = config, server = server)
        self.inputs = _InputsReactionForce(self)
        self.outputs = _OutputsReactionForce(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal reaction forces by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "RF")

#internal name: V
#scripting name: velocity
class _InputsVelocity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(velocity._spec().inputs, op)
        self.time_scoping = Input(velocity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(velocity._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(velocity._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(velocity._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(velocity._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(velocity._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(velocity._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(velocity._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsVelocity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(velocity._spec().outputs, op)
        self.fields_container = Output(velocity._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class velocity(Operator):
    """Read/compute nodal velocities by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.velocity()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="V", config = config, server = server)
        self.inputs = _InputsVelocity(self)
        self.outputs = _OutputsVelocity(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal velocities by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "V")

#internal name: VX
#scripting name: velocity_X
class _InputsVelocityX(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(velocity_X._spec().inputs, op)
        self.time_scoping = Input(velocity_X._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(velocity_X._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(velocity_X._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(velocity_X._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(velocity_X._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(velocity_X._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(velocity_X._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(velocity_X._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsVelocityX(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(velocity_X._spec().outputs, op)
        self.fields_container = Output(velocity_X._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class velocity_X(Operator):
    """Read/compute nodal velocities X component of the vector (1st component) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.velocity_X()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="VX", config = config, server = server)
        self.inputs = _InputsVelocityX(self)
        self.outputs = _OutputsVelocityX(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal velocities X component of the vector (1st component) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "VX")

#internal name: VY
#scripting name: velocity_Y
class _InputsVelocityY(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(velocity_Y._spec().inputs, op)
        self.time_scoping = Input(velocity_Y._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(velocity_Y._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(velocity_Y._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(velocity_Y._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(velocity_Y._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(velocity_Y._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(velocity_Y._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(velocity_Y._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsVelocityY(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(velocity_Y._spec().outputs, op)
        self.fields_container = Output(velocity_Y._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class velocity_Y(Operator):
    """Read/compute nodal velocities Y component of the vector (2nd component) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.velocity_Y()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="VY", config = config, server = server)
        self.inputs = _InputsVelocityY(self)
        self.outputs = _OutputsVelocityY(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal velocities Y component of the vector (2nd component) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "VY")

#internal name: VZ
#scripting name: velocity_Z
class _InputsVelocityZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(velocity_Z._spec().inputs, op)
        self.time_scoping = Input(velocity_Z._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(velocity_Z._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(velocity_Z._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(velocity_Z._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(velocity_Z._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(velocity_Z._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(velocity_Z._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(velocity_Z._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsVelocityZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(velocity_Z._spec().outputs, op)
        self.fields_container = Output(velocity_Z._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class velocity_Z(Operator):
    """Read/compute nodal velocities Z component of the vector (3rd component) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.velocity_Z()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="VZ", config = config, server = server)
        self.inputs = _InputsVelocityZ(self)
        self.outputs = _OutputsVelocityZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal velocities Z component of the vector (3rd component) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "VZ")

#internal name: U
#scripting name: displacement
class _InputsDisplacement(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(displacement._spec().inputs, op)
        self.time_scoping = Input(displacement._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(displacement._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(displacement._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(displacement._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(displacement._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(displacement._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(displacement._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(displacement._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsDisplacement(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(displacement._spec().outputs, op)
        self.fields_container = Output(displacement._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class displacement(Operator):
    """Read/compute nodal displacements by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.displacement()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="U", config = config, server = server)
        self.inputs = _InputsDisplacement(self)
        self.outputs = _OutputsDisplacement(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal displacements by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "U")

#internal name: UX
#scripting name: displacement_X
class _InputsDisplacementX(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(displacement_X._spec().inputs, op)
        self.time_scoping = Input(displacement_X._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(displacement_X._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(displacement_X._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(displacement_X._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(displacement_X._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(displacement_X._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(displacement_X._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(displacement_X._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsDisplacementX(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(displacement_X._spec().outputs, op)
        self.fields_container = Output(displacement_X._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class displacement_X(Operator):
    """Read/compute nodal displacements X component of the vector (1st component) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.displacement_X()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="UX", config = config, server = server)
        self.inputs = _InputsDisplacementX(self)
        self.outputs = _OutputsDisplacementX(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal displacements X component of the vector (1st component) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "UX")

#internal name: UY
#scripting name: displacement_Y
class _InputsDisplacementY(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(displacement_Y._spec().inputs, op)
        self.time_scoping = Input(displacement_Y._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(displacement_Y._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(displacement_Y._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(displacement_Y._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(displacement_Y._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(displacement_Y._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(displacement_Y._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(displacement_Y._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsDisplacementY(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(displacement_Y._spec().outputs, op)
        self.fields_container = Output(displacement_Y._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class displacement_Y(Operator):
    """Read/compute nodal displacements Y component of the vector (2nd component) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.displacement_Y()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="UY", config = config, server = server)
        self.inputs = _InputsDisplacementY(self)
        self.outputs = _OutputsDisplacementY(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal displacements Y component of the vector (2nd component) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "UY")

#internal name: UZ
#scripting name: displacement_Z
class _InputsDisplacementZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(displacement_Z._spec().inputs, op)
        self.time_scoping = Input(displacement_Z._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(displacement_Z._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(displacement_Z._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(displacement_Z._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(displacement_Z._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(displacement_Z._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(displacement_Z._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(displacement_Z._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsDisplacementZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(displacement_Z._spec().outputs, op)
        self.fields_container = Output(displacement_Z._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class displacement_Z(Operator):
    """Read/compute nodal displacements Z component of the vector (3rd component) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.displacement_Z()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="UZ", config = config, server = server)
        self.inputs = _InputsDisplacementZ(self)
        self.outputs = _OutputsDisplacementZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal displacements Z component of the vector (3rd component) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "UZ")

#internal name: TFX
#scripting name: heat_flux_X
class _InputsHeatFluxX(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(heat_flux_X._spec().inputs, op)
        self.time_scoping = Input(heat_flux_X._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(heat_flux_X._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(heat_flux_X._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(heat_flux_X._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(heat_flux_X._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(heat_flux_X._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(heat_flux_X._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(heat_flux_X._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(heat_flux_X._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsHeatFluxX(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(heat_flux_X._spec().outputs, op)
        self.fields_container = Output(heat_flux_X._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class heat_flux_X(Operator):
    """Read/compute heat flux X component of the vector (1st component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.heat_flux_X()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="TFX", config = config, server = server)
        self.inputs = _InputsHeatFluxX(self)
        self.outputs = _OutputsHeatFluxX(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute heat flux X component of the vector (1st component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "TFX")

#internal name: EF
#scripting name: electric_field
class _InputsElectricField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(electric_field._spec().inputs, op)
        self.time_scoping = Input(electric_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(electric_field._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(electric_field._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(electric_field._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(electric_field._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(electric_field._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(electric_field._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(electric_field._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(electric_field._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElectricField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(electric_field._spec().outputs, op)
        self.fields_container = Output(electric_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class electric_field(Operator):
    """Read/compute electric field by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.electric_field()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="EF", config = config, server = server)
        self.inputs = _InputsElectricField(self)
        self.outputs = _OutputsElectricField(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute electric field by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "EF")

#internal name: TFY
#scripting name: heat_flux_Y
class _InputsHeatFluxY(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(heat_flux_Y._spec().inputs, op)
        self.time_scoping = Input(heat_flux_Y._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(heat_flux_Y._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(heat_flux_Y._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(heat_flux_Y._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(heat_flux_Y._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(heat_flux_Y._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(heat_flux_Y._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(heat_flux_Y._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(heat_flux_Y._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsHeatFluxY(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(heat_flux_Y._spec().outputs, op)
        self.fields_container = Output(heat_flux_Y._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class heat_flux_Y(Operator):
    """Read/compute heat flux Y component of the vector (2nd component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.heat_flux_Y()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="TFY", config = config, server = server)
        self.inputs = _InputsHeatFluxY(self)
        self.outputs = _OutputsHeatFluxY(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute heat flux Y component of the vector (2nd component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "TFY")

#internal name: TFZ
#scripting name: heat_flux_Z
class _InputsHeatFluxZ(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(heat_flux_Z._spec().inputs, op)
        self.time_scoping = Input(heat_flux_Z._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(heat_flux_Z._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(heat_flux_Z._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(heat_flux_Z._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(heat_flux_Z._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(heat_flux_Z._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(heat_flux_Z._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(heat_flux_Z._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(heat_flux_Z._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsHeatFluxZ(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(heat_flux_Z._spec().outputs, op)
        self.fields_container = Output(heat_flux_Z._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class heat_flux_Z(Operator):
    """Read/compute heat flux Z component of the vector (3rd component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.heat_flux_Z()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="TFZ", config = config, server = server)
        self.inputs = _InputsHeatFluxZ(self)
        self.outputs = _OutputsHeatFluxZ(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute heat flux Z component of the vector (3rd component) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location, default is Nodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "TFZ")

#internal name: ENF
#scripting name: element_nodal_forces
class _InputsElementNodalForces(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(element_nodal_forces._spec().inputs, op)
        self.time_scoping = Input(element_nodal_forces._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(element_nodal_forces._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(element_nodal_forces._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(element_nodal_forces._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(element_nodal_forces._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(element_nodal_forces._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(element_nodal_forces._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(element_nodal_forces._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(element_nodal_forces._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElementNodalForces(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(element_nodal_forces._spec().outputs, op)
        self.fields_container = Output(element_nodal_forces._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class element_nodal_forces(Operator):
    """Read/compute element nodal forces by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.element_nodal_forces()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ENF", config = config, server = server)
        self.inputs = _InputsElementNodalForces(self)
        self.outputs = _OutputsElementNodalForces(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal forces by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENF")

#internal name: BFE
#scripting name: structural_temperature
class _InputsStructuralTemperature(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(structural_temperature._spec().inputs, op)
        self.time_scoping = Input(structural_temperature._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(structural_temperature._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(structural_temperature._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(structural_temperature._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(structural_temperature._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(structural_temperature._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(structural_temperature._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(structural_temperature._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(structural_temperature._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStructuralTemperature(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(structural_temperature._spec().outputs, op)
        self.fields_container = Output(structural_temperature._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class structural_temperature(Operator):
    """Read/compute element structural nodal temperatures by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.structural_temperature()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="BFE", config = config, server = server)
        self.inputs = _InputsStructuralTemperature(self)
        self.outputs = _OutputsStructuralTemperature(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element structural nodal temperatures by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "BFE")

#internal name: ENG_INC
#scripting name: incremental_energy
class _InputsIncrementalEnergy(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(incremental_energy._spec().inputs, op)
        self.time_scoping = Input(incremental_energy._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(incremental_energy._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(incremental_energy._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(incremental_energy._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(incremental_energy._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(incremental_energy._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(incremental_energy._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(incremental_energy._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsIncrementalEnergy(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(incremental_energy._spec().outputs, op)
        self.fields_container = Output(incremental_energy._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class incremental_energy(Operator):
    """Read/compute incremental energy (magnetics) by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.incremental_energy()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="ENG_INC", config = config, server = server)
        self.inputs = _InputsIncrementalEnergy(self)
        self.outputs = _OutputsIncrementalEnergy(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute incremental energy (magnetics) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENG_INC")

#internal name: ENG_SE
#scripting name: stiffness_matrix_energy
class _InputsStiffnessMatrixEnergy(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stiffness_matrix_energy._spec().inputs, op)
        self.time_scoping = Input(stiffness_matrix_energy._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stiffness_matrix_energy._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stiffness_matrix_energy._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stiffness_matrix_energy._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stiffness_matrix_energy._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stiffness_matrix_energy._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stiffness_matrix_energy._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(stiffness_matrix_energy._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStiffnessMatrixEnergy(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stiffness_matrix_energy._spec().outputs, op)
        self.fields_container = Output(stiffness_matrix_energy._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stiffness_matrix_energy(Operator):
    """Read/compute element energy associated with the stiffness matrix by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stiffness_matrix_energy()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="ENG_SE", config = config, server = server)
        self.inputs = _InputsStiffnessMatrixEnergy(self)
        self.outputs = _OutputsStiffnessMatrixEnergy(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element energy associated with the stiffness matrix by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENG_SE")

#internal name: ETH
#scripting name: thermal_strain
class _InputsThermalStrain(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(thermal_strain._spec().inputs, op)
        self.time_scoping = Input(thermal_strain._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(thermal_strain._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(thermal_strain._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(thermal_strain._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(thermal_strain._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(thermal_strain._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(thermal_strain._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(thermal_strain._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(thermal_strain._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsThermalStrain(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(thermal_strain._spec().outputs, op)
        self.fields_container = Output(thermal_strain._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class thermal_strain(Operator):
    """Read/compute element nodal component thermal strains by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.thermal_strain()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ETH", config = config, server = server)
        self.inputs = _InputsThermalStrain(self)
        self.outputs = _OutputsThermalStrain(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal component thermal strains by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ETH")

#internal name: ENL_SEPL
#scripting name: eqv_stress_parameter
class _InputsEqvStressParameter(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(eqv_stress_parameter._spec().inputs, op)
        self.time_scoping = Input(eqv_stress_parameter._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(eqv_stress_parameter._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(eqv_stress_parameter._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(eqv_stress_parameter._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(eqv_stress_parameter._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(eqv_stress_parameter._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(eqv_stress_parameter._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(eqv_stress_parameter._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(eqv_stress_parameter._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsEqvStressParameter(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(eqv_stress_parameter._spec().outputs, op)
        self.fields_container = Output(eqv_stress_parameter._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class eqv_stress_parameter(Operator):
    """Read/compute element nodal equivalent stress parameter by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.eqv_stress_parameter()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ENL_SEPL", config = config, server = server)
        self.inputs = _InputsEqvStressParameter(self)
        self.outputs = _OutputsEqvStressParameter(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal equivalent stress parameter by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENL_SEPL")

#internal name: ENL_SRAT
#scripting name: stress_ratio
class _InputsStressRatio(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_ratio._spec().inputs, op)
        self.time_scoping = Input(stress_ratio._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_ratio._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_ratio._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_ratio._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_ratio._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_ratio._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_ratio._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_ratio._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_ratio._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressRatio(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_ratio._spec().outputs, op)
        self.fields_container = Output(stress_ratio._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_ratio(Operator):
    """Read/compute element nodal stress ratio by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_ratio()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ENL_SRAT", config = config, server = server)
        self.inputs = _InputsStressRatio(self)
        self.outputs = _OutputsStressRatio(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal stress ratio by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENL_SRAT")

#internal name: ENL_EPEQ
#scripting name: accu_eqv_plastic_strain
class _InputsAccuEqvPlasticStrain(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(accu_eqv_plastic_strain._spec().inputs, op)
        self.time_scoping = Input(accu_eqv_plastic_strain._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(accu_eqv_plastic_strain._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(accu_eqv_plastic_strain._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(accu_eqv_plastic_strain._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(accu_eqv_plastic_strain._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(accu_eqv_plastic_strain._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(accu_eqv_plastic_strain._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(accu_eqv_plastic_strain._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(accu_eqv_plastic_strain._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsAccuEqvPlasticStrain(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(accu_eqv_plastic_strain._spec().outputs, op)
        self.fields_container = Output(accu_eqv_plastic_strain._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class accu_eqv_plastic_strain(Operator):
    """Read/compute element nodal accumulated equivalent plastic strain by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.accu_eqv_plastic_strain()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ENL_EPEQ", config = config, server = server)
        self.inputs = _InputsAccuEqvPlasticStrain(self)
        self.outputs = _OutputsAccuEqvPlasticStrain(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal accumulated equivalent plastic strain by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENL_EPEQ")

#internal name: ENL_PSV
#scripting name: plastic_state_variable
class _InputsPlasticStateVariable(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_state_variable._spec().inputs, op)
        self.time_scoping = Input(plastic_state_variable._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_state_variable._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_state_variable._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_state_variable._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_state_variable._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_state_variable._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_state_variable._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_state_variable._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_state_variable._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStateVariable(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_state_variable._spec().outputs, op)
        self.fields_container = Output(plastic_state_variable._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_state_variable(Operator):
    """Read/compute element nodal plastic state variable by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_state_variable()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ENL_PSV", config = config, server = server)
        self.inputs = _InputsPlasticStateVariable(self)
        self.outputs = _OutputsPlasticStateVariable(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal plastic state variable by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENL_PSV")

#internal name: ENL_CREQ
#scripting name: accu_eqv_creep_strain
class _InputsAccuEqvCreepStrain(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(accu_eqv_creep_strain._spec().inputs, op)
        self.time_scoping = Input(accu_eqv_creep_strain._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(accu_eqv_creep_strain._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(accu_eqv_creep_strain._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(accu_eqv_creep_strain._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(accu_eqv_creep_strain._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(accu_eqv_creep_strain._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(accu_eqv_creep_strain._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(accu_eqv_creep_strain._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(accu_eqv_creep_strain._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsAccuEqvCreepStrain(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(accu_eqv_creep_strain._spec().outputs, op)
        self.fields_container = Output(accu_eqv_creep_strain._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class accu_eqv_creep_strain(Operator):
    """Read/compute element nodal accumulated equivalent creep strain by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.accu_eqv_creep_strain()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ENL_CREQ", config = config, server = server)
        self.inputs = _InputsAccuEqvCreepStrain(self)
        self.outputs = _OutputsAccuEqvCreepStrain(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal accumulated equivalent creep strain by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENL_CREQ")

#internal name: ENL_PLWK
#scripting name: plastic_strain_energy_density
class _InputsPlasticStrainEnergyDensity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_energy_density._spec().inputs, op)
        self.time_scoping = Input(plastic_strain_energy_density._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(plastic_strain_energy_density._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(plastic_strain_energy_density._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_energy_density._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_energy_density._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(plastic_strain_energy_density._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(plastic_strain_energy_density._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(plastic_strain_energy_density._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(plastic_strain_energy_density._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsPlasticStrainEnergyDensity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_energy_density._spec().outputs, op)
        self.fields_container = Output(plastic_strain_energy_density._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_energy_density(Operator):
    """Read/compute element nodal plastic strain energy density by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_energy_density()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ENL_PLWK", config = config, server = server)
        self.inputs = _InputsPlasticStrainEnergyDensity(self)
        self.outputs = _OutputsPlasticStrainEnergyDensity(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal plastic strain energy density by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENL_PLWK")

#internal name: MaterialPropertyOfElement
#scripting name: material_property_of_element
class _InputsMaterialPropertyOfElement(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(material_property_of_element._spec().inputs, op)
        self.streams_container = Input(material_property_of_element._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(material_property_of_element._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsMaterialPropertyOfElement(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(material_property_of_element._spec().outputs, op)
        self.material_properties = Output(material_property_of_element._spec().output_pin(0), 0, op) 
        self._outputs.append(self.material_properties)

class material_property_of_element(Operator):
    """ Load the appropriate operator based on the data sources and get material properties

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         material_properties (Field)

      Examples
      --------
      >>> op = operators.result.material_property_of_element()

    """
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="MaterialPropertyOfElement", config = config, server = server)
        self.inputs = _InputsMaterialPropertyOfElement(self)
        self.outputs = _OutputsMaterialPropertyOfElement(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description=""" Load the appropriate operator based on the data sources and get material properties""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "material_properties", type_names=["field"], optional=False, document="""material properties""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "MaterialPropertyOfElement")

#internal name: ENL_CRWK
#scripting name: creep_strain_energy_density
class _InputsCreepStrainEnergyDensity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(creep_strain_energy_density._spec().inputs, op)
        self.time_scoping = Input(creep_strain_energy_density._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(creep_strain_energy_density._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(creep_strain_energy_density._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(creep_strain_energy_density._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(creep_strain_energy_density._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(creep_strain_energy_density._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(creep_strain_energy_density._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(creep_strain_energy_density._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(creep_strain_energy_density._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsCreepStrainEnergyDensity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(creep_strain_energy_density._spec().outputs, op)
        self.fields_container = Output(creep_strain_energy_density._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class creep_strain_energy_density(Operator):
    """Read/compute element nodal creep strain energy density by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.creep_strain_energy_density()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ENL_CRWK", config = config, server = server)
        self.inputs = _InputsCreepStrainEnergyDensity(self)
        self.outputs = _OutputsCreepStrainEnergyDensity(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal creep strain energy density by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENL_CRWK")

#internal name: ENL_ELENG
#scripting name: elastic_strain_energy_density
class _InputsElasticStrainEnergyDensity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_energy_density._spec().inputs, op)
        self.time_scoping = Input(elastic_strain_energy_density._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elastic_strain_energy_density._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elastic_strain_energy_density._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_energy_density._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_energy_density._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elastic_strain_energy_density._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elastic_strain_energy_density._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(elastic_strain_energy_density._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(elastic_strain_energy_density._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElasticStrainEnergyDensity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_energy_density._spec().outputs, op)
        self.fields_container = Output(elastic_strain_energy_density._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_energy_density(Operator):
    """Read/compute element nodal elastic strain energy density by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_energy_density()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ENL_ELENG", config = config, server = server)
        self.inputs = _InputsElasticStrainEnergyDensity(self)
        self.outputs = _OutputsElasticStrainEnergyDensity(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element nodal elastic strain energy density by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENL_ELENG")

#internal name: ECT_STAT
#scripting name: contact_status
class _InputsContactStatus(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(contact_status._spec().inputs, op)
        self.time_scoping = Input(contact_status._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(contact_status._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(contact_status._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(contact_status._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(contact_status._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(contact_status._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(contact_status._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(contact_status._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(contact_status._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsContactStatus(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(contact_status._spec().outputs, op)
        self.fields_container = Output(contact_status._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class contact_status(Operator):
    """Read/compute element contact status by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.contact_status()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ECT_STAT", config = config, server = server)
        self.inputs = _InputsContactStatus(self)
        self.outputs = _OutputsContactStatus(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element contact status by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_STAT")

#internal name: ECT_PENE
#scripting name: contact_penetration
class _InputsContactPenetration(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(contact_penetration._spec().inputs, op)
        self.time_scoping = Input(contact_penetration._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(contact_penetration._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(contact_penetration._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(contact_penetration._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(contact_penetration._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(contact_penetration._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(contact_penetration._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(contact_penetration._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(contact_penetration._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsContactPenetration(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(contact_penetration._spec().outputs, op)
        self.fields_container = Output(contact_penetration._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class contact_penetration(Operator):
    """Read/compute element contact penetration by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.contact_penetration()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ECT_PENE", config = config, server = server)
        self.inputs = _InputsContactPenetration(self)
        self.outputs = _OutputsContactPenetration(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element contact penetration by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_PENE")

#internal name: ECT_PRES
#scripting name: contact_pressure
class _InputsContactPressure(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(contact_pressure._spec().inputs, op)
        self.time_scoping = Input(contact_pressure._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(contact_pressure._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(contact_pressure._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(contact_pressure._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(contact_pressure._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(contact_pressure._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(contact_pressure._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(contact_pressure._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(contact_pressure._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsContactPressure(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(contact_pressure._spec().outputs, op)
        self.fields_container = Output(contact_pressure._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class contact_pressure(Operator):
    """Read/compute element contact pressure by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.contact_pressure()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ECT_PRES", config = config, server = server)
        self.inputs = _InputsContactPressure(self)
        self.outputs = _OutputsContactPressure(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element contact pressure by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_PRES")

#internal name: ECT_SFRIC
#scripting name: contact_friction_stress
class _InputsContactFrictionStress(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(contact_friction_stress._spec().inputs, op)
        self.time_scoping = Input(contact_friction_stress._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(contact_friction_stress._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(contact_friction_stress._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(contact_friction_stress._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(contact_friction_stress._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(contact_friction_stress._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(contact_friction_stress._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(contact_friction_stress._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(contact_friction_stress._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsContactFrictionStress(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(contact_friction_stress._spec().outputs, op)
        self.fields_container = Output(contact_friction_stress._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class contact_friction_stress(Operator):
    """Read/compute element contact friction stress by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.contact_friction_stress()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ECT_SFRIC", config = config, server = server)
        self.inputs = _InputsContactFrictionStress(self)
        self.outputs = _OutputsContactFrictionStress(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element contact friction stress by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_SFRIC")

#internal name: ECT_STOT
#scripting name: contact_total_stress
class _InputsContactTotalStress(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(contact_total_stress._spec().inputs, op)
        self.time_scoping = Input(contact_total_stress._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(contact_total_stress._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(contact_total_stress._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(contact_total_stress._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(contact_total_stress._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(contact_total_stress._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(contact_total_stress._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(contact_total_stress._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(contact_total_stress._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsContactTotalStress(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(contact_total_stress._spec().outputs, op)
        self.fields_container = Output(contact_total_stress._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class contact_total_stress(Operator):
    """Read/compute element contact total stress (pressure plus friction) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.contact_total_stress()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ECT_STOT", config = config, server = server)
        self.inputs = _InputsContactTotalStress(self)
        self.outputs = _OutputsContactTotalStress(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element contact total stress (pressure plus friction) by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_STOT")

#internal name: ECT_SLIDE
#scripting name: contact_sliding_distance
class _InputsContactSlidingDistance(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(contact_sliding_distance._spec().inputs, op)
        self.time_scoping = Input(contact_sliding_distance._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(contact_sliding_distance._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(contact_sliding_distance._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(contact_sliding_distance._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(contact_sliding_distance._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(contact_sliding_distance._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(contact_sliding_distance._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(contact_sliding_distance._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(contact_sliding_distance._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsContactSlidingDistance(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(contact_sliding_distance._spec().outputs, op)
        self.fields_container = Output(contact_sliding_distance._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class contact_sliding_distance(Operator):
    """Read/compute element contact sliding distance by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.contact_sliding_distance()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ECT_SLIDE", config = config, server = server)
        self.inputs = _InputsContactSlidingDistance(self)
        self.outputs = _OutputsContactSlidingDistance(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element contact sliding distance by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_SLIDE")

#internal name: ECT_GAP
#scripting name: contact_gap_distance
class _InputsContactGapDistance(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(contact_gap_distance._spec().inputs, op)
        self.time_scoping = Input(contact_gap_distance._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(contact_gap_distance._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(contact_gap_distance._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(contact_gap_distance._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(contact_gap_distance._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(contact_gap_distance._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(contact_gap_distance._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(contact_gap_distance._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(contact_gap_distance._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsContactGapDistance(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(contact_gap_distance._spec().outputs, op)
        self.fields_container = Output(contact_gap_distance._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class contact_gap_distance(Operator):
    """Read/compute element contact gap distance by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.contact_gap_distance()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ECT_GAP", config = config, server = server)
        self.inputs = _InputsContactGapDistance(self)
        self.outputs = _OutputsContactGapDistance(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element contact gap distance by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_GAP")

#internal name: ECT_FLUX
#scripting name: contact_surface_heat_flux
class _InputsContactSurfaceHeatFlux(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(contact_surface_heat_flux._spec().inputs, op)
        self.time_scoping = Input(contact_surface_heat_flux._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(contact_surface_heat_flux._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(contact_surface_heat_flux._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(contact_surface_heat_flux._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(contact_surface_heat_flux._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(contact_surface_heat_flux._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(contact_surface_heat_flux._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(contact_surface_heat_flux._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(contact_surface_heat_flux._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsContactSurfaceHeatFlux(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(contact_surface_heat_flux._spec().outputs, op)
        self.fields_container = Output(contact_surface_heat_flux._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class contact_surface_heat_flux(Operator):
    """Read/compute element total heat flux at contact surface by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.contact_surface_heat_flux()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ECT_FLUX", config = config, server = server)
        self.inputs = _InputsContactSurfaceHeatFlux(self)
        self.outputs = _OutputsContactSurfaceHeatFlux(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element total heat flux at contact surface by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_FLUX")

#internal name: ECT_CNOS
#scripting name: num_surface_status_changes
class _InputsNumSurfaceStatusChanges(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(num_surface_status_changes._spec().inputs, op)
        self.time_scoping = Input(num_surface_status_changes._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(num_surface_status_changes._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(num_surface_status_changes._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(num_surface_status_changes._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(num_surface_status_changes._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(num_surface_status_changes._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(num_surface_status_changes._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(num_surface_status_changes._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(num_surface_status_changes._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsNumSurfaceStatusChanges(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(num_surface_status_changes._spec().outputs, op)
        self.fields_container = Output(num_surface_status_changes._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class num_surface_status_changes(Operator):
    """Read/compute element total number of contact status changes during substep by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.num_surface_status_changes()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ECT_CNOS", config = config, server = server)
        self.inputs = _InputsNumSurfaceStatusChanges(self)
        self.outputs = _OutputsNumSurfaceStatusChanges(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element total number of contact status changes during substep by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_CNOS")

#internal name: ECT_FRES
#scripting name: contact_fluid_penetration_pressure
class _InputsContactFluidPenetrationPressure(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(contact_fluid_penetration_pressure._spec().inputs, op)
        self.time_scoping = Input(contact_fluid_penetration_pressure._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(contact_fluid_penetration_pressure._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(contact_fluid_penetration_pressure._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(contact_fluid_penetration_pressure._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(contact_fluid_penetration_pressure._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(contact_fluid_penetration_pressure._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(contact_fluid_penetration_pressure._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(contact_fluid_penetration_pressure._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(contact_fluid_penetration_pressure._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsContactFluidPenetrationPressure(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(contact_fluid_penetration_pressure._spec().outputs, op)
        self.fields_container = Output(contact_fluid_penetration_pressure._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class contact_fluid_penetration_pressure(Operator):
    """Read/compute element actual applied fluid penetration pressure by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.contact_fluid_penetration_pressure()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="ECT_FRES", config = config, server = server)
        self.inputs = _InputsContactFluidPenetrationPressure(self)
        self.outputs = _OutputsContactFluidPenetrationPressure(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element actual applied fluid penetration pressure by calling the readers defined by the datasources. Regarding the requested location and the input mesh scoping, the result location can be Nodal/ElementalNodal/Elemental.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""requested location Nodal, Elemental or ElementalNodal"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_FRES")

#internal name: ENG_VOL
#scripting name: elemental_volume
class _InputsElementalVolume(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_volume._spec().inputs, op)
        self.time_scoping = Input(elemental_volume._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(elemental_volume._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(elemental_volume._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elemental_volume._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elemental_volume._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(elemental_volume._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(elemental_volume._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(elemental_volume._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElementalVolume(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_volume._spec().outputs, op)
        self.fields_container = Output(elemental_volume._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elemental_volume(Operator):
    """Read/compute element volume by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elemental_volume()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="ENG_VOL", config = config, server = server)
        self.inputs = _InputsElementalVolume(self)
        self.outputs = _OutputsElementalVolume(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element volume by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENG_VOL")

#internal name: ENG_AHO
#scripting name: artificial_hourglass_energy
class _InputsArtificialHourglassEnergy(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(artificial_hourglass_energy._spec().inputs, op)
        self.time_scoping = Input(artificial_hourglass_energy._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(artificial_hourglass_energy._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(artificial_hourglass_energy._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(artificial_hourglass_energy._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(artificial_hourglass_energy._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(artificial_hourglass_energy._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(artificial_hourglass_energy._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(artificial_hourglass_energy._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsArtificialHourglassEnergy(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(artificial_hourglass_energy._spec().outputs, op)
        self.fields_container = Output(artificial_hourglass_energy._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class artificial_hourglass_energy(Operator):
    """Read/compute artificial hourglass energy by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.artificial_hourglass_energy()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="ENG_AHO", config = config, server = server)
        self.inputs = _InputsArtificialHourglassEnergy(self)
        self.outputs = _OutputsArtificialHourglassEnergy(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute artificial hourglass energy by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENG_AHO")

#internal name: ENG_KE
#scripting name: kinetic_energy
class _InputsKineticEnergy(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(kinetic_energy._spec().inputs, op)
        self.time_scoping = Input(kinetic_energy._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(kinetic_energy._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(kinetic_energy._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(kinetic_energy._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(kinetic_energy._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(kinetic_energy._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(kinetic_energy._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(kinetic_energy._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsKineticEnergy(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(kinetic_energy._spec().outputs, op)
        self.fields_container = Output(kinetic_energy._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class kinetic_energy(Operator):
    """Read/compute kinetic energy by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.kinetic_energy()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="ENG_KE", config = config, server = server)
        self.inputs = _InputsKineticEnergy(self)
        self.outputs = _OutputsKineticEnergy(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute kinetic energy by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENG_KE")

#internal name: ENG_TH
#scripting name: thermal_dissipation_energy
class _InputsThermalDissipationEnergy(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(thermal_dissipation_energy._spec().inputs, op)
        self.time_scoping = Input(thermal_dissipation_energy._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(thermal_dissipation_energy._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(thermal_dissipation_energy._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(thermal_dissipation_energy._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(thermal_dissipation_energy._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(thermal_dissipation_energy._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(thermal_dissipation_energy._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(thermal_dissipation_energy._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsThermalDissipationEnergy(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(thermal_dissipation_energy._spec().outputs, op)
        self.fields_container = Output(thermal_dissipation_energy._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class thermal_dissipation_energy(Operator):
    """Read/compute thermal dissipation energy by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.thermal_dissipation_energy()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="ENG_TH", config = config, server = server)
        self.inputs = _InputsThermalDissipationEnergy(self)
        self.outputs = _OutputsThermalDissipationEnergy(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute thermal dissipation energy by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENG_TH")

#internal name: F
#scripting name: nodal_force
class _InputsNodalForce(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_force._spec().inputs, op)
        self.time_scoping = Input(nodal_force._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_force._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_force._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_force._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_force._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(nodal_force._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(nodal_force._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(nodal_force._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsNodalForce(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_force._spec().outputs, op)
        self.fields_container = Output(nodal_force._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_force(Operator):
    """Read/compute nodal forces by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_force()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="F", config = config, server = server)
        self.inputs = _InputsNodalForce(self)
        self.outputs = _OutputsNodalForce(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute nodal forces by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "F")

#internal name: TEMP
#scripting name: temperature
class _InputsTemperature(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(temperature._spec().inputs, op)
        self.time_scoping = Input(temperature._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(temperature._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(temperature._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(temperature._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(temperature._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(temperature._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(temperature._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(temperature._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsTemperature(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(temperature._spec().outputs, op)
        self.fields_container = Output(temperature._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class temperature(Operator):
    """Read/compute temperature field by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.temperature()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="TEMP", config = config, server = server)
        self.inputs = _InputsTemperature(self)
        self.outputs = _OutputsTemperature(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute temperature field by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "TEMP")

#internal name: UTOT
#scripting name: raw_displacement
class _InputsRawDisplacement(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(raw_displacement._spec().inputs, op)
        self.time_scoping = Input(raw_displacement._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(raw_displacement._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(raw_displacement._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(raw_displacement._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(raw_displacement._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(raw_displacement._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(raw_displacement._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(raw_displacement._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsRawDisplacement(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(raw_displacement._spec().outputs, op)
        self.fields_container = Output(raw_displacement._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class raw_displacement(Operator):
    """Read/compute U vector from the finite element problem KU=F by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.raw_displacement()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="UTOT", config = config, server = server)
        self.inputs = _InputsRawDisplacement(self)
        self.outputs = _OutputsRawDisplacement(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute U vector from the finite element problem KU=F by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "UTOT")

#internal name: RFTOT
#scripting name: raw_reaction_force
class _InputsRawReactionForce(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(raw_reaction_force._spec().inputs, op)
        self.time_scoping = Input(raw_reaction_force._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(raw_reaction_force._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(raw_reaction_force._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(raw_reaction_force._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(raw_reaction_force._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(raw_reaction_force._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(raw_reaction_force._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(raw_reaction_force._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsRawReactionForce(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(raw_reaction_force._spec().outputs, op)
        self.fields_container = Output(raw_reaction_force._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class raw_reaction_force(Operator):
    """Read/compute F vector from the finite element problem KU=F by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.raw_reaction_force()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="RFTOT", config = config, server = server)
        self.inputs = _InputsRawReactionForce(self)
        self.outputs = _OutputsRawReactionForce(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute F vector from the finite element problem KU=F by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "RFTOT")

#internal name: VOLT
#scripting name: electric_potential
class _InputsElectricPotential(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(electric_potential._spec().inputs, op)
        self.time_scoping = Input(electric_potential._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(electric_potential._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(electric_potential._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(electric_potential._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(electric_potential._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(electric_potential._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(electric_potential._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(electric_potential._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsElectricPotential(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(electric_potential._spec().outputs, op)
        self.fields_container = Output(electric_potential._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class electric_potential(Operator):
    """Read/compute electric Potential by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.electric_potential()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="VOLT", config = config, server = server)
        self.inputs = _InputsElectricPotential(self)
        self.outputs = _OutputsElectricPotential(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute electric Potential by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "VOLT")

#internal name: thickness
#scripting name: thickness
class _InputsThickness(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(thickness._spec().inputs, op)
        self.time_scoping = Input(thickness._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(thickness._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(thickness._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(thickness._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(thickness._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(thickness._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(thickness._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(thickness._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsThickness(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(thickness._spec().outputs, op)
        self.fields_container = Output(thickness._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class thickness(Operator):
    """Read/compute thickness by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.thickness()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="thickness", config = config, server = server)
        self.inputs = _InputsThickness(self)
        self.outputs = _OutputsThickness(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute thickness by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "thickness")

#internal name: custom
#scripting name: custom
class _InputsCustom(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(custom._spec().inputs, op)
        self.time_scoping = Input(custom._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(custom._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(custom._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(custom._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(custom._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(custom._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(custom._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.read_cyclic = Input(custom._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsCustom(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(custom._spec().outputs, op)
        self.fields_container = Output(custom._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class custom(Operator):
    """Read/compute user defined result by calling the readers defined by the datasources.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.custom()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="custom", config = config, server = server)
        self.inputs = _InputsCustom(self)
        self.outputs = _OutputsCustom(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute user defined result by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "custom")

#internal name: S_eqv
#scripting name: stress_von_mises
class _InputsStressVonMises(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_von_mises._spec().inputs, op)
        self.time_scoping = Input(stress_von_mises._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(stress_von_mises._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(stress_von_mises._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_von_mises._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_von_mises._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(stress_von_mises._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.mesh = Input(stress_von_mises._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(stress_von_mises._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(stress_von_mises._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsStressVonMises(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_von_mises._spec().outputs, op)
        self.fields_container = Output(stress_von_mises._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_von_mises(Operator):
    """Reads/computes element nodal component stresses, average it on nodes (by default) and computes its invariants.

      available inputs:
         time_scoping (Scoping, int, listfloat, Field, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_von_mises()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="S_eqv", config = config, server = server)
        self.inputs = _InputsStressVonMises(self)
        self.outputs = _OutputsStressVonMises(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Reads/computes element nodal component stresses, average it on nodes (by default) and computes its invariants.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document=""""""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "S_eqv")

"""
Result Operators
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils.dll plugin, from "result" category
"""

#internal name: cyclic_expansion
#scripting name: cyclic_expansion
class _InputsCyclicExpansion(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expansion._spec().inputs, op)
        self.time_scoping = Input(cyclic_expansion._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_expansion._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_expansion._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.cyclic_support = Input(cyclic_expansion._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)

class _OutputsCyclicExpansion(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expansion._spec().outputs, op)
        self.fields_container = Output(cyclic_expansion._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class cyclic_expansion(Operator):
    """Expand cyclic results from a fieldsContainer for given sets, sectors and scoping (optionals).

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer)
         cyclic_support (CyclicSupport)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_expansion()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, cyclic_support=None, config=None, server=None):
        super().__init__(name="cyclic_expansion", config = config, server = server)
        self.inputs = _InputsCyclicExpansion(self)
        self.outputs = _OutputsCyclicExpansion(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)

    @staticmethod
    def _spec():
        spec = Specification(description="""Expand cyclic results from a fieldsContainer for given sets, sectors and scoping (optionals).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field container with the base and duplicate sectors"""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cyclic_expansion")

#internal name: ERP
#scripting name: equivalent_radiated_power
class _InputsEquivalentRadiatedPower(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(equivalent_radiated_power._spec().inputs, op)
        self.fields_container = Input(equivalent_radiated_power._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.meshed_region = Input(equivalent_radiated_power._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.meshed_region)
        self.time_scoping = Input(equivalent_radiated_power._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.time_scoping)

class _OutputsEquivalentRadiatedPower(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(equivalent_radiated_power._spec().outputs, op)
        self.fields_container = Output(equivalent_radiated_power._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class equivalent_radiated_power(Operator):
    """Compute the Equivalent Radiated Power (ERP)

      available inputs:
         fields_container (FieldsContainer)
         meshed_region (MeshedRegion, MeshesContainer) (optional)
         time_scoping (int, list, Scoping) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.equivalent_radiated_power()

    """
    def __init__(self, fields_container=None, meshed_region=None, time_scoping=None, config=None, server=None):
        super().__init__(name="ERP", config = config, server = server)
        self.inputs = _InputsEquivalentRadiatedPower(self)
        self.outputs = _OutputsEquivalentRadiatedPower(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if meshed_region !=None:
            self.inputs.meshed_region.connect(meshed_region)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the Equivalent Radiated Power (ERP)""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""the mesh region in this pin have to be boundary or skin mesh"""), 
                                 2 : PinSpecification(name = "time_scoping", type_names=["int32","vector<int32>","scoping"], optional=True, document="""load step number (if it's specified, the ERP is computed only on the substeps of this step) or time scoping""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ERP")

#internal name: torque
#scripting name: torque
class _InputsTorque(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(torque._spec().inputs, op)
        self.fields_container = Input(torque._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.vector_of_double = Input(torque._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.vector_of_double)

class _OutputsTorque(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(torque._spec().outputs, op)
        self.fields_container = Output(torque._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class torque(Operator):
    """Compute torque of a force based on a 3D point.

      available inputs:
         fields_container (FieldsContainer)
         vector_of_double (list)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.torque()

    """
    def __init__(self, fields_container=None, vector_of_double=None, config=None, server=None):
        super().__init__(name="torque", config = config, server = server)
        self.inputs = _InputsTorque(self)
        self.outputs = _OutputsTorque(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if vector_of_double !=None:
            self.inputs.vector_of_double.connect(vector_of_double)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute torque of a force based on a 3D point.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""fields_container"""), 
                                 1 : PinSpecification(name = "vector_of_double", type_names=["vector<double>"], optional=False, document="""vector_of_double""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "torque")

#internal name: cyclic_analytic_usum_max
#scripting name: cyclic_analytic_usum_max
class _InputsCyclicAnalyticUsumMax(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_analytic_usum_max._spec().inputs, op)
        self.time_scoping = Input(cyclic_analytic_usum_max._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_analytic_usum_max._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_analytic_usum_max._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.cyclic_support = Input(cyclic_analytic_usum_max._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)

class _OutputsCyclicAnalyticUsumMax(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_analytic_usum_max._spec().outputs, op)
        self.fields_container = Output(cyclic_analytic_usum_max._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class cyclic_analytic_usum_max(Operator):
    """Compute the maximum of the total deformation that can be expected on 360 degrees

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer)
         cyclic_support (CyclicSupport)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_analytic_usum_max()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, cyclic_support=None, config=None, server=None):
        super().__init__(name="cyclic_analytic_usum_max", config = config, server = server)
        self.inputs = _InputsCyclicAnalyticUsumMax(self)
        self.outputs = _OutputsCyclicAnalyticUsumMax(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the maximum of the total deformation that can be expected on 360 degrees""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field container with the base and duplicate sectors"""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cyclic_analytic_usum_max")

#internal name: cyclic_analytic_stress_eqv_max
#scripting name: cyclic_analytic_seqv_max
class _InputsCyclicAnalyticSeqvMax(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_analytic_seqv_max._spec().inputs, op)
        self.time_scoping = Input(cyclic_analytic_seqv_max._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_analytic_seqv_max._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_analytic_seqv_max._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.cyclic_support = Input(cyclic_analytic_seqv_max._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)

class _OutputsCyclicAnalyticSeqvMax(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_analytic_seqv_max._spec().outputs, op)
        self.fields_container = Output(cyclic_analytic_seqv_max._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class cyclic_analytic_seqv_max(Operator):
    """Compute the maximum of the Von Mises equivalent stress that can be expected on 360 degrees

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer)
         cyclic_support (CyclicSupport)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_analytic_seqv_max()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, cyclic_support=None, config=None, server=None):
        super().__init__(name="cyclic_analytic_stress_eqv_max", config = config, server = server)
        self.inputs = _InputsCyclicAnalyticSeqvMax(self)
        self.outputs = _OutputsCyclicAnalyticSeqvMax(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the maximum of the Von Mises equivalent stress that can be expected on 360 degrees""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field container with the base and duplicate sectors"""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cyclic_analytic_stress_eqv_max")

#internal name: recombine_harmonic_indeces_cyclic
#scripting name: recombine_harmonic_indeces_cyclic
class _InputsRecombineHarmonicIndecesCyclic(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(recombine_harmonic_indeces_cyclic._spec().inputs, op)
        self.fields_container = Input(recombine_harmonic_indeces_cyclic._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsRecombineHarmonicIndecesCyclic(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(recombine_harmonic_indeces_cyclic._spec().outputs, op)
        self.fields_container = Output(recombine_harmonic_indeces_cyclic._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class recombine_harmonic_indeces_cyclic(Operator):
    """Add the fields corresponding to different load steps with the same frequencies to compute the response.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.recombine_harmonic_indeces_cyclic()

    """
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="recombine_harmonic_indeces_cyclic", config = config, server = server)
        self.inputs = _InputsRecombineHarmonicIndecesCyclic(self)
        self.outputs = _OutputsRecombineHarmonicIndecesCyclic(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Add the fields corresponding to different load steps with the same frequencies to compute the response.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "recombine_harmonic_indeces_cyclic")

#internal name: PoyntingVector
#scripting name: poynting_vector
class _InputsPoyntingVector(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(poynting_vector._spec().inputs, op)
        self.fields_containerA = Input(poynting_vector._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_containerA)
        self.fields_containerB = Input(poynting_vector._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fields_containerB)
        self.fields_containerC = Input(poynting_vector._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_containerC)
        self.fields_containerD = Input(poynting_vector._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.fields_containerD)
        self.meshed_region = Input(poynting_vector._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.meshed_region)
        self.int32 = Input(poynting_vector._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.int32)

class _OutputsPoyntingVector(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(poynting_vector._spec().outputs, op)
        self.fields_container = Output(poynting_vector._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class poynting_vector(Operator):
    """Compute the Poynting Vector

      available inputs:
         fields_containerA (FieldsContainer)
         fields_containerB (FieldsContainer)
         fields_containerC (FieldsContainer)
         fields_containerD (FieldsContainer)
         meshed_region (MeshedRegion) (optional)
         int32 (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.poynting_vector()

    """
    def __init__(self, fields_containerA=None, fields_containerB=None, fields_containerC=None, fields_containerD=None, meshed_region=None, int32=None, config=None, server=None):
        super().__init__(name="PoyntingVector", config = config, server = server)
        self.inputs = _InputsPoyntingVector(self)
        self.outputs = _OutputsPoyntingVector(self)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)
        if fields_containerC !=None:
            self.inputs.fields_containerC.connect(fields_containerC)
        if fields_containerD !=None:
            self.inputs.fields_containerD.connect(fields_containerD)
        if meshed_region !=None:
            self.inputs.meshed_region.connect(meshed_region)
        if int32 !=None:
            self.inputs.int32.connect(int32)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the Poynting Vector""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "fields_containerC", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "fields_containerD", type_names=["fields_container"], optional=False, document=""""""), 
                                 4 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region"], optional=True, document="""the mesh region in this pin have to be boundary or skin mesh"""), 
                                 5 : PinSpecification(name = "int32", type_names=["int32"], optional=True, document="""load step number, if it's specified, the Poynting Vector is computed only on the substeps of this step""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "PoyntingVector")

#internal name: PoyntingVectorSurface
#scripting name: poynting_vector_surface
class _InputsPoyntingVectorSurface(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(poynting_vector_surface._spec().inputs, op)
        self.fields_containerA = Input(poynting_vector_surface._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_containerA)
        self.fields_containerB = Input(poynting_vector_surface._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fields_containerB)
        self.fields_containerC = Input(poynting_vector_surface._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_containerC)
        self.fields_containerD = Input(poynting_vector_surface._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.fields_containerD)
        self.meshed_region = Input(poynting_vector_surface._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.meshed_region)
        self.int32 = Input(poynting_vector_surface._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.int32)

class _OutputsPoyntingVectorSurface(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(poynting_vector_surface._spec().outputs, op)
        self.fields_container = Output(poynting_vector_surface._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class poynting_vector_surface(Operator):
    """Compute the Poynting Vector surface integral

      available inputs:
         fields_containerA (FieldsContainer)
         fields_containerB (FieldsContainer)
         fields_containerC (FieldsContainer)
         fields_containerD (FieldsContainer)
         meshed_region (MeshedRegion) (optional)
         int32 (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.poynting_vector_surface()

    """
    def __init__(self, fields_containerA=None, fields_containerB=None, fields_containerC=None, fields_containerD=None, meshed_region=None, int32=None, config=None, server=None):
        super().__init__(name="PoyntingVectorSurface", config = config, server = server)
        self.inputs = _InputsPoyntingVectorSurface(self)
        self.outputs = _OutputsPoyntingVectorSurface(self)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)
        if fields_containerC !=None:
            self.inputs.fields_containerC.connect(fields_containerC)
        if fields_containerD !=None:
            self.inputs.fields_containerD.connect(fields_containerD)
        if meshed_region !=None:
            self.inputs.meshed_region.connect(meshed_region)
        if int32 !=None:
            self.inputs.int32.connect(int32)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the Poynting Vector surface integral""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "fields_containerC", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "fields_containerD", type_names=["fields_container"], optional=False, document=""""""), 
                                 4 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region"], optional=True, document="""the mesh region in this pin have to be boundary or skin mesh"""), 
                                 5 : PinSpecification(name = "int32", type_names=["int32"], optional=True, document="""load step number, if it's specified, the Poynting Vector is computed only on the substeps of this step""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "PoyntingVectorSurface")

"""
Result Operators
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore.dll plugin, from "result" category
"""

#internal name: mapdl::rst::NPEL
#scripting name: nodal_averaged_elastic_strains
class _InputsNodalAveragedElasticStrains(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_elastic_strains._spec().inputs, op)
        self.time_scoping = Input(nodal_averaged_elastic_strains._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_averaged_elastic_strains._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_averaged_elastic_strains._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_averaged_elastic_strains._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_averaged_elastic_strains._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nodal_averaged_elastic_strains._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalAveragedElasticStrains(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_elastic_strains._spec().outputs, op)
        self.fields_container = Output(nodal_averaged_elastic_strains._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_averaged_elastic_strains(Operator):
    """Read nodal averaged elastic strains as averaged nodal result from rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_averaged_elastic_strains()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NPEL", config = config, server = server)
        self.inputs = _InputsNodalAveragedElasticStrains(self)
        self.outputs = _OutputsNodalAveragedElasticStrains(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged elastic strains as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NPEL")

#internal name: RigidBodyAddition
#scripting name: add_rigid_body_motion
class _InputsAddRigidBodyMotion(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(add_rigid_body_motion._spec().inputs, op)
        self.displacement_field = Input(add_rigid_body_motion._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.displacement_field)
        self.translation_field = Input(add_rigid_body_motion._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.translation_field)
        self.rotation_field = Input(add_rigid_body_motion._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.rotation_field)
        self.center_field = Input(add_rigid_body_motion._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.center_field)
        self.mesh = Input(add_rigid_body_motion._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsAddRigidBodyMotion(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(add_rigid_body_motion._spec().outputs, op)
        self.field = Output(add_rigid_body_motion._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class add_rigid_body_motion(Operator):
    """Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem

      available inputs:
         displacement_field (Field)
         translation_field (Field)
         rotation_field (Field)
         center_field (Field)
         mesh (MeshedRegion) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.result.add_rigid_body_motion()

    """
    def __init__(self, displacement_field=None, translation_field=None, rotation_field=None, center_field=None, mesh=None, config=None, server=None):
        super().__init__(name="RigidBodyAddition", config = config, server = server)
        self.inputs = _InputsAddRigidBodyMotion(self)
        self.outputs = _OutputsAddRigidBodyMotion(self)
        if displacement_field !=None:
            self.inputs.displacement_field.connect(displacement_field)
        if translation_field !=None:
            self.inputs.translation_field.connect(translation_field)
        if rotation_field !=None:
            self.inputs.rotation_field.connect(rotation_field)
        if center_field !=None:
            self.inputs.center_field.connect(center_field)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "displacement_field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "translation_field", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "rotation_field", type_names=["field"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "center_field", type_names=["field"], optional=False, document=""""""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""default is the mesh in the support""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "RigidBodyAddition")

#internal name: mapdl::rst::NPEL_EQV
#scripting name: nodal_averaged_equivalent_elastic_strain
class _InputsNodalAveragedEquivalentElasticStrain(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_equivalent_elastic_strain._spec().inputs, op)
        self.time_scoping = Input(nodal_averaged_equivalent_elastic_strain._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_averaged_equivalent_elastic_strain._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_averaged_equivalent_elastic_strain._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_averaged_equivalent_elastic_strain._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_averaged_equivalent_elastic_strain._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nodal_averaged_equivalent_elastic_strain._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalAveragedEquivalentElasticStrain(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_equivalent_elastic_strain._spec().outputs, op)
        self.fields_container = Output(nodal_averaged_equivalent_elastic_strain._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_averaged_equivalent_elastic_strain(Operator):
    """Read nodal averaged equivalent elastic strain as averaged nodal result from rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_averaged_equivalent_elastic_strain()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NPEL_EQV", config = config, server = server)
        self.inputs = _InputsNodalAveragedEquivalentElasticStrain(self)
        self.outputs = _OutputsNodalAveragedEquivalentElasticStrain(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged equivalent elastic strain as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NPEL_EQV")

#internal name: mapdl::run
#scripting name: run
class _InputsRun(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(run._spec().inputs, op)
        self.mapdl_exe_path = Input(run._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mapdl_exe_path)
        self.working_dir = Input(run._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.working_dir)
        self.number_of_processes = Input(run._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.number_of_processes)
        self.data_sources = Input(run._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsRun(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(run._spec().outputs, op)
        self.data_sources = Output(run._spec().output_pin(0), 0, op) 
        self._outputs.append(self.data_sources)

class run(Operator):
    """Solve in mapdl a dat/inp file and returns a datasources with the rst file.

      available inputs:
         mapdl_exe_path (str) (optional)
         working_dir (str) (optional)
         number_of_processes (int) (optional)
         data_sources (DataSources)

      available outputs:
         data_sources (DataSources)

      Examples
      --------
      >>> op = operators.result.run()

    """
    def __init__(self, mapdl_exe_path=None, working_dir=None, number_of_processes=None, data_sources=None, config=None, server=None):
        super().__init__(name="mapdl::run", config = config, server = server)
        self.inputs = _InputsRun(self)
        self.outputs = _OutputsRun(self)
        if mapdl_exe_path !=None:
            self.inputs.mapdl_exe_path.connect(mapdl_exe_path)
        if working_dir !=None:
            self.inputs.working_dir.connect(working_dir)
        if number_of_processes !=None:
            self.inputs.number_of_processes.connect(number_of_processes)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Solve in mapdl a dat/inp file and returns a datasources with the rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mapdl_exe_path", type_names=["string"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "working_dir", type_names=["string"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "number_of_processes", type_names=["int32"], optional=True, document="""Set the number of MPI processes used for resolution (default is 2)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the input file.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::run")

#internal name: mapdl::rst::V_cyclic
#scripting name: cyclic_expanded_velocity
class _InputsCyclicExpandedVelocity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_velocity._spec().inputs, op)
        self.time_scoping = Input(cyclic_expanded_velocity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_expanded_velocity._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_expanded_velocity._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(cyclic_expanded_velocity._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(cyclic_expanded_velocity._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(cyclic_expanded_velocity._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.sector_mesh = Input(cyclic_expanded_velocity._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.sector_mesh)
        self.requested_location = Input(cyclic_expanded_velocity._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(cyclic_expanded_velocity._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)
        self.expanded_meshed_region = Input(cyclic_expanded_velocity._spec().input_pin(15), 15, op, -1) 
        self._inputs.append(self.expanded_meshed_region)
        self.cyclic_support = Input(cyclic_expanded_velocity._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)
        self.sectors_to_expand = Input(cyclic_expanded_velocity._spec().input_pin(18), 18, op, -1) 
        self._inputs.append(self.sectors_to_expand)
        self.phi = Input(cyclic_expanded_velocity._spec().input_pin(19), 19, op, -1) 
        self._inputs.append(self.phi)

class _OutputsCyclicExpandedVelocity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_velocity._spec().outputs, op)
        self.fields_container = Output(cyclic_expanded_velocity._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)
        self.expanded_meshes = Output(cyclic_expanded_velocity._spec().output_pin(1), 1, op) 
        self._outputs.append(self.expanded_meshes)

class cyclic_expanded_velocity(Operator):
    """Read velocity from an rst file and expand it with cyclic symmetry.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         sector_mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)
         expanded_meshed_region (MeshedRegion, MeshesContainer) (optional)
         cyclic_support (CyclicSupport) (optional)
         sectors_to_expand (list, Scoping, ScopingsContainer) (optional)
         phi (float) (optional)

      available outputs:
         fields_container (FieldsContainer)
         expanded_meshes (MeshesContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_expanded_velocity()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, bool_rotate_to_global=None, sector_mesh=None, requested_location=None, read_cyclic=None, expanded_meshed_region=None, cyclic_support=None, sectors_to_expand=None, phi=None, config=None, server=None):
        super().__init__(name="mapdl::rst::V_cyclic", config = config, server = server)
        self.inputs = _InputsCyclicExpandedVelocity(self)
        self.outputs = _OutputsCyclicExpandedVelocity(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if bool_rotate_to_global !=None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if sector_mesh !=None:
            self.inputs.sector_mesh.connect(sector_mesh)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if read_cyclic !=None:
            self.inputs.read_cyclic.connect(read_cyclic)
        if expanded_meshed_region !=None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)
        if sectors_to_expand !=None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)
        if phi !=None:
            self.inputs.phi.connect(phi)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read velocity from an rst file and expand it with cyclic symmetry.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is roated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "sector_mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh of the base sector (can be a skin)."""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""location needed in output"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)"""), 
                                 15 : PinSpecification(name = "expanded_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh expanded."""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=True, document=""""""), 
                                 18 : PinSpecification(name = "sectors_to_expand", type_names=["vector<int32>","scoping","scopings_container"], optional=True, document="""sectors to expand (start at 0), for multistage: use scopings container with 'stage' label."""), 
                                 19 : PinSpecification(name = "phi", type_names=["double"], optional=True, document="""angle phi (default value 0.0)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in"""), 
                                 1 : PinSpecification(name = "expanded_meshes", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::V_cyclic")

#internal name: mapdl::rst::EPEL_cyclic
#scripting name: cyclic_expanded_el_strain
class _InputsCyclicExpandedElStrain(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_el_strain._spec().inputs, op)
        self.time_scoping = Input(cyclic_expanded_el_strain._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_expanded_el_strain._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_expanded_el_strain._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(cyclic_expanded_el_strain._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(cyclic_expanded_el_strain._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(cyclic_expanded_el_strain._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.sector_mesh = Input(cyclic_expanded_el_strain._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.sector_mesh)
        self.requested_location = Input(cyclic_expanded_el_strain._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(cyclic_expanded_el_strain._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)
        self.expanded_meshed_region = Input(cyclic_expanded_el_strain._spec().input_pin(15), 15, op, -1) 
        self._inputs.append(self.expanded_meshed_region)
        self.cyclic_support = Input(cyclic_expanded_el_strain._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)
        self.sectors_to_expand = Input(cyclic_expanded_el_strain._spec().input_pin(18), 18, op, -1) 
        self._inputs.append(self.sectors_to_expand)
        self.phi = Input(cyclic_expanded_el_strain._spec().input_pin(19), 19, op, -1) 
        self._inputs.append(self.phi)

class _OutputsCyclicExpandedElStrain(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_el_strain._spec().outputs, op)
        self.fields_container = Output(cyclic_expanded_el_strain._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)
        self.expanded_meshes = Output(cyclic_expanded_el_strain._spec().output_pin(1), 1, op) 
        self._outputs.append(self.expanded_meshes)

class cyclic_expanded_el_strain(Operator):
    """Read mapdl::rst::EPEL from an rst file and expand it with cyclic symmetry.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         sector_mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)
         expanded_meshed_region (MeshedRegion, MeshesContainer) (optional)
         cyclic_support (CyclicSupport) (optional)
         sectors_to_expand (list, Scoping, ScopingsContainer) (optional)
         phi (float) (optional)

      available outputs:
         fields_container (FieldsContainer)
         expanded_meshes (MeshesContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_expanded_el_strain()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, bool_rotate_to_global=None, sector_mesh=None, requested_location=None, read_cyclic=None, expanded_meshed_region=None, cyclic_support=None, sectors_to_expand=None, phi=None, config=None, server=None):
        super().__init__(name="mapdl::rst::EPEL_cyclic", config = config, server = server)
        self.inputs = _InputsCyclicExpandedElStrain(self)
        self.outputs = _OutputsCyclicExpandedElStrain(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if bool_rotate_to_global !=None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if sector_mesh !=None:
            self.inputs.sector_mesh.connect(sector_mesh)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if read_cyclic !=None:
            self.inputs.read_cyclic.connect(read_cyclic)
        if expanded_meshed_region !=None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)
        if sectors_to_expand !=None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)
        if phi !=None:
            self.inputs.phi.connect(phi)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read mapdl::rst::EPEL from an rst file and expand it with cyclic symmetry.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is roated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "sector_mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh of the base sector (can be a skin)."""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""location needed in output"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)"""), 
                                 15 : PinSpecification(name = "expanded_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh expanded."""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=True, document=""""""), 
                                 18 : PinSpecification(name = "sectors_to_expand", type_names=["vector<int32>","scoping","scopings_container"], optional=True, document="""sectors to expand (start at 0), for multistage: use scopings container with 'stage' label."""), 
                                 19 : PinSpecification(name = "phi", type_names=["double"], optional=True, document="""phi angle (default value 0.0)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in"""), 
                                 1 : PinSpecification(name = "expanded_meshes", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::EPEL_cyclic")

#internal name: mapdl::rst::NTH_SWL
#scripting name: nodal_averaged_thermal_swelling_strains
class _InputsNodalAveragedThermalSwellingStrains(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_thermal_swelling_strains._spec().inputs, op)
        self.time_scoping = Input(nodal_averaged_thermal_swelling_strains._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_averaged_thermal_swelling_strains._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_averaged_thermal_swelling_strains._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_averaged_thermal_swelling_strains._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_averaged_thermal_swelling_strains._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nodal_averaged_thermal_swelling_strains._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalAveragedThermalSwellingStrains(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_thermal_swelling_strains._spec().outputs, op)
        self.fields_container = Output(nodal_averaged_thermal_swelling_strains._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_averaged_thermal_swelling_strains(Operator):
    """Read nodal averaged thermal swelling strains as averaged nodal result from rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_averaged_thermal_swelling_strains()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NTH_SWL", config = config, server = server)
        self.inputs = _InputsNodalAveragedThermalSwellingStrains(self)
        self.outputs = _OutputsNodalAveragedThermalSwellingStrains(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged thermal swelling strains as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NTH_SWL")

#internal name: mapdl::rst::NS
#scripting name: nodal_averaged_stresses
class _InputsNodalAveragedStresses(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_stresses._spec().inputs, op)
        self.time_scoping = Input(nodal_averaged_stresses._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_averaged_stresses._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_averaged_stresses._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_averaged_stresses._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_averaged_stresses._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nodal_averaged_stresses._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalAveragedStresses(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_stresses._spec().outputs, op)
        self.fields_container = Output(nodal_averaged_stresses._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_averaged_stresses(Operator):
    """Read nodal averaged stresses as averaged nodal result from rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_averaged_stresses()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NS", config = config, server = server)
        self.inputs = _InputsNodalAveragedStresses(self)
        self.outputs = _OutputsNodalAveragedStresses(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged stresses as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NS")

#internal name: mapdl::rst::NTH
#scripting name: nodal_averaged_thermal_strains
class _InputsNodalAveragedThermalStrains(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_thermal_strains._spec().inputs, op)
        self.time_scoping = Input(nodal_averaged_thermal_strains._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_averaged_thermal_strains._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_averaged_thermal_strains._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_averaged_thermal_strains._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_averaged_thermal_strains._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nodal_averaged_thermal_strains._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalAveragedThermalStrains(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_thermal_strains._spec().outputs, op)
        self.fields_container = Output(nodal_averaged_thermal_strains._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_averaged_thermal_strains(Operator):
    """Read nodal averaged thermal strains as averaged nodal result from rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_averaged_thermal_strains()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NTH", config = config, server = server)
        self.inputs = _InputsNodalAveragedThermalStrains(self)
        self.outputs = _OutputsNodalAveragedThermalStrains(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged thermal strains as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NTH")

#internal name: mapdl::rst::NPPL
#scripting name: nodal_averaged_plastic_strains
class _InputsNodalAveragedPlasticStrains(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_plastic_strains._spec().inputs, op)
        self.time_scoping = Input(nodal_averaged_plastic_strains._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_averaged_plastic_strains._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_averaged_plastic_strains._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_averaged_plastic_strains._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_averaged_plastic_strains._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nodal_averaged_plastic_strains._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalAveragedPlasticStrains(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_plastic_strains._spec().outputs, op)
        self.fields_container = Output(nodal_averaged_plastic_strains._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_averaged_plastic_strains(Operator):
    """Read nodal averaged plastic strains as averaged nodal result from rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_averaged_plastic_strains()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NPPL", config = config, server = server)
        self.inputs = _InputsNodalAveragedPlasticStrains(self)
        self.outputs = _OutputsNodalAveragedPlasticStrains(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged plastic strains as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NPPL")

#internal name: mapdl::rst::NCR
#scripting name: nodal_averaged_creep_strains
class _InputsNodalAveragedCreepStrains(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_creep_strains._spec().inputs, op)
        self.time_scoping = Input(nodal_averaged_creep_strains._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_averaged_creep_strains._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_averaged_creep_strains._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_averaged_creep_strains._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_averaged_creep_strains._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nodal_averaged_creep_strains._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalAveragedCreepStrains(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_creep_strains._spec().outputs, op)
        self.fields_container = Output(nodal_averaged_creep_strains._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_averaged_creep_strains(Operator):
    """Read nodal averaged creep strains as averaged nodal result from rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_averaged_creep_strains()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NCR", config = config, server = server)
        self.inputs = _InputsNodalAveragedCreepStrains(self)
        self.outputs = _OutputsNodalAveragedCreepStrains(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged creep strains as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NCR")

#internal name: mapdl::rst::NTH_EQV
#scripting name: nodal_averaged_equivalent_thermal_strains
class _InputsNodalAveragedEquivalentThermalStrains(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_equivalent_thermal_strains._spec().inputs, op)
        self.time_scoping = Input(nodal_averaged_equivalent_thermal_strains._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_averaged_equivalent_thermal_strains._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_averaged_equivalent_thermal_strains._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_averaged_equivalent_thermal_strains._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_averaged_equivalent_thermal_strains._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nodal_averaged_equivalent_thermal_strains._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalAveragedEquivalentThermalStrains(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_equivalent_thermal_strains._spec().outputs, op)
        self.fields_container = Output(nodal_averaged_equivalent_thermal_strains._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_averaged_equivalent_thermal_strains(Operator):
    """Read nodal averaged equivalent thermal strains as averaged nodal result from rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_averaged_equivalent_thermal_strains()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NTH_EQV", config = config, server = server)
        self.inputs = _InputsNodalAveragedEquivalentThermalStrains(self)
        self.outputs = _OutputsNodalAveragedEquivalentThermalStrains(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged equivalent thermal strains as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NTH_EQV")

#internal name: mapdl::rst::NPPL_EQV
#scripting name: nodal_averaged_equivalent_plastic_strain
class _InputsNodalAveragedEquivalentPlasticStrain(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_equivalent_plastic_strain._spec().inputs, op)
        self.time_scoping = Input(nodal_averaged_equivalent_plastic_strain._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_averaged_equivalent_plastic_strain._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_averaged_equivalent_plastic_strain._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_averaged_equivalent_plastic_strain._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_averaged_equivalent_plastic_strain._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nodal_averaged_equivalent_plastic_strain._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalAveragedEquivalentPlasticStrain(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_equivalent_plastic_strain._spec().outputs, op)
        self.fields_container = Output(nodal_averaged_equivalent_plastic_strain._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_averaged_equivalent_plastic_strain(Operator):
    """Read nodal averaged equivalent plastic strain as averaged nodal result from rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_averaged_equivalent_plastic_strain()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NPPL_EQV", config = config, server = server)
        self.inputs = _InputsNodalAveragedEquivalentPlasticStrain(self)
        self.outputs = _OutputsNodalAveragedEquivalentPlasticStrain(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged equivalent plastic strain as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NPPL_EQV")

#internal name: mapdl::rst::NCR_EQV
#scripting name: nodal_averaged_equivalent_creep_strain
class _InputsNodalAveragedEquivalentCreepStrain(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_equivalent_creep_strain._spec().inputs, op)
        self.time_scoping = Input(nodal_averaged_equivalent_creep_strain._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nodal_averaged_equivalent_creep_strain._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nodal_averaged_equivalent_creep_strain._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_averaged_equivalent_creep_strain._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_averaged_equivalent_creep_strain._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nodal_averaged_equivalent_creep_strain._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalAveragedEquivalentCreepStrain(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_equivalent_creep_strain._spec().outputs, op)
        self.fields_container = Output(nodal_averaged_equivalent_creep_strain._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_averaged_equivalent_creep_strain(Operator):
    """Read nodal averaged equivalent creep strain as averaged nodal result from rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_averaged_equivalent_creep_strain()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NCR_EQV", config = config, server = server)
        self.inputs = _InputsNodalAveragedEquivalentCreepStrain(self)
        self.outputs = _OutputsNodalAveragedEquivalentCreepStrain(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged equivalent creep strain as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NCR_EQV")

#internal name: mapdl::rst::coords_and_euler_nodes
#scripting name: euler_nodes
class _InputsEulerNodes(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(euler_nodes._spec().inputs, op)
        self.streams_container = Input(euler_nodes._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(euler_nodes._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.coord_and_euler = Input(euler_nodes._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self.coord_and_euler)
        self.mesh = Input(euler_nodes._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsEulerNodes(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(euler_nodes._spec().outputs, op)
        self.fields_container = Output(euler_nodes._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class euler_nodes(Operator):
    """read a field made of 3 coordinates and 3 Euler angles (6 dofs) by node from the rst file.

      available inputs:
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         coord_and_euler (bool)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.euler_nodes()

    """
    def __init__(self, streams_container=None, data_sources=None, coord_and_euler=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::coords_and_euler_nodes", config = config, server = server)
        self.inputs = _InputsEulerNodes(self)
        self.outputs = _OutputsEulerNodes(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if coord_and_euler !=None:
            self.inputs.coord_and_euler.connect(coord_and_euler)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""read a field made of 3 coordinates and 3 Euler angles (6 dofs) by node from the rst file.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document=""""""), 
                                 6 : PinSpecification(name = "coord_and_euler", type_names=["bool"], optional=False, document="""if true, then the field has ncomp=6 with 3 oords and 3 euler angles, else there is only the euler angles (default is true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::coords_and_euler_nodes")

#internal name: mapdl::nmisc
#scripting name: nmisc
class _InputsNmisc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nmisc._spec().inputs, op)
        self.time_scoping = Input(nmisc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(nmisc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(nmisc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nmisc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nmisc._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(nmisc._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNmisc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nmisc._spec().outputs, op)
        self.fields_container = Output(nmisc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nmisc(Operator):
    """Read NMISC results from the rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nmisc()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::nmisc", config = config, server = server)
        self.inputs = _InputsNmisc(self)
        self.outputs = _OutputsNmisc(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read NMISC results from the rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::nmisc")

#internal name: ENF_rotation_by_euler_nodes
#scripting name: enf_rotation_by_euler_nodes
class _InputsEnfRotationByEulerNodes(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(enf_rotation_by_euler_nodes._spec().inputs, op)
        self.fields_container = Input(enf_rotation_by_euler_nodes._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(enf_rotation_by_euler_nodes._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(enf_rotation_by_euler_nodes._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsEnfRotationByEulerNodes(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(enf_rotation_by_euler_nodes._spec().outputs, op)
        self.fields_container = Output(enf_rotation_by_euler_nodes._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class enf_rotation_by_euler_nodes(Operator):
    """read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

      available inputs:
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.enf_rotation_by_euler_nodes()

    """
    def __init__(self, fields_container=None, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="ENF_rotation_by_euler_nodes", config = config, server = server)
        self.inputs = _InputsEnfRotationByEulerNodes(self)
        self.outputs = _OutputsEnfRotationByEulerNodes(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.""",
                             map_input_pin_spec={
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ENF_rotation_by_euler_nodes")

#internal name: cms_matrices_provider
#scripting name: cms_matrices_provider
class _InputsCmsMatricesProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cms_matrices_provider._spec().inputs, op)
        self.data_sources = Input(cms_matrices_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsCmsMatricesProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cms_matrices_provider._spec().outputs, op)
        self.fields_container = Output(cms_matrices_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class cms_matrices_provider(Operator):
    """Read reducted matrices for cms elements. Extract stiffness, damping, mass matrices and load vector from a subfile.

      available inputs:
         data_sources (DataSources)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.cms_matrices_provider()

    """
    def __init__(self, data_sources=None, config=None, server=None):
        super().__init__(name="cms_matrices_provider", config = config, server = server)
        self.inputs = _InputsCmsMatricesProvider(self)
        self.outputs = _OutputsCmsMatricesProvider(self)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read reducted matrices for cms elements. Extract stiffness, damping, mass matrices and load vector from a subfile.""",
                             map_input_pin_spec={
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""Data_sources (must contain at list one subfile).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""Fields container containing in this order : stiffness, damping, mass matrices, and then load vector.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cms_matrices_provider")

#internal name: mapdl::smisc
#scripting name: smisc
class _InputsSmisc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(smisc._spec().inputs, op)
        self.time_scoping = Input(smisc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(smisc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(smisc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(smisc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(smisc._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.mesh = Input(smisc._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsSmisc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(smisc._spec().outputs, op)
        self.fields_container = Output(smisc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class smisc(Operator):
    """Read SMISC results from the rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.smisc()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::smisc", config = config, server = server)
        self.inputs = _InputsSmisc(self)
        self.outputs = _OutputsSmisc(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read SMISC results from the rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::smisc")

#internal name: mapdl::rst::RotateNodalFCByEulerNodes
#scripting name: nodal_rotation_by_euler_nodes
class _InputsNodalRotationByEulerNodes(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_rotation_by_euler_nodes._spec().inputs, op)
        self.fields_container = Input(nodal_rotation_by_euler_nodes._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(nodal_rotation_by_euler_nodes._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(nodal_rotation_by_euler_nodes._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsNodalRotationByEulerNodes(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_rotation_by_euler_nodes._spec().outputs, op)
        self.fields_container = Output(nodal_rotation_by_euler_nodes._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_rotation_by_euler_nodes(Operator):
    """read Euler angles on nodes from the rst file and rotate the fields in the fieldsContainer.

      available inputs:
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.nodal_rotation_by_euler_nodes()

    """
    def __init__(self, fields_container=None, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="mapdl::rst::RotateNodalFCByEulerNodes", config = config, server = server)
        self.inputs = _InputsNodalRotationByEulerNodes(self)
        self.outputs = _OutputsNodalRotationByEulerNodes(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""read Euler angles on nodes from the rst file and rotate the fields in the fieldsContainer.""",
                             map_input_pin_spec={
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::RotateNodalFCByEulerNodes")

#internal name: mapdl::rst::S_rotation_by_euler_nodes
#scripting name: stress_rotation_by_euler_nodes
class _InputsStressRotationByEulerNodes(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stress_rotation_by_euler_nodes._spec().inputs, op)
        self.fields_container = Input(stress_rotation_by_euler_nodes._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(stress_rotation_by_euler_nodes._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(stress_rotation_by_euler_nodes._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsStressRotationByEulerNodes(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stress_rotation_by_euler_nodes._spec().outputs, op)
        self.fields_container = Output(stress_rotation_by_euler_nodes._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class stress_rotation_by_euler_nodes(Operator):
    """read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

      available inputs:
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.stress_rotation_by_euler_nodes()

    """
    def __init__(self, fields_container=None, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="mapdl::rst::S_rotation_by_euler_nodes", config = config, server = server)
        self.inputs = _InputsStressRotationByEulerNodes(self)
        self.outputs = _OutputsStressRotationByEulerNodes(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.""",
                             map_input_pin_spec={
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::S_rotation_by_euler_nodes")

#internal name: mapdl::rst::EPEL_rotation_by_euler_nodes
#scripting name: elastic_strain_rotation_by_euler_nodes
class _InputsElasticStrainRotationByEulerNodes(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_rotation_by_euler_nodes._spec().inputs, op)
        self.fields_container = Input(elastic_strain_rotation_by_euler_nodes._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(elastic_strain_rotation_by_euler_nodes._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(elastic_strain_rotation_by_euler_nodes._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsElasticStrainRotationByEulerNodes(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elastic_strain_rotation_by_euler_nodes._spec().outputs, op)
        self.fields_container = Output(elastic_strain_rotation_by_euler_nodes._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elastic_strain_rotation_by_euler_nodes(Operator):
    """read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

      available inputs:
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.elastic_strain_rotation_by_euler_nodes()

    """
    def __init__(self, fields_container=None, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="mapdl::rst::EPEL_rotation_by_euler_nodes", config = config, server = server)
        self.inputs = _InputsElasticStrainRotationByEulerNodes(self)
        self.outputs = _OutputsElasticStrainRotationByEulerNodes(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.""",
                             map_input_pin_spec={
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::EPEL_rotation_by_euler_nodes")

#internal name: mapdl::rst::EPPL_rotation_by_euler_nodes
#scripting name: plastic_strain_rotation_by_euler_nodes
class _InputsPlasticStrainRotationByEulerNodes(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_rotation_by_euler_nodes._spec().inputs, op)
        self.fields_container = Input(plastic_strain_rotation_by_euler_nodes._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(plastic_strain_rotation_by_euler_nodes._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(plastic_strain_rotation_by_euler_nodes._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsPlasticStrainRotationByEulerNodes(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(plastic_strain_rotation_by_euler_nodes._spec().outputs, op)
        self.fields_container = Output(plastic_strain_rotation_by_euler_nodes._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class plastic_strain_rotation_by_euler_nodes(Operator):
    """read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.

      available inputs:
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.plastic_strain_rotation_by_euler_nodes()

    """
    def __init__(self, fields_container=None, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="mapdl::rst::EPPL_rotation_by_euler_nodes", config = config, server = server)
        self.inputs = _InputsPlasticStrainRotationByEulerNodes(self)
        self.outputs = _OutputsPlasticStrainRotationByEulerNodes(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""read Euler angles on elements from the rst file and rotate the fields in the fieldsContainer.""",
                             map_input_pin_spec={
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::EPPL_rotation_by_euler_nodes")

#internal name: PRES_Reader
#scripting name: pres_to_field
class _InputsPresToField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(pres_to_field._spec().inputs, op)
        self.filepath = Input(pres_to_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.filepath)

class _OutputsPresToField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(pres_to_field._spec().outputs, op)
        self.field = Output(pres_to_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class pres_to_field(Operator):
    """Read the presol generated file from mapdl.

      available inputs:
         filepath (str)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.result.pres_to_field()

    """
    def __init__(self, filepath=None, config=None, server=None):
        super().__init__(name="PRES_Reader", config = config, server = server)
        self.inputs = _InputsPresToField(self)
        self.outputs = _OutputsPresToField(self)
        if filepath !=None:
            self.inputs.filepath.connect(filepath)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read the presol generated file from mapdl.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "filepath", type_names=["string"], optional=False, document="""filepath""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "PRES_Reader")

#internal name: PRNS_Reader
#scripting name: prns_to_field
class _InputsPrnsToField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(prns_to_field._spec().inputs, op)
        self.filepath = Input(prns_to_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.filepath)

class _OutputsPrnsToField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(prns_to_field._spec().outputs, op)
        self.field = Output(prns_to_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class prns_to_field(Operator):
    """Read the presol of nodal field generated file from mapdl.

      available inputs:
         filepath (str)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.result.prns_to_field()

    """
    def __init__(self, filepath=None, config=None, server=None):
        super().__init__(name="PRNS_Reader", config = config, server = server)
        self.inputs = _InputsPrnsToField(self)
        self.outputs = _OutputsPrnsToField(self)
        if filepath !=None:
            self.inputs.filepath.connect(filepath)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read the presol of nodal field generated file from mapdl.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "filepath", type_names=["string"], optional=False, document="""filepath""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "PRNS_Reader")

#internal name: ExtractRigidBodyMotion
#scripting name: remove_rigid_body_motion
class _InputsRemoveRigidBodyMotion(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(remove_rigid_body_motion._spec().inputs, op)
        self.field = Input(remove_rigid_body_motion._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.reference_node_id = Input(remove_rigid_body_motion._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.reference_node_id)
        self.mesh = Input(remove_rigid_body_motion._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsRemoveRigidBodyMotion(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(remove_rigid_body_motion._spec().outputs, op)
        self.field = Output(remove_rigid_body_motion._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class remove_rigid_body_motion(Operator):
    """Removes rigid body mode from a total displacement field by minimization. Use a reference point in order to substract its displacement to the result displacement field.

      available inputs:
         field (Field, FieldsContainer)
         reference_node_id (int) (optional)
         mesh (MeshedRegion) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.result.remove_rigid_body_motion()

    """
    def __init__(self, field=None, reference_node_id=None, mesh=None, config=None, server=None):
        super().__init__(name="ExtractRigidBodyMotion", config = config, server = server)
        self.inputs = _InputsRemoveRigidBodyMotion(self)
        self.outputs = _OutputsRemoveRigidBodyMotion(self)
        if field !=None:
            self.inputs.field.connect(field)
        if reference_node_id !=None:
            self.inputs.reference_node_id.connect(reference_node_id)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Removes rigid body mode from a total displacement field by minimization. Use a reference point in order to substract its displacement to the result displacement field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "reference_node_id", type_names=["int32"], optional=True, document="""Id of the reference entity (node)."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""default is the mesh in the support""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ExtractRigidBodyMotion")

#internal name: ExtractRigidBodyMotion_fc
#scripting name: remove_rigid_body_motion_fc
class _InputsRemoveRigidBodyMotionFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(remove_rigid_body_motion_fc._spec().inputs, op)
        self.fields_container = Input(remove_rigid_body_motion_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.reference_node_id = Input(remove_rigid_body_motion_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.reference_node_id)
        self.mesh = Input(remove_rigid_body_motion_fc._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsRemoveRigidBodyMotionFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(remove_rigid_body_motion_fc._spec().outputs, op)
        self.fields_container = Output(remove_rigid_body_motion_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class remove_rigid_body_motion_fc(Operator):
    """Removes rigid body mode from a total displacement field by minimization. Use a reference point in order to substract its displacement to the result displacement field.

      available inputs:
         fields_container (FieldsContainer)
         reference_node_id (int) (optional)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.remove_rigid_body_motion_fc()

    """
    def __init__(self, fields_container=None, reference_node_id=None, mesh=None, config=None, server=None):
        super().__init__(name="ExtractRigidBodyMotion_fc", config = config, server = server)
        self.inputs = _InputsRemoveRigidBodyMotionFc(self)
        self.outputs = _OutputsRemoveRigidBodyMotionFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if reference_node_id !=None:
            self.inputs.reference_node_id.connect(reference_node_id)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Removes rigid body mode from a total displacement field by minimization. Use a reference point in order to substract its displacement to the result displacement field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "reference_node_id", type_names=["int32"], optional=True, document="""Id of the reference entity (node)."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""default is the mesh in the support""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ExtractRigidBodyMotion_fc")

#internal name: RigidBodyAddition_fc
#scripting name: add_rigid_body_motion_fc
class _InputsAddRigidBodyMotionFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(add_rigid_body_motion_fc._spec().inputs, op)
        self.fields_container = Input(add_rigid_body_motion_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.translation_field = Input(add_rigid_body_motion_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.translation_field)
        self.rotation_field = Input(add_rigid_body_motion_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.rotation_field)
        self.center_field = Input(add_rigid_body_motion_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.center_field)
        self.mesh = Input(add_rigid_body_motion_fc._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsAddRigidBodyMotionFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(add_rigid_body_motion_fc._spec().outputs, op)
        self.fields_container = Output(add_rigid_body_motion_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class add_rigid_body_motion_fc(Operator):
    """Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem

      available inputs:
         fields_container (FieldsContainer)
         translation_field (Field)
         rotation_field (Field)
         center_field (Field)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.result.add_rigid_body_motion_fc()

    """
    def __init__(self, fields_container=None, translation_field=None, rotation_field=None, center_field=None, mesh=None, config=None, server=None):
        super().__init__(name="RigidBodyAddition_fc", config = config, server = server)
        self.inputs = _InputsAddRigidBodyMotionFc(self)
        self.outputs = _OutputsAddRigidBodyMotionFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if translation_field !=None:
            self.inputs.translation_field.connect(translation_field)
        if rotation_field !=None:
            self.inputs.rotation_field.connect(rotation_field)
        if center_field !=None:
            self.inputs.center_field.connect(center_field)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "translation_field", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "rotation_field", type_names=["field"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "center_field", type_names=["field"], optional=False, document=""""""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""default is the mesh in the support""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "RigidBodyAddition_fc")

#internal name: mapdl::rst::U_cyclic
#scripting name: cyclic_expanded_displacement
class _InputsCyclicExpandedDisplacement(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_displacement._spec().inputs, op)
        self.time_scoping = Input(cyclic_expanded_displacement._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_expanded_displacement._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_expanded_displacement._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(cyclic_expanded_displacement._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(cyclic_expanded_displacement._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(cyclic_expanded_displacement._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.sector_mesh = Input(cyclic_expanded_displacement._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.sector_mesh)
        self.requested_location = Input(cyclic_expanded_displacement._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(cyclic_expanded_displacement._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)
        self.expanded_meshed_region = Input(cyclic_expanded_displacement._spec().input_pin(15), 15, op, -1) 
        self._inputs.append(self.expanded_meshed_region)
        self.cyclic_support = Input(cyclic_expanded_displacement._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)
        self.sectors_to_expand = Input(cyclic_expanded_displacement._spec().input_pin(18), 18, op, -1) 
        self._inputs.append(self.sectors_to_expand)
        self.phi = Input(cyclic_expanded_displacement._spec().input_pin(19), 19, op, -1) 
        self._inputs.append(self.phi)

class _OutputsCyclicExpandedDisplacement(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_displacement._spec().outputs, op)
        self.fields_container = Output(cyclic_expanded_displacement._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)
        self.expanded_meshes = Output(cyclic_expanded_displacement._spec().output_pin(1), 1, op) 
        self._outputs.append(self.expanded_meshes)

class cyclic_expanded_displacement(Operator):
    """Read displacements from an rst file and expand it with cyclic symmetry.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         sector_mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)
         expanded_meshed_region (MeshedRegion, MeshesContainer) (optional)
         cyclic_support (CyclicSupport) (optional)
         sectors_to_expand (list, Scoping, ScopingsContainer) (optional)
         phi (float) (optional)

      available outputs:
         fields_container (FieldsContainer)
         expanded_meshes (MeshesContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_expanded_displacement()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, bool_rotate_to_global=None, sector_mesh=None, requested_location=None, read_cyclic=None, expanded_meshed_region=None, cyclic_support=None, sectors_to_expand=None, phi=None, config=None, server=None):
        super().__init__(name="mapdl::rst::U_cyclic", config = config, server = server)
        self.inputs = _InputsCyclicExpandedDisplacement(self)
        self.outputs = _OutputsCyclicExpandedDisplacement(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if bool_rotate_to_global !=None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if sector_mesh !=None:
            self.inputs.sector_mesh.connect(sector_mesh)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if read_cyclic !=None:
            self.inputs.read_cyclic.connect(read_cyclic)
        if expanded_meshed_region !=None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)
        if sectors_to_expand !=None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)
        if phi !=None:
            self.inputs.phi.connect(phi)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read displacements from an rst file and expand it with cyclic symmetry.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is roated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "sector_mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh of the base sector (can be a skin)."""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""location needed in output"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)"""), 
                                 15 : PinSpecification(name = "expanded_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh expanded."""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=True, document=""""""), 
                                 18 : PinSpecification(name = "sectors_to_expand", type_names=["vector<int32>","scoping","scopings_container"], optional=True, document="""sectors to expand (start at 0), for multistage: use scopings container with 'stage' label."""), 
                                 19 : PinSpecification(name = "phi", type_names=["double"], optional=True, document="""angle phi (default value 0.0)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in"""), 
                                 1 : PinSpecification(name = "expanded_meshes", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::U_cyclic")

#internal name: mapdl::rst::A_cyclic
#scripting name: cyclic_expanded_acceleration
class _InputsCyclicExpandedAcceleration(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_acceleration._spec().inputs, op)
        self.time_scoping = Input(cyclic_expanded_acceleration._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_expanded_acceleration._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_expanded_acceleration._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(cyclic_expanded_acceleration._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(cyclic_expanded_acceleration._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(cyclic_expanded_acceleration._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.sector_mesh = Input(cyclic_expanded_acceleration._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.sector_mesh)
        self.requested_location = Input(cyclic_expanded_acceleration._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(cyclic_expanded_acceleration._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)
        self.expanded_meshed_region = Input(cyclic_expanded_acceleration._spec().input_pin(15), 15, op, -1) 
        self._inputs.append(self.expanded_meshed_region)
        self.cyclic_support = Input(cyclic_expanded_acceleration._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)
        self.sectors_to_expand = Input(cyclic_expanded_acceleration._spec().input_pin(18), 18, op, -1) 
        self._inputs.append(self.sectors_to_expand)
        self.phi = Input(cyclic_expanded_acceleration._spec().input_pin(19), 19, op, -1) 
        self._inputs.append(self.phi)

class _OutputsCyclicExpandedAcceleration(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_acceleration._spec().outputs, op)
        self.fields_container = Output(cyclic_expanded_acceleration._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)
        self.expanded_meshes = Output(cyclic_expanded_acceleration._spec().output_pin(1), 1, op) 
        self._outputs.append(self.expanded_meshes)

class cyclic_expanded_acceleration(Operator):
    """Read acceleration from an rst file and expand it with cyclic symmetry.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         sector_mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)
         expanded_meshed_region (MeshedRegion, MeshesContainer) (optional)
         cyclic_support (CyclicSupport) (optional)
         sectors_to_expand (list, Scoping, ScopingsContainer) (optional)
         phi (float) (optional)

      available outputs:
         fields_container (FieldsContainer)
         expanded_meshes (MeshesContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_expanded_acceleration()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, bool_rotate_to_global=None, sector_mesh=None, requested_location=None, read_cyclic=None, expanded_meshed_region=None, cyclic_support=None, sectors_to_expand=None, phi=None, config=None, server=None):
        super().__init__(name="mapdl::rst::A_cyclic", config = config, server = server)
        self.inputs = _InputsCyclicExpandedAcceleration(self)
        self.outputs = _OutputsCyclicExpandedAcceleration(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if bool_rotate_to_global !=None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if sector_mesh !=None:
            self.inputs.sector_mesh.connect(sector_mesh)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if read_cyclic !=None:
            self.inputs.read_cyclic.connect(read_cyclic)
        if expanded_meshed_region !=None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)
        if sectors_to_expand !=None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)
        if phi !=None:
            self.inputs.phi.connect(phi)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read acceleration from an rst file and expand it with cyclic symmetry.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is roated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "sector_mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh of the base sector (can be a skin)."""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""location needed in output"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)"""), 
                                 15 : PinSpecification(name = "expanded_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh expanded."""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=True, document=""""""), 
                                 18 : PinSpecification(name = "sectors_to_expand", type_names=["vector<int32>","scoping","scopings_container"], optional=True, document="""sectors to expand (start at 0), for multistage: use scopings container with 'stage' label."""), 
                                 19 : PinSpecification(name = "phi", type_names=["double"], optional=True, document="""angle phi (default value 0.0)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in"""), 
                                 1 : PinSpecification(name = "expanded_meshes", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::A_cyclic")

#internal name: mapdl::rst::S_cyclic
#scripting name: cyclic_expanded_stress
class _InputsCyclicExpandedStress(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_stress._spec().inputs, op)
        self.time_scoping = Input(cyclic_expanded_stress._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_expanded_stress._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_expanded_stress._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(cyclic_expanded_stress._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(cyclic_expanded_stress._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(cyclic_expanded_stress._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.sector_mesh = Input(cyclic_expanded_stress._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.sector_mesh)
        self.requested_location = Input(cyclic_expanded_stress._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(cyclic_expanded_stress._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)
        self.expanded_meshed_region = Input(cyclic_expanded_stress._spec().input_pin(15), 15, op, -1) 
        self._inputs.append(self.expanded_meshed_region)
        self.cyclic_support = Input(cyclic_expanded_stress._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)
        self.sectors_to_expand = Input(cyclic_expanded_stress._spec().input_pin(18), 18, op, -1) 
        self._inputs.append(self.sectors_to_expand)
        self.phi = Input(cyclic_expanded_stress._spec().input_pin(19), 19, op, -1) 
        self._inputs.append(self.phi)

class _OutputsCyclicExpandedStress(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_stress._spec().outputs, op)
        self.fields_container = Output(cyclic_expanded_stress._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)
        self.expanded_meshes = Output(cyclic_expanded_stress._spec().output_pin(1), 1, op) 
        self._outputs.append(self.expanded_meshes)

class cyclic_expanded_stress(Operator):
    """Read mapdl::rst::S from an rst file and expand it with cyclic symmetry.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         sector_mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)
         expanded_meshed_region (MeshedRegion, MeshesContainer) (optional)
         cyclic_support (CyclicSupport) (optional)
         sectors_to_expand (list, Scoping, ScopingsContainer) (optional)
         phi (float) (optional)

      available outputs:
         fields_container (FieldsContainer)
         expanded_meshes (MeshesContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_expanded_stress()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, bool_rotate_to_global=None, sector_mesh=None, requested_location=None, read_cyclic=None, expanded_meshed_region=None, cyclic_support=None, sectors_to_expand=None, phi=None, config=None, server=None):
        super().__init__(name="mapdl::rst::S_cyclic", config = config, server = server)
        self.inputs = _InputsCyclicExpandedStress(self)
        self.outputs = _OutputsCyclicExpandedStress(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if bool_rotate_to_global !=None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if sector_mesh !=None:
            self.inputs.sector_mesh.connect(sector_mesh)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if read_cyclic !=None:
            self.inputs.read_cyclic.connect(read_cyclic)
        if expanded_meshed_region !=None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)
        if sectors_to_expand !=None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)
        if phi !=None:
            self.inputs.phi.connect(phi)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read mapdl::rst::S from an rst file and expand it with cyclic symmetry.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is roated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "sector_mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh of the base sector (can be a skin)."""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""location needed in output"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)"""), 
                                 15 : PinSpecification(name = "expanded_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh expanded."""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=True, document=""""""), 
                                 18 : PinSpecification(name = "sectors_to_expand", type_names=["vector<int32>","scoping","scopings_container"], optional=True, document="""sectors to expand (start at 0), for multistage: use scopings container with 'stage' label."""), 
                                 19 : PinSpecification(name = "phi", type_names=["double"], optional=True, document="""phi angle (default value 0.0)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in"""), 
                                 1 : PinSpecification(name = "expanded_meshes", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::S_cyclic")

#internal name: mapdl::rst::ENF_cyclic
#scripting name: cyclic_expanded_enf
class _InputsCyclicExpandedEnf(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_enf._spec().inputs, op)
        self.time_scoping = Input(cyclic_expanded_enf._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_expanded_enf._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_expanded_enf._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(cyclic_expanded_enf._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(cyclic_expanded_enf._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(cyclic_expanded_enf._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.sector_mesh = Input(cyclic_expanded_enf._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.sector_mesh)
        self.requested_location = Input(cyclic_expanded_enf._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.read_cyclic = Input(cyclic_expanded_enf._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)
        self.expanded_meshed_region = Input(cyclic_expanded_enf._spec().input_pin(15), 15, op, -1) 
        self._inputs.append(self.expanded_meshed_region)
        self.cyclic_support = Input(cyclic_expanded_enf._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)
        self.sectors_to_expand = Input(cyclic_expanded_enf._spec().input_pin(18), 18, op, -1) 
        self._inputs.append(self.sectors_to_expand)
        self.phi = Input(cyclic_expanded_enf._spec().input_pin(19), 19, op, -1) 
        self._inputs.append(self.phi)

class _OutputsCyclicExpandedEnf(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_enf._spec().outputs, op)
        self.fields_container = Output(cyclic_expanded_enf._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)
        self.expanded_meshes = Output(cyclic_expanded_enf._spec().output_pin(1), 1, op) 
        self._outputs.append(self.expanded_meshes)

class cyclic_expanded_enf(Operator):
    """Read ENF from an rst file and expand it with cyclic symmetry.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         sector_mesh (MeshedRegion, MeshesContainer) (optional)
         requested_location (str) (optional)
         read_cyclic (int) (optional)
         expanded_meshed_region (MeshedRegion, MeshesContainer) (optional)
         cyclic_support (CyclicSupport) (optional)
         sectors_to_expand (list, Scoping, ScopingsContainer) (optional)
         phi (float) (optional)

      available outputs:
         fields_container (FieldsContainer)
         expanded_meshes (MeshesContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_expanded_enf()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, bool_rotate_to_global=None, sector_mesh=None, requested_location=None, read_cyclic=None, expanded_meshed_region=None, cyclic_support=None, sectors_to_expand=None, phi=None, config=None, server=None):
        super().__init__(name="mapdl::rst::ENF_cyclic", config = config, server = server)
        self.inputs = _InputsCyclicExpandedEnf(self)
        self.outputs = _OutputsCyclicExpandedEnf(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if bool_rotate_to_global !=None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if sector_mesh !=None:
            self.inputs.sector_mesh.connect(sector_mesh)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if read_cyclic !=None:
            self.inputs.read_cyclic.connect(read_cyclic)
        if expanded_meshed_region !=None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)
        if sectors_to_expand !=None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)
        if phi !=None:
            self.inputs.phi.connect(phi)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read ENF from an rst file and expand it with cyclic symmetry.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is roated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "sector_mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh of the base sector (can be a skin)."""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""location needed in output"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)"""), 
                                 15 : PinSpecification(name = "expanded_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh expanded."""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=True, document=""""""), 
                                 18 : PinSpecification(name = "sectors_to_expand", type_names=["vector<int32>","scoping","scopings_container"], optional=True, document="""sectors to expand (start at 0), for multistage: use scopings container with 'stage' label."""), 
                                 19 : PinSpecification(name = "phi", type_names=["double"], optional=True, document="""phi angle (default value 0.0)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in"""), 
                                 1 : PinSpecification(name = "expanded_meshes", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::ENF_cyclic")

#internal name: mapdl::rst::ENG_VOL_cyclic
#scripting name: cyclic_volume
class _InputsCyclicVolume(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_volume._spec().inputs, op)
        self.time_scoping = Input(cyclic_volume._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_volume._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_volume._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(cyclic_volume._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(cyclic_volume._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(cyclic_volume._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.sector_mesh = Input(cyclic_volume._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.sector_mesh)
        self.read_cyclic = Input(cyclic_volume._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)
        self.expanded_meshed_region = Input(cyclic_volume._spec().input_pin(15), 15, op, -1) 
        self._inputs.append(self.expanded_meshed_region)
        self.cyclic_support = Input(cyclic_volume._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)

class _OutputsCyclicVolume(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_volume._spec().outputs, op)
        self.fields_container = Output(cyclic_volume._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)
        self.expanded_meshes = Output(cyclic_volume._spec().output_pin(1), 1, op) 
        self._outputs.append(self.expanded_meshes)

class cyclic_volume(Operator):
    """Read mapdl::rst::ENG_VOL from an rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         sector_mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)
         expanded_meshed_region (MeshedRegion, MeshesContainer) (optional)
         cyclic_support (CyclicSupport) (optional)

      available outputs:
         fields_container (FieldsContainer)
         expanded_meshes (MeshesContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_volume()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, bool_rotate_to_global=None, sector_mesh=None, read_cyclic=None, expanded_meshed_region=None, cyclic_support=None, config=None, server=None):
        super().__init__(name="mapdl::rst::ENG_VOL_cyclic", config = config, server = server)
        self.inputs = _InputsCyclicVolume(self)
        self.outputs = _OutputsCyclicVolume(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if bool_rotate_to_global !=None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if sector_mesh !=None:
            self.inputs.sector_mesh.connect(sector_mesh)
        if read_cyclic !=None:
            self.inputs.read_cyclic.connect(read_cyclic)
        if expanded_meshed_region !=None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read mapdl::rst::ENG_VOL from an rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is roated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "sector_mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh of the base sector (can be a skin)."""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)"""), 
                                 15 : PinSpecification(name = "expanded_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh expanded."""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in"""), 
                                 1 : PinSpecification(name = "expanded_meshes", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::ENG_VOL_cyclic")

#internal name: mapdl::rst::ENG_SE_cyclic
#scripting name: cyclic_strain_energy
class _InputsCyclicStrainEnergy(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_strain_energy._spec().inputs, op)
        self.time_scoping = Input(cyclic_strain_energy._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(cyclic_strain_energy._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.fields_container = Input(cyclic_strain_energy._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_container)
        self.streams_container = Input(cyclic_strain_energy._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(cyclic_strain_energy._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.bool_rotate_to_global = Input(cyclic_strain_energy._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.bool_rotate_to_global)
        self.sector_mesh = Input(cyclic_strain_energy._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.sector_mesh)
        self.read_cyclic = Input(cyclic_strain_energy._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)
        self.expanded_meshed_region = Input(cyclic_strain_energy._spec().input_pin(15), 15, op, -1) 
        self._inputs.append(self.expanded_meshed_region)
        self.cyclic_support = Input(cyclic_strain_energy._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)

class _OutputsCyclicStrainEnergy(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_strain_energy._spec().outputs, op)
        self.fields_container = Output(cyclic_strain_energy._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)
        self.expanded_meshes = Output(cyclic_strain_energy._spec().output_pin(1), 1, op) 
        self._outputs.append(self.expanded_meshes)

class cyclic_strain_energy(Operator):
    """Computes mapdl::rst::ENG_SE from an rst file.

      available inputs:
         time_scoping (Scoping, list) (optional)
         mesh_scoping (ScopingsContainer, Scoping, list) (optional)
         fields_container (FieldsContainer) (optional)
         streams_container (StreamsContainer, Stream) (optional)
         data_sources (DataSources)
         bool_rotate_to_global (bool) (optional)
         sector_mesh (MeshedRegion, MeshesContainer) (optional)
         read_cyclic (int) (optional)
         expanded_meshed_region (MeshedRegion, MeshesContainer) (optional)
         cyclic_support (CyclicSupport) (optional)

      available outputs:
         fields_container (FieldsContainer)
         expanded_meshes (MeshesContainer)

      Examples
      --------
      >>> op = operators.result.cyclic_strain_energy()

    """
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, bool_rotate_to_global=None, sector_mesh=None, read_cyclic=None, expanded_meshed_region=None, cyclic_support=None, config=None, server=None):
        super().__init__(name="mapdl::rst::ENG_SE_cyclic", config = config, server = server)
        self.inputs = _InputsCyclicStrainEnergy(self)
        self.outputs = _OutputsCyclicStrainEnergy(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if bool_rotate_to_global !=None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if sector_mesh !=None:
            self.inputs.sector_mesh.connect(sector_mesh)
        if read_cyclic !=None:
            self.inputs.read_cyclic.connect(read_cyclic)
        if expanded_meshed_region !=None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes mapdl::rst::ENG_SE from an rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is roated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "sector_mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh of the base sector (can be a skin)."""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)"""), 
                                 15 : PinSpecification(name = "expanded_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh expanded."""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in"""), 
                                 1 : PinSpecification(name = "expanded_meshes", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::ENG_SE_cyclic")

