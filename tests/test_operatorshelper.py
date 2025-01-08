# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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

import numpy as np

from ansys import dpf


def test_add_method():
    data = np.array([1, 2, 3])
    field_a = dpf.core.field_from_array(data)
    field_b = dpf.core.field_from_array(data)
    fout = dpf.core.help.add(field_a, field_b)
    assert np.allclose(fout.data, data * 2)


def test_add_builtin():
    data = np.array([1, 2, 3])
    field_a = dpf.core.field_from_array(data)
    field_b = dpf.core.field_from_array(data)
    fout = field_a + field_b
    assert np.allclose(fout.outputs.field().data, np.array(data) * 2)


def test_element_dot():
    data = np.random.random((10, 3))
    field_a = dpf.core.field_from_array(data)
    field_b = dpf.core.field_from_array(data)
    fout = dpf.core.help.element_dot(field_a, field_b)
    assert np.allclose(fout.data, np.sum(data * data, 1))


def test_sqr():
    data = np.array([1, 2, 3])
    field = dpf.core.field_from_array(data)
    field_sqr = dpf.core.help.sqr(field)
    assert np.allclose(field_sqr.data, data**2)


def test_sqr_builtin():
    data = np.array([1, 2, 3])
    field = dpf.core.field_from_array(data)
    field_sqr = field**2
    assert np.allclose(field_sqr.outputs.field().data, data**2)


def test_dot_tensor():
    arr_a = np.ones((5, 3))
    arr_a[:, 2] = 0
    arr_b = np.ones((5, 3))
    arr_b[:, 1] = 0
    field_a = dpf.core.field_from_array(arr_a)
    field_b = dpf.core.field_from_array(arr_b)
    fout = dpf.core.help.dot_tensor(field_a, field_b)
    arr_out = fout.data
    assert np.all(arr_out[:, [0, 1, 6, 7]] == 1)


def test_nodal_averaging(simple_bar):
    model = dpf.core.Model(simple_bar)
    evol = model.results.element_nodal_forces()
    field = evol.outputs.fields_container()[0]
    nodal_evol = field.to_nodal()
    assert nodal_evol.location == dpf.core.locations.nodal


def test_ellispsis_pin(simple_bar, tmpdir):
    tmp_path = str(tmpdir.join("vtk.vtk"))
    model = dpf.core.Model(simple_bar)
    u = model.operator("U")
    s = model.operator("S")
    op = dpf.core.Operator("vtk_export")
    op.inputs.connect(tmp_path)
    op.inputs.fields1(s.outputs)
    op.inputs.fields2(u.outputs)
    assert len(op.inputs._connected_inputs) == 3
