"""
gauss_to_node
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "geo" category
"""

class gauss_to_node(Operator):
    """Extrapolating results available at Gauss or quadrature points to nodal points for one field. The available elements are : Linear quadrangle , parabolique quadrangle,Linear Hexagonal, quadratic hexagonal , linear tetrahedral, quadratic tetrahedral 

      available inputs:
        - field (Field)
        - scoping (Scoping) (optional)
        - mesh (MeshedRegion) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.gauss_to_node()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.geo.gauss_to_node(field=my_field,scoping=my_scoping,mesh=my_mesh)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, scoping=None, mesh=None, config=None, server=None):
        super().__init__(name="gauss_to_node", config = config, server = server)
        self._inputs = InputsGaussToNode(self)
        self._outputs = OutputsGaussToNode(self)
        if field !=None:
            self.inputs.field.connect(field)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extrapolating results available at Gauss or quadrature points to nodal points for one field. The available elements are : Linear quadrangle , parabolique quadrangle,Linear Hexagonal, quadratic hexagonal , linear tetrahedral, quadratic tetrahedral """,
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""Scoping to integrate on, if not provided, the one from input field is provided."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""Mesh to integrate on.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "gauss_to_node")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsGaussToNode 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsGaussToNode 
        """
        return super().outputs


#internal name: gauss_to_node
#scripting name: gauss_to_node
class InputsGaussToNode(_Inputs):
    """Intermediate class used to connect user inputs to gauss_to_node operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.gauss_to_node()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(gauss_to_node._spec().inputs, op)
        self._field = Input(gauss_to_node._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._scoping = Input(gauss_to_node._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._scoping)
        self._mesh = Input(gauss_to_node._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def field(self):
        """Allows to connect field input to the operator

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.gauss_to_node()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator

        - pindoc: Scoping to integrate on, if not provided, the one from input field is provided.

        Parameters
        ----------
        my_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.gauss_to_node()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> #or
        >>> op.inputs.scoping(my_scoping)

        """
        return self._scoping

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: Mesh to integrate on.

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.gauss_to_node()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsGaussToNode(_Outputs):
    """Intermediate class used to get outputs from gauss_to_node operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.gauss_to_node()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(gauss_to_node._spec().outputs, op)
        self._field = Output(gauss_to_node._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.gauss_to_node()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

