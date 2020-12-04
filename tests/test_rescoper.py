from ansys import dpf
from ansys.dpf.core import Model, Operator
from ansys.dpf.core import locations
import os
import numpy as np
from ansys.dpf.core.rescoper import Rescoper

if not dpf.core.has_local_server():
    dpf.core.start_local_server()
    

if 'AWP_UNIT_TEST_FILES' in os.environ:
    unit_test_files = os.environ['AWP_UNIT_TEST_FILES']
else:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')
    
FILE_PATH = os.path.join(unit_test_files, 'DataProcessing', 'rst_operators',
                              'allKindOfComplexity.rst')



def test_rescoper_init():
    model = Model(FILE_PATH)
    disp_op = model.results.displacement()
    disp = disp_op.outputs.fields_container()
    assert len(disp) == 1
    rescoper = Rescoper(model.metadata.meshed_region, disp[0].location, disp[0].component_count)
    assert rescoper.location == disp[0].location
    assert rescoper.mesh_scoping.location == locations.nodal
    stress_op = model.results.stress()
    stress_op.inputs.requested_location.connect(locations.elemental)
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress_op.outputs.fields_container)
    stress = avg_op.outputs.fields_container()
    assert len(stress) == 2
    rescoper = Rescoper(model.metadata.meshed_region, stress[0].location, stress[0].component_count)
    assert rescoper.location == stress[0].location
    assert rescoper.mesh_scoping.location == locations.elemental
    

def test_rescoper_nanfield():
    model = Model(FILE_PATH)
    disp_op = model.results.displacement()
    disp = disp_op.outputs.fields_container()
    assert len(disp) == 1
    rescoper1 = Rescoper(model.metadata.meshed_region, disp[0].location, disp[0].component_count)
    assert len(rescoper1.nan_field) == 15129
    assert len(rescoper1.nan_field[10]) == 3
    for j in rescoper1.nan_field:
        for i in j:
            assert np.isnan(i)
    stress_op = model.results.stress()
    stress_op.inputs.requested_location.connect(locations.elemental)
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress_op.outputs.fields_container)
    stress = avg_op.outputs.fields_container()
    assert len(stress) == 2
    rescoper2 = Rescoper(model.metadata.meshed_region, stress[0].location, stress[0].component_count)
    assert len(rescoper2.nan_field) == 10292
    assert len(rescoper2.nan_field[10]) == 6
    for j in rescoper1.nan_field:
        for i in j:
            assert np.isnan(i)
    

def test_rescoper_rescope():
    model = Model(FILE_PATH)
    disp_op = model.results.displacement()
    disp = disp_op.outputs.fields_container()
    assert len(disp) == 1
    rescoper = Rescoper(model.metadata.meshed_region, disp[0].location, disp[0].component_count)
    field = rescoper.rescope(disp[0])
    assert len(field) == 15129
    assert len(field[0]) == 3
    assert field[20][2] == -1.0882665178147842e-07
    assert field[103][0] == 1.334345300352076e-07
    assert field[12][1] == 4.343049969079495e-07