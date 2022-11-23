"""
set_property
============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class set_property(Operator):
    """Set a property to an input field/field container

      available inputs:
        - field (Field, FieldsContainer)
        - property_name (str)
        - property_value (str, int, float)

      available outputs:
        - field (Field ,FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.set_property()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_property_name = str()
      >>> op.inputs.property_name.connect(my_property_name)
      >>> my_property_value = str()
      >>> op.inputs.property_value.connect(my_property_value)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.set_property(field=my_field,property_name=my_property_name,property_value=my_property_value)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, property_name=None, property_value=None, config=None, server=None):
        super().__init__(name="field::set_property", config = config, server = server)
        self._inputs = InputsSetProperty(self)
        self._outputs = OutputsSetProperty(self)
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

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSetProperty 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSetProperty 
        """
        return super().outputs


#internal name: field::set_property
#scripting name: set_property
class InputsSetProperty(_Inputs):
    """Intermediate class used to connect user inputs to set_property operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.set_property()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_property_name = str()
      >>> op.inputs.property_name.connect(my_property_name)
      >>> my_property_value = str()
      >>> op.inputs.property_value.connect(my_property_value)
    """
    def __init__(self, op: Operator):
        super().__init__(set_property._spec().inputs, op)
        self._field = Input(set_property._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._property_name = Input(set_property._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._property_name)
        self._property_value = Input(set_property._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._property_value)

    @property
    def field(self):
        """Allows to connect field input to the operator

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.set_property()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def property_name(self):
        """Allows to connect property_name input to the operator

        - pindoc: Property to set

        Parameters
        ----------
        my_property_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.set_property()
        >>> op.inputs.property_name.connect(my_property_name)
        >>> #or
        >>> op.inputs.property_name(my_property_name)

        """
        return self._property_name

    @property
    def property_value(self):
        """Allows to connect property_value input to the operator

        - pindoc: Property to set

        Parameters
        ----------
        my_property_value : str, int, float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.set_property()
        >>> op.inputs.property_value.connect(my_property_value)
        >>> #or
        >>> op.inputs.property_value(my_property_value)

        """
        return self._property_value

class OutputsSetProperty(_Outputs):
    """Intermediate class used to get outputs from set_property operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.set_property()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(set_property._spec().outputs, op)
        self.field_as_field = Output( _modify_output_spec_with_one_type(set_property._spec().output_pin(0), "field"), 0, op) 
        self._outputs.append(self.field_as_field)
        self.field_as_fields_container = Output( _modify_output_spec_with_one_type(set_property._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.field_as_fields_container)

