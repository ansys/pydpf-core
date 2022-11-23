"""
intersect
=========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "scoping" category
"""

class intersect(Operator):
    """Intersect 2 scopings and return the intersection and the difference between the intersection and the first scoping.

      available inputs:
        - scopingA (Scoping)
        - scopingB (Scoping)

      available outputs:
        - intersection (Scoping)
        - scopingA_min_intersection (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.scoping.intersect()

      >>> # Make input connections
      >>> my_scopingA = dpf.Scoping()
      >>> op.inputs.scopingA.connect(my_scopingA)
      >>> my_scopingB = dpf.Scoping()
      >>> op.inputs.scopingB.connect(my_scopingB)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.scoping.intersect(scopingA=my_scopingA,scopingB=my_scopingB)

      >>> # Get output data
      >>> result_intersection = op.outputs.intersection()
      >>> result_scopingA_min_intersection = op.outputs.scopingA_min_intersection()"""
    def __init__(self, scopingA=None, scopingB=None, config=None, server=None):
        super().__init__(name="scoping::intersect", config = config, server = server)
        self._inputs = InputsIntersect(self)
        self._outputs = OutputsIntersect(self)
        if scopingA !=None:
            self.inputs.scopingA.connect(scopingA)
        if scopingB !=None:
            self.inputs.scopingB.connect(scopingB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Intersect 2 scopings and return the intersection and the difference between the intersection and the first scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "scopingA", type_names=["scoping"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scopingB", type_names=["scoping"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "intersection", type_names=["scoping"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scopingA_min_intersection", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scoping::intersect")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsIntersect 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsIntersect 
        """
        return super().outputs


#internal name: scoping::intersect
#scripting name: intersect
class InputsIntersect(_Inputs):
    """Intermediate class used to connect user inputs to intersect operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.intersect()
      >>> my_scopingA = dpf.Scoping()
      >>> op.inputs.scopingA.connect(my_scopingA)
      >>> my_scopingB = dpf.Scoping()
      >>> op.inputs.scopingB.connect(my_scopingB)
    """
    def __init__(self, op: Operator):
        super().__init__(intersect._spec().inputs, op)
        self._scopingA = Input(intersect._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._scopingA)
        self._scopingB = Input(intersect._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._scopingB)

    @property
    def scopingA(self):
        """Allows to connect scopingA input to the operator

        Parameters
        ----------
        my_scopingA : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.intersect()
        >>> op.inputs.scopingA.connect(my_scopingA)
        >>> #or
        >>> op.inputs.scopingA(my_scopingA)

        """
        return self._scopingA

    @property
    def scopingB(self):
        """Allows to connect scopingB input to the operator

        Parameters
        ----------
        my_scopingB : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.intersect()
        >>> op.inputs.scopingB.connect(my_scopingB)
        >>> #or
        >>> op.inputs.scopingB(my_scopingB)

        """
        return self._scopingB

class OutputsIntersect(_Outputs):
    """Intermediate class used to get outputs from intersect operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.intersect()
      >>> # Connect inputs : op.inputs. ...
      >>> result_intersection = op.outputs.intersection()
      >>> result_scopingA_min_intersection = op.outputs.scopingA_min_intersection()
    """
    def __init__(self, op: Operator):
        super().__init__(intersect._spec().outputs, op)
        self._intersection = Output(intersect._spec().output_pin(0), 0, op) 
        self._outputs.append(self._intersection)
        self._scopingA_min_intersection = Output(intersect._spec().output_pin(1), 1, op) 
        self._outputs.append(self._scopingA_min_intersection)

    @property
    def intersection(self):
        """Allows to get intersection output of the operator


        Returns
        ----------
        my_intersection : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.intersect()
        >>> # Connect inputs : op.inputs. ...
        >>> result_intersection = op.outputs.intersection() 
        """
        return self._intersection

    @property
    def scopingA_min_intersection(self):
        """Allows to get scopingA_min_intersection output of the operator


        Returns
        ----------
        my_scopingA_min_intersection : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.intersect()
        >>> # Connect inputs : op.inputs. ...
        >>> result_scopingA_min_intersection = op.outputs.scopingA_min_intersection() 
        """
        return self._scopingA_min_intersection

