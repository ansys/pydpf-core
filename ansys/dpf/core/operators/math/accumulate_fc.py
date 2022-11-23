"""
accumulate_fc
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class accumulate_fc(Operator):
    """Sum all the elementary data of a field to get one elementary data at the end.

      available inputs:
        - fields_container (FieldsContainer)
        - ponderation (Field)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.accumulate_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_ponderation = dpf.Field()
      >>> op.inputs.ponderation.connect(my_ponderation)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.accumulate_fc(fields_container=my_fields_container,ponderation=my_ponderation)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, ponderation=None, config=None, server=None):
        super().__init__(name="accumulate_fc", config = config, server = server)
        self._inputs = InputsAccumulateFc(self)
        self._outputs = OutputsAccumulateFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)

    @staticmethod
    def _spec():
        spec = Specification(description="""Sum all the elementary data of a field to get one elementary data at the end.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "ponderation", type_names=["field"], optional=False, document="""field""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "accumulate_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAccumulateFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAccumulateFc 
        """
        return super().outputs


#internal name: accumulate_fc
#scripting name: accumulate_fc
class InputsAccumulateFc(_Inputs):
    """Intermediate class used to connect user inputs to accumulate_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.accumulate_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_ponderation = dpf.Field()
      >>> op.inputs.ponderation.connect(my_ponderation)
    """
    def __init__(self, op: Operator):
        super().__init__(accumulate_fc._spec().inputs, op)
        self._fields_container = Input(accumulate_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._ponderation = Input(accumulate_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._ponderation)

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

        >>> op = dpf.operators.math.accumulate_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def ponderation(self):
        """Allows to connect ponderation input to the operator

        - pindoc: field

        Parameters
        ----------
        my_ponderation : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.accumulate_fc()
        >>> op.inputs.ponderation.connect(my_ponderation)
        >>> #or
        >>> op.inputs.ponderation(my_ponderation)

        """
        return self._ponderation

class OutputsAccumulateFc(_Outputs):
    """Intermediate class used to get outputs from accumulate_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.accumulate_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(accumulate_fc._spec().outputs, op)
        self._fields_container = Output(accumulate_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.accumulate_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

