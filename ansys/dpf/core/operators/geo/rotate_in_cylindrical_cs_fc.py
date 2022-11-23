"""
rotate_in_cylindrical_cs_fc
===========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "geo" category
"""

class rotate_in_cylindrical_cs_fc(Operator):
    """Rotate all the fields of a fields container (not defined with a cynlindrical coordinate system) to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.

      available inputs:
        - field (Field, FieldsContainer)
        - coordinate_system (Field) (optional)
        - mesh (MeshedRegion) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.rotate_in_cylindrical_cs_fc()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_coordinate_system = dpf.Field()
      >>> op.inputs.coordinate_system.connect(my_coordinate_system)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.geo.rotate_in_cylindrical_cs_fc(field=my_field,coordinate_system=my_coordinate_system,mesh=my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field=None, coordinate_system=None, mesh=None, config=None, server=None):
        super().__init__(name="transform_cylindrical_cs_fc", config = config, server = server)
        self._inputs = InputsRotateInCylindricalCsFc(self)
        self._outputs = OutputsRotateInCylindricalCsFc(self)
        if field !=None:
            self.inputs.field.connect(field)
        if coordinate_system !=None:
            self.inputs.coordinate_system.connect(coordinate_system)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rotate all the fields of a fields container (not defined with a cynlindrical coordinate system) to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "coordinate_system", type_names=["field"], optional=True, document="""3-3 rotation matrix and origin coordinates must be set here to define a coordinate system."""), 
                                 2 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""mesh support of the input fields_container, in case it does not have one defined.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "transform_cylindrical_cs_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRotateInCylindricalCsFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRotateInCylindricalCsFc 
        """
        return super().outputs


#internal name: transform_cylindrical_cs_fc
#scripting name: rotate_in_cylindrical_cs_fc
class InputsRotateInCylindricalCsFc(_Inputs):
    """Intermediate class used to connect user inputs to rotate_in_cylindrical_cs_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.rotate_in_cylindrical_cs_fc()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_coordinate_system = dpf.Field()
      >>> op.inputs.coordinate_system.connect(my_coordinate_system)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(rotate_in_cylindrical_cs_fc._spec().inputs, op)
        self._field = Input(rotate_in_cylindrical_cs_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._coordinate_system = Input(rotate_in_cylindrical_cs_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._coordinate_system)
        self._mesh = Input(rotate_in_cylindrical_cs_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def field(self):
        """Allows to connect field input to the operator

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.rotate_in_cylindrical_cs_fc()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def coordinate_system(self):
        """Allows to connect coordinate_system input to the operator

        - pindoc: 3-3 rotation matrix and origin coordinates must be set here to define a coordinate system.

        Parameters
        ----------
        my_coordinate_system : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.rotate_in_cylindrical_cs_fc()
        >>> op.inputs.coordinate_system.connect(my_coordinate_system)
        >>> #or
        >>> op.inputs.coordinate_system(my_coordinate_system)

        """
        return self._coordinate_system

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: mesh support of the input fields_container, in case it does not have one defined.

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.rotate_in_cylindrical_cs_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsRotateInCylindricalCsFc(_Outputs):
    """Intermediate class used to get outputs from rotate_in_cylindrical_cs_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.rotate_in_cylindrical_cs_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(rotate_in_cylindrical_cs_fc._spec().outputs, op)
        self._fields_container = Output(rotate_in_cylindrical_cs_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.geo.rotate_in_cylindrical_cs_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

