"""
modal_damping_ratio

Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class modal_damping_ratio(Operator):
    """Computes damping ratio for each mode shape as X_i = const + ratio_i +
    m_coefficient / (2*omega_i) + k_coefficient * omega_i/2.

    Parameters
    ----------
    natural_freq :
        Input vector expects natural frequencies.
    const_ratio : float, optional
        Constant modal damping ratio
    ratio_by_modes : optional
        Modal damping ratio for each mode shape
    m_coefficient : float
        Global mass matrix multiplier
    k_coefficient : float
        Global stiffness matrix multiplier

    Returns
    -------
    field : Field
        Field of modal damping ratio.

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.modal_damping_ratio()

    >>> # Make input connections
    >>> my_natural_freq = dpf.()
    >>> op.inputs.natural_freq.connect(my_natural_freq)
    >>> my_const_ratio = float()
    >>> op.inputs.const_ratio.connect(my_const_ratio)
    >>> my_ratio_by_modes = dpf.()
    >>> op.inputs.ratio_by_modes.connect(my_ratio_by_modes)
    >>> my_m_coefficient = float()
    >>> op.inputs.m_coefficient.connect(my_m_coefficient)
    >>> my_k_coefficient = float()
    >>> op.inputs.k_coefficient.connect(my_k_coefficient)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.modal_damping_ratio(
    ...     natural_freq=my_natural_freq,
    ...     const_ratio=my_const_ratio,
    ...     ratio_by_modes=my_ratio_by_modes,
    ...     m_coefficient=my_m_coefficient,
    ...     k_coefficient=my_k_coefficient,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        natural_freq=None,
        const_ratio=None,
        ratio_by_modes=None,
        m_coefficient=None,
        k_coefficient=None,
        config=None,
        server=None,
    ):
        super().__init__(name="modal_damping_ratio", config=config, server=server)
        self._inputs = InputsModalDampingRatio(self)
        self._outputs = OutputsModalDampingRatio(self)
        if natural_freq is not None:
            self.inputs.natural_freq.connect(natural_freq)
        if const_ratio is not None:
            self.inputs.const_ratio.connect(const_ratio)
        if ratio_by_modes is not None:
            self.inputs.ratio_by_modes.connect(ratio_by_modes)
        if m_coefficient is not None:
            self.inputs.m_coefficient.connect(m_coefficient)
        if k_coefficient is not None:
            self.inputs.k_coefficient.connect(k_coefficient)

    @staticmethod
    def _spec():
        description = """Computes damping ratio for each mode shape as X_i = const + ratio_i +
            m_coefficient / (2*omega_i) + k_coefficient * omega_i/2."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="natural_freq",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""Input vector expects natural frequencies.""",
                ),
                1: PinSpecification(
                    name="const_ratio",
                    type_names=["double"],
                    optional=True,
                    document="""Constant modal damping ratio""",
                ),
                2: PinSpecification(
                    name="ratio_by_modes",
                    type_names=["vector<double>"],
                    optional=True,
                    document="""Modal damping ratio for each mode shape""",
                ),
                3: PinSpecification(
                    name="m_coefficient",
                    type_names=["double"],
                    optional=False,
                    document="""Global mass matrix multiplier""",
                ),
                4: PinSpecification(
                    name="k_coefficient",
                    type_names=["double"],
                    optional=False,
                    document="""Global stiffness matrix multiplier""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""Field of modal damping ratio.""",
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
        return Operator.default_config(name="modal_damping_ratio", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsModalDampingRatio
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsModalDampingRatio
        """
        return super().outputs


class InputsModalDampingRatio(_Inputs):
    """Intermediate class used to connect user inputs to
    modal_damping_ratio operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.modal_damping_ratio()
    >>> my_natural_freq = dpf.()
    >>> op.inputs.natural_freq.connect(my_natural_freq)
    >>> my_const_ratio = float()
    >>> op.inputs.const_ratio.connect(my_const_ratio)
    >>> my_ratio_by_modes = dpf.()
    >>> op.inputs.ratio_by_modes.connect(my_ratio_by_modes)
    >>> my_m_coefficient = float()
    >>> op.inputs.m_coefficient.connect(my_m_coefficient)
    >>> my_k_coefficient = float()
    >>> op.inputs.k_coefficient.connect(my_k_coefficient)
    """

    def __init__(self, op: Operator):
        super().__init__(modal_damping_ratio._spec().inputs, op)
        self._natural_freq = Input(modal_damping_ratio._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._natural_freq)
        self._const_ratio = Input(modal_damping_ratio._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._const_ratio)
        self._ratio_by_modes = Input(
            modal_damping_ratio._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._ratio_by_modes)
        self._m_coefficient = Input(modal_damping_ratio._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._m_coefficient)
        self._k_coefficient = Input(modal_damping_ratio._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._k_coefficient)

    @property
    def natural_freq(self):
        """Allows to connect natural_freq input to the operator.

        Input vector expects natural frequencies.

        Parameters
        ----------
        my_natural_freq :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_damping_ratio()
        >>> op.inputs.natural_freq.connect(my_natural_freq)
        >>> # or
        >>> op.inputs.natural_freq(my_natural_freq)
        """
        return self._natural_freq

    @property
    def const_ratio(self):
        """Allows to connect const_ratio input to the operator.

        Constant modal damping ratio

        Parameters
        ----------
        my_const_ratio : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_damping_ratio()
        >>> op.inputs.const_ratio.connect(my_const_ratio)
        >>> # or
        >>> op.inputs.const_ratio(my_const_ratio)
        """
        return self._const_ratio

    @property
    def ratio_by_modes(self):
        """Allows to connect ratio_by_modes input to the operator.

        Modal damping ratio for each mode shape

        Parameters
        ----------
        my_ratio_by_modes :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_damping_ratio()
        >>> op.inputs.ratio_by_modes.connect(my_ratio_by_modes)
        >>> # or
        >>> op.inputs.ratio_by_modes(my_ratio_by_modes)
        """
        return self._ratio_by_modes

    @property
    def m_coefficient(self):
        """Allows to connect m_coefficient input to the operator.

        Global mass matrix multiplier

        Parameters
        ----------
        my_m_coefficient : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_damping_ratio()
        >>> op.inputs.m_coefficient.connect(my_m_coefficient)
        >>> # or
        >>> op.inputs.m_coefficient(my_m_coefficient)
        """
        return self._m_coefficient

    @property
    def k_coefficient(self):
        """Allows to connect k_coefficient input to the operator.

        Global stiffness matrix multiplier

        Parameters
        ----------
        my_k_coefficient : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_damping_ratio()
        >>> op.inputs.k_coefficient.connect(my_k_coefficient)
        >>> # or
        >>> op.inputs.k_coefficient(my_k_coefficient)
        """
        return self._k_coefficient


class OutputsModalDampingRatio(_Outputs):
    """Intermediate class used to get outputs from
    modal_damping_ratio operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.modal_damping_ratio()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(modal_damping_ratio._spec().outputs, op)
        self._field = Output(modal_damping_ratio._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_damping_ratio()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
