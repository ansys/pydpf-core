import gc
import weakref
import os
import shutil

import numpy as np
import pytest

from ansys import dpf
from ansys.dpf.core import errors

# Check for ANSYS installation env var
HAS_AWP_ROOT211 = os.environ.get('AWP_ROOT211', False) is not False


def test_create_operator():
    op = dpf.core.Operator("min_max")
    assert op._message.id


def test_invalid_operator_name():
    with pytest.raises(errors.DPFServerException):
        dpf.core.Operator("not-an-operator")


def test_connect_field_operator():
    op= dpf.core.Operator("min_max")
    inpt = dpf.core.Field(nentities=3)
    data = [1,2,3,4,5,6,7,8,9]
    scop = dpf.core.Scoping()
    scop.ids = [1,2,3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    fOut = op.get_output(0, dpf.core.types.field)
    assert np.allclose(fOut.data,[1.0,2.0,3.0])
    fOut = op.get_output(1, dpf.core.types.field)
    assert np.allclose(fOut.data,[7.0,8.0,9.0])


def test_connect_list_operator(velocity_acceleration):
    model = dpf.core.Model(velocity_acceleration)
    op = model.operator("U")
    op.connect(0, [1, 2])
    fcOut = op.get_output(0, dpf.core.types.fields_container)
    assert fcOut.get_ids() == [1, 2]


def test_connect_list_operator_builtin(velocity_acceleration):
    model = dpf.core.Model(velocity_acceleration)
    disp = model.results.displacement()
    disp.inputs.time_scoping([1, 2])
    fields = disp.outputs.fields_container()
    assert fields.get_ids() == [1, 2]


def test_connect_fieldscontainer_operator():
    op = dpf.core.Operator("min_max_fc")
    fc = dpf.core.FieldsContainer()
    fc.labels=['time','complex']
    scop = dpf.core.Scoping()
    scop.ids = list(range(1, 11))
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0}
        field = dpf.core.Field(nentities=10)
        field.scoping = scop
        fc.add_field(mscop, field)
    op.connect(0, fc)
    fOut = op.get_output(0, dpf.core.types.field)
    assert fOut.data.size == 60


def test_connect_bool_operator():
    op = dpf.core.Operator("S")
    op.connect(5, True)


def test_print_operator():
    op = dpf.core.Operator("S")
    print(op)
    
def test_connect_scoping_operator():
    op = dpf.core.Operator("Rescope")
    scop = dpf.core.Scoping()
    scop.ids = list(range(1,11))
    field = dpf.core.Field(nentities=10)
    field.scoping = scop
    scop = dpf.core.Scoping()
    scop.ids = list(range(1,11))
    scop2=dpf.core.Scoping()
    scop2.ids = list(range(1,5))
    op.connect(0, field)
    op.connect(1, scop2)
    fOut = op.get_output(0, dpf.core.types.field)
    scopOut = fOut.scoping
    assert scopOut.ids == list(range(1,5))


def test_connect_datasources_operator(fields_container_csv):
    op = dpf.core.Operator("csv_to_field")
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(fields_container_csv)
    op.connect(4, data_sources)
    fcOut = op.get_output(0, dpf.core.types.fields_container)
    assert len(fcOut.get_ids()) == 4


def test_connect_operator_operator():
    op= dpf.core.Operator("norm")
    inpt = dpf.core.Field(nentities=3)
    data = [1,2,3,4,5,6,7,8,9]
    scop = dpf.core.Scoping()
    scop.ids = [1,2,3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0,inpt)
    op2=dpf.core.Operator("component_selector")
    op2.connect(0,op,0)
    op2.connect(1,0)
    fOut = op2.get_output(0, dpf.core.types.field)
    assert len(fOut.data) == 3
    op2=dpf.core.Operator("component_selector")

    # attempt to connect without specifying a pin
    # with pytest.raises(Exception):
    #     op2.connect(0, op)

    op2.connect(0, op)
    op2.connect(1, 0)
    fOut = op2.get_output(0, dpf.core.types.field)
    assert len(fOut.data) == 3


def test_eval_operator():
    op = dpf.core.Operator("min_max")
    inpt = dpf.core.Field(nentities=3)
    data = range(1, 10)
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop

    op.connect(0, inpt)
    op.get_output()
    op.run()


