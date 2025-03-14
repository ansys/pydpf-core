"""
extract_sub_mc

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


class extract_sub_mc(Operator):
    r"""Creates a new meshes container with all the meshed regions corresponding
    to the label space in input 1. If pin 1 is not defined, pin 0 input will
    be copied to the output.


    Parameters
    ----------
    meshes: MeshesContainer
        meshes
    label_space: dict or Scoping, optional
        Label space, or scoping defining the label space (scoping location), values to keep (scoping IDs)
    collapse_labels: bool, optional
        If set to true (default) the input label space (scoping location) is suppressed from the output meshes container, otherwise, label space is kept.

    Returns
    -------
    meshes_container: MeshesContainer
        meshes

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.extract_sub_mc()

    >>> # Make input connections
    >>> my_meshes = dpf.MeshesContainer()
    >>> op.inputs.meshes.connect(my_meshes)
    >>> my_label_space = dict()
    >>> op.inputs.label_space.connect(my_label_space)
    >>> my_collapse_labels = bool()
    >>> op.inputs.collapse_labels.connect(my_collapse_labels)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.extract_sub_mc(
    ...     meshes=my_meshes,
    ...     label_space=my_label_space,
    ...     collapse_labels=my_collapse_labels,
    ... )

    >>> # Get output data
    >>> result_meshes_container = op.outputs.meshes_container()
    """

    def __init__(
        self,
        meshes=None,
        label_space=None,
        collapse_labels=None,
        config=None,
        server=None,
    ):
        super().__init__(name="extract_sub_mc", config=config, server=server)
        self._inputs = InputsExtractSubMc(self)
        self._outputs = OutputsExtractSubMc(self)
        if meshes is not None:
            self.inputs.meshes.connect(meshes)
        if label_space is not None:
            self.inputs.label_space.connect(label_space)
        if collapse_labels is not None:
            self.inputs.collapse_labels.connect(collapse_labels)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Creates a new meshes container with all the meshed regions corresponding
to the label space in input 1. If pin 1 is not defined, pin 0 input will
be copied to the output.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="meshes",
                    type_names=["meshes_container"],
                    optional=False,
                    document=r"""meshes""",
                ),
                1: PinSpecification(
                    name="label_space",
                    type_names=["label_space", "scoping"],
                    optional=True,
                    document=r"""Label space, or scoping defining the label space (scoping location), values to keep (scoping IDs)""",
                ),
                2: PinSpecification(
                    name="collapse_labels",
                    type_names=["bool"],
                    optional=True,
                    document=r"""If set to true (default) the input label space (scoping location) is suppressed from the output meshes container, otherwise, label space is kept.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="meshes_container",
                    type_names=["meshes_container"],
                    optional=False,
                    document=r"""meshes""",
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
        return Operator.default_config(name="extract_sub_mc", server=server)

    @property
    def inputs(self) -> InputsExtractSubMc:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsExtractSubMc.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsExtractSubMc:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsExtractSubMc.
        """
        return super().outputs


class InputsExtractSubMc(_Inputs):
    """Intermediate class used to connect user inputs to
    extract_sub_mc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.extract_sub_mc()
    >>> my_meshes = dpf.MeshesContainer()
    >>> op.inputs.meshes.connect(my_meshes)
    >>> my_label_space = dict()
    >>> op.inputs.label_space.connect(my_label_space)
    >>> my_collapse_labels = bool()
    >>> op.inputs.collapse_labels.connect(my_collapse_labels)
    """

    def __init__(self, op: Operator):
        super().__init__(extract_sub_mc._spec().inputs, op)
        self._meshes = Input(extract_sub_mc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._meshes)
        self._label_space = Input(extract_sub_mc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._label_space)
        self._collapse_labels = Input(extract_sub_mc._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._collapse_labels)

    @property
    def meshes(self) -> Input:
        r"""Allows to connect meshes input to the operator.

        meshes

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.extract_sub_mc()
        >>> op.inputs.meshes.connect(my_meshes)
        >>> # or
        >>> op.inputs.meshes(my_meshes)
        """
        return self._meshes

    @property
    def label_space(self) -> Input:
        r"""Allows to connect label_space input to the operator.

        Label space, or scoping defining the label space (scoping location), values to keep (scoping IDs)

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.extract_sub_mc()
        >>> op.inputs.label_space.connect(my_label_space)
        >>> # or
        >>> op.inputs.label_space(my_label_space)
        """
        return self._label_space

    @property
    def collapse_labels(self) -> Input:
        r"""Allows to connect collapse_labels input to the operator.

        If set to true (default) the input label space (scoping location) is suppressed from the output meshes container, otherwise, label space is kept.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.extract_sub_mc()
        >>> op.inputs.collapse_labels.connect(my_collapse_labels)
        >>> # or
        >>> op.inputs.collapse_labels(my_collapse_labels)
        """
        return self._collapse_labels


class OutputsExtractSubMc(_Outputs):
    """Intermediate class used to get outputs from
    extract_sub_mc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.extract_sub_mc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_meshes_container = op.outputs.meshes_container()
    """

    def __init__(self, op: Operator):
        super().__init__(extract_sub_mc._spec().outputs, op)
        self._meshes_container = Output(extract_sub_mc._spec().output_pin(0), 0, op)
        self._outputs.append(self._meshes_container)

    @property
    def meshes_container(self) -> Output:
        r"""Allows to get meshes_container output of the operator

        meshes

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.extract_sub_mc()
        >>> # Get the output from op.outputs. ...
        >>> result_meshes_container = op.outputs.meshes_container()
        """
        return self._meshes_container
