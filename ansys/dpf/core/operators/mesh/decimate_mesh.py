"""
decimate_mesh
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "mesh" category
"""

class decimate_mesh(Operator):
    """Decimate a surface meshed region with triangle elements

      available inputs:
        - mesh (MeshedRegion)
        - preservation_ratio (float) (optional)
        - aggressiveness (int) (optional)

      available outputs:
        - mesh (MeshedRegion)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.decimate_mesh()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_preservation_ratio = float()
      >>> op.inputs.preservation_ratio.connect(my_preservation_ratio)
      >>> my_aggressiveness = int()
      >>> op.inputs.aggressiveness.connect(my_aggressiveness)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.decimate_mesh(mesh=my_mesh,preservation_ratio=my_preservation_ratio,aggressiveness=my_aggressiveness)

      >>> # Get output data
      >>> result_mesh = op.outputs.mesh()"""
    def __init__(self, mesh=None, preservation_ratio=None, aggressiveness=None, config=None, server=None):
        super().__init__(name="decimate_mesh", config = config, server = server)
        self._inputs = InputsDecimateMesh(self)
        self._outputs = OutputsDecimateMesh(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if preservation_ratio !=None:
            self.inputs.preservation_ratio.connect(preservation_ratio)
        if aggressiveness !=None:
            self.inputs.aggressiveness.connect(aggressiveness)

    @staticmethod
    def _spec():
        spec = Specification(description="""Decimate a surface meshed region with triangle elements""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""Mesh to decimate"""), 
                                 1 : PinSpecification(name = "preservation_ratio", type_names=["double"], optional=True, document="""Ratio of triangles to preserve. Default value is 0.5."""), 
                                 2 : PinSpecification(name = "aggressiveness", type_names=["int32"], optional=True, document="""Quality measure for the resulting decimated mesh. Lower aggresiveness will provide a higher quality mesh with the tradeoff of higher execution time. Value range is 0 to 150, default is 1.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""Decimated mesh""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "decimate_mesh")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsDecimateMesh 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsDecimateMesh 
        """
        return super().outputs


#internal name: decimate_mesh
#scripting name: decimate_mesh
class InputsDecimateMesh(_Inputs):
    """Intermediate class used to connect user inputs to decimate_mesh operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.decimate_mesh()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_preservation_ratio = float()
      >>> op.inputs.preservation_ratio.connect(my_preservation_ratio)
      >>> my_aggressiveness = int()
      >>> op.inputs.aggressiveness.connect(my_aggressiveness)
    """
    def __init__(self, op: Operator):
        super().__init__(decimate_mesh._spec().inputs, op)
        self._mesh = Input(decimate_mesh._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mesh)
        self._preservation_ratio = Input(decimate_mesh._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._preservation_ratio)
        self._aggressiveness = Input(decimate_mesh._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._aggressiveness)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: Mesh to decimate

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.decimate_mesh()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def preservation_ratio(self):
        """Allows to connect preservation_ratio input to the operator

        - pindoc: Ratio of triangles to preserve. Default value is 0.5.

        Parameters
        ----------
        my_preservation_ratio : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.decimate_mesh()
        >>> op.inputs.preservation_ratio.connect(my_preservation_ratio)
        >>> #or
        >>> op.inputs.preservation_ratio(my_preservation_ratio)

        """
        return self._preservation_ratio

    @property
    def aggressiveness(self):
        """Allows to connect aggressiveness input to the operator

        - pindoc: Quality measure for the resulting decimated mesh. Lower aggresiveness will provide a higher quality mesh with the tradeoff of higher execution time. Value range is 0 to 150, default is 1.

        Parameters
        ----------
        my_aggressiveness : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.decimate_mesh()
        >>> op.inputs.aggressiveness.connect(my_aggressiveness)
        >>> #or
        >>> op.inputs.aggressiveness(my_aggressiveness)

        """
        return self._aggressiveness

class OutputsDecimateMesh(_Outputs):
    """Intermediate class used to get outputs from decimate_mesh operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.decimate_mesh()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh = op.outputs.mesh()
    """
    def __init__(self, op: Operator):
        super().__init__(decimate_mesh._spec().outputs, op)
        self._mesh = Output(decimate_mesh._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mesh)

    @property
    def mesh(self):
        """Allows to get mesh output of the operator


        - pindoc: Decimated mesh

        Returns
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.decimate_mesh()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh() 
        """
        return self._mesh

