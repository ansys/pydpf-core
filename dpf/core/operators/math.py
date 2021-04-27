"""
Math Operators
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

#internal name: minus
#scripting name: minus
class _InputsMinus(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(minus._spec().inputs, op)
        self.fieldA = Input(minus._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(minus._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)

class _OutputsMinus(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(minus._spec().outputs, op)
        self.field = Output(minus._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class minus(Operator):
    """Computes the difference of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.minus()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="minus", config = config, server = server)
        self.inputs = _InputsMinus(self)
        self.outputs = _OutputsMinus(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the difference of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "minus")

#internal name: cplx_multiply
#scripting name: cplx_multiply
class _InputsCplxMultiply(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cplx_multiply._spec().inputs, op)
        self.fields_containerA = Input(cplx_multiply._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_containerA)
        self.fields_containerB = Input(cplx_multiply._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fields_containerB)

class _OutputsCplxMultiply(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cplx_multiply._spec().outputs, op)
        self.fields_container = Output(cplx_multiply._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class cplx_multiply(Operator):
    """Computes multiply between two field containers containing complex fields.

      available inputs:
         fields_containerA (FieldsContainer)
         fields_containerB (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.cplx_multiply()

      >>> # Make input connections
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_containerA=None, fields_containerB=None, config=None, server=None):
        super().__init__(name="cplx_multiply", config = config, server = server)
        self.inputs = _InputsCplxMultiply(self)
        self.outputs = _OutputsCplxMultiply(self)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes multiply between two field containers containing complex fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cplx_multiply")

#internal name: unit_convert
#scripting name: unit_convert
class _InputsUnitConvert(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(unit_convert._spec().inputs, op)
        self.entity_to_convert = Input(unit_convert._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.entity_to_convert)
        self.unit_name = Input(unit_convert._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.unit_name)

class _OutputsUnitConvert(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(unit_convert._spec().outputs, op)
        self.converted_entity_as_field = Output( _modify_output_spec_with_one_type(unit_convert._spec().output_pin(0), "field"), 0, op) 
        self._outputs.append(self.converted_entity_as_field)
        self.converted_entity_as_fields_container = Output( _modify_output_spec_with_one_type(unit_convert._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.converted_entity_as_fields_container)
        self.converted_entity_as_meshed_region = Output( _modify_output_spec_with_one_type(unit_convert._spec().output_pin(0), "abstract_meshed_region"), 0, op) 
        self._outputs.append(self.converted_entity_as_meshed_region)
        self.converted_entity_as_meshes_container = Output( _modify_output_spec_with_one_type(unit_convert._spec().output_pin(0), "meshes_container"), 0, op) 
        self._outputs.append(self.converted_entity_as_meshes_container)

class unit_convert(Operator):
    """Convert an input field/fields container or mesh of a given unit to another unit.

      available inputs:
         entity_to_convert (Field, FieldsContainer, MeshedRegion, MeshesContainer)
         unit_name (str)

      available outputs:
         converted_entity (Field ,FieldsContainer ,MeshedRegion ,MeshesContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.unit_convert()

      >>> # Make input connections
      >>> my_entity_to_convert = dpf.Field()
      >>> op.inputs.entity_to_convert.connect(my_entity_to_convert)
      >>> my_unit_name = str()
      >>> op.inputs.unit_name.connect(my_unit_name)

      >>> # Get output data
      >>> result_converted_entity = op.outputs.converted_entity()"""
    def __init__(self, entity_to_convert=None, unit_name=None, config=None, server=None):
        super().__init__(name="unit_convert", config = config, server = server)
        self.inputs = _InputsUnitConvert(self)
        self.outputs = _OutputsUnitConvert(self)
        if entity_to_convert !=None:
            self.inputs.entity_to_convert.connect(entity_to_convert)
        if unit_name !=None:
            self.inputs.unit_name.connect(unit_name)

    @staticmethod
    def _spec():
        spec = Specification(description="""Convert an input field/fields container or mesh of a given unit to another unit.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "entity_to_convert", type_names=["field","fields_container","abstract_meshed_region","meshes_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "unit_name", type_names=["string"], optional=False, document="""unit as a string, ex 'm' for meter, 'Pa' for pascal,...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "converted_entity", type_names=["field","fields_container","abstract_meshed_region","meshes_container"], optional=False, document="""the output entity is the same as the input (inplace operator)""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "unit_convert")

#internal name: minus_fc
#scripting name: minus_fc
class _InputsMinusFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(minus_fc._spec().inputs, op)
        self.field_or_fields_container_A = Input(minus_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field_or_fields_container_A)
        self.field_or_fields_container_B = Input(minus_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.field_or_fields_container_B)

class _OutputsMinusFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(minus_fc._spec().outputs, op)
        self.fields_container = Output(minus_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class minus_fc(Operator):
    """Computes the difference of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

      available inputs:
         field_or_fields_container_A (FieldsContainer)
         field_or_fields_container_B (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.minus_fc()

      >>> # Make input connections
      >>> my_field_or_fields_container_A = dpf.FieldsContainer()
      >>> op.inputs.field_or_fields_container_A.connect(my_field_or_fields_container_A)
      >>> my_field_or_fields_container_B = dpf.FieldsContainer()
      >>> op.inputs.field_or_fields_container_B.connect(my_field_or_fields_container_B)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field_or_fields_container_A=None, field_or_fields_container_B=None, config=None, server=None):
        super().__init__(name="minus_fc", config = config, server = server)
        self.inputs = _InputsMinusFc(self)
        self.outputs = _OutputsMinusFc(self)
        if field_or_fields_container_A !=None:
            self.inputs.field_or_fields_container_A.connect(field_or_fields_container_A)
        if field_or_fields_container_B !=None:
            self.inputs.field_or_fields_container_B.connect(field_or_fields_container_B)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the difference of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field_or_fields_container_A", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "field_or_fields_container_B", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "minus_fc")

#internal name: accumulate
#scripting name: accumulate
class _InputsAccumulate(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(accumulate._spec().inputs, op)
        self.fieldA = Input(accumulate._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)

class _OutputsAccumulate(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(accumulate._spec().outputs, op)
        self.field = Output(accumulate._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class accumulate(Operator):
    """Sum all the elementary data of a field to get one elementary data at the end.

      available inputs:
         fieldA (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.accumulate()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, config=None, server=None):
        super().__init__(name="accumulate", config = config, server = server)
        self.inputs = _InputsAccumulate(self)
        self.outputs = _OutputsAccumulate(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)

    @staticmethod
    def _spec():
        spec = Specification(description="""Sum all the elementary data of a field to get one elementary data at the end.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "accumulate")

#internal name: unit_convert_fc
#scripting name: unit_convert_fc
class _InputsUnitConvertFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(unit_convert_fc._spec().inputs, op)
        self.fields_container = Input(unit_convert_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.unit_name = Input(unit_convert_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.unit_name)

class _OutputsUnitConvertFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(unit_convert_fc._spec().outputs, op)
        self.fields_container = Output(unit_convert_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class unit_convert_fc(Operator):
    """Convert an input fields container of a given unit to another unit.

      available inputs:
         fields_container (FieldsContainer)
         unit_name (str)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.unit_convert_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_unit_name = str()
      >>> op.inputs.unit_name.connect(my_unit_name)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, unit_name=None, config=None, server=None):
        super().__init__(name="unit_convert_fc", config = config, server = server)
        self.inputs = _InputsUnitConvertFc(self)
        self.outputs = _OutputsUnitConvertFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if unit_name !=None:
            self.inputs.unit_name.connect(unit_name)

    @staticmethod
    def _spec():
        spec = Specification(description="""Convert an input fields container of a given unit to another unit.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "unit_name", type_names=["string"], optional=False, document="""unit as a string, ex 'm' for meter, 'Pa' for pascal,...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "unit_convert_fc")

#internal name: accumulate_min_over_label_fc
#scripting name: accumulate_min_over_label_fc
class _InputsAccumulateMinOverLabelFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(accumulate_min_over_label_fc._spec().inputs, op)
        self.fields_container = Input(accumulate_min_over_label_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsAccumulateMinOverLabelFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(accumulate_min_over_label_fc._spec().outputs, op)
        self.field = Output(accumulate_min_over_label_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class accumulate_min_over_label_fc(Operator):
    """Compute the component-wise sum over all the fields having the same id for the label set in input in the fields container and take its opposite. This computation can be incremental, if the input fields container is connected and the operator is ran several time, the output field will be on all the inputs connected

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.accumulate_min_over_label_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="accumulate_min_over_label_fc", config = config, server = server)
        self.inputs = _InputsAccumulateMinOverLabelFc(self)
        self.outputs = _OutputsAccumulateMinOverLabelFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the component-wise sum over all the fields having the same id for the label set in input in the fields container and take its opposite. This computation can be incremental, if the input fields container is connected and the operator is ran several time, the output field will be on all the inputs connected""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "accumulate_min_over_label_fc")

#internal name: add
#scripting name: add
class _InputsAdd(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(add._spec().inputs, op)
        self.fieldA = Input(add._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(add._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)

class _OutputsAdd(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(add._spec().outputs, op)
        self.field = Output(add._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class add(Operator):
    """Computes the sum of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field. if one of the input field is empty, the remaining is forwarded to the output.

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.add()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="add", config = config, server = server)
        self.inputs = _InputsAdd(self)
        self.outputs = _OutputsAdd(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the sum of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field. if one of the input field is empty, the remaining is forwarded to the output.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "add")

#internal name: add_fc
#scripting name: add_fc
class _InputsAddFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(add_fc._spec().inputs, op)
        self.fields_container1 = Input(add_fc._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self.fields_container1)
        self.fields_container2 = Input(add_fc._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self.fields_container2)

class _OutputsAddFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(add_fc._spec().outputs, op)
        self.fields_container = Output(add_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class add_fc(Operator):
    """Select all fields having the same label space in the input fields container, and add those together. If fields, doubles, or vectors of doubles are put in input, they are added to all the fields.

      available inputs:
         fields_container1 (FieldsContainer, Field, float, list)
         fields_container2 (FieldsContainer, Field, float, list)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.add_fc()

      >>> # Make input connections
      >>> my_fields_container1 = dpf.FieldsContainer()
      >>> op.inputs.fields_container1.connect(my_fields_container1)
      >>> my_fields_container2 = dpf.FieldsContainer()
      >>> op.inputs.fields_container2.connect(my_fields_container2)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container1=None, fields_container2=None, config=None, server=None):
        super().__init__(name="add_fc", config = config, server = server)
        self.inputs = _InputsAddFc(self)
        self.outputs = _OutputsAddFc(self)
        if fields_container1 !=None:
            self.inputs.fields_container1.connect(fields_container1)
        if fields_container2 !=None:
            self.inputs.fields_container2.connect(fields_container2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Select all fields having the same label space in the input fields container, and add those together. If fields, doubles, or vectors of doubles are put in input, they are added to all the fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container","field","double","vector<double>"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_container", type_names=["fields_container","field","double","vector<double>"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "add_fc")

#internal name: sin_fc
#scripting name: sin_fc
class _InputsSinFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(sin_fc._spec().inputs, op)
        self.fields_container = Input(sin_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsSinFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(sin_fc._spec().outputs, op)
        self.fields_container = Output(sin_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class sin_fc(Operator):
    """Computes element-wise sin(field[i]).

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.sin_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="sin_fc", config = config, server = server)
        self.inputs = _InputsSinFc(self)
        self.outputs = _OutputsSinFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise sin(field[i]).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sin_fc")

#internal name: add_constant
#scripting name: add_constant
class _InputsAddConstant(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(add_constant._spec().inputs, op)
        self.field = Input(add_constant._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.ponderation = Input(add_constant._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.ponderation)

class _OutputsAddConstant(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(add_constant._spec().outputs, op)
        self.field = Output(add_constant._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class add_constant(Operator):
    """Computes the sum of a field (in 0) and a scalar (in 1).

      available inputs:
         field (Field, FieldsContainer)
         ponderation (float, list)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.add_constant()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, ponderation=None, config=None, server=None):
        super().__init__(name="add_constant", config = config, server = server)
        self.inputs = _InputsAddConstant(self)
        self.outputs = _OutputsAddConstant(self)
        if field !=None:
            self.inputs.field.connect(field)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the sum of a field (in 0) and a scalar (in 1).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "ponderation", type_names=["double","vector<double>"], optional=False, document="""double or vector of double""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "add_constant")

#internal name: invert_fc
#scripting name: invert_fc
class _InputsInvertFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(invert_fc._spec().inputs, op)
        self.fields_container = Input(invert_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsInvertFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(invert_fc._spec().outputs, op)
        self.fields_container = Output(invert_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class invert_fc(Operator):
    """Compute the element-wise, component-wise, inverse of a field (1./x)

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.invert_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="invert_fc", config = config, server = server)
        self.inputs = _InputsInvertFc(self)
        self.outputs = _OutputsInvertFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the element-wise, component-wise, inverse of a field (1./x)""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "invert_fc")

#internal name: Pow
#scripting name: pow
class _InputsPow(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(pow._spec().inputs, op)
        self.field = Input(pow._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.factor = Input(pow._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.factor)

class _OutputsPow(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(pow._spec().outputs, op)
        self.field = Output(pow._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class pow(Operator):
    """Computes element-wise field[i]^p.

      available inputs:
         field (Field)
         factor (float)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.pow()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_factor = float()
      >>> op.inputs.factor.connect(my_factor)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, factor=None, config=None, server=None):
        super().__init__(name="Pow", config = config, server = server)
        self.inputs = _InputsPow(self)
        self.outputs = _OutputsPow(self)
        if field !=None:
            self.inputs.field.connect(field)
        if factor !=None:
            self.inputs.factor.connect(factor)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise field[i]^p.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "factor", type_names=["double"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "Pow")

#internal name: add_constant_fc
#scripting name: add_constant_fc
class _InputsAddConstantFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(add_constant_fc._spec().inputs, op)
        self.fields_container = Input(add_constant_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.ponderation = Input(add_constant_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.ponderation)

class _OutputsAddConstantFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(add_constant_fc._spec().outputs, op)
        self.fields_container = Output(add_constant_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class add_constant_fc(Operator):
    """Computes the sum of a field (in 0) and a scalar (in 1).

      available inputs:
         fields_container (FieldsContainer)
         ponderation (float, list)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.add_constant_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, ponderation=None, config=None, server=None):
        super().__init__(name="add_constant_fc", config = config, server = server)
        self.inputs = _InputsAddConstantFc(self)
        self.outputs = _OutputsAddConstantFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the sum of a field (in 0) and a scalar (in 1).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "ponderation", type_names=["double","vector<double>"], optional=False, document="""double or vector of double""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "add_constant_fc")

#internal name: scale
#scripting name: scale
class _InputsScale(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(scale._spec().inputs, op)
        self.field = Input(scale._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.ponderation = Input(scale._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.ponderation)
        self.boolean = Input(scale._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.boolean)

class _OutputsScale(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(scale._spec().outputs, op)
        self.field = Output(scale._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class scale(Operator):
    """Scales a field by a constant factor.

      available inputs:
         field (Field, FieldsContainer)
         ponderation (float, Field)
         boolean (bool) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.scale()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)
      >>> my_boolean = bool()
      >>> op.inputs.boolean.connect(my_boolean)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, ponderation=None, boolean=None, config=None, server=None):
        super().__init__(name="scale", config = config, server = server)
        self.inputs = _InputsScale(self)
        self.outputs = _OutputsScale(self)
        if field !=None:
            self.inputs.field.connect(field)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)
        if boolean !=None:
            self.inputs.boolean.connect(boolean)

    @staticmethod
    def _spec():
        spec = Specification(description="""Scales a field by a constant factor.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "ponderation", type_names=["double","field"], optional=False, document="""Double/Field scoped on overall"""), 
                                 2 : PinSpecification(name = "boolean", type_names=["bool"], optional=True, document="""bool(optional, default false) if set to true, output of scale is mane dimensionless""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scale")

#internal name: Pow_fc
#scripting name: pow_fc
class _InputsPowFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(pow_fc._spec().inputs, op)
        self.fields_container = Input(pow_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.factor = Input(pow_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.factor)

class _OutputsPowFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(pow_fc._spec().outputs, op)
        self.fields_container = Output(pow_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class pow_fc(Operator):
    """Computes element-wise field[i]^p.

      available inputs:
         fields_container (FieldsContainer)
         factor (float)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.pow_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_factor = float()
      >>> op.inputs.factor.connect(my_factor)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, factor=None, config=None, server=None):
        super().__init__(name="Pow_fc", config = config, server = server)
        self.inputs = _InputsPowFc(self)
        self.outputs = _OutputsPowFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if factor !=None:
            self.inputs.factor.connect(factor)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise field[i]^p.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "factor", type_names=["double"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "Pow_fc")

#internal name: scale_fc
#scripting name: scale_fc
class _InputsScaleFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(scale_fc._spec().inputs, op)
        self.fields_container = Input(scale_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.ponderation = Input(scale_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.ponderation)
        self.boolean = Input(scale_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.boolean)

class _OutputsScaleFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(scale_fc._spec().outputs, op)
        self.fields_container = Output(scale_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class scale_fc(Operator):
    """Scales a field by a constant factor.

      available inputs:
         fields_container (FieldsContainer)
         ponderation (float, Field)
         boolean (bool) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.scale_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)
      >>> my_boolean = bool()
      >>> op.inputs.boolean.connect(my_boolean)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, ponderation=None, boolean=None, config=None, server=None):
        super().__init__(name="scale_fc", config = config, server = server)
        self.inputs = _InputsScaleFc(self)
        self.outputs = _OutputsScaleFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)
        if boolean !=None:
            self.inputs.boolean.connect(boolean)

    @staticmethod
    def _spec():
        spec = Specification(description="""Scales a field by a constant factor.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "ponderation", type_names=["double","field"], optional=False, document="""Double/Field scoped on overall"""), 
                                 2 : PinSpecification(name = "boolean", type_names=["bool"], optional=True, document="""bool(optional, default false) if set to true, output of scale is mane dimensionless""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scale_fc")

#internal name: centroid
#scripting name: centroid
class _InputsCentroid(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(centroid._spec().inputs, op)
        self.fieldA = Input(centroid._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(centroid._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)
        self.factor = Input(centroid._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.factor)

class _OutputsCentroid(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(centroid._spec().outputs, op)
        self.field = Output(centroid._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class centroid(Operator):
    """Computes centroid of field1 and field2, using fieldOut = field1*(1.-fact)+field2*(fact).

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)
         factor (float)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.centroid()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
      >>> my_factor = float()
      >>> op.inputs.factor.connect(my_factor)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, factor=None, config=None, server=None):
        super().__init__(name="centroid", config = config, server = server)
        self.inputs = _InputsCentroid(self)
        self.outputs = _OutputsCentroid(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)
        if factor !=None:
            self.inputs.factor.connect(factor)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes centroid of field1 and field2, using fieldOut = field1*(1.-fact)+field2*(fact).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 2 : PinSpecification(name = "factor", type_names=["double"], optional=False, document="""Scalar""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "centroid")

#internal name: sweeping_phase
#scripting name: sweeping_phase
class _InputsSweepingPhase(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(sweeping_phase._spec().inputs, op)
        self.real_field = Input(sweeping_phase._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.real_field)
        self.imaginary_field = Input(sweeping_phase._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.imaginary_field)
        self.angle = Input(sweeping_phase._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.angle)
        self.unit_name = Input(sweeping_phase._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.unit_name)
        self.abs_value = Input(sweeping_phase._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.abs_value)
        self.imaginary_part_null = Input(sweeping_phase._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self.imaginary_part_null)

class _OutputsSweepingPhase(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(sweeping_phase._spec().outputs, op)
        self.field = Output(sweeping_phase._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class sweeping_phase(Operator):
    """Shift the phase of a real and an imaginary fields (in 0 and 1) of a given angle (in 3) of unit (in 4).

      available inputs:
         real_field (Field, FieldsContainer)
         imaginary_field (Field, FieldsContainer)
         angle (float)
         unit_name (str)
         abs_value (bool)
         imaginary_part_null (bool)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.sweeping_phase()

      >>> # Make input connections
      >>> my_real_field = dpf.Field()
      >>> op.inputs.real_field.connect(my_real_field)
      >>> my_imaginary_field = dpf.Field()
      >>> op.inputs.imaginary_field.connect(my_imaginary_field)
      >>> my_angle = float()
      >>> op.inputs.angle.connect(my_angle)
      >>> my_unit_name = str()
      >>> op.inputs.unit_name.connect(my_unit_name)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_imaginary_part_null = bool()
      >>> op.inputs.imaginary_part_null.connect(my_imaginary_part_null)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, real_field=None, imaginary_field=None, angle=None, unit_name=None, abs_value=None, imaginary_part_null=None, config=None, server=None):
        super().__init__(name="sweeping_phase", config = config, server = server)
        self.inputs = _InputsSweepingPhase(self)
        self.outputs = _OutputsSweepingPhase(self)
        if real_field !=None:
            self.inputs.real_field.connect(real_field)
        if imaginary_field !=None:
            self.inputs.imaginary_field.connect(imaginary_field)
        if angle !=None:
            self.inputs.angle.connect(angle)
        if unit_name !=None:
            self.inputs.unit_name.connect(unit_name)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)
        if imaginary_part_null !=None:
            self.inputs.imaginary_part_null.connect(imaginary_part_null)

    @staticmethod
    def _spec():
        spec = Specification(description="""Shift the phase of a real and an imaginary fields (in 0 and 1) of a given angle (in 3) of unit (in 4).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "real_field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "imaginary_field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 2 : PinSpecification(name = "angle", type_names=["double"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "unit_name", type_names=["string"], optional=False, document="""String Unit"""), 
                                 4 : PinSpecification(name = "abs_value", type_names=["bool"], optional=False, document=""""""), 
                                 5 : PinSpecification(name = "imaginary_part_null", type_names=["bool"], optional=False, document="""if the imaginary part field is empty and this pin is true, then the imaginary part is supposed to be 0 (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sweeping_phase")

#internal name: centroid_fc
#scripting name: centroid_fc
class _InputsCentroidFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(centroid_fc._spec().inputs, op)
        self.fields_container = Input(centroid_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.time_freq = Input(centroid_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.time_freq)
        self.step = Input(centroid_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.step)

class _OutputsCentroidFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(centroid_fc._spec().outputs, op)
        self.fields_container = Output(centroid_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class centroid_fc(Operator):
    """Computes the centroid of all the matching fields of a fields container at a given time or frequency, using fieldOut = field1*(1.-fact)+field2*(fact).

      available inputs:
         fields_container (FieldsContainer)
         time_freq (float)
         step (int) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.centroid_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_time_freq = float()
      >>> op.inputs.time_freq.connect(my_time_freq)
      >>> my_step = int()
      >>> op.inputs.step.connect(my_step)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, time_freq=None, step=None, config=None, server=None):
        super().__init__(name="centroid_fc", config = config, server = server)
        self.inputs = _InputsCentroidFc(self)
        self.outputs = _OutputsCentroidFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if time_freq !=None:
            self.inputs.time_freq.connect(time_freq)
        if step !=None:
            self.inputs.step.connect(step)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the centroid of all the matching fields of a fields container at a given time or frequency, using fieldOut = field1*(1.-fact)+field2*(fact).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "time_freq", type_names=["double"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "step", type_names=["int32"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "centroid_fc")

#internal name: sweeping_phase_fc
#scripting name: sweeping_phase_fc
class _InputsSweepingPhaseFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(sweeping_phase_fc._spec().inputs, op)
        self.fields_container = Input(sweeping_phase_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.angle = Input(sweeping_phase_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.angle)
        self.unit_name = Input(sweeping_phase_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.unit_name)
        self.abs_value = Input(sweeping_phase_fc._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.abs_value)

class _OutputsSweepingPhaseFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(sweeping_phase_fc._spec().outputs, op)
        self.fields_container = Output(sweeping_phase_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class sweeping_phase_fc(Operator):
    """Shift the phase of all the corresponding real and imaginary fields of a fields container for a given angle (in 2) of unit (in 4).

      available inputs:
         fields_container (FieldsContainer)
         angle (float)
         unit_name (str)
         abs_value (bool)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.sweeping_phase_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_angle = float()
      >>> op.inputs.angle.connect(my_angle)
      >>> my_unit_name = str()
      >>> op.inputs.unit_name.connect(my_unit_name)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, angle=None, unit_name=None, abs_value=None, config=None, server=None):
        super().__init__(name="sweeping_phase_fc", config = config, server = server)
        self.inputs = _InputsSweepingPhaseFc(self)
        self.outputs = _OutputsSweepingPhaseFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if angle !=None:
            self.inputs.angle.connect(angle)
        if unit_name !=None:
            self.inputs.unit_name.connect(unit_name)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)

    @staticmethod
    def _spec():
        spec = Specification(description="""Shift the phase of all the corresponding real and imaginary fields of a fields container for a given angle (in 2) of unit (in 4).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "angle", type_names=["double"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "unit_name", type_names=["string"], optional=False, document="""String Unit"""), 
                                 4 : PinSpecification(name = "abs_value", type_names=["bool"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sweeping_phase_fc")

#internal name: sqr
#scripting name: sqr
class _InputsSqr(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(sqr._spec().inputs, op)
        self.field = Input(sqr._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsSqr(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(sqr._spec().outputs, op)
        self.field = Output(sqr._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class sqr(Operator):
    """Computes element-wise field[i]^2.

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.sqr()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="sqr", config = config, server = server)
        self.inputs = _InputsSqr(self)
        self.outputs = _OutputsSqr(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise field[i]^2.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sqr")

#internal name: sin
#scripting name: sin
class _InputsSin(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(sin._spec().inputs, op)
        self.field = Input(sin._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsSin(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(sin._spec().outputs, op)
        self.field = Output(sin._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class sin(Operator):
    """Computes element-wise sin(field[i]).

      available inputs:
         field (Field)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.sin()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="sin", config = config, server = server)
        self.inputs = _InputsSin(self)
        self.outputs = _OutputsSin(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise sin(field[i]).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sin")

#internal name: cos
#scripting name: cos
class _InputsCos(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cos._spec().inputs, op)
        self.field = Input(cos._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsCos(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cos._spec().outputs, op)
        self.field = Output(cos._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class cos(Operator):
    """Computes element-wise cos(field[i]).

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.cos()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="cos", config = config, server = server)
        self.inputs = _InputsCos(self)
        self.outputs = _OutputsCos(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise cos(field[i]).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cos")

#internal name: cos_fc
#scripting name: cos_fc
class _InputsCosFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cos_fc._spec().inputs, op)
        self.fields_container = Input(cos_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsCosFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cos_fc._spec().outputs, op)
        self.fields_container = Output(cos_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class cos_fc(Operator):
    """Computes element-wise cos(field[i]).

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.cos_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="cos_fc", config = config, server = server)
        self.inputs = _InputsCosFc(self)
        self.outputs = _OutputsCosFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise cos(field[i]).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cos_fc")

#internal name: CplxOp
#scripting name: linear_combination
class _InputsLinearCombination(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(linear_combination._spec().inputs, op)
        self.a = Input(linear_combination._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.a)
        self.fields_containerA = Input(linear_combination._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fields_containerA)
        self.fields_containerB = Input(linear_combination._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.fields_containerB)
        self.b = Input(linear_combination._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.b)
        self.fields_containerC = Input(linear_combination._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.fields_containerC)

class _OutputsLinearCombination(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(linear_combination._spec().outputs, op)
        self.fields_container = Output(linear_combination._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class linear_combination(Operator):
    """Computes aXY + bZ where a,b (in 0, in 3) are scalar and X,Y,Z (in 1,2,4) are complex numbers.

      available inputs:
         a (float)
         fields_containerA (FieldsContainer)
         fields_containerB (FieldsContainer)
         b (float)
         fields_containerC (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.linear_combination()

      >>> # Make input connections
      >>> my_a = float()
      >>> op.inputs.a.connect(my_a)
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)
      >>> my_b = float()
      >>> op.inputs.b.connect(my_b)
      >>> my_fields_containerC = dpf.FieldsContainer()
      >>> op.inputs.fields_containerC.connect(my_fields_containerC)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, a=None, fields_containerA=None, fields_containerB=None, b=None, fields_containerC=None, config=None, server=None):
        super().__init__(name="CplxOp", config = config, server = server)
        self.inputs = _InputsLinearCombination(self)
        self.outputs = _OutputsLinearCombination(self)
        if a !=None:
            self.inputs.a.connect(a)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)
        if b !=None:
            self.inputs.b.connect(b)
        if fields_containerC !=None:
            self.inputs.fields_containerC.connect(fields_containerC)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes aXY + bZ where a,b (in 0, in 3) are scalar and X,Y,Z (in 1,2,4) are complex numbers.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "a", type_names=["double"], optional=False, document="""Double"""), 
                                 1 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "b", type_names=["double"], optional=False, document="""Double"""), 
                                 4 : PinSpecification(name = "fields_containerC", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "CplxOp")

#internal name: sqr_fc
#scripting name: sqr_fc
class _InputsSqrFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(sqr_fc._spec().inputs, op)
        self.fields_container = Input(sqr_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsSqrFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(sqr_fc._spec().outputs, op)
        self.fields_container = Output(sqr_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class sqr_fc(Operator):
    """Computes element-wise field[i]^2.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.sqr_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="sqr_fc", config = config, server = server)
        self.inputs = _InputsSqrFc(self)
        self.outputs = _OutputsSqrFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise field[i]^2.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sqr_fc")

#internal name: sqrt
#scripting name: sqrt
class _InputsSqrt(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(sqrt._spec().inputs, op)
        self.field = Input(sqrt._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsSqrt(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(sqrt._spec().outputs, op)
        self.field = Output(sqrt._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class sqrt(Operator):
    """Computes element-wise sqrt(field1).

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.sqrt()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="sqrt", config = config, server = server)
        self.inputs = _InputsSqrt(self)
        self.outputs = _OutputsSqrt(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise sqrt(field1).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sqrt")

#internal name: norm
#scripting name: norm
class _InputsNorm(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(norm._spec().inputs, op)
        self.field = Input(norm._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsNorm(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(norm._spec().outputs, op)
        self.field = Output(norm._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class norm(Operator):
    """Computes the element-wise L2 norm of the field elementary data.

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.norm()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="norm", config = config, server = server)
        self.inputs = _InputsNorm(self)
        self.outputs = _OutputsNorm(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise L2 norm of the field elementary data.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "norm")

#internal name: sqrt_fc
#scripting name: sqrt_fc
class _InputsSqrtFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(sqrt_fc._spec().inputs, op)
        self.fields_container = Input(sqrt_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsSqrtFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(sqrt_fc._spec().outputs, op)
        self.fields_container = Output(sqrt_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class sqrt_fc(Operator):
    """Computes element-wise sqrt(field1).

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.sqrt_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="sqrt_fc", config = config, server = server)
        self.inputs = _InputsSqrtFc(self)
        self.outputs = _OutputsSqrtFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise sqrt(field1).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sqrt_fc")

#internal name: norm_fc
#scripting name: norm_fc
class _InputsNormFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(norm_fc._spec().inputs, op)
        self.fields_container = Input(norm_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsNormFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(norm_fc._spec().outputs, op)
        self.fields_container = Output(norm_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class norm_fc(Operator):
    """Computes the element-wise L2 norm of the field elementary data. This process is applied on eah field of the input fields container.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.norm_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="norm_fc", config = config, server = server)
        self.inputs = _InputsNormFc(self)
        self.outputs = _OutputsNormFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise L2 norm of the field elementary data. This process is applied on eah field of the input fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "norm_fc")

#internal name: component_wise_divide
#scripting name: component_wise_divide
class _InputsComponentWiseDivide(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(component_wise_divide._spec().inputs, op)
        self.fieldA = Input(component_wise_divide._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(component_wise_divide._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)

class _OutputsComponentWiseDivide(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(component_wise_divide._spec().outputs, op)
        self.field = Output(component_wise_divide._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class component_wise_divide(Operator):
    """Computes component-wise fraction between two fields of same dimensionality. If one field's scoping has overall location, then these field's values are applied on the entire other field.

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.component_wise_divide()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="component_wise_divide", config = config, server = server)
        self.inputs = _InputsComponentWiseDivide(self)
        self.outputs = _OutputsComponentWiseDivide(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes component-wise fraction between two fields of same dimensionality. If one field's scoping has overall location, then these field's values are applied on the entire other field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "component_wise_divide")

#internal name: component_wise_divide_fc
#scripting name: component_wise_divide_fc
class _InputsComponentWiseDivideFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(component_wise_divide_fc._spec().inputs, op)
        self.fields_containerA = Input(component_wise_divide_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_containerA)
        self.fields_containerB = Input(component_wise_divide_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fields_containerB)

class _OutputsComponentWiseDivideFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(component_wise_divide_fc._spec().outputs, op)
        self.fields_container = Output(component_wise_divide_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class component_wise_divide_fc(Operator):
    """For every two fields with the same label space (from the two input fields containers), computes component-wise fraction between two fields of same dimensionality. If one field's scoping has overall location, then these field's values are applied on the entire other field.

      available inputs:
         fields_containerA (FieldsContainer)
         fields_containerB (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.component_wise_divide_fc()

      >>> # Make input connections
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_containerA=None, fields_containerB=None, config=None, server=None):
        super().__init__(name="component_wise_divide_fc", config = config, server = server)
        self.inputs = _InputsComponentWiseDivideFc(self)
        self.outputs = _OutputsComponentWiseDivideFc(self)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)

    @staticmethod
    def _spec():
        spec = Specification(description="""For every two fields with the same label space (from the two input fields containers), computes component-wise fraction between two fields of same dimensionality. If one field's scoping has overall location, then these field's values are applied on the entire other field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "component_wise_divide_fc")

#internal name: kronecker_prod
#scripting name: kronecker_prod
class _InputsKroneckerProd(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(kronecker_prod._spec().inputs, op)
        self.fieldA = Input(kronecker_prod._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(kronecker_prod._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)

class _OutputsKroneckerProd(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(kronecker_prod._spec().outputs, op)
        self.field = Output(kronecker_prod._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class kronecker_prod(Operator):
    """Computes element-wise Kronecker product between two tensor fields.

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.kronecker_prod()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="kronecker_prod", config = config, server = server)
        self.inputs = _InputsKroneckerProd(self)
        self.outputs = _OutputsKroneckerProd(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise Kronecker product between two tensor fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "kronecker_prod")

#internal name: realP_part
#scripting name: real_part
class _InputsRealPart(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(real_part._spec().inputs, op)
        self.fields_container = Input(real_part._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsRealPart(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(real_part._spec().outputs, op)
        self.fields_container = Output(real_part._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class real_part(Operator):
    """Extracts element-wise real part of field containers containing complex fields.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.real_part()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="realP_part", config = config, server = server)
        self.inputs = _InputsRealPart(self)
        self.outputs = _OutputsRealPart(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts element-wise real part of field containers containing complex fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "realP_part")

#internal name: conjugate
#scripting name: conjugate
class _InputsConjugate(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(conjugate._spec().inputs, op)
        self.fields_container = Input(conjugate._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsConjugate(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(conjugate._spec().outputs, op)
        self.fields_container = Output(conjugate._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class conjugate(Operator):
    """Computes element-wise conjugate of field containers containing complex fields.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.conjugate()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="conjugate", config = config, server = server)
        self.inputs = _InputsConjugate(self)
        self.outputs = _OutputsConjugate(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise conjugate of field containers containing complex fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "conjugate")

#internal name: img_part
#scripting name: img_part
class _InputsImgPart(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(img_part._spec().inputs, op)
        self.fields_container = Input(img_part._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsImgPart(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(img_part._spec().outputs, op)
        self.fields_container = Output(img_part._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class img_part(Operator):
    """Extracts element-wise imaginary part of field containers containing complex fields.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.img_part()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="img_part", config = config, server = server)
        self.inputs = _InputsImgPart(self)
        self.outputs = _OutputsImgPart(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts element-wise imaginary part of field containers containing complex fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "img_part")

#internal name: amplitude
#scripting name: amplitude
class _InputsAmplitude(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(amplitude._spec().inputs, op)
        self.fieldA = Input(amplitude._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(amplitude._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)

class _OutputsAmplitude(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(amplitude._spec().outputs, op)
        self.field = Output(amplitude._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class amplitude(Operator):
    """Computes amplitude of a real and an imaginary field.

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.amplitude()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="amplitude", config = config, server = server)
        self.inputs = _InputsAmplitude(self)
        self.outputs = _OutputsAmplitude(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes amplitude of a real and an imaginary field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "amplitude")

#internal name: cplx_add
#scripting name: cplx_add
class _InputsCplxAdd(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cplx_add._spec().inputs, op)
        self.fields_containerA = Input(cplx_add._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_containerA)
        self.fields_containerB = Input(cplx_add._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fields_containerB)

class _OutputsCplxAdd(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cplx_add._spec().outputs, op)
        self.fields_container = Output(cplx_add._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class cplx_add(Operator):
    """Computes addition between two field containers containing complex fields.

      available inputs:
         fields_containerA (FieldsContainer)
         fields_containerB (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.cplx_add()

      >>> # Make input connections
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_containerA=None, fields_containerB=None, config=None, server=None):
        super().__init__(name="cplx_add", config = config, server = server)
        self.inputs = _InputsCplxAdd(self)
        self.outputs = _OutputsCplxAdd(self)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes addition between two field containers containing complex fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cplx_add")

#internal name: cplx_dot
#scripting name: cplx_dot
class _InputsCplxDot(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cplx_dot._spec().inputs, op)
        self.fields_containerA = Input(cplx_dot._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_containerA)
        self.fields_containerB = Input(cplx_dot._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fields_containerB)

class _OutputsCplxDot(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cplx_dot._spec().outputs, op)
        self.fields_container = Output(cplx_dot._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class cplx_dot(Operator):
    """Computes product between two field containers containing complex fields.

      available inputs:
         fields_containerA (FieldsContainer)
         fields_containerB (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.cplx_dot()

      >>> # Make input connections
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_containerA=None, fields_containerB=None, config=None, server=None):
        super().__init__(name="cplx_dot", config = config, server = server)
        self.inputs = _InputsCplxDot(self)
        self.outputs = _OutputsCplxDot(self)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes product between two field containers containing complex fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cplx_dot")

#internal name: cplx_divide
#scripting name: cplx_divide
class _InputsCplxDivide(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cplx_divide._spec().inputs, op)
        self.fields_containerA = Input(cplx_divide._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_containerA)
        self.fields_containerB = Input(cplx_divide._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fields_containerB)

class _OutputsCplxDivide(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cplx_divide._spec().outputs, op)
        self.fields_container = Output(cplx_divide._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class cplx_divide(Operator):
    """Computes division between two field containers containing complex fields.

      available inputs:
         fields_containerA (FieldsContainer)
         fields_containerB (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.cplx_divide()

      >>> # Make input connections
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_containerA=None, fields_containerB=None, config=None, server=None):
        super().__init__(name="cplx_divide", config = config, server = server)
        self.inputs = _InputsCplxDivide(self)
        self.outputs = _OutputsCplxDivide(self)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes division between two field containers containing complex fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cplx_divide")

#internal name: dot
#scripting name: dot
class _InputsDot(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(dot._spec().inputs, op)
        self.fieldA = Input(dot._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(dot._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)

class _OutputsDot(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(dot._spec().outputs, op)
        self.field = Output(dot._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class dot(Operator):
    """Computes element-wise dot product between two vector fields. If one field's scoping has 'overall' location, then this field's values are applied on the entire other field.

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.dot()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="dot", config = config, server = server)
        self.inputs = _InputsDot(self)
        self.outputs = _OutputsDot(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise dot product between two vector fields. If one field's scoping has 'overall' location, then this field's values are applied on the entire other field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "dot")

#internal name: cplx_derive
#scripting name: cplx_derive
class _InputsCplxDerive(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cplx_derive._spec().inputs, op)
        self.fields_container = Input(cplx_derive._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsCplxDerive(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cplx_derive._spec().outputs, op)
        self.fields_container = Output(cplx_derive._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class cplx_derive(Operator):
    """Derive field containers containing complex fields.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.cplx_derive()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="cplx_derive", config = config, server = server)
        self.inputs = _InputsCplxDerive(self)
        self.outputs = _OutputsCplxDerive(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Derive field containers containing complex fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cplx_derive")

#internal name: polar_to_cplx
#scripting name: polar_to_cplx
class _InputsPolarToCplx(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(polar_to_cplx._spec().inputs, op)
        self.fields_container = Input(polar_to_cplx._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsPolarToCplx(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(polar_to_cplx._spec().outputs, op)
        self.fields_container = Output(polar_to_cplx._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class polar_to_cplx(Operator):
    """Convert complex number from polar form to complex.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.polar_to_cplx()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="polar_to_cplx", config = config, server = server)
        self.inputs = _InputsPolarToCplx(self)
        self.outputs = _OutputsPolarToCplx(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Convert complex number from polar form to complex.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "polar_to_cplx")

#internal name: amplitude_fc
#scripting name: amplitude_fc
class _InputsAmplitudeFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(amplitude_fc._spec().inputs, op)
        self.fields_container = Input(amplitude_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsAmplitudeFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(amplitude_fc._spec().outputs, op)
        self.fields_container = Output(amplitude_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class amplitude_fc(Operator):
    """Computes amplitude of a real and an imaginary fields.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.amplitude_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="amplitude_fc", config = config, server = server)
        self.inputs = _InputsAmplitudeFc(self)
        self.outputs = _OutputsAmplitudeFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes amplitude of a real and an imaginary fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "amplitude_fc")

#internal name: scale_by_field
#scripting name: scale_by_field
class _InputsScaleByField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(scale_by_field._spec().inputs, op)
        self.fieldA = Input(scale_by_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(scale_by_field._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)

class _OutputsScaleByField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(scale_by_field._spec().outputs, op)
        self.field = Output(scale_by_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class scale_by_field(Operator):
    """Scales a field (in 0) by a scalar field (in 1). If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.scale_by_field()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="scale_by_field", config = config, server = server)
        self.inputs = _InputsScaleByField(self)
        self.outputs = _OutputsScaleByField(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Scales a field (in 0) by a scalar field (in 1). If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scale_by_field")

#internal name: generalized_inner_product_fc
#scripting name: generalized_inner_product_fc
class _InputsGeneralizedInnerProductFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(generalized_inner_product_fc._spec().inputs, op)
        self.field_or_fields_container_A = Input(generalized_inner_product_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field_or_fields_container_A)
        self.field_or_fields_container_B = Input(generalized_inner_product_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.field_or_fields_container_B)

class _OutputsGeneralizedInnerProductFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(generalized_inner_product_fc._spec().outputs, op)
        self.fields_container = Output(generalized_inner_product_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class generalized_inner_product_fc(Operator):
    """Computes a general notion of inner product between two fields of possibly different dimensionality.

      available inputs:
         field_or_fields_container_A (FieldsContainer)
         field_or_fields_container_B (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.generalized_inner_product_fc()

      >>> # Make input connections
      >>> my_field_or_fields_container_A = dpf.FieldsContainer()
      >>> op.inputs.field_or_fields_container_A.connect(my_field_or_fields_container_A)
      >>> my_field_or_fields_container_B = dpf.FieldsContainer()
      >>> op.inputs.field_or_fields_container_B.connect(my_field_or_fields_container_B)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field_or_fields_container_A=None, field_or_fields_container_B=None, config=None, server=None):
        super().__init__(name="generalized_inner_product_fc", config = config, server = server)
        self.inputs = _InputsGeneralizedInnerProductFc(self)
        self.outputs = _OutputsGeneralizedInnerProductFc(self)
        if field_or_fields_container_A !=None:
            self.inputs.field_or_fields_container_A.connect(field_or_fields_container_A)
        if field_or_fields_container_B !=None:
            self.inputs.field_or_fields_container_B.connect(field_or_fields_container_B)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes a general notion of inner product between two fields of possibly different dimensionality.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field_or_fields_container_A", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "field_or_fields_container_B", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "generalized_inner_product_fc")

#internal name: phase
#scripting name: phase
class _InputsPhase(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(phase._spec().inputs, op)
        self.fieldA = Input(phase._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(phase._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)

class _OutputsPhase(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(phase._spec().outputs, op)
        self.field = Output(phase._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class phase(Operator):
    """Computes the phase (in rad) between a real and an imaginary field.

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.phase()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="phase", config = config, server = server)
        self.inputs = _InputsPhase(self)
        self.outputs = _OutputsPhase(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the phase (in rad) between a real and an imaginary field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "phase")

#internal name: scale_by_field_fc
#scripting name: scale_by_field_fc
class _InputsScaleByFieldFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(scale_by_field_fc._spec().inputs, op)
        self.field_or_fields_container_A = Input(scale_by_field_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field_or_fields_container_A)
        self.field_or_fields_container_B = Input(scale_by_field_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.field_or_fields_container_B)

class _OutputsScaleByFieldFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(scale_by_field_fc._spec().outputs, op)
        self.fields_container = Output(scale_by_field_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class scale_by_field_fc(Operator):
    """Scales a field (in 0) by a scalar field (in 1). If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.

      available inputs:
         field_or_fields_container_A (FieldsContainer)
         field_or_fields_container_B (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.scale_by_field_fc()

      >>> # Make input connections
      >>> my_field_or_fields_container_A = dpf.FieldsContainer()
      >>> op.inputs.field_or_fields_container_A.connect(my_field_or_fields_container_A)
      >>> my_field_or_fields_container_B = dpf.FieldsContainer()
      >>> op.inputs.field_or_fields_container_B.connect(my_field_or_fields_container_B)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field_or_fields_container_A=None, field_or_fields_container_B=None, config=None, server=None):
        super().__init__(name="scale_by_field_fc", config = config, server = server)
        self.inputs = _InputsScaleByFieldFc(self)
        self.outputs = _OutputsScaleByFieldFc(self)
        if field_or_fields_container_A !=None:
            self.inputs.field_or_fields_container_A.connect(field_or_fields_container_A)
        if field_or_fields_container_B !=None:
            self.inputs.field_or_fields_container_B.connect(field_or_fields_container_B)

    @staticmethod
    def _spec():
        spec = Specification(description="""Scales a field (in 0) by a scalar field (in 1). If one field's scoping has 'overall' location, then these field's values are applied on the entire other field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field_or_fields_container_A", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "field_or_fields_container_B", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scale_by_field_fc")

#internal name: phase_fc
#scripting name: phase_fc
class _InputsPhaseFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(phase_fc._spec().inputs, op)
        self.fields_container = Input(phase_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsPhaseFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(phase_fc._spec().outputs, op)
        self.fields_container = Output(phase_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class phase_fc(Operator):
    """Computes phase (in rad) between real and imaginary fields.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.phase_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="phase_fc", config = config, server = server)
        self.inputs = _InputsPhaseFc(self)
        self.outputs = _OutputsPhaseFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes phase (in rad) between real and imaginary fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "phase_fc")

#internal name: modulus
#scripting name: modulus
class _InputsModulus(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(modulus._spec().inputs, op)
        self.fields_container = Input(modulus._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsModulus(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(modulus._spec().outputs, op)
        self.fields_container = Output(modulus._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class modulus(Operator):
    """Computes element-wise modulus of field containers containing complex fields.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.modulus()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="modulus", config = config, server = server)
        self.inputs = _InputsModulus(self)
        self.outputs = _OutputsModulus(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise modulus of field containers containing complex fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "modulus")

#internal name: accumulate_fc
#scripting name: accumulate_fc
class _InputsAccumulateFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(accumulate_fc._spec().inputs, op)
        self.fields_container = Input(accumulate_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsAccumulateFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(accumulate_fc._spec().outputs, op)
        self.fields_container = Output(accumulate_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class accumulate_fc(Operator):
    """Sum all the elementary data of a field to get one elementary data at the end.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.accumulate_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="accumulate_fc", config = config, server = server)
        self.inputs = _InputsAccumulateFc(self)
        self.outputs = _OutputsAccumulateFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Sum all the elementary data of a field to get one elementary data at the end.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "accumulate_fc")

#internal name: generalized_inner_product
#scripting name: generalized_inner_product
class _InputsGeneralizedInnerProduct(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(generalized_inner_product._spec().inputs, op)
        self.fieldA = Input(generalized_inner_product._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(generalized_inner_product._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)

class _OutputsGeneralizedInnerProduct(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(generalized_inner_product._spec().outputs, op)
        self.field = Output(generalized_inner_product._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class generalized_inner_product(Operator):
    """Computes a general notion of inner product between two fields of possibly different dimensionality.

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.generalized_inner_product()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="generalized_inner_product", config = config, server = server)
        self.inputs = _InputsGeneralizedInnerProduct(self)
        self.outputs = _OutputsGeneralizedInnerProduct(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes a general notion of inner product between two fields of possibly different dimensionality.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "generalized_inner_product")

#internal name: native::overall_dot
#scripting name: overall_dot
class _InputsOverallDot(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(overall_dot._spec().inputs, op)
        self.FieldA = Input(overall_dot._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.FieldA)
        self.FieldB = Input(overall_dot._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.FieldB)

class _OutputsOverallDot(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(overall_dot._spec().outputs, op)
        self.field = Output(overall_dot._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class overall_dot(Operator):
    """Compute a sdot product between two fields and return a scalar.

      available inputs:
         FieldA (Field)
         FieldB (Field)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.overall_dot()

      >>> # Make input connections
      >>> my_FieldA = dpf.Field()
      >>> op.inputs.FieldA.connect(my_FieldA)
      >>> my_FieldB = dpf.Field()
      >>> op.inputs.FieldB.connect(my_FieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, FieldA=None, FieldB=None, config=None, server=None):
        super().__init__(name="native::overall_dot", config = config, server = server)
        self.inputs = _InputsOverallDot(self)
        self.outputs = _OutputsOverallDot(self)
        if FieldA !=None:
            self.inputs.FieldA.connect(FieldA)
        if FieldB !=None:
            self.inputs.FieldB.connect(FieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute a sdot product between two fields and return a scalar.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "FieldA", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "FieldB", type_names=["field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""Field defined on over-all location, contains a unique scalar value""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "native::overall_dot")

#internal name: invert
#scripting name: invert
class _InputsInvert(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(invert._spec().inputs, op)
        self.field = Input(invert._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsInvert(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(invert._spec().outputs, op)
        self.field = Output(invert._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class invert(Operator):
    """Compute the element-wise, component-wise, inverse of a field (1./x)

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.invert()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="invert", config = config, server = server)
        self.inputs = _InputsInvert(self)
        self.outputs = _OutputsInvert(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the element-wise, component-wise, inverse of a field (1./x)""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "invert")

#internal name: dot_tensor
#scripting name: dot_tensor
class _InputsDotTensor(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(dot_tensor._spec().inputs, op)
        self.fieldA = Input(dot_tensor._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fieldA)
        self.fieldB = Input(dot_tensor._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.fieldB)

class _OutputsDotTensor(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(dot_tensor._spec().outputs, op)
        self.field = Output(dot_tensor._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class dot_tensor(Operator):
    """Computes element-wise dot product between two tensor fields.

      available inputs:
         fieldA (Field, FieldsContainer)
         fieldB (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.dot_tensor()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="dot_tensor", config = config, server = server)
        self.inputs = _InputsDotTensor(self)
        self.outputs = _OutputsDotTensor(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes element-wise dot product between two tensor fields.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "dot_tensor")

#internal name: average_over_label_fc
#scripting name: average_over_label_fc
class _InputsAverageOverLabelFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(average_over_label_fc._spec().inputs, op)
        self.fields_container = Input(average_over_label_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsAverageOverLabelFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(average_over_label_fc._spec().outputs, op)
        self.field = Output(average_over_label_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class average_over_label_fc(Operator):
    """Compute the component-wise average over all the fields having the same id for the label set in input in the fields container. This computation can be incremental, if the input fields container is connected and the operator is ran several time, the output field will be on all the inputs connected

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.average_over_label_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="average_over_label_fc", config = config, server = server)
        self.inputs = _InputsAverageOverLabelFc(self)
        self.outputs = _OutputsAverageOverLabelFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the component-wise average over all the fields having the same id for the label set in input in the fields container. This computation can be incremental, if the input fields container is connected and the operator is ran several time, the output field will be on all the inputs connected""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "average_over_label_fc")

#internal name: accumulate_over_label_fc
#scripting name: accumulate_over_label_fc
class _InputsAccumulateOverLabelFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(accumulate_over_label_fc._spec().inputs, op)
        self.fields_container = Input(accumulate_over_label_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsAccumulateOverLabelFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(accumulate_over_label_fc._spec().outputs, op)
        self.field = Output(accumulate_over_label_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class accumulate_over_label_fc(Operator):
    """Compute the component-wise sum over all the fields having the same id for the label set in input in the fields container. This computation can be incremental, if the input fields container is connected and the operator is ran several time, the output field will be on all the inputs connected

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.accumulate_over_label_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="accumulate_over_label_fc", config = config, server = server)
        self.inputs = _InputsAccumulateOverLabelFc(self)
        self.outputs = _OutputsAccumulateOverLabelFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the component-wise sum over all the fields having the same id for the label set in input in the fields container. This computation can be incremental, if the input fields container is connected and the operator is ran several time, the output field will be on all the inputs connected""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "accumulate_over_label_fc")

#internal name: accumulate_level_over_label_fc
#scripting name: accumulate_level_over_label_fc
class _InputsAccumulateLevelOverLabelFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(accumulate_level_over_label_fc._spec().inputs, op)
        self.fields_container = Input(accumulate_level_over_label_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsAccumulateLevelOverLabelFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(accumulate_level_over_label_fc._spec().outputs, op)
        self.field = Output(accumulate_level_over_label_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class accumulate_level_over_label_fc(Operator):
    """Compute the component-wise sum over all the fields having the same id for the label set in input in the fields container and apply 10.0xlog10(data/10xx-12) on the result. This computation can be incremental, if the input fields container is connected and the operator is ran several time, the output field will be on all the inputs connected

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.accumulate_level_over_label_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="accumulate_level_over_label_fc", config = config, server = server)
        self.inputs = _InputsAccumulateLevelOverLabelFc(self)
        self.outputs = _OutputsAccumulateLevelOverLabelFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the component-wise sum over all the fields having the same id for the label set in input in the fields container and apply 10.0xlog10(data/10xx-12) on the result. This computation can be incremental, if the input fields container is connected and the operator is ran several time, the output field will be on all the inputs connected""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "accumulate_level_over_label_fc")

"""
Math Operators
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "math" category
"""

#internal name: expansion::modal_superposition
#scripting name: modal_superposition
class _InputsModalSuperposition(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(modal_superposition._spec().inputs, op)
        self.modal_basis = Input(modal_superposition._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.modal_basis)
        self.solution_in_modal_space = Input(modal_superposition._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.solution_in_modal_space)
        self.time_scoping = Input(modal_superposition._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.time_scoping)
        self.mesh_scoping = Input(modal_superposition._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.mesh_scoping)

class _OutputsModalSuperposition(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(modal_superposition._spec().outputs, op)
        self.fields_container = Output(modal_superposition._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class modal_superposition(Operator):
    """Compute the solution in the time/frequency space from a modal solution by multiplying a modal basis (in 0) by the solution in this modal space (coefficients for each mode for each time/frequency) (in 1).

      available inputs:
         modal_basis (FieldsContainer)
         solution_in_modal_space (FieldsContainer)
         time_scoping (Scoping, list) (optional)
         mesh_scoping (Scoping, ScopingsContainer) (optional)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.modal_superposition()

      >>> # Make input connections
      >>> my_modal_basis = dpf.FieldsContainer()
      >>> op.inputs.modal_basis.connect(my_modal_basis)
      >>> my_solution_in_modal_space = dpf.FieldsContainer()
      >>> op.inputs.solution_in_modal_space.connect(my_solution_in_modal_space)
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, modal_basis=None, solution_in_modal_space=None, time_scoping=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="expansion::modal_superposition", config = config, server = server)
        self.inputs = _InputsModalSuperposition(self)
        self.outputs = _OutputsModalSuperposition(self)
        if modal_basis !=None:
            self.inputs.modal_basis.connect(modal_basis)
        if solution_in_modal_space !=None:
            self.inputs.solution_in_modal_space.connect(solution_in_modal_space)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the solution in the time/frequency space from a modal solution by multiplying a modal basis (in 0) by the solution in this modal space (coefficients for each mode for each time/frequency) (in 1).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "modal_basis", type_names=["fields_container"], optional=False, document="""one field by mode with each field representing a mode shape on nodes or elements"""), 
                                 1 : PinSpecification(name = "solution_in_modal_space", type_names=["fields_container"], optional=False, document="""one field by time/frequency with each field having a ponderating coefficient for each mode of the modal_basis pin"""), 
                                 3 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document="""this input allows to compute the result on a subset of the time frequency domain defined in the solution_in_modal_space fields container"""), 
                                 4 : PinSpecification(name = "mesh_scoping", type_names=["scoping","scopings_container"], optional=True, document="""this input allows to compute the result on a subset of the space domain defined in the modal_basis fields container""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "expansion::modal_superposition")

