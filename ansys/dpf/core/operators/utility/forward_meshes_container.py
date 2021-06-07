"""
forward_meshes_container
========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class forward_meshes_container(Operator):
    """Return the input mesh or meshes container into a meshes container.

      available inputs:
        - meshes (MeshesContainer, MeshedRegion)
        - default_label (str) (optional)

      available outputs:
        - meshes_container (MeshesContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.forward_meshes_container()

      >>> # Make input connections
      >>> my_meshes = dpf.MeshesContainer()
      >>> op.inputs.meshes.connect(my_meshes)
      >>> my_default_label = str()
      >>> op.inputs.default_label.connect(my_default_label)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.forward_meshes_container(meshes=my_meshes,default_label=my_default_label)

      >>> # Get output data
      >>> result_meshes_container = op.outputs.meshes_container()"""
    def __init__(self, meshes=None, default_label=None, config=None, server=None):
        super().__init__(name="forward_meshes_container", config = config, server = server)
        self._inputs = InputsForwardMeshesContainer(self)
        self._outputs = OutputsForwardMeshesContainer(self)
        if meshes !=None:
            self.inputs.meshes.connect(meshes)
        if default_label !=None:
            self.inputs.default_label.connect(default_label)

    @staticmethod
    def _spec():
        spec = Specification(description="""Return the input mesh or meshes container into a meshes container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "meshes", type_names=["meshes_container","abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "default_label", type_names=["string"], optional=True, document="""this default label is used if a new meshes container needs to be created (default is unknown)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "meshes_container", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "forward_meshes_container")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsForwardMeshesContainer 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsForwardMeshesContainer 
        """
        return super().outputs


#internal name: forward_meshes_container
#scripting name: forward_meshes_container
class InputsForwardMeshesContainer(_Inputs):
    """Intermediate class used to connect user inputs to forward_meshes_container operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.forward_meshes_container()
      >>> my_meshes = dpf.MeshesContainer()
      >>> op.inputs.meshes.connect(my_meshes)
      >>> my_default_label = str()
      >>> op.inputs.default_label.connect(my_default_label)
    """
    def __init__(self, op: Operator):
        super().__init__(forward_meshes_container._spec().inputs, op)
        self._meshes = Input(forward_meshes_container._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._meshes)
        self._default_label = Input(forward_meshes_container._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._default_label)

    @property
    def meshes(self):
        """Allows to connect meshes input to the operator

        Parameters
        ----------
        my_meshes : MeshesContainer, MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.forward_meshes_container()
        >>> op.inputs.meshes.connect(my_meshes)
        >>> #or
        >>> op.inputs.meshes(my_meshes)

        """
        return self._meshes

    @property
    def default_label(self):
        """Allows to connect default_label input to the operator

        - pindoc: this default label is used if a new meshes container needs to be created (default is unknown)

        Parameters
        ----------
        my_default_label : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.forward_meshes_container()
        >>> op.inputs.default_label.connect(my_default_label)
        >>> #or
        >>> op.inputs.default_label(my_default_label)

        """
        return self._default_label

class OutputsForwardMeshesContainer(_Outputs):
    """Intermediate class used to get outputs from forward_meshes_container operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.forward_meshes_container()
      >>> # Connect inputs : op.inputs. ...
      >>> result_meshes_container = op.outputs.meshes_container()
    """
    def __init__(self, op: Operator):
        super().__init__(forward_meshes_container._spec().outputs, op)
        self._meshes_container = Output(forward_meshes_container._spec().output_pin(0), 0, op) 
        self._outputs.append(self._meshes_container)

    @property
    def meshes_container(self):
        """Allows to get meshes_container output of the operator


        Returns
        ----------
        my_meshes_container : MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.forward_meshes_container()
        >>> # Connect inputs : op.inputs. ...
        >>> result_meshes_container = op.outputs.meshes_container() 
        """
        return self._meshes_container

