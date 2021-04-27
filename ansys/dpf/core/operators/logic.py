"""
Logic Operators
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "logic" category
"""

#internal name: compare::mesh
#scripting name: identical_meshes
class _InputsIdenticalMeshes(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(identical_meshes._spec().inputs, op)
        self.meshA = Input(identical_meshes._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.meshA)
        self.meshB = Input(identical_meshes._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.meshB)
        self.small_value = Input(identical_meshes._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.small_value)
        self.tolerance = Input(identical_meshes._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.tolerance)

class _OutputsIdenticalMeshes(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(identical_meshes._spec().outputs, op)
        self.are_identical = Output(identical_meshes._spec().output_pin(0), 0, op) 
        self._outputs.append(self.are_identical)

class identical_meshes(Operator):
    """Take two meshes and compare them.

      available inputs:
         meshA (MeshedRegion)
         meshB (MeshedRegion)
         small_value (float)
         tolerance (float)

      available outputs:
         are_identical (bool)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.identical_meshes()

      >>> # Make input connections
      >>> my_meshA = dpf.MeshedRegion()
      >>> op.inputs.meshA.connect(my_meshA)
      >>> my_meshB = dpf.MeshedRegion()
      >>> op.inputs.meshB.connect(my_meshB)
      >>> my_small_value = float()
      >>> op.inputs.small_value.connect(my_small_value)
      >>> my_tolerance = float()
      >>> op.inputs.tolerance.connect(my_tolerance)

      >>> # Get output data
      >>> result_are_identical = op.outputs.are_identical()"""
    def __init__(self, meshA=None, meshB=None, small_value=None, tolerance=None, config=None, server=None):
        super().__init__(name="compare::mesh", config = config, server = server)
        self.inputs = _InputsIdenticalMeshes(self)
        self.outputs = _OutputsIdenticalMeshes(self)
        if meshA !=None:
            self.inputs.meshA.connect(meshA)
        if meshB !=None:
            self.inputs.meshB.connect(meshB)
        if small_value !=None:
            self.inputs.small_value.connect(small_value)
        if tolerance !=None:
            self.inputs.tolerance.connect(tolerance)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take two meshes and compare them.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "meshA", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "meshB", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "small_value", type_names=["double"], optional=False, document="""define what is a small value for numeric comparison."""), 
                                 3 : PinSpecification(name = "tolerance", type_names=["double"], optional=False, document="""define the relative tolerance ceil for numeric comparison.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "are_identical", type_names=["bool"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "compare::mesh")

#internal name: component_selector_fc
#scripting name: component_selector_fc
class _InputsComponentSelectorFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(component_selector_fc._spec().inputs, op)
        self.fields_container = Input(component_selector_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.component_number = Input(component_selector_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.component_number)

class _OutputsComponentSelectorFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(component_selector_fc._spec().outputs, op)
        self.fields_container = Output(component_selector_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class component_selector_fc(Operator):
    """Create a scalar fields container based on the selected component for each field.

      available inputs:
         fields_container (FieldsContainer)
         component_number (int, list)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.component_selector_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_component_number = int()
      >>> op.inputs.component_number.connect(my_component_number)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, component_number=None, config=None, server=None):
        super().__init__(name="component_selector_fc", config = config, server = server)
        self.inputs = _InputsComponentSelectorFc(self)
        self.outputs = _OutputsComponentSelectorFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if component_number !=None:
            self.inputs.component_number.connect(component_number)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create a scalar fields container based on the selected component for each field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "component_number", type_names=["int32","vector<int32>"], optional=False, document="""one or several component index that will be extracted from the initial field.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "component_selector_fc")

#internal name: component_selector
#scripting name: component_selector
class _InputsComponentSelector(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(component_selector._spec().inputs, op)
        self.field = Input(component_selector._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.component_number = Input(component_selector._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.component_number)
        self.default_value = Input(component_selector._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.default_value)

class _OutputsComponentSelector(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(component_selector._spec().outputs, op)
        self.field = Output(component_selector._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class component_selector(Operator):
    """Create a scalar/vector field based on the selected component.

      available inputs:
         field (Field, FieldsContainer)
         component_number (int, list)
         default_value (float) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.component_selector()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_component_number = int()
      >>> op.inputs.component_number.connect(my_component_number)
      >>> my_default_value = float()
      >>> op.inputs.default_value.connect(my_default_value)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, component_number=None, default_value=None, config=None, server=None):
        super().__init__(name="component_selector", config = config, server = server)
        self.inputs = _InputsComponentSelector(self)
        self.outputs = _OutputsComponentSelector(self)
        if field !=None:
            self.inputs.field.connect(field)
        if component_number !=None:
            self.inputs.component_number.connect(component_number)
        if default_value !=None:
            self.inputs.default_value.connect(default_value)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create a scalar/vector field based on the selected component.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "component_number", type_names=["int32","vector<int32>"], optional=False, document="""one or several component index that will be extracted from the initial field."""), 
                                 2 : PinSpecification(name = "default_value", type_names=["double"], optional=True, document="""set a default value for components that do not exist""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "component_selector")

#internal name: compare::property_field
#scripting name: identical_property_fields
class _InputsIdenticalPropertyFields(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(identical_property_fields._spec().inputs, op)
        self.property_fieldA = Input(identical_property_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.property_fieldA)
        self.property_fieldB = Input(identical_property_fields._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.property_fieldB)

class _OutputsIdenticalPropertyFields(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(identical_property_fields._spec().outputs, op)
        self.are_identical = Output(identical_property_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self.are_identical)
        self.informations = Output(identical_property_fields._spec().output_pin(1), 1, op) 
        self._outputs.append(self.informations)

class identical_property_fields(Operator):
    """Take two property fields and compare them.

      available inputs:
         property_fieldA (MeshedRegion)
         property_fieldB (MeshedRegion)

      available outputs:
         are_identical (bool)
         informations (str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.identical_property_fields()

      >>> # Make input connections
      >>> my_property_fieldA = dpf.MeshedRegion()
      >>> op.inputs.property_fieldA.connect(my_property_fieldA)
      >>> my_property_fieldB = dpf.MeshedRegion()
      >>> op.inputs.property_fieldB.connect(my_property_fieldB)

      >>> # Get output data
      >>> result_are_identical = op.outputs.are_identical()
      >>> result_informations = op.outputs.informations()"""
    def __init__(self, property_fieldA=None, property_fieldB=None, config=None, server=None):
        super().__init__(name="compare::property_field", config = config, server = server)
        self.inputs = _InputsIdenticalPropertyFields(self)
        self.outputs = _OutputsIdenticalPropertyFields(self)
        if property_fieldA !=None:
            self.inputs.property_fieldA.connect(property_fieldA)
        if property_fieldB !=None:
            self.inputs.property_fieldB.connect(property_fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take two property fields and compare them.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "property_fieldA", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "property_fieldB", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "are_identical", type_names=["bool"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "informations", type_names=["string"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "compare::property_field")

#internal name: merge::fields_container_label
#scripting name: merge_fields_by_label
class _InputsMergeFieldsByLabel(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(merge_fields_by_label._spec().inputs, op)
        self.fields_container = Input(merge_fields_by_label._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.label = Input(merge_fields_by_label._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.label)
        self.merged_field_support = Input(merge_fields_by_label._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.merged_field_support)
        self.sumMerge = Input(merge_fields_by_label._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.sumMerge)

class _OutputsMergeFieldsByLabel(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(merge_fields_by_label._spec().outputs, op)
        self.fields_container = Output(merge_fields_by_label._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)
        self.merged_field_support = Output(merge_fields_by_label._spec().output_pin(1), 1, op) 
        self._outputs.append(self.merged_field_support)

class merge_fields_by_label(Operator):
    """Take a fields container and merge its fields that share the same label value.

      available inputs:
         fields_container (FieldsContainer)
         label (str)
         merged_field_support (AbstractFieldSupport) (optional)
         sumMerge (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)
         merged_field_support (AbstractFieldSupport)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.merge_fields_by_label()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_label = str()
      >>> op.inputs.label.connect(my_label)
      >>> my_merged_field_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_field_support.connect(my_merged_field_support)
      >>> my_sumMerge = bool()
      >>> op.inputs.sumMerge.connect(my_sumMerge)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()
      >>> result_merged_field_support = op.outputs.merged_field_support()"""
    def __init__(self, fields_container=None, label=None, merged_field_support=None, sumMerge=None, config=None, server=None):
        super().__init__(name="merge::fields_container_label", config = config, server = server)
        self.inputs = _InputsMergeFieldsByLabel(self)
        self.outputs = _OutputsMergeFieldsByLabel(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if label !=None:
            self.inputs.label.connect(label)
        if merged_field_support !=None:
            self.inputs.merged_field_support.connect(merged_field_support)
        if sumMerge !=None:
            self.inputs.sumMerge.connect(sumMerge)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a fields container and merge its fields that share the same label value.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "label", type_names=["string"], optional=False, document="""Label identifier that should be merged."""), 
                                 2 : PinSpecification(name = "merged_field_support", type_names=["abstract_field_support"], optional=True, document="""The FieldsContainer's support that has already been merged."""), 
                                 3 : PinSpecification(name = "sumMerge", type_names=["bool"], optional=True, document="""Default is false. If true redundant quantities are summed instead of being ignored.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "merged_field_support", type_names=["abstract_field_support"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::fields_container_label")

#internal name: merge::solid_shell_fields
#scripting name: solid_shell_fields
class _InputsSolidShellFields(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(solid_shell_fields._spec().inputs, op)
        self.fields_container = Input(solid_shell_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsSolidShellFields(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(solid_shell_fields._spec().outputs, op)
        self.fields_container = Output(solid_shell_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class solid_shell_fields(Operator):
    """Makes a fields based on fields container containing shell and solid fields with respect to time steps/frequencies.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.solid_shell_fields()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="merge::solid_shell_fields", config = config, server = server)
        self.inputs = _InputsSolidShellFields(self)
        self.outputs = _OutputsSolidShellFields(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Makes a fields based on fields container containing shell and solid fields with respect to time steps/frequencies.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::solid_shell_fields")

#internal name: AreFieldsIdentical
#scripting name: identical_fields
class _InputsIdenticalFields(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(identical_fields._spec().inputs, op)
        self.fieldA = Input(identical_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(identical_fields._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)
        self.double_value = Input(identical_fields._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.double_value)
        self.double_tolerance = Input(identical_fields._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.double_tolerance)

class _OutputsIdenticalFields(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(identical_fields._spec().outputs, op)
        self.boolean = Output(identical_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self.boolean)
        self.message = Output(identical_fields._spec().output_pin(1), 1, op) 
        self._outputs.append(self.message)

class identical_fields(Operator):
    """Check if two fields are identical.

      available inputs:
         fieldA (Field)
         fieldB (Field)
         double_value (float) (optional)
         double_tolerance (float) (optional)

      available outputs:
         boolean (bool)
         message (str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.identical_fields()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
      >>> my_double_value = float()
      >>> op.inputs.double_value.connect(my_double_value)
      >>> my_double_tolerance = float()
      >>> op.inputs.double_tolerance.connect(my_double_tolerance)

      >>> # Get output data
      >>> result_boolean = op.outputs.boolean()
      >>> result_message = op.outputs.message()"""
    def __init__(self, fieldA=None, fieldB=None, double_value=None, double_tolerance=None, config=None, server=None):
        super().__init__(name="AreFieldsIdentical", config = config, server = server)
        self.inputs = _InputsIdenticalFields(self)
        self.outputs = _OutputsIdenticalFields(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)
        if double_value !=None:
            self.inputs.double_value.connect(double_value)
        if double_tolerance !=None:
            self.inputs.double_tolerance.connect(double_tolerance)

    @staticmethod
    def _spec():
        spec = Specification(description="""Check if two fields are identical.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "double_value", type_names=["double"], optional=True, document="""Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14)."""), 
                                 3 : PinSpecification(name = "double_tolerance", type_names=["double"], optional=True, document="""Double relative tolerance.Maximum tolerance gap between to compared values : values within relative tolerance are considered identical(v1 - v2) / v2 < relativeTol(default is 0.001).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "boolean", type_names=["bool"], optional=False, document="""bool (true if identical...)"""), 
                                 1 : PinSpecification(name = "message", type_names=["string"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "AreFieldsIdentical")

#internal name: Are_fields_included
#scripting name: included_fields
class _InputsIncludedFields(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(included_fields._spec().inputs, op)
        self.fieldA = Input(included_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(included_fields._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)
        self.double_value = Input(included_fields._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.double_value)
        self.double_tolerance = Input(included_fields._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.double_tolerance)

class _OutputsIncludedFields(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(included_fields._spec().outputs, op)
        self.included = Output(included_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self.included)
        self.message = Output(included_fields._spec().output_pin(1), 1, op) 
        self._outputs.append(self.message)

class included_fields(Operator):
    """Check if one field belongs to another.

      available inputs:
         fieldA (Field)
         fieldB (Field)
         double_value (float)
         double_tolerance (float) (optional)

      available outputs:
         included (bool)
         message (str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.included_fields()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
      >>> my_double_value = float()
      >>> op.inputs.double_value.connect(my_double_value)
      >>> my_double_tolerance = float()
      >>> op.inputs.double_tolerance.connect(my_double_tolerance)

      >>> # Get output data
      >>> result_included = op.outputs.included()
      >>> result_message = op.outputs.message()"""
    def __init__(self, fieldA=None, fieldB=None, double_value=None, double_tolerance=None, config=None, server=None):
        super().__init__(name="Are_fields_included", config = config, server = server)
        self.inputs = _InputsIncludedFields(self)
        self.outputs = _OutputsIncludedFields(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)
        if double_value !=None:
            self.inputs.double_value.connect(double_value)
        if double_tolerance !=None:
            self.inputs.double_tolerance.connect(double_tolerance)

    @staticmethod
    def _spec():
        spec = Specification(description="""Check if one field belongs to another.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "double_value", type_names=["double"], optional=False, document="""Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14)."""), 
                                 3 : PinSpecification(name = "double_tolerance", type_names=["double"], optional=True, document="""Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "included", type_names=["bool"], optional=False, document="""bool (true if belongs...)"""), 
                                 1 : PinSpecification(name = "message", type_names=["string"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "Are_fields_included")

#internal name: AreFieldsIdentical_fc
#scripting name: identical_fc
class _InputsIdenticalFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(identical_fc._spec().inputs, op)
        self.fields_containerA = Input(identical_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_containerA)
        self.fields_containerB = Input(identical_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fields_containerB)
        self.tolerance = Input(identical_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.tolerance)
        self.small_value = Input(identical_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.small_value)

class _OutputsIdenticalFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(identical_fc._spec().outputs, op)
        self.boolean = Output(identical_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.boolean)
        self.message = Output(identical_fc._spec().output_pin(1), 1, op) 
        self._outputs.append(self.message)

class identical_fc(Operator):
    """Check if two fields container are identical.

      available inputs:
         fields_containerA (FieldsContainer)
         fields_containerB (FieldsContainer)
         tolerance (float)
         small_value (float)

      available outputs:
         boolean (bool)
         message (str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.identical_fc()

      >>> # Make input connections
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)
      >>> my_tolerance = float()
      >>> op.inputs.tolerance.connect(my_tolerance)
      >>> my_small_value = float()
      >>> op.inputs.small_value.connect(my_small_value)

      >>> # Get output data
      >>> result_boolean = op.outputs.boolean()
      >>> result_message = op.outputs.message()"""
    def __init__(self, fields_containerA=None, fields_containerB=None, tolerance=None, small_value=None, config=None, server=None):
        super().__init__(name="AreFieldsIdentical_fc", config = config, server = server)
        self.inputs = _InputsIdenticalFc(self)
        self.outputs = _OutputsIdenticalFc(self)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)
        if tolerance !=None:
            self.inputs.tolerance.connect(tolerance)
        if small_value !=None:
            self.inputs.small_value.connect(small_value)

    @staticmethod
    def _spec():
        spec = Specification(description="""Check if two fields container are identical.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "tolerance", type_names=["double"], optional=False, document="""Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001)."""), 
                                 3 : PinSpecification(name = "small_value", type_names=["double"], optional=False, document="""Double positive small value.Smallest value which will be considered during the comparison step : all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "boolean", type_names=["bool"], optional=False, document="""bool (true if identical...)"""), 
                                 1 : PinSpecification(name = "message", type_names=["string"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "AreFieldsIdentical_fc")

#internal name: enrich_materials
#scripting name: enrich_materials
class _InputsEnrichMaterials(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(enrich_materials._spec().inputs, op)
        self.streams = Input(enrich_materials._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.streams)

class _OutputsEnrichMaterials(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(enrich_materials._spec().outputs, op)
        self.MaterialContainer = Output(enrich_materials._spec().output_pin(0), 0, op) 
        self._outputs.append(self.MaterialContainer)

class enrich_materials(Operator):
    """Take a MaterialContainer and a stream and enrich the MaterialContainer using stream data.

      available inputs:
         MaterialContainer ()
         streams (StreamsContainer, FieldsContainer)
         streams_mapping ()

      available outputs:
         MaterialContainer (bool)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.enrich_materials()

      >>> # Make input connections
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)

      >>> # Get output data
      >>> result_MaterialContainer = op.outputs.MaterialContainer()"""
    def __init__(self, streams=None, config=None, server=None):
        super().__init__(name="enrich_materials", config = config, server = server)
        self.inputs = _InputsEnrichMaterials(self)
        self.outputs = _OutputsEnrichMaterials(self)
        if streams !=None:
            self.inputs.streams.connect(streams)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a MaterialContainer and a stream and enrich the MaterialContainer using stream data.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "MaterialContainer", type_names=[], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "streams", type_names=["streams_container","fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "streams_mapping", type_names=[], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "MaterialContainer", type_names=["bool"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "enrich_materials")

