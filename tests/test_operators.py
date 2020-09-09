import os
import numpy as np
from ansys import dpf


if 'AWP_UNIT_TEST_FILES' in os.environ:
    unit_test_files = os.environ['AWP_UNIT_TEST_FILES']
else:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')

TEST_FILE_PATH = os.path.join(unit_test_files, 'DataProcessing', 'rst_operators',
                              'ASimpleBar.rst')


if not dpf.has_local_server():
    dpf.start_local_server()


def test_add_method():
    data = np.array([1, 2, 3])
    field_a = dpf.field_from_array(data)
    field_b = dpf.field_from_array(data)
    fout = dpf.operators.add(field_a, field_b)
    assert np.allclose(fout.data, data*2)


def test_add_builtin():
    data = np.array([1, 2, 3])
    field_a = dpf.field_from_array(data)
    field_b = dpf.field_from_array(data)
    fout = field_a + field_b
    assert np.allclose(fout.data, np.array(data)*2)


def test_element_dot():
    data = np.random.random((10, 3))
    field_a = dpf.field_from_array(data)
    field_b = dpf.field_from_array(data)
    fout = dpf.operators.element_dot(field_a, field_b)
    assert np.allclose(fout.data, np.sum(data*data, 1))


def test_sqr():
    data = np.array([1, 2, 3])
    field = dpf.field_from_array(data)
    field_sqr = dpf.operators.sqr(field)
    assert np.allclose(field_sqr.data, data**2)


def test_sqr_builtin():
    data = np.array([1, 2, 3])
    field = dpf.field_from_array(data)
    field_sqr = field**2
    assert np.allclose(field_sqr.data, data**2)


def test_dot_tensor():
    arr_a = np.ones((5, 3))
    arr_a[:, 2] = 0
    arr_b = np.ones((5, 3))
    arr_b[:, 1] = 0
    field_a = dpf.field_from_array(arr_a)
    field_b = dpf.field_from_array(arr_b)
    fout = dpf.operators.dot_tensor(field_a, field_b)
    arr_out = fout.data
    assert np.all(arr_out[:, [0, 1, 6, 7]] == 1)


def test_nodal_averaging():
    model = dpf.Model(TEST_FILE_PATH)
    evol = model.results.element_nodal_forces()
    field = evol.outputs.fields_container()[0]
    nodal_evol = field.to_nodal()
    assert nodal_evol.location == dpf.locations.nodal

def test_ellispsis_pin():
    model=dpf.Model(TEST_FILE_PATH)
    u = model.operator("U")
    s= model.operator("S")
    op = dpf.Operator("vtk_export")
    op.inputs.connect(r'c:/temp/vtk.vtk')
    op.inputs.fields1(s.outputs)
    op.inputs.fields2(u.outputs)
    assert len(op.inputs._connected_inputs)==3