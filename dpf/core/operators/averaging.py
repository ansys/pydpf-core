"""
Averaging Operators
===================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

#internal name: nodal_fraction_fc
#scripting name: nodal_fraction_fc
class _InputsNodalFractionFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_fraction_fc._spec().inputs, op)
        self.fields_container = Input(nodal_fraction_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh = Input(nodal_fraction_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.scoping = Input(nodal_fraction_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.scoping)
        self.denominator = Input(nodal_fraction_fc._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self.denominator)

class _OutputsNodalFractionFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_fraction_fc._spec().outputs, op)
        self.fields_container = Output(nodal_fraction_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_fraction_fc(Operator):
    """Transform ElementalNodal fields into Nodal fields. Each nodal value is the fraction between the nodal difference and the nodal average. Result is computed on a given node scoping.

      available inputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion) (optional)
         scoping (Scoping) (optional)
         denominator (FieldsContainer) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.nodal_fraction_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_denominator = dpf.FieldsContainer()
      >>> op.inputs.denominator.connect(my_denominator)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, scoping=None, denominator=None, config=None, server=None):
        super().__init__(name="nodal_fraction_fc", config = config, server = server)
        self.inputs = _InputsNodalFractionFc(self)
        self.outputs = _OutputsNodalFractionFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if denominator !=None:
            self.inputs.denominator.connect(denominator)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal fields into Nodal fields. Each nodal value is the fraction between the nodal difference and the nodal average. Result is computed on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container"""), 
                                 6 : PinSpecification(name = "denominator", type_names=["fields_container"], optional=True, document="""if a fields container is set in this pin, it is used as the denominator of the fraction instead of elemental_nodal_To_nodal_fc""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "nodal_fraction_fc")

