import tempfile
import os

import pytest

from ansys.dpf import core
from ansys import dpf
import ansys.grpc.dpf

if 'AWP_UNIT_TEST_FILES' in os.environ:
    unit_test_files = os.environ['AWP_UNIT_TEST_FILES']
else:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')

# start local server if necessary
if not dpf.core.has_local_server():
    dpf.core.start_local_server()
    
TEST_FILE_PATH = os.path.join(unit_test_files, 'DataProcessing', 'rst_operators',
                              'allKindOfComplexity.rst')

#def test_generateoperatorscode():
#    core.database_tools.loadOperators()
    
def test_workflowwithgeneratedcode():
    disp = core.operators.result.displacement()
    ds = core.DataSources(TEST_FILE_PATH)
    nodes = [1]
    scop = core.Scoping()
    scop.ids = nodes
    scop.location = "Nodal"
    disp.inputs.data_sources.connect(ds)
    disp.inputs.mesh_scoping.connect(scop)
    a = disp.outputs.fields_container.get_data()
    assert a[0].data[0][0] == 7.120546307743541e-07
    assert len(a[0].data[0]) == 3
    assert len(a[0].data) == 1
    norm = core.operators.math.norm()
    norm.inputs.field.connect(disp.outputs.fields_container)
    b = norm.outputs.field()
    assert b.data[0] == 1.26387078548793e-06
    filt = core.operators.filter.scoping.high_pass()
    filt.inputs.field.connect(norm.outputs.field)
    filt.inputs.threshold.connect(1e-05)
    pow_op = core.operators.math.pow()
    pow_op.inputs.factor.connect(3.0)
    pow_op.inputs.field.connect(norm.outputs.field)
    d = pow_op.outputs.field.get_data()
    assert d.data[0] == 2.0188684707833254e-18
    
def test_calloperators():
    my_data_sources = core.DataSources(TEST_FILE_PATH)
    my_model = core.Model(my_data_sources)
    displacement_op = my_model.results.displacement()
    assert isinstance(displacement_op, ansys.dpf.core.dpf_operator.Operator)
    norm_op = my_model.operator('norm_fc')
    assert isinstance(norm_op, ansys.dpf.core.dpf_operator.Operator)
    square_op = core.operators.math.sqr()
    assert isinstance(square_op, ansys.dpf.core.operators.math._Sqr)
    
def test_makeconnections():
    my_data_sources = core.DataSources(TEST_FILE_PATH)
    my_model = core.Model(my_data_sources)
    displacement_op = my_model.results.displacement()
    norm_op = my_model.operator('norm')
    square_op = core.operators.math.sqr()
    assert len(displacement_op.inputs._connected_inputs)==1
    assert len(norm_op.inputs._connected_inputs)==0
    # assert len(square_op.inputs._connected_inputs)==0
    norm_op.inputs.connect(displacement_op.outputs)
    square_op.inputs.field.connect(norm_op.outputs.field)
    assert len(displacement_op.inputs._connected_inputs)==1
    assert len(norm_op.inputs._connected_inputs)==1
    # assert len(square_op.inputs._connected_inputs)==1
    
def test_get_result():
    stress = core.operators.result.stress_X()
    ds = core.DataSources("d:/rst/twobodies.rst")
    stress.inputs.data_sources.connect(ds)
    stress.inputs.requested_location.connect('Elemental')
    avg = core.operators.averaging.to_elemental_fc()
    avg.inputs.fields_container.connect(stress.outputs.fields_container)
    out = avg.outputs.fields_container()
    assert len(out) == 1
    assert len(out[0]) == 914
    assert out[0].data[3] == -2947934263296.0
    mesh_op = core.operators.mesh.mesh_provider()
    mesh_op.inputs.data_sources.connect(ds)
    mesh = mesh_op.outputs.mesh()    
    mesh.plot(out)
    
    