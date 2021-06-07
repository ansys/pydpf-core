"""
integrate_over_elements
=======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "geo" category
"""

class integrate_over_elements(Operator):
    """Integration of an input field over mesh.

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
      >>> op = dpf.operators.geo.integrate_over_elements()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.geo.integrate_over_elements(field=my_field,scoping=my_scoping,mesh=my_mesh)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, scoping=None, mesh=None, config=None, server=None):
        super().__init__(name="element::integrate", config = config, server = server)
        self._inputs = InputsIntegrateOverElements(self)
        self._outputs = OutputsIntegrateOverElements(self)
        if field !=None:
            self.inputs.field.connect(field)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Integration of an input field over mesh.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""Integrate the input field over a specific scoping."""), 
                                 2 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""Mesh to integrate on, if not provided the one from input field is provided.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "element::integrate")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsIntegrateOverElements 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsIntegrateOverElements 
        """
        return super().outputs


#internal name: element::integrate
#scripting name: integrate_over_elements
class InputsIntegrateOverElements(_Inputs):
    """Intermediate class used to connect user inputs to integrate_over_elements operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.integrate_over_elements()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(integrate_over_elements._spec().inputs, op)
        self._field = Input(integrate_over_elements._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._scoping = Input(integrate_over_elements._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._scoping)
        self._mesh = Input(integrate_over_elements._spec().input_pin(2), 2, op, -1) 
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

        >>> op = dpf.operators.geo.integrate_over_elements()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator

        - pindoc: Integrate the input field over a specific scoping.

        Parameters
        ----------
        my_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.integrate_over_elements()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> #or
        >>> op.inputs.scoping(my_scoping)

        """
        return self._scoping

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: Mesh to integrate on, if not provided the one from input field is provided.

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.integrate_over_elements()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsIntegrateOverElements(_Outputs):
    """Intermediate class used to get outputs from integrate_over_elements operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.integrate_over_elements()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(integrate_over_elements._spec().outputs, op)
        self._field = Output(integrate_over_elements._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.geo.integrate_over_elements()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

