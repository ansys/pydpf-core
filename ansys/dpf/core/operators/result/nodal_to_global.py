"""
nodal_to_global
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class nodal_to_global(Operator):
    """Rotates nodal elemental results to global coordinate system

      available inputs:
        - fieldA (Field)
        - fieldB (Field)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.nodal_to_global()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.nodal_to_global(fieldA=my_fieldA,fieldB=my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="NodalElementalResultsRotation", config = config, server = server)
        self._inputs = InputsNodalToGlobal(self)
        self._outputs = OutputsNodalToGlobal(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rotates nodal elemental results to global coordinate system""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field"], optional=False, document="""Vector or tensor field that must be rotated, expressed in nodal coordinate system."""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field"], optional=False, document="""Nodal euler angles defined from an rst file. Those  must be the rotations from Nodal to Global.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""Rotated field""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "NodalElementalResultsRotation")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNodalToGlobal 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNodalToGlobal 
        """
        return super().outputs


#internal name: NodalElementalResultsRotation
#scripting name: nodal_to_global
class InputsNodalToGlobal(_Inputs):
    """Intermediate class used to connect user inputs to nodal_to_global operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.nodal_to_global()
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_to_global._spec().inputs, op)
        self._fieldA = Input(nodal_to_global._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fieldA)
        self._fieldB = Input(nodal_to_global._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fieldB)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator

        - pindoc: Vector or tensor field that must be rotated, expressed in nodal coordinate system.

        Parameters
        ----------
        my_fieldA : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_to_global()
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

        >>> op = dpf.operators.result.nodal_to_global()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> #or
        >>> op.inputs.fieldB(my_fieldB)

        """
        return self._fieldB

class OutputsNodalToGlobal(_Outputs):
    """Intermediate class used to get outputs from nodal_to_global operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.nodal_to_global()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_to_global._spec().outputs, op)
        self._field = Output(nodal_to_global._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.nodal_to_global()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

