from ansys.dpf import core


# try:
#     core.BaseService(load_operators=False)._load_hdf5_operators()
#     hdf5_loaded = True
# except OSError:
#     hdf5_loaded = False

# skip_no_hdf5 = pytest.mark.skipif(not hdf5_loaded, reason='Requires HDF5 operators')


# @skip_no_hdf5
def test_hdf5_loaded():
    op = core.Operator("serialize_to_hdf5")
    assert op.inputs is not None


# @skip_no_hdf5
def test_hdf5_ellipsis_any_pins(simple_bar, tmpdir):
    tmp_path = str(tmpdir.join("hdf5.h5"))
    model = core.Model(simple_bar)
    u = model.results.displacement()
    s = model.operator("S")
    op = core.Operator("serialize_to_hdf5")
    op.inputs.file_path.connect(tmp_path)
    op.inputs.data1.connect(u.outputs)
    op.inputs.data2.connect(s.outputs)
    assert len(op.inputs._connected_inputs) == 3
