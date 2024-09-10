import gc
import os
import shutil
import types
import weakref

import numpy as np
import pytest
import copy

from ansys import dpf
from ansys.dpf.core import errors
from ansys.dpf.core import operators as ops
from ansys.dpf.core.misc import get_ansys_path
from ansys.dpf.core.operator_specification import Specification
import conftest
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_2,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0,
)

# Check for ANSYS installation env var
HAS_AWP_ROOT212 = os.environ.get("AWP_ROOT212", False) is not False


def test_create_operator(server_type):
    op = dpf.core.Operator("min_max", server=server_type)
    assert op._internal_obj


def test_invalid_operator_name(server_type):
    # with pytest.raises(errors.DPFServerException):
    with pytest.raises(Exception):
        dpf.core.Operator("not-an-operator", server=server_type)


def test_connect_field_operator(server_type):
    op = dpf.core.Operator("min_max", server=server_type)
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    fOut = op.get_output(0, dpf.core.types.field)
    assert np.allclose(fOut.data, [1.0, 2.0, 3.0])
    fOut = op.get_output(1, dpf.core.types.field)
    assert np.allclose(fOut.data, [7.0, 8.0, 9.0])


def test_connect_list_operator(velocity_acceleration):
    model = dpf.core.Model(velocity_acceleration)
    op = model.operator("U")
    op.connect(0, [1, 2])
    fcOut = op.get_output(0, dpf.core.types.fields_container)
    assert fcOut.get_available_ids_for_label() == [1, 2]


def test_connect_list_operator_builtin(velocity_acceleration):
    model = dpf.core.Model(velocity_acceleration)
    disp = model.results.displacement()
    disp.inputs.time_scoping([1, 2])
    fields = disp.outputs.fields_container()
    assert fields.get_available_ids_for_label() == [1, 2]


def test_connect_fieldscontainer_operator(server_type):
    op = dpf.core.Operator("min_max_fc", server=server_type)
    fc = dpf.core.FieldsContainer(server=server_type)
    fc.labels = ["time", "complex"]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = list(range(1, 11))
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0}
        field = dpf.core.Field(nentities=10, server=server_type)
        field.scoping = scop
        field.data = np.zeros(len(field.scoping) * 3)
        fc.add_field(mscop, field)
    op.connect(0, fc)
    fOut = op.get_output(0, dpf.core.types.field)
    assert fOut.data.size == 60


def test_connect_bool_operator(server_type):
    op = dpf.core.Operator("S", server=server_type)
    op.connect(5, True)


def test_print_operator():
    op = dpf.core.Operator("S")
    assert str(op)


def test_connect_get_out_all_types_operator(server_type):
    forward = ops.utility.forward(server=server_type)
    to_connect = (
        [
            1,
            1.5,
            "hello",
            True,
            dpf.core.Field(server=server_type),
            # dpf.core.PropertyField(server=server_type),
            dpf.core.FieldsContainer(server=server_type),
            dpf.core.MeshesContainer(server=server_type),
            dpf.core.ScopingsContainer(server=server_type),
            dpf.core.DataSources("file.rst", server=server_type),
            # dpf.core.CyclicSupport(server=server_type),
            # dpf.core.MeshedRegion(server=server_type),
            dpf.core.TimeFreqSupport(server=server_type),
            dpf.core.Workflow(server=server_type),
            dpf.core.DataTree(server=server_type),
            # dpf.core.GenericDataContainer(server=server_type),  # Fails for LegacyGrpc
            dpf.core.StringField(server=server_type),
            dpf.core.CustomTypeField(np.float64, server=server_type),
        ]
        if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0
        else [
            1,
            1.5,
            "hello",
            True,
            dpf.core.Field(server=server_type),
            # dpf.core.PropertyField(server=server_type),
            dpf.core.FieldsContainer(server=server_type),
            dpf.core.MeshesContainer(server=server_type),
            dpf.core.ScopingsContainer(server=server_type),
            dpf.core.DataSources("file.rst", server=server_type),
            # dpf.core.CyclicSupport(server=server_type),
            # dpf.core.MeshedRegion(server=server_type),
            dpf.core.TimeFreqSupport(server=server_type),
            dpf.core.Workflow(server=server_type),
            dpf.core.DataTree(server=server_type),
        ]
        if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0
        else [
            1,
            1.5,
            "hello",
            True,
            dpf.core.Field(server=server_type),
            # dpf.core.PropertyField(server=server_type),
            dpf.core.FieldsContainer(server=server_type),
            dpf.core.MeshesContainer(server=server_type),
            dpf.core.ScopingsContainer(server=server_type),
            dpf.core.DataSources("file.rst", server=server_type),
            # dpf.core.CyclicSupport(server=server_type),
            # dpf.core.MeshedRegion(server=server_type),
            dpf.core.TimeFreqSupport(server=server_type),
            dpf.core.Workflow(server=server_type),
        ]
        if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0
        else [
            1,
            1.5,
            "hello",
            True,
            dpf.core.Field(server=server_type),
            # dpf.core.PropertyField(server=server_type),
            dpf.core.FieldsContainer(server=server_type),
            dpf.core.MeshesContainer(server=server_type),
            dpf.core.ScopingsContainer(server=server_type),
            dpf.core.DataSources("file.rst", server=server_type),
        ]
    )

    for i, data in enumerate(to_connect):
        forward.connect(i, data)
    for i, data in enumerate(to_connect):
        assert forward.get_output(i, type(data)) is not None


