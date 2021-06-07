"""
from_mesh
=========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "scoping" category
"""

class from_mesh(Operator):
    """Provides the entire mesh scoping based on the requested location

      available inputs:
        - mesh (MeshedRegion)
        - requested_location (str) (optional)

      available outputs:
        - scoping (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.scoping.from_mesh()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.scoping.from_mesh(mesh=my_mesh,requested_location=my_requested_location)

      >>> # Get output data
      >>> result_scoping = op.outputs.scoping()"""
    def __init__(self, mesh=None, requested_location=None, config=None, server=None):
        super().__init__(name="MeshScopingProvider", config = config, server = server)
        self._inputs = InputsFromMesh(self)
        self._outputs = OutputsFromMesh(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Provides the entire mesh scoping based on the requested location""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""if nothing the operator returns the nodes scoping, possible locations are: Nodal or Elemental""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "MeshScopingProvider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFromMesh 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFromMesh 
        """
        return super().outputs


#internal name: MeshScopingProvider
#scripting name: from_mesh
class InputsFromMesh(_Inputs):
    """Intermediate class used to connect user inputs to from_mesh operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.from_mesh()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
    """
    def __init__(self, op: Operator):
        super().__init__(from_mesh._spec().inputs, op)
        self._mesh = Input(from_mesh._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mesh)
        self._requested_location = Input(from_mesh._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._requested_location)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.from_mesh()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator

        - pindoc: if nothing the operator returns the nodes scoping, possible locations are: Nodal or Elemental

        Parameters
        ----------
        my_requested_location : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.from_mesh()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> #or
        >>> op.inputs.requested_location(my_requested_location)

        """
        return self._requested_location

class OutputsFromMesh(_Outputs):
    """Intermediate class used to get outputs from from_mesh operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.from_mesh()
      >>> # Connect inputs : op.inputs. ...
      >>> result_scoping = op.outputs.scoping()
    """
    def __init__(self, op: Operator):
        super().__init__(from_mesh._spec().outputs, op)
        self._scoping = Output(from_mesh._spec().output_pin(0), 0, op) 
        self._outputs.append(self._scoping)

    @property
    def scoping(self):
        """Allows to get scoping output of the operator


        Returns
        ----------
        my_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.from_mesh()
        >>> # Connect inputs : op.inputs. ...
        >>> result_scoping = op.outputs.scoping() 
        """
        return self._scoping

