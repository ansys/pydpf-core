"""
add_rigid_body_motion_fc
========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "result" category
"""

class add_rigid_body_motion_fc(Operator):
    """Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem

      available inputs:
        - fields_container (FieldsContainer)
        - translation_field (Field)
        - rotation_field (Field)
        - center_field (Field)
        - mesh (MeshedRegion) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.add_rigid_body_motion_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_translation_field = dpf.Field()
      >>> op.inputs.translation_field.connect(my_translation_field)
      >>> my_rotation_field = dpf.Field()
      >>> op.inputs.rotation_field.connect(my_rotation_field)
      >>> my_center_field = dpf.Field()
      >>> op.inputs.center_field.connect(my_center_field)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.add_rigid_body_motion_fc(fields_container=my_fields_container,translation_field=my_translation_field,rotation_field=my_rotation_field,center_field=my_center_field,mesh=my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, translation_field=None, rotation_field=None, center_field=None, mesh=None, config=None, server=None):
        super().__init__(name="RigidBodyAddition_fc", config = config, server = server)
        self._inputs = InputsAddRigidBodyMotionFc(self)
        self._outputs = OutputsAddRigidBodyMotionFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if translation_field !=None:
            self.inputs.translation_field.connect(translation_field)
        if rotation_field !=None:
            self.inputs.rotation_field.connect(rotation_field)
        if center_field !=None:
            self.inputs.center_field.connect(center_field)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "translation_field", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "rotation_field", type_names=["field"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "center_field", type_names=["field"], optional=False, document=""""""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""default is the mesh in the support""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "RigidBodyAddition_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAddRigidBodyMotionFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAddRigidBodyMotionFc 
        """
        return super().outputs


#internal name: RigidBodyAddition_fc
#scripting name: add_rigid_body_motion_fc
class InputsAddRigidBodyMotionFc(_Inputs):
    """Intermediate class used to connect user inputs to add_rigid_body_motion_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.add_rigid_body_motion_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_translation_field = dpf.Field()
      >>> op.inputs.translation_field.connect(my_translation_field)
      >>> my_rotation_field = dpf.Field()
      >>> op.inputs.rotation_field.connect(my_rotation_field)
      >>> my_center_field = dpf.Field()
      >>> op.inputs.center_field.connect(my_center_field)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(add_rigid_body_motion_fc._spec().inputs, op)
        self._fields_container = Input(add_rigid_body_motion_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._translation_field = Input(add_rigid_body_motion_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._translation_field)
        self._rotation_field = Input(add_rigid_body_motion_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._rotation_field)
        self._center_field = Input(add_rigid_body_motion_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._center_field)
        self._mesh = Input(add_rigid_body_motion_fc._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.add_rigid_body_motion_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def translation_field(self):
        """Allows to connect translation_field input to the operator

        Parameters
        ----------
        my_translation_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.add_rigid_body_motion_fc()
        >>> op.inputs.translation_field.connect(my_translation_field)
        >>> #or
        >>> op.inputs.translation_field(my_translation_field)

        """
        return self._translation_field

    @property
    def rotation_field(self):
        """Allows to connect rotation_field input to the operator

        Parameters
        ----------
        my_rotation_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.add_rigid_body_motion_fc()
        >>> op.inputs.rotation_field.connect(my_rotation_field)
        >>> #or
        >>> op.inputs.rotation_field(my_rotation_field)

        """
        return self._rotation_field

    @property
    def center_field(self):
        """Allows to connect center_field input to the operator

        Parameters
        ----------
        my_center_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.add_rigid_body_motion_fc()
        >>> op.inputs.center_field.connect(my_center_field)
        >>> #or
        >>> op.inputs.center_field(my_center_field)

        """
        return self._center_field

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

        >>> op = dpf.operators.result.add_rigid_body_motion_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsAddRigidBodyMotionFc(_Outputs):
    """Intermediate class used to get outputs from add_rigid_body_motion_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.add_rigid_body_motion_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(add_rigid_body_motion_fc._spec().outputs, op)
        self._fields_container = Output(add_rigid_body_motion_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.add_rigid_body_motion_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

