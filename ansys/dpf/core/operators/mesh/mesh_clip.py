"""
mesh_clip
=========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "mesh" category
"""

class mesh_clip(Operator):
    """Clip a volume mesh along an iso value x, and construct the volume mesh defined by v < x.

      available inputs:
        - field (Field)
        - iso_value (float)
        - closed_surface (int)
        - mesh (MeshedRegion) (optional)
        - slice_surfaces (bool)

      available outputs:
        - field (Field)
        - mesh (MeshedRegion)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.mesh_clip()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_iso_value = float()
      >>> op.inputs.iso_value.connect(my_iso_value)
      >>> my_closed_surface = int()
      >>> op.inputs.closed_surface.connect(my_closed_surface)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_slice_surfaces = bool()
      >>> op.inputs.slice_surfaces.connect(my_slice_surfaces)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.mesh_clip(field=my_field,iso_value=my_iso_value,closed_surface=my_closed_surface,mesh=my_mesh,slice_surfaces=my_slice_surfaces)

      >>> # Get output data
      >>> result_field = op.outputs.field()
      >>> result_mesh = op.outputs.mesh()"""
    def __init__(self, field=None, iso_value=None, closed_surface=None, mesh=None, slice_surfaces=None, config=None, server=None):
        super().__init__(name="mesh_clip", config = config, server = server)
        self._inputs = InputsMeshClip(self)
        self._outputs = OutputsMeshClip(self)
        if field !=None:
            self.inputs.field.connect(field)
        if iso_value !=None:
            self.inputs.iso_value.connect(iso_value)
        if closed_surface !=None:
            self.inputs.closed_surface.connect(closed_surface)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if slice_surfaces !=None:
            self.inputs.slice_surfaces.connect(slice_surfaces)

    @staticmethod
    def _spec():
        spec = Specification(description="""Clip a volume mesh along an iso value x, and construct the volume mesh defined by v < x.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "iso_value", type_names=["double"], optional=False, document="""iso value"""), 
                                 2 : PinSpecification(name = "closed_surface", type_names=["int32"], optional=False, document="""1: closed surface, 0:iso surface"""), 
                                 3 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "slice_surfaces", type_names=["bool"], optional=False, document="""true: slicing will also take into account shell and 2D elements, false: slicing will ignore shell and 2D elements. default is true""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "mesh", type_names=["meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh_clip")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMeshClip 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMeshClip 
        """
        return super().outputs


#internal name: mesh_clip
#scripting name: mesh_clip
class InputsMeshClip(_Inputs):
    """Intermediate class used to connect user inputs to mesh_clip operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.mesh_clip()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_iso_value = float()
      >>> op.inputs.iso_value.connect(my_iso_value)
      >>> my_closed_surface = int()
      >>> op.inputs.closed_surface.connect(my_closed_surface)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_slice_surfaces = bool()
      >>> op.inputs.slice_surfaces.connect(my_slice_surfaces)
    """
    def __init__(self, op: Operator):
        super().__init__(mesh_clip._spec().inputs, op)
        self._field = Input(mesh_clip._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._iso_value = Input(mesh_clip._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._iso_value)
        self._closed_surface = Input(mesh_clip._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._closed_surface)
        self._mesh = Input(mesh_clip._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._mesh)
        self._slice_surfaces = Input(mesh_clip._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._slice_surfaces)

    @property
    def field(self):
        """Allows to connect field input to the operator

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_clip()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def iso_value(self):
        """Allows to connect iso_value input to the operator

        - pindoc: iso value

        Parameters
        ----------
        my_iso_value : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_clip()
        >>> op.inputs.iso_value.connect(my_iso_value)
        >>> #or
        >>> op.inputs.iso_value(my_iso_value)

        """
        return self._iso_value

    @property
    def closed_surface(self):
        """Allows to connect closed_surface input to the operator

        - pindoc: 1: closed surface, 0:iso surface

        Parameters
        ----------
        my_closed_surface : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_clip()
        >>> op.inputs.closed_surface.connect(my_closed_surface)
        >>> #or
        >>> op.inputs.closed_surface(my_closed_surface)

        """
        return self._closed_surface

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_clip()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def slice_surfaces(self):
        """Allows to connect slice_surfaces input to the operator

        - pindoc: true: slicing will also take into account shell and 2D elements, false: slicing will ignore shell and 2D elements. default is true

        Parameters
        ----------
        my_slice_surfaces : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_clip()
        >>> op.inputs.slice_surfaces.connect(my_slice_surfaces)
        >>> #or
        >>> op.inputs.slice_surfaces(my_slice_surfaces)

        """
        return self._slice_surfaces

class OutputsMeshClip(_Outputs):
    """Intermediate class used to get outputs from mesh_clip operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.mesh_clip()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
      >>> result_mesh = op.outputs.mesh()
    """
    def __init__(self, op: Operator):
        super().__init__(mesh_clip._spec().outputs, op)
        self._field = Output(mesh_clip._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)
        self._mesh = Output(mesh_clip._spec().output_pin(2), 2, op) 
        self._outputs.append(self._mesh)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_clip()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

    @property
    def mesh(self):
        """Allows to get mesh output of the operator


        Returns
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_clip()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh() 
        """
        return self._mesh

