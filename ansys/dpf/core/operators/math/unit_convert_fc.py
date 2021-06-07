"""
unit_convert_fc
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class unit_convert_fc(Operator):
    """Convert an input fields container of a given unit to another unit.

      available inputs:
        - fields_container (FieldsContainer)
        - unit_name (str)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.unit_convert_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_unit_name = str()
      >>> op.inputs.unit_name.connect(my_unit_name)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.unit_convert_fc(fields_container=my_fields_container,unit_name=my_unit_name)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, unit_name=None, config=None, server=None):
        super().__init__(name="unit_convert_fc", config = config, server = server)
        self._inputs = InputsUnitConvertFc(self)
        self._outputs = OutputsUnitConvertFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if unit_name !=None:
            self.inputs.unit_name.connect(unit_name)

    @staticmethod
    def _spec():
        spec = Specification(description="""Convert an input fields container of a given unit to another unit.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "unit_name", type_names=["string"], optional=False, document="""unit as a string, ex 'm' for meter, 'Pa' for pascal,...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "unit_convert_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsUnitConvertFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsUnitConvertFc 
        """
        return super().outputs


#internal name: unit_convert_fc
#scripting name: unit_convert_fc
class InputsUnitConvertFc(_Inputs):
    """Intermediate class used to connect user inputs to unit_convert_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.unit_convert_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_unit_name = str()
      >>> op.inputs.unit_name.connect(my_unit_name)
    """
    def __init__(self, op: Operator):
        super().__init__(unit_convert_fc._spec().inputs, op)
        self._fields_container = Input(unit_convert_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._unit_name = Input(unit_convert_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._unit_name)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.unit_convert_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def unit_name(self):
        """Allows to connect unit_name input to the operator

        - pindoc: unit as a string, ex 'm' for meter, 'Pa' for pascal,...

        Parameters
        ----------
        my_unit_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.unit_convert_fc()
        >>> op.inputs.unit_name.connect(my_unit_name)
        >>> #or
        >>> op.inputs.unit_name(my_unit_name)

        """
        return self._unit_name

class OutputsUnitConvertFc(_Outputs):
    """Intermediate class used to get outputs from unit_convert_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.unit_convert_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(unit_convert_fc._spec().outputs, op)
        self._fields_container = Output(unit_convert_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.unit_convert_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

