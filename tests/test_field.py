import numpy as np
import pytest
import copy
import gc
from ansys import dpf
import conftest
from ansys.dpf import core
from ansys.dpf.core import FieldDefinition
from ansys.dpf.core import operators as ops
from ansys.dpf.core.common import locations, shell_layers
from conftest import running_docker


@pytest.fixture()
def stress_field(allkindofcomplexity, server_type):
    model = dpf.core.Model(allkindofcomplexity, server=server_type)
    stress = model.results.stress()
    return stress.outputs.fields_container()[0]


def test_create_field(server_type):
    field = dpf.core.Field(server=server_type)
    assert field._internal_obj is not None


def test_empty_field(server_type):
    field = dpf.core.Field(server=server_type)
    assert np.allclose(field.data, np.empty((0,), dtype=np.float64))
    field = dpf.core.PropertyField(server=server_type)
    assert np.allclose(field.data, np.empty((0,), dtype=np.int32))


def test_create_field_from_helper_scalar(server_type):
    data = np.random.random(10)
    field_a = dpf.core.field_from_array(data, server=server_type)
    assert np.allclose(field_a.data, data)


def test_create_field_from_helper_vector(server_type):
    data = np.random.random((10, 3))
    field_a = dpf.core.field_from_array(data, server=server_type)
    assert np.allclose(field_a.data, data)


def test_set_get_data_from_list_of_list(server_type):
    data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    field = dpf.core.Field(server=server_type)
    field.data = data
    assert np.allclose(field.data, data)


def test_append_scalar_data(server_type):
    field = dpf.core.Field(nature=dpf.core.natures.scalar, server=server_type)
    for i in range(0, 10):
        field.append(float(i), i + 1)
    assert np.allclose(field.data, list(range(0, 10)))


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_createbycopy_field(server_type):
    field = dpf.core.Field(server=server_type)
    field2 = dpf.core.Field(field=field)
    assert field._internal_obj != field2._internal_obj


def test_set_get_scoping(server_type):
    field = dpf.core.Field(server=server_type)
    scoping = dpf.core.Scoping(server=server_type)
    ids = [1, 2, 3, 5, 8, 9, 10]
    scoping.ids = ids
    field.scoping = scoping
    assert np.allclose(field.scoping.ids, ids)


def test_set_get_data_field(server_type):
    field = dpf.core.Field(nentities=20, nature=dpf.core.natures.scalar, server=server_type)
    scoping = dpf.core.Scoping(server=server_type)
    ids = []
    data = []
    for i in range(0, 20):
        ids.append(i + 1)
        data.append(i + 0.001)
    scoping.ids = ids
    field.scoping = scoping
    field.data = data
    assert np.allclose(field.data, data)


def test_set_get_data_array_field(server_type):
    field = dpf.core.Field(nentities=20, nature=dpf.core.natures.vector, server=server_type)
    scoping = dpf.core.Scoping(server=server_type)
    ids = []
    data = []
    for i in range(0, 20):
        ids.append(i + 1)
        data.append(i + 0.001)
        data.append(i + 0.001)
        data.append(i + 0.001)
    data = np.array(data)
    data = data.reshape((20, 3))
    scoping.ids = ids
    field.scoping = scoping
    field.data = data
    assert np.allclose(field.data, data)


def test_append_data_field(server_type):
    field = dpf.core.Field(nentities=20, nature=dpf.core.natures.vector, server=server_type)
    for i in range(0, 20):
        scopingid = i + 1
        scopingindex = i
        data = [0.01 + i, 0.02 + i, 0.03 + i]
        field.append(data, scopingid)
    scopingOut = field.scoping
    assert np.allclose(scopingOut.ids, list(range(1, 21)))
    for i in range(0, 20):
        scopingid = i + 1
        scopingindex = i
        datain = [0.01 + i, 0.02 + i, 0.03 + i]
        dataout = field.get_entity_data(scopingindex)
        assert np.allclose(dataout, datain)


def test_set_get_entity_data_array_field(server_type):
    field = dpf.core.Field(nentities=20, nature=dpf.core.natures.vector, server=server_type)
    for i in range(0, 20):
        scopingid = i + 1
        scopingindex = i
        data = [0.01 + i, 0.02 + i, 0.03 + i]
        data = np.array(data)
        data = data.reshape((1, 3))
        field.append(data, scopingid)
    scopingOut = field.scoping
    assert np.allclose(scopingOut.ids, list(range(1, 21)))
    for i in range(0, 20):
        scopingid = i + 1
        scopingindex = i
        datain = [0.01 + i, 0.02 + i, 0.03 + i]
        dataout = field.get_entity_data(scopingindex)
        assert np.allclose(dataout, datain)
        dataout = field.get_entity_data_by_id(scopingid)
        assert np.allclose(dataout, datain)


# def test_get_data_ptr_field():
#    field= dpf.core.Field(nentities=3, nature=dpf.core.natures.scalar,
#                     location=dpf.core.locations.elemental_nodal)
#    data = [0.01,0.02,0.03]
#    field.set_entity_data(data,0,1)
#    data = [0.01,0.02,0.03,0.01,0.02,0.03]
#    field.set_entity_data(data,1,2)
#    data = [0.01,0.02,0.03,0.01]
#    field.set_entity_data(data,2,3)
#    scopingOut = field.scoping
#    assert scopingOut.ids == [1,2,3]
#    dataptr = field.data_ptr
#    assert dataptr == [0,3,9]