def test_connect_scoping_operator(server_type):
    op = dpf.core.Operator("Rescope", server=server_type)
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = list(range(1, 11))
    field = dpf.core.Field(nentities=10, server=server_type)
    field.scoping = scop
    field.data = np.zeros(len(field.scoping) * 3)
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = list(range(1, 11))
    scop2 = dpf.core.Scoping(server=server_type)
    scop2.ids = list(range(1, 5))
    op.connect(0, field)
    op.connect(1, scop2)
    fOut = op.get_output(0, dpf.core.types.field)
    scopOut = fOut.scoping
    assert np.allclose(scopOut.ids, list(range(1, 5)))


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="Copying data is " "supported starting server version 5.0",
)
def test_connect_label_space_operator(server_type):
    op = dpf.core.Operator("Rescope", server=server_type)
    dic = {"time": 1, "complex": 0}
    op.connect(0, dic)


def test_connect_datasources_operator(fields_container_csv, server_type):
    op = dpf.core.Operator("csv_to_field", server=server_type)
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(fields_container_csv)
    op.connect(4, data_sources)
    fcOut = op.get_output(0, dpf.core.types.fields_container)
    assert len(fcOut.get_available_ids_for_label()) == 4


def test_connect_operator_operator(server_type):
    op = dpf.core.Operator("norm", server=server_type)
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    op2 = dpf.core.Operator("component_selector", server=server_type)
    op2.connect(0, op, 0)
    op2.connect(1, 0)
    fOut = op2.get_output(0, dpf.core.types.field)
    assert len(fOut.data) == 3
    op2 = dpf.core.Operator("component_selector", server=server_type)

    # attempt to connect without specifying a pin
    # with pytest.raises(Exception):
    #     op2.connect(0, op)

    op2.connect(0, op)
    op2.connect(1, 0)
    fOut = op2.get_output(0, dpf.core.types.field)
    assert len(fOut.data) == 3


def test_connect_operator_output_operator(server_type):
    op = dpf.core.Operator("norm", server=server_type)
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    op2 = dpf.core.Operator("component_selector", server=server_type)
    op2.connect(0, op, 0)
    op2.connect(1, 0)
    fOut = op2.get_output(0, dpf.core.types.field)
    assert len(fOut.data) == 3
    op2 = dpf.core.Operator("component_selector", server=server_type)

    # attempt to connect without specifying a pin
    # with pytest.raises(Exception):
    #     op2.connect(0, op)

    op2.connect(0, op.outputs.field)
    op2.connect(1, 0)
    fOut = op2.get_output(0, dpf.core.types.field)
    assert len(fOut.data) == 3


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_2,
    reason="Connect an operator as an input is supported starting server version 6.2",
)
def test_connect_operator_as_input(server_type):
    op_for_each = dpf.core.Operator("for_each", server=server_type)
    fieldify = dpf.core.Operator("fieldify", server=server_type)
    op_merge = dpf.core.Operator("incremental::merge::field", server=server_type)

    op_for_each.connect_operator_as_input(0, fieldify)
    op_for_each.connect(1, [1.0, 2.0, 3.0, 4.0])
    op_for_each.connect(3, op_merge, 0)
    op_merge.connect(0, fieldify, 0)
    op_merge.connect(-2, True)

    op_for_each.run()
    assert op_for_each.get_output(3, dpf.core.types.field).get_entity_data(0) == 10.0


def test_eval_operator(server_type):
    op = dpf.core.Operator("min_max", server=server_type)
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = range(1, 10)
    scop = dpf.core.Scoping(server=server_type)
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
    assert "data_sources" in str(op.inputs)
    assert "fields_container" in str(op.outputs)

    support = model.operator("mapdl::rst::support_provider_cyclic")
    expand = model.operator("cyclic_expansion")
    expand.inputs.connect(support.outputs)
    expand.inputs.connect(op.outputs)
    mesh = model.operator("cyclic_expansion_mesh")
    mesh.inputs.cyclic_support.connect(support.outputs.cyclic_support)

    meshed_region = mesh.outputs.meshed_region()
    coord = meshed_region.nodes.coordinates_field
    assert coord.shape == (meshed_region.nodes.n_nodes, 3)
    assert (
        meshed_region.elements.connectivities_field.data.size
        == meshed_region.elements.connectivities_field.size
    )


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
    op = dpf.core.Operator("mapdl::rst::U")
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


