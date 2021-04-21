from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from /shared/home1/cbellot/ansys_inc/v212/aisol/dll/linx64/libAns.Dpf.FEMutils.so plugin, from "scoping" category
"""

#internal name: MeshScopingProvider
#scripting name: from_mesh
class _InputsFromMesh(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(from_mesh._spec().inputs, op)
        self.mesh = Input(from_mesh._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(from_mesh._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.requested_location)

class _OutputsFromMesh(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(from_mesh._spec().outputs, op)
        self.scoping = Output(from_mesh._spec().output_pin(0), 0, op) 
        self._outputs.append(self.scoping)

class from_mesh(Operator):
    """Provides the entire mesh scoping based on the requested location

      available inputs:
         mesh (MeshedRegion)
         requested_location (str) (optional)

      available outputs:
         scoping (Scoping)

      Examples
      --------
      op = operators.scoping.from_mesh()

    """
    def __init__(self, mesh=None, requested_location=None, config=None, server=None):
        super().__init__(name="MeshScopingProvider", config = config, server = server)
        self.inputs = _InputsFromMesh(self)
        self.outputs = _OutputsFromMesh(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Provides the entire mesh scoping based on the requested location""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""if nothing the operator returns the nodes scoping, possible locations are: Nodal or Elemental""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "MeshScopingProvider")

from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from /shared/home1/cbellot/ansys_inc/v212/aisol/dll/linx64/libAns.Dpf.Native.so plugin, from "scoping" category
"""