def test_set_get_data_property_field(server_type):
    field = core.Field(nentities=20, nature=dpf.core.natures.scalar, server=server_type)
    scoping = core.Scoping(server=server_type)
    ids = []
    data = []
    for i in range(0, 20):
        ids.append(i + 1)
        data.append(i + 0.001)
    scoping.ids = ids
    field.scoping = scoping
    field.data = data
    assert np.allclose(field.data, data)


def test_count_field(server_type):
    field = dpf.core.Field(nentities=20, nature=dpf.core.natures.scalar, server=server_type)
    scoping = dpf.core.Scoping(server=server_type)
    ids = []
    data = []
    for i in range(0, 20):
        ids.append(i + 1)
        data.append(i + 0.001)
    scoping.ids = ids
    field.scoping = scoping
    field.data = data
    assert field.component_count == 1
    assert field.elementary_data_count == 20
    assert field.size == 20


def test_resize_field(server_type):
    field = dpf.core.Field(nentities=1, nature=dpf.core.natures.scalar, server=server_type)
    scoping = dpf.core.Scoping(server=server_type)
    ids = []
    data = []
    for i in range(0, 20):
        ids.append(i + 1)
        data.append(i + 0.001)
    field.resize(20, 20)
    scoping.ids = ids
    field.scoping = scoping
    field.data = data
    assert field.component_count == 1
    assert field.elementary_data_count == 20
    assert field.size == 20


def test_fromarray_field(server_type):
    data = np.empty((100, 6))
    f = dpf.core.field_from_array(data, server=server_type)
    assert f.shape == (100, 6)


def test_field_definition_field(allkindofcomplexity):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(allkindofcomplexity)
    op = dpf.core.Operator("U")
    op.connect(4, dataSource)

    fcOut = op.get_output(0, dpf.core.types.fields_container)
    f = fcOut[0]
    assert f.unit == "m"
    assert f.location == dpf.core.locations.nodal


def test_field_definition_modif_field(allkindofcomplexity):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(allkindofcomplexity)
    op = dpf.core.Operator("U")
    op.connect(4, dataSource)

    fcOut = op.get_output(0, dpf.core.types.fields_container)
    f = fcOut[0]
    fielddef = f.field_definition
    assert fielddef.unit == "m"
    assert fielddef.location == dpf.core.locations.nodal
    assert fielddef.dimensionality.nature == dpf.core.natures.vector
    assert fielddef.dimensionality.dim == [3]
    assert fielddef.shell_layers == dpf.core.shell_layers.layerindependent

    fielddef.unit = "mm"
    assert fielddef.unit == "mm"
    fielddef.location = dpf.core.locations.elemental
    assert fielddef.location == dpf.core.locations.elemental
    fielddef.dimensionality = dpf.core.Dimensionality.scalar_dim()
    assert fielddef.dimensionality.nature == dpf.core.natures.scalar
    assert fielddef.dimensionality.dim == [1]

    fielddef.dimensionality = dpf.core.Dimensionality.tensor_dim()
    assert fielddef.dimensionality.nature == dpf.core.natures.symmatrix
    assert fielddef.dimensionality.dim == [3, 3]

    fielddef.dimensionality = dpf.core.Dimensionality.vector_3d_dim()
    assert fielddef.dimensionality.nature == dpf.core.natures.vector
    assert fielddef.dimensionality.dim == [3]

    fielddef.dimensionality = dpf.core.Dimensionality.vector_dim(4)
    assert fielddef.dimensionality.nature == dpf.core.natures.vector
    assert fielddef.dimensionality.dim == [4]

    fielddef.shell_layers = dpf.core.shell_layers.bottom
    assert fielddef.shell_layers == dpf.core.shell_layers.bottom


def test_field_definition_set_in_field(allkindofcomplexity):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(allkindofcomplexity)
    op = dpf.core.Operator("U")
    op.connect(4, dataSource)

    fcOut = op.get_output(0, dpf.core.types.fields_container)
    f = fcOut[0]
    fielddef = f.field_definition
    fielddef.unit = "mm"
    fielddef.location = dpf.core.locations.elemental
    fielddef.dimensionality = dpf.core.Dimensionality.scalar_dim()
    fielddef.shell_layers = dpf.core.shell_layers.bottom

    f.field_definition = fielddef
    fielddef = f.field_definition
    assert fielddef.unit == "mm"
    assert fielddef.location == dpf.core.locations.elemental
    assert fielddef.dimensionality.nature == dpf.core.natures.scalar
    assert fielddef.dimensionality.dim == [1]
    assert fielddef.shell_layers == dpf.core.shell_layers.bottom

    assert f.unit == "mm"
    assert f.location == dpf.core.locations.elemental
    assert f.dimensionality.nature == dpf.core.natures.scalar
    assert f.dimensionality.dim == [1]
    assert f.shell_layers == dpf.core.shell_layers.bottom


def test_change_field_definition_in_field(allkindofcomplexity):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(allkindofcomplexity)
    op = dpf.core.Operator("U")
    op.connect(4, dataSource)

    fcOut = op.get_output(0, dpf.core.types.fields_container)
    f = fcOut[0]
    f.unit = "mm"
    f.location = dpf.core.locations.elemental
    f.dimensionality = dpf.core.Dimensionality.scalar_dim()
    f.shell_layers = dpf.core.shell_layers.bottom

    fielddef = f.field_definition
    assert fielddef.unit == "mm"
    assert fielddef.location == dpf.core.locations.elemental
    assert fielddef.dimensionality.nature == dpf.core.natures.scalar
    assert fielddef.dimensionality.dim == [1]
    assert fielddef.shell_layers == dpf.core.shell_layers.bottom

    assert f.unit == "mm"
    assert f.location == dpf.core.locations.elemental
    assert f.dimensionality.nature == dpf.core.natures.scalar
    assert f.dimensionality.dim == [1]
    assert f.shell_layers == dpf.core.shell_layers.bottom


