import numpy as np
import pytest
import copy
import conftest
import gc

from ansys import dpf
from ansys.dpf import core
from ansys.dpf.core.common import locations, natures


@pytest.fixture()
def property_field(simple_bar):
    """Return a property field from the simple bar model"""
    model = dpf.core.Model(simple_bar)
    mesh = model.metadata.meshed_region
    op = dpf.core.Operator("meshed_skin_sector")
    op.inputs.mesh.connect(mesh)
    property_field = op.outputs.property_field_new_elements_to_old()
    return property_field


def test_scopingdata_property_field(server_type):
    pfield = dpf.core.PropertyField(server=server_type)
    list_ids = [1, 2, 4, 6, 7]
    scop = core.Scoping(ids=list_ids, location=locations.nodal, server=server_type)
    pfield.scoping = scop
    list_data = [20, 30, 50, 70, 80]
    pfield.data = list_data
    pfield.data
    assert np.allclose(pfield.data, list_data)
    assert np.allclose(pfield.scoping.ids, list_ids)


def test_set_get_data_property_field(server_type):
    field = dpf.core.PropertyField(nentities=20, nature=natures.scalar, server=server_type)
    data = []
    for i in range(0, 20):
        data.append(i)
    field.data = data
    assert np.allclose(field.data, data)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_1,
    reason="Available starting with DPF 8.1",
)
def test_set_get_name_property_field(server_type):
    field = dpf.core.PropertyField(server=server_type)
    field.name = "test"
    assert field.name == "test"


def test_create_property_field_push_back(server_type):
    f_vec = core.PropertyField(1, core.natures.vector, core.locations.nodal, server=server_type)
    f_vec.append([1, 2, 4], 1)
    assert len(f_vec.data) == 3
    assert f_vec.data[0] == 1
    assert f_vec.data[1] == 2
    assert f_vec.data[2] == 4
    assert f_vec.scoping.ids == [1]
    assert len(f_vec.scoping.ids) == 1

    f_scal = core.PropertyField(1, core.natures.scalar, core.locations.nodal, server=server_type)
    f_scal.append([2], 1)
    f_scal.append([5], 2)
    assert len(f_scal.data) == 2
    assert f_scal.data[0] == 2
    assert f_scal.data[1] == 5
    assert len(f_scal.scoping.ids) == 2
    assert f_scal.scoping.ids[0] == 1
    assert f_scal.scoping.ids[1] == 2


def check_on_property_field_from_simplebar(prop_field):
    assert prop_field is not None
    assert len(prop_field.data) != 0
    assert isinstance(prop_field, core.field_base._FieldBase)
    assert isinstance(prop_field, core.PropertyField)
    assert prop_field.component_count == 1
    assert prop_field.data is not None
    assert len(prop_field.data) != 0
    assert len(prop_field.data) == 1400
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_1:
        assert prop_field.data[15] == 1502
        assert np.allclose(prop_field.data[12], 1603)
        assert prop_field.data[1201] == 1980
        assert prop_field.get_entity_data(8) == [1605]
        assert prop_field.get_entity_data_by_id(23) == [1707]
    else:
        assert prop_field.data[15] == 29
        assert np.allclose(prop_field.data[12], 10)
        assert prop_field.data[1201] == 2500
        assert prop_field.get_entity_data(8) == [7]
        assert prop_field.get_entity_data_by_id(23) == [60]
    assert prop_field.elementary_data_count == 1400
    assert prop_field.elementary_data_shape == 1
    assert prop_field.location == locations.elemental
    assert prop_field.location == prop_field.scoping.location
    assert prop_field.size == 1400
    assert np.allclose(prop_field.scoping.ids[201], 202)


def test_getoutput_property_field_operator(property_field):
    check_on_property_field_from_simplebar(property_field)


def test_set_location(property_field):
    assert property_field.location == locations.elemental
    property_field.location = locations.nodal
    assert property_field.location == locations.nodal


def test_set_prop_field_from_message(simple_bar, server_type_legacy_grpc):
    model = dpf.core.Model(simple_bar, server=server_type_legacy_grpc)
    mesh = model.metadata.meshed_region
    op = dpf.core.Operator("meshed_skin_sector", server=server_type_legacy_grpc)
    op.inputs.mesh.connect(mesh)
    property_field = op.outputs.property_field_new_elements_to_old()
    prop_field_message = property_field._internal_obj
    new_prop_field = dpf.core.PropertyField(
        property_field=prop_field_message, server=server_type_legacy_grpc
    )
    assert isinstance(new_prop_field, dpf.core.PropertyField)
    check_on_property_field_from_simplebar(new_prop_field)


def test_set_prop_field_from_prop_field(property_field):
    new_prop_field = dpf.core.PropertyField(property_field=property_field)
    assert isinstance(new_prop_field, dpf.core.PropertyField)
    check_on_property_field_from_simplebar(new_prop_field)


