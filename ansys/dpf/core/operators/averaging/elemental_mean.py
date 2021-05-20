"""
elemental_mean
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class elemental_mean(Operator):
    """Computes the average of a multi-entity fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal).

      available inputs:
        - field (Field)
        - collapse_shell_layers (bool) (optional)
        - force_averaging (bool) (optional)
        - scoping (Scoping) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_mean()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
      >>> my_force_averaging = bool()
      >>> op.inputs.force_averaging.connect(my_force_averaging)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.elemental_mean(field=my_field,collapse_shell_layers=my_collapse_shell_layers,force_averaging=my_force_averaging,scoping=my_scoping)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, collapse_shell_layers=None, force_averaging=None, scoping=None, config=None, server=None):
        super().__init__(name="entity_average", config = config, server = server)
        self._inputs = InputsElementalMean(self)
        self._outputs = OutputsElementalMean(self)
        if field !=None:
            self.inputs.field.connect(field)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)
        if force_averaging !=None:
            self.inputs.force_averaging.connect(force_averaging)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the average of a multi-entity fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""if true shell layers are averaged as well (default is false)"""), 
                                 2 : PinSpecification(name = "force_averaging", type_names=["bool"], optional=True, document="""if true you average, if false you just sum"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "entity_average")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementalMean 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsElementalMean 
        """
        return super().outputs


#internal name: entity_average
#scripting name: elemental_mean
class InputsElementalMean(_Inputs):
    """Intermediate class used to connect user inputs to elemental_mean operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_mean()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
      >>> my_force_averaging = bool()
      >>> op.inputs.force_averaging.connect(my_force_averaging)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_mean._spec().inputs, op)
        self._field = Input(elemental_mean._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._collapse_shell_layers = Input(elemental_mean._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._collapse_shell_layers)
        self._force_averaging = Input(elemental_mean._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._force_averaging)
        self._scoping = Input(elemental_mean._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._scoping)

    @property
    def field(self):
        """Allows to connect field input to the operator

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_mean()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

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

        >>> op = dpf.operators.averaging.elemental_mean()
        >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
        >>> #or
        >>> op.inputs.collapse_shell_layers(my_collapse_shell_layers)

        """
        return self._collapse_shell_layers

    @property
    def force_averaging(self):
        """Allows to connect force_averaging input to the operator

        - pindoc: if true you average, if false you just sum

        Parameters
        ----------
        my_force_averaging : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_mean()
        >>> op.inputs.force_averaging.connect(my_force_averaging)
        >>> #or
        >>> op.inputs.force_averaging(my_force_averaging)

        """
        return self._force_averaging

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator

        - pindoc: average only on these elements, if it is scoping container, the label must correspond to the one of the fields container

        Parameters
        ----------
        my_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_mean()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> #or
        >>> op.inputs.scoping(my_scoping)

        """
        return self._scoping

class OutputsElementalMean(_Outputs):
    """Intermediate class used to get outputs from elemental_mean operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_mean()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_mean._spec().outputs, op)
        self._field = Output(elemental_mean._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.averaging.elemental_mean()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

