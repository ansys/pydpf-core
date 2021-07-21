"""
normals_provider_nl
===================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "geo" category
"""

class normals_provider_nl(Operator):
    """Compute the normals on nodes/elements based on integration points(more accurate for non-linear elements), on a skin mesh

      available inputs:
        - mesh (MeshedRegion)
        - mesh_scoping (Scoping) (optional)
        - requested_location (str) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.normals_provider_nl()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.geo.normals_provider_nl(mesh=my_mesh,mesh_scoping=my_mesh_scoping,requested_location=my_requested_location)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, mesh=None, mesh_scoping=None, requested_location=None, config=None, server=None):
        super().__init__(name="normals_provider_nl", config = config, server = server)
        self._inputs = InputsNormalsProviderNl(self)
        self._outputs = OutputsNormalsProviderNl(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the normals on nodes/elements based on integration points(more accurate for non-linear elements), on a skin mesh""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""skin or shell mesh region"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""Elemental, ElementalNodal, or Nodal scoping. Location derived from this."""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""If no scoping, specifies location. If scoping is Elemental or ElementalNodal this overrides scoping. Default Elemental.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "normals_provider_nl")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNormalsProviderNl 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNormalsProviderNl 
        """
        return super().outputs


#internal name: normals_provider_nl
#scripting name: normals_provider_nl
class InputsNormalsProviderNl(_Inputs):
    """Intermediate class used to connect user inputs to normals_provider_nl operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.normals_provider_nl()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
    """
    def __init__(self, op: Operator):
        super().__init__(normals_provider_nl._spec().inputs, op)
        self._mesh = Input(normals_provider_nl._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mesh)
        self._mesh_scoping = Input(normals_provider_nl._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._requested_location = Input(normals_provider_nl._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self._requested_location)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: skin or shell mesh region

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.normals_provider_nl()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        - pindoc: Elemental, ElementalNodal, or Nodal scoping. Location derived from this.

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.normals_provider_nl()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator

        - pindoc: If no scoping, specifies location. If scoping is Elemental or ElementalNodal this overrides scoping. Default Elemental.

        Parameters
        ----------
        my_requested_location : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.normals_provider_nl()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> #or
        >>> op.inputs.requested_location(my_requested_location)

        """
        return self._requested_location

class OutputsNormalsProviderNl(_Outputs):
    """Intermediate class used to get outputs from normals_provider_nl operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.normals_provider_nl()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(normals_provider_nl._spec().outputs, op)
        self._field = Output(normals_provider_nl._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.geo.normals_provider_nl()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