def test_create_overall_field():
    field_overall = dpf.core.Field(nentities=1, location="overall", nature="vector")
    field_overall.scoping.location = "overall"
    field_overall.scoping.ids = [0]
    field_overall.data = [1.0, 2.0, 3.0]

    field = dpf.core.Field(nentities=5, location="nodal")
    field.scoping.location = "nodal"
    field.scoping.ids = list(range(1, 6))
    data = [float(i) for i in range(0, 15)]
    field.data = data
    add = dpf.core.Operator("add")
    add.inputs.fieldA(field)
    add.inputs.fieldB(field_overall)
    field_added = add.outputs.field()
    data_added = field_added.data
    for i in range(0, 5):
        assert np.allclose(data_added[i], [i * 3.0 + 1.0, i * 3.0 + 3.0, i * 3.0 + 5.0])


def test_data_pointer_field(allkindofcomplexity):
    dataSource = dpf.core.DataSources()
    dataSource.set_result_file_path(allkindofcomplexity)
    op = dpf.core.Operator("S")
    op.connect(4, dataSource)

    fcOut = op.get_output(0, dpf.core.types.fields_container)

    data_pointer = fcOut[0]._data_pointer
    assert len(data_pointer) == len(fcOut[0].scoping)
    assert data_pointer[0] == 0
    assert data_pointer[1] == 72

    f = fcOut[0]
    data_pointer[1] = 40
    f._data_pointer = data_pointer
    data_pointer = fcOut[0]._data_pointer

    assert len(data_pointer) == len(fcOut[0].scoping)
    assert data_pointer[0] == 0
    assert data_pointer[1] == 40


def test_data_pointer_prop_field(server_type):
    pfield = dpf.core.PropertyField(server=server_type)
    pfield.append([1, 2, 3], 1)
    pfield.append([1, 2, 3, 4], 2)
    pfield.append([1, 2, 3], 3)
    data_pointer = pfield._data_pointer
    assert len(data_pointer) == 3
    assert data_pointer[0] == 0
    assert data_pointer[1] == 3
    assert data_pointer[2] == 7

    data_pointer[1] = 4
    pfield._data_pointer = data_pointer
    data_pointer = pfield._data_pointer
    assert len(data_pointer) == 3
    assert data_pointer[0] == 0
    assert data_pointer[1] == 4
    assert data_pointer[2] == 7


