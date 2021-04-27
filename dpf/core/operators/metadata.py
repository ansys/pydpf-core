"""
Metadata Operators
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "metadata" category
"""

#internal name: mesh_support_provider
#scripting name: mesh_support_provider
class _InputsMeshSupportProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(mesh_support_provider._spec().inputs, op)
        self.streams_container = Input(mesh_support_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(mesh_support_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsMeshSupportProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(mesh_support_provider._spec().outputs, op)
        self.abstract_field_support = Output(mesh_support_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self.abstract_field_support)

class mesh_support_provider(Operator):
    """Read the mesh support.

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         abstract_field_support (AbstractFieldSupport)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.mesh_support_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Get output data
      >>> result_abstract_field_support = op.outputs.abstract_field_support()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="mesh_support_provider", config = config, server = server)
        self.inputs = _InputsMeshSupportProvider(self)
        self.outputs = _OutputsMeshSupportProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read the mesh support.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container) (optional)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "abstract_field_support", type_names=["abstract_field_support"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh_support_provider")

#internal name: ResultInfoProvider
#scripting name: result_info_provider
class _InputsResultInfoProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(result_info_provider._spec().inputs, op)
        self.streams_container = Input(result_info_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(result_info_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsResultInfoProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(result_info_provider._spec().outputs, op)
        self.result_info = Output(result_info_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self.result_info)

class result_info_provider(Operator):
    """Read the result info with information sucha as available results or unit system from the results files contained in the streams or data sources.

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         result_info (ResultInfo)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.result_info_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Get output data
      >>> result_result_info = op.outputs.result_info()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="ResultInfoProvider", config = config, server = server)
        self.inputs = _InputsResultInfoProvider(self)
        self.outputs = _OutputsResultInfoProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read the result info with information sucha as available results or unit system from the results files contained in the streams or data sources.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container) (optional)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "result_info", type_names=["result_info"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ResultInfoProvider")

#internal name: TimeFreqSupportProvider
#scripting name: time_freq_provider
class _InputsTimeFreqProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(time_freq_provider._spec().inputs, op)
        self.streams_container = Input(time_freq_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(time_freq_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsTimeFreqProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(time_freq_provider._spec().outputs, op)
        self.time_freq_support = Output(time_freq_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self.time_freq_support)

class time_freq_provider(Operator):
    """Read the time freq support from the results files contained in the streams or data sources.

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         time_freq_support (TimeFreqSupport)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.time_freq_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Get output data
      >>> result_time_freq_support = op.outputs.time_freq_support()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="TimeFreqSupportProvider", config = config, server = server)
        self.inputs = _InputsTimeFreqProvider(self)
        self.outputs = _OutputsTimeFreqProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read the time freq support from the results files contained in the streams or data sources.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container) (optional)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "time_freq_support", type_names=["time_freq_support"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "TimeFreqSupportProvider")

#internal name: MaterialsProvider
#scripting name: material_provider
class _InputsMaterialProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(material_provider._spec().inputs, op)
        self.streams_container = Input(material_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(material_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsMaterialProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(material_provider._spec().outputs, op)
        self.materials = Output(material_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self.materials)

class material_provider(Operator):
    """Read available materials and properties from the results files contained in the streams or data sources.

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         materials (Materials)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.material_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Get output data
      >>> result_materials = op.outputs.materials()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="MaterialsProvider", config = config, server = server)
        self.inputs = _InputsMaterialProvider(self)
        self.outputs = _OutputsMaterialProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read available materials and properties from the results files contained in the streams or data sources.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "materials", type_names=["materials"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "MaterialsProvider")

#internal name: stream_provider
#scripting name: streams_provider
class _InputsStreamsProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(streams_provider._spec().inputs, op)
        self.data_sources = Input(streams_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsStreamsProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(streams_provider._spec().outputs, op)
        self.streams_container = Output(streams_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self.streams_container)

class streams_provider(Operator):
    """Creates streams (files with cache) from the data sources.

      available inputs:
         data_sources (DataSources)

      available outputs:
         streams_container (StreamsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.streams_provider()

      >>> # Make input connections
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Get output data
      >>> result_streams_container = op.outputs.streams_container()"""
    def __init__(self, data_sources=None, config=None, server=None):
        super().__init__(name="stream_provider", config = config, server = server)
        self.inputs = _InputsStreamsProvider(self)
        self.outputs = _OutputsStreamsProvider(self)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Creates streams (files with cache) from the data sources.""",
                             map_input_pin_spec={
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "stream_provider")

#internal name: MeshSelectionManagerProvider
#scripting name: mesh_selection_manager_provider
class _InputsMeshSelectionManagerProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(mesh_selection_manager_provider._spec().inputs, op)
        self.streams_container = Input(mesh_selection_manager_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(mesh_selection_manager_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsMeshSelectionManagerProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(mesh_selection_manager_provider._spec().outputs, op)
        self.mesh_selection_manager = Output(mesh_selection_manager_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self.mesh_selection_manager)

class mesh_selection_manager_provider(Operator):
    """Read mesh properties from the results files contained in the streams or data sources and make those properties available through a mesh selection manager in output.

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         mesh_selection_manager (MeshSelectionManager)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.mesh_selection_manager_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Get output data
      >>> result_mesh_selection_manager = op.outputs.mesh_selection_manager()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="MeshSelectionManagerProvider", config = config, server = server)
        self.inputs = _InputsMeshSelectionManagerProvider(self)
        self.outputs = _OutputsMeshSelectionManagerProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read mesh properties from the results files contained in the streams or data sources and make those properties available through a mesh selection manager in output.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container) (optional)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_selection_manager", type_names=["mesh_selection_manager"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "MeshSelectionManagerProvider")

#internal name: boundary_conditions
#scripting name: boundary_condition_provider
class _InputsBoundaryConditionProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(boundary_condition_provider._spec().inputs, op)
        self.streams_container = Input(boundary_condition_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(boundary_condition_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsBoundaryConditionProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(boundary_condition_provider._spec().outputs, op)
        self.results_info_as_field = Output( _modify_output_spec_with_one_type(boundary_condition_provider._spec().output_pin(0), "field"), 0, op) 
        self._outputs.append(self.results_info_as_field)
        self.results_info_as_fields_container = Output( _modify_output_spec_with_one_type(boundary_condition_provider._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.results_info_as_fields_container)

class boundary_condition_provider(Operator):
    """Read boundary conditions from the results files contained in the streams or data sources.

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         results_info (Field ,FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.boundary_condition_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Get output data
      >>> result_results_info = op.outputs.results_info()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="boundary_conditions", config = config, server = server)
        self.inputs = _InputsBoundaryConditionProvider(self)
        self.outputs = _OutputsBoundaryConditionProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read boundary conditions from the results files contained in the streams or data sources.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "results_info", type_names=["field","fields_container"], optional=False, document="""results info""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "boundary_conditions")

#internal name: is_cyclic
#scripting name: is_cyclic
class _InputsIsCyclic(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(is_cyclic._spec().inputs, op)
        self.streams_container = Input(is_cyclic._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(is_cyclic._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsIsCyclic(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(is_cyclic._spec().outputs, op)
        self.file_path = Output(is_cyclic._spec().output_pin(0), 0, op) 
        self._outputs.append(self.file_path)

class is_cyclic(Operator):
    """Read if the model is cyclic form the result file.

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         file_path (str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.is_cyclic()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Get output data
      >>> result_file_path = op.outputs.file_path()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="is_cyclic", config = config, server = server)
        self.inputs = _InputsIsCyclic(self)
        self.outputs = _OutputsIsCyclic(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read if the model is cyclic form the result file.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container) (optional)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document="""returns 'single_stage' or 'multi_stage' or an empty string for non cyclic model""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "is_cyclic")

#internal name: mat_support_provider
#scripting name: material_support_provider
class _InputsMaterialSupportProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(material_support_provider._spec().inputs, op)
        self.streams_container = Input(material_support_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(material_support_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsMaterialSupportProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(material_support_provider._spec().outputs, op)
        self.abstract_field_support = Output(material_support_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self.abstract_field_support)

class material_support_provider(Operator):
    """Read the material support.

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         abstract_field_support (AbstractFieldSupport)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.material_support_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Get output data
      >>> result_abstract_field_support = op.outputs.abstract_field_support()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="mat_support_provider", config = config, server = server)
        self.inputs = _InputsMaterialSupportProvider(self)
        self.outputs = _OutputsMaterialSupportProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read the material support.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container) (optional)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "abstract_field_support", type_names=["abstract_field_support"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mat_support_provider")

"""
Metadata Operators
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "metadata" category
"""

#internal name: cyclic_expansion_mesh
#scripting name: cyclic_mesh_expansion
class _InputsCyclicMeshExpansion(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_mesh_expansion._spec().inputs, op)
        self.sector_meshed_region = Input(cyclic_mesh_expansion._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.sector_meshed_region)
        self.cyclic_support = Input(cyclic_mesh_expansion._spec().input_pin(16), 16, op, -1) 
        self._inputs.append(self.cyclic_support)
        self.sectors_to_expand = Input(cyclic_mesh_expansion._spec().input_pin(18), 18, op, -1) 
        self._inputs.append(self.sectors_to_expand)

class _OutputsCyclicMeshExpansion(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_mesh_expansion._spec().outputs, op)
        self.meshed_region = Output(cyclic_mesh_expansion._spec().output_pin(0), 0, op) 
        self._outputs.append(self.meshed_region)
        self.cyclic_support = Output(cyclic_mesh_expansion._spec().output_pin(1), 1, op) 
        self._outputs.append(self.cyclic_support)

class cyclic_mesh_expansion(Operator):
    """Expand the mesh.

      available inputs:
         sector_meshed_region (MeshedRegion, MeshesContainer) (optional)
         cyclic_support (CyclicSupport)
         sectors_to_expand (list, Scoping, ScopingsContainer) (optional)

      available outputs:
         meshed_region (MeshedRegion)
         cyclic_support (CyclicSupport)

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

      >>> # Get output data
      >>> result_meshed_region = op.outputs.meshed_region()
      >>> result_cyclic_support = op.outputs.cyclic_support()"""
    def __init__(self, sector_meshed_region=None, cyclic_support=None, sectors_to_expand=None, config=None, server=None):
        super().__init__(name="cyclic_expansion_mesh", config = config, server = server)
        self.inputs = _InputsCyclicMeshExpansion(self)
        self.outputs = _OutputsCyclicMeshExpansion(self)
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

"""
Metadata Operators
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "metadata" category
"""

#internal name: mapdl::rst::support_provider_cyclic
#scripting name: cyclic_support_provider
class _InputsCyclicSupportProvider(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_support_provider._spec().inputs, op)
        self.streams_container = Input(cyclic_support_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(cyclic_support_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.sector_meshed_region = Input(cyclic_support_provider._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self.sector_meshed_region)
        self.expanded_meshed_region = Input(cyclic_support_provider._spec().input_pin(15), 15, op, -1) 
        self._inputs.append(self.expanded_meshed_region)
        self.sectors_to_expand = Input(cyclic_support_provider._spec().input_pin(18), 18, op, -1) 
        self._inputs.append(self.sectors_to_expand)

class _OutputsCyclicSupportProvider(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(cyclic_support_provider._spec().outputs, op)
        self.cyclic_support = Output(cyclic_support_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self.cyclic_support)
        self.sector_meshes = Output(cyclic_support_provider._spec().output_pin(1), 1, op) 
        self._outputs.append(self.sector_meshes)

class cyclic_support_provider(Operator):
    """Read the cyclic support (DPF entity containing necessary informations for expansions) and expands the mesh.

      available inputs:
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources)
         sector_meshed_region (MeshedRegion, MeshesContainer) (optional)
         expanded_meshed_region (MeshedRegion, MeshesContainer) (optional)
         sectors_to_expand (Scoping, ScopingsContainer, list) (optional)

      available outputs:
         cyclic_support (CyclicSupport)
         sector_meshes (MeshesContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.cyclic_support_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_sector_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)
      >>> my_expanded_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.expanded_meshed_region.connect(my_expanded_meshed_region)
      >>> my_sectors_to_expand = dpf.Scoping()
      >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)

      >>> # Get output data
      >>> result_cyclic_support = op.outputs.cyclic_support()
      >>> result_sector_meshes = op.outputs.sector_meshes()"""
    def __init__(self, streams_container=None, data_sources=None, sector_meshed_region=None, expanded_meshed_region=None, sectors_to_expand=None, config=None, server=None):
        super().__init__(name="mapdl::rst::support_provider_cyclic", config = config, server = server)
        self.inputs = _InputsCyclicSupportProvider(self)
        self.outputs = _OutputsCyclicSupportProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if sector_meshed_region !=None:
            self.inputs.sector_meshed_region.connect(sector_meshed_region)
        if expanded_meshed_region !=None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if sectors_to_expand !=None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read the cyclic support (DPF entity containing necessary informations for expansions) and expands the mesh.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "sector_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh of the first sector."""), 
                                 15 : PinSpecification(name = "expanded_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""if this pin is set, expanding the mesh is not necessary."""), 
                                 18 : PinSpecification(name = "sectors_to_expand", type_names=["scoping","scopings_container","vector<int32>"], optional=True, document="""sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "sector_meshes", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::support_provider_cyclic")

