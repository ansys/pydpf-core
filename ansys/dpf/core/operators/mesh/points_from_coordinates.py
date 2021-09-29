"""
points_from_coordinates
=======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "mesh" category
"""

class points_from_coordinates(Operator):
    """Extract a mesh made of points elements. This mesh is made from input meshes coordinates on the input scopings.

      available inputs:
        - nodes_to_keep (Scoping, ScopingsContainer)
        - mesh (MeshedRegion, MeshesContainer)

      available outputs:
        - meshed_region (MeshedRegion)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.points_from_coordinates()

      >>> # Make input connections
      >>> my_nodes_to_keep = dpf.Scoping()
      >>> op.inputs.nodes_to_keep.connect(my_nodes_to_keep)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.points_from_coordinates(nodes_to_keep=my_nodes_to_keep,mesh=my_mesh)

      >>> # Get output data
      >>> result_meshed_region = op.outputs.meshed_region()"""
    def __init__(self, nodes_to_keep=None, mesh=None, config=None, server=None):
        super().__init__(name="mesh::points_from_coordinates", config = config, server = server)
        self._inputs = InputsPointsFromCoordinates(self)
        self._outputs = OutputsPointsFromCoordinates(self)
        if nodes_to_keep !=None:
            self.inputs.nodes_to_keep.connect(nodes_to_keep)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extract a mesh made of points elements. This mesh is made from input meshes coordinates on the input scopings.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "nodes_to_keep", type_names=["scoping","scopings_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh::points_from_coordinates")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPointsFromCoordinates 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPointsFromCoordinates 
        """
        return super().outputs


#internal name: mesh::points_from_coordinates
#scripting name: points_from_coordinates
class InputsPointsFromCoordinates(_Inputs):
    """Intermediate class used to connect user inputs to points_from_coordinates operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.points_from_coordinates()
      >>> my_nodes_to_keep = dpf.Scoping()
      >>> op.inputs.nodes_to_keep.connect(my_nodes_to_keep)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(points_from_coordinates._spec().inputs, op)
        self._nodes_to_keep = Input(points_from_coordinates._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._nodes_to_keep)
        self._mesh = Input(points_from_coordinates._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def nodes_to_keep(self):
        """Allows to connect nodes_to_keep input to the operator

        Parameters
        ----------
        my_nodes_to_keep : Scoping, ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.points_from_coordinates()
        >>> op.inputs.nodes_to_keep.connect(my_nodes_to_keep)
        >>> #or
        >>> op.inputs.nodes_to_keep(my_nodes_to_keep)

        """
        return self._nodes_to_keep

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.points_from_coordinates()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsPointsFromCoordinates(_Outputs):
    """Intermediate class used to get outputs from points_from_coordinates operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.points_from_coordinates()
      >>> # Connect inputs : op.inputs. ...
      >>> result_meshed_region = op.outputs.meshed_region()
    """
    def __init__(self, op: Operator):
        super().__init__(points_from_coordinates._spec().outputs, op)
        self._meshed_region = Output(points_from_coordinates._spec().output_pin(0), 0, op) 
        self._outputs.append(self._meshed_region)

    @property
    def meshed_region(self):
        """Allows to get meshed_region output of the operator


        Returns
        ----------
        my_meshed_region : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.points_from_coordinates()
        >>> # Connect inputs : op.inputs. ...
        >>> result_meshed_region = op.outputs.meshed_region() 
        """
        return self._meshed_region