def test_append_data_elemental_nodal_field(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    stress = model.results.stress()
    f = stress.outputs.fields_container()[0]
    assert f.location == "ElementalNodal"
    f_new = dpf.core.Field(
        f.scoping.size,
        nature=dpf.core.natures.symmatrix,
        location=dpf.core.locations.elemental_nodal,
    )
    size = int(f.scoping.size / 100)
    for i in range(0, size):
        f_new.append(f.get_entity_data(i), f.scoping.id(i))
    for i in range(0, size):
        assert np.allclose(f_new.get_entity_data(i), f.get_entity_data(i))


def test_str_field(stress_field):
    assert "Location" in str(stress_field)
    assert "ElementalNodal" in str(stress_field)
    assert "Unit" in str(stress_field)
    assert "Pa" in str(stress_field)
    assert "9255" in str(stress_field)
    assert "40016" in str(stress_field)
    assert "6" in str(stress_field)


def test_documentation_string_on_field(server_type):
    field = core.Field(
        location=locations.elemental_nodal,
        nature=core.natures.symmatrix,
        server=server_type,
    )
    field.unit = "Pa"
    vec_base = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    field.append(vec_base, 1)
    field.append(vec_base, 2)
    field.append(vec_base, 3)
    to_check = str(field)
    assert "Location" in to_check
    assert "ElementalNodal" in to_check
    assert "Unit" in to_check
    assert "Pa" in to_check
    assert "3" in to_check
    assert "3 elementary data" in to_check
    assert "6 components" in to_check


def test_to_nodal(stress_field):
    assert stress_field.location == "ElementalNodal"
    field_out = stress_field.to_nodal()
    assert field_out.location == "Nodal"


def test_mesh_support_field(stress_field):
    mesh = stress_field.meshed_region
    assert len(mesh.nodes.scoping) == 15129
    assert len(mesh.elements.scoping) == 10292


def test_shell_layers_1(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    stress = model.results.stress()
    f = stress.outputs.fields_container()[0]
    assert f.shell_layers == shell_layers.topbottommid
    model = dpf.core.Model(allkindofcomplexity)
    disp = model.results.displacement()
    f = disp.outputs.fields_container()[0]
    assert f.shell_layers == shell_layers.layerindependent


def test_shell_layers_2(velocity_acceleration):
    model = dpf.core.Model(velocity_acceleration)
    stress = model.results.stress()
    f = stress.outputs.fields_container()[0]
    assert f.shell_layers == shell_layers.nonelayer


def test_mesh_support_field_model(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    stress = model.results.stress()
    f = stress.outputs.fields_container()[0]
    mesh = f.meshed_region
    assert len(mesh.nodes.scoping) == 15129
    assert len(mesh.elements.scoping) == 10292


def test_delete_auto_field(server_type):
    field = dpf.core.Field(server=server_type)
    field2 = dpf.core.Field(field=field, server=server_type)
    field = None
    gc.collect()
    with pytest.raises(Exception):
        field2.get_ids()


def test_create_and_update_field_definition(server_type):
    fieldDef = FieldDefinition(server=server_type)
    assert fieldDef is not None
    with pytest.raises(Exception):
        assert fieldDef.location is None
    fieldDef.location = locations.nodal
    assert fieldDef.location == locations.nodal


@conftest.raises_for_servers_version_under("4.0")
def test_create_and_set_get_name_field_definition(server_type):
    fieldDef = FieldDefinition(server=server_type)
    assert fieldDef is not None

    fieldDef.name = "my_field"
    assert fieldDef.name == "my_field"


def test_set_support_timefreq(simple_bar, server_type):
    tfq = dpf.core.TimeFreqSupport(server=server_type)
    time_frequencies = dpf.core.Field(
        nature=dpf.core.natures.scalar,
        location=dpf.core.locations.time_freq,
        server=server_type,
    )
    time_frequencies.scoping.location = dpf.core.locations.time_freq_step
    time_frequencies.append([0.1, 0.32, 0.4], 1)
    tfq.time_frequencies = time_frequencies

    model = dpf.core.Model(simple_bar, server=server_type)
    disp = model.results.displacement()
    fc = disp.outputs.fields_container()
    field = fc[0]

    # initial_support = field.time_freq_support
    # assert initial_support is None
    field.time_freq_support = tfq
    tfq_to_check = field.time_freq_support
    assert np.allclose(tfq.time_frequencies.data, tfq_to_check.time_frequencies.data)


def test_set_support_mesh(simple_bar):
    mesh = dpf.core.MeshedRegion()
    mesh.nodes.add_node(1, [0.0, 0.0, 0.0])

    model = dpf.core.Model(simple_bar)
    disp = model.results.displacement()
    fc = disp.outputs.fields_container()
    field = fc[0]

    field.meshed_region = mesh
    mesh_to_check = field.meshed_region
    assert mesh_to_check.nodes.n_nodes == 1
    assert mesh_to_check.elements.n_elements == 0

    mesh.nodes.add_node(2, [1.0, 0.0, 0.0])
    mesh.nodes.add_node(3, [1.0, 1.0, 0.0])
    mesh.nodes.add_node(4, [0.0, 1.0, 0.0])
    field.meshed_region = mesh
    mesh_to_check_2 = field.meshed_region
    assert mesh_to_check_2.nodes.n_nodes == 4
    assert mesh_to_check_2.elements.n_elements == 0


def test_local_field_append():
    num_entities = 400
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(num_entities)
    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            f.append([0.1 * i, 0.2 * i, 0.3 * i], i)
        assert f._is_set == True
    field = dpf.core.fields_factory.create_3d_vector_field(num_entities)
    for i in range(1, num_entities + 1):
        field.append([0.1 * i, 0.2 * i, 0.3 * i], i)

    assert np.allclose(field.data, field_to_local.data)
    assert np.allclose(field.scoping.ids, field_to_local.scoping.ids)
    assert len(field_to_local._data_pointer) == 0


def test_local_elemental_nodal_field_append():
    num_entities = 100
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        num_entities, location=dpf.core.locations.elemental_nodal
    )
    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            f.append([[0.1 * i, 0.2 * i, 0.3 * i], [0.1 * i, 0.2 * i, 0.3 * i]], i)
    field = dpf.core.fields_factory.create_3d_vector_field(num_entities)
    for i in range(1, num_entities + 1):
        field.append([[0.1 * i, 0.2 * i, 0.3 * i], [0.1 * i, 0.2 * i, 0.3 * i]], i)

    assert np.allclose(field.data, field_to_local.data)
    assert np.allclose(field.scoping.ids, field_to_local.scoping.ids)
    assert len(field_to_local._data_pointer) == num_entities

    # flat data
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        num_entities, location=dpf.core.locations.elemental_nodal
    )
    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            f.append([0.1 * i, 0.2 * i, 0.3 * i, 0.1 * i, 0.2 * i, 0.3 * i], i)
        assert f._is_set is True
    assert np.allclose(field.data, field_to_local.data)
    assert np.allclose(field.scoping.ids, field_to_local.scoping.ids)
    assert len(field_to_local._data_pointer) == num_entities


def test_local_array_field_append():
    num_entities = 400
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(num_entities)
    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            f.append(np.array([0.1 * i, 0.2 * i, 0.3 * i]), i)
        assert f._is_set is True
    field = dpf.core.fields_factory.create_3d_vector_field(num_entities)
    for i in range(1, num_entities + 1):
        field.append(np.array([0.1 * i, 0.2 * i, 0.3 * i]), i)

    assert np.allclose(field.data, field_to_local.data)
    assert np.allclose(field.scoping.ids, field_to_local.scoping.ids)
    assert len(field_to_local._data_pointer) == 0


def test_local_elemental_nodal_array_field_append():
    num_entities = 100
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        num_entities, location=dpf.core.locations.elemental_nodal
    )
    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            f.append(np.array([[0.1 * i, 0.2 * i, 0.3 * i], [0.1 * i, 0.2 * i, 0.3 * i]]), i)
    field = dpf.core.fields_factory.create_3d_vector_field(num_entities)
    for i in range(1, num_entities + 1):
        field.append(np.array([[0.1 * i, 0.2 * i, 0.3 * i], [0.1 * i, 0.2 * i, 0.3 * i]]), i)

    assert np.allclose(field.data, field_to_local.data)
    assert np.allclose(field.scoping.ids, field_to_local.scoping.ids)
    assert len(field_to_local._data_pointer) == num_entities

    # flat data
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        num_entities, location=dpf.core.locations.elemental_nodal
    )
    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            f.append(np.array([0.1 * i, 0.2 * i, 0.3 * i, 0.1 * i, 0.2 * i, 0.3 * i]), i)

    assert np.allclose(field.data, field_to_local.data)
    assert np.allclose(field.scoping.ids, field_to_local.scoping.ids)
    assert len(field_to_local._data_pointer) == num_entities


