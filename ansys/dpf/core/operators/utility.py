"""
Utility Operators
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native.dll plugin, from "utility" category
"""

#internal name: InjectToFieldContainer
#scripting name: field_to_fc
class _InputsFieldToFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(field_to_fc._spec().inputs, op)
        self.field = Input(field_to_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsFieldToFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(field_to_fc._spec().outputs, op)
        self.fields_container = Output(field_to_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class field_to_fc(Operator):
    """Create a field container containing the field in input.

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.utility.field_to_fc()

    """
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="InjectToFieldContainer", config = config, server = server)
        self.inputs = _InputsFieldToFc(self)
        self.outputs = _OutputsFieldToFc(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create a field container containing the field in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""if a fields container is set in input, it is pass on as output.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "InjectToFieldContainer")

#internal name: html_doc
#scripting name: html_doc
class _InputsHtmlDoc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(html_doc._spec().inputs, op)
        self.output_path = Input(html_doc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.output_path)

class _OutputsHtmlDoc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(html_doc._spec().outputs, op)
        pass 

class html_doc(Operator):
    """Create dpf's html documentation. Only on windows, use deprecated doc for linux

      available inputs:
         output_path (str) (optional)

      available outputs:


      Examples
      --------
      >>> op = operators.utility.html_doc()

    """
    def __init__(self, output_path=None, config=None, server=None):
        super().__init__(name="html_doc", config = config, server = server)
        self.inputs = _InputsHtmlDoc(self)
        self.outputs = _OutputsHtmlDoc(self)
        if output_path !=None:
            self.inputs.output_path.connect(output_path)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create dpf's html documentation. Only on windows, use deprecated doc for linux""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "output_path", type_names=["string"], optional=True, document="""default is {working directory}/dataProcessingDoc.html""")},
                             map_output_pin_spec={
})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "html_doc")

