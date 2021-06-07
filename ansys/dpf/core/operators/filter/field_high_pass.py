"""
field_high_pass
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "filter" category
"""

class field_high_pass(Operator):
    """The high pass filter returns all the values strictly superior to the threshold value in input.

      available inputs:
        - field (Field, FieldsContainer)
        - threshold (float, Field)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.filter.field_high_pass()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_threshold = float()
      >>> op.inputs.threshold.connect(my_threshold)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.filter.field_high_pass(field=my_field,threshold=my_threshold)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, threshold=None, config=None, server=None):
        super().__init__(name="core::field::high_pass", config = config, server = server)
        self._inputs = InputsFieldHighPass(self)
        self._outputs = OutputsFieldHighPass(self)
        if field !=None:
            self.inputs.field.connect(field)
        if threshold !=None:
            self.inputs.threshold.connect(threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The high pass filter returns all the values strictly superior to the threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "threshold", type_names=["double","field"], optional=False, document="""a threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::field::high_pass")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFieldHighPass 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFieldHighPass 
        """
        return super().outputs


#internal name: core::field::high_pass
#scripting name: field_high_pass
class InputsFieldHighPass(_Inputs):
    """Intermediate class used to connect user inputs to field_high_pass operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.filter.field_high_pass()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_threshold = float()
      >>> op.inputs.threshold.connect(my_threshold)
    """
    def __init__(self, op: Operator):
        super().__init__(field_high_pass._spec().inputs, op)
        self._field = Input(field_high_pass._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._threshold = Input(field_high_pass._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._threshold)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.filter.field_high_pass()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def threshold(self):
        """Allows to connect threshold input to the operator

        - pindoc: a threshold scalar or a field containing one value is expected

        Parameters
        ----------
        my_threshold : float, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.filter.field_high_pass()
        >>> op.inputs.threshold.connect(my_threshold)
        >>> #or
        >>> op.inputs.threshold(my_threshold)

        """
        return self._threshold

class OutputsFieldHighPass(_Outputs):
    """Intermediate class used to get outputs from field_high_pass operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.filter.field_high_pass()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(field_high_pass._spec().outputs, op)
        self._field = Output(field_high_pass._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.filter.field_high_pass()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

