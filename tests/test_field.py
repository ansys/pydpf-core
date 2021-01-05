import pytest
import numpy as np

from ansys import dpf
from ansys.dpf.core.common import ShellLayers


@pytest.fixture()
def stress_field(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    stress = model.results.stress()
    return stress.outputs.fields_container()[0]


def test_create_field():
    field = dpf.core.Field()
    assert field._message.id != 0


def test_create_field_from_helper_scalar():
    data = np.random.random(10)
    field_a = dpf.core.field_from_array(data)
    assert np.allclose(field_a.data, data)


def test_create_field_from_helper_vector():
    data = np.random.random((10, 3))
    field_a = dpf.core.field_from_array(data)
    assert np.allclose(field_a.data, data)


def test_createbycopy_field():
    field = dpf.core.Field()
    field2 = dpf.core.Field(field=field._message)
    assert field._message.id == field2._message.id


def test_set_get_scoping():
    field = dpf.core.Field()
    scoping = dpf.core.Scoping()
    ids=[1,2,3,5,8,9,10]
    scoping.ids=ids
    field.scoping = scoping
    assert field.scoping.ids == ids


def test_set_get_data_field():
    field = dpf.core.Field(nentities=20, nature=dpf.core.natures.scalar)
    scoping = dpf.core.Scoping()
    ids = []
    data= []
    for i in range(0, 20):
        ids.append(i+1)
        data.append(i+0.001)
    scoping.ids = ids
    field.scoping = scoping
    field.data = data
    assert np.allclose(field.data,data)
    
    
def test_set_get_data_array_field(): 
    field= dpf.core.Field(nentities=20, nature=dpf.core.natures.vector)
    scoping = dpf.core.Scoping()
    ids =[]
    data=[]
    for i in range(0, 20):
        ids.append(i+1)
        data.append(i+0.001)
        data.append(i+0.001)
        data.append(i+0.001)
    data = np.array(data)
    data =data.reshape((20,3))
    scoping.ids = ids
    field.scoping = scoping
    field.data = data
    assert np.allclose(field.data,data)


def test_set_get_entity_data_field(): 
    field= dpf.core.Field(nentities=20, nature=dpf.core.natures.vector)
    for i in range(0,20):
        scopingid= i+1
        scopingindex=i
        data = [0.01+i,0.02+i,0.03+i]
        field.set_entity_data(data, scopingindex,scopingid)
    scopingOut = field.scoping
    assert scopingOut.ids == list(range(1,21))
    for i in range(0,20):
        scopingid= i+1
        scopingindex=i
        datain = [0.01+i,0.02+i,0.03+i]
        dataout = field.get_entity_data(scopingindex)
        assert np.allclose(dataout,datain)
        

def test_set_get_entity_data_array_field(): 
    field= dpf.core.Field(nentities=20, nature=dpf.core.natures.vector)
    for i in range(0,20):
        scopingid= i+1
        scopingindex=i
        data = [0.01+i,0.02+i,0.03+i]
        data = np.array(data)
        data =data.reshape((1,3))
        field.set_entity_data(data, scopingindex,scopingid)
    scopingOut = field.scoping
    assert scopingOut.ids == list(range(1,21))
    for i in range(0,20):
        scopingid= i+1
        scopingindex=i
        datain = [0.01+i,0.02+i,0.03+i]
        dataout = field.get_entity_data(scopingindex)
        assert np.allclose(dataout,datain)
        dataout = field.get_entity_data_by_id(scopingid)
        assert np.allclose(dataout,datain)


#def test_get_data_ptr_field(): 
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


def test_set_get_data_property_field():
    field= dpf.core.Field(nentities=20, nature=dpf.core.natures.scalar)
    scoping = dpf.core.Scoping()
    ids = []
    data= []
    for i in range(0, 20):
        ids.append(i+1)
        data.append(i+0.001)
    scoping.ids = ids
    field.scoping = scoping
    field.data = data
    assert np.allclose(field.data,data)


def test_count_field():
    field= dpf.core.Field(nentities=20, nature=dpf.core.natures.scalar)
    scoping = dpf.core.Scoping()
    ids = []
    data= []
    for i in range(0, 20):
        ids.append(i+1)
        data.append(i+0.001)
    scoping.ids = ids
    field.scoping = scoping
    field.data = data
    assert field.component_count == 1
    assert field.elementary_data_count == 20
    assert field.size == 20
    
def test_resize_field():
    field= dpf.core.Field(nentities=1, nature=dpf.core.natures.scalar)
    scoping = dpf.core.Scoping()
    ids = []
    data= []
    for i in range(0, 20):
        ids.append(i+1)
        data.append(i+0.001)
    field.resize(20,20)
    scoping.ids = ids
    field.scoping = scoping
    field.data = data
    assert field.component_count == 1
    assert field.elementary_data_count == 20
    assert field.size == 20


def test_fromarray_field():
    data = np.empty((100, 6))
    f = dpf.core.field_from_array(data)
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


def test_create_overall_field():
    field_overall = dpf.core.Field(nentities=1, location="overall", nature="vector")
    field_overall.scoping.location = "overall"
    field_overall.data = [1.0, 2.0, 3.0]

    field = dpf.core.Field(nentities=5, location="nodal")
    field.scoping.location = "nodal"
    field.scoping.ids = list(range(1,6))
    data =[float(i) for i in range(0,15)]
    field.data = data
    add = dpf.core.Operator("add")
    add.inputs.fieldA(field)
    add.inputs.fieldB(field_overall)
    field_added= add.outputs.field()
    data_added = field_added.data
    for i in range(0,5):
        assert np.allclose(data_added[i],[i*3.0+1.0,i*3.0+3.0,i*3.0+5.0])


@pytest.mark.skipif(True, reason="set entity data has an issue when location is elemental nodal")
def test_set_entity_data_elemental_nodal_field(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    stress = model.results.stress()
    f = stress.outputs.fields_container()[0]
    assert f.location == "ElementalNodal"
    f_new= dpf.core.Field(nature=dpf.core.natures.symmatrix, location='elemental_nodal')
    f_new.resize(f.scoping.size, f.size)
    for i in range(0,f.scoping.size):
        f_new.set_entity_data(f.get_entity_data(i),i,f.scoping.id(i))
    for i in range(0,f.scoping.size):
        assert np.allclose(f_new.get_entity_data(i), f.get_entity_data(i))


def test_str_field(stress_field):
    assert 'Location:   ElementalNodal' in str(stress_field)
    assert 'Unit:       Pa' in str(stress_field)
    assert 'Num. id(s): 9255' in str(stress_field)
    assert 'Shape:      (40016, 6)' in str(stress_field)


def test_mesh_support_field(stress_field):
    mesh = stress_field.meshed_region
    assert len(mesh.nodes.scoping) == 15129
    assert len(mesh.elements.scoping) == 10292


def test_shell_layers_1(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    stress = model.results.stress()
    f = stress.outputs.fields_container()[0]
    assert f.shell_layers == ShellLayers.TOPBOTTOMMID
    model = dpf.core.Model(allkindofcomplexity)
    disp = model.results.displacement()
    f = disp.outputs.fields_container()[0]
    assert f.shell_layers == ShellLayers.INDEPENDANTLAYER


def test_shell_layers_2(velocity_acceleration):
    model = dpf.core.Model(velocity_acceleration)
    stress = model.results.stress()
    f = stress.outputs.fields_container()[0]
    assert f.shell_layers == ShellLayers.NONELAYER


def test_delete_auto_field():
    field = dpf.core.Field()
    field2 = dpf.core.Field(field=field)
    del field
    assert field2.location == 'Nodal'
