"""
split_fields
============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "mesh" category
"""

class split_fields(Operator):
    """Split the input field or fields container based on the input mesh regions 

      available inputs:
        - field_or_fields_container (Field, FieldsContainer)
        - mesh_controller (MeshesContainer)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.split_fields()

      >>> # Make input connections
      >>> my_field_or_fields_container = dpf.Field()
      >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
      >>> my_mesh_controller = dpf.MeshesContainer()
      >>> op.inputs.mesh_controller.connect(my_mesh_controller)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.split_fields(field_or_fields_container=my_field_or_fields_container,mesh_controller=my_mesh_controller)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field_or_fields_container=None, mesh_controller=None, config=None, server=None):
        super().__init__(name="split_fields", config = config, server = server)
        self._inputs = InputsSplitFields(self)
        self._outputs = OutputsSplitFields(self)
        if field_or_fields_container !=None:
            self.inputs.field_or_fields_container.connect(field_or_fields_container)
        if mesh_controller !=None:
            self.inputs.mesh_controller.connect(mesh_controller)

    @staticmethod
    def _spec():
        spec = Specification(description="""Split the input field or fields container based on the input mesh regions """,
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field_or_fields_container", type_names=["field","fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh_controller", type_names=["meshes_container"], optional=False, document="""body meshes in the mesh controller cannot be mixed shell/solid""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "split_fields")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSplitFields 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSplitFields 
        """
        return super().outputs


#internal name: split_fields
#scripting name: split_fields
class InputsSplitFields(_Inputs):
    """Intermediate class used to connect user inputs to split_fields operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.split_fields()
      >>> my_field_or_fields_container = dpf.Field()
      >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
      >>> my_mesh_controller = dpf.MeshesContainer()
      >>> op.inputs.mesh_controller.connect(my_mesh_controller)
    """
    def __init__(self, op: Operator):
        super().__init__(split_fields._spec().inputs, op)
        self._field_or_fields_container = Input(split_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field_or_fields_container)
        self._mesh_controller = Input(split_fields._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_controller)

    @property
    def field_or_fields_container(self):
        """Allows to connect field_or_fields_container input to the operator

        Parameters
        ----------
        my_field_or_fields_container : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.split_fields()
        >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
        >>> #or
        >>> op.inputs.field_or_fields_container(my_field_or_fields_container)

        """
        return self._field_or_fields_container

    @property
    def mesh_controller(self):
        """Allows to connect mesh_controller input to the operator

        - pindoc: body meshes in the mesh controller cannot be mixed shell/solid

        Parameters
        ----------
        my_mesh_controller : MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.split_fields()
        >>> op.inputs.mesh_controller.connect(my_mesh_controller)
        >>> #or
        >>> op.inputs.mesh_controller(my_mesh_controller)

        """
        return self._mesh_controller

class OutputsSplitFields(_Outputs):
    """Intermediate class used to get outputs from split_fields operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.split_fields()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(split_fields._spec().outputs, op)
        self._fields_container = Output(split_fields._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.mesh.split_fields()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

