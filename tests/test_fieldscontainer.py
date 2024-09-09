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

import weakref

import numpy as np
import pytest
import os

import conftest
from ansys.dpf.core.check_version import server_meet_version
from ansys.dpf import core as dpf
from ansys.dpf.core import FieldsContainer, Field, TimeFreqSupport
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core import examples
from ansys.dpf.core import fields_factory
from ansys.dpf.core import operators as ops
from ansys.dpf.core.custom_fields_container import (
    ElShapeFieldsContainer,
    BodyFieldsContainer,
)


@pytest.fixture()
def disp_fc(allkindofcomplexity):
    """Return a displacement fields container"""
    model = dpf.Model(allkindofcomplexity)
    return model.results.displacement().outputs.fields_container()


def test_create_fields_container(server_type):
    fc = FieldsContainer(server=server_type)
    assert fc._internal_obj is not None


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0,
    reason="Renaming collections is supported via gRPC starting server version 8.0",
)
def test_rename_fields_container(server_type):
    fc = FieldsContainer(server=server_type)
    assert fc.name is None
    fc.name = "test"
    assert fc.name == "test"


def test_empty_index(server_type):
    fc = FieldsContainer(server=server_type)
    with pytest.raises(IndexError):
        fc[0]


def test_createby_message_copy_fields_container(server_type_legacy_grpc):
    fc = FieldsContainer(server=server_type_legacy_grpc)
    fields_container2 = FieldsContainer(
        fields_container=fc._internal_obj, server=server_type_legacy_grpc
    )
    assert fc._internal_obj == fields_container2._internal_obj


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Copying data is supported starting server version 3.0",
)
def test_createbycopy_fields_container(server_type):
    fc = FieldsContainer(server=server_type)
    fields_container2 = FieldsContainer(fields_container=fc)
    assert fc._internal_obj != fields_container2._internal_obj


def test_set_get_field_fields_container(server_type):
    fc = FieldsContainer(server=server_type)
    fc.labels = ["time", "complex"]
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0}
        fc.add_field(mscop, Field(nentities=i + 10, server=server_type))
    assert fc.get_available_ids_for_label() == list(range(1, 21))
    for i in range(0, 20):
        fieldid = fc.get_field({"time": i + 1, "complex": 0})._internal_obj
        assert fieldid != None
        assert fc.get_field(i)._internal_obj != None
        assert fc.get_field_by_time_complex_ids(timeid=i + 1, complexid=0)._internal_obj != None
        assert fc[i]._internal_obj != None


def test_get_label_scoping(server_type):
    fc = FieldsContainer(server=server_type)
    fc.labels = ["time", "complex"]
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0}
        fc.add_field(mscop, Field(nentities=i + 10, server=server_type))
    scop = fc.get_label_scoping()
    assert scop._internal_obj is not None
    assert np.allclose(scop.ids, list(range(1, 21)))


def test_set_get_field_fields_container_new_label(server_type):
    fc = FieldsContainer(server=server_type)
    fc.labels = ["time", "complex"]
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0}
        fc.add_field(mscop, Field(nentities=i + 10, server=server_type))
    assert fc.get_available_ids_for_label() == list(range(1, 21))
    for i in range(0, 20):
        assert fc.get_field({"time": i + 1, "complex": 0})._internal_obj != None
        assert fc.get_field(i)._internal_obj != None
        assert fc.get_field_by_time_complex_ids(timeid=i + 1, complexid=0)._internal_obj != None
        assert fc[i]._internal_obj != None
        assert fc.get_label_space(i) == {"time": i + 1, "complex": 0}
    fc.add_label("shape")
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0, "shape": 1}
        fc.add_field(mscop, Field(nentities=i + 10, server=server_type))

    assert len(fc.get_fields({"time": i + 1, "complex": 0})) == 2

    for i in range(0, 20):
        fieldid = fc.get_field({"time": i + 1, "complex": 0, "shape": 1})._internal_obj != None
        assert fieldid != 0
        assert fc.get_field(i + 20)._internal_obj != None
        assert fc[i]._internal_obj != None
        assert fc.get_label_space(i + 20) == {"time": i + 1, "complex": 0, "shape": 1}


def test_set_get_field_fields_container_new_label_default_value(server_type):
    fc = FieldsContainer(server=server_type)
    fc.labels = ["time", "complex"]
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0}
        fc.add_field(mscop, Field(nentities=i + 10, server=server_type))
    fc.add_label("shape", 3)
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0, "shape": 1}
        fc.add_field(mscop, Field(nentities=i + 10, server=server_type))
    for i in range(0, 20):
        fieldid = fc.get_field({"time": i + 1, "complex": 0, "shape": 1})._internal_obj
        assert fieldid != None
        assert fc.get_field(i + 20)._internal_obj != None
        assert fc[i]._internal_obj != None
        assert fc.get_label_space(i + 20) == {"time": i + 1, "complex": 0, "shape": 1}
    for i in range(0, 20):
        fieldid = fc.get_field({"time": i + 1, "complex": 0, "shape": 3})._internal_obj
        assert fieldid != None
        assert fc.get_field(i)._internal_obj != None
        assert fc[i]._internal_obj != None
        assert fc.get_label_space(i) == {"time": i + 1, "complex": 0, "shape": 3}