#internal name: rescope_fc
#scripting name: change_fc
class _InputsChangeFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(change_fc._spec().inputs, op)
        self.fields_container = Input(change_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.scopings_container = Input(change_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.scopings_container)

class _OutputsChangeFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(change_fc._spec().outputs, op)
        self.fields_container = Output(change_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class change_fc(Operator):
    """Rescope a fields container to correspond to a scopings container

      available inputs:
         fields_container (FieldsContainer)
         scopings_container (ScopingsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      op = operators.scoping.change_fc()

    """
    def __init__(self, fields_container=None, scopings_container=None, config=None, server=None):
        super().__init__(name="rescope_fc", config = config, server = server)
        self.inputs = _InputsChangeFc(self)
        self.outputs = _OutputsChangeFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if scopings_container !=None:
            self.inputs.scopings_container.connect(scopings_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rescope a fields container to correspond to a scopings container""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scopings_container", type_names=["scopings_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "rescope_fc")

#internal name: GetNodeScopingFromMesh
#scripting name: nodal_from_mesh
class _InputsNodalFromMesh(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_from_mesh._spec().inputs, op)
        self.mesh = Input(nodal_from_mesh._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalFromMesh(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_from_mesh._spec().outputs, op)
        self.mesh_scoping = Output(nodal_from_mesh._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh_scoping)

class nodal_from_mesh(Operator):
    """Get the nodes ids scoping of an input mesh.

      available inputs:
         mesh (MeshedRegion)

      available outputs:
         mesh_scoping (Scoping)

      Examples
      --------
      op = operators.scoping.nodal_from_mesh()

    """
    def __init__(self, mesh=None, config=None, server=None):
        super().__init__(name="GetNodeScopingFromMesh", config = config, server = server)
        self.inputs = _InputsNodalFromMesh(self)
        self.outputs = _OutputsNodalFromMesh(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Get the nodes ids scoping of an input mesh.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "GetNodeScopingFromMesh")

#internal name: scoping::connectivity_ids
#scripting name: connectivity_ids
class _InputsConnectivityIds(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(connectivity_ids._spec().inputs, op)
        self.mesh_scoping = Input(connectivity_ids._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.mesh = Input(connectivity_ids._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.take_mid_nodes = Input(connectivity_ids._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self.take_mid_nodes)

class _OutputsConnectivityIds(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(connectivity_ids._spec().outputs, op)
        self.mesh_scoping = Output(connectivity_ids._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh_scoping)
        self.elemental_scoping = Output(connectivity_ids._spec().output_pin(1), 1, op) 
        self._outputs.append(self.elemental_scoping)

class connectivity_ids(Operator):
    """Returns the ordered node ids corresponding to the element ids scoping in input. For each element the node ids are its connectivity.

      available inputs:
         mesh_scoping (Scoping)
         mesh (MeshedRegion) (optional)
         take_mid_nodes (bool) (optional)

      available outputs:
         mesh_scoping (Scoping)
         elemental_scoping (Scoping)

      Examples
      --------
      op = operators.scoping.connectivity_ids()

    """
    def __init__(self, mesh_scoping=None, mesh=None, take_mid_nodes=None, config=None, server=None):
        super().__init__(name="scoping::connectivity_ids", config = config, server = server)
        self.inputs = _InputsConnectivityIds(self)
        self.outputs = _OutputsConnectivityIds(self)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if take_mid_nodes !=None:
            self.inputs.take_mid_nodes.connect(take_mid_nodes)

    @staticmethod
    def _spec():
        spec = Specification(description="""Returns the ordered node ids corresponding to the element ids scoping in input. For each element the node ids are its connectivity.""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document="""Elemental scoping"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""the support of the scoping is expected if there is no mesh in input"""), 
                                 10 : PinSpecification(name = "take_mid_nodes", type_names=["bool"], optional=True, document="""default is true""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "elemental_scoping", type_names=["scoping"], optional=False, document="""same as the input scoping but with ids dupplicated to havve the same size as nodal output scoping""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scoping::connectivity_ids")

#internal name: scoping::by_property
#scripting name: splitted_on_property_type
class _InputsSplittedOnPropertyType(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(splitted_on_property_type._spec().inputs, op)
        self.mesh_scoping = Input(splitted_on_property_type._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.mesh = Input(splitted_on_property_type._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.requested_location = Input(splitted_on_property_type._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)
        self.label1 = Input(splitted_on_property_type._spec().input_pin(13), 13, op, 0) 
        self._inputs.append(self.label1)
        self.label2 = Input(splitted_on_property_type._spec().input_pin(14), 14, op, 1) 
        self._inputs.append(self.label2)

class _OutputsSplittedOnPropertyType(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(splitted_on_property_type._spec().outputs, op)
        self.mesh_scoping = Output(splitted_on_property_type._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh_scoping)

class splitted_on_property_type(Operator):
    """Splits a given scoping or the mesh scoping (nodal or elemental) on given properties (elshape and/or material) and returns a scopings container with those splitted scopings.

      available inputs:
         mesh_scoping (Scoping) (optional)
         mesh (MeshedRegion)
         requested_location (str)
         label1 (str) (optional)
         label2 (str) (optional)

      available outputs:
         mesh_scoping (ScopingsContainer)

      Examples
      --------
      op = operators.scoping.splitted_on_property_type()

    """
    def __init__(self, mesh_scoping=None, mesh=None, requested_location=None, label1=None, label2=None, config=None, server=None):
        super().__init__(name="scoping::by_property", config = config, server = server)
        self.inputs = _InputsSplittedOnPropertyType(self)
        self.outputs = _OutputsSplittedOnPropertyType(self)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if label1 !=None:
            self.inputs.label1.connect(label1)
        if label2 !=None:
            self.inputs.label2.connect(label2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Splits a given scoping or the mesh scoping (nodal or elemental) on given properties (elshape and/or material) and returns a scopings container with those splitted scopings.""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""Scoping"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""mesh region"""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=False, document="""location (default is elemental)"""), 
                                 13 : PinSpecification(name = "label", type_names=["string"], optional=True, document="""properties to apply the filtering 'mat' and/or 'elshape' (default is 'elshape)"""), 
                                 14 : PinSpecification(name = "label", type_names=["string"], optional=True, document="""properties to apply the filtering 'mat' and/or 'elshape' (default is 'elshape)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container"], optional=False, document="""Scoping""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scoping::by_property")

#internal name: scoping::intersect
#scripting name: intersect
class _InputsIntersect(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(intersect._spec().inputs, op)
        self.scopingA = Input(intersect._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.scopingA)
        self.scopingB = Input(intersect._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.scopingB)

class _OutputsIntersect(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(intersect._spec().outputs, op)
        self.intersection = Output(intersect._spec().output_pin(0), 0, op) 
        self._outputs.append(self.intersection)
        self.scopingA_min_intersection = Output(intersect._spec().output_pin(1), 1, op) 
        self._outputs.append(self.scopingA_min_intersection)

class intersect(Operator):
    """Intersect 2 scopings and return the intersection and the difference between the intersection and the first scoping.

      available inputs:
         scopingA (Scoping)
         scopingB (Scoping)

      available outputs:
         intersection (Scoping)
         scopingA_min_intersection (Scoping)

      Examples
      --------
      op = operators.scoping.intersect()

    """
    def __init__(self, scopingA=None, scopingB=None, config=None, server=None):
        super().__init__(name="scoping::intersect", config = config, server = server)
        self.inputs = _InputsIntersect(self)
        self.outputs = _OutputsIntersect(self)
        if scopingA !=None:
            self.inputs.scopingA.connect(scopingA)
        if scopingB !=None:
            self.inputs.scopingB.connect(scopingB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Intersect 2 scopings and return the intersection and the difference between the intersection and the first scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "scopingA", type_names=["scoping"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scopingB", type_names=["scoping"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "intersection", type_names=["scoping"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scopingA_min_intersection", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scoping::intersect")

#internal name: transpose_scoping
#scripting name: transpose
class _InputsTranspose(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(transpose._spec().inputs, op)
        self.mesh_scoping = Input(transpose._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.meshed_region = Input(transpose._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.meshed_region)
        self.inclusive = Input(transpose._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.inclusive)

class _OutputsTranspose(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(transpose._spec().outputs, op)
        self.mesh_scoping_as_scoping = Output( _modify_output_spec_with_one_type(transpose._spec().output_pin(0), "scoping"), 0, op) 
        self._outputs.append(self.mesh_scoping_as_scoping)
        self.mesh_scoping_as_scopings_container = Output( _modify_output_spec_with_one_type(transpose._spec().output_pin(0), "scopings_container"), 0, op) 
        self._outputs.append(self.mesh_scoping_as_scopings_container)

class transpose(Operator):
    """Transposes the input scoping or scopings container (Elemental --> Nodal, or Nodal ---> Elemental), based on the input mesh region.

      available inputs:
         mesh_scoping (Scoping, ScopingsContainer)
         meshed_region (MeshedRegion, MeshesContainer)
         inclusive (int) (optional)

      available outputs:
         mesh_scoping (Scoping ,ScopingsContainer)

      Examples
      --------
      op = operators.scoping.transpose()

    """
    def __init__(self, mesh_scoping=None, meshed_region=None, inclusive=None, config=None, server=None):
        super().__init__(name="transpose_scoping", config = config, server = server)
        self.inputs = _InputsTranspose(self)
        self.outputs = _OutputsTranspose(self)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if meshed_region !=None:
            self.inputs.meshed_region.connect(meshed_region)
        if inclusive !=None:
            self.inputs.inclusive.connect(inclusive)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transposes the input scoping or scopings container (Elemental --> Nodal, or Nodal ---> Elemental), based on the input mesh region.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping","scopings_container"], optional=False, document="""Scoping or scopings container (the input type is the output type)"""), 
                                 1 : PinSpecification(name = "meshed_region", type_names=["meshed_region","meshes_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "inclusive", type_names=["int32"], optional=True, document="""if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping","scopings_container"], optional=False, document="""Scoping or scopings container (the input type is the output type)""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "transpose_scoping")

#internal name: scoping_provider_by_prop
#scripting name: on_property
class _InputsOnProperty(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(on_property._spec().inputs, op)
        self.requested_location = Input(on_property._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.requested_location)
        self.property_name = Input(on_property._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.property_name)
        self.property_id = Input(on_property._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.property_id)
        self.streams_container = Input(on_property._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(on_property._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.inclusive = Input(on_property._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.inclusive)

class _OutputsOnProperty(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(on_property._spec().outputs, op)
        self.mesh_scoping = Output(on_property._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh_scoping)

class on_property(Operator):
    """Provides a scoping at a given location based on a given property name and a property number.

      available inputs:
         requested_location (str)
         property_name (str)
         property_id (int)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         inclusive (int) (optional)

      available outputs:
         mesh_scoping (Scoping)

      Examples
      --------
      op = operators.scoping.on_property()

    """
    def __init__(self, requested_location=None, property_name=None, property_id=None, streams_container=None, data_sources=None, inclusive=None, config=None, server=None):
        super().__init__(name="scoping_provider_by_prop", config = config, server = server)
        self.inputs = _InputsOnProperty(self)
        self.outputs = _OutputsOnProperty(self)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if property_name !=None:
            self.inputs.property_name.connect(property_name)
        if property_id !=None:
            self.inputs.property_id.connect(property_id)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if inclusive !=None:
            self.inputs.inclusive.connect(inclusive)

    @staticmethod
    def _spec():
        spec = Specification(description="""Provides a scoping at a given location based on a given property name and a property number.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "requested_location", type_names=["string"], optional=False, document="""Nodal or Elemental location are expected"""), 
                                 1 : PinSpecification(name = "property_name", type_names=["string"], optional=False, document="""ex "mapdl_element_type", "apdl_type_index", "mapdl_type_id", "material", "apdl_section_id", "apdl_real_id", "shell_axi", "volume_axi"..."""), 
                                 2 : PinSpecification(name = "property_id", type_names=["int32"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document=""""""), 
                                 5 : PinSpecification(name = "inclusive", type_names=["int32"], optional=True, document="""If element scoping is requested on a nodal named selection, if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document="""Scoping""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scoping_provider_by_prop")

#internal name: Rescope_fc
#scripting name: rescope_fc
class _InputsRescopeFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(rescope_fc._spec().inputs, op)
        self.fields_container = Input(rescope_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh_scoping = Input(rescope_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.default_value = Input(rescope_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.default_value)

class _OutputsRescopeFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(rescope_fc._spec().outputs, op)
        self.fields_container = Output(rescope_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class rescope_fc(Operator):
    """Rescope a field on the given scoping. If an id does not exists in the original field, default value (in 2) is used if defined.

      available inputs:
         fields_container (FieldsContainer)
         mesh_scoping (Scoping, list)
         default_value (float, list)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      op = operators.scoping.rescope_fc()

    """
    def __init__(self, fields_container=None, mesh_scoping=None, default_value=None, config=None, server=None):
        super().__init__(name="Rescope_fc", config = config, server = server)
        self.inputs = _InputsRescopeFc(self)
        self.outputs = _OutputsRescopeFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if default_value !=None:
            self.inputs.default_value.connect(default_value)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rescope a field on the given scoping. If an id does not exists in the original field, default value (in 2) is used if defined.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping","vector<int32>"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "default_value", type_names=["double","vector<double>"], optional=False, document="""if a the pin 2 is used, the ids not found in the fields are added with this default value""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "Rescope_fc")

#internal name: GetElementScopingFromMesh
#scripting name: elemental_from_mesh
class _InputsElementalFromMesh(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_from_mesh._spec().inputs, op)
        self.mesh = Input(elemental_from_mesh._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsElementalFromMesh(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_from_mesh._spec().outputs, op)
        self.mesh_scoping = Output(elemental_from_mesh._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh_scoping)

class elemental_from_mesh(Operator):
    """Get the elements ids scoping of a given input mesh.

      available inputs:
         mesh (MeshedRegion)

      available outputs:
         mesh_scoping (Scoping)

      Examples
      --------
      op = operators.scoping.elemental_from_mesh()

    """
    def __init__(self, mesh=None, config=None, server=None):
        super().__init__(name="GetElementScopingFromMesh", config = config, server = server)
        self.inputs = _InputsElementalFromMesh(self)
        self.outputs = _OutputsElementalFromMesh(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Get the elements ids scoping of a given input mesh.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "GetElementScopingFromMesh")

#internal name: Rescope
#scripting name: rescope
class _InputsRescope(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(rescope._spec().inputs, op)
        self.fields = Input(rescope._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields)
        self.mesh_scoping = Input(rescope._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.default_value = Input(rescope._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.default_value)

class _OutputsRescope(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(rescope._spec().outputs, op)
        self.fields_as_fields_container = Output( _modify_output_spec_with_one_type(rescope._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.fields_as_fields_container)
        self.fields_as_field = Output( _modify_output_spec_with_one_type(rescope._spec().output_pin(0), "field"), 0, op) 
        self._outputs.append(self.fields_as_field)

class rescope(Operator):
    """Rescope a field on the given scoping. If an id does not exists in the original field, default value (in 2) is used if defined.

      available inputs:
         fields (FieldsContainer, Field)
         mesh_scoping (Scoping, list)
         default_value (float, list)

      available outputs:
         fields (FieldsContainer ,Field)

      Examples
      --------
      op = operators.scoping.rescope()

    """
    def __init__(self, fields=None, mesh_scoping=None, default_value=None, config=None, server=None):
        super().__init__(name="Rescope", config = config, server = server)
        self.inputs = _InputsRescope(self)
        self.outputs = _OutputsRescope(self)
        if fields !=None:
            self.inputs.fields.connect(fields)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if default_value !=None:
            self.inputs.default_value.connect(default_value)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rescope a field on the given scoping. If an id does not exists in the original field, default value (in 2) is used if defined.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping","vector<int32>"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "default_value", type_names=["double","vector<double>"], optional=False, document="""if a the pin 2 is used, the ids not found in the fields are added with this default value""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "Rescope")

#internal name: scoping_provider_by_ns
#scripting name: on_named_selection
class _InputsOnNamedSelection(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(on_named_selection._spec().inputs, op)
        self.requested_location = Input(on_named_selection._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.requested_location)
        self.named_selection_name = Input(on_named_selection._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.named_selection_name)
        self.int_inclusive = Input(on_named_selection._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.int_inclusive)
        self.streams_container = Input(on_named_selection._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(on_named_selection._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsOnNamedSelection(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(on_named_selection._spec().outputs, op)
        self.mesh_scoping = Output(on_named_selection._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh_scoping)

class on_named_selection(Operator):
    """provides a scoping at a given location based on a given named selection

      available inputs:
         requested_location (str)
         named_selection_name (str)
         int_inclusive (int) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         mesh_scoping (Scoping)

      Examples
      --------
      op = operators.scoping.on_named_selection()

    """
    def __init__(self, requested_location=None, named_selection_name=None, int_inclusive=None, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="scoping_provider_by_ns", config = config, server = server)
        self.inputs = _InputsOnNamedSelection(self)
        self.outputs = _OutputsOnNamedSelection(self)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if named_selection_name !=None:
            self.inputs.named_selection_name.connect(named_selection_name)
        if int_inclusive !=None:
            self.inputs.int_inclusive.connect(int_inclusive)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""provides a scoping at a given location based on a given named selection""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "requested_location", type_names=["string"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "named_selection_name", type_names=["string"], optional=False, document="""the string is expected to be in upper case"""), 
                                 2 : PinSpecification(name = "int_inclusive", type_names=["int32"], optional=True, document="""If element scoping is requested on a nodal named selection, if Inclusive == 1 then add all the elements adjacent to the nodes.If Inclusive == 0, only the elements which have all their nodes in the named selection are included"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scoping_provider_by_ns")

