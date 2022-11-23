"""
elemental_nodal_to_nodal_elemental_fc
=====================================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "averaging" category
"""

class elemental_nodal_to_nodal_elemental_fc(Operator):
    """Transform ElementalNodal fields to NodalElemental fields, compute result on a given node scoping.

      available inputs:
        - fields_container (FieldsContainer)
        - mesh_scoping (Scoping) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental_fc(fields_container=my_fields_container,mesh_scoping=my_mesh_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="ElementalNodal_To_NodalElemental_fc", config = config, server = server)
        self._inputs = InputsElementalNodalToNodalElementalFc(self)
        self._outputs = OutputsElementalNodalToNodalElementalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal fields to NodalElemental fields, compute result on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ElementalNodal_To_NodalElemental_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementalNodalToNodalElementalFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsElementalNodalToNodalElementalFc 
        """
        return super().outputs


#internal name: ElementalNodal_To_NodalElemental_fc
#scripting name: elemental_nodal_to_nodal_elemental_fc
class InputsElementalNodalToNodalElementalFc(_Inputs):
    """Intermediate class used to connect user inputs to elemental_nodal_to_nodal_elemental_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_elemental_fc._spec().inputs, op)
        self._fields_container = Input(elemental_nodal_to_nodal_elemental_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._mesh_scoping = Input(elemental_nodal_to_nodal_elemental_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental_fc()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

class OutputsElementalNodalToNodalElementalFc(_Outputs):
    """Intermediate class used to get outputs from elemental_nodal_to_nodal_elemental_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_elemental_fc._spec().outputs, op)
        self._fields_container = Output(elemental_nodal_to_nodal_elemental_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

