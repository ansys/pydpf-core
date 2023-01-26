import numpy as np

import conftest

from ansys import dpf
from ansys.dpf import core


@conftest.raises_for_servers_version_under("5.0")
def test_scopingdata_custom_type_field(server_type):
    pfield = core.CustomTypeField(np.uint64, server=server_type)
    list_ids = [1, 2, 4, 6, 7]
    scop = core.Scoping(ids=list_ids, location=core.locations.nodal, server=server_type)
    pfield.scoping = scop
    list_data = np.array([20, 30, 50, 70, 80], dtype=np.uint64)
    pfield.data = list_data
    pfield.data
    assert np.allclose(pfield.data, list_data)
    assert np.allclose(pfield.scoping.ids, list_ids)


@conftest.raises_for_servers_version_under("5.0")
def test_set_get_data_custom_type_field(server_type):
    field = dpf.core.CustomTypeField(np.byte, nentities=20, server=server_type)
    data = np.empty((20,), dtype=np.byte)
    for i in range(0, 20):
        data[i] = np.byte(b"2")
    field.data = data
    assert np.allclose(field.data, data)
    print(field.data)


@conftest.raises_for_servers_version_under("5.0")
def test_create_custom_type_field_push_back(server_type):
    f_vec = core.CustomTypeField(np.int16, server=server_type)
    f_vec.append([1, 2, 4], 1)
    assert len(f_vec.data) == 3
    assert f_vec.data[0] == 1
    assert f_vec.data[1] == 2
    assert f_vec.data[2] == 4
    assert f_vec.scoping.ids == [1]
    assert len(f_vec.scoping.ids) == 1

    f_scal = core.CustomTypeField(np.longlong, server=server_type)
    f_scal.append([2], 1)
    f_scal.append([5], 2)
    assert len(f_scal.data) == 2
    assert f_scal.data[0] == 2
    assert f_scal.data[1] == 5
    assert len(f_scal.scoping.ids) == 2
    assert f_scal.scoping.ids[0] == 1
    assert f_scal.scoping.ids[1] == 2


@conftest.raises_for_servers_version_under("5.0")
def test_set_get_data_pointer_custom_type_field(server_type):
    field = dpf.core.CustomTypeField(np.float, nentities=20, server=server_type)
    field_def = dpf.core.FieldDefinition(server=server_type)
    field_def.dimensionality = dpf.core.Dimensionality({3}, dpf.core.natures.vector)
    field.field_definition = field_def
    scop = dpf.core.Scoping(ids=[1, 2, 3, 4], location="faces", server=server_type)
    field.scoping = scop

    data = np.empty((24,), dtype=np.float)
    for i in range(0, 24):
        data[i] = i
    field.data = data
    field._data_pointer = [0, 6, 12, 18]
    assert np.allclose(field.data, np.array(data, dtype=float).reshape(8, 3))
    assert np.allclose(field._data_pointer, [0, 6, 12, 18])
    assert np.allclose(field.get_entity_data(0), np.array(range(0, 6)).reshape(2, 3))
    assert np.allclose(field.get_entity_data(1), np.array(range(6, 12)).reshape(2, 3))
    assert np.allclose(field.get_entity_data(2), np.array(range(12, 18)).reshape(2, 3))
    assert np.allclose(field.get_entity_data(3), np.array(range(18, 24)).reshape(2, 3))
    assert np.allclose(field.get_entity_data_by_id(1), np.array(range(0, 6)).reshape(2, 3))
    assert np.allclose(field.get_entity_data_by_id(2), np.array(range(6, 12)).reshape(2, 3))
    assert np.allclose(field.get_entity_data_by_id(3), np.array(range(12, 18)).reshape(2, 3))
    assert np.allclose(field.get_entity_data_by_id(4), np.array(range(18, 24)).reshape(2, 3))
    assert field.elementary_data_count == 8
    assert field.size == 24

    field.resize(5, 36)
    assert field.size == 36


@conftest.raises_for_servers_version_under("5.0")
def test_set_get_field_def_custom_type_field(server_type):
    field = dpf.core.CustomTypeField(np.float, nentities=20, server=server_type)
    field_def = dpf.core.FieldDefinition(server=server_type)
    field_def.dimensionality = dpf.core.Dimensionality([3], dpf.core.natures.vector)
    field_def.location = core.locations.elemental
    field_def.name = "thing"
    field_def.shell_layers = core.shell_layers.layerindependent
    field_def.unit = "m"
    field.field_definition = field_def

    copy = field.field_definition

    print(copy.dimensionality)
    assert copy.dimensionality == dpf.core.Dimensionality([3], dpf.core.natures.vector)
    assert copy.location == core.locations.elemental
    assert copy.name == "thing"
    assert copy.shell_layers == core.shell_layers.layerindependent
    assert field.location == core.locations.elemental
    field.location = core.locations.nodal
    assert field.location == core.locations.nodal
    assert field.component_count == 3
    assert field.unit == "m"
    field.unit = "mm"
    assert field.unit == "mm"
    assert field.dimensionality == dpf.core.Dimensionality([3], dpf.core.natures.vector)
    field.dimensionality = dpf.core.Dimensionality([1], dpf.core.natures.scalar)
    assert field.dimensionality == dpf.core.Dimensionality([1], dpf.core.natures.scalar)
    assert field.name == "thing"