def test_inputs_outputs_1_operator(cyclic_lin_rst, cyclic_ds, tmpdir):
    data_sources = dpf.core.DataSources(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    model = dpf.core.Model(data_sources)
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


def test_inputs_outputs_2_operator(cyclic_lin_rst, cyclic_ds):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    op = dpf.core.Operator("mapdl::rst::U")
    op.inputs.data_sources.connect(data_sources)
    support = dpf.core.Operator("mapdl::rst::support_provider_cyclic")
    support.inputs.data_sources.connect(data_sources)
    expand = dpf.core.Operator("cyclic_expansion")
    expand.inputs.cyclic_support.connect(support.outputs)
    expand.inputs.fields_container.connect(op.outputs)
    mesh = dpf.core.Operator("cyclic_expansion_mesh")
    mesh.inputs.cyclic_support.connect(support.outputs)

    meshed_region = mesh.outputs.meshed_region()
    coord = meshed_region.nodes.coordinates_field
    assert coord.shape == (meshed_region.nodes.n_nodes, 3)
    assert meshed_region.elements.connectivities_field.size


def test_inputs_outputs_3_operator(cyclic_lin_rst, cyclic_ds, tmpdir):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    op = dpf.core.Operator("mapdl::rst::U")
    op.inputs.data_sources.connect(data_sources)
    support = dpf.core.Operator("mapdl::rst::support_provider_cyclic")
    support.inputs.data_sources.connect(data_sources)
    expand = dpf.core.Operator("cyclic_expansion")
    expand.inputs.cyclic_support.connect(support.outputs.cyclic_support)
    expand.inputs.fields_container.connect(op.outputs.fields_container)
    mesh = dpf.core.Operator("cyclic_expansion_mesh")
    mesh.inputs.cyclic_support.connect(support.outputs.cyclic_support)

    meshed_region = mesh.outputs.meshed_region()
    coord = meshed_region.nodes.coordinates_field
    assert coord.shape == (meshed_region.nodes.n_nodes, 3)
    assert meshed_region.elements.connectivities_field.size


def test_inputs_outputs_4_operator(cyclic_lin_rst, cyclic_ds, tmpdir):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    op= dpf.core.Operator("mapdl::rst::U")
    op.inputs.connect(data_sources)
    support = dpf.core.Operator("mapdl::rst::support_provider_cyclic")
    support.inputs.connect(data_sources)
    expand = dpf.core.Operator("cyclic_expansion")
    expand.inputs.connect(support.outputs.cyclic_support)
    expand.inputs.connect(op.outputs.fields_container)
    mesh = dpf.core.Operator("cyclic_expansion_mesh")
    mesh.inputs.connect(support.outputs.cyclic_support)

    meshed_region = mesh.outputs.meshed_region()
    coord = meshed_region.nodes.coordinates_field
    assert coord.shape == (meshed_region.nodes.n_nodes, 3)
    assert meshed_region.elements.connectivities_field.size


def test_inputs_outputs_bool_operator(cyclic_lin_rst, cyclic_ds):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    op = dpf.core.Operator("mapdl::rst::U")
    op.inputs.connect(data_sources)
    op.inputs.read_cyclic.connect(1)
    support = dpf.core.Operator("mapdl::rst::support_provider_cyclic")
    support.inputs.connect(data_sources)
    expand = dpf.core.Operator("cyclic_expansion")
    expand.inputs.connect(support.outputs.cyclic_support)
    expand.inputs.connect(op.outputs.fields_container)
    fc = expand.outputs.fields_container()
    assert isinstance(fc, dpf.core.FieldsContainer)


@pytest.mark.skipif(not HAS_AWP_ROOT211, reason='Requires AWP_ROOT211')
def test_inputs_outputs_datasources_operator(cyclic_ds):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(cyclic_ds)
    op = dpf.core.Operator("mapdl::run")
    op.inputs.connect(data_sources)
    dsout = op.outputs.data_sources()
    assert dsout is not None
    assert dsout.result_key == "rst"
    path = os.path.join(dsout.result_files[0])
    shutil.rmtree(os.path.dirname(path))


def test_subresults_operator(cyclic_lin_rst, cyclic_ds):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    model = dpf.core.Model(data_sources)
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
# def test_inputs_outputs_bool_operator_with_model(cyclic_lin_rst, cyclic_ds):
#     model = dpf.core.Model(cyclic_lin_rst)
#     model.add_file_path(cyclic_ds)

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
#     assert isinstance(fc, dpf.core.FieldsContainer)


def test_inputs_outputs_list_operator(cyclic_lin_rst, cyclic_ds):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    op = dpf.core.Operator("mapdl::rst::U")
    op.inputs.connect(data_sources)
    op.inputs.time_scoping.connect([1,2,3,8])
    fc = op.outputs.fields_container()
    assert fc.get_ids() == [1,2,3,8]


def test_delete_operator():
    op = dpf.core.Operator("min_max")
    op.__del__()
    with pytest.raises(Exception):
        op.connect(0, 1)


def test_delete_auto_operator():
    op = dpf.core.Operator("min_max")

    op_ref = weakref.ref(op)

    del op
    gc.collect()
    assert op_ref() is None
