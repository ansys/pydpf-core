"""
nodal_to_elemental_fc
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class nodal_to_elemental_fc(Operator):
    """Transform Nodal fields into Elemental fields using an averaging process, result is computed on a given elements scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are splitted by element shape and the output fields container has elshape label.

      available inputs:
        - fields_container (FieldsContainer)
        - mesh (MeshedRegion, MeshesContainer) (optional)
        - scoping (Scoping, ScopingsContainer) (optional)
        - collapse_shell_layers (bool) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.nodal_to_elemental_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.nodal_to_elemental_fc(fields_container=my_fields_container,mesh=my_mesh,scoping=my_scoping,collapse_shell_layers=my_collapse_shell_layers)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, scoping=None, collapse_shell_layers=None, config=None, server=None):
        super().__init__(name="nodal_to_elemental_fc", config = config, server = server)
        self._inputs = InputsNodalToElementalFc(self)
        self._outputs = OutputsNodalToElementalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform Nodal fields into Elemental fields using an averaging process, result is computed on a given elements scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are splitted by element shape and the output fields container has elshape label.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping","scopings_container"], optional=True, document="""average only on these elements, if it is scoping container, the label must correspond to the one of the fields container"""), 
                                 10 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""if true shell layers are averaged as well (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "nodal_to_elemental_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNodalToElementalFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNodalToElementalFc 
        """
        return super().outputs


#internal name: nodal_to_elemental_fc
#scripting name: nodal_to_elemental_fc
class InputsNodalToElementalFc(_Inputs):
    """Intermediate class used to connect user inputs to nodal_to_elemental_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_to_elemental_fc._spec().inputs, op)
        self._fields_container = Input(nodal_to_elemental_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._mesh = Input(nodal_to_elemental_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)
        self._scoping = Input(nodal_to_elemental_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._scoping)
        self._collapse_shell_layers = Input(nodal_to_elemental_fc._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self._collapse_shell_layers)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: the mesh region in this pin is used to perform the averaging, if there is no field's support it is used

        Parameters
        ----------
        my_mesh : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator

        - pindoc: average only on these elements, if it is scoping container, the label must correspond to the one of the fields container

        Parameters
        ----------
        my_scoping : Scoping, ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> #or
        >>> op.inputs.scoping(my_scoping)

        """
        return self._scoping

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

        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
        >>> #or
        >>> op.inputs.collapse_shell_layers(my_collapse_shell_layers)

        """
        return self._collapse_shell_layers

class OutputsNodalToElementalFc(_Outputs):
    """Intermediate class used to get outputs from nodal_to_elemental_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_to_elemental_fc._spec().outputs, op)
        self._fields_container = Output(nodal_to_elemental_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

