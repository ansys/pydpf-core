import numpy as np

import conftest

import ansys.dpf.core as dpf


def integer_field(server):
    field = dpf.CustomTypeField(np.uint64, server=server)
    list_ids = [1, 2, 4, 6, 7]
    scop = dpf.Scoping(ids=list_ids, location=dpf.locations.nodal, server=server)
    field.scoping = scop
    list_data = np.array([20, 30, 50, 70, 80], dtype=np.uint64)
    field.data = list_data
    field.location = dpf.locations.nodal
    field.unit = "m"
    return field


@conftest.raises_for_servers_version_under("5.0")
def test_create_custom_type_fields_container(server_type):
    field = integer_field(server_type)
    fc = dpf.CustomTypeFieldsContainer(np.uint64, server_type)
    assert str(fc) == ""
    assert fc.type == np.uint64
    assert fc.is_of_type(np.uint64)
    print(fc.create_subtype(field))