def test_inputs_int_operator(cyclic_lin_rst, cyclic_ds, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    op = dpf.core.Operator("mapdl::rst::U", server=server_type)
    op.inputs.connect(data_sources)
    op.inputs.read_cyclic.connect(1)
    support = dpf.core.Operator("mapdl::rst::support_provider_cyclic", server=server_type)
    support.inputs.connect(data_sources)
    expand = dpf.core.Operator("cyclic_expansion", server=server_type)
    expand.inputs.connect(support.outputs.cyclic_support)
    expand.inputs.connect(op.outputs.fields_container)
    fc = expand.outputs.fields_container()
    assert isinstance(fc, dpf.core.FieldsContainer)


def test_outputs_bool_operator(server_type):
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op = dpf.core.Operator("AreFieldsIdentical", server=server_type)
    op.inputs.fieldA(inpt)
    op.inputs.fieldB(inpt)
    out = op.outputs.boolean()
    assert out is True


def find_mapdl():
    try:
        path = get_ansys_path()
        if dpf.core.SERVER.os == "nt":
            exe = os.path.join(path, "ansys", "bin", "winx64", "ANSYS.exe")
            return os.path.isfile(exe)
        else:
            return False

        return True
    except:
        return False


@pytest.mark.skipif(not find_mapdl(), reason="requires mapdl solver in install")
def test_inputs_outputs_datasources_operator(cyclic_ds, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(cyclic_ds)
    op = dpf.core.Operator("mapdl::run", server=server_type)
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
    assert u.get_available_ids_for_label() == ux.get_available_ids_for_label()
    assert u.get_available_ids_for_label() == uy.get_available_ids_for_label()
    assert u.get_available_ids_for_label() == uz.get_available_ids_for_label()
    size_tot = u[0].data.size
    assert size_tot / 3 == len(ux[0].data)
    assert size_tot / 3 == len(uy[0].data)
    assert size_tot / 3 == len(uz[0].data)

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


def test_inputs_outputs_list_operator(cyclic_lin_rst, cyclic_ds, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    op = dpf.core.Operator("mapdl::rst::U", server=server_type)
    op.inputs.connect(data_sources)
    op.inputs.time_scoping.connect([1, 2, 3, 8])
    fc = op.outputs.fields_container()
    assert fc.get_available_ids_for_label() == [1, 2, 3, 8]


def test_inputs_outputs_scopings_container(allkindofcomplexity):
    data_sources = dpf.core.DataSources(allkindofcomplexity)
    model = dpf.core.Model(data_sources)
    op = dpf.core.Operator("scoping::by_property")
    op.inputs.mesh.connect(model.metadata.meshed_region)
    sc = op.outputs.mesh_scoping()
    assert len(sc) == 4
    assert sc.labels == ["elshape"]
    scop = sc.get_scoping({"elshape": 1})
    assert len(scop.ids) == 9052
    assert scop.location == dpf.core.locations.elemental

    stress = model.results.stress()
    stress.inputs.connect(op.outputs)
    fc = stress.outputs.fields_container()
    assert fc.labels == ["elshape", "time"]
    assert len(fc) == 4

    stress.inputs.connect(sc)
    fc = stress.outputs.fields_container()
    assert fc.labels == ["elshape", "time"]
    assert len(fc) == 4

    stress.inputs.connect(op.outputs.mesh_scoping)
    fc = stress.outputs.fields_container()
    assert fc.labels == ["elshape", "time"]
    assert len(fc) == 4


def test_inputs_outputs_meshes_container(allkindofcomplexity):
    data_sources = dpf.core.DataSources(allkindofcomplexity)
    model = dpf.core.Model(data_sources)
    op = dpf.core.Operator("split_mesh")
    op.inputs.mesh.connect(model.metadata.meshed_region)
    op.inputs.property("elshape")
    mc = op.get_output(0, dpf.core.types.meshes_container)
    assert len(mc) == 4
    assert mc.labels == ["body", "elshape"]
    mesh = mc.get_mesh({"elshape": 1})
    assert len(mesh.nodes.scoping.ids) == 14826

    opsc = dpf.core.Operator("scoping::by_property")
    opsc.inputs.mesh.connect(model.metadata.meshed_region)
    sc = opsc.outputs.mesh_scoping()

    stress = model.results.stress()
    stress.inputs.connect(op.outputs)
    stress.inputs.connect(opsc.outputs)
    fc = stress.outputs.fields_container()
    assert fc.labels == ["body", "elshape", "time"]
    assert len(fc) == 4

    stress.inputs.connect(mc)
    fc = stress.outputs.fields_container()
    assert fc.labels == ["body", "elshape", "time"]
    assert len(fc) == 4
    if hasattr(op.outputs, "mesh_controller"):
        stress.inputs.connect(op.outputs.mesh_controller)
    else:
        stress.inputs.connect(op.outputs.meshes)

    fc = stress.outputs.fields_container()
    assert fc.labels == ["body", "elshape", "time"]
    assert len(fc) == 4


def test_inputs_connect_op(allkindofcomplexity, server_type):
    model = dpf.core.Model(allkindofcomplexity, server=server_type)
    u = model.results.displacement()
    norm = dpf.core.Operator("norm_fc", server=server_type)
    norm.inputs.connect(u)
    fc = norm.outputs.fields_container()
    assert len(fc) == 1
    assert fc[0].data[0] == 1.1118681761302609e-05
    norm.inputs.fields_container.connect(u)
    fc = norm.outputs.fields_container()
    assert len(fc) == 1
    assert fc[0].data[0] == 1.1118681761302609e-05


def test_connect_time_scoping(plate_msup, server_type):
    model = dpf.core.Model(plate_msup, server=server_type)
    u = model.results.displacement()
    u.inputs.time_scoping.connect(0.015)
    fc = u.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [5.12304110e-14, 3.64308310e-04, 5.79805917e-06])
    u.inputs.time_scoping.connect(0.025)
    fc = u.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [1.50367127e-13, 8.96539310e-04, 1.62125644e-05])
    u.inputs.time_scoping.connect([0.015, 0.025])
    fc = u.outputs.fields_container()
    assert len(fc) == 2
    assert np.allclose(fc[0].data[0], [5.12304110e-14, 3.64308310e-04, 5.79805917e-06])
    assert np.allclose(fc[1].data[0], [1.50367127e-13, 8.96539310e-04, 1.62125644e-05])
    u.inputs.time_scoping.connect(1)
    fc = u.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [1.62364553e-14, 1.47628321e-04, 1.96440004e-06])


