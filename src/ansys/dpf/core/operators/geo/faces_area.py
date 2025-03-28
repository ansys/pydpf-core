"""
faces_area

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


class faces_area(Operator):
    r"""Compute the measure of the Faces (surface for 2D faces of a 3D model or
    length for 1D faces of a 2D model) using default shape functions, except
    for polygons.


    Parameters
    ----------
    mesh: MeshedRegion
    mesh_scoping: Scoping
        If not provided, the measure of all Faces in the mesh is computed. If provided, the Scoping needs to have "Faces" location.

    Returns
    -------
    field: Field

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.geo.faces_area()

    >>> # Make input connections
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.geo.faces_area(
    ...     mesh=my_mesh,
    ...     mesh_scoping=my_mesh_scoping,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, mesh=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="face::area", config=config, server=server)
        self._inputs = InputsFacesArea(self)
        self._outputs = OutputsFacesArea(self)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Compute the measure of the Faces (surface for 2D faces of a 3D model or
length for 1D faces of a 2D model) using default shape functions, except
for polygons.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=False,
                    document=r"""If not provided, the measure of all Faces in the mesh is computed. If provided, the Scoping needs to have "Faces" location.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
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
        return Operator.default_config(name="face::area", server=server)

    @property
    def inputs(self) -> InputsFacesArea:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsFacesArea.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsFacesArea:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsFacesArea.
        """
        return super().outputs


class InputsFacesArea(_Inputs):
    """Intermediate class used to connect user inputs to
    faces_area operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.faces_area()
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    """

    def __init__(self, op: Operator):
        super().__init__(faces_area._spec().inputs, op)
        self._mesh = Input(faces_area._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._mesh)
        self._mesh_scoping = Input(faces_area._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)

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
        >>> op = dpf.operators.geo.faces_area()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def mesh_scoping(self) -> Input:
        r"""Allows to connect mesh_scoping input to the operator.

        If not provided, the measure of all Faces in the mesh is computed. If provided, the Scoping needs to have "Faces" location.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.faces_area()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping


class OutputsFacesArea(_Outputs):
    """Intermediate class used to get outputs from
    faces_area operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.faces_area()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(faces_area._spec().outputs, op)
        self._field = Output(faces_area._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self) -> Output:
        r"""Allows to get field output of the operator

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.faces_area()
        >>> # Get the output from op.outputs. ...
        >>> result_field = op.outputs.field()
        """
        return self._field
