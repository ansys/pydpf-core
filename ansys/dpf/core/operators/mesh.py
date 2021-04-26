"""
Mesh Operators
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native.dll plugin, from "mesh" category
"""

#internal name: mesh::node_coordinates
#scripting name: node_coordinates
class _InputsNodeCoordinates(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(node_coordinates._spec().inputs, op)
        self.mesh = Input(node_coordinates._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodeCoordinates(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(node_coordinates._spec().outputs, op)
        self.coordinates_as_field = Output( _modify_output_spec_with_one_type(node_coordinates._spec().output_pin(0), "field"), 0, op) 
        self._outputs.append(self.coordinates_as_field)
        self.coordinates_as_fields_container = Output( _modify_output_spec_with_one_type(node_coordinates._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.coordinates_as_fields_container)

class node_coordinates(Operator):
    """Returns the node coordinates of the mesh(es) in input

      available inputs:
         mesh (MeshedRegion, MeshesContainer)

      available outputs:
         coordinates (Field ,FieldsContainer)

      Examples
      --------
      >>> op = operators.mesh.node_coordinates()

    """
    def __init__(self, mesh=None, config=None, server=None):
        super().__init__(name="mesh::node_coordinates", config = config, server = server)
        self.inputs = _InputsNodeCoordinates(self)
        self.outputs = _OutputsNodeCoordinates(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Returns the node coordinates of the mesh(es) in input""",
                             map_input_pin_spec={
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "coordinates", type_names=["field","fields_container"], optional=False, document="""if the input is a meshed region, a field of coordinates is the output, else if the input is a  meshes container, a fields container (one field by mesh) is the output""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh::node_coordinates")

#internal name: GetSupportFromField
#scripting name: from_field
class _InputsFromField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(from_field._spec().inputs, op)
        self.field = Input(from_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsFromField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(from_field._spec().outputs, op)
        self.mesh = Output(from_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh)

class from_field(Operator):
    """Returns the meshed region contained in the support of the mesh.

      available inputs:
         field (Field)

      available outputs:
         mesh (MeshedRegion)

      Examples
      --------
      >>> op = operators.mesh.from_field()

    """
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="GetSupportFromField", config = config, server = server)
        self.inputs = _InputsFromField(self)
        self.outputs = _OutputsFromField(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Returns the meshed region contained in the support of the mesh.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "GetSupportFromField")

#internal name: MeshProvider
#scripting name: mesh_provider
class _InputsMeshProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(mesh_provider._spec().inputs, op)
        self.streams_container = Input(mesh_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(mesh_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.read_cyclic = Input(mesh_provider._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self.read_cyclic)

class _OutputsMeshProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(mesh_provider._spec().outputs, op)
        self.mesh = Output(mesh_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh)

class mesh_provider(Operator):
    """Read a mesh from result files and cure degenerated elements

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         read_cyclic (int) (optional)

      available outputs:
         mesh (MeshedRegion)

      Examples
      --------
      >>> op = operators.mesh.mesh_provider()

    """
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="MeshProvider", config = config, server = server)
        self.inputs = _InputsMeshProvider(self)
        self.outputs = _OutputsMeshProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read a mesh from result files and cure degenerated elements""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 1 cyclic symmetry is ignored, if 2 cyclic expansion is done (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "MeshProvider")

"""
Mesh Operators
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils.dll plugin, from "mesh" category
"""

#internal name: mesh::points_from_coordinates
#scripting name: points_from_coordinates
class _InputsPointsFromCoordinates(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(points_from_coordinates._spec().inputs, op)
        self.nodes_to_keep = Input(points_from_coordinates._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.nodes_to_keep)
        self.mesh = Input(points_from_coordinates._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsPointsFromCoordinates(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(points_from_coordinates._spec().outputs, op)
        self.meshed_region = Output(points_from_coordinates._spec().output_pin(0), 0, op) 
        self._outputs.append(self.meshed_region)

class points_from_coordinates(Operator):
    """Extract a mesh made of points elements. This mesh is made from input meshes coordinates on the input scopings.

      available inputs:
         nodes_to_keep (Scoping, ScopingsContainer)
         mesh (MeshedRegion, MeshesContainer)

      available outputs:
         meshed_region (MeshedRegion)

      Examples
      --------
      >>> op = operators.mesh.points_from_coordinates()

    """
    def __init__(self, nodes_to_keep=None, mesh=None, config=None, server=None):
        super().__init__(name="mesh::points_from_coordinates", config = config, server = server)
        self.inputs = _InputsPointsFromCoordinates(self)
        self.outputs = _OutputsPointsFromCoordinates(self)
        if nodes_to_keep !=None:
            self.inputs.nodes_to_keep.connect(nodes_to_keep)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extract a mesh made of points elements. This mesh is made from input meshes coordinates on the input scopings.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "nodes_to_keep", type_names=["scoping","scopings_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh::points_from_coordinates")

#internal name: split_mesh
#scripting name: split_mesh
class _InputsSplitMesh(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(split_mesh._spec().inputs, op)
        self.mesh_scoping = Input(split_mesh._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.mesh = Input(split_mesh._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.property = Input(split_mesh._spec().input_pin(13), 13, op, -1) 
        self._inputs.append(self.property)

class _OutputsSplitMesh(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(split_mesh._spec().outputs, op)
        self.mesh_controller = Output(split_mesh._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh_controller)

class split_mesh(Operator):
    """Split the input mesh into several meshes based on a given property (material property be default)

      available inputs:
         mesh_scoping (Scoping) (optional)
         mesh (MeshedRegion)
         property (str)

      available outputs:
         mesh_controller (MeshesContainer)

      Examples
      --------
      >>> op = operators.mesh.split_mesh()

    """
    def __init__(self, mesh_scoping=None, mesh=None, property=None, config=None, server=None):
        super().__init__(name="split_mesh", config = config, server = server)
        self.inputs = _InputsSplitMesh(self)
        self.outputs = _OutputsSplitMesh(self)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if property !=None:
            self.inputs.property.connect(property)

    @staticmethod
    def _spec():
        spec = Specification(description="""Split the input mesh into several meshes based on a given property (material property be default)""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""Scoping"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 13 : PinSpecification(name = "property", type_names=["string"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_controller", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "split_mesh")

#internal name: mesh::by_scoping
#scripting name: from_scoping
class _InputsFromScoping(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(from_scoping._spec().inputs, op)
        self.scoping = Input(from_scoping._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.scoping)
        self.inclusive = Input(from_scoping._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.inclusive)
        self.mesh = Input(from_scoping._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsFromScoping(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(from_scoping._spec().outputs, op)
        self.mesh = Output(from_scoping._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh)

class from_scoping(Operator):
    """Extracts a meshed region from an other meshed region base on a scoping

      available inputs:
         scoping (Scoping)
         inclusive (int) (optional)
         mesh (MeshedRegion)

      available outputs:
         mesh (MeshedRegion)

      Examples
      --------
      >>> op = operators.mesh.from_scoping()

    """
    def __init__(self, scoping=None, inclusive=None, mesh=None, config=None, server=None):
        super().__init__(name="mesh::by_scoping", config = config, server = server)
        self.inputs = _InputsFromScoping(self)
        self.outputs = _OutputsFromScoping(self)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if inclusive !=None:
            self.inputs.inclusive.connect(inclusive)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts a meshed region from an other meshed region base on a scoping""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "scoping", type_names=["scoping"], optional=False, document="""if nodal scoping, then the scoping is transposed respecting the inclusive pin"""), 
                                 2 : PinSpecification(name = "inclusive", type_names=["int32"], optional=True, document="""if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh::by_scoping")

#internal name: split_fields
#scripting name: split_fields
class _InputsSplitFields(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(split_fields._spec().inputs, op)
        self.field_or_fields_container = Input(split_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field_or_fields_container)
        self.mesh_controller = Input(split_fields._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_controller)

class _OutputsSplitFields(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(split_fields._spec().outputs, op)
        self.fields_container = Output(split_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class split_fields(Operator):
    """Split the input field or fields container based on the input mesh regions 

      available inputs:
         field_or_fields_container (Field, FieldsContainer)
         mesh_controller (MeshesContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.mesh.split_fields()

    """
    def __init__(self, field_or_fields_container=None, mesh_controller=None, config=None, server=None):
        super().__init__(name="split_fields", config = config, server = server)
        self.inputs = _InputsSplitFields(self)
        self.outputs = _OutputsSplitFields(self)
        if field_or_fields_container !=None:
            self.inputs.field_or_fields_container.connect(field_or_fields_container)
        if mesh_controller !=None:
            self.inputs.mesh_controller.connect(mesh_controller)

    @staticmethod
    def _spec():
        spec = Specification(description="""Split the input field or fields container based on the input mesh regions """,
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field_or_fields_container", type_names=["field","fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh_controller", type_names=["meshes_container"], optional=False, document="""body meshes in the mesh controller cannot be mixed shell/solid""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "split_fields")

"""
Mesh Operators
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore.dll plugin, from "mesh" category
"""

#internal name: meshed_skin_sector_triangle
#scripting name: tri_mesh_skin
class _InputsTriMeshSkin(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(tri_mesh_skin._spec().inputs, op)
        self.mesh = Input(tri_mesh_skin._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsTriMeshSkin(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(tri_mesh_skin._spec().outputs, op)
        self.mesh = Output(tri_mesh_skin._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh)
        self.nodes_mesh_scoping = Output(tri_mesh_skin._spec().output_pin(1), 1, op) 
        self._outputs.append(self.nodes_mesh_scoping)

class tri_mesh_skin(Operator):
    """Extracts a skin of the mesh in triangles (2D elements) in a new meshed region

      available inputs:
         mesh (MeshedRegion)

      available outputs:
         mesh (MeshedRegion)
         nodes_mesh_scoping (Scoping)

      Examples
      --------
      >>> op = operators.mesh.tri_mesh_skin()

    """
    def __init__(self, mesh=None, config=None, server=None):
        super().__init__(name="meshed_skin_sector_triangle", config = config, server = server)
        self.inputs = _InputsTriMeshSkin(self)
        self.outputs = _OutputsTriMeshSkin(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts a skin of the mesh in triangles (2D elements) in a new meshed region""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "nodes_mesh_scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "meshed_skin_sector_triangle")

#internal name: mesh_cut
#scripting name: mesh_cut
class _InputsMeshCut(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(mesh_cut._spec().inputs, op)
        self.field = Input(mesh_cut._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.iso_value = Input(mesh_cut._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.iso_value)
        self.closed_surface = Input(mesh_cut._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.closed_surface)
        self.slice_surfaces = Input(mesh_cut._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.slice_surfaces)

class _OutputsMeshCut(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(mesh_cut._spec().outputs, op)
        self.mesh = Output(mesh_cut._spec().output_pin(2), 2, op) 
        self._outputs.append(self.mesh)

class mesh_cut(Operator):
    """Extracts a skin of the mesh in triangles (2D elements) in a new meshed region

      available inputs:
         field (Field)
         iso_value (float)
         closed_surface (float)
         slice_surfaces (bool)

      available outputs:
         mesh (MeshedRegion)

      Examples
      --------
      >>> op = operators.mesh.mesh_cut()

    """
    def __init__(self, field=None, iso_value=None, closed_surface=None, slice_surfaces=None, config=None, server=None):
        super().__init__(name="mesh_cut", config = config, server = server)
        self.inputs = _InputsMeshCut(self)
        self.outputs = _OutputsMeshCut(self)
        if field !=None:
            self.inputs.field.connect(field)
        if iso_value !=None:
            self.inputs.iso_value.connect(iso_value)
        if closed_surface !=None:
            self.inputs.closed_surface.connect(closed_surface)
        if slice_surfaces !=None:
            self.inputs.slice_surfaces.connect(slice_surfaces)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts a skin of the mesh in triangles (2D elements) in a new meshed region""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "iso_value", type_names=["double"], optional=False, document="""iso value"""), 
                                 3 : PinSpecification(name = "closed_surface", type_names=["double"], optional=False, document="""1: closed surface, 0:iso surface"""), 
                                 4 : PinSpecification(name = "slice_surfaces", type_names=["bool"], optional=False, document="""true: slicing will also take into account shell and 2D elements, false: sliicing will ignore shell and 2D elements. default is true""")},
                             map_output_pin_spec={
                                 2 : PinSpecification(name = "mesh", type_names=["meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh_cut")

#internal name: meshed_external_layer_sector
#scripting name: external_layer
class _InputsExternalLayer(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(external_layer._spec().inputs, op)
        self.mesh = Input(external_layer._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsExternalLayer(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(external_layer._spec().outputs, op)
        self.mesh = Output(external_layer._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh)
        self.nodes_mesh_scoping = Output(external_layer._spec().output_pin(1), 1, op) 
        self._outputs.append(self.nodes_mesh_scoping)
        self.elements_mesh_scoping = Output(external_layer._spec().output_pin(2), 2, op) 
        self._outputs.append(self.elements_mesh_scoping)

class external_layer(Operator):
    """Extracts the external layer (thick skin) of the mesh (3D elements) in a new meshed region

      available inputs:
         mesh (MeshedRegion)

      available outputs:
         mesh (MeshedRegion)
         nodes_mesh_scoping (Scoping)
         elements_mesh_scoping (Scoping)

      Examples
      --------
      >>> op = operators.mesh.external_layer()

    """
    def __init__(self, mesh=None, config=None, server=None):
        super().__init__(name="meshed_external_layer_sector", config = config, server = server)
        self.inputs = _InputsExternalLayer(self)
        self.outputs = _OutputsExternalLayer(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts the external layer (thick skin) of the mesh (3D elements) in a new meshed region""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "nodes_mesh_scoping", type_names=["scoping"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "elements_mesh_scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "meshed_external_layer_sector")

#internal name: meshed_skin_sector
#scripting name: skin
class _InputsSkin(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(skin._spec().inputs, op)
        self.mesh = Input(skin._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)
        self.mesh_scoping = Input(skin._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)

class _OutputsSkin(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(skin._spec().outputs, op)
        self.mesh = Output(skin._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh)
        self.nodes_mesh_scoping = Output(skin._spec().output_pin(1), 1, op) 
        self._outputs.append(self.nodes_mesh_scoping)
        pass 

class skin(Operator):
    """Extracts a skin of the mesh (2D elements) in a new meshed region. Material id of initial elements are propagated to their facets.

      available inputs:
         mesh (MeshedRegion)
         mesh_scoping (Scoping) (optional)

      available outputs:
         mesh (MeshedRegion)
         nodes_mesh_scoping (Scoping)
         map_new_elements_to_old ()
         property_field_new_elements_to_old (PropertyField)

      Examples
      --------
      >>> op = operators.mesh.skin()

    """
    def __init__(self, mesh=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="meshed_skin_sector", config = config, server = server)
        self.inputs = _InputsSkin(self)
        self.outputs = _OutputsSkin(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts a skin of the mesh (2D elements) in a new meshed region. Material id of initial elements are propagated to their facets.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""skin meshed region with facets and facets_to_ele property fields"""), 
                                 1 : PinSpecification(name = "nodes_mesh_scoping", type_names=["scoping"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "map_new_elements_to_old", type_names=[], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "property_field_new_elements_to_old", type_names=["property_field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "meshed_skin_sector")

#internal name: stl_export
#scripting name: stl_export
class _InputsStlExport(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(stl_export._spec().inputs, op)
        self.mesh = Input(stl_export._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)
        self.file_path = Input(stl_export._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.file_path)

class _OutputsStlExport(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(stl_export._spec().outputs, op)
        self.data_sources = Output(stl_export._spec().output_pin(0), 0, op) 
        self._outputs.append(self.data_sources)

class stl_export(Operator):
    """export a mesh into a stl file.

      available inputs:
         mesh (MeshedRegion)
         file_path (str)

      available outputs:
         data_sources (DataSources)

      Examples
      --------
      >>> op = operators.mesh.stl_export()

    """
    def __init__(self, mesh=None, file_path=None, config=None, server=None):
        super().__init__(name="stl_export", config = config, server = server)
        self.inputs = _InputsStlExport(self)
        self.outputs = _OutputsStlExport(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if file_path !=None:
            self.inputs.file_path.connect(file_path)

    @staticmethod
    def _spec():
        spec = Specification(description="""export a mesh into a stl file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "stl_export")