def test_connect_model(plate_msup, server_type):
    model = dpf.core.Model(plate_msup, server=server_type)
    u = dpf.core.Operator("U", server=server_type)
    u.inputs.connect(model)
    u.inputs.time_scoping.connect(0.015)
    fc = u.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [5.12304110e-14, 3.64308310e-04, 5.79805917e-06])
    u.inputs.data_sources(model)
    fc = u.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [5.12304110e-14, 3.64308310e-04, 5.79805917e-06])
    u.connect(4, model)
    fc = u.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [5.12304110e-14, 3.64308310e-04, 5.79805917e-06])


def test_operator_several_output_types_remote(plate_msup, server_type_remote_process):
    inpt = dpf.core.Field(nentities=3, server=server_type_remote_process)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"
    op = dpf.core.Operator("unit_convert", server=server_type_remote_process)
    op.inputs.entity_to_convert(inpt)
    op.inputs.unit_name("mm")
    f = op.outputs.converted_entity_as_field()
    assert f.unit == "mm"
    assert np.allclose(f.data.flatten("C"), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) * 1000)

    model = dpf.core.Model(plate_msup, server=server_type_remote_process)
    din = model.metadata.meshed_region.nodes.coordinates_field.data

    assert model.metadata.meshed_region.nodes.coordinates_field.unit == "m"

    op.inputs.entity_to_convert(model.metadata.meshed_region)
    op.inputs.unit_name("mm")
    m = op.outputs.converted_entity_as_meshed_region()

    assert m.nodes.coordinates_field.unit == "mm"
    assert np.allclose(m.nodes.coordinates_field.data, np.array(din) * 1000)


def test_create_operator_config(server_type):
    conf = dpf.core.Config(server=server_type)
    assert conf.config_option_documentation("mutex") == ""
    assert conf.available_config_options == []
    conf.set_config_option("mutex", 3)
    assert conf.config_option_documentation("mutex") == ""
    assert conf.available_config_options == ["mutex"]
    assert conf.options == {"mutex": "3"}


def test_operator_config(server_type):
    # print("---> CREATING OPERATOR <----")
    op = dpf.core.Operator("min_max", server=server_type)
    # print("---> CALLING OP.CONFIG <----")
    conf = op.config
    assert hasattr(conf, "get_mutex_option")
    assert hasattr(conf, "set_mutex_option")
    # print("==============test===================")
    # print("Conf", conf)
    # print("Conf.mutex", conf.config_option_documentation("mutex"))
    assert "multiple threads" in conf.config_option_documentation("mutex")
    assert conf.config_option_value("mutex") == "false"
    assert conf.get_mutex_option() == "false"
    conf.set_mutex_option(True)
    assert conf.config_option_value("mutex") == "true"
    assert conf.get_mutex_option() == "true"
    assert conf.config_option_default_value("mutex") == "false"
    assert conf.config_option_accepted_types("mutex") == ["bool"]
    assert conf.options["mutex"] == "true"


def test_operator_config_2(server_type):
    op = dpf.core.Operator("add_fc", server=server_type)
    conf = op.config
    assert hasattr(conf, "get_mutex_option")
    assert hasattr(conf, "set_mutex_option")
    assert "multiple threads" in conf.config_option_documentation("mutex")
    assert conf.config_option_value("mutex") == "false"
    assert conf.get_mutex_option() == "false"
    conf.set_mutex_option(True)
    assert conf.config_option_value("mutex") == "true"
    assert conf.get_mutex_option() == "true"
    assert conf.config_option_default_value("mutex") == "false"
    assert conf.config_option_accepted_types("mutex") == ["bool"]
    assert conf.options["mutex"] == "true"

    assert conf.get_work_by_index_option() == "false"
    conf.set_work_by_index_option(True)
    assert conf.get_work_by_index_option() == "true"

    assert conf.get_run_in_parallel_option() == "true"
    conf.set_run_in_parallel_option(False)
    assert conf.get_run_in_parallel_option() == "false"

    assert conf.get_binary_operation_option() == "1"
    conf.set_binary_operation_option(2)
    assert conf.get_binary_operation_option() == "2"


