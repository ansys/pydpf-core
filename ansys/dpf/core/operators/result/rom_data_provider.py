"""
rom_data_provider
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class rom_data_provider(Operator):
    """Set the required data for the invariant terms computation (reduced matrices, lumped mass matrix, modes ...)

      available inputs:
        - rom_type (bool)
        - reduced_stiff_matrix (FieldsContainer)
        - reduced_damping_matrix (FieldsContainer)
        - reduced_mass_matrix (FieldsContainer)
        - data_sources (DataSources)
        - reduced_rhs_vector (FieldsContainer)
        - lumped_mass_matrix (FieldsContainer)
        - mode_shapes (FieldsContainer)

      available outputs:
        - rom_matrices (FieldsContainer)
        - mode_shapes (FieldsContainer)
        - lumped_mass (FieldsContainer)
        - model_data (PropertyField)
        - center_of_mass (PropertyField)
        - inertia_relief (Field)
        - model_size (float)
        - field_coordinates_and_euler_angles (float)
        - nod (list)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.rom_data_provider()

      >>> # Make input connections
      >>> my_rom_type = bool()
      >>> op.inputs.rom_type.connect(my_rom_type)
      >>> my_reduced_stiff_matrix = dpf.FieldsContainer()
      >>> op.inputs.reduced_stiff_matrix.connect(my_reduced_stiff_matrix)
      >>> my_reduced_damping_matrix = dpf.FieldsContainer()
      >>> op.inputs.reduced_damping_matrix.connect(my_reduced_damping_matrix)
      >>> my_reduced_mass_matrix = dpf.FieldsContainer()
      >>> op.inputs.reduced_mass_matrix.connect(my_reduced_mass_matrix)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_reduced_rhs_vector = dpf.FieldsContainer()
      >>> op.inputs.reduced_rhs_vector.connect(my_reduced_rhs_vector)
      >>> my_lumped_mass_matrix = dpf.FieldsContainer()
      >>> op.inputs.lumped_mass_matrix.connect(my_lumped_mass_matrix)
      >>> my_mode_shapes = dpf.FieldsContainer()
      >>> op.inputs.mode_shapes.connect(my_mode_shapes)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.rom_data_provider(rom_type=my_rom_type,reduced_stiff_matrix=my_reduced_stiff_matrix,reduced_damping_matrix=my_reduced_damping_matrix,reduced_mass_matrix=my_reduced_mass_matrix,data_sources=my_data_sources,reduced_rhs_vector=my_reduced_rhs_vector,lumped_mass_matrix=my_lumped_mass_matrix,mode_shapes=my_mode_shapes)

      >>> # Get output data
      >>> result_rom_matrices = op.outputs.rom_matrices()
      >>> result_mode_shapes = op.outputs.mode_shapes()
      >>> result_lumped_mass = op.outputs.lumped_mass()
      >>> result_model_data = op.outputs.model_data()
      >>> result_center_of_mass = op.outputs.center_of_mass()
      >>> result_inertia_relief = op.outputs.inertia_relief()
      >>> result_model_size = op.outputs.model_size()
      >>> result_field_coordinates_and_euler_angles = op.outputs.field_coordinates_and_euler_angles()
      >>> result_nod = op.outputs.nod()"""
    def __init__(self, rom_type=None, reduced_stiff_matrix=None, reduced_damping_matrix=None, reduced_mass_matrix=None, data_sources=None, reduced_rhs_vector=None, lumped_mass_matrix=None, mode_shapes=None, config=None, server=None):
        super().__init__(name="rom_data_provider", config = config, server = server)
        self._inputs = InputsRomDataProvider(self)
        self._outputs = OutputsRomDataProvider(self)
        if rom_type !=None:
            self.inputs.rom_type.connect(rom_type)
        if reduced_stiff_matrix !=None:
            self.inputs.reduced_stiff_matrix.connect(reduced_stiff_matrix)
        if reduced_damping_matrix !=None:
            self.inputs.reduced_damping_matrix.connect(reduced_damping_matrix)
        if reduced_mass_matrix !=None:
            self.inputs.reduced_mass_matrix.connect(reduced_mass_matrix)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if reduced_rhs_vector !=None:
            self.inputs.reduced_rhs_vector.connect(reduced_rhs_vector)
        if lumped_mass_matrix !=None:
            self.inputs.lumped_mass_matrix.connect(lumped_mass_matrix)
        if mode_shapes !=None:
            self.inputs.mode_shapes.connect(mode_shapes)

    @staticmethod
    def _spec():
        spec = Specification(description="""Set the required data for the invariant terms computation (reduced matrices, lumped mass matrix, modes ...)""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "rom_type", type_names=["bool"], optional=False, document="""If this pin is set to true, customized rom data must be given"""), 
                                 1 : PinSpecification(name = "reduced_stiff_matrix", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the reduced Stiffness matrix"""), 
                                 2 : PinSpecification(name = "reduced_damping_matrix", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the reduced Mass matrix"""), 
                                 3 : PinSpecification(name = "reduced_mass_matrix", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the reduced Damp matrix"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document=""""""), 
                                 5 : PinSpecification(name = "reduced_rhs_vector", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the reduced RHS vector"""), 
                                 6 : PinSpecification(name = "lumped_mass_matrix", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the lumped Mass matrix"""), 
                                 7 : PinSpecification(name = "mode_shapes", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the customized mode shapes""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "rom_matrices", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the reduced matrices"""), 
                                 1 : PinSpecification(name = "mode_shapes", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the mode shapes, which are CST and NOR for the cms method"""), 
                                 2 : PinSpecification(name = "lumped_mass", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the lumped mass"""), 
                                 3 : PinSpecification(name = "model_data", type_names=["property_field"], optional=False, document="""data describing the finite element model"""), 
                                 4 : PinSpecification(name = "center_of_mass", type_names=["property_field"], optional=False, document=""""""), 
                                 5 : PinSpecification(name = "inertia_relief", type_names=["field"], optional=False, document="""inertia matrix"""), 
                                 6 : PinSpecification(name = "model_size", type_names=["double"], optional=False, document="""size of the model"""), 
                                 7 : PinSpecification(name = "field_coordinates_and_euler_angles", type_names=["double"], optional=False, document="""coordinates and euler angles of all nodes"""), 
                                 8 : PinSpecification(name = "nod", type_names=["vector<int32>"], optional=False, document="""ids of master nodes""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "rom_data_provider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRomDataProvider 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRomDataProvider 
        """
        return super().outputs


#internal name: rom_data_provider
#scripting name: rom_data_provider
class InputsRomDataProvider(_Inputs):
    """Intermediate class used to connect user inputs to rom_data_provider operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.rom_data_provider()
      >>> my_rom_type = bool()
      >>> op.inputs.rom_type.connect(my_rom_type)
      >>> my_reduced_stiff_matrix = dpf.FieldsContainer()
      >>> op.inputs.reduced_stiff_matrix.connect(my_reduced_stiff_matrix)
      >>> my_reduced_damping_matrix = dpf.FieldsContainer()
      >>> op.inputs.reduced_damping_matrix.connect(my_reduced_damping_matrix)
      >>> my_reduced_mass_matrix = dpf.FieldsContainer()
      >>> op.inputs.reduced_mass_matrix.connect(my_reduced_mass_matrix)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_reduced_rhs_vector = dpf.FieldsContainer()
      >>> op.inputs.reduced_rhs_vector.connect(my_reduced_rhs_vector)
      >>> my_lumped_mass_matrix = dpf.FieldsContainer()
      >>> op.inputs.lumped_mass_matrix.connect(my_lumped_mass_matrix)
      >>> my_mode_shapes = dpf.FieldsContainer()
      >>> op.inputs.mode_shapes.connect(my_mode_shapes)
    """
    def __init__(self, op: Operator):
        super().__init__(rom_data_provider._spec().inputs, op)
        self._rom_type = Input(rom_data_provider._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._rom_type)
        self._reduced_stiff_matrix = Input(rom_data_provider._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._reduced_stiff_matrix)
        self._reduced_damping_matrix = Input(rom_data_provider._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._reduced_damping_matrix)
        self._reduced_mass_matrix = Input(rom_data_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._reduced_mass_matrix)
        self._data_sources = Input(rom_data_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._reduced_rhs_vector = Input(rom_data_provider._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._reduced_rhs_vector)
        self._lumped_mass_matrix = Input(rom_data_provider._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self._lumped_mass_matrix)
        self._mode_shapes = Input(rom_data_provider._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mode_shapes)

    @property
    def rom_type(self):
        """Allows to connect rom_type input to the operator

        - pindoc: If this pin is set to true, customized rom data must be given

        Parameters
        ----------
        my_rom_type : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> op.inputs.rom_type.connect(my_rom_type)
        >>> #or
        >>> op.inputs.rom_type(my_rom_type)

        """
        return self._rom_type

    @property
    def reduced_stiff_matrix(self):
        """Allows to connect reduced_stiff_matrix input to the operator

        - pindoc: FieldsContainers containing the reduced Stiffness matrix

        Parameters
        ----------
        my_reduced_stiff_matrix : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> op.inputs.reduced_stiff_matrix.connect(my_reduced_stiff_matrix)
        >>> #or
        >>> op.inputs.reduced_stiff_matrix(my_reduced_stiff_matrix)

        """
        return self._reduced_stiff_matrix

    @property
    def reduced_damping_matrix(self):
        """Allows to connect reduced_damping_matrix input to the operator

        - pindoc: FieldsContainers containing the reduced Mass matrix

        Parameters
        ----------
        my_reduced_damping_matrix : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> op.inputs.reduced_damping_matrix.connect(my_reduced_damping_matrix)
        >>> #or
        >>> op.inputs.reduced_damping_matrix(my_reduced_damping_matrix)

        """
        return self._reduced_damping_matrix

    @property
    def reduced_mass_matrix(self):
        """Allows to connect reduced_mass_matrix input to the operator

        - pindoc: FieldsContainers containing the reduced Damp matrix

        Parameters
        ----------
        my_reduced_mass_matrix : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> op.inputs.reduced_mass_matrix.connect(my_reduced_mass_matrix)
        >>> #or
        >>> op.inputs.reduced_mass_matrix(my_reduced_mass_matrix)

        """
        return self._reduced_mass_matrix

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def reduced_rhs_vector(self):
        """Allows to connect reduced_rhs_vector input to the operator

        - pindoc: FieldsContainers containing the reduced RHS vector

        Parameters
        ----------
        my_reduced_rhs_vector : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> op.inputs.reduced_rhs_vector.connect(my_reduced_rhs_vector)
        >>> #or
        >>> op.inputs.reduced_rhs_vector(my_reduced_rhs_vector)

        """
        return self._reduced_rhs_vector

    @property
    def lumped_mass_matrix(self):
        """Allows to connect lumped_mass_matrix input to the operator

        - pindoc: FieldsContainers containing the lumped Mass matrix

        Parameters
        ----------
        my_lumped_mass_matrix : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> op.inputs.lumped_mass_matrix.connect(my_lumped_mass_matrix)
        >>> #or
        >>> op.inputs.lumped_mass_matrix(my_lumped_mass_matrix)

        """
        return self._lumped_mass_matrix

    @property
    def mode_shapes(self):
        """Allows to connect mode_shapes input to the operator

        - pindoc: FieldsContainers containing the customized mode shapes

        Parameters
        ----------
        my_mode_shapes : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> op.inputs.mode_shapes.connect(my_mode_shapes)
        >>> #or
        >>> op.inputs.mode_shapes(my_mode_shapes)

        """
        return self._mode_shapes

class OutputsRomDataProvider(_Outputs):
    """Intermediate class used to get outputs from rom_data_provider operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.rom_data_provider()
      >>> # Connect inputs : op.inputs. ...
      >>> result_rom_matrices = op.outputs.rom_matrices()
      >>> result_mode_shapes = op.outputs.mode_shapes()
      >>> result_lumped_mass = op.outputs.lumped_mass()
      >>> result_model_data = op.outputs.model_data()
      >>> result_center_of_mass = op.outputs.center_of_mass()
      >>> result_inertia_relief = op.outputs.inertia_relief()
      >>> result_model_size = op.outputs.model_size()
      >>> result_field_coordinates_and_euler_angles = op.outputs.field_coordinates_and_euler_angles()
      >>> result_nod = op.outputs.nod()
    """
    def __init__(self, op: Operator):
        super().__init__(rom_data_provider._spec().outputs, op)
        self._rom_matrices = Output(rom_data_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self._rom_matrices)
        self._mode_shapes = Output(rom_data_provider._spec().output_pin(1), 1, op) 
        self._outputs.append(self._mode_shapes)
        self._lumped_mass = Output(rom_data_provider._spec().output_pin(2), 2, op) 
        self._outputs.append(self._lumped_mass)
        self._model_data = Output(rom_data_provider._spec().output_pin(3), 3, op) 
        self._outputs.append(self._model_data)
        self._center_of_mass = Output(rom_data_provider._spec().output_pin(4), 4, op) 
        self._outputs.append(self._center_of_mass)
        self._inertia_relief = Output(rom_data_provider._spec().output_pin(5), 5, op) 
        self._outputs.append(self._inertia_relief)
        self._model_size = Output(rom_data_provider._spec().output_pin(6), 6, op) 
        self._outputs.append(self._model_size)
        self._field_coordinates_and_euler_angles = Output(rom_data_provider._spec().output_pin(7), 7, op) 
        self._outputs.append(self._field_coordinates_and_euler_angles)
        self._nod = Output(rom_data_provider._spec().output_pin(8), 8, op) 
        self._outputs.append(self._nod)

    @property
    def rom_matrices(self):
        """Allows to get rom_matrices output of the operator


        - pindoc: FieldsContainers containing the reduced matrices

        Returns
        ----------
        my_rom_matrices : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_rom_matrices = op.outputs.rom_matrices() 
        """
        return self._rom_matrices

    @property
    def mode_shapes(self):
        """Allows to get mode_shapes output of the operator


        - pindoc: FieldsContainers containing the mode shapes, which are CST and NOR for the cms method

        Returns
        ----------
        my_mode_shapes : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mode_shapes = op.outputs.mode_shapes() 
        """
        return self._mode_shapes

    @property
    def lumped_mass(self):
        """Allows to get lumped_mass output of the operator


        - pindoc: FieldsContainers containing the lumped mass

        Returns
        ----------
        my_lumped_mass : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_lumped_mass = op.outputs.lumped_mass() 
        """
        return self._lumped_mass

    @property
    def model_data(self):
        """Allows to get model_data output of the operator


        - pindoc: data describing the finite element model

        Returns
        ----------
        my_model_data : PropertyField, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_model_data = op.outputs.model_data() 
        """
        return self._model_data

    @property
    def center_of_mass(self):
        """Allows to get center_of_mass output of the operator


        Returns
        ----------
        my_center_of_mass : PropertyField, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_center_of_mass = op.outputs.center_of_mass() 
        """
        return self._center_of_mass

    @property
    def inertia_relief(self):
        """Allows to get inertia_relief output of the operator


        - pindoc: inertia matrix

        Returns
        ----------
        my_inertia_relief : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_inertia_relief = op.outputs.inertia_relief() 
        """
        return self._inertia_relief

    @property
    def model_size(self):
        """Allows to get model_size output of the operator


        - pindoc: size of the model

        Returns
        ----------
        my_model_size : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_model_size = op.outputs.model_size() 
        """
        return self._model_size

    @property
    def field_coordinates_and_euler_angles(self):
        """Allows to get field_coordinates_and_euler_angles output of the operator


        - pindoc: coordinates and euler angles of all nodes

        Returns
        ----------
        my_field_coordinates_and_euler_angles : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_coordinates_and_euler_angles = op.outputs.field_coordinates_and_euler_angles() 
        """
        return self._field_coordinates_and_euler_angles

    @property
    def nod(self):
        """Allows to get nod output of the operator


        - pindoc: ids of master nodes

        Returns
        ----------
        my_nod : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rom_data_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_nod = op.outputs.nod() 
        """
        return self._nod

