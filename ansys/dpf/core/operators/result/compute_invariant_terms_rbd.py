"""
compute_invariant_terms_rbd
===========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class compute_invariant_terms_rbd(Operator):
    """Set the required data for the invariant terms computation (reduced matrices, lumped mass matrix, modes ...)

      available inputs:
        - rom_matrices (FieldsContainer)
        - mode_shapes (FieldsContainer)
        - lumped_mass (FieldsContainer)
        - model_data (FieldsContainer)
        - center_of_mass (FieldsContainer)
        - inertia_relief (FieldsContainer)
        - model_size (float)
        - field_coordinates (Field)
        - nod (list)

      available outputs:
        - model_data (PropertyField)
        - center_of_mass (Field)
        - inertia_relief (Field)
        - model_size (PropertyField)
        - master_node_coordinates (list)
        - v_trsf (list)
        - k_mat (Field)
        - mass_mat (Field)
        - c_mat (Field)
        - rhs (Field)
        - dn (list)
        - dr_cross_n (list)
        - drn (list)
        - dn_cross_n (list)
        - dnx_y (list)
        - dny_y (list)
        - dnz_y (list)
        - dyx_n (list)
        - dyy_n (list)
        - dyz_n (list)
        - dnxn (list)
        - dnyn (list)
        - dnzn (list)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.compute_invariant_terms_rbd()

      >>> # Make input connections
      >>> my_rom_matrices = dpf.FieldsContainer()
      >>> op.inputs.rom_matrices.connect(my_rom_matrices)
      >>> my_mode_shapes = dpf.FieldsContainer()
      >>> op.inputs.mode_shapes.connect(my_mode_shapes)
      >>> my_lumped_mass = dpf.FieldsContainer()
      >>> op.inputs.lumped_mass.connect(my_lumped_mass)
      >>> my_model_data = dpf.FieldsContainer()
      >>> op.inputs.model_data.connect(my_model_data)
      >>> my_center_of_mass = dpf.FieldsContainer()
      >>> op.inputs.center_of_mass.connect(my_center_of_mass)
      >>> my_inertia_relief = dpf.FieldsContainer()
      >>> op.inputs.inertia_relief.connect(my_inertia_relief)
      >>> my_model_size = float()
      >>> op.inputs.model_size.connect(my_model_size)
      >>> my_field_coordinates = dpf.Field()
      >>> op.inputs.field_coordinates.connect(my_field_coordinates)
      >>> my_nod = dpf.list()
      >>> op.inputs.nod.connect(my_nod)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.compute_invariant_terms_rbd(rom_matrices=my_rom_matrices,mode_shapes=my_mode_shapes,lumped_mass=my_lumped_mass,model_data=my_model_data,center_of_mass=my_center_of_mass,inertia_relief=my_inertia_relief,model_size=my_model_size,field_coordinates=my_field_coordinates,nod=my_nod)

      >>> # Get output data
      >>> result_model_data = op.outputs.model_data()
      >>> result_center_of_mass = op.outputs.center_of_mass()
      >>> result_inertia_relief = op.outputs.inertia_relief()
      >>> result_model_size = op.outputs.model_size()
      >>> result_master_node_coordinates = op.outputs.master_node_coordinates()
      >>> result_v_trsf = op.outputs.v_trsf()
      >>> result_k_mat = op.outputs.k_mat()
      >>> result_mass_mat = op.outputs.mass_mat()
      >>> result_c_mat = op.outputs.c_mat()
      >>> result_rhs = op.outputs.rhs()
      >>> result_dn = op.outputs.dn()
      >>> result_dr_cross_n = op.outputs.dr_cross_n()
      >>> result_drn = op.outputs.drn()
      >>> result_dn_cross_n = op.outputs.dn_cross_n()
      >>> result_dnx_y = op.outputs.dnx_y()
      >>> result_dny_y = op.outputs.dny_y()
      >>> result_dnz_y = op.outputs.dnz_y()
      >>> result_dyx_n = op.outputs.dyx_n()
      >>> result_dyy_n = op.outputs.dyy_n()
      >>> result_dyz_n = op.outputs.dyz_n()
      >>> result_dnxn = op.outputs.dnxn()
      >>> result_dnyn = op.outputs.dnyn()
      >>> result_dnzn = op.outputs.dnzn()"""
    def __init__(self, rom_matrices=None, mode_shapes=None, lumped_mass=None, model_data=None, center_of_mass=None, inertia_relief=None, model_size=None, field_coordinates=None, nod=None, config=None, server=None):
        super().__init__(name="compute_invariant_terms_rbd", config = config, server = server)
        self._inputs = InputsComputeInvariantTermsRbd(self)
        self._outputs = OutputsComputeInvariantTermsRbd(self)
        if rom_matrices !=None:
            self.inputs.rom_matrices.connect(rom_matrices)
        if mode_shapes !=None:
            self.inputs.mode_shapes.connect(mode_shapes)
        if lumped_mass !=None:
            self.inputs.lumped_mass.connect(lumped_mass)
        if model_data !=None:
            self.inputs.model_data.connect(model_data)
        if center_of_mass !=None:
            self.inputs.center_of_mass.connect(center_of_mass)
        if inertia_relief !=None:
            self.inputs.inertia_relief.connect(inertia_relief)
        if model_size !=None:
            self.inputs.model_size.connect(model_size)
        if field_coordinates !=None:
            self.inputs.field_coordinates.connect(field_coordinates)
        if nod !=None:
            self.inputs.nod.connect(nod)

    @staticmethod
    def _spec():
        spec = Specification(description="""Set the required data for the invariant terms computation (reduced matrices, lumped mass matrix, modes ...)""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "rom_matrices", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the reduced matrices"""), 
                                 1 : PinSpecification(name = "mode_shapes", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the mode shapes, which are CST and NOR for the cms method"""), 
                                 2 : PinSpecification(name = "lumped_mass", type_names=["fields_container"], optional=False, document="""FieldsContainers containing the lumped mass"""), 
                                 3 : PinSpecification(name = "model_data", type_names=["fields_container"], optional=False, document="""data describing the finite element model"""), 
                                 4 : PinSpecification(name = "center_of_mass", type_names=["fields_container"], optional=False, document=""""""), 
                                 5 : PinSpecification(name = "inertia_relief", type_names=["fields_container"], optional=False, document="""inertia matrix"""), 
                                 6 : PinSpecification(name = "model_size", type_names=["double"], optional=False, document="""model size"""), 
                                 7 : PinSpecification(name = "field_coordinates", type_names=["field"], optional=False, document="""coordinates of all nodes"""), 
                                 9 : PinSpecification(name = "nod", type_names=["vector<int32>"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "model_data", type_names=["property_field"], optional=False, document="""data describing the finite element model"""), 
                                 1 : PinSpecification(name = "center_of_mass", type_names=["field"], optional=False, document="""center of mass of the body"""), 
                                 2 : PinSpecification(name = "inertia_relief", type_names=["field"], optional=False, document="""inertia matrix"""), 
                                 3 : PinSpecification(name = "model_size", type_names=["property_field"], optional=False, document=""""""), 
                                 4 : PinSpecification(name = "master_node_coordinates", type_names=["vector<double>"], optional=False, document=""""""), 
                                 5 : PinSpecification(name = "v_trsf", type_names=["vector<double>"], optional=False, document="""translational and rotational shape functions"""), 
                                 6 : PinSpecification(name = "k_mat", type_names=["field"], optional=False, document=""""""), 
                                 7 : PinSpecification(name = "mass_mat", type_names=["field"], optional=False, document=""""""), 
                                 8 : PinSpecification(name = "c_mat", type_names=["field"], optional=False, document=""""""), 
                                 9 : PinSpecification(name = "rhs", type_names=["field"], optional=False, document=""""""), 
                                 10 : PinSpecification(name = "dn", type_names=["vector<double>"], optional=False, document=""""""), 
                                 11 : PinSpecification(name = "dr_cross_n", type_names=["vector<double>"], optional=False, document=""""""), 
                                 12 : PinSpecification(name = "drn", type_names=["vector<double>"], optional=False, document=""""""), 
                                 13 : PinSpecification(name = "dn_cross_n", type_names=["vector<double>"], optional=False, document=""""""), 
                                 14 : PinSpecification(name = "dnx_y", type_names=["vector<double>"], optional=False, document=""""""), 
                                 15 : PinSpecification(name = "dny_y", type_names=["vector<double>"], optional=False, document=""""""), 
                                 16 : PinSpecification(name = "dnz_y", type_names=["vector<double>"], optional=False, document=""""""), 
                                 17 : PinSpecification(name = "dyx_n", type_names=["vector<double>"], optional=False, document=""""""), 
                                 18 : PinSpecification(name = "dyy_n", type_names=["vector<double>"], optional=False, document=""""""), 
                                 19 : PinSpecification(name = "dyz_n", type_names=["vector<double>"], optional=False, document=""""""), 
                                 20 : PinSpecification(name = "dnxn", type_names=["vector<double>"], optional=False, document=""""""), 
                                 21 : PinSpecification(name = "dnyn", type_names=["vector<double>"], optional=False, document=""""""), 
                                 22 : PinSpecification(name = "dnzn", type_names=["vector<double>"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "compute_invariant_terms_rbd")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsComputeInvariantTermsRbd 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsComputeInvariantTermsRbd 
        """
        return super().outputs


#internal name: compute_invariant_terms_rbd
#scripting name: compute_invariant_terms_rbd
class InputsComputeInvariantTermsRbd(_Inputs):
    """Intermediate class used to connect user inputs to compute_invariant_terms_rbd operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.compute_invariant_terms_rbd()
      >>> my_rom_matrices = dpf.FieldsContainer()
      >>> op.inputs.rom_matrices.connect(my_rom_matrices)
      >>> my_mode_shapes = dpf.FieldsContainer()
      >>> op.inputs.mode_shapes.connect(my_mode_shapes)
      >>> my_lumped_mass = dpf.FieldsContainer()
      >>> op.inputs.lumped_mass.connect(my_lumped_mass)
      >>> my_model_data = dpf.FieldsContainer()
      >>> op.inputs.model_data.connect(my_model_data)
      >>> my_center_of_mass = dpf.FieldsContainer()
      >>> op.inputs.center_of_mass.connect(my_center_of_mass)
      >>> my_inertia_relief = dpf.FieldsContainer()
      >>> op.inputs.inertia_relief.connect(my_inertia_relief)
      >>> my_model_size = float()
      >>> op.inputs.model_size.connect(my_model_size)
      >>> my_field_coordinates = dpf.Field()
      >>> op.inputs.field_coordinates.connect(my_field_coordinates)
      >>> my_nod = dpf.list()
      >>> op.inputs.nod.connect(my_nod)
    """
    def __init__(self, op: Operator):
        super().__init__(compute_invariant_terms_rbd._spec().inputs, op)
        self._rom_matrices = Input(compute_invariant_terms_rbd._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._rom_matrices)
        self._mode_shapes = Input(compute_invariant_terms_rbd._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mode_shapes)
        self._lumped_mass = Input(compute_invariant_terms_rbd._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._lumped_mass)
        self._model_data = Input(compute_invariant_terms_rbd._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._model_data)
        self._center_of_mass = Input(compute_invariant_terms_rbd._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._center_of_mass)
        self._inertia_relief = Input(compute_invariant_terms_rbd._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._inertia_relief)
        self._model_size = Input(compute_invariant_terms_rbd._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self._model_size)
        self._field_coordinates = Input(compute_invariant_terms_rbd._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._field_coordinates)
        self._nod = Input(compute_invariant_terms_rbd._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self._nod)

    @property
    def rom_matrices(self):
        """Allows to connect rom_matrices input to the operator

        - pindoc: FieldsContainers containing the reduced matrices

        Parameters
        ----------
        my_rom_matrices : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> op.inputs.rom_matrices.connect(my_rom_matrices)
        >>> #or
        >>> op.inputs.rom_matrices(my_rom_matrices)

        """
        return self._rom_matrices

    @property
    def mode_shapes(self):
        """Allows to connect mode_shapes input to the operator

        - pindoc: FieldsContainers containing the mode shapes, which are CST and NOR for the cms method

        Parameters
        ----------
        my_mode_shapes : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> op.inputs.mode_shapes.connect(my_mode_shapes)
        >>> #or
        >>> op.inputs.mode_shapes(my_mode_shapes)

        """
        return self._mode_shapes

    @property
    def lumped_mass(self):
        """Allows to connect lumped_mass input to the operator

        - pindoc: FieldsContainers containing the lumped mass

        Parameters
        ----------
        my_lumped_mass : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> op.inputs.lumped_mass.connect(my_lumped_mass)
        >>> #or
        >>> op.inputs.lumped_mass(my_lumped_mass)

        """
        return self._lumped_mass

    @property
    def model_data(self):
        """Allows to connect model_data input to the operator

        - pindoc: data describing the finite element model

        Parameters
        ----------
        my_model_data : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> op.inputs.model_data.connect(my_model_data)
        >>> #or
        >>> op.inputs.model_data(my_model_data)

        """
        return self._model_data

    @property
    def center_of_mass(self):
        """Allows to connect center_of_mass input to the operator

        Parameters
        ----------
        my_center_of_mass : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> op.inputs.center_of_mass.connect(my_center_of_mass)
        >>> #or
        >>> op.inputs.center_of_mass(my_center_of_mass)

        """
        return self._center_of_mass

    @property
    def inertia_relief(self):
        """Allows to connect inertia_relief input to the operator

        - pindoc: inertia matrix

        Parameters
        ----------
        my_inertia_relief : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> op.inputs.inertia_relief.connect(my_inertia_relief)
        >>> #or
        >>> op.inputs.inertia_relief(my_inertia_relief)

        """
        return self._inertia_relief

    @property
    def model_size(self):
        """Allows to connect model_size input to the operator

        - pindoc: model size

        Parameters
        ----------
        my_model_size : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> op.inputs.model_size.connect(my_model_size)
        >>> #or
        >>> op.inputs.model_size(my_model_size)

        """
        return self._model_size

    @property
    def field_coordinates(self):
        """Allows to connect field_coordinates input to the operator

        - pindoc: coordinates of all nodes

        Parameters
        ----------
        my_field_coordinates : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> op.inputs.field_coordinates.connect(my_field_coordinates)
        >>> #or
        >>> op.inputs.field_coordinates(my_field_coordinates)

        """
        return self._field_coordinates

    @property
    def nod(self):
        """Allows to connect nod input to the operator

        Parameters
        ----------
        my_nod : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> op.inputs.nod.connect(my_nod)
        >>> #or
        >>> op.inputs.nod(my_nod)

        """
        return self._nod

class OutputsComputeInvariantTermsRbd(_Outputs):
    """Intermediate class used to get outputs from compute_invariant_terms_rbd operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.compute_invariant_terms_rbd()
      >>> # Connect inputs : op.inputs. ...
      >>> result_model_data = op.outputs.model_data()
      >>> result_center_of_mass = op.outputs.center_of_mass()
      >>> result_inertia_relief = op.outputs.inertia_relief()
      >>> result_model_size = op.outputs.model_size()
      >>> result_master_node_coordinates = op.outputs.master_node_coordinates()
      >>> result_v_trsf = op.outputs.v_trsf()
      >>> result_k_mat = op.outputs.k_mat()
      >>> result_mass_mat = op.outputs.mass_mat()
      >>> result_c_mat = op.outputs.c_mat()
      >>> result_rhs = op.outputs.rhs()
      >>> result_dn = op.outputs.dn()
      >>> result_dr_cross_n = op.outputs.dr_cross_n()
      >>> result_drn = op.outputs.drn()
      >>> result_dn_cross_n = op.outputs.dn_cross_n()
      >>> result_dnx_y = op.outputs.dnx_y()
      >>> result_dny_y = op.outputs.dny_y()
      >>> result_dnz_y = op.outputs.dnz_y()
      >>> result_dyx_n = op.outputs.dyx_n()
      >>> result_dyy_n = op.outputs.dyy_n()
      >>> result_dyz_n = op.outputs.dyz_n()
      >>> result_dnxn = op.outputs.dnxn()
      >>> result_dnyn = op.outputs.dnyn()
      >>> result_dnzn = op.outputs.dnzn()
    """
    def __init__(self, op: Operator):
        super().__init__(compute_invariant_terms_rbd._spec().outputs, op)
        self._model_data = Output(compute_invariant_terms_rbd._spec().output_pin(0), 0, op) 
        self._outputs.append(self._model_data)
        self._center_of_mass = Output(compute_invariant_terms_rbd._spec().output_pin(1), 1, op) 
        self._outputs.append(self._center_of_mass)
        self._inertia_relief = Output(compute_invariant_terms_rbd._spec().output_pin(2), 2, op) 
        self._outputs.append(self._inertia_relief)
        self._model_size = Output(compute_invariant_terms_rbd._spec().output_pin(3), 3, op) 
        self._outputs.append(self._model_size)
        self._master_node_coordinates = Output(compute_invariant_terms_rbd._spec().output_pin(4), 4, op) 
        self._outputs.append(self._master_node_coordinates)
        self._v_trsf = Output(compute_invariant_terms_rbd._spec().output_pin(5), 5, op) 
        self._outputs.append(self._v_trsf)
        self._k_mat = Output(compute_invariant_terms_rbd._spec().output_pin(6), 6, op) 
        self._outputs.append(self._k_mat)
        self._mass_mat = Output(compute_invariant_terms_rbd._spec().output_pin(7), 7, op) 
        self._outputs.append(self._mass_mat)
        self._c_mat = Output(compute_invariant_terms_rbd._spec().output_pin(8), 8, op) 
        self._outputs.append(self._c_mat)
        self._rhs = Output(compute_invariant_terms_rbd._spec().output_pin(9), 9, op) 
        self._outputs.append(self._rhs)
        self._dn = Output(compute_invariant_terms_rbd._spec().output_pin(10), 10, op) 
        self._outputs.append(self._dn)
        self._dr_cross_n = Output(compute_invariant_terms_rbd._spec().output_pin(11), 11, op) 
        self._outputs.append(self._dr_cross_n)
        self._drn = Output(compute_invariant_terms_rbd._spec().output_pin(12), 12, op) 
        self._outputs.append(self._drn)
        self._dn_cross_n = Output(compute_invariant_terms_rbd._spec().output_pin(13), 13, op) 
        self._outputs.append(self._dn_cross_n)
        self._dnx_y = Output(compute_invariant_terms_rbd._spec().output_pin(14), 14, op) 
        self._outputs.append(self._dnx_y)
        self._dny_y = Output(compute_invariant_terms_rbd._spec().output_pin(15), 15, op) 
        self._outputs.append(self._dny_y)
        self._dnz_y = Output(compute_invariant_terms_rbd._spec().output_pin(16), 16, op) 
        self._outputs.append(self._dnz_y)
        self._dyx_n = Output(compute_invariant_terms_rbd._spec().output_pin(17), 17, op) 
        self._outputs.append(self._dyx_n)
        self._dyy_n = Output(compute_invariant_terms_rbd._spec().output_pin(18), 18, op) 
        self._outputs.append(self._dyy_n)
        self._dyz_n = Output(compute_invariant_terms_rbd._spec().output_pin(19), 19, op) 
        self._outputs.append(self._dyz_n)
        self._dnxn = Output(compute_invariant_terms_rbd._spec().output_pin(20), 20, op) 
        self._outputs.append(self._dnxn)
        self._dnyn = Output(compute_invariant_terms_rbd._spec().output_pin(21), 21, op) 
        self._outputs.append(self._dnyn)
        self._dnzn = Output(compute_invariant_terms_rbd._spec().output_pin(22), 22, op) 
        self._outputs.append(self._dnzn)

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

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_model_data = op.outputs.model_data() 
        """
        return self._model_data

    @property
    def center_of_mass(self):
        """Allows to get center_of_mass output of the operator


        - pindoc: center of mass of the body

        Returns
        ----------
        my_center_of_mass : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
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

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_inertia_relief = op.outputs.inertia_relief() 
        """
        return self._inertia_relief

    @property
    def model_size(self):
        """Allows to get model_size output of the operator


        Returns
        ----------
        my_model_size : PropertyField, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_model_size = op.outputs.model_size() 
        """
        return self._model_size

    @property
    def master_node_coordinates(self):
        """Allows to get master_node_coordinates output of the operator


        Returns
        ----------
        my_master_node_coordinates : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_master_node_coordinates = op.outputs.master_node_coordinates() 
        """
        return self._master_node_coordinates

    @property
    def v_trsf(self):
        """Allows to get v_trsf output of the operator


        - pindoc: translational and rotational shape functions

        Returns
        ----------
        my_v_trsf : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_v_trsf = op.outputs.v_trsf() 
        """
        return self._v_trsf

    @property
    def k_mat(self):
        """Allows to get k_mat output of the operator


        Returns
        ----------
        my_k_mat : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_k_mat = op.outputs.k_mat() 
        """
        return self._k_mat

    @property
    def mass_mat(self):
        """Allows to get mass_mat output of the operator


        Returns
        ----------
        my_mass_mat : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mass_mat = op.outputs.mass_mat() 
        """
        return self._mass_mat

    @property
    def c_mat(self):
        """Allows to get c_mat output of the operator


        Returns
        ----------
        my_c_mat : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_c_mat = op.outputs.c_mat() 
        """
        return self._c_mat

    @property
    def rhs(self):
        """Allows to get rhs output of the operator


        Returns
        ----------
        my_rhs : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_rhs = op.outputs.rhs() 
        """
        return self._rhs

    @property
    def dn(self):
        """Allows to get dn output of the operator


        Returns
        ----------
        my_dn : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dn = op.outputs.dn() 
        """
        return self._dn

    @property
    def dr_cross_n(self):
        """Allows to get dr_cross_n output of the operator


        Returns
        ----------
        my_dr_cross_n : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dr_cross_n = op.outputs.dr_cross_n() 
        """
        return self._dr_cross_n

    @property
    def drn(self):
        """Allows to get drn output of the operator


        Returns
        ----------
        my_drn : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_drn = op.outputs.drn() 
        """
        return self._drn

    @property
    def dn_cross_n(self):
        """Allows to get dn_cross_n output of the operator


        Returns
        ----------
        my_dn_cross_n : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dn_cross_n = op.outputs.dn_cross_n() 
        """
        return self._dn_cross_n

    @property
    def dnx_y(self):
        """Allows to get dnx_y output of the operator


        Returns
        ----------
        my_dnx_y : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dnx_y = op.outputs.dnx_y() 
        """
        return self._dnx_y

    @property
    def dny_y(self):
        """Allows to get dny_y output of the operator


        Returns
        ----------
        my_dny_y : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dny_y = op.outputs.dny_y() 
        """
        return self._dny_y

    @property
    def dnz_y(self):
        """Allows to get dnz_y output of the operator


        Returns
        ----------
        my_dnz_y : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dnz_y = op.outputs.dnz_y() 
        """
        return self._dnz_y

    @property
    def dyx_n(self):
        """Allows to get dyx_n output of the operator


        Returns
        ----------
        my_dyx_n : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dyx_n = op.outputs.dyx_n() 
        """
        return self._dyx_n

    @property
    def dyy_n(self):
        """Allows to get dyy_n output of the operator


        Returns
        ----------
        my_dyy_n : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dyy_n = op.outputs.dyy_n() 
        """
        return self._dyy_n

    @property
    def dyz_n(self):
        """Allows to get dyz_n output of the operator


        Returns
        ----------
        my_dyz_n : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dyz_n = op.outputs.dyz_n() 
        """
        return self._dyz_n

    @property
    def dnxn(self):
        """Allows to get dnxn output of the operator


        Returns
        ----------
        my_dnxn : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dnxn = op.outputs.dnxn() 
        """
        return self._dnxn

    @property
    def dnyn(self):
        """Allows to get dnyn output of the operator


        Returns
        ----------
        my_dnyn : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dnyn = op.outputs.dnyn() 
        """
        return self._dnyn

    @property
    def dnzn(self):
        """Allows to get dnzn output of the operator


        Returns
        ----------
        my_dnzn : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_invariant_terms_rbd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dnzn = op.outputs.dnzn() 
        """
        return self._dnzn