@conftest.raises_for_servers_version_under("5.0")
def test_mutable_data_custom_type_field(server_clayer):
    field = dpf.core.CustomTypeField(np.float, nentities=20, server=server_clayer)
    field_def = dpf.core.FieldDefinition(server=server_clayer)
    field_def.dimensionality = dpf.core.Dimensionality({3}, dpf.core.natures.vector)
    field.field_definition = field_def
    scop = dpf.core.Scoping(ids=[1, 2, 3, 4], location="faces", server=server_clayer)
    field.scoping = scop

    data = np.empty((24,), dtype=np.float)
    for i in range(0, 24):
        data[i] = i
    field.data = data
    field._data_pointer = [0, 6, 12, 18]

    vec = field.get_entity_data(0)
    assert np.allclose(vec, np.array(range(0, 6)).reshape(2, 3))

    vec[0][0] = 1
    vec[1][2] = 4

    assert np.allclose(vec, np.array([1, 1, 2, 3, 4, 4]).reshape(2, 3))

    vec.commit()

    assert np.allclose(field.get_entity_data(0), np.array([1, 1, 2, 3, 4, 4]).reshape(2, 3))

    vec = field.get_entity_data_by_id(2)
    assert np.allclose(vec, np.array(range(6, 12)).reshape(2, 3))

    vec[0][0] = 1
    vec[1][2] = 4
    assert np.allclose(vec, np.array([1, 7, 8, 9, 10, 4]).reshape(2, 3))
    vec = None
    assert np.allclose(field.get_entity_data_by_id(2), np.array([1, 7, 8, 9, 10, 4]).reshape(2, 3))


@conftest.raises_for_servers_version_under("5.0")
def test_mutable_data_contiguous_custom_type_field(server_clayer):
    field = dpf.core.CustomTypeField(np.float, nentities=20, server=server_clayer)
    field_def = dpf.core.FieldDefinition(server=server_clayer)
    field_def.dimensionality = dpf.core.Dimensionality([6], dpf.core.natures.vector)
    field.field_definition = field_def
    scop = dpf.core.Scoping(ids=[1, 2, 3, 4], location="faces", server=server_clayer)
    field.scoping = scop

    data = np.empty((24,), dtype=np.float)
    for i in range(0, 24):
        data[i] = i
    field.data = data

    vec = field.get_entity_data(0)
    assert np.allclose(vec, np.array(range(0, 6)))

    vec[0][0] = 1
    vec[0][5] = 4

    assert np.allclose(vec, np.array([1, 1, 2, 3, 4, 4]))

    vec.commit()

    assert np.allclose(field.get_entity_data(0), np.array([1, 1, 2, 3, 4, 4]))

    vec = field.get_entity_data_by_id(2)
    assert np.allclose(vec, np.array(range(6, 12)))

    vec[0][0] = 1
    vec[0][5] = 4
    assert np.allclose(vec, np.array([1, 7, 8, 9, 10, 4]))
    vec = None
    assert np.allclose(field.get_entity_data_by_id(2), np.array([1, 7, 8, 9, 10, 4]))


# not using a fixture on purpose: the instance of simple field SHOULD be owned by each test
def get_float_field(server_clayer):
    field = dpf.core.CustomTypeField(np.float32, nentities=20, server=server_clayer)
    field = dpf.core.CustomTypeField(np.float, nentities=20, server=server_clayer)
    field_def = dpf.core.FieldDefinition(server=server_clayer)
    field_def.dimensionality = dpf.core.Dimensionality({3}, dpf.core.natures.vector)
    field.field_definition = field_def
    scop = dpf.core.Scoping(ids=[1, 2, 3, 4], location="faces", server=server_clayer)
    field.scoping = scop

    data = np.empty((24,), dtype=np.float)
    for i in range(0, 24):
        data[i] = i
    field.data = data
    field._data_pointer = [0, 6, 12, 18]
    return field


@conftest.raises_for_servers_version_under("5.0")
def test_mutable_data_pointer_custom_type_field(server_clayer):
    float_field = get_float_field(server_clayer)
    assert np.allclose(float_field.get_entity_data(0), np.array(range(0, 6)).reshape(2, 3))
    assert np.allclose(float_field.get_entity_data(1), np.array(range(6, 12)).reshape(2, 3))
    vec = float_field._data_pointer
    vec[1] = 9
    vec[2] = 15
    vec.commit()

    assert np.allclose(float_field.get_entity_data(0), np.array(range(0, 9)).reshape(3, 3))
    assert np.allclose(float_field.get_entity_data(1), np.array(range(9, 15)).reshape(2, 3))
    vec[1] = 6
    vec[2] = 12
    vec = None
    assert np.allclose(float_field.get_entity_data(0), np.array(range(0, 6)).reshape(2, 3))
    assert np.allclose(float_field.get_entity_data(1), np.array(range(6, 12)).reshape(2, 3))


