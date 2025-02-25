"""
identical_mc

Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class identical_mc(Operator):
    """Checks if two meshes_container are identical.

    Parameters
    ----------
    meshes_containerA : MeshesContainer
    meshes_containerB : MeshesContainer
    small_value : float, optional
        Double positive small value. smallest value
        which will be considered during the
        comparison step. all the abs(values)
        in the field less than this value are
        considered as null, (default
        value:1.0e-14).
    tolerance : float, optional
        Double relative tolerance. maximum tolerance
        gap between two compared values.
        values within relative tolerance are
        considered identical (v1-v2)/v2 <
        relativetol (default is 0.001).
    compare_auxiliary : bool
        Compare auxiliary data (i.e property fields,
        scopings...). default value is
        'false'.

    Returns
    -------
    boolean : bool
        Bool (true if identical...)
    message : str

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.logic.identical_mc()

    >>> # Make input connections
    >>> my_meshes_containerA = dpf.MeshesContainer()
    >>> op.inputs.meshes_containerA.connect(my_meshes_containerA)
    >>> my_meshes_containerB = dpf.MeshesContainer()
    >>> op.inputs.meshes_containerB.connect(my_meshes_containerB)
    >>> my_small_value = float()
    >>> op.inputs.small_value.connect(my_small_value)
    >>> my_tolerance = float()
    >>> op.inputs.tolerance.connect(my_tolerance)
    >>> my_compare_auxiliary = bool()
    >>> op.inputs.compare_auxiliary.connect(my_compare_auxiliary)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.logic.identical_mc(
    ...     meshes_containerA=my_meshes_containerA,
    ...     meshes_containerB=my_meshes_containerB,
    ...     small_value=my_small_value,
    ...     tolerance=my_tolerance,
    ...     compare_auxiliary=my_compare_auxiliary,
    ... )

    >>> # Get output data
    >>> result_boolean = op.outputs.boolean()
    >>> result_message = op.outputs.message()
    """

    def __init__(
        self,
        meshes_containerA=None,
        meshes_containerB=None,
        small_value=None,
        tolerance=None,
        compare_auxiliary=None,
        config=None,
        server=None,
    ):
        super().__init__(name="compare::meshes_container", config=config, server=server)
        self._inputs = InputsIdenticalMc(self)
        self._outputs = OutputsIdenticalMc(self)
        if meshes_containerA is not None:
            self.inputs.meshes_containerA.connect(meshes_containerA)
        if meshes_containerB is not None:
            self.inputs.meshes_containerB.connect(meshes_containerB)
        if small_value is not None:
            self.inputs.small_value.connect(small_value)
        if tolerance is not None:
            self.inputs.tolerance.connect(tolerance)
        if compare_auxiliary is not None:
            self.inputs.compare_auxiliary.connect(compare_auxiliary)

    @staticmethod
    def _spec():
        description = """Checks if two meshes_container are identical."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="meshes_containerA",
                    type_names=["meshes_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="meshes_containerB",
                    type_names=["meshes_container"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="small_value",
                    type_names=["double"],
                    optional=True,
                    document="""Double positive small value. smallest value
        which will be considered during the
        comparison step. all the abs(values)
        in the field less than this value are
        considered as null, (default
        value:1.0e-14).""",
                ),
                3: PinSpecification(
                    name="tolerance",
                    type_names=["double"],
                    optional=True,
                    document="""Double relative tolerance. maximum tolerance
        gap between two compared values.
        values within relative tolerance are
        considered identical (v1-v2)/v2 <
        relativetol (default is 0.001).""",
                ),
                4: PinSpecification(
                    name="compare_auxiliary",
                    type_names=["bool"],
                    optional=False,
                    document="""Compare auxiliary data (i.e property fields,
        scopings...). default value is
        'false'.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="boolean",
                    type_names=["bool"],
                    optional=False,
                    document="""Bool (true if identical...)""",
                ),
                1: PinSpecification(
                    name="message",
                    type_names=["string"],
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
        return Operator.default_config(name="compare::meshes_container", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsIdenticalMc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsIdenticalMc
        """
        return super().outputs


class InputsIdenticalMc(_Inputs):
    """Intermediate class used to connect user inputs to
    identical_mc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.identical_mc()
    >>> my_meshes_containerA = dpf.MeshesContainer()
    >>> op.inputs.meshes_containerA.connect(my_meshes_containerA)
    >>> my_meshes_containerB = dpf.MeshesContainer()
    >>> op.inputs.meshes_containerB.connect(my_meshes_containerB)
    >>> my_small_value = float()
    >>> op.inputs.small_value.connect(my_small_value)
    >>> my_tolerance = float()
    >>> op.inputs.tolerance.connect(my_tolerance)
    >>> my_compare_auxiliary = bool()
    >>> op.inputs.compare_auxiliary.connect(my_compare_auxiliary)
    """

    def __init__(self, op: Operator):
        super().__init__(identical_mc._spec().inputs, op)
        self._meshes_containerA = Input(identical_mc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._meshes_containerA)
        self._meshes_containerB = Input(identical_mc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._meshes_containerB)
        self._small_value = Input(identical_mc._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._small_value)
        self._tolerance = Input(identical_mc._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._tolerance)
        self._compare_auxiliary = Input(identical_mc._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._compare_auxiliary)

    @property
    def meshes_containerA(self):
        """Allows to connect meshes_containerA input to the operator.

        Parameters
        ----------
        my_meshes_containerA : MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_mc()
        >>> op.inputs.meshes_containerA.connect(my_meshes_containerA)
        >>> # or
        >>> op.inputs.meshes_containerA(my_meshes_containerA)
        """
        return self._meshes_containerA

    @property
    def meshes_containerB(self):
        """Allows to connect meshes_containerB input to the operator.

        Parameters
        ----------
        my_meshes_containerB : MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_mc()
        >>> op.inputs.meshes_containerB.connect(my_meshes_containerB)
        >>> # or
        >>> op.inputs.meshes_containerB(my_meshes_containerB)
        """
        return self._meshes_containerB

    @property
    def small_value(self):
        """Allows to connect small_value input to the operator.

        Double positive small value. smallest value
        which will be considered during the
        comparison step. all the abs(values)
        in the field less than this value are
        considered as null, (default
        value:1.0e-14).

        Parameters
        ----------
        my_small_value : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_mc()
        >>> op.inputs.small_value.connect(my_small_value)
        >>> # or
        >>> op.inputs.small_value(my_small_value)
        """
        return self._small_value

    @property
    def tolerance(self):
        """Allows to connect tolerance input to the operator.

        Double relative tolerance. maximum tolerance
        gap between two compared values.
        values within relative tolerance are
        considered identical (v1-v2)/v2 <
        relativetol (default is 0.001).

        Parameters
        ----------
        my_tolerance : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_mc()
        >>> op.inputs.tolerance.connect(my_tolerance)
        >>> # or
        >>> op.inputs.tolerance(my_tolerance)
        """
        return self._tolerance

    @property
    def compare_auxiliary(self):
        """Allows to connect compare_auxiliary input to the operator.

        Compare auxiliary data (i.e property fields,
        scopings...). default value is
        'false'.

        Parameters
        ----------
        my_compare_auxiliary : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_mc()
        >>> op.inputs.compare_auxiliary.connect(my_compare_auxiliary)
        >>> # or
        >>> op.inputs.compare_auxiliary(my_compare_auxiliary)
        """
        return self._compare_auxiliary


class OutputsIdenticalMc(_Outputs):
    """Intermediate class used to get outputs from
    identical_mc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.identical_mc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_boolean = op.outputs.boolean()
    >>> result_message = op.outputs.message()
    """

    def __init__(self, op: Operator):
        super().__init__(identical_mc._spec().outputs, op)
        self._boolean = Output(identical_mc._spec().output_pin(0), 0, op)
        self._outputs.append(self._boolean)
        self._message = Output(identical_mc._spec().output_pin(1), 1, op)
        self._outputs.append(self._message)

    @property
    def boolean(self):
        """Allows to get boolean output of the operator

        Returns
        ----------
        my_boolean : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_mc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_boolean = op.outputs.boolean()
        """  # noqa: E501
        return self._boolean

    @property
    def message(self):
        """Allows to get message output of the operator

        Returns
        ----------
        my_message : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_mc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_message = op.outputs.message()
        """  # noqa: E501
        return self._message