#internal name: ElementalNodal_To_NodalElemental_fc
#scripting name: elemental_nodal_to_nodal_elemental_fc
class _InputsElementalNodalToNodalElementalFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_elemental_fc._spec().inputs, op)
        self.fields_container = Input(elemental_nodal_to_nodal_elemental_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh_scoping = Input(elemental_nodal_to_nodal_elemental_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)

class _OutputsElementalNodalToNodalElementalFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_elemental_fc._spec().outputs, op)
        self.fields_container = Output(elemental_nodal_to_nodal_elemental_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elemental_nodal_to_nodal_elemental_fc(Operator):
    """Transform ElementalNodal fields to NodalElemental fields, compute result on a given node scoping.

      available inputs:
         fields_container (FieldsContainer)
         mesh_scoping (Scoping) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="ElementalNodal_To_NodalElemental_fc", config = config, server = server)
        self.inputs = _InputsElementalNodalToNodalElementalFc(self)
        self.outputs = _OutputsElementalNodalToNodalElementalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal fields to NodalElemental fields, compute result on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ElementalNodal_To_NodalElemental_fc")

#internal name: elemental_difference
#scripting name: elemental_difference
class _InputsElementalDifference(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_difference._spec().inputs, op)
        self.field = Input(elemental_difference._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.mesh_scoping = Input(elemental_difference._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.mesh = Input(elemental_difference._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)
        self.through_layers = Input(elemental_difference._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self.through_layers)

class _OutputsElementalDifference(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_difference._spec().outputs, op)
        self.fields_container = Output(elemental_difference._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elemental_difference(Operator):
    """Transform ElementalNodal or Nodal field into Elemental field. Each elemental value is the maximum difference between the computed result for all nodes in this element. Result is computed on a given element scoping.

      available inputs:
         field (Field, FieldsContainer)
         mesh_scoping (Scoping) (optional)
         mesh (MeshedRegion) (optional)
         through_layers (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_difference()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_through_layers = bool()
      >>> op.inputs.through_layers.connect(my_through_layers)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field=None, mesh_scoping=None, mesh=None, through_layers=None, config=None, server=None):
        super().__init__(name="elemental_difference", config = config, server = server)
        self.inputs = _InputsElementalDifference(self)
        self.outputs = _OutputsElementalDifference(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if through_layers !=None:
            self.inputs.through_layers.connect(through_layers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal or Nodal field into Elemental field. Each elemental value is the maximum difference between the computed result for all nodes in this element. Result is computed on a given element scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""average only on these entities"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 10 : PinSpecification(name = "through_layers", type_names=["bool"], optional=True, document="""the max elemental difference is taken through the different shell layers if true (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_difference")

#internal name: elemental_nodal_To_nodal
#scripting name: elemental_nodal_to_nodal
class _InputsElementalNodalToNodal(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal._spec().inputs, op)
        self.field = Input(elemental_nodal_to_nodal._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.mesh_scoping = Input(elemental_nodal_to_nodal._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.should_average = Input(elemental_nodal_to_nodal._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.should_average)
        self.mesh = Input(elemental_nodal_to_nodal._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsElementalNodalToNodal(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal._spec().outputs, op)
        self.fields_container = Output(elemental_nodal_to_nodal._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elemental_nodal_to_nodal(Operator):
    """Transform ElementalNodal field into Nodal field using an averaging process, result is computed on a given node scoping.

      available inputs:
         field (Field, FieldsContainer)
         mesh_scoping (Scoping) (optional)
         should_average (bool) (optional)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_should_average = bool()
      >>> op.inputs.should_average.connect(my_should_average)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field=None, mesh_scoping=None, should_average=None, mesh=None, config=None, server=None):
        super().__init__(name="elemental_nodal_To_nodal", config = config, server = server)
        self.inputs = _InputsElementalNodalToNodal(self)
        self.outputs = _OutputsElementalNodalToNodal(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if should_average !=None:
            self.inputs.should_average.connect(should_average)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal field into Nodal field using an averaging process, result is computed on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""average only on these entities"""), 
                                 2 : PinSpecification(name = "should_average", type_names=["bool"], optional=True, document="""each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_nodal_To_nodal")

#internal name: elemental_difference_fc
#scripting name: elemental_difference_fc
class _InputsElementalDifferenceFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_difference_fc._spec().inputs, op)
        self.fields_container = Input(elemental_difference_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh = Input(elemental_difference_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.scoping = Input(elemental_difference_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.scoping)
        self.collapse_shell_layers = Input(elemental_difference_fc._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self.collapse_shell_layers)

class _OutputsElementalDifferenceFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_difference_fc._spec().outputs, op)
        self.fields_container = Output(elemental_difference_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elemental_difference_fc(Operator):
    """Transform ElementalNodal or Nodal field into Elemental field. Each elemental value is the maximum difference between the unaveraged or averaged (depending on the input fields) computed result for all nodes in this element. Result is computed on a given element scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are splitted by element shape and the output fields container has elshape label.

      available inputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion, MeshesContainer) (optional)
         scoping (Scoping, ScopingsContainer) (optional)
         collapse_shell_layers (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_difference_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, scoping=None, collapse_shell_layers=None, config=None, server=None):
        super().__init__(name="elemental_difference_fc", config = config, server = server)
        self.inputs = _InputsElementalDifferenceFc(self)
        self.outputs = _OutputsElementalDifferenceFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal or Nodal field into Elemental field. Each elemental value is the maximum difference between the unaveraged or averaged (depending on the input fields) computed result for all nodes in this element. Result is computed on a given element scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are splitted by element shape and the output fields container has elshape label.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping","scopings_container"], optional=True, document="""average only on these elements, if it is scoping container, the label must correspond to the one of the fields container"""), 
                                 10 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""the max elemental difference is taken through the different shell layers if true (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_difference_fc")

#internal name: elemental_nodal_To_nodal_fc
#scripting name: elemental_nodal_to_nodal_fc
class _InputsElementalNodalToNodalFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_fc._spec().inputs, op)
        self.fields_container = Input(elemental_nodal_to_nodal_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh = Input(elemental_nodal_to_nodal_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.should_average = Input(elemental_nodal_to_nodal_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.should_average)
        self.scoping = Input(elemental_nodal_to_nodal_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.scoping)

class _OutputsElementalNodalToNodalFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_fc._spec().outputs, op)
        self.fields_container = Output(elemental_nodal_to_nodal_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elemental_nodal_to_nodal_fc(Operator):
    """Transform ElementalNodal fields into Nodal fields using an averaging process, result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are splitted by element shape and the output fields container has elshape label.

      available inputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion, MeshesContainer) (optional)
         should_average (bool) (optional)
         scoping (Scoping, ScopingsContainer) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_should_average = bool()
      >>> op.inputs.should_average.connect(my_should_average)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, should_average=None, scoping=None, config=None, server=None):
        super().__init__(name="elemental_nodal_To_nodal_fc", config = config, server = server)
        self.inputs = _InputsElementalNodalToNodalFc(self)
        self.outputs = _OutputsElementalNodalToNodalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if should_average !=None:
            self.inputs.should_average.connect(should_average)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal fields into Nodal fields using an averaging process, result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are splitted by element shape and the output fields container has elshape label.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used"""), 
                                 2 : PinSpecification(name = "should_average", type_names=["bool"], optional=True, document="""each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities)"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping","scopings_container"], optional=True, document="""average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_nodal_To_nodal_fc")

#internal name: elemental_to_nodal
#scripting name: elemental_to_nodal
class _InputsElementalToNodal(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_to_nodal._spec().inputs, op)
        self.field = Input(elemental_to_nodal._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.mesh_scoping = Input(elemental_to_nodal._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.force_averaging = Input(elemental_to_nodal._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.force_averaging)

class _OutputsElementalToNodal(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_to_nodal._spec().outputs, op)
        self.field = Output(elemental_to_nodal._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class elemental_to_nodal(Operator):
    """Transform ElementalNodal field to Nodal field, compute result on a given node scoping.

      available inputs:
         field (Field, FieldsContainer)
         mesh_scoping (Scoping) (optional)
         force_averaging (int) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_to_nodal()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_force_averaging = int()
      >>> op.inputs.force_averaging.connect(my_force_averaging)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, mesh_scoping=None, force_averaging=None, config=None, server=None):
        super().__init__(name="elemental_to_nodal", config = config, server = server)
        self.inputs = _InputsElementalToNodal(self)
        self.outputs = _OutputsElementalToNodal(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if force_averaging !=None:
            self.inputs.force_averaging.connect(force_averaging)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal field to Nodal field, compute result on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "force_averaging", type_names=["int32"], optional=True, document="""averaging on nodes is used if this pin is set to 1 (default is 1 for integrated results and 0 for dicrete ones)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_to_nodal")

#internal name: elemental_to_nodal_fc
#scripting name: elemental_to_nodal_fc
class _InputsElementalToNodalFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_to_nodal_fc._spec().inputs, op)
        self.fields_container = Input(elemental_to_nodal_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh = Input(elemental_to_nodal_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.force_averaging = Input(elemental_to_nodal_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.force_averaging)
        self.mesh_scoping = Input(elemental_to_nodal_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.mesh_scoping)

class _OutputsElementalToNodalFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_to_nodal_fc._spec().outputs, op)
        self.fields_container = Output(elemental_to_nodal_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elemental_to_nodal_fc(Operator):
    """Transform ElementalNodal fields to Nodal fields, compute result on a given node scoping.

      available inputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion, MeshesContainer) (optional)
         force_averaging (int) (optional)
         mesh_scoping (Scoping, ScopingsContainer) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_to_nodal_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_force_averaging = int()
      >>> op.inputs.force_averaging.connect(my_force_averaging)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, force_averaging=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="elemental_to_nodal_fc", config = config, server = server)
        self.inputs = _InputsElementalToNodalFc(self)
        self.outputs = _OutputsElementalToNodalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if force_averaging !=None:
            self.inputs.force_averaging.connect(force_averaging)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal fields to Nodal fields, compute result on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "force_averaging", type_names=["int32"], optional=True, document="""averaging on nodes is used if this pin is set to 1 (default is one for integrated results and 0 for dicrete ones)"""), 
                                 3 : PinSpecification(name = "mesh_scoping", type_names=["scoping","scopings_container"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_to_nodal_fc")

#internal name: nodal_difference
#scripting name: nodal_difference
class _InputsNodalDifference(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_difference._spec().inputs, op)
        self.field = Input(nodal_difference._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.mesh_scoping = Input(nodal_difference._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.mesh = Input(nodal_difference._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsNodalDifference(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_difference._spec().outputs, op)
        self.fields_container = Output(nodal_difference._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_difference(Operator):
    """Transform ElementalNodal field into Nodal field. Each nodal value is the maximum difference between the unaveraged computed result for all elements that share this particular node. Result is computed on a given node scoping.

      available inputs:
         field (Field, FieldsContainer)
         mesh_scoping (Scoping) (optional)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.nodal_difference()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field=None, mesh_scoping=None, mesh=None, config=None, server=None):
        super().__init__(name="nodal_difference", config = config, server = server)
        self.inputs = _InputsNodalDifference(self)
        self.outputs = _OutputsNodalDifference(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal field into Nodal field. Each nodal value is the maximum difference between the unaveraged computed result for all elements that share this particular node. Result is computed on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""average only on these entities"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "nodal_difference")

#internal name: nodal_difference_fc
#scripting name: nodal_difference_fc
class _InputsNodalDifferenceFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_difference_fc._spec().inputs, op)
        self.fields_container = Input(nodal_difference_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh = Input(nodal_difference_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.scoping = Input(nodal_difference_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.scoping)

class _OutputsNodalDifferenceFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_difference_fc._spec().outputs, op)
        self.fields_container = Output(nodal_difference_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_difference_fc(Operator):
    """Transform ElementalNodal fields into Nodal fields. Each nodal value is the maximum difference between the unaveraged computed result for all elements that share this particular node. Result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are splitted by element shape and the output fields container has elshape label.

      available inputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion, MeshesContainer) (optional)
         scoping (Scoping, ScopingsContainer) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.nodal_difference_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, scoping=None, config=None, server=None):
        super().__init__(name="nodal_difference_fc", config = config, server = server)
        self.inputs = _InputsNodalDifferenceFc(self)
        self.outputs = _OutputsNodalDifferenceFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal fields into Nodal fields. Each nodal value is the maximum difference between the unaveraged computed result for all elements that share this particular node. Result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are splitted by element shape and the output fields container has elshape label.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping","scopings_container"], optional=True, document="""average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "nodal_difference_fc")

#internal name: elemental_fraction_fc
#scripting name: elemental_fraction_fc
class _InputsElementalFractionFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_fraction_fc._spec().inputs, op)
        self.fields_container = Input(elemental_fraction_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh = Input(elemental_fraction_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.scoping = Input(elemental_fraction_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.scoping)
        self.denominator = Input(elemental_fraction_fc._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self.denominator)
        self.collapse_shell_layers = Input(elemental_fraction_fc._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self.collapse_shell_layers)

class _OutputsElementalFractionFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_fraction_fc._spec().outputs, op)
        self.fields_container = Output(elemental_fraction_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elemental_fraction_fc(Operator):
    """Transform ElementalNodal fields into Elemental fields. Each elemental value is the fraction between the elemental difference and the entity average. Result is computed on a given elements scoping.

      available inputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion) (optional)
         scoping (Scoping) (optional)
         denominator (FieldsContainer) (optional)
         collapse_shell_layers (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_fraction_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_denominator = dpf.FieldsContainer()
      >>> op.inputs.denominator.connect(my_denominator)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, scoping=None, denominator=None, collapse_shell_layers=None, config=None, server=None):
        super().__init__(name="elemental_fraction_fc", config = config, server = server)
        self.inputs = _InputsElementalFractionFc(self)
        self.outputs = _OutputsElementalFractionFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if denominator !=None:
            self.inputs.denominator.connect(denominator)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal fields into Elemental fields. Each elemental value is the fraction between the elemental difference and the entity average. Result is computed on a given elements scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""average only on these elements, if it is scoping container, the label must correspond to the one of the fields container"""), 
                                 6 : PinSpecification(name = "denominator", type_names=["fields_container"], optional=True, document="""if a fields container is set in this pin, it is used as the denominator of the fraction instead of entity_average_fc"""), 
                                 10 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""the elemental difference and the entity average are taken through the different shell layers if true (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_fraction_fc")

#internal name: to_nodal
#scripting name: to_nodal
class _InputsToNodal(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(to_nodal._spec().inputs, op)
        self.field = Input(to_nodal._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.mesh_scoping = Input(to_nodal._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)

class _OutputsToNodal(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(to_nodal._spec().outputs, op)
        self.field = Output(to_nodal._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class to_nodal(Operator):
    """Transform input field into Nodal field using an averaging process, result is computed on a given node scoping.

      available inputs:
         field (Field, FieldsContainer)
         mesh_scoping (Scoping) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.to_nodal()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="to_nodal", config = config, server = server)
        self.inputs = _InputsToNodal(self)
        self.outputs = _OutputsToNodal(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform input field into Nodal field using an averaging process, result is computed on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "to_nodal")

#internal name: to_nodal_fc
#scripting name: to_nodal_fc
class _InputsToNodalFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(to_nodal_fc._spec().inputs, op)
        self.fields_container = Input(to_nodal_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh = Input(to_nodal_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.mesh_scoping = Input(to_nodal_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.mesh_scoping)

class _OutputsToNodalFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(to_nodal_fc._spec().outputs, op)
        self.fields_container = Output(to_nodal_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class to_nodal_fc(Operator):
    """Transform input fields into Nodal fields using an averaging process, result is computed on a given node scoping.

      available inputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion) (optional)
         mesh_scoping (Scoping) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.to_nodal_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="to_nodal_fc", config = config, server = server)
        self.inputs = _InputsToNodalFc(self)
        self.outputs = _OutputsToNodalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform input fields into Nodal fields using an averaging process, result is computed on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "to_nodal_fc")

#internal name: ElementalNodal_To_NodalElemental
#scripting name: elemental_nodal_to_nodal_elemental
class _InputsElementalNodalToNodalElemental(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_elemental._spec().inputs, op)
        self.field = Input(elemental_nodal_to_nodal_elemental._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.mesh_scoping = Input(elemental_nodal_to_nodal_elemental._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)

class _OutputsElementalNodalToNodalElemental(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_elemental._spec().outputs, op)
        self.field = Output(elemental_nodal_to_nodal_elemental._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class elemental_nodal_to_nodal_elemental(Operator):
    """Transform ElementalNodal field to NodalElemental, compute result on a given node scoping.

      available inputs:
         field (Field, FieldsContainer)
         mesh_scoping (Scoping) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="ElementalNodal_To_NodalElemental", config = config, server = server)
        self.inputs = _InputsElementalNodalToNodalElemental(self)
        self.outputs = _OutputsElementalNodalToNodalElemental(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal field to NodalElemental, compute result on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ElementalNodal_To_NodalElemental")

#internal name: extend_to_mid_nodes
#scripting name: extend_to_mid_nodes
class _InputsExtendToMidNodes(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(extend_to_mid_nodes._spec().inputs, op)
        self.field = Input(extend_to_mid_nodes._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.mesh = Input(extend_to_mid_nodes._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsExtendToMidNodes(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(extend_to_mid_nodes._spec().outputs, op)
        self.field = Output(extend_to_mid_nodes._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class extend_to_mid_nodes(Operator):
    """Extends ElementalNodal field defined on corner nodes to a ElementalNodal field defined also on the mid nodes.

      available inputs:
         field (Field, FieldsContainer)
         mesh (MeshedRegion) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.extend_to_mid_nodes()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, mesh=None, config=None, server=None):
        super().__init__(name="extend_to_mid_nodes", config = config, server = server)
        self.inputs = _InputsExtendToMidNodes(self)
        self.outputs = _OutputsExtendToMidNodes(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extends ElementalNodal field defined on corner nodes to a ElementalNodal field defined also on the mid nodes.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "extend_to_mid_nodes")

#internal name: extend_to_mid_nodes_fc
#scripting name: extend_to_mid_nodes_fc
class _InputsExtendToMidNodesFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(extend_to_mid_nodes_fc._spec().inputs, op)
        self.fields_container = Input(extend_to_mid_nodes_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh = Input(extend_to_mid_nodes_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)

class _OutputsExtendToMidNodesFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(extend_to_mid_nodes_fc._spec().outputs, op)
        self.fields_container = Output(extend_to_mid_nodes_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class extend_to_mid_nodes_fc(Operator):
    """Extends ElementalNodal fields defined on corner nodes to ElementalNodal fields defined also on the mid nodes.

      available inputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.extend_to_mid_nodes_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, config=None, server=None):
        super().__init__(name="extend_to_mid_nodes_fc", config = config, server = server)
        self.inputs = _InputsExtendToMidNodesFc(self)
        self.outputs = _OutputsExtendToMidNodesFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extends ElementalNodal fields defined on corner nodes to ElementalNodal fields defined also on the mid nodes.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "extend_to_mid_nodes_fc")

#internal name: entity_average
#scripting name: elemental_mean
class _InputsElementalMean(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_mean._spec().inputs, op)
        self.field = Input(elemental_mean._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.collapse_shell_layers = Input(elemental_mean._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.collapse_shell_layers)
        self.force_averaging = Input(elemental_mean._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.force_averaging)
        self.scoping = Input(elemental_mean._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.scoping)

class _OutputsElementalMean(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_mean._spec().outputs, op)
        self.field = Output(elemental_mean._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class elemental_mean(Operator):
    """Computes the average of a multi-entity fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal).

      available inputs:
         field (Field)
         collapse_shell_layers (bool) (optional)
         force_averaging (bool) (optional)
         scoping (Scoping) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_mean()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
      >>> my_force_averaging = bool()
      >>> op.inputs.force_averaging.connect(my_force_averaging)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, collapse_shell_layers=None, force_averaging=None, scoping=None, config=None, server=None):
        super().__init__(name="entity_average", config = config, server = server)
        self.inputs = _InputsElementalMean(self)
        self.outputs = _OutputsElementalMean(self)
        if field !=None:
            self.inputs.field.connect(field)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)
        if force_averaging !=None:
            self.inputs.force_averaging.connect(force_averaging)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the average of a multi-entity fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""if true shell layers are averaged as well (default is false)"""), 
                                 2 : PinSpecification(name = "force_averaging", type_names=["bool"], optional=True, document="""if true you average, if false you just sum"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "entity_average")

#internal name: entity_average_fc
#scripting name: elemental_mean_fc
class _InputsElementalMeanFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_mean_fc._spec().inputs, op)
        self.fields_container = Input(elemental_mean_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.collapse_shell_layers = Input(elemental_mean_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.collapse_shell_layers)
        self.force_averaging = Input(elemental_mean_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.force_averaging)
        self.scoping = Input(elemental_mean_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.scoping)
        self.meshed_region = Input(elemental_mean_fc._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.meshed_region)

class _OutputsElementalMeanFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(elemental_mean_fc._spec().outputs, op)
        self.fields_container = Output(elemental_mean_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class elemental_mean_fc(Operator):
    """Computes the average of a multi-entity container of fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal). If the input fields are mixed shell/solid and collapseShellLayers is not asked, then the fields are splitted by element shape and the output fields container has elshape label.

      available inputs:
         fields_container (FieldsContainer)
         collapse_shell_layers (bool) (optional)
         force_averaging (bool) (optional)
         scoping (Scoping) (optional)
         meshed_region (MeshedRegion) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_mean_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
      >>> my_force_averaging = bool()
      >>> op.inputs.force_averaging.connect(my_force_averaging)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.meshed_region.connect(my_meshed_region)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, collapse_shell_layers=None, force_averaging=None, scoping=None, meshed_region=None, config=None, server=None):
        super().__init__(name="entity_average_fc", config = config, server = server)
        self.inputs = _InputsElementalMeanFc(self)
        self.outputs = _OutputsElementalMeanFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)
        if force_averaging !=None:
            self.inputs.force_averaging.connect(force_averaging)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if meshed_region !=None:
            self.inputs.meshed_region.connect(meshed_region)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the average of a multi-entity container of fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal). If the input fields are mixed shell/solid and collapseShellLayers is not asked, then the fields are splitted by element shape and the output fields container has elshape label.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""if true shell layers are averaged as well (default is false)"""), 
                                 2 : PinSpecification(name = "force_averaging", type_names=["bool"], optional=True, document="""if true you average, if false you just sum"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""average only on these elements, if it is scoping container, the label must correspond to the one of the fields container"""), 
                                 4 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "entity_average_fc")

#internal name: to_elemental_fc
#scripting name: to_elemental_fc
class _InputsToElementalFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(to_elemental_fc._spec().inputs, op)
        self.fields_container = Input(to_elemental_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh = Input(to_elemental_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.mesh_scoping = Input(to_elemental_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.smoothen_values = Input(to_elemental_fc._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.smoothen_values)
        self.collapse_shell_layers = Input(to_elemental_fc._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self.collapse_shell_layers)

class _OutputsToElementalFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(to_elemental_fc._spec().outputs, op)
        self.fields_container = Output(to_elemental_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class to_elemental_fc(Operator):
    """Transform input fields into Elemental fields using an averaging process, result is computed on a given elements scoping.

      available inputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion) (optional)
         mesh_scoping (Scoping) (optional)
         smoothen_values (bool) (optional)
         collapse_shell_layers (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.to_elemental_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_smoothen_values = bool()
      >>> op.inputs.smoothen_values.connect(my_smoothen_values)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, mesh_scoping=None, smoothen_values=None, collapse_shell_layers=None, config=None, server=None):
        super().__init__(name="to_elemental_fc", config = config, server = server)
        self.inputs = _InputsToElementalFc(self)
        self.outputs = _OutputsToElementalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if smoothen_values !=None:
            self.inputs.smoothen_values.connect(smoothen_values)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform input fields into Elemental fields using an averaging process, result is computed on a given elements scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 7 : PinSpecification(name = "smoothen_values", type_names=["bool"], optional=True, document="""if it is set to true, elemental nodal fields are first averaged on nodes and then averaged on elements (default is false)"""), 
                                 10 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""if true shell layers are averaged as well (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "to_elemental_fc")

#internal name: nodal_to_elemental
#scripting name: nodal_to_elemental
class _InputsNodalToElemental(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_to_elemental._spec().inputs, op)
        self.field = Input(nodal_to_elemental._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.mesh_scoping = Input(nodal_to_elemental._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh_scoping)
        self.collapse_shell_layers = Input(nodal_to_elemental._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self.collapse_shell_layers)

class _OutputsNodalToElemental(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_to_elemental._spec().outputs, op)
        self.field = Output(nodal_to_elemental._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class nodal_to_elemental(Operator):
    """Transform Nodal field to Elemental field, compute result on a given element scoping.

      available inputs:
         field (Field, FieldsContainer)
         mesh_scoping (Scoping) (optional)
         collapse_shell_layers (bool) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.nodal_to_elemental()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, mesh_scoping=None, collapse_shell_layers=None, config=None, server=None):
        super().__init__(name="nodal_to_elemental", config = config, server = server)
        self.inputs = _InputsNodalToElemental(self)
        self.outputs = _OutputsNodalToElemental(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform Nodal field to Elemental field, compute result on a given element scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 10 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""if true shell layers are averaged as well (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "nodal_to_elemental")

#internal name: nodal_to_elemental_fc
#scripting name: nodal_to_elemental_fc
class _InputsNodalToElementalFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_to_elemental_fc._spec().inputs, op)
        self.fields_container = Input(nodal_to_elemental_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.mesh = Input(nodal_to_elemental_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.scoping = Input(nodal_to_elemental_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.scoping)
        self.collapse_shell_layers = Input(nodal_to_elemental_fc._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self.collapse_shell_layers)

class _OutputsNodalToElementalFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(nodal_to_elemental_fc._spec().outputs, op)
        self.fields_container = Output(nodal_to_elemental_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class nodal_to_elemental_fc(Operator):
    """Transform Nodal fields into Elemental fields using an averaging process, result is computed on a given elements scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are splitted by element shape and the output fields container has elshape label.

      available inputs:
         fields_container (FieldsContainer)
         mesh (MeshedRegion, MeshesContainer) (optional)
         scoping (Scoping, ScopingsContainer) (optional)
         collapse_shell_layers (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.nodal_to_elemental_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, scoping=None, collapse_shell_layers=None, config=None, server=None):
        super().__init__(name="nodal_to_elemental_fc", config = config, server = server)
        self.inputs = _InputsNodalToElementalFc(self)
        self.outputs = _OutputsNodalToElementalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform Nodal fields into Elemental fields using an averaging process, result is computed on a given elements scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are splitted by element shape and the output fields container has elshape label.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping","scopings_container"], optional=True, document="""average only on these elements, if it is scoping container, the label must correspond to the one of the fields container"""), 
                                 10 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""if true shell layers are averaged as well (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "nodal_to_elemental_fc")

