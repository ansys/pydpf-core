import gc
import weakref
import os
import shutil
import numpy as np

import pytest
from ansys import dpf

if 'AWP_UNIT_TEST_FILES' not in os.environ:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')

unit_test_files = os.environ['AWP_UNIT_TEST_FILES']
TEST_FILE_PATH = os.path.join(unit_test_files, 'DataProcessing', 'rst_operators',
                              'velocity_acceleration', 'file.rst')

CYCLIC_RESULT_PATH = os.path.join(unit_test_files, 'DataProcessing', 'cyclic', 'lin', 'file.rst')
CYCLIC_DS_PATH = os.path.join(unit_test_files, 'DataProcessing', 'cyclic', 'lin', 'ds.dat')


# if not dpf.has_local_server():
#     dpf.start_local_server()


def test_create_operator():
    op = dpf.Operator("min_max")
    assert op._message.id


def test_connect_field_operator():
    op= dpf.Operator("min_max")
    inpt = dpf.Field(nentities=3)
    data = [1,2,3,4,5,6,7,8,9]
    scop = dpf.Scoping()
    scop.ids = [1,2,3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    fOut = op.get_output(0, dpf.types.field)
    assert np.allclose(fOut.data,[1.0,2.0,3.0])
    fOut = op.get_output(1, dpf.types.field)
    assert np.allclose(fOut.data,[7.0,8.0,9.0])


def test_connect_list_operator():
    model = dpf.Model(TEST_FILE_PATH)
    op = model.operator("U")
    op.connect(0, [1, 2])
    fcOut = op.get_output(0, dpf.types.fields_container)
    assert fcOut.get_ids() == [1, 2]


def test_connect_list_operator_builtin():
    model = dpf.Model(TEST_FILE_PATH)
    disp = model.results.displacement()
    disp.inputs.time_scoping([1, 2])
    fields = disp.outputs.fields_container()
    assert fields.get_ids() == [1, 2]


def test_connect_fieldscontainer_operator():
    op = dpf.Operator("min_max_fc")
    fc = dpf.FieldsContainer()
    fc.labels=['time','complex']
    scop = dpf.Scoping()
    scop.ids = list(range(1, 11))
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0}
        field = dpf.Field(nentities=10)
        field.scoping = scop
        fc.add_field(mscop, field)
    op.connect(0, fc)
    fOut = op.get_output(0, dpf.types.field)
    assert fOut.data.size == 60


def test_connect_bool_operator():
    op = dpf.Operator("S")
    op.connect(5, True)


def test_print_operator():
    op = dpf.Operator("S")
    print(op)
    
def test_connect_scoping_operator():
    op = dpf.Operator("Rescope")
    scop = dpf.Scoping()
    scop.ids = list(range(1,11))
    field = dpf.Field(nentities=10)
    field.scoping = scop
    scop = dpf.Scoping()
    scop.ids = list(range(1,11))
    scop2=dpf.Scoping()
    scop2.ids = list(range(1,5))
    op.connect(0, field)
    op.connect(1, scop2)
    fOut = op.get_output(0, dpf.types.field)
    scopOut = fOut.scoping
    assert scopOut.ids == list(range(1,5))


def test_connect_datasources_operator():
    op = dpf.Operator("csv_to_field")
    path = os.path.join(unit_test_files, 'DataProcessing', 'csvToField',
                        'fields_container.csv')
    data_sources = dpf.DataSources()
    data_sources.set_result_file_path(path)
    op.connect(4, data_sources)
    fcOut = op.get_output(0, dpf.types.fields_container)
    assert len(fcOut.get_ids()) == 4


def test_connect_operator_operator():
    op= dpf.Operator("norm")
    inpt = dpf.Field(nentities=3)
    data = [1,2,3,4,5,6,7,8,9]
    scop = dpf.Scoping()
    scop.ids = [1,2,3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0,inpt)
    op2=dpf.Operator("component_selector")
    op2.connect(0,op,0)
    op2.connect(1,0)
    fOut = op2.get_output(0, dpf.types.field)
    assert len(fOut.data) == 3
    op2=dpf.Operator("component_selector")

    # attempt to connect without specifying a pin
    # with pytest.raises(Exception):
    #     op2.connect(0, op)

    op2.connect(0, op)
    op2.connect(1, 0)
    fOut = op2.get_output(0, dpf.types.field)
    assert len(fOut.data) == 3


def test_eval_operator():
    op = dpf.Operator("min_max")
    inpt = dpf.Field(nentities=3)
    data = [1,2,3,4,5,6,7,8,9]
    scop = dpf.Scoping()
    scop.ids = [1,2,3]
    inpt.data = data
    inpt.scoping = scop

    op.connect(0, inpt)
    op.get_output()
    op.run()