def test_local_get_entity_data():
    num_entities = 100
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        num_entities, location=dpf.core.locations.elemental_nodal
    )
    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            f.append(np.array([[0.1 * i, 0.2 * i, 0.3 * i]]), i)
            assert np.allclose(f.get_entity_data(i - 1), [[0.1 * i, 0.2 * i, 0.3 * i]])
            assert np.allclose(f.get_entity_data_by_id(i), [[0.1 * i, 0.2 * i, 0.3 * i]])
        assert hasattr(f, "_is_set") is True

    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            assert np.allclose(f.get_entity_data(i - 1), [[0.1 * i, 0.2 * i, 0.3 * i]])
            assert np.allclose(f.get_entity_data_by_id(i), [[0.1 * i, 0.2 * i, 0.3 * i]])

        assert hasattr(f, "_is_set") is False


def test_local_elemental_nodal_get_entity_data():
    num_entities = 100
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        num_entities, location=dpf.core.locations.elemental_nodal
    )
    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            f.append(np.array([[0.1 * i, 0.2 * i, 0.3 * i], [0.1 * i, 0.2 * i, 0.3 * i]]), i)
            assert np.allclose(
                f.get_entity_data(i - 1),
                [[0.1 * i, 0.2 * i, 0.3 * i], [0.1 * i, 0.2 * i, 0.3 * i]],
            )
            assert np.allclose(
                f.get_entity_data_by_id(i),
                [[0.1 * i, 0.2 * i, 0.3 * i], [0.1 * i, 0.2 * i, 0.3 * i]],
            )
        assert hasattr(f, "_is_set") is True
        assert f._is_set is True

    with field_to_local.as_local_field() as f:
        for i in range(1, num_entities + 1):
            assert np.allclose(
                f.get_entity_data(i - 1),
                [[0.1 * i, 0.2 * i, 0.3 * i], [0.1 * i, 0.2 * i, 0.3 * i]],
            )
            assert np.allclose(
                f.get_entity_data_by_id(i),
                [[0.1 * i, 0.2 * i, 0.3 * i], [0.1 * i, 0.2 * i, 0.3 * i]],
            )
        assert hasattr(f, "_is_set") is False


def test_auto_delete_field_local():
    num_entities = 1
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        num_entities, location=dpf.core.locations.elemental_nodal
    )
    field_to_local.append([3.0, 4.0, 5.0], 1)
    fc = dpf.core.fields_container_factory.over_time_freq_fields_container([field_to_local])
    field_to_local = None
    with fc[0].as_local_field() as f:
        assert np.allclose(f.get_entity_data(0), [3.0, 4.0, 5.0])


def test_auto_delete_field_local2():
    num_entities = 1
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        num_entities, location=dpf.core.locations.elemental_nodal
    )
    f = field_to_local.as_local_field()
    f.append([3.0, 4.0, 5.0], 1)
    del f
    with field_to_local.as_local_field() as f:
        assert np.allclose(f.get_entity_data(0), [3.0, 4.0, 5.0])


def test_get_set_data_local_field():
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        2, location=dpf.core.locations.elemental_nodal
    )
    with field_to_local.as_local_field() as f:
        f.data = [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]]
        assert np.allclose(f.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])

    assert np.allclose(field_to_local.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])

    with field_to_local.as_local_field() as f:
        f.data = [0.1, 0.2, 0.3, 0.1, 0.2, 0.3]
        assert np.allclose(f.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
    assert np.allclose(field_to_local.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])

    with field_to_local.as_local_field() as f:
        f.data = np.array([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
        assert np.allclose(f.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
    assert np.allclose(field_to_local.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])


def test_get_set_data_elemental_nodal_local_field():
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        2, location=dpf.core.locations.elemental_nodal
    )
    with field_to_local.as_local_field() as f:
        f.data = [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.4]]
        f._data_pointer = [0, 6]
        f.scoping_ids = [1, 2]
        assert np.allclose(
            f.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.4]]
        )
        assert np.allclose(f._data_pointer, [0, 6])
        assert np.allclose(f.get_entity_data(0), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
        assert np.allclose(f.get_entity_data(1), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.4]])
        assert hasattr(f, "_is_set") is True
        assert f._is_set is True

    assert np.allclose(
        field_to_local.data,
        [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.4]],
    )
    assert np.allclose(field_to_local._data_pointer, [0, 6])
    assert np.allclose(field_to_local.get_entity_data(0), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
    assert np.allclose(field_to_local.get_entity_data(1), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.4]])

    with field_to_local.as_local_field() as f:
        f.data = [0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.1, 0.2, 0.4]
        f._data_pointer = [0, 6]
        f.scoping_ids = [1, 2]
        assert np.allclose(
            f.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.4]]
        )
        assert np.allclose(f._data_pointer, [0, 6])
        assert np.allclose(f.get_entity_data(0), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
        assert np.allclose(f.get_entity_data(1), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.4]])
        assert hasattr(f, "_is_set") is True
        assert f._is_set is True

    assert np.allclose(
        field_to_local.data,
        [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.4]],
    )
    assert np.allclose(field_to_local._data_pointer, [0, 6])
    assert np.allclose(field_to_local.get_entity_data(0), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
    assert np.allclose(field_to_local.get_entity_data(1), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.4]])

    with field_to_local.as_local_field() as f:
        f.data = np.array([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.4]])
        f._data_pointer = [0, 6]
        f.scoping_ids = [1, 2]
        assert np.allclose(
            f.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.4]]
        )
        assert np.allclose(f._data_pointer, [0, 6])
        assert np.allclose(f.get_entity_data(0), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
        assert np.allclose(f.get_entity_data(1), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.4]])
        assert hasattr(f, "_is_set") is True
        assert f._is_set is True

    assert np.allclose(
        field_to_local.data,
        [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.4]],
    )
    assert np.allclose(field_to_local._data_pointer, [0, 6])
    assert np.allclose(field_to_local.get_entity_data(0), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
    assert np.allclose(field_to_local.get_entity_data(1), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.4]])


