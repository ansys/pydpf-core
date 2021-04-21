from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from /shared/home1/cbellot/ansys_inc/v212/aisol/dll/linx64/libAns.Dpf.FEMutils.so plugin, from "mapping" category
"""

#internal name: mapping
#scripting name: on_coordinates
class _InputsOnCoordinates(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(on_coordinates._spec().inputs, op)
        self.fields_container = Input(on_coordinates._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.coordinates = Input(on_coordinates._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.coordinates)
        self.create_support = Input(on_coordinates._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.create_support)
        self.mapping_on_scoping = Input(on_coordinates._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.mapping_on_scoping)
        self.mesh = Input(on_coordinates._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsOnCoordinates(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(on_coordinates._spec().outputs, op)
        self.fields_container = Output(on_coordinates._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class on_coordinates(Operator):
    """Evaluates a result on specified coordinates (interpolates results inside elements with shape functions).

      available inputs:
         fields_container (FieldsContainer)
         coordinates (Field, FieldsContainer)
         create_support (bool) (optional)
         mapping_on_scoping (bool) (optional)
         mesh (MeshedRegion, MeshesContainer) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      op = operators.mapping.on_coordinates()

    """
    def __init__(self, fields_container=None, coordinates=None, create_support=None, mapping_on_scoping=None, mesh=None, config=None, server=None):
        super().__init__(name="mapping", config = config, server = server)
        self.inputs = _InputsOnCoordinates(self)
        self.outputs = _OutputsOnCoordinates(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if coordinates !=None:
            self.inputs.coordinates.connect(coordinates)
        if create_support !=None:
            self.inputs.create_support.connect(create_support)
        if mapping_on_scoping !=None:
            self.inputs.mapping_on_scoping.connect(mapping_on_scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates a result on specified coordinates (interpolates results inside elements with shape functions).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "coordinates", type_names=["field","fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "create_support", type_names=["bool"], optional=True, document="""if this pin is set to true, then, a support associated to the fields consisting of points is created"""), 
                                 3 : PinSpecification(name = "mapping_on_scoping", type_names=["bool"], optional=True, document="""if this pin is set to true, then the mapping between the coordinates and the fields is created only on the first field scoping"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""if the first field in input has no mesh in support, then the mesh in this pin is expected (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapping")

#internal name: scoping::on_coordinates
#scripting name: scoping_on_coordinates
class _InputsScopingOnCoordinates(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(scoping_on_coordinates._spec().inputs, op)
        self.coordinates = Input(scoping_on_coordinates._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.coordinates)
        self.mesh = Input(scoping_on_coordinates._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsScopingOnCoordinates(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(scoping_on_coordinates._spec().outputs, op)
        self.scoping = Output(scoping_on_coordinates._spec().output_pin(0), 0, op) 
        self._outputs.append(self.scoping)

class scoping_on_coordinates(Operator):
    """Finds the Elemental scoping of a set of coordinates.

      available inputs:
         coordinates (Field)
         mesh (MeshedRegion)

      available outputs:
         scoping (Scoping)

      Examples
      --------
      op = operators.mapping.scoping_on_coordinates()

    """
    def __init__(self, coordinates=None, mesh=None, config=None, server=None):
        super().__init__(name="scoping::on_coordinates", config = config, server = server)
        self.inputs = _InputsScopingOnCoordinates(self)
        self.outputs = _OutputsScopingOnCoordinates(self)
        if coordinates !=None:
            self.inputs.coordinates.connect(coordinates)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Finds the Elemental scoping of a set of coordinates.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "coordinates", type_names=["field"], optional=False, document=""""""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scoping::on_coordinates")

#internal name: solid_to_skin
#scripting name: solid_to_skin
class _InputsSolidToSkin(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(solid_to_skin._spec().inputs, op)
        self.field = Input(solid_to_skin._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.mesh_scoping = Input(solid_to_skin._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)

class _OutputsSolidToSkin(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(solid_to_skin._spec().outputs, op)
        self.field = Output(solid_to_skin._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class solid_to_skin(Operator):
    """Maps a field defined on solid elements to a field defined on skin elements.

      available inputs:
         field (Field, FieldsContainer)
         mesh_scoping (MeshedRegion) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      op = operators.mapping.solid_to_skin()

    """
    def __init__(self, field=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="solid_to_skin", config = config, server = server)
        self.inputs = _InputsSolidToSkin(self)
        self.outputs = _OutputsSolidToSkin(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Maps a field defined on solid elements to a field defined on skin elements.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["abstract_meshed_region"], optional=True, document="""skin mesh region expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "solid_to_skin")

