"""
identical_sc

Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class identical_sc(Operator):
    """Checks if two scopings_container are identical.

    Parameters
    ----------
    scopings_containerA : ScopingsContainer
    scopings_containerB : ScopingsContainer

    Returns
    -------
    boolean : bool
        Bool (true if identical...)
    message : str

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.logic.identical_sc()

    >>> # Make input connections
    >>> my_scopings_containerA = dpf.ScopingsContainer()
    >>> op.inputs.scopings_containerA.connect(my_scopings_containerA)
    >>> my_scopings_containerB = dpf.ScopingsContainer()
    >>> op.inputs.scopings_containerB.connect(my_scopings_containerB)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.logic.identical_sc(
    ...     scopings_containerA=my_scopings_containerA,
    ...     scopings_containerB=my_scopings_containerB,
    ... )

    >>> # Get output data
    >>> result_boolean = op.outputs.boolean()
    >>> result_message = op.outputs.message()
    """

    def __init__(
        self,
        scopings_containerA=None,
        scopings_containerB=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="compare::scopings_container", config=config, server=server
        )
        self._inputs = InputsIdenticalSc(self)
        self._outputs = OutputsIdenticalSc(self)
        if scopings_containerA is not None:
            self.inputs.scopings_containerA.connect(scopings_containerA)
        if scopings_containerB is not None:
            self.inputs.scopings_containerB.connect(scopings_containerB)

    @staticmethod
    def _spec():
        description = """Checks if two scopings_container are identical."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="scopings_containerA",
                    type_names=["scopings_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="scopings_containerB",
                    type_names=["scopings_container"],
                    optional=False,
                    document="""""",
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
        return Operator.default_config(
            name="compare::scopings_container", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsIdenticalSc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsIdenticalSc
        """
        return super().outputs


class InputsIdenticalSc(_Inputs):
    """Intermediate class used to connect user inputs to
    identical_sc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.identical_sc()
    >>> my_scopings_containerA = dpf.ScopingsContainer()
    >>> op.inputs.scopings_containerA.connect(my_scopings_containerA)
    >>> my_scopings_containerB = dpf.ScopingsContainer()
    >>> op.inputs.scopings_containerB.connect(my_scopings_containerB)
    """

    def __init__(self, op: Operator):
        super().__init__(identical_sc._spec().inputs, op)
        self._scopings_containerA = Input(identical_sc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._scopings_containerA)
        self._scopings_containerB = Input(identical_sc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._scopings_containerB)

    @property
    def scopings_containerA(self):
        """Allows to connect scopings_containerA input to the operator.

        Parameters
        ----------
        my_scopings_containerA : ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_sc()
        >>> op.inputs.scopings_containerA.connect(my_scopings_containerA)
        >>> # or
        >>> op.inputs.scopings_containerA(my_scopings_containerA)
        """
        return self._scopings_containerA

    @property
    def scopings_containerB(self):
        """Allows to connect scopings_containerB input to the operator.

        Parameters
        ----------
        my_scopings_containerB : ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_sc()
        >>> op.inputs.scopings_containerB.connect(my_scopings_containerB)
        >>> # or
        >>> op.inputs.scopings_containerB(my_scopings_containerB)
        """
        return self._scopings_containerB


class OutputsIdenticalSc(_Outputs):
    """Intermediate class used to get outputs from
    identical_sc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.identical_sc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_boolean = op.outputs.boolean()
    >>> result_message = op.outputs.message()
    """

    def __init__(self, op: Operator):
        super().__init__(identical_sc._spec().outputs, op)
        self._boolean = Output(identical_sc._spec().output_pin(0), 0, op)
        self._outputs.append(self._boolean)
        self._message = Output(identical_sc._spec().output_pin(1), 1, op)
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
        >>> op = dpf.operators.logic.identical_sc()
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
        >>> op = dpf.operators.logic.identical_sc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_message = op.outputs.message()
        """  # noqa: E501
        return self._message
