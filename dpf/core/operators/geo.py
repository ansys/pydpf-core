"""
Geo Operators
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "geo" category
"""

#internal name: normals_provider_nl
#scripting name: normals_provider_nl
class _InputsNormalsProviderNl(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(normals_provider_nl._spec().inputs, op)
        self.mesh = Input(normals_provider_nl._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)
        self.mesh_scoping = Input(normals_provider_nl._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)

class _OutputsNormalsProviderNl(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(normals_provider_nl._spec().outputs, op)
        self.field = Output(normals_provider_nl._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class normals_provider_nl(Operator):
    """Compute the normals on nodes/elements based on integration points(more accurate for non-linear elements), on a skin mesh

      available inputs:
         mesh (MeshedRegion)
         mesh_scoping (Scoping)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.normals_provider_nl()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, mesh=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="normals_provider_nl", config = config, server = server)
        self.inputs = _InputsNormalsProviderNl(self)
        self.outputs = _OutputsNormalsProviderNl(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the normals on nodes/elements based on integration points(more accurate for non-linear elements), on a skin mesh""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""skin or shell mesh region"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "normals_provider_nl")

#internal name: transform_cylindrical_cs_fc
#scripting name: rotate_in_cylindrical_cs_fc
class _InputsRotateInCylindricalCsFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(rotate_in_cylindrical_cs_fc._spec().inputs, op)
        self.field = Input(rotate_in_cylindrical_cs_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.coordinate_system = Input(rotate_in_cylindrical_cs_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.coordinate_system)

class _OutputsRotateInCylindricalCsFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(rotate_in_cylindrical_cs_fc._spec().outputs, op)
        self.fields_container = Output(rotate_in_cylindrical_cs_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class rotate_in_cylindrical_cs_fc(Operator):
    """Rotate all the fields of a fields container (not defined with a cynlindrical coordinate system) to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.

      available inputs:
         field (Field, FieldsContainer)
         coordinate_system (Field) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.rotate_in_cylindrical_cs_fc()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_coordinate_system = dpf.Field()
      >>> op.inputs.coordinate_system.connect(my_coordinate_system)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field=None, coordinate_system=None, config=None, server=None):
        super().__init__(name="transform_cylindrical_cs_fc", config = config, server = server)
        self.inputs = _InputsRotateInCylindricalCsFc(self)
        self.outputs = _OutputsRotateInCylindricalCsFc(self)
        if field !=None:
            self.inputs.field.connect(field)
        if coordinate_system !=None:
            self.inputs.coordinate_system.connect(coordinate_system)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rotate all the fields of a fields container (not defined with a cynlindrical coordinate system) to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "coordinate_system", type_names=["field"], optional=True, document="""3-3 rotation matrix and origin coordinates must be set here to define a coordinate system.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "transform_cylindrical_cs_fc")

#internal name: transform_cylindricalCS
#scripting name: rotate_in_cylindrical_cs
class _InputsRotateInCylindricalCs(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(rotate_in_cylindrical_cs._spec().inputs, op)
        self.field = Input(rotate_in_cylindrical_cs._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.coordinate_system = Input(rotate_in_cylindrical_cs._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.coordinate_system)

class _OutputsRotateInCylindricalCs(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(rotate_in_cylindrical_cs._spec().outputs, op)
        self.fields_container = Output(rotate_in_cylindrical_cs._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class rotate_in_cylindrical_cs(Operator):
    """Rotate a field to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.

      available inputs:
         field (Field, FieldsContainer)
         coordinate_system (Field) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.rotate_in_cylindrical_cs()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_coordinate_system = dpf.Field()
      >>> op.inputs.coordinate_system.connect(my_coordinate_system)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field=None, coordinate_system=None, config=None, server=None):
        super().__init__(name="transform_cylindricalCS", config = config, server = server)
        self.inputs = _InputsRotateInCylindricalCs(self)
        self.outputs = _OutputsRotateInCylindricalCs(self)
        if field !=None:
            self.inputs.field.connect(field)
        if coordinate_system !=None:
            self.inputs.coordinate_system.connect(coordinate_system)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rotate a field to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "coordinate_system", type_names=["field"], optional=True, document="""3-3 rotation matrix and origin coordinates must be set here to define a coordinate system.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "transform_cylindricalCS")

#internal name: rotate
#scripting name: rotate
class _InputsRotate(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(rotate._spec().inputs, op)
        self.field = Input(rotate._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.field_rotation_matrix = Input(rotate._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.field_rotation_matrix)

class _OutputsRotate(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(rotate._spec().outputs, op)
        self.field = Output(rotate._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class rotate(Operator):
    """Apply a transformation (rotation) matrix on field.

      available inputs:
         field (Field, FieldsContainer)
         field_rotation_matrix (Field)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.rotate()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_field_rotation_matrix = dpf.Field()
      >>> op.inputs.field_rotation_matrix.connect(my_field_rotation_matrix)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, field_rotation_matrix=None, config=None, server=None):
        super().__init__(name="rotate", config = config, server = server)
        self.inputs = _InputsRotate(self)
        self.outputs = _OutputsRotate(self)
        if field !=None:
            self.inputs.field.connect(field)
        if field_rotation_matrix !=None:
            self.inputs.field_rotation_matrix.connect(field_rotation_matrix)

    @staticmethod
    def _spec():
        spec = Specification(description="""Apply a transformation (rotation) matrix on field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "field_rotation_matrix", type_names=["field"], optional=False, document="""3-3 rotation matrix""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "rotate")