#internal name: make_unit
#scripting name: unitary_field
class _InputsUnitaryField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(unitary_field._spec().inputs, op)
        self.field = Input(unitary_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsUnitaryField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(unitary_field._spec().outputs, op)
        self.field = Output(unitary_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class unitary_field(Operator):
    """Take a field and returns an other field of scalars on the same location and scoping as the input field

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.utility.unitary_field()

    """
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="make_unit", config = config, server = server)
        self.inputs = _InputsUnitaryField(self)
        self.outputs = _OutputsUnitaryField(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a field and returns an other field of scalars on the same location and scoping as the input field""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "make_unit")

#internal name: ExtractFromFC
#scripting name: extract_field
class _InputsExtractField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(extract_field._spec().inputs, op)
        self.fields_container = Input(extract_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.indeces = Input(extract_field._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.indeces)

class _OutputsExtractField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(extract_field._spec().outputs, op)
        self.field = Output(extract_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class extract_field(Operator):
    """Extract the fields at the indeces defined in the vector (in 1) form the fields container (in:0).

      available inputs:
         fields_container (Field, FieldsContainer)
         indeces (list) (optional)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.utility.extract_field()

    """
    def __init__(self, fields_container=None, indeces=None, config=None, server=None):
        super().__init__(name="ExtractFromFC", config = config, server = server)
        self.inputs = _InputsExtractField(self)
        self.outputs = _OutputsExtractField(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if indeces !=None:
            self.inputs.indeces.connect(indeces)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extract the fields at the indeces defined in the vector (in 1) form the fields container (in:0).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["field","fields_container"], optional=False, document="""if a field is in input, it is passed on as output"""), 
                                 1 : PinSpecification(name = "indeces", type_names=["vector<int32>"], optional=True, document="""default is the first field""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ExtractFromFC")

#internal name: BindSupport
#scripting name: bind_support
class _InputsBindSupport(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(bind_support._spec().inputs, op)
        self.field = Input(bind_support._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.support = Input(bind_support._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.support)

class _OutputsBindSupport(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(bind_support._spec().outputs, op)
        self.field = Output(bind_support._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class bind_support(Operator):
    """Tie a support to a field.

      available inputs:
         field (Field, FieldsContainer)
         support (MeshedRegion, AbstractFieldSupport)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.utility.bind_support()

    """
    def __init__(self, field=None, support=None, config=None, server=None):
        super().__init__(name="BindSupport", config = config, server = server)
        self.inputs = _InputsBindSupport(self)
        self.outputs = _OutputsBindSupport(self)
        if field !=None:
            self.inputs.field.connect(field)
        if support !=None:
            self.inputs.support.connect(support)

    @staticmethod
    def _spec():
        spec = Specification(description="""Tie a support to a field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "support", type_names=["abstract_meshed_region","abstract_field_support"], optional=False, document="""meshed region or a support of the field""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "BindSupport")

#internal name: fieldify
#scripting name: scalars_to_field
class _InputsScalarsToField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(scalars_to_field._spec().inputs, op)
        self.double_or_vector_double = Input(scalars_to_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.double_or_vector_double)

class _OutputsScalarsToField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(scalars_to_field._spec().outputs, op)
        self.field = Output(scalars_to_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class scalars_to_field(Operator):
    """take a double or a vector of double and transform it in a one entity field of location "numeric".

      available inputs:
         double_or_vector_double (float, list)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.utility.scalars_to_field()

    """
    def __init__(self, double_or_vector_double=None, config=None, server=None):
        super().__init__(name="fieldify", config = config, server = server)
        self.inputs = _InputsScalarsToField(self)
        self.outputs = _OutputsScalarsToField(self)
        if double_or_vector_double !=None:
            self.inputs.double_or_vector_double.connect(double_or_vector_double)

    @staticmethod
    def _spec():
        spec = Specification(description="""take a double or a vector of double and transform it in a one entity field of location "numeric".""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "double_or_vector_double", type_names=["double","vector<double>"], optional=False, document="""double or vector of double""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "fieldify")

#internal name: change_location
#scripting name: change_location
class _InputsChangeLocation(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(change_location._spec().inputs, op)
        self.field = Input(change_location._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.new_location = Input(change_location._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.new_location)

class _OutputsChangeLocation(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(change_location._spec().outputs, op)
        self.field = Output(change_location._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class change_location(Operator):
    """change the location of a field.

      available inputs:
         field (Field)
         new_location (str)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.utility.change_location()

    """
    def __init__(self, field=None, new_location=None, config=None, server=None):
        super().__init__(name="change_location", config = config, server = server)
        self.inputs = _InputsChangeLocation(self)
        self.outputs = _OutputsChangeLocation(self)
        if field !=None:
            self.inputs.field.connect(field)
        if new_location !=None:
            self.inputs.new_location.connect(new_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""change the location of a field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "new_location", type_names=["string"], optional=False, document="""new location of the output field ex 'Nodal', 'ElementalNodal', 'Elemental'...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "change_location")

#internal name: strain_from_voigt
#scripting name: strain_from_voigt
class _InputsStrainFromVoigt(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(strain_from_voigt._spec().inputs, op)
        self.field = Input(strain_from_voigt._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsStrainFromVoigt(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(strain_from_voigt._spec().outputs, op)
        self.field = Output(strain_from_voigt._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class strain_from_voigt(Operator):
    """Put strain field from Voigt notation to standard format.

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.utility.strain_from_voigt()

    """
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="strain_from_voigt", config = config, server = server)
        self.inputs = _InputsStrainFromVoigt(self)
        self.outputs = _OutputsStrainFromVoigt(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Put strain field from Voigt notation to standard format.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "strain_from_voigt")

#internal name: field::set_property
#scripting name: set_property
class _InputsSetProperty(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(set_property._spec().inputs, op)
        self.field = Input(set_property._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)
        self.property_name = Input(set_property._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.property_name)
        self.property_value = Input(set_property._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.property_value)

class _OutputsSetProperty(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(set_property._spec().outputs, op)
        self.field_as_field = Output( _modify_output_spec_with_one_type(set_property._spec().output_pin(0), "field"), 0, op) 
        self._outputs.append(self.field_as_field)
        self.field_as_fields_container = Output( _modify_output_spec_with_one_type(set_property._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.field_as_fields_container)

class set_property(Operator):
    """Set a property to an input field/field container

      available inputs:
         field (Field, FieldsContainer)
         property_name (str)
         property_value (str, int, float)

      available outputs:
         field (Field ,FieldsContainer)

      Examples
      --------
      >>> op = operators.utility.set_property()

    """
    def __init__(self, field=None, property_name=None, property_value=None, config=None, server=None):
        super().__init__(name="field::set_property", config = config, server = server)
        self.inputs = _InputsSetProperty(self)
        self.outputs = _OutputsSetProperty(self)
        if field !=None:
            self.inputs.field.connect(field)
        if property_name !=None:
            self.inputs.property_name.connect(property_name)
        if property_value !=None:
            self.inputs.property_value.connect(property_value)

    @staticmethod
    def _spec():
        spec = Specification(description="""Set a property to an input field/field container""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "property_name", type_names=["string"], optional=False, document="""Property to set"""), 
                                 2 : PinSpecification(name = "property_value", type_names=["string","int32","double"], optional=False, document="""Property to set""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "field::set_property")

#internal name: forward_field
#scripting name: forward_field
class _InputsForwardField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(forward_field._spec().inputs, op)
        self.field = Input(forward_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsForwardField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(forward_field._spec().outputs, op)
        self.field = Output(forward_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class forward_field(Operator):
    """Return the input field or fields container.

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.utility.forward_field()

    """
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="forward_field", config = config, server = server)
        self.inputs = _InputsForwardField(self)
        self.outputs = _OutputsForwardField(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Return the input field or fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "forward_field")

#internal name: forward_fc
#scripting name: forward_fields_container
class _InputsForwardFieldsContainer(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(forward_fields_container._spec().inputs, op)
        self.fields = Input(forward_fields_container._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields)

class _OutputsForwardFieldsContainer(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(forward_fields_container._spec().outputs, op)
        self.fields_container = Output(forward_fields_container._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class forward_fields_container(Operator):
    """Return the input field or fields container.

      available inputs:
         fields (FieldsContainer, Field)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.utility.forward_fields_container()

    """
    def __init__(self, fields=None, config=None, server=None):
        super().__init__(name="forward_fc", config = config, server = server)
        self.inputs = _InputsForwardFieldsContainer(self)
        self.outputs = _OutputsForwardFieldsContainer(self)
        if fields !=None:
            self.inputs.fields.connect(fields)

    @staticmethod
    def _spec():
        spec = Specification(description="""Return the input field or fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "forward_fc")

#internal name: forward_meshes_container
#scripting name: forward_meshes_container
class _InputsForwardMeshesContainer(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(forward_meshes_container._spec().inputs, op)
        self.meshes = Input(forward_meshes_container._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.meshes)
        self.default_label = Input(forward_meshes_container._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.default_label)

class _OutputsForwardMeshesContainer(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(forward_meshes_container._spec().outputs, op)
        self.meshes_container = Output(forward_meshes_container._spec().output_pin(0), 0, op) 
        self._outputs.append(self.meshes_container)

class forward_meshes_container(Operator):
    """Return the input mesh or meshes container into a meshes container.

      available inputs:
         meshes (MeshesContainer, MeshedRegion)
         default_label (str) (optional)

      available outputs:
         meshes_container (MeshesContainer)

      Examples
      --------
      >>> op = operators.utility.forward_meshes_container()

    """
    def __init__(self, meshes=None, default_label=None, config=None, server=None):
        super().__init__(name="forward_meshes_container", config = config, server = server)
        self.inputs = _InputsForwardMeshesContainer(self)
        self.outputs = _OutputsForwardMeshesContainer(self)
        if meshes !=None:
            self.inputs.meshes.connect(meshes)
        if default_label !=None:
            self.inputs.default_label.connect(default_label)

    @staticmethod
    def _spec():
        spec = Specification(description="""Return the input mesh or meshes container into a meshes container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "meshes", type_names=["meshes_container","abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "default_label", type_names=["string"], optional=True, document="""this default label is used if a new meshes container needs to be created (default is unknown)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "meshes_container", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "forward_meshes_container")

#internal name: forward
#scripting name: forward
class _InputsForward(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(forward._spec().inputs, op)
        self.any = Input(forward._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.any)

class _OutputsForward(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(forward._spec().outputs, op)
        pass 

class forward(Operator):
    """Return all the inputs as outputs.

      available inputs:
         any (Any)

      available outputs:
         any ()

      Examples
      --------
      >>> op = operators.utility.forward()

    """
    def __init__(self, any=None, config=None, server=None):
        super().__init__(name="forward", config = config, server = server)
        self.inputs = _InputsForward(self)
        self.outputs = _OutputsForward(self)
        if any !=None:
            self.inputs.any.connect(any)

    @staticmethod
    def _spec():
        spec = Specification(description="""Return all the inputs as outputs.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "any", type_names=["any"], optional=False, document="""any type of input""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "any", type_names=[], optional=False, document="""same types as inputs""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "forward")

#internal name: text_parser
#scripting name: txt_file_to_dpf
class _InputsTxtFileToDpf(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(txt_file_to_dpf._spec().inputs, op)
        self.input_string = Input(txt_file_to_dpf._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.input_string)

class _OutputsTxtFileToDpf(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(txt_file_to_dpf._spec().outputs, op)
        pass 

class txt_file_to_dpf(Operator):
    """Take an input string and parse it into dataProcessing type.

      available inputs:
         input_string (str)

      available outputs:
         any_output1 ()
         any_output2 ()

      Examples
      --------
      >>> op = operators.utility.txt_file_to_dpf()

    """
    def __init__(self, input_string=None, config=None, server=None):
        super().__init__(name="text_parser", config = config, server = server)
        self.inputs = _InputsTxtFileToDpf(self)
        self.outputs = _OutputsTxtFileToDpf(self)
        if input_string !=None:
            self.inputs.input_string.connect(input_string)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take an input string and parse it into dataProcessing type.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "input_string", type_names=["string"], optional=False, document="""ex: 'double:1.0', 'int:1', 'vector<double>:1.0;1.0'""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "any_output", type_names=[], optional=False, document="""any output"""), 
                                 1 : PinSpecification(name = "any_output", type_names=[], optional=False, document="""any output""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "text_parser")

#internal name: BindSupportFC
#scripting name: bind_support_fc
class _InputsBindSupportFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(bind_support_fc._spec().inputs, op)
        self.fields_container = Input(bind_support_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.support = Input(bind_support_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.support)

class _OutputsBindSupportFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(bind_support_fc._spec().outputs, op)
        self.fields_container = Output(bind_support_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class bind_support_fc(Operator):
    """Tie a support to a fields container.

      available inputs:
         fields_container (FieldsContainer)
         support (MeshedRegion, AbstractFieldSupport)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.utility.bind_support_fc()

    """
    def __init__(self, fields_container=None, support=None, config=None, server=None):
        super().__init__(name="BindSupportFC", config = config, server = server)
        self.inputs = _InputsBindSupportFc(self)
        self.outputs = _OutputsBindSupportFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if support !=None:
            self.inputs.support.connect(support)

    @staticmethod
    def _spec():
        spec = Specification(description="""Tie a support to a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "support", type_names=["abstract_meshed_region","abstract_field_support"], optional=False, document="""meshed region or a support of the field""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "BindSupportFC")

#internal name: python_generator
#scripting name: python_generator
class _InputsPythonGenerator(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(python_generator._spec().inputs, op)
        self.dll_source_path = Input(python_generator._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.dll_source_path)
        self.output_path = Input(python_generator._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.output_path)
        self.overwrite_existing_files = Input(python_generator._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.overwrite_existing_files)

class _OutputsPythonGenerator(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(python_generator._spec().outputs, op)
        pass 

class python_generator(Operator):
    """Generates .py file with specifications for loaded plugin(s).

      available inputs:
         dll_source_path (str)
         output_path (str)
         overwrite_existing_files (bool) (optional)

      available outputs:


      Examples
      --------
      >>> op = operators.utility.python_generator()

    """
    def __init__(self, dll_source_path=None, output_path=None, overwrite_existing_files=None, config=None, server=None):
        super().__init__(name="python_generator", config = config, server = server)
        self.inputs = _InputsPythonGenerator(self)
        self.outputs = _OutputsPythonGenerator(self)
        if dll_source_path !=None:
            self.inputs.dll_source_path.connect(dll_source_path)
        if output_path !=None:
            self.inputs.output_path.connect(output_path)
        if overwrite_existing_files !=None:
            self.inputs.overwrite_existing_files.connect(overwrite_existing_files)

    @staticmethod
    def _spec():
        spec = Specification(description="""Generates .py file with specifications for loaded plugin(s).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "dll_source_path", type_names=["string"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "output_path", type_names=["string"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "overwrite_existing_files", type_names=["bool"], optional=True, document="""Default: true. Note that if several plugins are imported, the first one must be set at 'true', and the others at 'false'. One file that will overwrite is needed.""")},
                             map_output_pin_spec={
})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "python_generator")

"""
Utility Operators
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils.dll plugin, from "utility" category
"""

#internal name: change_shellLayers
#scripting name: change_shell_layers
class _InputsChangeShellLayers(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(change_shell_layers._spec().inputs, op)
        self.fields_container = Input(change_shell_layers._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)
        self.e_shell_layer = Input(change_shell_layers._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.e_shell_layer)

class _OutputsChangeShellLayers(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(change_shell_layers._spec().outputs, op)
        self.fields_container = Output(change_shell_layers._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class change_shell_layers(Operator):
    """Extract the expected shell layers from the input fields, if the fields contain only one layer then it returns the input fields

      available inputs:
         fields_container (FieldsContainer, Field)
         e_shell_layer (int)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.utility.change_shell_layers()

    """
    def __init__(self, fields_container=None, e_shell_layer=None, config=None, server=None):
        super().__init__(name="change_shellLayers", config = config, server = server)
        self.inputs = _InputsChangeShellLayers(self)
        self.outputs = _OutputsChangeShellLayers(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if e_shell_layer !=None:
            self.inputs.e_shell_layer.connect(e_shell_layer)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extract the expected shell layers from the input fields, if the fields contain only one layer then it returns the input fields""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container","field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "e_shell_layer", type_names=["int32"], optional=False, document="""0:Top, 1: Bottom, 2: BottomTop, 3:Mid, 4:BottomTopMid""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "change_shellLayers")

