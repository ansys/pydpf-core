"""
read_cms_rbd_file

Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class read_cms_rbd_file(Operator):
    """Read the invariant terms and the model data from a cms_rbd file

    Parameters
    ----------
    in_cms_rbd_file_path : str
        File name with cms_rbd extension where to
        read the input cms_rbd file.

    Returns
    -------
    model_data : PropertyField
        Data describing the finite element model
    center_of_mass : Field
        Center of mass of the body
    inertia_relief : Field
        Inertia matrix
    model_size : PropertyField
    master_node_coordinates :
    v_trsf :
        Translational and rotational shape functions
    k_mat : Field
    mass_mat : Field
    c_mat : Field
    rhs : Field
    dn :
    dr_cross_n :
    drn :
    dn_cross_n :
    dnx_y :
    dny_y :
    dnz_y :
    dyx_n :
    dyy_n :
    dyz_n :
    dnxn :
    dnyn :
    dnzn :

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.read_cms_rbd_file()

    >>> # Make input connections
    >>> my_in_cms_rbd_file_path = str()
    >>> op.inputs.in_cms_rbd_file_path.connect(my_in_cms_rbd_file_path)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.read_cms_rbd_file(
    ...     in_cms_rbd_file_path=my_in_cms_rbd_file_path,
    ... )

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
    >>> result_dnzn = op.outputs.dnzn()
    """

    def __init__(self, in_cms_rbd_file_path=None, config=None, server=None):
        super().__init__(name="read_cms_rbd_file", config=config, server=server)
        self._inputs = InputsReadCmsRbdFile(self)
        self._outputs = OutputsReadCmsRbdFile(self)
        if in_cms_rbd_file_path is not None:
            self.inputs.in_cms_rbd_file_path.connect(in_cms_rbd_file_path)

    @staticmethod
    def _spec():
        description = (
            """Read the invariant terms and the model data from a cms_rbd file"""
        )
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="in_cms_rbd_file_path",
                    type_names=["string"],
                    optional=False,
                    document="""File name with cms_rbd extension where to
        read the input cms_rbd file.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="model_data",
                    type_names=["property_field"],
                    optional=False,
                    document="""Data describing the finite element model""",
                ),
                1: PinSpecification(
                    name="center_of_mass",
                    type_names=["field"],
                    optional=False,
                    document="""Center of mass of the body""",
                ),
                2: PinSpecification(
                    name="inertia_relief",
                    type_names=["field"],
                    optional=False,
                    document="""Inertia matrix""",
                ),
                3: PinSpecification(
                    name="model_size",
                    type_names=["property_field"],
                    optional=False,
                    document="""""",
                ),
                4: PinSpecification(
                    name="master_node_coordinates",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                5: PinSpecification(
                    name="v_trsf",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""Translational and rotational shape functions""",
                ),
                6: PinSpecification(
                    name="k_mat",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                7: PinSpecification(
                    name="mass_mat",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                8: PinSpecification(
                    name="c_mat",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                9: PinSpecification(
                    name="rhs",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                10: PinSpecification(
                    name="dn",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                11: PinSpecification(
                    name="dr_cross_n",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                12: PinSpecification(
                    name="drn",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                13: PinSpecification(
                    name="dn_cross_n",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                14: PinSpecification(
                    name="dnx_y",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                15: PinSpecification(
                    name="dny_y",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                16: PinSpecification(
                    name="dnz_y",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                17: PinSpecification(
                    name="dyx_n",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                18: PinSpecification(
                    name="dyy_n",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                19: PinSpecification(
                    name="dyz_n",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                20: PinSpecification(
                    name="dnxn",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                21: PinSpecification(
                    name="dnyn",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                22: PinSpecification(
                    name="dnzn",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server=None):
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server : server.DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="read_cms_rbd_file", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsReadCmsRbdFile
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsReadCmsRbdFile
        """
        return super().outputs


class InputsReadCmsRbdFile(_Inputs):
    """Intermediate class used to connect user inputs to
    read_cms_rbd_file operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.read_cms_rbd_file()
    >>> my_in_cms_rbd_file_path = str()
    >>> op.inputs.in_cms_rbd_file_path.connect(my_in_cms_rbd_file_path)
    """

    def __init__(self, op: Operator):
        super().__init__(read_cms_rbd_file._spec().inputs, op)
        self._in_cms_rbd_file_path = Input(
            read_cms_rbd_file._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._in_cms_rbd_file_path)

    @property
    def in_cms_rbd_file_path(self):
        """Allows to connect in_cms_rbd_file_path input to the operator.

        File name with cms_rbd extension where to
        read the input cms_rbd file.

        Parameters
        ----------
        my_in_cms_rbd_file_path : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> op.inputs.in_cms_rbd_file_path.connect(my_in_cms_rbd_file_path)
        >>> # or
        >>> op.inputs.in_cms_rbd_file_path(my_in_cms_rbd_file_path)
        """
        return self._in_cms_rbd_file_path


class OutputsReadCmsRbdFile(_Outputs):
    """Intermediate class used to get outputs from
    read_cms_rbd_file operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.read_cms_rbd_file()
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
        super().__init__(read_cms_rbd_file._spec().outputs, op)
        self._model_data = Output(read_cms_rbd_file._spec().output_pin(0), 0, op)
        self._outputs.append(self._model_data)
        self._center_of_mass = Output(read_cms_rbd_file._spec().output_pin(1), 1, op)
        self._outputs.append(self._center_of_mass)
        self._inertia_relief = Output(read_cms_rbd_file._spec().output_pin(2), 2, op)
        self._outputs.append(self._inertia_relief)
        self._model_size = Output(read_cms_rbd_file._spec().output_pin(3), 3, op)
        self._outputs.append(self._model_size)
        self._master_node_coordinates = Output(
            read_cms_rbd_file._spec().output_pin(4), 4, op
        )
        self._outputs.append(self._master_node_coordinates)
        self._v_trsf = Output(read_cms_rbd_file._spec().output_pin(5), 5, op)
        self._outputs.append(self._v_trsf)
        self._k_mat = Output(read_cms_rbd_file._spec().output_pin(6), 6, op)
        self._outputs.append(self._k_mat)
        self._mass_mat = Output(read_cms_rbd_file._spec().output_pin(7), 7, op)
        self._outputs.append(self._mass_mat)
        self._c_mat = Output(read_cms_rbd_file._spec().output_pin(8), 8, op)
        self._outputs.append(self._c_mat)
        self._rhs = Output(read_cms_rbd_file._spec().output_pin(9), 9, op)
        self._outputs.append(self._rhs)
        self._dn = Output(read_cms_rbd_file._spec().output_pin(10), 10, op)
        self._outputs.append(self._dn)
        self._dr_cross_n = Output(read_cms_rbd_file._spec().output_pin(11), 11, op)
        self._outputs.append(self._dr_cross_n)
        self._drn = Output(read_cms_rbd_file._spec().output_pin(12), 12, op)
        self._outputs.append(self._drn)
        self._dn_cross_n = Output(read_cms_rbd_file._spec().output_pin(13), 13, op)
        self._outputs.append(self._dn_cross_n)
        self._dnx_y = Output(read_cms_rbd_file._spec().output_pin(14), 14, op)
        self._outputs.append(self._dnx_y)
        self._dny_y = Output(read_cms_rbd_file._spec().output_pin(15), 15, op)
        self._outputs.append(self._dny_y)
        self._dnz_y = Output(read_cms_rbd_file._spec().output_pin(16), 16, op)
        self._outputs.append(self._dnz_y)
        self._dyx_n = Output(read_cms_rbd_file._spec().output_pin(17), 17, op)
        self._outputs.append(self._dyx_n)
        self._dyy_n = Output(read_cms_rbd_file._spec().output_pin(18), 18, op)
        self._outputs.append(self._dyy_n)
        self._dyz_n = Output(read_cms_rbd_file._spec().output_pin(19), 19, op)
        self._outputs.append(self._dyz_n)
        self._dnxn = Output(read_cms_rbd_file._spec().output_pin(20), 20, op)
        self._outputs.append(self._dnxn)
        self._dnyn = Output(read_cms_rbd_file._spec().output_pin(21), 21, op)
        self._outputs.append(self._dnyn)
        self._dnzn = Output(read_cms_rbd_file._spec().output_pin(22), 22, op)
        self._outputs.append(self._dnzn)

    @property
    def model_data(self):
        """Allows to get model_data output of the operator

        Returns
        ----------
        my_model_data : PropertyField

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_model_data = op.outputs.model_data()
        """  # noqa: E501
        return self._model_data

    @property
    def center_of_mass(self):
        """Allows to get center_of_mass output of the operator

        Returns
        ----------
        my_center_of_mass : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_center_of_mass = op.outputs.center_of_mass()
        """  # noqa: E501
        return self._center_of_mass

    @property
    def inertia_relief(self):
        """Allows to get inertia_relief output of the operator

        Returns
        ----------
        my_inertia_relief : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_inertia_relief = op.outputs.inertia_relief()
        """  # noqa: E501
        return self._inertia_relief

    @property
    def model_size(self):
        """Allows to get model_size output of the operator

        Returns
        ----------
        my_model_size : PropertyField

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_model_size = op.outputs.model_size()
        """  # noqa: E501
        return self._model_size

    @property
    def master_node_coordinates(self):
        """Allows to get master_node_coordinates output of the operator

        Returns
        ----------
        my_master_node_coordinates :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_master_node_coordinates = op.outputs.master_node_coordinates()
        """  # noqa: E501
        return self._master_node_coordinates

    @property
    def v_trsf(self):
        """Allows to get v_trsf output of the operator

        Returns
        ----------
        my_v_trsf :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_v_trsf = op.outputs.v_trsf()
        """  # noqa: E501
        return self._v_trsf

    @property
    def k_mat(self):
        """Allows to get k_mat output of the operator

        Returns
        ----------
        my_k_mat : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_k_mat = op.outputs.k_mat()
        """  # noqa: E501
        return self._k_mat

    @property
    def mass_mat(self):
        """Allows to get mass_mat output of the operator

        Returns
        ----------
        my_mass_mat : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mass_mat = op.outputs.mass_mat()
        """  # noqa: E501
        return self._mass_mat

    @property
    def c_mat(self):
        """Allows to get c_mat output of the operator

        Returns
        ----------
        my_c_mat : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_c_mat = op.outputs.c_mat()
        """  # noqa: E501
        return self._c_mat

    @property
    def rhs(self):
        """Allows to get rhs output of the operator

        Returns
        ----------
        my_rhs : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_rhs = op.outputs.rhs()
        """  # noqa: E501
        return self._rhs

    @property
    def dn(self):
        """Allows to get dn output of the operator

        Returns
        ----------
        my_dn :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dn = op.outputs.dn()
        """  # noqa: E501
        return self._dn

    @property
    def dr_cross_n(self):
        """Allows to get dr_cross_n output of the operator

        Returns
        ----------
        my_dr_cross_n :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dr_cross_n = op.outputs.dr_cross_n()
        """  # noqa: E501
        return self._dr_cross_n

    @property
    def drn(self):
        """Allows to get drn output of the operator

        Returns
        ----------
        my_drn :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_drn = op.outputs.drn()
        """  # noqa: E501
        return self._drn

    @property
    def dn_cross_n(self):
        """Allows to get dn_cross_n output of the operator

        Returns
        ----------
        my_dn_cross_n :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dn_cross_n = op.outputs.dn_cross_n()
        """  # noqa: E501
        return self._dn_cross_n

    @property
    def dnx_y(self):
        """Allows to get dnx_y output of the operator

        Returns
        ----------
        my_dnx_y :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dnx_y = op.outputs.dnx_y()
        """  # noqa: E501
        return self._dnx_y

    @property
    def dny_y(self):
        """Allows to get dny_y output of the operator

        Returns
        ----------
        my_dny_y :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dny_y = op.outputs.dny_y()
        """  # noqa: E501
        return self._dny_y

    @property
    def dnz_y(self):
        """Allows to get dnz_y output of the operator

        Returns
        ----------
        my_dnz_y :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dnz_y = op.outputs.dnz_y()
        """  # noqa: E501
        return self._dnz_y

    @property
    def dyx_n(self):
        """Allows to get dyx_n output of the operator

        Returns
        ----------
        my_dyx_n :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dyx_n = op.outputs.dyx_n()
        """  # noqa: E501
        return self._dyx_n

    @property
    def dyy_n(self):
        """Allows to get dyy_n output of the operator

        Returns
        ----------
        my_dyy_n :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dyy_n = op.outputs.dyy_n()
        """  # noqa: E501
        return self._dyy_n

    @property
    def dyz_n(self):
        """Allows to get dyz_n output of the operator

        Returns
        ----------
        my_dyz_n :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dyz_n = op.outputs.dyz_n()
        """  # noqa: E501
        return self._dyz_n

    @property
    def dnxn(self):
        """Allows to get dnxn output of the operator

        Returns
        ----------
        my_dnxn :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dnxn = op.outputs.dnxn()
        """  # noqa: E501
        return self._dnxn

    @property
    def dnyn(self):
        """Allows to get dnyn output of the operator

        Returns
        ----------
        my_dnyn :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dnyn = op.outputs.dnyn()
        """  # noqa: E501
        return self._dnyn

    @property
    def dnzn(self):
        """Allows to get dnzn output of the operator

        Returns
        ----------
        my_dnzn :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.read_cms_rbd_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dnzn = op.outputs.dnzn()
        """  # noqa: E501
        return self._dnzn