def test_operator_set_config(server_type):
    inpt = dpf.core.Field(nentities=3, server=server_type)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"

    inpt2 = dpf.core.Field(nentities=3, server=server_type)
    inpt2.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt2.scoping.ids = [3, 4, 5]
    inpt2.unit = "m"

    conf = dpf.core.Config("add", server=server_type)
    # print(conf)
    conf.set_work_by_index_option(True)
    op = dpf.core.Operator("add", conf, server=server_type)
    op.inputs.fieldA.connect(inpt)
    op.inputs.fieldB.connect(inpt2)
    out = op.outputs.field()
    assert np.allclose(out.data, np.array([[2.0, 4.0, 6.0], [8.0, 10.0, 12.0], [14.0, 16.0, 18.0]]))

    conf.set_work_by_index_option(False)
    op = dpf.core.Operator("add", conf, server=server_type)
    op.inputs.fieldA.connect(inpt)
    op.inputs.fieldB.connect(inpt2)
    out = op.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2, 3, 4, 5])
    assert np.allclose(
        out.data,
        np.array(
            [
                [1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [8.0, 10.0, 12.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 9.0],
            ]
        ),
    )

    inpt2.unit = "Pa"
    conf = dpf.core.Operator.default_config("add", server=server_type)
    conf.set_permissive_option(True)
    op.config = conf
    op.inputs.fieldB.connect(inpt2)
    out = op.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2, 3, 4, 5])
    assert np.allclose(
        out.data,
        np.array(
            [
                [1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [8.0, 10.0, 12.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 9.0],
            ]
        ),
    )


@conftest.raises_for_servers_version_under("3.0")
def test_connect_get_output_int_list_operator(server_type):
    d = list(range(0, 100000))
    op = dpf.core.operators.utility.forward(d, server=server_type)
    d_out = op.get_output(0, dpf.core.types.vec_int)
    assert np.allclose(d, d_out)


@conftest.raises_for_servers_version_under("5.0")
def test_connect_get_output_string_list_operator(server_clayer):
    d = ["hello", "bye"]
    dpf.core.operators.utility.forward(d, server=server_clayer)


def test_connect_result(plate_msup, server_type):
    model = dpf.core.Model(plate_msup, server=server_type)
    stress = model.results.stress
    eqv = ops.invariant.von_mises_eqv_fc(stress, server=server_type)
    out = eqv.outputs.fields_container()
    eqv = ops.invariant.von_mises_eqv_fc(server=server_type)
    eqv.inputs.fields_container.connect(stress)
    out2 = eqv.outputs.fields_container()
    assert len(out) == len(out2)
    eqv = ops.invariant.von_mises_eqv_fc(server=server_type)
    eqv.inputs.connect(stress)
    out2 = eqv.outputs.fields_container()
    assert len(out) == len(out2)


def test_connect_result2(plate_msup, server_type):
    model = dpf.core.Model(plate_msup, server=server_type)
    disp = model.results.displacement
    norm = ops.math.norm_fc(disp, server=server_type)
    out = norm.outputs.fields_container()
    norm = ops.math.norm_fc(server=server_type)
    norm.inputs.fields_container.connect(disp)
    out2 = norm.outputs.fields_container()
    assert len(out) == len(out2)
    norm = ops.math.norm_fc(server=server_type)
    norm.inputs.connect(disp)
    out2 = norm.outputs.fields_container()
    assert len(out) == len(out2)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Bug in server version lower than 3.0",
)
def test_connect_get_output_int_list_operator(server_type):
    d = list(range(0, 1000000))
    op = dpf.core.operators.utility.forward(d, server=server_type)
    d_out = op.get_output(0, dpf.core.types.vec_int)
    assert np.allclose(d, d_out)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Bug in server version lower than 3.0",
)
def test_connect_get_output_double_list_operator(server_type):
    d = list(np.ones(1000000))
    op = dpf.core.operators.utility.forward(d, server=server_type)
    d_out = op.get_output(0, dpf.core.types.vec_double)
    assert np.allclose(d, d_out)


@conftest.raises_for_servers_version_under("4.0")
def test_connect_get_output_data_tree_operator(server_type):
    d = dpf.core.DataTree({"name": "Paul"}, server=server_type)
    op = dpf.core.operators.utility.forward(d, server=server_type)
    d_out = op.get_output(0, dpf.core.types.data_tree)
    assert d_out.get_as("name") == "Paul"


@conftest.raises_for_servers_version_under("7.0")
def test_connect_get_output_generic_data_container_operator(server_clayer):
    gdc = dpf.core.GenericDataContainer(server=server_clayer)
    gdc.set_property("n", 1)
    op = dpf.core.operators.utility.forward(gdc, server=server_clayer)
    gdc_out = op.get_output(0, dpf.core.types.generic_data_container)
    assert gdc_out.get_property("n") == 1


