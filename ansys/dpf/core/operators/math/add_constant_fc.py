"""
add_constant_fc
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class add_constant_fc(Operator):
    """Computes the sum of a field (in 0) and a scalar (in 1).

      available inputs:
        - fields_container (FieldsContainer)
        - ponderation (float, list)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.add_constant_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.add_constant_fc(fields_container=my_fields_container,ponderation=my_ponderation)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, ponderation=None, config=None, server=None):
        super().__init__(name="add_constant_fc", config = config, server = server)
        self._inputs = InputsAddConstantFc(self)
        self._outputs = OutputsAddConstantFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the sum of a field (in 0) and a scalar (in 1).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "ponderation", type_names=["double","vector<double>"], optional=False, document="""double or vector of double""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "add_constant_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAddConstantFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAddConstantFc 
        """
        return super().outputs


#internal name: add_constant_fc
#scripting name: add_constant_fc
class InputsAddConstantFc(_Inputs):
    """Intermediate class used to connect user inputs to add_constant_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.add_constant_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)
    """
    def __init__(self, op: Operator):
        super().__init__(add_constant_fc._spec().inputs, op)
        self._fields_container = Input(add_constant_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._ponderation = Input(add_constant_fc._spec().input_pin(1), 1, op, -1) 
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

        >>> op = dpf.operators.math.add_constant_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def ponderation(self):
        """Allows to connect ponderation input to the operator

        - pindoc: double or vector of double

        Parameters
        ----------
        my_ponderation : float, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.add_constant_fc()
        >>> op.inputs.ponderation.connect(my_ponderation)
        >>> #or
        >>> op.inputs.ponderation(my_ponderation)

        """
        return self._ponderation

class OutputsAddConstantFc(_Outputs):
    """Intermediate class used to get outputs from add_constant_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.add_constant_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(add_constant_fc._spec().outputs, op)
        self._fields_container = Output(add_constant_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.add_constant_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

