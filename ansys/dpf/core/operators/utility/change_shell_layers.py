"""
change_shell_layers
===================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "utility" category
"""

class change_shell_layers(Operator):
    """Extract the expected shell layers from the input fields, if the fields contain only one layer then it returns the input fields

      available inputs:
        - fields_container (FieldsContainer, Field)
        - e_shell_layer (int)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.change_shell_layers()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_e_shell_layer = int()
      >>> op.inputs.e_shell_layer.connect(my_e_shell_layer)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.change_shell_layers(fields_container=my_fields_container,e_shell_layer=my_e_shell_layer)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, e_shell_layer=None, config=None, server=None):
        super().__init__(name="change_shellLayers", config = config, server = server)
        self._inputs = InputsChangeShellLayers(self)
        self._outputs = OutputsChangeShellLayers(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if e_shell_layer !=None:
            self.inputs.e_shell_layer.connect(e_shell_layer)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extract the expected shell layers from the input fields, if the fields contain only one layer then it returns the input fields""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container","field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "e_shell_layer", type_names=["int32"], optional=False, document="""0:Top, 1: Bottom, 2: BottomTop, 3:Mid, 4:BottomTopMid""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "change_shellLayers")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsChangeShellLayers 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsChangeShellLayers 
        """
        return super().outputs


#internal name: change_shellLayers
#scripting name: change_shell_layers
class InputsChangeShellLayers(_Inputs):
    """Intermediate class used to connect user inputs to change_shell_layers operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.change_shell_layers()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_e_shell_layer = int()
      >>> op.inputs.e_shell_layer.connect(my_e_shell_layer)
    """
    def __init__(self, op: Operator):
        super().__init__(change_shell_layers._spec().inputs, op)
        self._fields_container = Input(change_shell_layers._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._e_shell_layer = Input(change_shell_layers._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._e_shell_layer)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.change_shell_layers()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def e_shell_layer(self):
        """Allows to connect e_shell_layer input to the operator

        - pindoc: 0:Top, 1: Bottom, 2: BottomTop, 3:Mid, 4:BottomTopMid

        Parameters
        ----------
        my_e_shell_layer : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.change_shell_layers()
        >>> op.inputs.e_shell_layer.connect(my_e_shell_layer)
        >>> #or
        >>> op.inputs.e_shell_layer(my_e_shell_layer)

        """
        return self._e_shell_layer

class OutputsChangeShellLayers(_Outputs):
    """Intermediate class used to get outputs from change_shell_layers operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.change_shell_layers()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(change_shell_layers._spec().outputs, op)
        self._fields_container = Output(change_shell_layers._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.utility.change_shell_layers()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