#internal name: rotate_fc
#scripting name: rotate_fc
class _InputsRotateFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(rotate_fc._spec().inputs, op)
        self.fields_container = Input(rotate_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.coordinate_system = Input(rotate_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.coordinate_system)

class _OutputsRotateFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(rotate_fc._spec().outputs, op)
        self.fields_container = Output(rotate_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class rotate_fc(Operator):
    """Apply a transformation (rotation) matrix on all the fields of a fields container.

      available inputs:
         fields_container (FieldsContainer)
         coordinate_system (Field)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.rotate_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_coordinate_system = dpf.Field()
      >>> op.inputs.coordinate_system.connect(my_coordinate_system)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, coordinate_system=None, config=None, server=None):
        super().__init__(name="rotate_fc", config = config, server = server)
        self.inputs = _InputsRotateFc(self)
        self.outputs = _OutputsRotateFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if coordinate_system !=None:
            self.inputs.coordinate_system.connect(coordinate_system)

    @staticmethod
    def _spec():
        spec = Specification(description="""Apply a transformation (rotation) matrix on all the fields of a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "coordinate_system", type_names=["field"], optional=False, document="""3-3 rotation matrix""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "rotate_fc")

#internal name: polar_coordinates
#scripting name: to_polar_coordinates
class _InputsToPolarCoordinates(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(to_polar_coordinates._spec().inputs, op)
        self.field = Input(to_polar_coordinates._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.coordinate_system = Input(to_polar_coordinates._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.coordinate_system)

class _OutputsToPolarCoordinates(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(to_polar_coordinates._spec().outputs, op)
        self.fields_container = Output(to_polar_coordinates._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class to_polar_coordinates(Operator):
    """Find r, theta (rad), z coordinates of a coordinates (nodal) field in cartesian coordinates system with respoect to the input coordinate system defining the rotation axis and the origin.

      available inputs:
         field (Field, FieldsContainer)
         coordinate_system (Field) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.to_polar_coordinates()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_coordinate_system = dpf.Field()
      >>> op.inputs.coordinate_system.connect(my_coordinate_system)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field=None, coordinate_system=None, config=None, server=None):
        super().__init__(name="polar_coordinates", config = config, server = server)
        self.inputs = _InputsToPolarCoordinates(self)
        self.outputs = _OutputsToPolarCoordinates(self)
        if field !=None:
            self.inputs.field.connect(field)
        if coordinate_system !=None:
            self.inputs.coordinate_system.connect(coordinate_system)

    @staticmethod
    def _spec():
        spec = Specification(description="""Find r, theta (rad), z coordinates of a coordinates (nodal) field in cartesian coordinates system with respoect to the input coordinate system defining the rotation axis and the origin.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "coordinate_system", type_names=["field"], optional=True, document="""3-3 rotation matrix and origin coordinates must be set here to define a coordinate system. By default, the rotation axis is the z axis and the origin is [0,0,0]""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "polar_coordinates")

#internal name: volumes_provider
#scripting name: elements_volumes_over_time
class _InputsElementsVolumesOverTime(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elements_volumes_over_time._spec().inputs, op)
        self.scoping = Input(elements_volumes_over_time._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.scoping)
        self.displacement = Input(elements_volumes_over_time._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.displacement)
        self.mesh = Input(elements_volumes_over_time._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsElementsVolumesOverTime(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elements_volumes_over_time._spec().outputs, op)
        self.fields_container = Output(elements_volumes_over_time._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elements_volumes_over_time(Operator):
    """Calculation of the volume of each element over time of a mesh for each specified time step.

      available inputs:
         scoping (Scoping) (optional)
         displacement (FieldsContainer) (optional)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.elements_volumes_over_time()

      >>> # Make input connections
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_displacement = dpf.FieldsContainer()
      >>> op.inputs.displacement.connect(my_displacement)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, scoping=None, displacement=None, mesh=None, config=None, server=None):
        super().__init__(name="volumes_provider", config = config, server = server)
        self.inputs = _InputsElementsVolumesOverTime(self)
        self.outputs = _OutputsElementsVolumesOverTime(self)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if displacement !=None:
            self.inputs.displacement.connect(displacement)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Calculation of the volume of each element over time of a mesh for each specified time step.""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "displacement", type_names=["fields_container"], optional=True, document="""Displacement field's container. Must contain the mesh if mesh not specified in input."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""Mesh must be defined if the displacement field's container does not contain it, or if there is no displacement.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "volumes_provider")

#internal name: surfaces_provider
#scripting name: elements_facets_surfaces_over_time
class _InputsElementsFacetsSurfacesOverTime(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elements_facets_surfaces_over_time._spec().inputs, op)
        self.scoping = Input(elements_facets_surfaces_over_time._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.scoping)
        self.displacement = Input(elements_facets_surfaces_over_time._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.displacement)
        self.mesh = Input(elements_facets_surfaces_over_time._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsElementsFacetsSurfacesOverTime(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elements_facets_surfaces_over_time._spec().outputs, op)
        self.fields_container = Output(elements_facets_surfaces_over_time._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)
        self.mesh = Output(elements_facets_surfaces_over_time._spec().output_pin(1), 1, op) 
        self._outputs.append(self.mesh)

class elements_facets_surfaces_over_time(Operator):
    """Calculation of the surface of each element's facet over time of a mesh for each specified time step. Moreover, it gives as output a new mesh made with only surface elements.

      available inputs:
         scoping (Scoping) (optional)
         displacement (FieldsContainer) (optional)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.elements_facets_surfaces_over_time()

      >>> # Make input connections
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_displacement = dpf.FieldsContainer()
      >>> op.inputs.displacement.connect(my_displacement)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()
      >>> result_mesh = op.outputs.mesh()"""
    def __init__(self, scoping=None, displacement=None, mesh=None, config=None, server=None):
        super().__init__(name="surfaces_provider", config = config, server = server)
        self.inputs = _InputsElementsFacetsSurfacesOverTime(self)
        self.outputs = _OutputsElementsFacetsSurfacesOverTime(self)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if displacement !=None:
            self.inputs.displacement.connect(displacement)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Calculation of the surface of each element's facet over time of a mesh for each specified time step. Moreover, it gives as output a new mesh made with only surface elements.""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "displacement", type_names=["fields_container"], optional=True, document="""Displacement field's container."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""Mesh must be defined if the displacement field's container does not contain it, or if there is no displacement.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""Surfaces field."""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""Mesh made of surface elements only.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "surfaces_provider")

#internal name: element::volume
#scripting name: elements_volume
class _InputsElementsVolume(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elements_volume._spec().inputs, op)
        self.mesh = Input(elements_volume._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsElementsVolume(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elements_volume._spec().outputs, op)
        self.field = Output(elements_volume._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class elements_volume(Operator):
    """Compute the volume of each element of a mesh, using default shape functions.

      available inputs:
         mesh (MeshedRegion)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.elements_volume()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, mesh=None, config=None, server=None):
        super().__init__(name="element::volume", config = config, server = server)
        self.inputs = _InputsElementsVolume(self)
        self.outputs = _OutputsElementsVolume(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the volume of each element of a mesh, using default shape functions.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "element::volume")

#internal name: element::nodal_contribution
#scripting name: element_nodal_contribution
class _InputsElementNodalContribution(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(element_nodal_contribution._spec().inputs, op)
        self.mesh = Input(element_nodal_contribution._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)
        self.scoping = Input(element_nodal_contribution._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.scoping)
        self.volume_fraction = Input(element_nodal_contribution._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.volume_fraction)

class _OutputsElementNodalContribution(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(element_nodal_contribution._spec().outputs, op)
        self.field = Output(element_nodal_contribution._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class element_nodal_contribution(Operator):
    """Compute the fraction of volume attributed to each node of each element.

      available inputs:
         mesh (MeshedRegion)
         scoping (Scoping) (optional)
         volume_fraction (bool) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.element_nodal_contribution()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_volume_fraction = bool()
      >>> op.inputs.volume_fraction.connect(my_volume_fraction)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, mesh=None, scoping=None, volume_fraction=None, config=None, server=None):
        super().__init__(name="element::nodal_contribution", config = config, server = server)
        self.inputs = _InputsElementNodalContribution(self)
        self.outputs = _OutputsElementNodalContribution(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if volume_fraction !=None:
            self.inputs.volume_fraction.connect(volume_fraction)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the fraction of volume attributed to each node of each element.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""Integrate the input field over a specific scoping."""), 
                                 2 : PinSpecification(name = "volume_fraction", type_names=["bool"], optional=True, document="""if true, returns influence volume, if false, return influence volume fraction (i.e. integrated value of shape function for each node).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "element::nodal_contribution")

#internal name: topology::center_of_gravity
#scripting name: center_of_gravity
class _InputsCenterOfGravity(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(center_of_gravity._spec().inputs, op)
        self.mesh = Input(center_of_gravity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)
        self.mesh_scoping = Input(center_of_gravity._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.field = Input(center_of_gravity._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.field)

class _OutputsCenterOfGravity(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(center_of_gravity._spec().outputs, op)
        self.field = Output(center_of_gravity._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)
        self.mesh = Output(center_of_gravity._spec().output_pin(1), 1, op) 
        self._outputs.append(self.mesh)

class center_of_gravity(Operator):
    """Compute the center of gravity of a set of elements

      available inputs:
         mesh (MeshedRegion) (optional)
         mesh_scoping (Scoping) (optional)
         field (Field) (optional)

      available outputs:
         field (Field)
         mesh (MeshedRegion)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.center_of_gravity()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()
      >>> result_mesh = op.outputs.mesh()"""
    def __init__(self, mesh=None, mesh_scoping=None, field=None, config=None, server=None):
        super().__init__(name="topology::center_of_gravity", config = config, server = server)
        self.inputs = _InputsCenterOfGravity(self)
        self.outputs = _OutputsCenterOfGravity(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the center of gravity of a set of elements""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""Mesh scoping, if not set, all the elements of the mesh are considered."""), 
                                 2 : PinSpecification(name = "field", type_names=["field"], optional=True, document="""Elemental or nodal ponderation used in computation.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""Center of gravity as a mesh""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "topology::center_of_gravity")

#internal name: element::integrate
#scripting name: integrate_over_elements
class _InputsIntegrateOverElements(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(integrate_over_elements._spec().inputs, op)
        self.field = Input(integrate_over_elements._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.scoping = Input(integrate_over_elements._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.scoping)
        self.mesh = Input(integrate_over_elements._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsIntegrateOverElements(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(integrate_over_elements._spec().outputs, op)
        self.field = Output(integrate_over_elements._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class integrate_over_elements(Operator):
    """Integration of an input field over mesh.

      available inputs:
         field (Field)
         scoping (Scoping) (optional)
         mesh (MeshedRegion) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.integrate_over_elements()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, scoping=None, mesh=None, config=None, server=None):
        super().__init__(name="element::integrate", config = config, server = server)
        self.inputs = _InputsIntegrateOverElements(self)
        self.outputs = _OutputsIntegrateOverElements(self)
        if field !=None:
            self.inputs.field.connect(field)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Integration of an input field over mesh.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""Integrate the input field over a specific scoping."""), 
                                 2 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""Mesh to integrate on, if not provided the one from input field is provided.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "element::integrate")

#internal name: topology::mass
#scripting name: mass
class _InputsMass(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(mass._spec().inputs, op)
        self.mesh = Input(mass._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)
        self.mesh_scoping = Input(mass._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.field = Input(mass._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.field)

class _OutputsMass(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(mass._spec().outputs, op)
        self.field = Output(mass._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class mass(Operator):
    """Compute the mass of a set of elements.

      available inputs:
         mesh (MeshedRegion) (optional)
         mesh_scoping (Scoping) (optional)
         field (Field) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.mass()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, mesh=None, mesh_scoping=None, field=None, config=None, server=None):
        super().__init__(name="topology::mass", config = config, server = server)
        self.inputs = _InputsMass(self)
        self.outputs = _OutputsMass(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the mass of a set of elements.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""Mesh scoping, if not set, all the elements of the mesh are considered."""), 
                                 2 : PinSpecification(name = "field", type_names=["field"], optional=True, document="""Elemental or nodal ponderation used in computation.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "topology::mass")

#internal name: topology::moment_of_inertia
#scripting name: moment_of_inertia
class _InputsMomentOfInertia(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(moment_of_inertia._spec().inputs, op)
        self.mesh = Input(moment_of_inertia._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)
        self.mesh_scoping = Input(moment_of_inertia._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.field = Input(moment_of_inertia._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.field)
        self.boolean = Input(moment_of_inertia._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.boolean)

class _OutputsMomentOfInertia(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(moment_of_inertia._spec().outputs, op)
        self.field = Output(moment_of_inertia._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class moment_of_inertia(Operator):
    """Compute the inertia tensor of a set of elements.

      available inputs:
         mesh (MeshedRegion) (optional)
         mesh_scoping (Scoping) (optional)
         field (Field) (optional)
         boolean (bool) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.moment_of_inertia()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_boolean = bool()
      >>> op.inputs.boolean.connect(my_boolean)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, mesh=None, mesh_scoping=None, field=None, boolean=None, config=None, server=None):
        super().__init__(name="topology::moment_of_inertia", config = config, server = server)
        self.inputs = _InputsMomentOfInertia(self)
        self.outputs = _OutputsMomentOfInertia(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if field !=None:
            self.inputs.field.connect(field)
        if boolean !=None:
            self.inputs.boolean.connect(boolean)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the inertia tensor of a set of elements.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""Mesh scoping, if not set, all the elements of the mesh are considered."""), 
                                 2 : PinSpecification(name = "field", type_names=["field"], optional=True, document="""Elemental or nodal ponderation used in computation."""), 
                                 3 : PinSpecification(name = "boolean", type_names=["bool"], optional=True, document="""default true, compute inertia tensor at center of gravity.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "topology::moment_of_inertia")

"""
Geo Operators
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "geo" category
"""

#internal name: normals_provider
#scripting name: normals
class _InputsNormals(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(normals._spec().inputs, op)
        self.mesh = Input(normals._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)
        self.mesh_scoping = Input(normals._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.field = Input(normals._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.field)

class _OutputsNormals(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(normals._spec().outputs, op)
        self.field = Output(normals._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class normals(Operator):
    """compute the normals at the given nodes or element scoping based on the given mesh (first version, the element normal is only handled on the shell elements)

      available inputs:
         mesh (MeshedRegion) (optional)
         mesh_scoping (Scoping) (optional)
         field (Field) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.normals()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, mesh=None, mesh_scoping=None, field=None, config=None, server=None):
        super().__init__(name="normals_provider", config = config, server = server)
        self.inputs = _InputsNormals(self)
        self.outputs = _OutputsNormals(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""compute the normals at the given nodes or element scoping based on the given mesh (first version, the element normal is only handled on the shell elements)""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "field", type_names=["field"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "normals_provider")

