"""
field_low_pass_fc
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "filter" category
"""

class field_low_pass_fc(Operator):
    """The low pass filter returns all the values strictly inferior to the threshold value in input.

      available inputs:
        - fields_container (FieldsContainer)
        - threshold (float, Field)
        - both (bool) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.filter.field_low_pass_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_threshold = float()
      >>> op.inputs.threshold.connect(my_threshold)
      >>> my_both = bool()
      >>> op.inputs.both.connect(my_both)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.filter.field_low_pass_fc(fields_container=my_fields_container,threshold=my_threshold,both=my_both)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, threshold=None, both=None, config=None, server=None):
        super().__init__(name="core::field::low_pass_fc", config = config, server = server)
        self._inputs = InputsFieldLowPassFc(self)
        self._outputs = OutputsFieldLowPassFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if threshold !=None:
            self.inputs.threshold.connect(threshold)
        if both !=None:
            self.inputs.both.connect(both)

    @staticmethod
    def _spec():
        spec = Specification(description="""The low pass filter returns all the values strictly inferior to the threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "threshold", type_names=["double","field"], optional=False, document="""a threshold scalar or a field containing one value is expected"""), 
                                 2 : PinSpecification(name = "both", type_names=["bool"], optional=True, document="""bool(optional, default false) if set to true, the complement of the filtered fields container is returned on output pin #1""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::field::low_pass_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFieldLowPassFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFieldLowPassFc 
        """
        return super().outputs


#internal name: core::field::low_pass_fc
#scripting name: field_low_pass_fc
class InputsFieldLowPassFc(_Inputs):
    """Intermediate class used to connect user inputs to field_low_pass_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.filter.field_low_pass_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_threshold = float()
      >>> op.inputs.threshold.connect(my_threshold)
      >>> my_both = bool()
      >>> op.inputs.both.connect(my_both)
    """
    def __init__(self, op: Operator):
        super().__init__(field_low_pass_fc._spec().inputs, op)
        self._fields_container = Input(field_low_pass_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._threshold = Input(field_low_pass_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._threshold)
        self._both = Input(field_low_pass_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._both)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.filter.field_low_pass_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

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

        >>> op = dpf.operators.filter.field_low_pass_fc()
        >>> op.inputs.threshold.connect(my_threshold)
        >>> #or
        >>> op.inputs.threshold(my_threshold)

        """
        return self._threshold

    @property
    def both(self):
        """Allows to connect both input to the operator

        - pindoc: bool(optional, default false) if set to true, the complement of the filtered fields container is returned on output pin #1

        Parameters
        ----------
        my_both : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.filter.field_low_pass_fc()
        >>> op.inputs.both.connect(my_both)
        >>> #or
        >>> op.inputs.both(my_both)

        """
        return self._both

class OutputsFieldLowPassFc(_Outputs):
    """Intermediate class used to get outputs from field_low_pass_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.filter.field_low_pass_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(field_low_pass_fc._spec().outputs, op)
        self._fields_container = Output(field_low_pass_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.filter.field_low_pass_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

