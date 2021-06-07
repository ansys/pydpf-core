"""
moment_of_inertia
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "geo" category
"""

class moment_of_inertia(Operator):
    """Compute the inertia tensor of a set of elements.

      available inputs:
        - mesh (MeshedRegion) (optional)
        - mesh_scoping (Scoping) (optional)
        - field (Field) (optional)
        - boolean (bool) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.moment_of_inertia()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_boolean = bool()
      >>> op.inputs.boolean.connect(my_boolean)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.geo.moment_of_inertia(mesh=my_mesh,mesh_scoping=my_mesh_scoping,field=my_field,boolean=my_boolean)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, mesh=None, mesh_scoping=None, field=None, boolean=None, config=None, server=None):
        super().__init__(name="topology::moment_of_inertia", config = config, server = server)
        self._inputs = InputsMomentOfInertia(self)
        self._outputs = OutputsMomentOfInertia(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if field !=None:
            self.inputs.field.connect(field)
        if boolean !=None:
            self.inputs.boolean.connect(boolean)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the inertia tensor of a set of elements.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""Mesh scoping, if not set, all the elements of the mesh are considered."""), 
                                 2 : PinSpecification(name = "field", type_names=["field"], optional=True, document="""Elemental or nodal ponderation used in computation."""), 
                                 3 : PinSpecification(name = "boolean", type_names=["bool"], optional=True, document="""default true, compute inertia tensor at center of gravity.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "topology::moment_of_inertia")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMomentOfInertia 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMomentOfInertia 
        """
        return super().outputs


#internal name: topology::moment_of_inertia
#scripting name: moment_of_inertia
class InputsMomentOfInertia(_Inputs):
    """Intermediate class used to connect user inputs to moment_of_inertia operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.moment_of_inertia()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_boolean = bool()
      >>> op.inputs.boolean.connect(my_boolean)
    """
    def __init__(self, op: Operator):
        super().__init__(moment_of_inertia._spec().inputs, op)
        self._mesh = Input(moment_of_inertia._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mesh)
        self._mesh_scoping = Input(moment_of_inertia._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._field = Input(moment_of_inertia._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._field)
        self._boolean = Input(moment_of_inertia._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._boolean)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.moment_of_inertia()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        - pindoc: Mesh scoping, if not set, all the elements of the mesh are considered.

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.moment_of_inertia()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: Elemental or nodal ponderation used in computation.

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.moment_of_inertia()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def boolean(self):
        """Allows to connect boolean input to the operator

        - pindoc: default true, compute inertia tensor at center of gravity.

        Parameters
        ----------
        my_boolean : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.moment_of_inertia()
        >>> op.inputs.boolean.connect(my_boolean)
        >>> #or
        >>> op.inputs.boolean(my_boolean)

        """
        return self._boolean

class OutputsMomentOfInertia(_Outputs):
    """Intermediate class used to get outputs from moment_of_inertia operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.moment_of_inertia()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(moment_of_inertia._spec().outputs, op)
        self._field = Output(moment_of_inertia._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.geo.moment_of_inertia()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