def test_connect_property_field_operator(server_type):
    f_vec = dpf.core.PropertyField(1, natures.vector, locations.nodal, server=server_type)
    f_vec.append([1, 2, 4], 1)
    op = dpf.core.operators.utility.forward(server=server_type)
    op.inputs.connect(f_vec)
    out = op.get_output(0, core.types.property_field)
    assert out is not None
    assert np.allclose(out.data, [1, 2, 4])
    assert np.allclose(out.scoping.ids, [1])


def test_getoutput_property_field_workflow(simple_bar):
    model = dpf.core.Model(simple_bar)
    mesh = model.metadata.meshed_region
    op = dpf.core.Operator("meshed_skin_sector")
    op.inputs.mesh.connect(mesh)

    wf = dpf.core.Workflow()
    wf.progress_bar = False
    wf.add_operator(op)
    wf.set_output_name("field_out", op, 3)

    property_field = wf.get_output("field_out", dpf.core.types.property_field)
    check_on_property_field_from_simplebar(property_field)


def test_connect_property_field_workflow():
    f_vec = dpf.core.PropertyField(1, natures.vector, locations.nodal)
    f_vec.append([1, 2, 4], 1)
    op = dpf.core.operators.utility.forward()

    wf = dpf.core.Workflow()
    wf.progress_bar = False
    wf.add_operator(op)
    wf.set_input_name("field_in", op, 0)
    wf.connect("field_in", f_vec)
    wf.set_output_name("field_out", op, 0)

    out = wf.get_output("field_out", core.types.property_field)
    assert out is not None
    assert np.allclose(out.data, [1, 2, 4])
    assert np.allclose(out.scoping.ids, [1])


def test_local_property_field():
    num_entities = 100
    field_to_local = dpf.core.PropertyField(num_entities, dpf.core.natures.scalar, locations.nodal)
    data = []
    data_pointer = []
    scoping_ids = []
    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            current_data = range(i, i + 3)
            current_data = list(current_data)
            data_pointer.append(3 * (i - 1))
            scoping_ids.append(i)
            data.extend(current_data)
            f.append(np.array(current_data), i)
            assert np.allclose(f.get_entity_data(i - 1), current_data)
            assert np.allclose(f.get_entity_data_by_id(i), current_data)

    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            assert np.allclose(f.get_entity_data(i - 1), range(i, i + 3))
            assert np.allclose(f.get_entity_data_by_id(i), list(range(i, i + 3)))

    assert np.allclose(field_to_local.data, data)
    assert np.allclose(field_to_local.scoping.ids, scoping_ids)
    assert np.allclose(field_to_local._data_pointer, data_pointer[0 : len(data_pointer)])

    with field_to_local.as_local_field() as f:
        assert np.allclose(f.data, data)
        assert np.allclose(f._data_pointer, data_pointer[0 : len(data_pointer)])


@conftest.raises_for_servers_version_under("4.0")
def test_mutable_data_property_field(server_clayer, simple_bar):
    model = dpf.core.Model(simple_bar, server=server_clayer)
    mesh = model.metadata.meshed_region
    op = dpf.core.Operator("meshed_skin_sector", server=server_clayer)
    op.inputs.mesh.connect(mesh)

    wf = dpf.core.Workflow(server=server_clayer)
    wf.progress_bar = False
    wf.add_operator(op)
    wf.set_output_name("field_out", op, 3)

    property_field = wf.get_output("field_out", dpf.core.types.property_field)
    data = property_field.data
    data_copy = copy.deepcopy(data)
    data[0] += 1
    data.commit()
    changed_data = property_field.data
    assert np.allclose(changed_data, data)
    assert not np.allclose(changed_data, data_copy)
    assert np.allclose(changed_data[0], data_copy[0] + 1)
    data[0] += 1
    data = None
    changed_data = property_field.data
    assert np.allclose(changed_data[0], data_copy[0] + 2)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="change in memory ownership in server 5.0",
)
def test_mutable_data_delete_property_field(server_clayer, simple_bar):
    model = dpf.core.Model(simple_bar, server=server_clayer)
    mesh = model.metadata.meshed_region
    op = dpf.core.Operator("meshed_skin_sector", server=server_clayer)
    op.inputs.mesh.connect(mesh)
    property_field = op.get_output(3, dpf.core.types.property_field)
    data = property_field.data
    data_copy = copy.deepcopy(data)
    changed_data = property_field.data
    property_field = None
    gc.collect()  # check that the memory is held by the dpfvector
    assert np.allclose(changed_data, data_copy)
    changed_data[0] = 1
    assert np.allclose(changed_data[0], 1)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="Copying data is " "supported starting server version 5.0",
)
def test_print_property_field(server_type):
    pfield = dpf.core.PropertyField(server=server_type)
    assert "Property Field" in str(pfield)
    list_ids = [1, 2, 4, 6, 7]
    scop = core.Scoping(ids=list_ids, location=locations.nodal, server=server_type)
    pfield.scoping = scop
    pfield.data = [1, 2, 4, 6, 7]
    # print(pfield)
    assert "Property Field" in str(pfield)
    assert "5" in str(pfield)
    assert "Nodal" in str(pfield)
    assert "entities" in str(pfield)
    assert "1 components and 5 elementary data" in str(pfield)


if __name__ == "__main__":
    test_local_property_field()
