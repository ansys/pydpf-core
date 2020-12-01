from ansys import dpf
from ansys.dpf import post
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
    result = post.result(FILE_PATH)
    disp = result.nodal_displacement()
    disp.num_fields()
    rescoper = Rescoper(result._model.metadata.meshed_region, disp.result_fields_container[0].location, disp.result_fields_container[0].component_count)
    assert rescoper.location == disp.result_fields_container[0].location
    assert rescoper.mesh_scoping.location == locations.nodal
    stress = result.elemental_stress()
    stress.num_fields()
    rescoper = Rescoper(result._model.metadata.meshed_region, stress.result_fields_container[0].location, stress.result_fields_container[0].component_count)
    assert rescoper.location == stress.result_fields_container[0].location
    assert rescoper.mesh_scoping.location == locations.elemental
    

def test_rescoper_nanfield():
    result = post.result(FILE_PATH)
    disp = result.nodal_displacement()
    disp.num_fields()
    rescoper1 = Rescoper(result._model.metadata.meshed_region, disp.result_fields_container[0].location, disp.result_fields_container[0].component_count)
    assert rescoper1.nan_field.__len__() == 15129
    assert rescoper1.nan_field[10].__len__() == 3
    for j in rescoper1.nan_field:
        for i in j:
            assert np.isnan(i)
    stress = result.elemental_stress()
    stress.num_fields()
    rescoper2 = Rescoper(result._model.metadata.meshed_region, stress.result_fields_container[0].location, stress.result_fields_container[0].component_count)
    assert rescoper2.nan_field.__len__() == 10292
    assert rescoper2.nan_field[10].__len__() == 6
    for j in rescoper1.nan_field:
        for i in j:
            assert np.isnan(i)
    

def test_rescoper_rescope():
    result = post.result(FILE_PATH)
    disp = result.nodal_displacement()
    disp.num_fields()
    rescoper = Rescoper(result._model.metadata.meshed_region, disp.result_fields_container[0].location, disp.result_fields_container[0].component_count)
    field = rescoper.rescope(disp.result_fields_container[0])
    assert field.__len__() == 15129
    assert field[0].__len__() == 3
    assert field[20][2] == -1.0882665178147842e-07
    assert field[103][0] == 1.334345300352076e-07
    assert field[12][1] == 4.343049969079495e-07