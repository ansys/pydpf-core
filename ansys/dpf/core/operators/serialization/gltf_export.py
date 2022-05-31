"""
gltf_export
===========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from D:\ANSYSDev\dpf-python-core\examples\07-python-operators\..\..\docs\source\examples\07-python-operators\plugins\gltf_plugin plugin, from "serialization" category
"""

class gltf_export(Operator):
    """Writes a GLTF file for a surface MeshedRegion with triangles elements and a Field using pygltflib python module.

      available inputs:
        - path (str)
        - mesh (MeshedRegion)
        - field (Field)

      available outputs:
        - path (str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.serialization.gltf_export()

      >>> # Make input connections
      >>> my_path = str()
      >>> op.inputs.path.connect(my_path)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.serialization.gltf_export(path=my_path,mesh=my_mesh,field=my_field)

      >>> # Get output data
      >>> result_path = op.outputs.path()"""
    def __init__(self, path=None, mesh=None, field=None, config=None, server=None):
        super().__init__(name="gltf_export", config = config, server = server)
        self._inputs = InputsGltfExport(self)
        self._outputs = OutputsGltfExport(self)
        if path !=None:
            self.inputs.path.connect(path)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Writes a GLTF file for a surface MeshedRegion with triangles elements and a Field using pygltflib python module.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "path", type_names=["string"], optional=False, document="""path to write GLTF file"""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""3D vector Field to export (ie displacement Field).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "path", type_names=["string"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "gltf_export")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsGltfExport 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsGltfExport 
        """
        return super().outputs


#internal name: gltf_export
#scripting name: gltf_export
class InputsGltfExport(_Inputs):
    """Intermediate class used to connect user inputs to gltf_export operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.gltf_export()
      >>> my_path = str()
      >>> op.inputs.path.connect(my_path)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
    """
    def __init__(self, op: Operator):
        super().__init__(gltf_export._spec().inputs, op)
        self._path = Input(gltf_export._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._path)
        self._mesh = Input(gltf_export._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)
        self._field = Input(gltf_export._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._field)

    @property
    def path(self):
        """Allows to connect path input to the operator

        - pindoc: path to write GLTF file

        Parameters
        ----------
        my_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.gltf_export()
        >>> op.inputs.path.connect(my_path)
        >>> #or
        >>> op.inputs.path(my_path)

        """
        return self._path

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.gltf_export()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: 3D vector Field to export (ie displacement Field).

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.gltf_export()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

class OutputsGltfExport(_Outputs):
    """Intermediate class used to get outputs from gltf_export operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.gltf_export()
      >>> # Connect inputs : op.inputs. ...
      >>> result_path = op.outputs.path()
    """
    def __init__(self, op: Operator):
        super().__init__(gltf_export._spec().outputs, op)
        self._path = Output(gltf_export._spec().output_pin(0), 0, op) 
        self._outputs.append(self._path)

    @property
    def path(self):
        """Allows to get path output of the operator


        Returns
        ----------
        my_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.gltf_export()
        >>> # Connect inputs : op.inputs. ...
        >>> result_path = op.outputs.path() 
        """
        return self._path

