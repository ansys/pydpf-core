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

from ansys.dpf.core import operators as ops
from ansys import dpf


def test_add_operator_server_field(local_server):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    # field+op
    forward = ops.utility.forward_field(field, server=local_server)
    add = field + forward
    assert isinstance(add, ops.math.add)
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array(field.data) * 2.0)

    # field + list
    add = field + [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.add)
    out = add.outputs.field()
    assert len(out) == 6
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, field.data + np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]))

    # field + float
    add = field + 1.0
    assert isinstance(add, ops.math.add)
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))


def test_minus_operator_server_field(local_server):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    # field-op
    forward = ops.utility.forward_field(field, server=local_server)
    add = field - forward
    assert isinstance(add, ops.math.minus)
    out = add.outputs.field()
    assert len(out) == 6
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.zeros((2, 3)))

    # fc - list
    add = field - [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.minus)
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([[0.0, 0.0, 0.0], [3.0, 3.0, 3.0]]))

    # operator - float
    add = field - 1.0
    assert isinstance(add, ops.math.minus)
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([[-1.0, 0.0, 1.0], [2.0, 3.0, 4.0]]))


def test_dot_operator_server_field(local_server):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    # field * op
    forward = ops.utility.forward_field(field, server=local_server)
    add = field * forward
    assert type(add) == ops.math.generalized_inner_product
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([5.0, 50.0]))

    # field * field
    add = field * field
    assert isinstance(add, ops.math.generalized_inner_product)
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([5.0, 50.0]))

    # field * list
    add = field * [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.generalized_inner_product)
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([5.0, 14.0]))

    # field * float
    add = field * -1.0
    assert isinstance(add, ops.math.generalized_inner_product)
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, -field.data)


def test_add_operator_server_fields_container(local_server):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    fc = dpf.core.fields_container_factory.over_time_freq_fields_container(
        [field, field], server=local_server
    )

    # operator with field out
    forward = ops.utility.forward_field(field, server=local_server)
    add = fc + forward
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)

    # fc + list
    add = fc + [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, field.data + np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]))

    # fc + float
    add = fc + 1.0
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))


def test_minus_operator_server_fields_container(local_server):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    fc = dpf.core.fields_container_factory.over_time_freq_fields_container(
        [field, field], server=local_server
    )

    # operator with field out
    forward = ops.utility.forward_field(field, server=local_server)
    add = fc - forward
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.zeros((2, 3)))

    # fc - list
    add = fc - [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[0.0, 0.0, 0.0], [3.0, 3.0, 3.0]]))

    # fc - float
    add = fc - 1.0
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[-1.0, 0.0, 1.0], [2.0, 3.0, 4.0]]))


def test_dot_operator_server_fields_container(local_server):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    fc = dpf.core.fields_container_factory.over_time_freq_fields_container(
        [field, field], server=local_server
    )

    # fc * op
    forward = ops.utility.forward_field(field, server=local_server)
    add = fc * forward
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # fc * field
    add = fc * field
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # fc * list
    add = fc * [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 14.0]))

    # fc * float
    add = fc * -1.0
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, -field.data)


def test_add_operator_server_fields_container(local_server):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    fc = dpf.core.fields_container_factory.over_time_freq_fields_container(
        [field, field], server=local_server
    )

    # operator with field out
    forward = ops.utility.forward_field(field, server=local_server)
    add = fc + forward
    assert type(add) == ops.math.add_fc
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)

    # fc + list
    add = fc + [0.0, 1.0, 2.0]
    assert type(add) == ops.math.add_fc
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, field.data + np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]))

    # fc + float
    add = fc + 1.0
    assert type(add) == ops.math.add_fc
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))


def test_minus_operator_server_fields_container(local_server):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    fc = dpf.core.fields_container_factory.over_time_freq_fields_container(
        [field, field], server=local_server
    )

    # operator with field out
    forward = ops.utility.forward_field(field, server=local_server)
    add = fc - forward
    assert type(add) == ops.math.minus_fc
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.zeros((2, 3)))

    # fc - list
    add = fc - [0.0, 1.0, 2.0]
    assert type(add) == ops.math.minus_fc
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[0.0, 0.0, 0.0], [3.0, 3.0, 3.0]]))

    # fc - float
    add = fc - 1.0
    assert type(add) == ops.math.minus_fc
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[-1.0, 0.0, 1.0], [2.0, 3.0, 4.0]]))


def test_dot_operator_server_fields_container(local_server):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    fc = dpf.core.fields_container_factory.over_time_freq_fields_container(
        [field, field], server=local_server
    )

    # fc * op
    forward = ops.utility.forward_field(field, server=local_server)
    add = fc * forward
    assert type(add) == ops.math.generalized_inner_product_fc
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # fc * field
    add = fc * field
    assert type(add) == ops.math.generalized_inner_product_fc
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # fc * list
    add = fc * [0.0, 1.0, 2.0]
    assert type(add) == ops.math.generalized_inner_product_fc
    out = add.outputs.fields_container()
    assert len(out) == 2
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 14.0]))

    # fc * float
    add = fc * -1.0
    assert type(add) == ops.math.generalized_inner_product_fc
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, -field.data)