def test_get_set_scoping_local_field():
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(
        2, location=dpf.core.locations.elemental_nodal
    )
    with field_to_local.as_local_field() as f:
        f.data = [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]]
        f.scoping = dpf.core.Scoping(ids=[3, 4])
        assert np.allclose(f.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
        assert np.allclose(f.scoping_ids, [3, 4])
        assert np.allclose(f.scoping.ids, [3, 4])
    assert np.allclose(field_to_local.data, [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
    assert np.allclose(field_to_local.scoping.ids, [3, 4])


def test_empty_data_field(server_type):
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(100, server=server_type)
    data = [1.0, 2.0, 3.0]
    field_to_local.data = data
    assert np.allclose(field_to_local.data, data)
    field_to_local.data = []
    assert len(field_to_local.data) == 0


def test_set_data_numpy_array_field(server_type):
    field_to_local = dpf.core.fields_factory.create_3d_vector_field(100, server=server_type)
    arr = np.arange(300, dtype=np.int32).reshape(100, 3)
    field_to_local.data = arr
    assert np.allclose(field_to_local.data, arr)
    arr = np.arange(300, dtype=np.float64).reshape(100, 3)
    field_to_local.data = arr
    assert np.allclose(field_to_local.data, arr)


def test_set_data_numpy_array_property_field(server_type):
    field_to_local = dpf.core.PropertyField(server=server_type)
    arr = np.arange(300, dtype=np.int32)
    field_to_local.data = arr
    assert np.allclose(field_to_local.data, arr)
    arr = np.arange(300, dtype=np.float64)
    field_to_local.data = arr
    assert np.allclose(field_to_local.data, arr)


def test_field_huge_amount_of_data(allkindofcomplexity):
    # set data with a field created from a model
    model = dpf.core.Model(allkindofcomplexity)
    field = model.results.displacement().outputs.fields_container()[0]
    data = field.data
    assert len(data) == 15113
    field.data = data
    new_data = field.data
    assert np.allclose(data, new_data)
    modif_data = data
    modif_data[245] = 45
    modif_data[1129] = 69
    modif_data[7209] = 2086
    modif_data[9046] = 12
    modif_data[12897] = 7894
    modif_data[15112] = 2789
    field.data = modif_data
    new_modif_data = field.data
    assert np.allclose(new_modif_data, modif_data)

    # set data with a field created from scratch
    field = dpf.core.Field(nature=dpf.core.natures.scalar)
    data = range(1, 1000000)
    field.data = data
    data_check = field.data
    assert np.allclose(data_check, data)
    modif_data = data_check
    modif_data[245] = 45
    modif_data[10046] = 69
    modif_data[1999] = 2086
    modif_data[50067] = 12
    modif_data[999345] = 7894
    modif_data[506734] = 2789
    modif_data = modif_data.tolist()
    field.data = modif_data
    new_modif_data = field.data
    assert np.allclose(new_modif_data, modif_data)


@conftest.raises_for_servers_version_under("4.0")
def test_field_mutable_data(server_clayer, allkindofcomplexity):
    # set data with a field created from a model
    model = dpf.core.Model(allkindofcomplexity, server=server_clayer)
    field = model.results.displacement().outputs.fields_container()[0]
    data = field.data
    data_copy = copy.deepcopy(data)
    data[0] += 1.0
    data.commit()
    changed_data = field.data
    assert np.allclose(changed_data, data)
    assert not np.allclose(changed_data, data_copy)
    assert np.allclose(changed_data[0], data_copy[0] + 1.0)
    data[0] += 1
    data = None
    changed_data = field.data
    assert np.allclose(changed_data[0], data_copy[0] + 2.0)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="change in memory ownership in server 5.0",
)
def test_field_mutable_data_delete(server_clayer, allkindofcomplexity):
    # set data with a field created from a model
    model = dpf.core.Model(allkindofcomplexity, server=server_clayer)
    field = model.results.displacement().outputs.fields_container()[0]
    data = field.data
    data_copy = copy.deepcopy(data)
    field = None
    gc.collect()  # check that the memory is held by the dpfvector
    assert np.allclose(data, data_copy)
    data[0][0] = 1
    assert np.allclose(data[0][0], 1)


# not using a fixture on purpose: the instance of simple field SHOULD be owned by each test
def get_simple_field(server_clayer):
    field = dpf.core.Field(nentities=20, server=server_clayer)
    field_def = dpf.core.FieldDefinition(server=server_clayer)
    field_def.dimensionality = dpf.core.Dimensionality([6], dpf.core.natures.vector)
    field.field_definition = field_def
    scop = dpf.core.Scoping(ids=[1, 2, 3, 4], location="faces", server=server_clayer)
    field.scoping = scop

    data = np.empty((24,), dtype=np.float64)
    for i in range(0, 24):
        data[i] = i
    field.data = data
    field._data_pointer = [0, 6, 12, 18]
    return field


@conftest.raises_for_servers_version_under("4.0")
def test_mutable_entity_data_contiguous_field(server_clayer):
    simple_field = get_simple_field(server_clayer)
    vec = simple_field.get_entity_data(0)
    assert np.allclose(vec, np.array(range(0, 6)))

    vec[0][0] = 1
    vec[0][5] = 4

    assert np.allclose(vec, np.array([1, 1, 2, 3, 4, 4]))

    vec.commit()

    assert np.allclose(simple_field.get_entity_data(0), np.array([1, 1, 2, 3, 4, 4]))

    vec = simple_field.get_entity_data_by_id(2)
    assert np.allclose(vec, np.array(range(6, 12)))

    vec[0][0] = 1
    vec[0][5] = 4
    assert np.allclose(vec, np.array([1, 7, 8, 9, 10, 4]))
    vec = None
    assert np.allclose(simple_field.get_entity_data_by_id(2), np.array([1, 7, 8, 9, 10, 4]))


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="change in memory ownership in server 5.0",
)
def test_field_mutable_entity_data_by_id_delete(server_clayer):
    simple_field = get_simple_field(server_clayer)
    data = simple_field.get_entity_data_by_id(2)
    simple_field = None
    gc.collect()  # check that the memory is held by the dpfvector
    assert np.allclose(data, np.array([6.0, 7.0, 8.0, 9.0, 10.0, 11.0]))
    data[0][0] = 0.0
    assert np.allclose(data, np.array([0, 7, 8, 9, 10, 11]))


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="change in memory ownership in server 5.0",
)
def test_field_mutable_entity_data_delete(server_clayer):
    simple_field = get_simple_field(server_clayer)
    data = simple_field.get_entity_data(1)
    simple_field = None
    gc.collect()  # check that the memory is held by the dpfvector
    assert np.allclose(data, np.array([6.0, 7.0, 8.0, 9.0, 10.0, 11.0]))
    data[0][0] = 0.0
    assert np.allclose(data, np.array([0, 7, 8, 9, 10, 11]))


