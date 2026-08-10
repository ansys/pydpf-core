"""
modal_superposition
===================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class modal_superposition(Operator):
    """Computes the solution in the time/frequency space from a modal solution by multiplying a modal basis (in 0)by the solution in this modal space (coefficients for each mode for each time/frequency) (in 1).

      available inputs:
        - modal_basis (FieldsContainer, CustomTypeFieldsContainer)
        - solution_in_modal_space (FieldsContainer, CustomTypeFieldsContainer)
        - incremental_fc (FieldsContainer, CustomTypeFieldsContainer) (optional)
        - time_scoping (Scoping, ScopingsContainer) (optional)
        - mesh_scoping (Scoping, ScopingsContainer) (optional)

      available outputs:
        - fields_container (FieldsContainer ,CustomTypeFieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.modal_superposition()

      >>> # Make input connections
      >>> my_modal_basis = dpf.FieldsContainer()
      >>> op.inputs.modal_basis.connect(my_modal_basis)
      >>> my_solution_in_modal_space = dpf.FieldsContainer()
      >>> op.inputs.solution_in_modal_space.connect(my_solution_in_modal_space)
      >>> my_incremental_fc = dpf.FieldsContainer()
      >>> op.inputs.incremental_fc.connect(my_incremental_fc)
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.modal_superposition(modal_basis=my_modal_basis,solution_in_modal_space=my_solution_in_modal_space,incremental_fc=my_incremental_fc,time_scoping=my_time_scoping,mesh_scoping=my_mesh_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, modal_basis=None, solution_in_modal_space=None, incremental_fc=None, time_scoping=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="expansion::modal_superposition", config = config, server = server)
        self._inputs = InputsModalSuperposition(self)
        self._outputs = OutputsModalSuperposition(self)
        if modal_basis !=None:
            self.inputs.modal_basis.connect(modal_basis)
        if solution_in_modal_space !=None:
            self.inputs.solution_in_modal_space.connect(solution_in_modal_space)
        if incremental_fc !=None:
            self.inputs.incremental_fc.connect(incremental_fc)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the solution in the time/frequency space from a modal solution by multiplying a modal basis (in 0)by the solution in this modal space (coefficients for each mode for each time/frequency) (in 1).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "modal_basis", type_names=["fields_container","custom_type_fields_container"], optional=False, document="""One field by mode with each field representing a mode shape on nodes or elements."""), 
                                 1 : PinSpecification(name = "solution_in_modal_space", type_names=["fields_container","custom_type_fields_container"], optional=False, document="""One field by time/frequency with each field having a ponderating coefficient for each mode of the modal_basis pin."""), 
                                 2 : PinSpecification(name = "incremental_fc", type_names=["fields_container","custom_type_fields_container"], optional=True, document="""If a non-empty fields container is introduced, it is modified, and sent to the output, to add the contribution of the requested expansion. The label spaces produced from the multiplication must be the same as the incremental ones."""), 
                                 3 : PinSpecification(name = "time_scoping", type_names=["scoping","scopings_container"], optional=True, document="""Compute the result on a subset of the time frequency domain defined in the solution_in_modal_space fields container."""), 
                                 4 : PinSpecification(name = "mesh_scoping", type_names=["scoping","scopings_container"], optional=True, document="""Compute the result on a subset of the space domain defined in the modal_basis fields container.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container","custom_type_fields_container"], optional=False, document="""Expanded mode superposition solution.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "expansion::modal_superposition")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsModalSuperposition 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsModalSuperposition 
        """
        return super().outputs


#internal name: expansion::modal_superposition
#scripting name: modal_superposition
class InputsModalSuperposition(_Inputs):
    """Intermediate class used to connect user inputs to modal_superposition operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.modal_superposition()
      >>> my_modal_basis = dpf.FieldsContainer()
      >>> op.inputs.modal_basis.connect(my_modal_basis)
      >>> my_solution_in_modal_space = dpf.FieldsContainer()
      >>> op.inputs.solution_in_modal_space.connect(my_solution_in_modal_space)
      >>> my_incremental_fc = dpf.FieldsContainer()
      >>> op.inputs.incremental_fc.connect(my_incremental_fc)
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(modal_superposition._spec().inputs, op)
        self._modal_basis = Input(modal_superposition._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._modal_basis)
        self._solution_in_modal_space = Input(modal_superposition._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._solution_in_modal_space)
        self._incremental_fc = Input(modal_superposition._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._incremental_fc)
        self._time_scoping = Input(modal_superposition._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(modal_superposition._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._mesh_scoping)

    @property
    def modal_basis(self):
        """Allows to connect modal_basis input to the operator

        - pindoc: One field by mode with each field representing a mode shape on nodes or elements.

        Parameters
        ----------
        my_modal_basis : FieldsContainer, CustomTypeFieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.modal_superposition()
        >>> op.inputs.modal_basis.connect(my_modal_basis)
        >>> #or
        >>> op.inputs.modal_basis(my_modal_basis)

        """
        return self._modal_basis

    @property
    def solution_in_modal_space(self):
        """Allows to connect solution_in_modal_space input to the operator

        - pindoc: One field by time/frequency with each field having a ponderating coefficient for each mode of the modal_basis pin.

        Parameters
        ----------
        my_solution_in_modal_space : FieldsContainer, CustomTypeFieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.modal_superposition()
        >>> op.inputs.solution_in_modal_space.connect(my_solution_in_modal_space)
        >>> #or
        >>> op.inputs.solution_in_modal_space(my_solution_in_modal_space)

        """
        return self._solution_in_modal_space

    @property
    def incremental_fc(self):
        """Allows to connect incremental_fc input to the operator

        - pindoc: If a non-empty fields container is introduced, it is modified, and sent to the output, to add the contribution of the requested expansion. The label spaces produced from the multiplication must be the same as the incremental ones.

        Parameters
        ----------
        my_incremental_fc : FieldsContainer, CustomTypeFieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.modal_superposition()
        >>> op.inputs.incremental_fc.connect(my_incremental_fc)
        >>> #or
        >>> op.inputs.incremental_fc(my_incremental_fc)

        """
        return self._incremental_fc

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        - pindoc: Compute the result on a subset of the time frequency domain defined in the solution_in_modal_space fields container.

        Parameters
        ----------
        my_time_scoping : Scoping, ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.modal_superposition()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        - pindoc: Compute the result on a subset of the space domain defined in the modal_basis fields container.

        Parameters
        ----------
        my_mesh_scoping : Scoping, ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.modal_superposition()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

class OutputsModalSuperposition(_Outputs):
    """Intermediate class used to get outputs from modal_superposition operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.modal_superposition()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(modal_superposition._spec().outputs, op)
        self.fields_container_as_fields_container = Output( _modify_output_spec_with_one_type(modal_superposition._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.fields_container_as_fields_container)
        self.fields_container_as_custom_type_fields_container = Output( _modify_output_spec_with_one_type(modal_superposition._spec().output_pin(0), "custom_type_fields_container"), 0, op) 
        self._outputs.append(self.fields_container_as_custom_type_fields_container)

