# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