def test_inputs_outputs_1_operator(tmpdir):
    path = os.path.join(unit_test_files, 'DataProcessing', 'cyclic', 'lin', 'file.rst')
    ds_path = os.path.join(unit_test_files, 'DataProcessing', 'cyclic', 'lin', 'ds.dat')
    data_sources = dpf.DataSources(path)
    data_sources.add_file_path(ds_path)
    model = dpf.Model(data_sources)
    op = model.operator("mapdl::rst::U")
    assert 'data_sources' in str(op.inputs)
    assert 'fields_container' in str(op.outputs)

    support = model.operator("mapdl::rst::support_provider_cyclic")
    expand =model.operator("cyclic_expansion")
    expand.inputs.connect(support.outputs)
    expand.inputs.connect(op.outputs)
    mesh = model.operator("cyclic_expansion_mesh")
    mesh.inputs.cyclic_support.connect(support.outputs.cyclic_support)

    meshed_region = mesh.outputs.meshed_region()
    coord = meshed_region.nodes.coordinates_field
    assert coord.shape == (meshed_region.nodes.n_nodes, 3)
    assert meshed_region.elements.connectivities_field.data.size == meshed_region.elements.connectivities_field.size


def test_inputs_outputs_2_operator(tmpdir):
    path = os.path.join(unit_test_files, 'DataProcessing', 'cyclic', 'lin', 'file.rst')
    ds_path = os.path.join(unit_test_files, 'DataProcessing', 'cyclic', 'lin', 'ds.dat')
    data_sources = dpf.DataSources()
    data_sources.set_result_file_path(path)
    data_sources.add_file_path(ds_path)
    op = dpf.Operator("mapdl::rst::U")
    op.inputs.data_sources.connect(data_sources)
    support = dpf.Operator("mapdl::rst::support_provider_cyclic")
    support.inputs.data_sources.connect(data_sources)
    expand = dpf.Operator("cyclic_expansion")
    expand.inputs.cyclic_support.connect(support.outputs)
    expand.inputs.fields_container.connect(op.outputs)
    mesh = dpf.Operator("cyclic_expansion_mesh")
    mesh.inputs.cyclic_support.connect(support.outputs)

    meshed_region = mesh.outputs.meshed_region()
    coord = meshed_region.nodes.coordinates_field
    assert coord.shape == (meshed_region.nodes.n_nodes, 3)
    assert meshed_region.elements.connectivities_field.size


def test_inputs_outputs_3_operator(tmpdir):
    path = os.path.join(unit_test_files, 'DataProcessing', 'cyclic', 'lin', 'file.rst')
    ds_path = os.path.join(unit_test_files, 'DataProcessing', 'cyclic', 'lin', 'ds.dat')
    data_sources = dpf.DataSources()
    data_sources.set_result_file_path(path)
    data_sources.add_file_path(ds_path)
    op = dpf.Operator("mapdl::rst::U")
    op.inputs.data_sources.connect(data_sources)
    support = dpf.Operator("mapdl::rst::support_provider_cyclic")
    support.inputs.data_sources.connect(data_sources)
    expand = dpf.Operator("cyclic_expansion")
    expand.inputs.cyclic_support.connect(support.outputs.cyclic_support)
    expand.inputs.fields_container.connect(op.outputs.fields_container)
    mesh = dpf.Operator("cyclic_expansion_mesh")
    mesh.inputs.cyclic_support.connect(support.outputs.cyclic_support)

    meshed_region = mesh.outputs.meshed_region()
    coord = meshed_region.nodes.coordinates_field
    assert coord.shape == (meshed_region.nodes.n_nodes, 3)
    assert meshed_region.elements.connectivities_field.size


def test_inputs_outputs_4_operator(tmpdir):
    path = os.path.join(unit_test_files, 'DataProcessing', 'cyclic', 'lin', 'file.rst')
    ds_path = os.path.join(unit_test_files, 'DataProcessing', 'cyclic', 'lin', 'ds.dat')
    data_sources = dpf.DataSources()
    data_sources.set_result_file_path(path)
    data_sources.add_file_path(ds_path)
    data_sources = dpf.DataSources()
    data_sources.set_result_file_path(path)
    data_sources.add_file_path(ds_path)
    op= dpf.Operator("mapdl::rst::U")
    op.inputs.connect(data_sources)
    support = dpf.Operator("mapdl::rst::support_provider_cyclic")
    support.inputs.connect(data_sources)
    expand = dpf.Operator("cyclic_expansion")
    expand.inputs.connect(support.outputs.cyclic_support)
    expand.inputs.connect(op.outputs.fields_container)
    mesh = dpf.Operator("cyclic_expansion_mesh")
    mesh.inputs.connect(support.outputs.cyclic_support)

    meshed_region = mesh.outputs.meshed_region()
    coord = meshed_region.nodes.coordinates_field
    assert coord.shape == (meshed_region.nodes.n_nodes, 3)
    assert meshed_region.elements.connectivities_field.size


