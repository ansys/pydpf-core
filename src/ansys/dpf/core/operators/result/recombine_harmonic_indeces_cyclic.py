"""
recombine_harmonic_indeces_cyclic

Autogenerated DPF operator classes.
"""

from __future__ import annotations

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification
from ansys.dpf.core.config import Config
from ansys.dpf.core.server_types import AnyServerType


class recombine_harmonic_indeces_cyclic(Operator):
    r"""Add the fields corresponding to different load steps with the same
    frequencies to compute the response.


    Parameters
    ----------
    fields_container: FieldsContainer

    Returns
    -------
    fields_container: FieldsContainer

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic(
    ...     fields_container=my_fields_container,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(
            name="recombine_harmonic_indeces_cyclic", config=config, server=server
        )
        self._inputs = InputsRecombineHarmonicIndecesCyclic(self)
        self._outputs = OutputsRecombineHarmonicIndecesCyclic(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Add the fields corresponding to different load steps with the same
frequencies to compute the response.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document=r"""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document=r"""""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server: AnyServerType = None) -> Config:
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server:
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.

        Returns
        -------
        config:
            A new Config instance equivalent to the default config for this operator.
        """
        return Operator.default_config(
            name="recombine_harmonic_indeces_cyclic", server=server
        )

    @property
    def inputs(self) -> InputsRecombineHarmonicIndecesCyclic:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsRecombineHarmonicIndecesCyclic.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsRecombineHarmonicIndecesCyclic:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsRecombineHarmonicIndecesCyclic.
        """
        return super().outputs


class InputsRecombineHarmonicIndecesCyclic(_Inputs):
    """Intermediate class used to connect user inputs to
    recombine_harmonic_indeces_cyclic operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    """

    def __init__(self, op: Operator):
        super().__init__(recombine_harmonic_indeces_cyclic._spec().inputs, op)
        self._fields_container = Input(
            recombine_harmonic_indeces_cyclic._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)

    @property
    def fields_container(self) -> Input:
        r"""Allows to connect fields_container input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container


class OutputsRecombineHarmonicIndecesCyclic(_Outputs):
    """Intermediate class used to get outputs from
    recombine_harmonic_indeces_cyclic operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(recombine_harmonic_indeces_cyclic._spec().outputs, op)
        self._fields_container = Output(
            recombine_harmonic_indeces_cyclic._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self) -> Output:
        r"""Allows to get fields_container output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic()
        >>> # Get the output from op.outputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """
        return self._fields_container
