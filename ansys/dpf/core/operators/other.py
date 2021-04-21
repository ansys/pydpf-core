from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from /shared/home1/cbellot/ansys_inc/v212/aisol/dll/linx64/libAns.Dpf.FEMutils.so plugin, from "other" category
"""

#internal name: topology::topology_from_mesh
#scripting name: wrap_in_topology
class _InputsWrapInTopology(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(wrap_in_topology._spec().inputs, op)
        self.mesh = Input(wrap_in_topology._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.mesh)
        self.id = Input(wrap_in_topology._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.id)

class _OutputsWrapInTopology(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(wrap_in_topology._spec().outputs, op)
        self.mesh = Output(wrap_in_topology._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh)

class wrap_in_topology(Operator):
    """Take various input, and wrap in geometry if necessary.

      available inputs:
         mesh (MeshedRegion, AbstractTopologyEntity)
         id (int) (optional)

      available outputs:
         mesh (AbstractTopologyEntity)

      Examples
      --------
      op = operators.other.wrap_in_topology()

    """
    def __init__(self, mesh=None, id=None, config=None, server=None):
        super().__init__(name="topology::topology_from_mesh", config = config, server = server)
        self.inputs = _InputsWrapInTopology(self)
        self.outputs = _OutputsWrapInTopology(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if id !=None:
            self.inputs.id.connect(id)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take various input, and wrap in geometry if necessary.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","abstract_topology_entity"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "id", type_names=["int32"], optional=True, document="""Id that must be attributed to the generated geometry (default is 0).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_topology_entity"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "topology::topology_from_mesh")

