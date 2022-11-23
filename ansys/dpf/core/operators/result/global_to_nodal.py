"""
global_to_nodal
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class global_to_nodal(Operator):
    """Rotate results from global coordinate system to local coordinate system.

      available inputs:
        - fieldA (Field)
        - fieldB (Field)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.global_to_nodal()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.global_to_nodal(fieldA=my_fieldA,fieldB=my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="GlobalToNodal", config = config, server = server)
        self._inputs = InputsGlobalToNodal(self)
        self._outputs = OutputsGlobalToNodal(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rotate results from global coordinate system to local coordinate system.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field"], optional=False, document="""Vector or tensor field that must be rotated, expressed in global coordinate systyem."""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field"], optional=False, document="""Nodal euler angles defined from an rst file. Those  must be the rotations from Nodal to Global.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""Rotated field""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "GlobalToNodal")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsGlobalToNodal 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsGlobalToNodal 
        """
        return super().outputs


#internal name: GlobalToNodal
#scripting name: global_to_nodal
class InputsGlobalToNodal(_Inputs):
    """Intermediate class used to connect user inputs to global_to_nodal operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.global_to_nodal()
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
    """
    def __init__(self, op: Operator):
        super().__init__(global_to_nodal._spec().inputs, op)
        self._fieldA = Input(global_to_nodal._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fieldA)
        self._fieldB = Input(global_to_nodal._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fieldB)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator

        - pindoc: Vector or tensor field that must be rotated, expressed in global coordinate systyem.

        Parameters
        ----------
        my_fieldA : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.global_to_nodal()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> #or
        >>> op.inputs.fieldA(my_fieldA)

        """
        return self._fieldA

    @property
    def fieldB(self):
        """Allows to connect fieldB input to the operator

        - pindoc: Nodal euler angles defined from an rst file. Those  must be the rotations from Nodal to Global.

        Parameters
        ----------
        my_fieldB : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.global_to_nodal()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> #or
        >>> op.inputs.fieldB(my_fieldB)

        """
        return self._fieldB

class OutputsGlobalToNodal(_Outputs):
    """Intermediate class used to get outputs from global_to_nodal operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.global_to_nodal()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(global_to_nodal._spec().outputs, op)
        self._field = Output(global_to_nodal._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        - pindoc: Rotated field

        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.global_to_nodal()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