def test_inputs_outputs_bool_operator():
    data_sources = dpf.DataSources()
    data_sources.set_result_file_path(CYCLIC_RESULT_PATH)
    data_sources.add_file_path(CYCLIC_DS_PATH)
    op = dpf.Operator("mapdl::rst::U")
    op.inputs.connect(data_sources)
    op.inputs.read_cyclic.connect(1)
    support = dpf.Operator("mapdl::rst::support_provider_cyclic")
    support.inputs.connect(data_sources)
    expand = dpf.Operator("cyclic_expansion")
    expand.inputs.connect(support.outputs.cyclic_support)
    expand.inputs.connect(op.outputs.fields_container)
    fc = expand.outputs.fields_container()
    assert isinstance(fc, dpf.FieldsContainer)
    
    
def test_inputs_outputs_datasources_operator():
    data_sources = dpf.DataSources()
    data_sources.set_result_file_path(CYCLIC_DS_PATH)
    op = dpf.Operator("mapdl::run")
    op.inputs.connect(data_sources)
    dsout=op.outputs.data_sources()
    assert dsout!=None
    assert dsout.result_key=="rst"
    path =os.path.join(dsout.result_files[0])
    try :
        shutil.rmtree(os.path.dirname(path))
        assert True
    except :
        assert False
    
def test_subresults_operator():
    data_sources = dpf.DataSources()
    data_sources.set_result_file_path(CYCLIC_RESULT_PATH)
    data_sources.add_file_path(CYCLIC_DS_PATH)
    model = dpf.Model(data_sources)
    u_op = model.results.displacement()
    ux_op = model.results.displacement().X()
    uy_op = model.results.displacement().Y()
    uz_op = model.results.displacement().Z()
    u = u_op.outputs.fields_container()
    ux = ux_op.outputs.fields_container()
    uy = uy_op.outputs.fields_container()
    uz = uz_op.outputs.fields_container()
    assert u.get_ids() == ux.get_ids()
    assert u.get_ids() == uy.get_ids()
    assert u.get_ids() == uz.get_ids()
    size_tot = u[0].data.size
    assert size_tot/3 == len(ux[0].data)
    assert size_tot/3 == len(uy[0].data)
    assert size_tot/3 == len(uz[0].data)
    
    s_op = model.results.stress()
    s_op.eqv()
    s_op.principal1()
    s_op.principal2()
    s_op.principal3()
    s_op.X()
    s_op.XY()
        
    

# test commented because "mapdl::rst::U" isn't available in
# "mapdl::rst::ResultInfoProvider"
# def test_inputs_outputs_bool_operator_with_model():
    # model = dpf.Model(CYCLIC_RESULT_PATH)
    # model.add_file_path(CYCLIC_DS_PATH)

#     # TODO: this should be available from model's available_results
#     op = model.operator("mapdl::rst::U")
#     op.inputs.connect(model._data_sources)
#     op.inputs.bool_ignore_cyclic.connect(True)

#     support = model.operator("mapdl::rst::CyclicSupportProvider")
#     support.inputs.connect(model._data_sources)
#     expand = model.operator("cyclic_expansion")
#     expand.inputs.connect(support.outputs.cyclic_support)
#     expand.inputs.connect(op.outputs.fields_container)
#     expand.run()
#     fc = expand.outputs.fields_container()
#     assert isinstance(fc, dpf.FieldsContainer)


def test_inputs_outputs_list_operator():
    data_sources = dpf.DataSources()
    data_sources.set_result_file_path(CYCLIC_RESULT_PATH)
    data_sources.add_file_path(CYCLIC_DS_PATH)
    op = dpf.Operator("mapdl::rst::U")
    op.inputs.connect(data_sources)
    op.inputs.time_scoping.connect([1,2,3,8])
    fc = op.outputs.fields_container()
    assert fc.get_ids() == [1,2,3,8]


def test_delete_operator():
    op = dpf.Operator("min_max")
    op.__del__()
    with pytest.raises(Exception):
        op.connect(0, 1)


def test_delete_auto_operator():
    op = dpf.Operator("min_max")

    op_ref = weakref.ref(op)

    del op
    gc.collect()
    assert op_ref() is None
    

if __name__ == '__main__':
    test_inputs_outputs_datasources_operator()
