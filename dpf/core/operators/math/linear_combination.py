"""
linear_combination
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class linear_combination(Operator):
    """Computes aXY + bZ where a,b (in 0, in 3) are scalar and X,Y,Z (in 1,2,4) are complex numbers.

      available inputs:
        - a (float)
        - fields_containerA (FieldsContainer)
        - fields_containerB (FieldsContainer)
        - b (float)
        - fields_containerC (FieldsContainer)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.linear_combination()

      >>> # Make input connections
      >>> my_a = float()
      >>> op.inputs.a.connect(my_a)
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)
      >>> my_b = float()
      >>> op.inputs.b.connect(my_b)
      >>> my_fields_containerC = dpf.FieldsContainer()
      >>> op.inputs.fields_containerC.connect(my_fields_containerC)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.linear_combination(a=my_a,fields_containerA=my_fields_containerA,fields_containerB=my_fields_containerB,b=my_b,fields_containerC=my_fields_containerC)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, a=None, fields_containerA=None, fields_containerB=None, b=None, fields_containerC=None, config=None, server=None):
        super().__init__(name="CplxOp", config = config, server = server)
        self._inputs = InputsLinearCombination(self)
        self._outputs = OutputsLinearCombination(self)
        if a !=None:
            self.inputs.a.connect(a)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)
        if b !=None:
            self.inputs.b.connect(b)
        if fields_containerC !=None:
            self.inputs.fields_containerC.connect(fields_containerC)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes aXY + bZ where a,b (in 0, in 3) are scalar and X,Y,Z (in 1,2,4) are complex numbers.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "a", type_names=["double"], optional=False, document="""Double"""), 
                                 1 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "b", type_names=["double"], optional=False, document="""Double"""), 
                                 4 : PinSpecification(name = "fields_containerC", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "CplxOp")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsLinearCombination 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsLinearCombination 
        """
        return super().outputs


#internal name: CplxOp
#scripting name: linear_combination
class InputsLinearCombination(_Inputs):
    """Intermediate class used to connect user inputs to linear_combination operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.linear_combination()
      >>> my_a = float()
      >>> op.inputs.a.connect(my_a)
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)
      >>> my_b = float()
      >>> op.inputs.b.connect(my_b)
      >>> my_fields_containerC = dpf.FieldsContainer()
      >>> op.inputs.fields_containerC.connect(my_fields_containerC)
    """
    def __init__(self, op: Operator):
        super().__init__(linear_combination._spec().inputs, op)
        self._a = Input(linear_combination._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._a)
        self._fields_containerA = Input(linear_combination._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fields_containerA)
        self._fields_containerB = Input(linear_combination._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._fields_containerB)
        self._b = Input(linear_combination._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._b)
        self._fields_containerC = Input(linear_combination._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._fields_containerC)

    @property
    def a(self):
        """Allows to connect a input to the operator

        - pindoc: Double

        Parameters
        ----------
        my_a : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.linear_combination()
        >>> op.inputs.a.connect(my_a)
        >>> #or
        >>> op.inputs.a(my_a)

        """
        return self._a

    @property
    def fields_containerA(self):
        """Allows to connect fields_containerA input to the operator

        Parameters
        ----------
        my_fields_containerA : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.linear_combination()
        >>> op.inputs.fields_containerA.connect(my_fields_containerA)
        >>> #or
        >>> op.inputs.fields_containerA(my_fields_containerA)

        """
        return self._fields_containerA

    @property
    def fields_containerB(self):
        """Allows to connect fields_containerB input to the operator

        Parameters
        ----------
        my_fields_containerB : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.linear_combination()
        >>> op.inputs.fields_containerB.connect(my_fields_containerB)
        >>> #or
        >>> op.inputs.fields_containerB(my_fields_containerB)

        """
        return self._fields_containerB

    @property
    def b(self):
        """Allows to connect b input to the operator

        - pindoc: Double

        Parameters
        ----------
        my_b : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.linear_combination()
        >>> op.inputs.b.connect(my_b)
        >>> #or
        >>> op.inputs.b(my_b)

        """
        return self._b

    @property
    def fields_containerC(self):
        """Allows to connect fields_containerC input to the operator

        Parameters
        ----------
        my_fields_containerC : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.linear_combination()
        >>> op.inputs.fields_containerC.connect(my_fields_containerC)
        >>> #or
        >>> op.inputs.fields_containerC(my_fields_containerC)

        """
        return self._fields_containerC

class OutputsLinearCombination(_Outputs):
    """Intermediate class used to get outputs from linear_combination operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.linear_combination()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(linear_combination._spec().outputs, op)
        self._fields_container = Output(linear_combination._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.linear_combination()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