def test_get_item_field_fields_container(server_type):
    fc = FieldsContainer(server=server_type)
    fc.labels = ["time", "complex"]
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0}
        fc.add_field(mscop, Field(nentities=i + 10, server=server_type))
    for i in range(0, 20):
        assert fc[i]._internal_obj != None


def test_delete_fields_container(server_type):
    fc = FieldsContainer(server=server_type)
    ref = weakref.ref(fc)
    fc = None
    import gc

    gc.collect()
    assert ref() is None


def test_str_fields_container(disp_fc):
    assert "time" in str(disp_fc)
    assert "location" in str(disp_fc)


def test_support_fields_container(disp_fc):
    support = disp_fc.time_freq_support
    assert len(support.time_frequencies) == 1


def test_getitem_fields_container(disp_fc):
    assert isinstance(disp_fc[0], dpf.Field)


def test_has_label(disp_fc):
    fc = FieldsContainer()
    fc.labels = ["time", "complex"]
    assert fc.has_label("time") == True
    assert fc.has_label("complex") == True
    assert fc.has_label("body") == False

    assert disp_fc.has_label("time") == True
    assert fc.has_label("body") == False


def test_add_field_by_time_id(server_type):
    fc = FieldsContainer(server=server_type)
    fc.labels = ["time", "complex"]
    f1 = Field(3, server=server_type)
    f1.append([10.2, 3.0, -11.8], 1)
    f1.data
    f1.append([10.2, 2.0, 11.8], 2)
    f1.append([10.2, 1.0, -11.8], 3)
    mscop1 = {"time": 1, "complex": 0}
    fc.add_field(mscop1, f1)
    assert len(fc) == 1
    f2 = Field(1, server=server_type)
    f2.append([4.0, 4.4, 3.6], 1)
    mscop2 = {"time": 1, "complex": 1}
    fc.add_field(mscop2, f2)
    assert len(fc) == 2
    f3 = Field(1, server=server_type)
    f3.append([0.0, 0.4, 0.6], 1)
    fc.add_field_by_time_id(f3, 2)
    field_to_compare = Field(1)
    field_to_compare.append([0.0, 0.4, 0.6], 1)
    field = fc.get_field({"time": 2, "complex": 0})
    assert len(fc) == 3
    assert np.allclose(field.data, field_to_compare.data)

    fc.add_field_by_time_id(f3, 1)
    field_result_1 = fc.get_field({"time": 1, "complex": 0})
    field_result_2 = fc.get_field({"time": 2, "complex": 0})
    assert np.allclose(field_result_1.data, field_result_2.data)

    fc.add_label("body")
    with pytest.raises(dpf_errors.DpfValueError):
        fc.add_field_by_time_id(f3, 10)


def test_add_imaginary_field(server_type):
    fc = FieldsContainer(server=server_type)
    fc.labels = ["time", "complex"]
    f1 = Field(3, server=server_type)
    f1.append([10.2, 3.0, -11.8], 1)
    f1.append([10.2, 2.0, 11.8], 2)
    f1.append([10.2, 1.0, -11.8], 3)
    mscop1 = {"time": 1, "complex": 1}
    fc.add_field(mscop1, f1)
    assert len(fc) == 1
    f2 = Field(1, server=server_type)
    f2.append([4.0, 4.4, 3.6], 1)
    mscop2 = {"time": 1, "complex": 0}
    fc.add_field(mscop2, f2)
    assert len(fc) == 2
    f3 = Field(1, server=server_type)
    f3.append([0.0, 0.4, 0.6], 1)
    fc.add_imaginary_field(f3, 2)
    field_to_compare = Field(1)
    field_to_compare.append([0.0, 0.4, 0.6], 1)
    field = fc.get_field({"time": 2, "complex": 1})
    assert len(fc) == 3
    assert np.allclose(field.data, field_to_compare.data)

    fc.add_imaginary_field(f3, 1)
    field_result_1 = fc.get_field({"time": 1, "complex": 1})
    field_result_2 = fc.get_field({"time": 2, "complex": 1})
    assert np.allclose(field_result_1.data, field_result_2.data)

    fc.add_label("body")
    with pytest.raises(dpf_errors.DpfValueError):
        fc.add_imaginary_field(f3, 10)


