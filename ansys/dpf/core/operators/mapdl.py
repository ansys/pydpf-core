from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

#internal name: mapdl::run
#scripting name: mapdl.run
def _get_input_spec_run(pin):
    inpin0 = _PinSpecification(name = "mapdl_exe_path", type_names = ["string"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "working_dir", type_names = ["string"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "number_of_processes", type_names = ["int32"], optional = True, document = """Set the number of MPI processes used for resolution (default is 2)""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the input file.""")
    inputs_dict_run = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        4 : inpin4
    }
    return inputs_dict_run[pin]

def _get_output_spec_run(pin):
    outpin0 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], document = """""")
    outputs_dict_run = { 
        0 : outpin0
    }
    return outputs_dict_run[pin]

class _InputSpecRun(_Inputs):
    def __init__(self, op: _Operator):
        self.mapdl_exe_path = _Input(_get_input_spec_run(0), 0, op, -1) 
        self.working_dir = _Input(_get_input_spec_run(1), 1, op, -1) 
        self.number_of_processes = _Input(_get_input_spec_run(2), 2, op, -1) 
        self.data_sources = _Input(_get_input_spec_run(4), 4, op, -1) 

class _OutputSpecRun(_Outputs):
    def __init__(self, op: _Operator):
        self.data_sources = _Output(_get_output_spec_run(0), 0, op) 

class _Run:
    """Operator's description:
Internal name is "mapdl::run"
Scripting name is "mapdl.run"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::run")
- using dpf.operators.result.mapdl.run()

Input list: 
   0: mapdl_exe_path 
   1: working_dir 
   2: number_of_processes (Set the number of MPI processes used for resolution (default is 2))
   4: data_sources (data sources containing the input file.)
Output list: 
   0: data_sources 
"""
    def __init__(self):
         self._name = "mapdl::run"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecRun(self._op)
         self.outputs = _OutputSpecRun(self._op)

def run():
    return _Run()

#internal name: mapdl::nmisc
#scripting name: mapdl.nmisc
def _get_input_spec_nmisc(pin):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_nmisc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    return inputs_dict_nmisc[pin]

def _get_output_spec_nmisc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_nmisc = { 
        0 : outpin0
    }
    return outputs_dict_nmisc[pin]

class _InputSpecNmisc(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_nmisc(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_nmisc(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_nmisc(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_nmisc(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_nmisc(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_nmisc(7), 7, op, -1) 

class _OutputSpecNmisc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_nmisc(0), 0, op) 

class _Nmisc:
    """Operator's description:
Internal name is "mapdl::nmisc"
Scripting name is "mapdl.nmisc"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::nmisc")
- using dpf.operators.result.mapdl.nmisc()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::nmisc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecNmisc(self._op)
         self.outputs = _OutputSpecNmisc(self._op)

def nmisc():
    return _Nmisc()

#internal name: mapdl::smisc
#scripting name: mapdl.smisc
def _get_input_spec_smisc(pin):
    inpin0 = _PinSpecification(name = "time_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scopings_container","scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = True, document = """FieldsContainer already allocated modified inplace""")
    inpin3 = _PinSpecification(name = "streams_container", type_names = ["streams_container","stream"], optional = True, document = """Streams containing the result file.""")
    inpin4 = _PinSpecification(name = "data_sources", type_names = ["data_sources"], optional = False, document = """data sources containing the result file.""")
    inpin7 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inputs_dict_smisc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4,
        7 : inpin7
    }
    return inputs_dict_smisc[pin]

def _get_output_spec_smisc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """FieldsContainer filled in""")
    outputs_dict_smisc = { 
        0 : outpin0
    }
    return outputs_dict_smisc[pin]

class _InputSpecSmisc(_Inputs):
    def __init__(self, op: _Operator):
        self.time_scoping = _Input(_get_input_spec_smisc(0), 0, op, -1) 
        self.mesh_scoping = _Input(_get_input_spec_smisc(1), 1, op, -1) 
        self.fields_container = _Input(_get_input_spec_smisc(2), 2, op, -1) 
        self.streams_container = _Input(_get_input_spec_smisc(3), 3, op, -1) 
        self.data_sources = _Input(_get_input_spec_smisc(4), 4, op, -1) 
        self.mesh = _Input(_get_input_spec_smisc(7), 7, op, -1) 

class _OutputSpecSmisc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_smisc(0), 0, op) 

class _Smisc:
    """Operator's description:
Internal name is "mapdl::smisc"
Scripting name is "mapdl.smisc"

This operator can be instantiated in both following ways:
- using dpf.Operator("mapdl::smisc")
- using dpf.operators.result.mapdl.smisc()

Input list: 
   0: time_scoping 
   1: mesh_scoping 
   2: fields_container (FieldsContainer already allocated modified inplace)
   3: streams_container (Streams containing the result file.)
   4: data_sources (data sources containing the result file.)
   7: mesh 
Output list: 
   0: fields_container (FieldsContainer filled in)
"""
    def __init__(self):
         self._name = "mapdl::smisc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSmisc(self._op)
         self.outputs = _OutputSpecSmisc(self._op)

def smisc():
    return _Smisc()

#internal name: PRES_Reader
#scripting name: mapdl.pres_to_field
def _get_input_spec_pres_to_field(pin):
    inpin0 = _PinSpecification(name = "filepath", type_names = ["string"], optional = False, document = """filepath""")
    inputs_dict_pres_to_field = { 
        0 : inpin0
    }
    return inputs_dict_pres_to_field[pin]

def _get_output_spec_pres_to_field(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_pres_to_field = { 
        0 : outpin0
    }
    return outputs_dict_pres_to_field[pin]

class _InputSpecPresToField(_Inputs):
    def __init__(self, op: _Operator):
        self.filepath = _Input(_get_input_spec_pres_to_field(0), 0, op, -1) 

class _OutputSpecPresToField(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_pres_to_field(0), 0, op) 

class _PresToField:
    """Operator's description:
Internal name is "PRES_Reader"
Scripting name is "mapdl.pres_to_field"

This operator can be instantiated in both following ways:
- using dpf.Operator("PRES_Reader")
- using dpf.operators.result.mapdl.pres_to_field()

Input list: 
   0: filepath (filepath)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "PRES_Reader"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPresToField(self._op)
         self.outputs = _OutputSpecPresToField(self._op)

def pres_to_field():
    return _PresToField()

#internal name: PRNS_Reader
#scripting name: mapdl.prns_to_field
def _get_input_spec_prns_to_field(pin):
    inpin0 = _PinSpecification(name = "filepath", type_names = ["string"], optional = False, document = """filepath""")
    inputs_dict_prns_to_field = { 
        0 : inpin0
    }
    return inputs_dict_prns_to_field[pin]

def _get_output_spec_prns_to_field(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_prns_to_field = { 
        0 : outpin0
    }
    return outputs_dict_prns_to_field[pin]

class _InputSpecPrnsToField(_Inputs):
    def __init__(self, op: _Operator):
        self.filepath = _Input(_get_input_spec_prns_to_field(0), 0, op, -1) 

class _OutputSpecPrnsToField(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_prns_to_field(0), 0, op) 

class _PrnsToField:
    """Operator's description:
Internal name is "PRNS_Reader"
Scripting name is "mapdl.prns_to_field"

This operator can be instantiated in both following ways:
- using dpf.Operator("PRNS_Reader")
- using dpf.operators.result.mapdl.prns_to_field()

Input list: 
   0: filepath (filepath)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "PRNS_Reader"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecPrnsToField(self._op)
         self.outputs = _OutputSpecPrnsToField(self._op)

def prns_to_field():
    return _PrnsToField()

