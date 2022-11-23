"""
rotate_fc
=========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "geo" category
"""

class rotate_fc(Operator):
    """Apply a transformation (rotation) matrix on all the fields of a fields container.

      available inputs:
        - fields_container (FieldsContainer)
        - coordinate_system (Field)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.rotate_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_coordinate_system = dpf.Field()
      >>> op.inputs.coordinate_system.connect(my_coordinate_system)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.geo.rotate_fc(fields_container=my_fields_container,coordinate_system=my_coordinate_system)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, coordinate_system=None, config=None, server=None):
        super().__init__(name="rotate_fc", config = config, server = server)
        self._inputs = InputsRotateFc(self)
        self._outputs = OutputsRotateFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if coordinate_system !=None:
            self.inputs.coordinate_system.connect(coordinate_system)

    @staticmethod
    def _spec():
        spec = Specification(description="""Apply a transformation (rotation) matrix on all the fields of a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "coordinate_system", type_names=["field"], optional=False, document="""3-3 rotation matrix""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "rotate_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRotateFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRotateFc 
        """
        return super().outputs


#internal name: rotate_fc
#scripting name: rotate_fc
class InputsRotateFc(_Inputs):
    """Intermediate class used to connect user inputs to rotate_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.rotate_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_coordinate_system = dpf.Field()
      >>> op.inputs.coordinate_system.connect(my_coordinate_system)
    """
    def __init__(self, op: Operator):
        super().__init__(rotate_fc._spec().inputs, op)
        self._fields_container = Input(rotate_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._coordinate_system = Input(rotate_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._coordinate_system)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.rotate_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def coordinate_system(self):
        """Allows to connect coordinate_system input to the operator

        - pindoc: 3-3 rotation matrix

        Parameters
        ----------
        my_coordinate_system : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.rotate_fc()
        >>> op.inputs.coordinate_system.connect(my_coordinate_system)
        >>> #or
        >>> op.inputs.coordinate_system(my_coordinate_system)

        """
        return self._coordinate_system

class OutputsRotateFc(_Outputs):
    """Intermediate class used to get outputs from rotate_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.rotate_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(rotate_fc._spec().outputs, op)
        self._fields_container = Output(rotate_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.geo.rotate_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

