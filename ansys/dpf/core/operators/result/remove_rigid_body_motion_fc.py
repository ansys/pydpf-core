"""
remove_rigid_body_motion_fc
===========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "result" category
"""

class remove_rigid_body_motion_fc(Operator):
    """Removes rigid body mode from a total displacement field by minimization. Use a reference point in order to substract its displacement to the result displacement field.

      available inputs:
        - fields_container (FieldsContainer)
        - reference_node_id (int) (optional)
        - mesh (MeshedRegion) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.remove_rigid_body_motion_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_reference_node_id = int()
      >>> op.inputs.reference_node_id.connect(my_reference_node_id)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.remove_rigid_body_motion_fc(fields_container=my_fields_container,reference_node_id=my_reference_node_id,mesh=my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, reference_node_id=None, mesh=None, config=None, server=None):
        super().__init__(name="ExtractRigidBodyMotion_fc", config = config, server = server)
        self._inputs = InputsRemoveRigidBodyMotionFc(self)
        self._outputs = OutputsRemoveRigidBodyMotionFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if reference_node_id !=None:
            self.inputs.reference_node_id.connect(reference_node_id)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Removes rigid body mode from a total displacement field by minimization. Use a reference point in order to substract its displacement to the result displacement field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "reference_node_id", type_names=["int32"], optional=True, document="""Id of the reference entity (node)."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""default is the mesh in the support""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ExtractRigidBodyMotion_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRemoveRigidBodyMotionFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRemoveRigidBodyMotionFc 
        """
        return super().outputs


#internal name: ExtractRigidBodyMotion_fc
#scripting name: remove_rigid_body_motion_fc
class InputsRemoveRigidBodyMotionFc(_Inputs):
    """Intermediate class used to connect user inputs to remove_rigid_body_motion_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.remove_rigid_body_motion_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_reference_node_id = int()
      >>> op.inputs.reference_node_id.connect(my_reference_node_id)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(remove_rigid_body_motion_fc._spec().inputs, op)
        self._fields_container = Input(remove_rigid_body_motion_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._reference_node_id = Input(remove_rigid_body_motion_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._reference_node_id)
        self._mesh = Input(remove_rigid_body_motion_fc._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.remove_rigid_body_motion_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def reference_node_id(self):
        """Allows to connect reference_node_id input to the operator

        - pindoc: Id of the reference entity (node).

        Parameters
        ----------
        my_reference_node_id : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.remove_rigid_body_motion_fc()
        >>> op.inputs.reference_node_id.connect(my_reference_node_id)
        >>> #or
        >>> op.inputs.reference_node_id(my_reference_node_id)

        """
        return self._reference_node_id

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: default is the mesh in the support

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.remove_rigid_body_motion_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsRemoveRigidBodyMotionFc(_Outputs):
    """Intermediate class used to get outputs from remove_rigid_body_motion_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.remove_rigid_body_motion_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(remove_rigid_body_motion_fc._spec().outputs, op)
        self._fields_container = Output(remove_rigid_body_motion_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.remove_rigid_body_motion_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

