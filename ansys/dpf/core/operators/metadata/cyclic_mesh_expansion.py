"""
cyclic_mesh_expansion
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "metadata" category
"""

class cyclic_mesh_expansion(Operator):
    """Expand the mesh.

      available inputs:
        - sector_meshed_region (MeshedRegion, MeshesContainer) (optional)
        - cyclic_support (CyclicSupport)
        - sectors_to_expand (list, Scoping, ScopingsContainer) (optional)

      available outputs:
        - meshed_region (MeshedRegion)
        - cyclic_support (CyclicSupport)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.cyclic_mesh_expansion()

      >>> # Make input connections
      >>> my_sector_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)
      >>> my_cyclic_support = dpf.CyclicSupport()
      >>> op.inputs.cyclic_support.connect(my_cyclic_support)
      >>> my_sectors_to_expand = dpf.list()
      >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.metadata.cyclic_mesh_expansion(sector_meshed_region=my_sector_meshed_region,cyclic_support=my_cyclic_support,sectors_to_expand=my_sectors_to_expand)

      >>> # Get output data
      >>> result_meshed_region = op.outputs.meshed_region()
      >>> result_cyclic_support = op.outputs.cyclic_support()"""
    def __init__(self, sector_meshed_region=None, cyclic_support=None, sectors_to_expand=None, config=None, server=None):
        super().__init__(name="cyclic_expansion_mesh", config = config, server = server)
        self._inputs = InputsCyclicMeshExpansion(self)
        self._outputs = OutputsCyclicMeshExpansion(self)
        if sector_meshed_region !=None:
            self.inputs.sector_meshed_region.connect(sector_meshed_region)
        if cyclic_support !=None:
            self.inputs.cyclic_support.connect(cyclic_support)
        if sectors_to_expand !=None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)

    @staticmethod
    def _spec():
        spec = Specification(description="""Expand the mesh.""",
                             map_input_pin_spec={
                                 7 : PinSpecification(name = "sector_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document=""""""), 
                                 16 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=False, document=""""""), 
                                 18 : PinSpecification(name = "sectors_to_expand", type_names=["vector<int32>","scoping","scopings_container"], optional=True, document="""sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region"], optional=False, document="""expanded meshed region."""), 
                                 1 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=False, document="""input cyclic support modified in place containing the new expanded meshed regions.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cyclic_expansion_mesh")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCyclicMeshExpansion 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCyclicMeshExpansion 
        """
        return super().outputs


#internal name: cyclic_expansion_mesh
#scripting name: cyclic_mesh_expansion
class InputsCyclicMeshExpansion(_Inputs):
    """Intermediate class used to connect user inputs to cyclic_mesh_expansion operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
      >>> my_sector_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)
      >>> my_cyclic_support = dpf.CyclicSupport()
      >>> op.inputs.cyclic_support.connect(my_cyclic_support)
      >>> my_sectors_to_expand = dpf.list()
      >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
    """
    def __init__(self, op: Operator):
        super().__init__(cyclic_mesh_expansion._spec().inputs, op)
        self._sector_meshed_region = Input(cyclic_mesh_expansion._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._sector_meshed_region)
        self._cyclic_support = Input(cyclic_mesh_expansion._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self._cyclic_support)
        self._sectors_to_expand = Input(cyclic_mesh_expansion._spec().input_pin(18), 18, op, -1) 
        self._inputs.append(self._sectors_to_expand)

    @property
    def sector_meshed_region(self):
        """Allows to connect sector_meshed_region input to the operator

        Parameters
        ----------
        my_sector_meshed_region : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
        >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)
        >>> #or
        >>> op.inputs.sector_meshed_region(my_sector_meshed_region)

        """
        return self._sector_meshed_region

    @property
    def cyclic_support(self):
        """Allows to connect cyclic_support input to the operator

        Parameters
        ----------
        my_cyclic_support : CyclicSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
        >>> op.inputs.cyclic_support.connect(my_cyclic_support)
        >>> #or
        >>> op.inputs.cyclic_support(my_cyclic_support)

        """
        return self._cyclic_support

    @property
    def sectors_to_expand(self):
        """Allows to connect sectors_to_expand input to the operator

        - pindoc: sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.

        Parameters
        ----------
        my_sectors_to_expand : list, Scoping, ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
        >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
        >>> #or
        >>> op.inputs.sectors_to_expand(my_sectors_to_expand)

        """
        return self._sectors_to_expand

class OutputsCyclicMeshExpansion(_Outputs):
    """Intermediate class used to get outputs from cyclic_mesh_expansion operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
      >>> # Connect inputs : op.inputs. ...
      >>> result_meshed_region = op.outputs.meshed_region()
      >>> result_cyclic_support = op.outputs.cyclic_support()
    """
    def __init__(self, op: Operator):
        super().__init__(cyclic_mesh_expansion._spec().outputs, op)
        self._meshed_region = Output(cyclic_mesh_expansion._spec().output_pin(0), 0, op) 
        self._outputs.append(self._meshed_region)
        self._cyclic_support = Output(cyclic_mesh_expansion._spec().output_pin(1), 1, op) 
        self._outputs.append(self._cyclic_support)

    @property
    def meshed_region(self):
        """Allows to get meshed_region output of the operator


        - pindoc: expanded meshed region.

        Returns
        ----------
        my_meshed_region : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_meshed_region = op.outputs.meshed_region() 
        """
        return self._meshed_region

    @property
    def cyclic_support(self):
        """Allows to get cyclic_support output of the operator


        - pindoc: input cyclic support modified in place containing the new expanded meshed regions.

        Returns
        ----------
        my_cyclic_support : CyclicSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_cyclic_support = op.outputs.cyclic_support() 
        """
        return self._cyclic_support