def test_get_imaginary_field(disp_fc):
    with pytest.raises(dpf_errors.DpfValueError):
        disp_fc.get_imaginary_fields(1)
    fc = FieldsContainer()
    fc.labels = ["complex"]
    with pytest.raises(dpf_errors.DpfValueError):
        fc.get_imaginary_fields(1)
    fc = FieldsContainer()
    fc.labels = ["time", "complex"]
    field_real = Field(1)
    field_real.append([0.0, 3.0, 4.1], 20)
    fc.add_field({"time": 1, "complex": 0}, field_real)
    field_to_check = fc.get_imaginary_field(1)
    assert field_to_check is None
    field_img = Field(1)
    field_img.append([1.0, 301.2, 4.2], 20)
    fc.add_field({"time": 1, "complex": 1}, field_img)
    field_to_check_2 = fc.get_imaginary_field(1)
    assert np.allclose(field_img.data, field_to_check_2.data)


def test_get_field_by_time_id(server_type):
    fc = FieldsContainer(server=server_type)
    fc.labels = ["complex"]
    with pytest.raises(dpf_errors.DpfValueError):
        fc.get_field_by_time_id(1)
    fc = FieldsContainer(server=server_type)
    fc.labels = ["time", "complex"]
    field_img = Field(1, server=server_type)
    field_img.append([0.0, 3.0, 4.1], 20)
    fc.add_field({"time": 1, "complex": 1}, field_img)
    field_to_check = fc.get_field_by_time_id(1)
    assert field_to_check is None
    field_real = Field(1, server=server_type)
    field_real.append([1.0, 301.2, 4.2], 20)
    fc.add_field({"time": 1, "complex": 0}, field_real)
    field_to_check_2 = fc.get_field_by_time_id(1)
    assert np.allclose(field_real.data, field_to_check_2.data)

    fc2 = FieldsContainer(server=server_type)
    fc2.labels = ["time"]
    f1 = Field(1, server=server_type)
    f1.append([0.0, 3.0, 4.1], 20)
    fc.add_field({"time": 1, "complex": 0}, f1)
    field_to_check = fc.get_field_by_time_id(1)
    assert np.allclose(f1.data, field_to_check.data)


def test_collection_update_support():
    # set time_freq_support
    fc = FieldsContainer()
    tfq = TimeFreqSupport()
    frequencies = fields_factory.create_scalar_field(3)
    frequencies.data = [0.1, 0.32, 0.4]
    tfq.time_frequencies = frequencies
    fc.time_freq_support = tfq
    # get time_freq_support
    tfq_check = fc.time_freq_support
    assert np.allclose(tfq.time_frequencies.data, tfq_check.time_frequencies.data)


@pytest.mark.skipif(os.name == "posix", reason="linux issue: SEGFAULT to investigate")
def test_deep_copy_over_time_fields_container(velocity_acceleration):
    model = dpf.Model(velocity_acceleration)
    stress = model.results.stress(time_scoping=[1, 2, 3])
    fc = stress.outputs.fields_container()
    copy = fc.deep_copy()

    idenfc = dpf.operators.logic.identical_fc(fc, copy)
    assert idenfc.outputs.boolean()

    tf = fc.time_freq_support
    copy = copy.time_freq_support
    assert np.allclose(tf.time_frequencies.data, copy.time_frequencies.data)
    assert tf.time_frequencies.scoping.ids == copy.time_frequencies.scoping.ids


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Bug in server version lower than 3.0",
)
def test_light_copy(server_type):
    fc = FieldsContainer(server=server_type)
    fc.labels = ["time"]
    field = Field(1, server=server_type)
    field.append([0.0, 3.0, 4.1], 20)
    fc.add_field({"time": 1}, field)
    assert fc[0] != None
    fc2 = FieldsContainer(fields_container=fc)
    assert fc2[0] != None
    fc = 2
    assert fc2[0] != None


@pytest.mark.slow
def test_el_shape_fc(allkindofcomplexity):
    model = dpf.Model(allkindofcomplexity)
    fc = model.results.stress.split_by_shape.eval()
    assert isinstance(fc, ElShapeFieldsContainer)
    assert len(fc.beam_fields()) == 1
    assert len(fc.shell_fields()) == 1
    assert len(fc.solid_fields()) == 1
    mesh = model.metadata.meshed_region

    f = fc.beam_field()
    ids = f.scoping.ids[0 : int(len(f.scoping) / 4)]
    for id in ids:
        assert mesh.elements.element_by_id(id).shape == "beam"

    f = fc.shell_field()
    ids = f.scoping.ids[0 : int(len(f.scoping) / 10)]
    for id in ids:
        assert mesh.elements.element_by_id(id).shape == "shell"

    f = fc.solid_field()
    ids = f.scoping.ids[0 : int(len(f.scoping) / 10)]
    for id in ids:
        assert mesh.elements.element_by_id(id).shape == "solid"


