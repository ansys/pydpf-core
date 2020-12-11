from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "metadata" category
"""

#internal name: ResultInfoProvider
#scripting name: result_info_provider
def _get_input_spec_result_info_provider(pin):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inputs_dict_result_info_provider = { 
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_result_info_provider[pin]

def _get_output_spec_result_info_provider(pin):
    outpin0 = _PinSpecification(name = "result_info", type_names = ["result_info"], document = """""")
    outputs_dict_result_info_provider = { 
        0 : outpin0
    }
    return outputs_dict_result_info_provider[pin]

class _InputSpecResultInfoProvider(_Inputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Input(_get_input_spec_result_info_provider(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_result_info_provider(4), 4, op, -1) 

class _OutputSpecResultInfoProvider(_Outputs):
    def __init__(self, op: _Operator):
        self.result_info = _Output(_get_output_spec_result_info_provider(0), 0, op) 

class _ResultInfoProvider(_Operator):
    """Operator's description:
    Internal name is "ResultInfoProvider"
    Scripting name is "result_info_provider"

    Description: Read the result info with information sucha as available results or unit system from the results files contained in the streams or data sources.

    Input list: 
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       0: result_info 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ResultInfoProvider")
    >>> op_way2 = core.operators.metadata.result_info_provider()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ResultInfoProvider")
        self._name = "ResultInfoProvider"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecResultInfoProvider(self._op)
        self.outputs = _OutputSpecResultInfoProvider(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def result_info_provider():
    """Operator's description:
    Internal name is "ResultInfoProvider"
    Scripting name is "result_info_provider"

    Description: Read the result info with information sucha as available results or unit system from the results files contained in the streams or data sources.

    Input list: 
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       0: result_info 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ResultInfoProvider")
    >>> op_way2 = core.operators.metadata.result_info_provider()
    """
    return _ResultInfoProvider()

#internal name: TimeFreqSupportProvider
#scripting name: time_freq_provider
def _get_input_spec_time_freq_provider(pin):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inputs_dict_time_freq_provider = { 
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_time_freq_provider[pin]

def _get_output_spec_time_freq_provider(pin):
    outpin0 = _PinSpecification(name = "time_freq_support", type_names = ["time_freq_support"], document = """""")
    outputs_dict_time_freq_provider = { 
        0 : outpin0
    }
    return outputs_dict_time_freq_provider[pin]

class _InputSpecTimeFreqProvider(_Inputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Input(_get_input_spec_time_freq_provider(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_time_freq_provider(4), 4, op, -1) 

class _OutputSpecTimeFreqProvider(_Outputs):
    def __init__(self, op: _Operator):
        self.time_freq_support = _Output(_get_output_spec_time_freq_provider(0), 0, op) 

class _TimeFreqProvider(_Operator):
    """Operator's description:
    Internal name is "TimeFreqSupportProvider"
    Scripting name is "time_freq_provider"

    Description: Read the time freq support from the results files contained in the streams or data sources.

    Input list: 
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       0: time_freq_support 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TimeFreqSupportProvider")
    >>> op_way2 = core.operators.metadata.time_freq_provider()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("TimeFreqSupportProvider")
        self._name = "TimeFreqSupportProvider"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecTimeFreqProvider(self._op)
        self.outputs = _OutputSpecTimeFreqProvider(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def time_freq_provider():
    """Operator's description:
    Internal name is "TimeFreqSupportProvider"
    Scripting name is "time_freq_provider"

    Description: Read the time freq support from the results files contained in the streams or data sources.

    Input list: 
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       0: time_freq_support 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("TimeFreqSupportProvider")
    >>> op_way2 = core.operators.metadata.time_freq_provider()
    """
    return _TimeFreqProvider()

#internal name: MaterialsProvider
#scripting name: material_provider
def _get_input_spec_material_provider(pin):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inputs_dict_material_provider = { 
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_material_provider[pin]

def _get_output_spec_material_provider(pin):
    outpin0 = _PinSpecification(name = "materials", type_names = ["materials"], document = """""")
    outputs_dict_material_provider = { 
        0 : outpin0
    }
    return outputs_dict_material_provider[pin]

class _InputSpecMaterialProvider(_Inputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Input(_get_input_spec_material_provider(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_material_provider(4), 4, op, -1) 

class _OutputSpecMaterialProvider(_Outputs):
    def __init__(self, op: _Operator):
        self.materials = _Output(_get_output_spec_material_provider(0), 0, op) 

class _MaterialProvider(_Operator):
    """Operator's description:
    Internal name is "MaterialsProvider"
    Scripting name is "material_provider"

    Description: Read available materials and properties from the results files contained in the streams or data sources.

    Input list: 
       3: streams_container (streams (result file container))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       0: materials 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("MaterialsProvider")
    >>> op_way2 = core.operators.metadata.material_provider()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("MaterialsProvider")
        self._name = "MaterialsProvider"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecMaterialProvider(self._op)
        self.outputs = _OutputSpecMaterialProvider(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def material_provider():
    """Operator's description:
    Internal name is "MaterialsProvider"
    Scripting name is "material_provider"

    Description: Read available materials and properties from the results files contained in the streams or data sources.

    Input list: 
       3: streams_container (streams (result file container))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       0: materials 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("MaterialsProvider")
    >>> op_way2 = core.operators.metadata.material_provider()
    """
    return _MaterialProvider()

#internal name: stream_provider
#scripting name: streams_provider
def _get_input_spec_streams_provider(pin):
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_streams_provider = { 
        4 : inpin4
    }
    return inputs_dict_streams_provider[pin]

def _get_output_spec_streams_provider(pin):
    outpin0 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], document = """""")
    outputs_dict_streams_provider = { 
        0 : outpin0
    }
    return outputs_dict_streams_provider[pin]

class _InputSpecStreamsProvider(_Inputs):
    def __init__(self, op: _Operator):
        self.data_sources = _Input(_get_input_spec_streams_provider(4), 4, op, -1) 

class _OutputSpecStreamsProvider(_Outputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Output(_get_output_spec_streams_provider(0), 0, op) 

class _StreamsProvider(_Operator):
    """Operator's description:
    Internal name is "stream_provider"
    Scripting name is "streams_provider"

    Description: Creates streams (files with cache) from the data sources.

    Input list: 
       4: data_sources 

    Output list: 
       0: streams_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("stream_provider")
    >>> op_way2 = core.operators.metadata.streams_provider()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("stream_provider")
        self._name = "stream_provider"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecStreamsProvider(self._op)
        self.outputs = _OutputSpecStreamsProvider(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def streams_provider():
    """Operator's description:
    Internal name is "stream_provider"
    Scripting name is "streams_provider"

    Description: Creates streams (files with cache) from the data sources.

    Input list: 
       4: data_sources 

    Output list: 
       0: streams_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("stream_provider")
    >>> op_way2 = core.operators.metadata.streams_provider()
    """
    return _StreamsProvider()

#internal name: MeshSelectionManagerProvider
#scripting name: mesh_selection_manager_provider
def _get_input_spec_mesh_selection_manager_provider(pin):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inputs_dict_mesh_selection_manager_provider = { 
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_mesh_selection_manager_provider[pin]

def _get_output_spec_mesh_selection_manager_provider(pin):
    outputs_dict_mesh_selection_manager_provider = {
    }
    return outputs_dict_mesh_selection_manager_provider[pin]

class _InputSpecMeshSelectionManagerProvider(_Inputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Input(_get_input_spec_mesh_selection_manager_provider(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_mesh_selection_manager_provider(4), 4, op, -1) 

class _OutputSpecMeshSelectionManagerProvider(_Outputs):
    def __init__(self, op: _Operator):
        pass 

class _MeshSelectionManagerProvider(_Operator):
    """Operator's description:
    Internal name is "MeshSelectionManagerProvider"
    Scripting name is "mesh_selection_manager_provider"

    Description: Read mesh properties from the results files contained in the streams or data sources and make those properties available through a mesh selection manager in output.

    Input list: 
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       empty 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("MeshSelectionManagerProvider")
    >>> op_way2 = core.operators.metadata.mesh_selection_manager_provider()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("MeshSelectionManagerProvider")
        self._name = "MeshSelectionManagerProvider"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecMeshSelectionManagerProvider(self._op)
        self.outputs = _OutputSpecMeshSelectionManagerProvider(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def mesh_selection_manager_provider():
    """Operator's description:
    Internal name is "MeshSelectionManagerProvider"
    Scripting name is "mesh_selection_manager_provider"

    Description: Read mesh properties from the results files contained in the streams or data sources and make those properties available through a mesh selection manager in output.

    Input list: 
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       empty 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("MeshSelectionManagerProvider")
    >>> op_way2 = core.operators.metadata.mesh_selection_manager_provider()
    """
    return _MeshSelectionManagerProvider()

#internal name: boundary_conditions
#scripting name: boundary_condition_provider
def _get_input_spec_boundary_condition_provider(pin):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """""")
    inputs_dict_boundary_condition_provider = { 
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_boundary_condition_provider[pin]

def _get_output_spec_boundary_condition_provider(pin):
    outpin0 = _PinSpecification(name = "results_info", type_names = ["field","fields_container"], document = """results info""")
    outputs_dict_boundary_condition_provider = { 
        0 : outpin0
    }
    return outputs_dict_boundary_condition_provider[pin]

class _InputSpecBoundaryConditionProvider(_Inputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Input(_get_input_spec_boundary_condition_provider(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_boundary_condition_provider(4), 4, op, -1) 

class _OutputSpecBoundaryConditionProvider(_Outputs):
    def __init__(self, op: _Operator):
        self.results_info = _Output(_get_output_spec_boundary_condition_provider(0), 0, op) 

class _BoundaryConditionProvider(_Operator):
    """Operator's description:
    Internal name is "boundary_conditions"
    Scripting name is "boundary_condition_provider"

    Description: Read boundary conditions from the results files contained in the streams or data sources.

    Input list: 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: results_info (results info)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("boundary_conditions")
    >>> op_way2 = core.operators.metadata.boundary_condition_provider()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("boundary_conditions")
        self._name = "boundary_conditions"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecBoundaryConditionProvider(self._op)
        self.outputs = _OutputSpecBoundaryConditionProvider(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def boundary_condition_provider():
    """Operator's description:
    Internal name is "boundary_conditions"
    Scripting name is "boundary_condition_provider"

    Description: Read boundary conditions from the results files contained in the streams or data sources.

    Input list: 
       3: streams_container 
       4: data_sources 

    Output list: 
       0: results_info (results info)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("boundary_conditions")
    >>> op_way2 = core.operators.metadata.boundary_condition_provider()
    """
    return _BoundaryConditionProvider()

#internal name: is_cyclic
#scripting name: is_cyclic
def _get_input_spec_is_cyclic(pin):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """streams (result file container) (optional)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """if the stream is null then we need to get the file path from the data sources""")
    inputs_dict_is_cyclic = { 
        3 : inpin3,
        4 : inpin4
    }
    return inputs_dict_is_cyclic[pin]

def _get_output_spec_is_cyclic(pin):
    outpin0 = _PinSpecification(name = "file_path", type_names = ["string"], document = """returns 'single_stage' or 'multi_stage' or an empty string for non cyclic model""")
    outputs_dict_is_cyclic = { 
        0 : outpin0
    }
    return outputs_dict_is_cyclic[pin]

class _InputSpecIsCyclic(_Inputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Input(_get_input_spec_is_cyclic(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_is_cyclic(4), 4, op, -1) 

class _OutputSpecIsCyclic(_Outputs):
    def __init__(self, op: _Operator):
        self.file_path = _Output(_get_output_spec_is_cyclic(0), 0, op) 

class _IsCyclic(_Operator):
    """Operator's description:
    Internal name is "is_cyclic"
    Scripting name is "is_cyclic"

    Description: Read if the model is cyclic form the result file.

    Input list: 
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       0: file_path (returns 'single_stage' or 'multi_stage' or an empty string for non cyclic model)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("is_cyclic")
    >>> op_way2 = core.operators.metadata.is_cyclic()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("is_cyclic")
        self._name = "is_cyclic"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecIsCyclic(self._op)
        self.outputs = _OutputSpecIsCyclic(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def is_cyclic():
    """Operator's description:
    Internal name is "is_cyclic"
    Scripting name is "is_cyclic"

    Description: Read if the model is cyclic form the result file.

    Input list: 
       3: streams_container (streams (result file container) (optional))
       4: data_sources (if the stream is null then we need to get the file path from the data sources)

    Output list: 
       0: file_path (returns 'single_stage' or 'multi_stage' or an empty string for non cyclic model)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("is_cyclic")
    >>> op_way2 = core.operators.metadata.is_cyclic()
    """
    return _IsCyclic()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from mapdlOperatorsCore.dll plugin, from "metadata" category
"""

#internal name: mapdl::rst::support_provider_cyclic
#scripting name: cyclic_support_provider
def _get_input_spec_cyclic_support_provider(pin):
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "sector_meshed_region", type_names = ["meshed_region"], optional = True, document = """mesh of the first sector.""")
    inpin15 = _PinSpecification(name = "expanded_meshed_region", type_names = ["meshed_region"], optional = True, document = """if this pin is set, expanding the mesh is not necessary.""")
    inpin18 = _PinSpecification(name = "sectors_to_expand", type_names = ["scoping","scopings_container"], optional = True, document = """sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.""")
    inputs_dict_cyclic_support_provider = { 
        3 : inpin3,
        4 : inpin4,
        7 : inpin7,
        15 : inpin15,
        18 : inpin18
    }
    return inputs_dict_cyclic_support_provider[pin]

def _get_output_spec_cyclic_support_provider(pin):
    outpin0 = _PinSpecification(name = "cyclic_support", type_names = ["cyclic_support"], document = """""")
    outpin1 = _PinSpecification(name = "sector_meshed_region", type_names = ["meshed_region"], document = """""")
    outputs_dict_cyclic_support_provider = { 
        0 : outpin0,
        1 : outpin1
    }
    return outputs_dict_cyclic_support_provider[pin]

class _InputSpecCyclicSupportProvider(_Inputs):
    def __init__(self, op: _Operator):
        self.streams_container = _Input(_get_input_spec_cyclic_support_provider(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_cyclic_support_provider(4), 4, op, -1) 
        self.sector_meshed_region = _Input(_get_input_spec_cyclic_support_provider(7), 7, op, -1) 
        self.expanded_meshed_region = _Input(_get_input_spec_cyclic_support_provider(15), 15, op, -1) 
        self.sectors_to_expand = _Input(_get_input_spec_cyclic_support_provider(18), 18, op, -1) 

class _OutputSpecCyclicSupportProvider(_Outputs):
    def __init__(self, op: _Operator):
        self.cyclic_support = _Output(_get_output_spec_cyclic_support_provider(0), 0, op) 
        self.sector_meshed_region = _Output(_get_output_spec_cyclic_support_provider(1), 1, op) 

class _CyclicSupportProvider(_Operator):
    """Operator's description:
    Internal name is "mapdl::rst::support_provider_cyclic"
    Scripting name is "cyclic_support_provider"

    Description: Read the cyclic support (DPF entity containing necessary informations for expansions) and expands the mesh.

    Input list: 
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: sector_meshed_region (mesh of the first sector.)
       15: expanded_meshed_region (if this pin is set, expanding the mesh is not necessary.)
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)

    Output list: 
       0: cyclic_support 
       1: sector_meshed_region 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::support_provider_cyclic")
    >>> op_way2 = core.operators.metadata.cyclic_support_provider()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("mapdl::rst::support_provider_cyclic")
        self._name = "mapdl::rst::support_provider_cyclic"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecCyclicSupportProvider(self._op)
        self.outputs = _OutputSpecCyclicSupportProvider(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def cyclic_support_provider():
    """Operator's description:
    Internal name is "mapdl::rst::support_provider_cyclic"
    Scripting name is "cyclic_support_provider"

    Description: Read the cyclic support (DPF entity containing necessary informations for expansions) and expands the mesh.

    Input list: 
       3: streams_container (Streams containing the result file.)
       4: data_sources (data sources containing the result file.)
       7: sector_meshed_region (mesh of the first sector.)
       15: expanded_meshed_region (if this pin is set, expanding the mesh is not necessary.)
       18: sectors_to_expand (sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.)

    Output list: 
       0: cyclic_support 
       1: sector_meshed_region 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("mapdl::rst::support_provider_cyclic")
    >>> op_way2 = core.operators.metadata.cyclic_support_provider()
    """
    return _CyclicSupportProvider()

