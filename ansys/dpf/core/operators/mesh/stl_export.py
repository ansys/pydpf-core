"""
stl_export
==========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "mesh" category
"""

class stl_export(Operator):
    """export a mesh into a stl file.

      available inputs:
        - mesh (MeshedRegion)
        - file_path (str)

      available outputs:
        - data_sources (DataSources)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.stl_export()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_file_path = str()
      >>> op.inputs.file_path.connect(my_file_path)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.stl_export(mesh=my_mesh,file_path=my_file_path)

      >>> # Get output data
      >>> result_data_sources = op.outputs.data_sources()"""
    def __init__(self, mesh=None, file_path=None, config=None, server=None):
        super().__init__(name="stl_export", config = config, server = server)
        self._inputs = InputsStlExport(self)
        self._outputs = OutputsStlExport(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if file_path !=None:
            self.inputs.file_path.connect(file_path)

    @staticmethod
    def _spec():
        spec = Specification(description="""export a mesh into a stl file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "stl_export")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsStlExport 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsStlExport 
        """
        return super().outputs


#internal name: stl_export
#scripting name: stl_export
class InputsStlExport(_Inputs):
    """Intermediate class used to connect user inputs to stl_export operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.stl_export()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_file_path = str()
      >>> op.inputs.file_path.connect(my_file_path)
    """
    def __init__(self, op: Operator):
        super().__init__(stl_export._spec().inputs, op)
        self._mesh = Input(stl_export._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mesh)
        self._file_path = Input(stl_export._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._file_path)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.stl_export()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def file_path(self):
        """Allows to connect file_path input to the operator

        Parameters
        ----------
        my_file_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.stl_export()
        >>> op.inputs.file_path.connect(my_file_path)
        >>> #or
        >>> op.inputs.file_path(my_file_path)

        """
        return self._file_path

class OutputsStlExport(_Outputs):
    """Intermediate class used to get outputs from stl_export operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.stl_export()
      >>> # Connect inputs : op.inputs. ...
      >>> result_data_sources = op.outputs.data_sources()
    """
    def __init__(self, op: Operator):
        super().__init__(stl_export._spec().outputs, op)
        self._data_sources = Output(stl_export._spec().output_pin(0), 0, op) 
        self._outputs.append(self._data_sources)

    @property
    def data_sources(self):
        """Allows to get data_sources output of the operator


        Returns
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.stl_export()
        >>> # Connect inputs : op.inputs. ...
        >>> result_data_sources = op.outputs.data_sources() 
        """
        return self._data_sources

