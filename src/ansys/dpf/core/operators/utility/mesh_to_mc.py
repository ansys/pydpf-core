"""
mesh_to_mc
==========
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class mesh_to_mc(Operator):
    """Creates a meshes container containing the mesh provided on pin 0.

    Parameters
    ----------
    mesh : MeshedRegion or MeshesContainer
        If a meshes container is set in input, it is
        passed on as an output with the
        additional label space (if any).
    label : dict
        Sets a label space.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.mesh_to_mc()

    >>> # Make input connections
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_label = dict()
    >>> op.inputs.label.connect(my_label)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.mesh_to_mc(
    ...     mesh=my_mesh,
    ...     label=my_label,
    ... )

    >>> # Get output data
    >>> result_meshes_container = op.outputs.meshes_container()
    """

    def __init__(self, mesh=None, label=None, config=None, server=None):
        super().__init__(name="InjectToMeshesContainer", config=config, server=server)
        self._inputs = InputsMeshToMc(self)
        self._outputs = OutputsMeshToMc(self)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if label is not None:
            self.inputs.label.connect(label)

    @staticmethod
    def _spec():
        description = (
            """Creates a meshes container containing the mesh provided on pin 0."""
        )
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=False,
                    document="""If a meshes container is set in input, it is
        passed on as an output with the
        additional label space (if any).""",
                ),
                1: PinSpecification(
                    name="label",
                    type_names=["label_space"],
                    optional=False,
                    document="""Sets a label space.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="meshes_container",
                    type_names=["meshes_container"],
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
        return Operator.default_config(name="InjectToMeshesContainer", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMeshToMc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMeshToMc
        """
        return super().outputs


class InputsMeshToMc(_Inputs):
    """Intermediate class used to connect user inputs to
    mesh_to_mc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.mesh_to_mc()
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_label = dict()
    >>> op.inputs.label.connect(my_label)
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_to_mc._spec().inputs, op)
        self._mesh = Input(mesh_to_mc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._mesh)
        self._label = Input(mesh_to_mc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._label)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        If a meshes container is set in input, it is
        passed on as an output with the
        additional label space (if any).

        Parameters
        ----------
        my_mesh : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.mesh_to_mc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def label(self):
        """Allows to connect label input to the operator.

        Sets a label space.

        Parameters
        ----------
        my_label : dict

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.mesh_to_mc()
        >>> op.inputs.label.connect(my_label)
        >>> # or
        >>> op.inputs.label(my_label)
        """
        return self._label


class OutputsMeshToMc(_Outputs):
    """Intermediate class used to get outputs from
    mesh_to_mc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.mesh_to_mc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_meshes_container = op.outputs.meshes_container()
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_to_mc._spec().outputs, op)
        self._meshes_container = Output(mesh_to_mc._spec().output_pin(0), 0, op)
        self._outputs.append(self._meshes_container)

    @property
    def meshes_container(self):
        """Allows to get meshes_container output of the operator

        Returns
        ----------
        my_meshes_container : MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.mesh_to_mc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_meshes_container = op.outputs.meshes_container()
        """  # noqa: E501
        return self._meshes_container