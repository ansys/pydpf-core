import pytest
from ansys import dpf


try:
    dpf.core.BaseService()._load_hdf5()
    hdf5_loaded = True
except OSError:
    hdf5_loaded = False

skip_no_hdf5 = pytest.mark.skipif(not hdf5_loaded, reason='Requires HDF5 operators')


@skip_no_hdf5
def test_hdf5_loaded():
    op = dpf.core.Operator("serialize_to_hdf5")
    assert op.inputs is not None


@skip_no_hdf5
@pytest.mark.xfail(reason='op.inputs has no member "data"')
def test_hdf5_ellipsis_any_pins(simple_bar, tmpdir):
    tmp_path = str(tmpdir.join('hdf5.h5'))
    model = dpf.core.Model(simple_bar)
    u = model.operator("U")
    s = model.operator("S")
    op = dpf.core.Operator("serialize_to_hdf5")
    op.inputs.file_path.connect(tmp_path)
    op.inputs.data(u.outputs)
    op.inputs.data(s.outputs)
    assert len(op.inputs._connected_inputs) == 3
