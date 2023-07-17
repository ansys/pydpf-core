import pytest

from ansys.dpf.core.property_fields_container import PropertyFieldsContainer, _LabelSpaceKV
from ansys.dpf import core as dpf


def test_property_fields_container(allkindofcomplexity, server_type):
    model = dpf.Model(allkindofcomplexity, server=server_type)
    fields_container = PropertyFieldsContainer(server=server_type)
    fields_container.add_label(label="test")
    assert fields_container.has_label(label="test")
    assert fields_container.labels == ["test"]
    with pytest.raises(ValueError, match="labels already set"):
        fields_container.labels = ["test"]
    field = model.metadata.meshed_region.elements.connectivities_field
    fields_container.add_field(label_space={"test": 42}, field=field)
    assert len(fields_container.label_spaces) == 1
    label_space = fields_container.label_spaces[0]
    assert fields_container.get_label_space(0) == {"test": 42}
    assert isinstance(label_space, _LabelSpaceKV)
    assert label_space.field == field
    assert label_space.dict == {"test": 42}
    label_space.field = model.metadata.meshed_region.elements.element_types_field
    ref = """DPF PropertyFieldsContainer with 1 fields
\t 0: Label Space: {'test': 42} with field
\t\t\tDPF Property Field
\t\t\t  10292 """  # noqa
    assert ref in str(fields_container)
    with pytest.raises(KeyError, match="label test2 not found"):
        fields_container.get_label_scoping("test2")
    scoping = fields_container.get_label_scoping("test")
    assert isinstance(scoping, dpf.Scoping)
    assert scoping.ids == [1]
    assert scoping.location == ""

    property_field = fields_container.get_entries(0)[0]
    assert isinstance(property_field, dpf.property_field.PropertyField)
    assert fields_container.get_entries({"test": 42})[0] == property_field
    with pytest.raises(KeyError, match="is not in labels:"):
        fields_container.get_entries(({"test2": 0}))
    assert fields_container.get_entry({"test": 42}) == property_field
    with pytest.raises(ValueError, match="Could not find corresponding entry"):
        fields_container.get_entry(({"test": 0}))
    assert fields_container[{"test": 42}] == property_field
    assert len(fields_container) == 1

    assert fields_container.get_fields({"test": 42})[0] == property_field
    assert fields_container.get_field(0) == property_field

    fields_container.add_field_by_time_id(property_field)
    assert fields_container.has_label("time")
    assert fields_container.get_field_by_time_id(1) == property_field
    fields_container.add_imaginary_field(property_field)
    assert fields_container.get_imaginary_field(1) == property_field
    time_scoping = fields_container.get_time_scoping()
    assert isinstance(time_scoping, dpf.Scoping)
    assert scoping.ids == [1]
