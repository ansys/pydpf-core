import pytest
import numpy as np

from ansys.dpf import core
import ansys.grpc.dpf




def test_workflowwithgeneratedcode(allkindofcomplexity):
    disp = core.operators.result.displacement()
    ds = core.DataSources(allkindofcomplexity)
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


def test_calloperators(allkindofcomplexity):
    my_data_sources = core.DataSources(allkindofcomplexity)
    my_model = core.Model(my_data_sources)
    displacement_op = my_model.results.displacement()
    assert isinstance(displacement_op, ansys.dpf.core.dpf_operator.Operator)
    norm_op = my_model.operator('norm_fc')
    assert isinstance(norm_op, ansys.dpf.core.dpf_operator.Operator)
    square_op = core.operators.math.sqr()
    assert isinstance(square_op, ansys.dpf.core.operators.math._Sqr)


def test_makeconnections(allkindofcomplexity):
    my_data_sources = core.DataSources(allkindofcomplexity)
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


def test_get_result(allkindofcomplexity):
    stress = core.operators.result.stress_X()
    ds = core.DataSources(allkindofcomplexity)
    stress.inputs.data_sources.connect(ds)
    stress.inputs.requested_location.connect('Nodal')
    avg = core.operators.averaging.to_elemental_fc()
    avg.inputs.fields_container.connect(stress.outputs.fields_container)
    out = avg.outputs.fields_container()
    assert len(out) == 2
    assert len(out[0]) == 1281
    assert np.isclose(out[0].data[3], 9328792.294959497)


def test_operator_inheritance(allkindofcomplexity):
    stress = core.operators.result.stress_X()
    ds = core.DataSources(allkindofcomplexity)
    stress.connect(4, ds)
    stress.inputs.requested_location.connect('Nodal')
    avg = core.operators.averaging.to_elemental_fc()
    avg.connect(0, stress)
    avg.run()
    out = avg.outputs.fields_container()
    assert len(out) == 2
    assert len(out[0]) == 1281
    assert np.isclose(out[0].data[3], 9328792.294959497)


def test_operator_inheritance_2(allkindofcomplexity):
    stress = core.operators.result.stress_X()
    ds = core.DataSources(allkindofcomplexity)
    stress.inputs.data_sources.connect(ds)
    stress.inputs.requested_location.connect('Nodal')
    avg = core.operators.averaging.to_elemental_fc()
    avg.connect(0, stress)
    avg.run()
    out = avg.outputs.fields_container()
    assert len(out) == 2
    assert len(out[0]) == 1281
    assert np.isclose(out[0].data[3], 9328792.294959497)


def test_inputs_inheritance(allkindofcomplexity):
    stress = core.operators.result.stress_X()
    ds = core.DataSources(allkindofcomplexity)
    stress.inputs.connect(ds)
    stress.inputs.requested_location.connect('Nodal')
    avg = core.operators.averaging.to_elemental_fc()
    avg.connect(0, stress)
    avg.run()
    out = avg.outputs.fields_container()
    assert len(out) == 2
    assert len(out[0]) == 1281
    assert np.isclose(out[0].data[3], 9328792.294959497)
