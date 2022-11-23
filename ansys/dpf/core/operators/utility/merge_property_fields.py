"""
merge_property_fields
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class merge_property_fields(Operator):
    """Take a set of property fields and assemble them in a unique one

      available inputs:
        - vector_shared_ptr_property_field__1 (PropertyField)
        - vector_shared_ptr_property_field__2 (PropertyField)

      available outputs:
        - property_field (PropertyField)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_property_fields()

      >>> # Make input connections
      >>> my_vector_shared_ptr_property_field__1 = dpf.PropertyField()
      >>> op.inputs.vector_shared_ptr_property_field__1.connect(my_vector_shared_ptr_property_field__1)
      >>> my_vector_shared_ptr_property_field__2 = dpf.PropertyField()
      >>> op.inputs.vector_shared_ptr_property_field__2.connect(my_vector_shared_ptr_property_field__2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_property_fields(vector_shared_ptr_property_field__1=my_vector_shared_ptr_property_field__1,vector_shared_ptr_property_field__2=my_vector_shared_ptr_property_field__2)

      >>> # Get output data
      >>> result_property_field = op.outputs.property_field()"""
    def __init__(self, vector_shared_ptr_property_field__1=None, vector_shared_ptr_property_field__2=None, config=None, server=None):
        super().__init__(name="merge::property_field", config = config, server = server)
        self._inputs = InputsMergePropertyFields(self)
        self._outputs = OutputsMergePropertyFields(self)
        if vector_shared_ptr_property_field__1 !=None:
            self.inputs.vector_shared_ptr_property_field__1.connect(vector_shared_ptr_property_field__1)
        if vector_shared_ptr_property_field__2 !=None:
            self.inputs.vector_shared_ptr_property_field__2.connect(vector_shared_ptr_property_field__2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of property fields and assemble them in a unique one""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "vector_shared_ptr_property_field__", type_names=["property_field"], optional=False, document="""Either a property fields container, a vector of property fields to merge or property fields from pin 0 to ..."""), 
                                 1 : PinSpecification(name = "vector_shared_ptr_property_field__", type_names=["property_field"], optional=False, document="""Either a property fields container, a vector of property fields to merge or property fields from pin 0 to ...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "property_field", type_names=["property_field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::property_field")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergePropertyFields 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergePropertyFields 
        """
        return super().outputs


#internal name: merge::property_field
#scripting name: merge_property_fields
class InputsMergePropertyFields(_Inputs):
    """Intermediate class used to connect user inputs to merge_property_fields operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_property_fields()
      >>> my_vector_shared_ptr_property_field__1 = dpf.PropertyField()
      >>> op.inputs.vector_shared_ptr_property_field__1.connect(my_vector_shared_ptr_property_field__1)
      >>> my_vector_shared_ptr_property_field__2 = dpf.PropertyField()
      >>> op.inputs.vector_shared_ptr_property_field__2.connect(my_vector_shared_ptr_property_field__2)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_property_fields._spec().inputs, op)
        self._vector_shared_ptr_property_field__1 = Input(merge_property_fields._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self._vector_shared_ptr_property_field__1)
        self._vector_shared_ptr_property_field__2 = Input(merge_property_fields._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self._vector_shared_ptr_property_field__2)

    @property
    def vector_shared_ptr_property_field__1(self):
        """Allows to connect vector_shared_ptr_property_field__1 input to the operator

        - pindoc: Either a property fields container, a vector of property fields to merge or property fields from pin 0 to ...

        Parameters
        ----------
        my_vector_shared_ptr_property_field__1 : PropertyField, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_property_fields()
        >>> op.inputs.vector_shared_ptr_property_field__1.connect(my_vector_shared_ptr_property_field__1)
        >>> #or
        >>> op.inputs.vector_shared_ptr_property_field__1(my_vector_shared_ptr_property_field__1)

        """
        return self._vector_shared_ptr_property_field__1

    @property
    def vector_shared_ptr_property_field__2(self):
        """Allows to connect vector_shared_ptr_property_field__2 input to the operator

        - pindoc: Either a property fields container, a vector of property fields to merge or property fields from pin 0 to ...

        Parameters
        ----------
        my_vector_shared_ptr_property_field__2 : PropertyField, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_property_fields()
        >>> op.inputs.vector_shared_ptr_property_field__2.connect(my_vector_shared_ptr_property_field__2)
        >>> #or
        >>> op.inputs.vector_shared_ptr_property_field__2(my_vector_shared_ptr_property_field__2)

        """
        return self._vector_shared_ptr_property_field__2

class OutputsMergePropertyFields(_Outputs):
    """Intermediate class used to get outputs from merge_property_fields operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_property_fields()
      >>> # Connect inputs : op.inputs. ...
      >>> result_property_field = op.outputs.property_field()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_property_fields._spec().outputs, op)
        self._property_field = Output(merge_property_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self._property_field)

    @property
    def property_field(self):
        """Allows to get property_field output of the operator


        Returns
        ----------
        my_property_field : PropertyField, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_property_fields()
        >>> # Connect inputs : op.inputs. ...
        >>> result_property_field = op.outputs.property_field() 
        """
        return self._property_field