def test_el_shape_time_fc():
    model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
    fc = model.results.stress.on_all_time_freqs.split_by_shape.eval()
    assert isinstance(fc, ElShapeFieldsContainer)
    assert len(fc.beam_fields()) == 45
    assert len(fc.shell_fields()) == 45
    assert len(fc.solid_fields()) == 45
    assert len(fc.beam_fields(1)) == 1
    assert len(fc.shell_fields(3)) == 1
    assert len(fc.solid_fields(20)) == 1
    mesh = model.metadata.meshed_region

    f = fc.beam_field(3)
    for id in f.scoping.ids[0 : int(len(f.scoping.ids) / 3)]:
        assert mesh.elements.element_by_id(id).shape == "beam"

    f = fc.shell_field(4)
    for id in f.scoping.ids[0 : int(len(f.scoping.ids) / 10)]:
        assert mesh.elements.element_by_id(id).shape == "shell"

    f = fc.solid_field(5)
    for id in f.scoping.ids[0 : int(len(f.scoping.ids) / 10)]:
        assert mesh.elements.element_by_id(id).shape == "solid"


def test_mat_time_fc():
    model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
    fc = model.results.stress.on_all_time_freqs.split_by_body.eval()
    assert isinstance(fc, BodyFieldsContainer)
    assert len(fc.get_fields_by_mat_id(45)) == 45
    assert np.allclose(fc.get_fields_by_mat_id(45)[0].data, fc.get_field_by_mat_id(45, 1).data)
    if server_meet_version("9.0", model._server):
        assert len(fc.get_mat_scoping().ids) == 44
    else:
        assert len(fc.get_mat_scoping().ids) == 32


def test_add_operator_fields_container():
    field = dpf.fields_factory.create_3d_vector_field(2)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    fc = dpf.fields_container_factory.over_time_freq_fields_container([field, field])

    # operator with field out
    forward = ops.utility.forward_field(field)
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


def test_minus_operator_fields_container():
    field = dpf.fields_factory.create_3d_vector_field(2)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    fc = dpf.fields_container_factory.over_time_freq_fields_container([field, field])

    # operator with field out
    forward = ops.utility.forward_field(field)
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


def test_dot_operator_fields_container():
    field = dpf.fields_factory.create_3d_vector_field(2)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    fc = dpf.fields_container_factory.over_time_freq_fields_container([field, field])

    # fc * op
    forward = ops.utility.forward_field(field)
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


def test_fields_container_factory_with_dict():
    field1 = dpf.Field()
    field1.data = [1, 2, 3]
    field2 = dpf.Field()
    field2.data = [2, 3, 4]
    fields_container = dpf.fields_container_factory.over_time_freq_fields_container(
        fields={0.1: field1, 0.2: field2}
    )

    assert fields_container[0].unit == ""


def test_fields_container_get_time_scoping(server_type, disp_fc):
    freq_scoping = disp_fc.get_time_scoping()
    assert freq_scoping.size == 1


@conftest.raises_for_servers_version_under("5.0")
def test_fields_container_set_tfsupport(server_type):
    coll = dpf.FieldsContainer(server=server_type)
    coll.labels = ["body", "time"]
    tfq = TimeFreqSupport(server=server_type)
    frequencies = fields_factory.create_scalar_field(3, server=server_type)
    frequencies.append([1.0], 1)
    tfq.time_frequencies = frequencies

    gen_support = dpf.GenericSupport(name="body", server=server_type)
    str_f = dpf.StringField(server=server_type)
    str_f.append(["inlet"], 1)
    gen_support.set_support_of_property("name", str_f)

    coll.set_support("time", tfq)
    coll.set_support("body", gen_support)

    assert coll.get_support("time").available_field_supported_properties() == ["time_freqs"]
    assert coll.get_support("body").available_string_field_supported_properties() == ["name"]
    assert coll.get_support("body").string_field_support_by_property("name").data == ["inlet"]


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_fields_container_empty_tf_support(server_type):
    fields_container = dpf.FieldsContainer(server=server_type)

    assert fields_container.time_freq_support == None


@conftest.raises_for_servers_version_under("9.0")
def test_get_entries_indices_fields_container(server_type):
    fc = FieldsContainer(server=server_type)
    fc.labels = ["time", "complex"]
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0}
        fc.add_field(mscop, Field(nentities=i + 10, server=server_type))
    assert np.allclose(fc.get_entries_indices({"time": 1, "complex": 0}), [0])
    assert np.allclose(fc.get_entries_indices({"time": 2}), [1])
    assert np.allclose(fc.get_entries_indices({"complex": 0}), range(0, 20))
