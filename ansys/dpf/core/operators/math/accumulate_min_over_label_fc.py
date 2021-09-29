"""
accumulate_min_over_label_fc
============================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class accumulate_min_over_label_fc(Operator):
    """Compute the component-wise sum over all the fields having the same id for the label set in input in the fields container and take its opposite. This computation can be incremental, if the input fields container is connected and the operator is ran several time, the output field will be on all the inputs connected

      available inputs:
        - fields_container (FieldsContainer)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.accumulate_min_over_label_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.accumulate_min_over_label_fc(fields_container=my_fields_container)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="accumulate_min_over_label_fc", config = config, server = server)
        self._inputs = InputsAccumulateMinOverLabelFc(self)
        self._outputs = OutputsAccumulateMinOverLabelFc(self)
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

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAccumulateMinOverLabelFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAccumulateMinOverLabelFc 
        """
        return super().outputs


#internal name: accumulate_min_over_label_fc
#scripting name: accumulate_min_over_label_fc
class InputsAccumulateMinOverLabelFc(_Inputs):
    """Intermediate class used to connect user inputs to accumulate_min_over_label_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.accumulate_min_over_label_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
    """
    def __init__(self, op: Operator):
        super().__init__(accumulate_min_over_label_fc._spec().inputs, op)
        self._fields_container = Input(accumulate_min_over_label_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.accumulate_min_over_label_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

class OutputsAccumulateMinOverLabelFc(_Outputs):
    """Intermediate class used to get outputs from accumulate_min_over_label_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.accumulate_min_over_label_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(accumulate_min_over_label_fc._spec().outputs, op)
        self._field = Output(accumulate_min_over_label_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.accumulate_min_over_label_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