def test_operator_several_output_types_copy(plate_msup):
    inpt = dpf.core.Field(nentities=3)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"
    op = dpf.core.Operator("unit_convert")
    op.inputs.entity_to_convert(inpt)
    op.inputs.unit_name("mm")
    f = op.outputs.converted_entity_as_field()
    assert f.unit == "mm"
    assert np.allclose(f.data.flatten("C"), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) * 1000)

    model = dpf.core.Model(plate_msup)
    din = copy.deepcopy(model.metadata.meshed_region.nodes.coordinates_field.data)

    assert model.metadata.meshed_region.nodes.coordinates_field.unit == "m"

    op.inputs.entity_to_convert(model.metadata.meshed_region)
    op.inputs.unit_name("mm")
    m = op.outputs.converted_entity_as_meshed_region()

    assert m.nodes.coordinates_field.unit == "mm"
    assert np.allclose(m.nodes.coordinates_field.data, np.array(din) * 1000)


def test_operator_several_output_types2(server_type):
    inpt = dpf.core.Field(nentities=3, server=server_type)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"
    uc = dpf.core.Operator("Rescope", server=server_type)
    uc.inputs.fields(inpt)
    uc.inputs.mesh_scoping(dpf.core.Scoping(ids=[1, 2], server=server_type))
    f = uc.outputs.fields_as_field()
    assert np.allclose(f.data.flatten("C"), [1, 2, 3, 4, 5, 6])

    fc = dpf.core.FieldsContainer(server=server_type)
    fc.labels = ["time"]
    fc.add_field({"time": 1}, inpt)

    uc.inputs.fields(fc)
    fc2 = uc.outputs.fields_as_fields_container()
    assert np.allclose(fc2[0].data.flatten("C"), [1, 2, 3, 4, 5, 6])


def test_add_operator_operator(server_type):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=server_type)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    ####forward field
    # operator with field out
    forward = ops.utility.forward_field(field, server=server_type)
    add = forward + forward
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)

    # operator + field
    add = forward + field
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)

    # operator + list
    add = forward + [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, field.data + np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]))

    # operator + float
    add = forward + 1.0
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))

    ####forward fields container
    # operator with field out
    forward = ops.utility.forward_fields_container(field, server=server_type)
    add = forward + forward
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)

    # operator + field
    add = forward + field
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)

    # operator + list
    add = forward + [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, field.data + np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]))

    # operator + float
    add = forward + 1.0
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))


def test_minus_operator_operator(server_type):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=server_type)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    ####forward field
    # operator with field out
    forward = ops.utility.forward_field(field, server=server_type)
    add = forward - forward
    assert type(add) == ops.math.minus_fc
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.zeros((2, 3)))

    # operator - field
    add = forward - field
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.zeros((2, 3)))

    # operator - list
    add = forward - [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[0.0, 0.0, 0.0], [3.0, 3.0, 3.0]]))

    # operator - float
    add = forward - 1.0
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[-1.0, 0.0, 1.0], [2.0, 3.0, 4.0]]))

    ####forward fields container
    # operator with field out
    forward = ops.utility.forward_fields_container(field, server=server_type)
    add = forward - forward
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.zeros((2, 3)))

    # operator- field
    add = forward - field
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.zeros((2, 3)))

    # operator - list
    add = forward - [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[0.0, 0.0, 0.0], [3.0, 3.0, 3.0]]))

    # operator - float
    add = forward - 1.0
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([[-1.0, 0.0, 1.0], [2.0, 3.0, 4.0]]))


def test_dot_operator_operator(server_type):
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=server_type)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    ####forward field
    # operator with field out
    forward = ops.utility.forward_field(field, server=server_type)
    add = forward * forward
    assert type(add) == ops.math.generalized_inner_product_fc
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # operator * field
    add = forward * field
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # operator * list
    add = forward * [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 14.0]))

    # operator * float
    add = forward * -1.0
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, -field.data)

    ####forward fields container
    # operator with field out
    forward = ops.utility.forward_fields_container(field, server=server_type)
    add = forward * forward
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # operator* field
    add = forward * field
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # operator * list
    add = forward * [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, np.array([5.0, 14.0]))

    # operator * float
    add = forward * -1.0
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert np.allclose(out[0].scoping.ids, [1, 2])
    assert np.allclose(out[0].data, -field.data)


@conftest.raises_for_servers_version_under("3.0")
def test_list_operators(server_type):
    l = dpf.core.dpf_operator.available_operator_names(server=server_type)
    assert len(l) > 400
    assert "merge::result_info" in l
    assert "unit_convert" in l
    assert "stream_provider" in l


@conftest.raises_for_servers_version_under("3.0")
def test_get_static_spec_operator(server_type_legacy_grpc):
    l = dpf.core.dpf_operator.available_operator_names(server=server_type_legacy_grpc)
    for i, name in enumerate(l):
        spec = dpf.core.Operator.operator_specification(name, server=server_type_legacy_grpc)
        assert len(spec.operator_name) > 0
        assert len(spec.inputs) > 0
        assert len(spec.description) > 0


