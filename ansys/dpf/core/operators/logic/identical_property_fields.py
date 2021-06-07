"""
identical_property_fields
=========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "logic" category
"""

class identical_property_fields(Operator):
    """Take two property fields and compare them.

      available inputs:
        - property_fieldA (MeshedRegion)
        - property_fieldB (MeshedRegion)

      available outputs:
        - are_identical (bool)
        - informations (str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.identical_property_fields()

      >>> # Make input connections
      >>> my_property_fieldA = dpf.MeshedRegion()
      >>> op.inputs.property_fieldA.connect(my_property_fieldA)
      >>> my_property_fieldB = dpf.MeshedRegion()
      >>> op.inputs.property_fieldB.connect(my_property_fieldB)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.logic.identical_property_fields(property_fieldA=my_property_fieldA,property_fieldB=my_property_fieldB)

      >>> # Get output data
      >>> result_are_identical = op.outputs.are_identical()
      >>> result_informations = op.outputs.informations()"""
    def __init__(self, property_fieldA=None, property_fieldB=None, config=None, server=None):
        super().__init__(name="compare::property_field", config = config, server = server)
        self._inputs = InputsIdenticalPropertyFields(self)
        self._outputs = OutputsIdenticalPropertyFields(self)
        if property_fieldA !=None:
            self.inputs.property_fieldA.connect(property_fieldA)
        if property_fieldB !=None:
            self.inputs.property_fieldB.connect(property_fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take two property fields and compare them.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "property_fieldA", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "property_fieldB", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "are_identical", type_names=["bool"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "informations", type_names=["string"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "compare::property_field")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsIdenticalPropertyFields 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsIdenticalPropertyFields 
        """
        return super().outputs


#internal name: compare::property_field
#scripting name: identical_property_fields
class InputsIdenticalPropertyFields(_Inputs):
    """Intermediate class used to connect user inputs to identical_property_fields operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.logic.identical_property_fields()
      >>> my_property_fieldA = dpf.MeshedRegion()
      >>> op.inputs.property_fieldA.connect(my_property_fieldA)
      >>> my_property_fieldB = dpf.MeshedRegion()
      >>> op.inputs.property_fieldB.connect(my_property_fieldB)
    """
    def __init__(self, op: Operator):
        super().__init__(identical_property_fields._spec().inputs, op)
        self._property_fieldA = Input(identical_property_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._property_fieldA)
        self._property_fieldB = Input(identical_property_fields._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._property_fieldB)

    @property
    def property_fieldA(self):
        """Allows to connect property_fieldA input to the operator

        Parameters
        ----------
        my_property_fieldA : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.identical_property_fields()
        >>> op.inputs.property_fieldA.connect(my_property_fieldA)
        >>> #or
        >>> op.inputs.property_fieldA(my_property_fieldA)

        """
        return self._property_fieldA

    @property
    def property_fieldB(self):
        """Allows to connect property_fieldB input to the operator

        Parameters
        ----------
        my_property_fieldB : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.identical_property_fields()
        >>> op.inputs.property_fieldB.connect(my_property_fieldB)
        >>> #or
        >>> op.inputs.property_fieldB(my_property_fieldB)

        """
        return self._property_fieldB

class OutputsIdenticalPropertyFields(_Outputs):
    """Intermediate class used to get outputs from identical_property_fields operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.logic.identical_property_fields()
      >>> # Connect inputs : op.inputs. ...
      >>> result_are_identical = op.outputs.are_identical()
      >>> result_informations = op.outputs.informations()
    """
    def __init__(self, op: Operator):
        super().__init__(identical_property_fields._spec().outputs, op)
        self._are_identical = Output(identical_property_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self._are_identical)
        self._informations = Output(identical_property_fields._spec().output_pin(1), 1, op) 
        self._outputs.append(self._informations)

    @property
    def are_identical(self):
        """Allows to get are_identical output of the operator


        Returns
        ----------
        my_are_identical : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.identical_property_fields()
        >>> # Connect inputs : op.inputs. ...
        >>> result_are_identical = op.outputs.are_identical() 
        """
        return self._are_identical

    @property
    def informations(self):
        """Allows to get informations output of the operator


        Returns
        ----------
        my_informations : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.identical_property_fields()
        >>> # Connect inputs : op.inputs. ...
        >>> result_informations = op.outputs.informations() 
        """
        return self._informations

