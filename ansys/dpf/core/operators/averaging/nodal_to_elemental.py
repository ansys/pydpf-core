"""
nodal_to_elemental
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "averaging" category
"""

class nodal_to_elemental(Operator):
    """Transform Nodal field to Elemental field, compute result on a given element scoping.

      available inputs:
        - field (Field, FieldsContainer)
        - mesh_scoping (Scoping) (optional)
        - collapse_shell_layers (bool) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.nodal_to_elemental()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.nodal_to_elemental(field=my_field,mesh_scoping=my_mesh_scoping,collapse_shell_layers=my_collapse_shell_layers)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, mesh_scoping=None, collapse_shell_layers=None, config=None, server=None):
        super().__init__(name="nodal_to_elemental", config = config, server = server)
        self._inputs = InputsNodalToElemental(self)
        self._outputs = OutputsNodalToElemental(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform Nodal field to Elemental field, compute result on a given element scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 10 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""if true shell layers are averaged as well (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "nodal_to_elemental")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNodalToElemental 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNodalToElemental 
        """
        return super().outputs


#internal name: nodal_to_elemental
#scripting name: nodal_to_elemental
class InputsNodalToElemental(_Inputs):
    """Intermediate class used to connect user inputs to nodal_to_elemental operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.nodal_to_elemental()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_to_elemental._spec().inputs, op)
        self._field = Input(nodal_to_elemental._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._mesh_scoping = Input(nodal_to_elemental._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._collapse_shell_layers = Input(nodal_to_elemental._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self._collapse_shell_layers)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_to_elemental()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_to_elemental()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def collapse_shell_layers(self):
        """Allows to connect collapse_shell_layers input to the operator

        - pindoc: if true shell layers are averaged as well (default is false)

        Parameters
        ----------
        my_collapse_shell_layers : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_to_elemental()
        >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
        >>> #or
        >>> op.inputs.collapse_shell_layers(my_collapse_shell_layers)

        """
        return self._collapse_shell_layers

class OutputsNodalToElemental(_Outputs):
    """Intermediate class used to get outputs from nodal_to_elemental operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.nodal_to_elemental()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_to_elemental._spec().outputs, op)
        self._field = Output(nodal_to_elemental._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_to_elemental()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