@conftest.raises_for_servers_version_under("4.0")
def test_get_static_spec_operator_in_proc(server_clayer):
    if isinstance(server_clayer, dpf.core.server_types.GrpcServer):
        return
    l = dpf.core.dpf_operator.available_operator_names(server=server_clayer)
    for i, name in enumerate(l):
        spec = dpf.core.Operator.operator_specification(name, server=server_clayer)
        assert len(spec.operator_name) > 0
        l = len(spec.inputs)
        d = spec.description


@conftest.raises_for_servers_version_under("3.0")
def test_with_progress_operator(allkindofcomplexity, server_type_legacy_grpc):
    model = dpf.core.Model(allkindofcomplexity, server=server_type_legacy_grpc)
    op = model.results.stress()
    op.inputs.read_cyclic(3)
    opnorm = dpf.core.operators.averaging.to_nodal_fc(op, server=server_type_legacy_grpc)
    add = dpf.core.operators.math.add_fc(opnorm, opnorm, server=server_type_legacy_grpc)
    add2 = dpf.core.operators.math.add_fc(add, add, server=server_type_legacy_grpc)
    add3 = dpf.core.operators.math.add_fc(add2, server=server_type_legacy_grpc)
    add4 = dpf.core.operators.math.add_fc(add3, add3, server=server_type_legacy_grpc)
    add4.progress_bar = True
    fc = add4.outputs.fields_container()
    assert len(fc) == 2


@conftest.raises_for_servers_version_under("4.0")
def test_with_progress_operator_in_proc(allkindofcomplexity, server_clayer):
    if isinstance(server_clayer, dpf.core.server_types.GrpcServer):
        return
    model = dpf.core.Model(allkindofcomplexity, server=server_clayer)
    op = model.results.stress()
    op.inputs.read_cyclic(3)
    opnorm = dpf.core.operators.averaging.to_nodal_fc(op, server=server_clayer)
    add = dpf.core.operators.math.add_fc(opnorm, opnorm, server=server_clayer)
    add2 = dpf.core.operators.math.add_fc(add, add, server=server_clayer)
    add3 = dpf.core.operators.math.add_fc(add2, server=server_clayer)
    add4 = dpf.core.operators.math.add_fc(add3, add3, server=server_clayer)
    add4.progress_bar = True
    fc = add4.outputs.fields_container()
    assert len(fc) == 2


@conftest.raises_for_servers_version_under("3.0")
def test_list_operators(server_type_legacy_grpc):
    l = dpf.core.dpf_operator.available_operator_names(server=server_type_legacy_grpc)
    assert len(l) > 400
    assert "merge::result_info" in l
    assert "unit_convert" in l
    assert "stream_provider" in l


@conftest.raises_for_servers_version_under("3.0")
def test_get_static_spec_operator(server_type_legacy_grpc):
    l = dpf.core.dpf_operator.available_operator_names(server=server_type_legacy_grpc)
    for i, name in enumerate(l):
        spec = dpf.core.Operator.operator_specification(name, server=server_type_legacy_grpc)
        assert len(spec.operator_name) > 0
        assert len(spec.inputs) > 0
        assert len(spec.description) > 0


@conftest.raises_for_servers_version_under("3.0")
def test_with_progress_operator(allkindofcomplexity, server_type):
    model = dpf.core.Model(allkindofcomplexity, server=server_type)
    op = model.results.stress()
    op.inputs.read_cyclic(3)
    opnorm = dpf.core.operators.averaging.to_nodal_fc(op, server=server_type)
    add = dpf.core.operators.math.add_fc(opnorm, opnorm, server=server_type)
    add2 = dpf.core.operators.math.add_fc(add, add, server=server_type)
    add3 = dpf.core.operators.math.add_fc(add2, server=server_type)
    add4 = dpf.core.operators.math.add_fc(add3, add3, server=server_type)
    add4.progress_bar = True
    fc = add4.outputs.fields_container()
    assert len(fc) == 2


def test_operator_specification_simple(server_type):
    spec = Specification(operator_name="U", server=server_type)
    assert "displacement" in spec.description
    assert "result file path" in spec.inputs[4].document
    assert "field" in spec.outputs[0].type_names[0]


def test_operator_specification_none(server_type):
    op = dpf.core.Operator("mapdl::rst::thickness", server=server_type)
    assert op.specification.description == ""
    assert op.specification.inputs == {}
    assert op.specification.outputs == {}
    assert op.specification.properties == {}
    inputs_dir = dir(op.inputs)
    for i in inputs_dir:
        if not i[0] == "_":
            assert False
    outputs_dir = dir(op.outputs)
    for i in outputs_dir:
        if not i[0] == "_":
            assert False


@conftest.raises_for_servers_version_under("3.0")
def test_generated_operator_specification(server_type):
    op = ops.result.displacement(server=server_type)
    spec = op.specification
    assert spec is not None
    assert "displacement" in spec.description
    assert "path" in spec.inputs[4].document


