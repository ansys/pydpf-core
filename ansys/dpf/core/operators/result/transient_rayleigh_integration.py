"""
transient_rayleigh_integration
==============================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class transient_rayleigh_integration(Operator):
    """Computes the transient Rayleigh integral

      available inputs:
        - fields_container (FieldsContainer)
        - mesh (MeshedRegion, MeshesContainer)
        - time_scoping (int, list, Scoping)
        - field (Field)
        - observation_mesh (MeshedRegion)
        - mass_density (float)
        - speed_of_sound (float)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.transient_rayleigh_integration()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_time_scoping = int()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_observation_mesh = dpf.MeshedRegion()
      >>> op.inputs.observation_mesh.connect(my_observation_mesh)
      >>> my_mass_density = float()
      >>> op.inputs.mass_density.connect(my_mass_density)
      >>> my_speed_of_sound = float()
      >>> op.inputs.speed_of_sound.connect(my_speed_of_sound)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.transient_rayleigh_integration(fields_container=my_fields_container,mesh=my_mesh,time_scoping=my_time_scoping,field=my_field,observation_mesh=my_observation_mesh,mass_density=my_mass_density,speed_of_sound=my_speed_of_sound)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, time_scoping=None, field=None, observation_mesh=None, mass_density=None, speed_of_sound=None, config=None, server=None):
        super().__init__(name="transient_rayleigh_integration", config = config, server = server)
        self._inputs = InputsTransientRayleighIntegration(self)
        self._outputs = OutputsTransientRayleighIntegration(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if field !=None:
            self.inputs.field.connect(field)
        if observation_mesh !=None:
            self.inputs.observation_mesh.connect(observation_mesh)
        if mass_density !=None:
            self.inputs.mass_density.connect(mass_density)
        if speed_of_sound !=None:
            self.inputs.speed_of_sound.connect(speed_of_sound)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the transient Rayleigh integral""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=False, document="""The meshes region in this pin has to be boundary or skin mesh. This is the source meshes."""), 
                                 2 : PinSpecification(name = "time_scoping", type_names=["int32","vector<int32>","scoping"], optional=False, document="""Load step number (if it's specified, the Transient rayleigh integration is computed only on the substeps of this step) or time scoping"""), 
                                 3 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""The field represents the coordinates of the observation position. It should be specified if not observation mesh is provided. """), 
                                 4 : PinSpecification(name = "observation_mesh", type_names=["abstract_meshed_region"], optional=False, document="""This is the observation mesh region"""), 
                                 5 : PinSpecification(name = "mass_density", type_names=["double"], optional=False, document="""Mass density (if it's not specified, default value of the air is applied)."""), 
                                 6 : PinSpecification(name = "speed_of_sound", type_names=["double"], optional=False, document="""Speed of sound (if it's not specified, default value of the speed of sound in the air is applied).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "transient_rayleigh_integration")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsTransientRayleighIntegration 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsTransientRayleighIntegration 
        """
        return super().outputs


#internal name: transient_rayleigh_integration
#scripting name: transient_rayleigh_integration
class InputsTransientRayleighIntegration(_Inputs):
    """Intermediate class used to connect user inputs to transient_rayleigh_integration operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.transient_rayleigh_integration()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_time_scoping = int()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_observation_mesh = dpf.MeshedRegion()
      >>> op.inputs.observation_mesh.connect(my_observation_mesh)
      >>> my_mass_density = float()
      >>> op.inputs.mass_density.connect(my_mass_density)
      >>> my_speed_of_sound = float()
      >>> op.inputs.speed_of_sound.connect(my_speed_of_sound)
    """
    def __init__(self, op: Operator):
        super().__init__(transient_rayleigh_integration._spec().inputs, op)
        self._fields_container = Input(transient_rayleigh_integration._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._mesh = Input(transient_rayleigh_integration._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)
        self._time_scoping = Input(transient_rayleigh_integration._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._time_scoping)
        self._field = Input(transient_rayleigh_integration._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._field)
        self._observation_mesh = Input(transient_rayleigh_integration._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._observation_mesh)
        self._mass_density = Input(transient_rayleigh_integration._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._mass_density)
        self._speed_of_sound = Input(transient_rayleigh_integration._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self._speed_of_sound)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.transient_rayleigh_integration()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: The meshes region in this pin has to be boundary or skin mesh. This is the source meshes.

        Parameters
        ----------
        my_mesh : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.transient_rayleigh_integration()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        - pindoc: Load step number (if it's specified, the Transient rayleigh integration is computed only on the substeps of this step) or time scoping

        Parameters
        ----------
        my_time_scoping : int, list, Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.transient_rayleigh_integration()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: The field represents the coordinates of the observation position. It should be specified if not observation mesh is provided. 

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.transient_rayleigh_integration()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def observation_mesh(self):
        """Allows to connect observation_mesh input to the operator

        - pindoc: This is the observation mesh region

        Parameters
        ----------
        my_observation_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.transient_rayleigh_integration()
        >>> op.inputs.observation_mesh.connect(my_observation_mesh)
        >>> #or
        >>> op.inputs.observation_mesh(my_observation_mesh)

        """
        return self._observation_mesh

    @property
    def mass_density(self):
        """Allows to connect mass_density input to the operator

        - pindoc: Mass density (if it's not specified, default value of the air is applied).

        Parameters
        ----------
        my_mass_density : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.transient_rayleigh_integration()
        >>> op.inputs.mass_density.connect(my_mass_density)
        >>> #or
        >>> op.inputs.mass_density(my_mass_density)

        """
        return self._mass_density

    @property
    def speed_of_sound(self):
        """Allows to connect speed_of_sound input to the operator

        - pindoc: Speed of sound (if it's not specified, default value of the speed of sound in the air is applied).

        Parameters
        ----------
        my_speed_of_sound : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.transient_rayleigh_integration()
        >>> op.inputs.speed_of_sound.connect(my_speed_of_sound)
        >>> #or
        >>> op.inputs.speed_of_sound(my_speed_of_sound)

        """
        return self._speed_of_sound

class OutputsTransientRayleighIntegration(_Outputs):
    """Intermediate class used to get outputs from transient_rayleigh_integration operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.transient_rayleigh_integration()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(transient_rayleigh_integration._spec().outputs, op)
        self._fields_container = Output(transient_rayleigh_integration._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.transient_rayleigh_integration()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

