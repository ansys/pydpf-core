"""
field_band_pass_fc
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "filter" category
"""

class field_band_pass_fc(Operator):
    """The band pass filter returns all the values strictly superior to the min threshold value and strictly inferior to the max threshold value in input.

      available inputs:
        - fields_container (FieldsContainer)
        - min_threshold (float, Field)
        - max_threshold (float, Field) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.filter.field_band_pass_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_min_threshold = float()
      >>> op.inputs.min_threshold.connect(my_min_threshold)
      >>> my_max_threshold = float()
      >>> op.inputs.max_threshold.connect(my_max_threshold)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.filter.field_band_pass_fc(fields_container=my_fields_container,min_threshold=my_min_threshold,max_threshold=my_max_threshold)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, min_threshold=None, max_threshold=None, config=None, server=None):
        super().__init__(name="core::field::band_pass_fc", config = config, server = server)
        self._inputs = InputsFieldBandPassFc(self)
        self._outputs = OutputsFieldBandPassFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if min_threshold !=None:
            self.inputs.min_threshold.connect(min_threshold)
        if max_threshold !=None:
            self.inputs.max_threshold.connect(max_threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The band pass filter returns all the values strictly superior to the min threshold value and strictly inferior to the max threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "min_threshold", type_names=["double","field"], optional=False, document="""a min threshold scalar or a field containing one value is expected"""), 
                                 2 : PinSpecification(name = "max_threshold", type_names=["double","field"], optional=True, document="""a max threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::field::band_pass_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFieldBandPassFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFieldBandPassFc 
        """
        return super().outputs


#internal name: core::field::band_pass_fc
#scripting name: field_band_pass_fc
class InputsFieldBandPassFc(_Inputs):
    """Intermediate class used to connect user inputs to field_band_pass_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.filter.field_band_pass_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_min_threshold = float()
      >>> op.inputs.min_threshold.connect(my_min_threshold)
      >>> my_max_threshold = float()
      >>> op.inputs.max_threshold.connect(my_max_threshold)
    """
    def __init__(self, op: Operator):
        super().__init__(field_band_pass_fc._spec().inputs, op)
        self._fields_container = Input(field_band_pass_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._min_threshold = Input(field_band_pass_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._min_threshold)
        self._max_threshold = Input(field_band_pass_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._max_threshold)

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

        >>> op = dpf.operators.filter.field_band_pass_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def min_threshold(self):
        """Allows to connect min_threshold input to the operator

        - pindoc: a min threshold scalar or a field containing one value is expected

        Parameters
        ----------
        my_min_threshold : float, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.filter.field_band_pass_fc()
        >>> op.inputs.min_threshold.connect(my_min_threshold)
        >>> #or
        >>> op.inputs.min_threshold(my_min_threshold)

        """
        return self._min_threshold

    @property
    def max_threshold(self):
        """Allows to connect max_threshold input to the operator

        - pindoc: a max threshold scalar or a field containing one value is expected

        Parameters
        ----------
        my_max_threshold : float, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.filter.field_band_pass_fc()
        >>> op.inputs.max_threshold.connect(my_max_threshold)
        >>> #or
        >>> op.inputs.max_threshold(my_max_threshold)

        """
        return self._max_threshold

class OutputsFieldBandPassFc(_Outputs):
    """Intermediate class used to get outputs from field_band_pass_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.filter.field_band_pass_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(field_band_pass_fc._spec().outputs, op)
        self._fields_container = Output(field_band_pass_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.filter.field_band_pass_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