def test_operator_config_specification_simple(server_type):
    spec = Specification(operator_name="add", server=server_type)
    conf_spec = spec.config_specification
    if server_type.os != "posix":
        assert (
            "enum dataProcessing::EBinaryOperation"
            or "binary_operation_enum" in conf_spec["binary_operation"].type_names
        )
    elif SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_2:
        assert "binary_operation_enum" in conf_spec["binary_operation"].type_names
    assert conf_spec["binary_operation"].default_value_str == "1"
    assert "Intersection" in conf_spec["binary_operation"].document
    assert "run_in_parallel" in conf_spec
    assert "index" in conf_spec["work_by_index"].document
    assert "id" in conf_spec["work_by_index"].document


def test_generated_operator_config_specification_simple(server_type):
    op = ops.math.add(server=server_type)
    spec = op.specification
    conf_spec = spec.config_specification
    if server_type.os != "posix":
        assert (
            "enum dataProcessing::EBinaryOperation"
            or "binary_operation_enum" in conf_spec["binary_operation"].type_names
        )
    elif SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_2:
        assert "binary_operation_enum" in conf_spec["binary_operation"].type_names
    assert conf_spec["binary_operation"].default_value_str == "1"
    assert "Intersection" in conf_spec["binary_operation"].document
    assert "run_in_parallel" in conf_spec
    assert "index" in conf_spec["work_by_index"].document
    assert "id" in conf_spec["work_by_index"].document


def test_operator_exception():
    ds = dpf.core.DataSources(r"dummy/file.rst")
    op = ops.result.displacement(data_sources=ds)
    with pytest.raises(errors.DPFServerException):
        op.eval()


def test_delete_operator(server_type):
    op = dpf.core.Operator("min_max", server=server_type)
    op = None
    with pytest.raises(Exception):
        op.connect(0, 1)


def test_memory_outputs_operator(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress_fc = model.results.stress().eqv().eval()
    assert len(stress_fc) == 2


def test_delete_auto_operator(server_type):
    op = dpf.core.Operator("min_max", server=server_type)

    op_ref = weakref.ref(op)

    op = None
    gc.collect()
    assert op_ref() is None


def deep_copy_using_operator(dpf_entity, server, stream_type=1):
    from ansys.dpf.core.operators.serialization import serializer_to_string, string_deserializer

    serializer = serializer_to_string(server=server)
    serializer.connect(-1, stream_type)
    serializer.connect(1, dpf_entity)
    if stream_type == 1:
        s_out = serializer.get_output(0, dpf.core.types.bytes)
    else:
        s_out = serializer.get_output(0, dpf.core.types.string)
    deserializer = string_deserializer(server=server)
    deserializer.connect(-1, stream_type)
    deserializer.connect(0, s_out)
    str_out = deserializer.get_output(1, dpf.core.types.string)
    return str_out


@conftest.raises_for_servers_version_under("8.0")
def test_connect_get_non_ascii_string_bytes(server_type):
    stream_type = 1
    str = "\N{GREEK CAPITAL LETTER DELTA}"
    str_out = deep_copy_using_operator(str, server_type, stream_type)
    assert str == str_out


def test_connect_get_non_ascii_string(server_type):
    stream_type = 0
    str = "\N{GREEK CAPITAL LETTER DELTA}"
    str_out = deep_copy_using_operator(str, server_type, stream_type)
    assert str == str_out


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0, reason="Available for servers >=8.0"
)
def test_deep_copy_non_ascii_string(server_type):
    str = "\N{GREEK CAPITAL LETTER DELTA}"
    str_out = dpf.core.core._deep_copy(str, server_type)
    assert str == str_out


def test_output_any(server_type):
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop

    op = dpf.core.Operator("forward", server=server_type)
    op.connect(0, inpt)

    output_field = op.get_output(0, dpf.core.types.any).cast(dpf.core.Field)
    assert isinstance(output_field, dpf.core.Field)
    assert output_field.data.size == 9
    assert output_field.scoping.size == 3


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="Input of Any requires DPF 7.0 or above.",
)
def test_input_any(server_type):
    field = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    field.data = data
    field.scoping = scop
    inpt = dpf.core.Any.new_from(field)
    op = dpf.core.Operator(name="forward", server=server_type)
    op.connect(pin=0, inpt=inpt)
    output = op.get_output(pin=0, output_type=dpf.core.types.field)
    assert isinstance(output, dpf.core.Field)
    assert len(output.data_as_list) == len(data)


def test_operator_input_output_streams(server_type, simple_bar):
    data_source = dpf.core.DataSources(simple_bar, server=server_type)
    streams_op = dpf.core.operators.metadata.streams_provider(server=server_type)
    streams_op.inputs.data_sources.connect(data_source)
    streams = streams_op.outputs.streams_container()
    time_provider = dpf.core.operators.metadata.time_freq_provider(server=server_type)
    time_provider.connect(pin=3, inpt=streams)
    times = time_provider.outputs.time_freq_support()
    assert times
