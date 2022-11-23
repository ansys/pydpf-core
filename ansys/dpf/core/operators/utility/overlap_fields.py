"""
overlap_fields
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class overlap_fields(Operator):
    """Take two fields and superpose them, the overlapping field will override values of base_field.

      available inputs:
        - base_field (Field) (optional)
        - overlapping_field (Field) (optional)

      available outputs:


      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.overlap_fields()

      >>> # Make input connections
      >>> my_base_field = dpf.Field()
      >>> op.inputs.base_field.connect(my_base_field)
      >>> my_overlapping_field = dpf.Field()
      >>> op.inputs.overlapping_field.connect(my_overlapping_field)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.overlap_fields(base_field=my_base_field,overlapping_field=my_overlapping_field)

      >>> # Get output data"""
    def __init__(self, base_field=None, overlapping_field=None, config=None, server=None):
        super().__init__(name="overlap_fields", config = config, server = server)
        self._inputs = InputsOverlapFields(self)
        self._outputs = OutputsOverlapFields(self)
        if base_field !=None:
            self.inputs.base_field.connect(base_field)
        if overlapping_field !=None:
            self.inputs.overlapping_field.connect(overlapping_field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take two fields and superpose them, the overlapping field will override values of base_field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "base_field", type_names=["field"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "overlapping_field", type_names=["field"], optional=True, document="""""")},
                             map_output_pin_spec={
})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "overlap_fields")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsOverlapFields 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsOverlapFields 
        """
        return super().outputs


#internal name: overlap_fields
#scripting name: overlap_fields
class InputsOverlapFields(_Inputs):
    """Intermediate class used to connect user inputs to overlap_fields operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.overlap_fields()
      >>> my_base_field = dpf.Field()
      >>> op.inputs.base_field.connect(my_base_field)
      >>> my_overlapping_field = dpf.Field()
      >>> op.inputs.overlapping_field.connect(my_overlapping_field)
    """
    def __init__(self, op: Operator):
        super().__init__(overlap_fields._spec().inputs, op)
        self._base_field = Input(overlap_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._base_field)
        self._overlapping_field = Input(overlap_fields._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._overlapping_field)

    @property
    def base_field(self):
        """Allows to connect base_field input to the operator

        Parameters
        ----------
        my_base_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.overlap_fields()
        >>> op.inputs.base_field.connect(my_base_field)
        >>> #or
        >>> op.inputs.base_field(my_base_field)

        """
        return self._base_field

    @property
    def overlapping_field(self):
        """Allows to connect overlapping_field input to the operator

        Parameters
        ----------
        my_overlapping_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.overlap_fields()
        >>> op.inputs.overlapping_field.connect(my_overlapping_field)
        >>> #or
        >>> op.inputs.overlapping_field(my_overlapping_field)

        """
        return self._overlapping_field

class OutputsOverlapFields(_Outputs):
    """Intermediate class used to get outputs from overlap_fields operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.overlap_fields()
      >>> # Connect inputs : op.inputs. ...
    """
    def __init__(self, op: Operator):
        super().__init__(overlap_fields._spec().outputs, op)
        pass 

