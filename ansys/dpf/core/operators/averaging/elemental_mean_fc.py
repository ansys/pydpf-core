"""
elemental_mean_fc
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class elemental_mean_fc(Operator):
    """Computes the average of a multi-entity container of fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal). If the input fields are mixed shell/solid and collapseShellLayers is not asked, then the fields are split by element shape and the output fields container has elshape label.

      available inputs:
        - fields_container (FieldsContainer)
        - collapse_shell_layers (bool) (optional)
        - force_averaging (bool) (optional)
        - scoping (Scoping) (optional)
        - meshed_region (MeshedRegion) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_mean_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
      >>> my_force_averaging = bool()
      >>> op.inputs.force_averaging.connect(my_force_averaging)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.meshed_region.connect(my_meshed_region)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.elemental_mean_fc(fields_container=my_fields_container,collapse_shell_layers=my_collapse_shell_layers,force_averaging=my_force_averaging,scoping=my_scoping,meshed_region=my_meshed_region)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, collapse_shell_layers=None, force_averaging=None, scoping=None, meshed_region=None, config=None, server=None):
        super().__init__(name="entity_average_fc", config = config, server = server)
        self._inputs = InputsElementalMeanFc(self)
        self._outputs = OutputsElementalMeanFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)
        if force_averaging !=None:
            self.inputs.force_averaging.connect(force_averaging)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if meshed_region !=None:
            self.inputs.meshed_region.connect(meshed_region)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the average of a multi-entity container of fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal). If the input fields are mixed shell/solid and collapseShellLayers is not asked, then the fields are split by element shape and the output fields container has elshape label.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""if true shell layers are averaged as well (default is false)"""), 
                                 2 : PinSpecification(name = "force_averaging", type_names=["bool"], optional=True, document="""if true you average, if false you just sum"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""average only on these elements, if it is scoping container, the label must correspond to the one of the fields container"""), 
                                 4 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "entity_average_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementalMeanFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsElementalMeanFc 
        """
        return super().outputs


#internal name: entity_average_fc
#scripting name: elemental_mean_fc
class InputsElementalMeanFc(_Inputs):
    """Intermediate class used to connect user inputs to elemental_mean_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_mean_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
      >>> my_force_averaging = bool()
      >>> op.inputs.force_averaging.connect(my_force_averaging)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.meshed_region.connect(my_meshed_region)
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_mean_fc._spec().inputs, op)
        self._fields_container = Input(elemental_mean_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._collapse_shell_layers = Input(elemental_mean_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._collapse_shell_layers)
        self._force_averaging = Input(elemental_mean_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._force_averaging)
        self._scoping = Input(elemental_mean_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._scoping)
        self._meshed_region = Input(elemental_mean_fc._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._meshed_region)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_mean_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

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

        >>> op = dpf.operators.averaging.elemental_mean_fc()
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

        >>> op = dpf.operators.averaging.elemental_mean_fc()
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

        >>> op = dpf.operators.averaging.elemental_mean_fc()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> #or
        >>> op.inputs.scoping(my_scoping)

        """
        return self._scoping

    @property
    def meshed_region(self):
        """Allows to connect meshed_region input to the operator

        - pindoc: the mesh region in this pin is used to perform the averaging, if there is no field's support it is used

        Parameters
        ----------
        my_meshed_region : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_mean_fc()
        >>> op.inputs.meshed_region.connect(my_meshed_region)
        >>> #or
        >>> op.inputs.meshed_region(my_meshed_region)

        """
        return self._meshed_region

class OutputsElementalMeanFc(_Outputs):
    """Intermediate class used to get outputs from elemental_mean_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_mean_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_mean_fc._spec().outputs, op)
        self._fields_container = Output(elemental_mean_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.averaging.elemental_mean_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

