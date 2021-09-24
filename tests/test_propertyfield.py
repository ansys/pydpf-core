import pytest
import numpy as np
import os

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


def test_scopingdata_property_field():
    pfield = dpf.core.PropertyField()
    list_ids = [1, 2, 4, 6, 7]
    scop = core.Scoping(ids=list_ids, location=locations.nodal)
    pfield.scoping = scop
    list_data = [20, 30, 50, 70, 80]
    pfield.data = list_data
    pfield.data
    assert np.allclose(pfield.data, list_data)
    assert np.allclose(pfield.scoping.ids, list_ids)


def test_set_get_data_property_field():
    field = dpf.core.PropertyField(nentities=20, nature=natures.scalar)
    data = []
    for i in range(0, 20):
        data.append(i)
    field.data = data
    assert np.allclose(field.data, data)


def test_create_property_field_push_back():
    f_vec = core.PropertyField(1, core.natures.vector, core.locations.nodal)
    f_vec.append([1, 2, 4], 1)
    assert len(f_vec.data) == 3
    assert f_vec.data[0] == 1
    assert f_vec.data[1] == 2
    assert f_vec.data[2] == 4
    assert f_vec.scoping.ids == [1]
    assert len(f_vec.scoping.ids) == 1

    f_scal = core.PropertyField(1, core.natures.scalar, core.locations.nodal)
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
    assert prop_field.data[15] == 29
    assert np.allclose(prop_field.data[12], 10)
    assert prop_field.elementary_data_count == 1400
    assert prop_field.data[1201] == 2500
    assert prop_field.elementary_data_shape == 1
    assert prop_field.get_entity_data(8) == [7]
    assert prop_field.get_entity_data_by_id(23) == [60]
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


def test_set_prop_field_from_message(property_field):
    prop_field_message = property_field._message
    new_prop_field = dpf.core.PropertyField(property_field=prop_field_message)
    assert isinstance(new_prop_field, dpf.core.PropertyField)
    check_on_property_field_from_simplebar(new_prop_field)


def test_set_prop_field_from_prop_field(property_field):
    new_prop_field = dpf.core.PropertyField(property_field=property_field)
    assert isinstance(new_prop_field, dpf.core.PropertyField)
    check_on_property_field_from_simplebar(new_prop_field)


def test_connect_property_field_operator():
    f_vec = dpf.core.PropertyField(1, natures.vector, locations.nodal)
    f_vec.append([1, 2, 4], 1)
    op = dpf.core.operators.utility.forward()
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
    wf.add_operator(op)
    wf.set_output_name("field_out", op, 3)

    property_field = wf.get_output("field_out", dpf.core.types.property_field)
    check_on_property_field_from_simplebar(property_field)


def test_connect_property_field_workflow():
    f_vec = dpf.core.PropertyField(1, natures.vector, locations.nodal)
    f_vec.append([1, 2, 4], 1)
    op = dpf.core.operators.utility.forward()

    wf = dpf.core.Workflow()
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
    field_to_local = dpf.core.PropertyField(
        num_entities, dpf.core.natures.scalar, locations.nodal
    )
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
    assert np.allclose(
        field_to_local._data_pointer, data_pointer[0 : len(data_pointer)]
    )

    with field_to_local.as_local_field() as f:
        assert np.allclose(f.data, data)
        assert np.allclose(f._data_pointer, data_pointer[0 : len(data_pointer)])


if __name__ == "__main__":
    test_local_property_field()