@conftest.raises_for_servers_version_under("4.0")
def test_mutable_entity_data_contiguous_field(server_clayer):
    field = dpf.core.Field(nentities=20, server=server_clayer)
    field_def = dpf.core.FieldDefinition(server=server_clayer)
    field_def.dimensionality = dpf.core.Dimensionality([6], dpf.core.natures.vector)
    field.field_definition = field_def
    scop = dpf.core.Scoping(ids=[1, 2, 3, 4], location="faces", server=server_clayer)
    field.scoping = scop

    data = np.empty((24,), dtype=np.float64)
    for i in range(0, 24):
        data[i] = i
    field.data = data
    field._data_pointer = [0, 6, 12, 18]

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


@conftest.raises_for_servers_version_under("4.0")
def test_field_mutable_data_pointer(server_clayer, allkindofcomplexity):
    # set data with a field created from a model
    model = dpf.core.Model(allkindofcomplexity, server=server_clayer)
    field = model.results.stress().outputs.fields_container()[0]
    data = field._data_pointer
    data_copy = copy.deepcopy(data)
    data[0] += 1
    data.commit()
    changed_data = field._data_pointer
    assert np.allclose(changed_data, data)
    assert not np.allclose(changed_data, data_copy)
    assert np.allclose(changed_data[0], data_copy[0] + 1)
    data[0] += 1
    data = None
    changed_data = field._data_pointer
    assert np.allclose(changed_data[0], data_copy[0] + 2)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="change in memory ownership in server 5.0",
)
def test_field_mutable_data_pointer_delete(server_clayer, allkindofcomplexity):
    # set data with a field created from a model
    model = dpf.core.Model(allkindofcomplexity, server=server_clayer)
    field = model.results.stress().outputs.fields_container()[0]
    data = field._data_pointer
    data_copy = copy.deepcopy(data)
    field = None
    gc.collect()  # check that the memory is held by the dpfvector
    assert np.allclose(data, data_copy)
    data[0] = 1
    data_copy[0] = 1
    assert np.allclose(data, data_copy)


def _deep_copy_test_identical_server(config):
    serv = dpf.core.start_local_server(as_global=False, config=config)
    field = dpf.core.fields_factory.create_3d_vector_field(100, server=serv)
    arr = np.arange(300).reshape(100, 3)
    field.data = arr
    copy = field.deep_copy(server=serv)
    iden = dpf.core.operators.logic.identical_fields(field, copy, server=serv)
    assert iden.outputs.boolean()
    assert field.unit == copy.unit


