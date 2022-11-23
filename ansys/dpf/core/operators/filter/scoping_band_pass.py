"""
scoping_band_pass
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "filter" category
"""

class scoping_band_pass(Operator):
    """The band pass filter returns all the values strictly superior to the min threshold value and strictly inferior to the max threshold value in input.

      available inputs:
        - field (Field, FieldsContainer)
        - min_threshold (float, Field)
        - max_threshold (float, Field) (optional)

      available outputs:
        - scoping (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.filter.scoping_band_pass()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_min_threshold = float()
      >>> op.inputs.min_threshold.connect(my_min_threshold)
      >>> my_max_threshold = float()
      >>> op.inputs.max_threshold.connect(my_max_threshold)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.filter.scoping_band_pass(field=my_field,min_threshold=my_min_threshold,max_threshold=my_max_threshold)

      >>> # Get output data
      >>> result_scoping = op.outputs.scoping()"""
    def __init__(self, field=None, min_threshold=None, max_threshold=None, config=None, server=None):
        super().__init__(name="core::scoping::band_pass", config = config, server = server)
        self._inputs = InputsScopingBandPass(self)
        self._outputs = OutputsScopingBandPass(self)
        if field !=None:
            self.inputs.field.connect(field)
        if min_threshold !=None:
            self.inputs.min_threshold.connect(min_threshold)
        if max_threshold !=None:
            self.inputs.max_threshold.connect(max_threshold)

    @staticmethod
    def _spec():
        spec = Specification(description="""The band pass filter returns all the values strictly superior to the min threshold value and strictly inferior to the max threshold value in input.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "min_threshold", type_names=["double","field"], optional=False, document="""a min threshold scalar or a field containing one value is expected"""), 
                                 2 : PinSpecification(name = "max_threshold", type_names=["double","field"], optional=True, document="""a max threshold scalar or a field containing one value is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "core::scoping::band_pass")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsScopingBandPass 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsScopingBandPass 
        """
        return super().outputs


#internal name: core::scoping::band_pass
#scripting name: scoping_band_pass
class InputsScopingBandPass(_Inputs):
    """Intermediate class used to connect user inputs to scoping_band_pass operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.filter.scoping_band_pass()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_min_threshold = float()
      >>> op.inputs.min_threshold.connect(my_min_threshold)
      >>> my_max_threshold = float()
      >>> op.inputs.max_threshold.connect(my_max_threshold)
    """
    def __init__(self, op: Operator):
        super().__init__(scoping_band_pass._spec().inputs, op)
        self._field = Input(scoping_band_pass._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._min_threshold = Input(scoping_band_pass._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._min_threshold)
        self._max_threshold = Input(scoping_band_pass._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._max_threshold)

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

        >>> op = dpf.operators.filter.scoping_band_pass()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

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

        >>> op = dpf.operators.filter.scoping_band_pass()
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

        >>> op = dpf.operators.filter.scoping_band_pass()
        >>> op.inputs.max_threshold.connect(my_max_threshold)
        >>> #or
        >>> op.inputs.max_threshold(my_max_threshold)

        """
        return self._max_threshold

class OutputsScopingBandPass(_Outputs):
    """Intermediate class used to get outputs from scoping_band_pass operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.filter.scoping_band_pass()
      >>> # Connect inputs : op.inputs. ...
      >>> result_scoping = op.outputs.scoping()
    """
    def __init__(self, op: Operator):
        super().__init__(scoping_band_pass._spec().outputs, op)
        self._scoping = Output(scoping_band_pass._spec().output_pin(0), 0, op) 
        self._outputs.append(self._scoping)

    @property
    def scoping(self):
        """Allows to get scoping output of the operator


        Returns
        ----------
        my_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.filter.scoping_band_pass()
        >>> # Connect inputs : op.inputs. ...
        >>> result_scoping = op.outputs.scoping() 
        """
        return self._scoping