@conftest.raises_for_servers_version_under("5.0")
def test_data_wrong_type_custom_type_field(server_type):
    pfield = core.CustomTypeField(np.uint64, server=server_type)
    list_ids = [1, 2, 4, 6, 7]
    scop = core.Scoping(ids=list_ids, location=core.locations.nodal, server=server_type)
    pfield.scoping = scop
    list_data = np.array([20, 30, 50, 70, 80], dtype=np.uint64)
    pfield.data = list_data
    assert np.allclose(pfield.data, list_data)

    list_data = np.array([20, 30, 50, 70, 80], dtype=np.int64)
    pfield.data = list_data
    assert np.allclose(pfield.data, list_data)


@conftest.raises_for_servers_version_under("5.0")
def test_data_wrong_type2_custom_type_field(server_type):
    pfield = core.CustomTypeField(np.int16, server=server_type)
    list_ids = [1, 2, 4, 6, 7]
    scop = core.Scoping(ids=list_ids, location=core.locations.nodal, server=server_type)
    pfield.scoping = scop
    list_data = np.array([20, 30, 50, 70, 80], dtype=np.uint64)
    pfield.data = list_data
    assert np.allclose(pfield.data, list_data)


@conftest.raises_for_servers_version_under("5.0")
def test_support_im_freq_custom_type_field(server_type):
    tfq = core.TimeFreqSupport(server=server_type)
    frequencies = core.fields_factory.create_scalar_field(3, server=server_type)
    frequencies.data = [0.1, 0.32, 0.4]
    tfq.time_frequencies = frequencies

    pfield = core.CustomTypeField(np.int16, server=server_type)
    pfield.support = tfq

    assert np.allclose(
        pfield.support.field_support_by_property("time_freqs").data, [0.1, 0.32, 0.4]
    )


@conftest.raises_for_servers_version_under("5.0")
def test_large_data_custom_type_field(server_type):
    size = 1000001
    pfield = core.CustomTypeField(np.uint64, server=server_type)
    list_ids = range(1, size + 1)
    scop = core.Scoping(ids=list_ids, location=core.locations.nodal, server=server_type)
    pfield.scoping = scop
    list_data = np.array(list(range(1, size + 1)), dtype=np.uint64)
    pfield.data = list_data
    pfield.data
    assert np.allclose(pfield.data, list_data)
    assert np.allclose(pfield.scoping.ids, list_ids)


@conftest.raises_for_servers_version_under("5.0")
def test_data_as_list_custom_type_field(server_type):
    pfield = core.CustomTypeField(np.uint64, server=server_type)
    list_ids = [1, 2, 4, 6, 7]
    scop = core.Scoping(ids=list_ids, location=core.locations.nodal, server=server_type)
    pfield.scoping = scop
    pfield.data = [20, 30, 50, 70, 80]
    pfield.append([90], 8)
    assert np.allclose(pfield.data, [20, 30, 50, 70, 80, 90])


@conftest.raises_for_servers_version_under("5.0")
def test_check_types_custom_type_field(server_type):
    pfield = core.CustomTypeField(np.uint64, server=server_type)
    pfield2 = core.CustomTypeField(np.int16, server=server_type)
    pfield3 = core.CustomTypeField(np.float32, server=server_type)
    pfield4 = core.CustomTypeField(np.float64, server=server_type)
    pfield5 = core.CustomTypeField(np.int8, server=server_type)

    forward = dpf.core.operators.utility.forward(server=server_type)
    forward.connect(0, pfield)
    forward.connect(1, pfield2)
    forward.connect(2, pfield3)
    forward.connect(3, pfield4)
    forward.connect(4, pfield5)

    pfieldout = forward.get_output(0, core.types.custom_type_field)
    assert pfieldout.type == np.uint64
    assert pfieldout.is_of_type(np.uint64)
    assert not pfieldout.is_of_type(np.short)
    pfieldout = forward.get_output(1, core.types.custom_type_field)
    assert pfieldout.type == np.int16
    assert pfieldout.is_of_type(np.int16)
    assert pfieldout.is_of_type(np.short)
    assert not pfieldout.is_of_type(np.uint64)
    pfieldout = forward.get_output(2, core.types.custom_type_field)
    assert pfieldout.type == np.float32
    assert pfieldout.is_of_type(np.float32)
    pfieldout = forward.get_output(3, core.types.custom_type_field)
    assert pfieldout.type == np.float64
    assert pfieldout.is_of_type(np.float64)
    assert pfieldout.is_of_type(np.double)
    assert not pfieldout.is_of_type(np.short)
    pfieldout = forward.get_output(4, core.types.custom_type_field)
    assert pfieldout.type == np.byte
    assert pfieldout.is_of_type(np.int8)
    assert not pfieldout.is_of_type(np.short)