@pytest.mark.skipif(
    running_docker or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="this server type does not exist before client" "dedicated to 4.0 server version",
)
def test_deep_copy_field_grpcclayer_to_grpcclayer():
    config = dpf.core.ServerConfig(
        protocol=dpf.core.server_factory.CommunicationProtocols.gRPC, legacy=False
    )
    _deep_copy_test_identical_server(config)


def test_deep_copy_field_grpclegacy_to_grpclegacy():
    config = dpf.core.ServerConfig(
        protocol=dpf.core.server_factory.CommunicationProtocols.gRPC, legacy=True
    )
    _deep_copy_test_identical_server(config)


@pytest.mark.skipif(
    running_docker or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="this server type does not exist before client" "dedicated to 4.0 server version",
)
def test_deep_copy_field_inprocess_to_inprocess():
    config = dpf.core.ServerConfig(
        protocol=dpf.core.server_factory.CommunicationProtocols.InProcess, legacy=False
    )
    _deep_copy_test_identical_server(config)


def test_deep_copy_field_2(plate_msup):
    model = dpf.core.Model(plate_msup)
    disp = model.results.displacement()
    fields_container = disp.outputs.fields_container()
    field = fields_container[0]
    field.deep_copy()


def test_deep_copy_field():
    field = dpf.core.fields_factory.create_3d_vector_field(100)
    arr = np.arange(300).reshape(100, 3)
    field.data = arr
    copy = field.deep_copy()
    iden = dpf.core.operators.logic.identical_fields(field, copy)
    assert iden.outputs.boolean()
    assert field.unit == copy.unit


@pytest.mark.slow
def test_deep_copy_elemental_nodal_field(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    stress = model.results.stress()
    field = stress.outputs.fields_container()[0]
    copy = field.deep_copy()
    iden = dpf.core.operators.logic.identical_fields(field, copy)

    try:
        assert iden.outputs.boolean()
    except AssertionError as e:
        print(iden.outputs.message())
        raise e

    mesh = field.meshed_region
    copy = copy.meshed_region
    assert np.allclose(copy.nodes.scoping.ids, mesh.nodes.scoping.ids)
    assert np.allclose(copy.elements.scoping.ids, mesh.elements.scoping.ids)
    assert copy.unit == mesh.unit
    assert np.allclose(copy.nodes.coordinates_field.data, mesh.nodes.coordinates_field.data)
    assert np.allclose(
        copy.elements.element_types_field.data, mesh.elements.element_types_field.data
    )
    assert np.allclose(
        copy.elements.connectivities_field.data, mesh.elements.connectivities_field.data
    )

    assert np.allclose(
        copy.nodes.coordinates_field.scoping.ids,
        mesh.nodes.coordinates_field.scoping.ids,
    )
    assert np.allclose(
        copy.elements.element_types_field.scoping.ids,
        mesh.elements.element_types_field.scoping.ids,
    )
    assert np.allclose(
        copy.elements.connectivities_field.scoping.ids,
        mesh.elements.connectivities_field.scoping.ids,
    )


def test_deep_copy_over_time_field(velocity_acceleration):
    model = dpf.core.Model(velocity_acceleration)
    stress = model.results.stress(time_scoping=[1, 2, 3])
    min_max = dpf.core.operators.min_max.min_max_fc(stress)
    field = min_max.outputs.field_max()
    copy = field.deep_copy()
    iden = dpf.core.operators.logic.identical_fields(field, copy)
    assert iden.outputs.boolean()

    tf = field.time_freq_support
    copy = copy.time_freq_support
    assert np.allclose(tf.time_frequencies.data, copy.time_frequencies.data)
    assert tf.time_frequencies.scoping.ids == copy.time_frequencies.scoping.ids


def test_deep_copy_spec_ncomp_field():
    field = dpf.core.fields_factory.create_vector_field(100, 6, dpf.core.locations.elemental)
    arr = np.arange(600).reshape(100, 6)
    field.data = arr
    copy = field.deep_copy()
    assert copy.component_count == 6
    assert copy.location == dpf.core.locations.elemental


def test_add_operator_field():
    field = dpf.core.fields_factory.create_3d_vector_field(2)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    # field+op
    forward = ops.utility.forward_field(field)
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


def test_minus_operator_field():
    field = dpf.core.fields_factory.create_3d_vector_field(2)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    # field-op
    forward = ops.utility.forward_field(field)
    add = field - forward
    assert type(add) == ops.math.minus
    out = add.outputs.field()
    assert len(out) == 6
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.zeros((2, 3)))

    # fc - list
    add = field - [0.0, 1.0, 2.0]
    assert type(add) == ops.math.minus
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([[0.0, 0.0, 0.0], [3.0, 3.0, 3.0]]))

    # operator - float
    add = field - 1.0
    assert type(add) == ops.math.minus
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([[-1.0, 0.0, 1.0], [2.0, 3.0, 4.0]]))


def test_dot_operator_field():
    field = dpf.core.fields_factory.create_3d_vector_field(2)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    # field * op
    forward = ops.utility.forward_field(field)
    add = field * forward
    assert type(add) == ops.math.generalized_inner_product
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([5.0, 50.0]))

    # field * field
    add = field * field
    assert type(add) == ops.math.generalized_inner_product
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([5.0, 50.0]))

    # field * list
    add = field * [0.0, 1.0, 2.0]
    assert type(add) == ops.math.generalized_inner_product
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, np.array([5.0, 14.0]))

    # field * float
    add = field * -1.0
    assert type(add) == ops.math.generalized_inner_product
    out = add.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2])
    assert np.allclose(out.data, -field.data)
