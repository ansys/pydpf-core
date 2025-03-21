"""
mesh_to_graphics_edges

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


class mesh_to_graphics_edges(Operator):
    r"""Generate edges of surface elements for input mesh


    Parameters
    ----------
    mesh_scoping: Scoping, optional
    include_mid_nodes: bool, optional
    mesh: MeshedRegion

    Returns
    -------
    nodes: Field
        node coordinates
    connectivity: PropertyField

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.mesh_to_graphics_edges()

    >>> # Make input connections
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_include_mid_nodes = bool()
    >>> op.inputs.include_mid_nodes.connect(my_include_mid_nodes)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.mesh_to_graphics_edges(
    ...     mesh_scoping=my_mesh_scoping,
    ...     include_mid_nodes=my_include_mid_nodes,
    ...     mesh=my_mesh,
    ... )

    >>> # Get output data
    >>> result_nodes = op.outputs.nodes()
    >>> result_connectivity = op.outputs.connectivity()
    """

    def __init__(
        self,
        mesh_scoping=None,
        include_mid_nodes=None,
        mesh=None,
        config=None,
        server=None,
    ):
        super().__init__(name="mesh_to_graphics_edges", config=config, server=server)
        self._inputs = InputsMeshToGraphicsEdges(self)
        self._outputs = OutputsMeshToGraphicsEdges(self)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if include_mid_nodes is not None:
            self.inputs.include_mid_nodes.connect(include_mid_nodes)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Generate edges of surface elements for input mesh
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document=r"""""",
                ),
                6: PinSpecification(
                    name="include_mid_nodes",
                    type_names=["bool"],
                    optional=True,
                    document=r"""""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document=r"""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="nodes",
                    type_names=["field"],
                    optional=False,
                    document=r"""node coordinates""",
                ),
                2: PinSpecification(
                    name="connectivity",
                    type_names=["property_field"],
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
        return Operator.default_config(name="mesh_to_graphics_edges", server=server)

    @property
    def inputs(self) -> InputsMeshToGraphicsEdges:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsMeshToGraphicsEdges.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsMeshToGraphicsEdges:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsMeshToGraphicsEdges.
        """
        return super().outputs


class InputsMeshToGraphicsEdges(_Inputs):
    """Intermediate class used to connect user inputs to
    mesh_to_graphics_edges operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_include_mid_nodes = bool()
    >>> op.inputs.include_mid_nodes.connect(my_include_mid_nodes)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_to_graphics_edges._spec().inputs, op)
        self._mesh_scoping = Input(
            mesh_to_graphics_edges._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._mesh_scoping)
        self._include_mid_nodes = Input(
            mesh_to_graphics_edges._spec().input_pin(6), 6, op, -1
        )
        self._inputs.append(self._include_mid_nodes)
        self._mesh = Input(mesh_to_graphics_edges._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)

    @property
    def mesh_scoping(self) -> Input:
        r"""Allows to connect mesh_scoping input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def include_mid_nodes(self) -> Input:
        r"""Allows to connect include_mid_nodes input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
        >>> op.inputs.include_mid_nodes.connect(my_include_mid_nodes)
        >>> # or
        >>> op.inputs.include_mid_nodes(my_include_mid_nodes)
        """
        return self._include_mid_nodes

    @property
    def mesh(self) -> Input:
        r"""Allows to connect mesh input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh


class OutputsMeshToGraphicsEdges(_Outputs):
    """Intermediate class used to get outputs from
    mesh_to_graphics_edges operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
    >>> # Connect inputs : op.inputs. ...
    >>> result_nodes = op.outputs.nodes()
    >>> result_connectivity = op.outputs.connectivity()
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_to_graphics_edges._spec().outputs, op)
        self._nodes = Output(mesh_to_graphics_edges._spec().output_pin(0), 0, op)
        self._outputs.append(self._nodes)
        self._connectivity = Output(mesh_to_graphics_edges._spec().output_pin(2), 2, op)
        self._outputs.append(self._connectivity)

    @property
    def nodes(self) -> Output:
        r"""Allows to get nodes output of the operator

        node coordinates

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
        >>> # Get the output from op.outputs. ...
        >>> result_nodes = op.outputs.nodes()
        """
        return self._nodes

    @property
    def connectivity(self) -> Output:
        r"""Allows to get connectivity output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
        >>> # Get the output from op.outputs. ...
        >>> result_connectivity = op.outputs.connectivity()
        """
        return self._connectivity
