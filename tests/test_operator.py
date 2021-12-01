import gc
import weakref
import os
import shutil

import numpy as np
import pytest

from ansys import dpf
from ansys.dpf.core import errors
from ansys.dpf.core import operators as ops
from ansys.dpf.core.check_version import meets_version, get_server_version
from conftest import local_server

# Check for ANSYS installation env var
HAS_AWP_ROOT212 = os.environ.get("AWP_ROOT212", False) is not False

SERVER_VERSION_HIGHER_THAN_3_0 = meets_version(get_server_version(dpf.core._global_server()), "3.0")


def test_create_operator():
    op = dpf.core.Operator("min_max")
    assert op._message.id


def test_invalid_operator_name():
    with pytest.raises(errors.DPFServerException):
        dpf.core.Operator("not-an-operator")


def test_connect_field_operator():
    op = dpf.core.Operator("min_max")
    inpt = dpf.core.Field(nentities=3)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping()
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


def test_connect_fieldscontainer_operator():
    op = dpf.core.Operator("min_max_fc")
    fc = dpf.core.FieldsContainer()
    fc.labels = ["time", "complex"]
    scop = dpf.core.Scoping()
    scop.ids = list(range(1, 11))
    for i in range(0, 20):
        mscop = {"time": i + 1, "complex": 0}
        field = dpf.core.Field(nentities=10)
        field.scoping = scop
        field.data = np.zeros(len(field.scoping) * 3)
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
    scop.ids = list(range(1, 11))
    field = dpf.core.Field(nentities=10)
    field.scoping = scop
    field.data = np.zeros(len(field.scoping) * 3)
    scop = dpf.core.Scoping()
    scop.ids = list(range(1, 11))
    scop2 = dpf.core.Scoping()
    scop2.ids = list(range(1, 5))
    op.connect(0, field)
    op.connect(1, scop2)
    fOut = op.get_output(0, dpf.core.types.field)
    scopOut = fOut.scoping
    assert scopOut.ids == list(range(1, 5))


def test_connect_datasources_operator(fields_container_csv):
    op = dpf.core.Operator("csv_to_field")
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(fields_container_csv)
    op.connect(4, data_sources)
    fcOut = op.get_output(0, dpf.core.types.fields_container)
    assert len(fcOut.get_available_ids_for_label()) == 4


def test_connect_operator_operator():
    op = dpf.core.Operator("norm")
    inpt = dpf.core.Field(nentities=3)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    op2 = dpf.core.Operator("component_selector")
    op2.connect(0, op, 0)
    op2.connect(1, 0)
    fOut = op2.get_output(0, dpf.core.types.field)
    assert len(fOut.data) == 3
    op2 = dpf.core.Operator("component_selector")

    # attempt to connect without specifying a pin
    # with pytest.raises(Exception):
    #     op2.connect(0, op)

    op2.connect(0, op)
    op2.connect(1, 0)
    fOut = op2.get_output(0, dpf.core.types.field)
    assert len(fOut.data) == 3


def test_connect_operator_output_operator():
    op = dpf.core.Operator("norm")
    inpt = dpf.core.Field(nentities=3)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    op2 = dpf.core.Operator("component_selector")
    op2.connect(0, op, 0)
    op2.connect(1, 0)
    fOut = op2.get_output(0, dpf.core.types.field)
    assert len(fOut.data) == 3
    op2 = dpf.core.Operator("component_selector")

    # attempt to connect without specifying a pin
    # with pytest.raises(Exception):
    #     op2.connect(0, op)

    op2.connect(0, op.outputs.field)
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


def test_inputs_int_operator(cyclic_lin_rst, cyclic_ds):
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


def test_outputs_bool_operator():
    inpt = dpf.core.Field(nentities=3)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op = dpf.core.Operator("AreFieldsIdentical")
    op.inputs.fieldA(inpt)
    op.inputs.fieldB(inpt)
    out = op.outputs.boolean()
    assert out == True


def find_mapdl():
    try:
        path = dpf.core.misc.find_ansys()
        if os.name == "nt":
            exe = os.path.join(path, "ansys", "bin", "winx64", "ANSYS.exe")
            return os.path.isfile(exe)
        else:
            return False

        return True
    except:
        return False


@pytest.mark.skipif(not find_mapdl(), reason="requires mapdl solver in install")
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


def test_inputs_outputs_list_operator(cyclic_lin_rst, cyclic_ds):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    op = dpf.core.Operator("mapdl::rst::U")
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


def test_inputs_connect_op(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    u = model.results.displacement()
    norm = dpf.core.Operator("norm_fc")
    norm.inputs.connect(u)
    fc = norm.outputs.fields_container()
    assert len(fc) == 1
    assert fc[0].data[0] == 1.1118681761302609e-05
    norm.inputs.fields_container.connect(u)
    fc = norm.outputs.fields_container()
    assert len(fc) == 1
    assert fc[0].data[0] == 1.1118681761302609e-05


def test_connect_time_scoping(plate_msup):
    model = dpf.core.Model(plate_msup)
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


def test_connect_model(plate_msup):
    model = dpf.core.Model(plate_msup)
    u = dpf.core.Operator("U")
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


def test_operator_several_output_types(plate_msup):
    inpt = dpf.core.Field(nentities=3)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"
    op = dpf.core.Operator("unit_convert")
    op.inputs.entity_to_convert(inpt)
    op.inputs.unit_name("mm")
    f = op.outputs.converted_entity_as_field()
    assert f.unit == "mm"
    assert np.allclose(
        f.data.flatten("C"), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) * 1000
    )

    model = dpf.core.Model(plate_msup)
    din = model.metadata.meshed_region.nodes.coordinates_field.data

    assert model.metadata.meshed_region.nodes.coordinates_field.unit == "m"

    op.inputs.entity_to_convert(model.metadata.meshed_region)
    op.inputs.unit_name("mm")
    m = op.outputs.converted_entity_as_meshed_region()

    assert m.nodes.coordinates_field.unit == "mm"
    assert np.allclose(m.nodes.coordinates_field.data, np.array(din) * 1000)


def test_operator_several_output_types2():
    inpt = dpf.core.Field(nentities=3)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"
    uc = dpf.core.Operator("Rescope")
    uc.inputs.fields(inpt)
    uc.inputs.mesh_scoping(dpf.core.Scoping(ids=[1, 2]))
    f = uc.outputs.fields_as_field()
    assert np.allclose(f.data.flatten("C"), [1, 2, 3, 4, 5, 6])

    fc = dpf.core.FieldsContainer()
    fc.labels = ["time"]
    fc.add_field({"time": 1}, inpt)

    uc.inputs.fields(fc)
    fc2 = uc.outputs.fields_as_fields_container()
    assert np.allclose(fc2[0].data.flatten("C"), [1, 2, 3, 4, 5, 6])


def test_create_operator_config():
    conf = dpf.core.Config()
    assert conf.config_option_documentation("mutex") == ""
    assert conf.available_config_options == []
    conf.set_config_option("mutex", 3)
    assert conf.config_option_documentation("mutex") == ""
    assert conf.available_config_options == ["mutex"]
    assert conf.options == {"mutex": "3"}


def test_operator_config():
    op = dpf.core.Operator("min_max")
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


def test_operator_config_2():
    op = dpf.core.Operator("add_fc")
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


def test_operator_set_config():
    inpt = dpf.core.Field(nentities=3)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"

    inpt2 = dpf.core.Field(nentities=3)
    inpt2.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt2.scoping.ids = [3, 4, 5]
    inpt2.unit = "m"

    conf = dpf.core.Config("add")
    print(conf)
    conf.set_work_by_index_option(True)
    op = dpf.core.Operator("add", conf)
    op.inputs.fieldA.connect(inpt)
    op.inputs.fieldB.connect(inpt2)
    out = op.outputs.field()
    assert np.allclose(out.data, np.array([[2., 4., 6.],
                                           [8., 10., 12.],
                                           [14., 16., 18.]]))

    conf.set_work_by_index_option(False)
    op = dpf.core.Operator("add", conf)
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
    conf = dpf.core.Operator.default_config("add")
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


def test_connect_model(plate_msup):
    model = dpf.core.Model(plate_msup)
    u = dpf.core.Operator("U")
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

@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0, reason='Requires server version higher than 3.0')
def test_connect_get_output_int_list_operator():
    d = list(range(0,10000000))
    op = dpf.core.operators.utility.forward(d)
    dout = op.get_output(0, dpf.core.types.vec_int)
    assert np.allclose(d,dout)

@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0, reason='Requires server version higher than 3.0')
def test_connect_get_output_double_list_operator():
    d = list(np.ones(10000000))
    op = dpf.core.operators.utility.forward(d)
    dout = op.get_output(0, dpf.core.types.vec_double)
    assert np.allclose(d,dout)



def test_connect_result(plate_msup):
    model = dpf.core.Model(plate_msup)
    stress = model.results.stress
    eqv = ops.invariant.von_mises_eqv_fc(stress)
    out = eqv.outputs.fields_container()
    eqv = ops.invariant.von_mises_eqv_fc()
    eqv.inputs.fields_container.connect(stress)
    out2 = eqv.outputs.fields_container()
    assert len(out) == len(out2)
    eqv = ops.invariant.von_mises_eqv_fc()
    eqv.inputs.connect(stress)
    out2 = eqv.outputs.fields_container()
    assert len(out) == len(out2)


def test_connect_result2(plate_msup):
    model = dpf.core.Model(plate_msup)
    disp = model.results.displacement
    norm = ops.math.norm_fc(disp)
    out = norm.outputs.fields_container()
    norm = ops.math.norm_fc()
    norm.inputs.fields_container.connect(disp)
    out2 = norm.outputs.fields_container()
    assert len(out) == len(out2)
    norm = ops.math.norm_fc()
    norm.inputs.connect(disp)
    out2 = norm.outputs.fields_container()
    assert len(out) == len(out2)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_connect_get_output_int_list_operator():
    d = list(range(0, 10000000))
    op = dpf.core.operators.utility.forward(d)
    dout = op.get_output(0, dpf.core.types.vec_int)
    assert np.allclose(d, dout)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_connect_get_output_double_list_operator():
    d = list(np.ones(10000000))
    op = dpf.core.operators.utility.forward(d)
    dout = op.get_output(0, dpf.core.types.vec_double)
    assert np.allclose(d, dout)
def test_operator_several_output_types(plate_msup):
    inpt = dpf.core.Field(nentities=3)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"
    op = dpf.core.Operator("unit_convert")
    op.inputs.entity_to_convert(inpt)
    op.inputs.unit_name("mm")
    f = op.outputs.converted_entity_as_field()
    assert f.unit == "mm"
    assert np.allclose(
        f.data.flatten("C"), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) * 1000
    )

    model = dpf.core.Model(plate_msup)
    din = model.metadata.meshed_region.nodes.coordinates_field.data

    assert model.metadata.meshed_region.nodes.coordinates_field.unit == "m"

    op.inputs.entity_to_convert(model.metadata.meshed_region)
    op.inputs.unit_name("mm")
    m = op.outputs.converted_entity_as_meshed_region()

    assert m.nodes.coordinates_field.unit == "mm"
    assert np.allclose(m.nodes.coordinates_field.data, np.array(din) * 1000)


def test_operator_several_output_types2():
    inpt = dpf.core.Field(nentities=3)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"
    uc = dpf.core.Operator("Rescope")
    uc.inputs.fields(inpt)
    uc.inputs.mesh_scoping(dpf.core.Scoping(ids=[1, 2]))
    f = uc.outputs.fields_as_field()
    assert np.allclose(f.data.flatten("C"), [1, 2, 3, 4, 5, 6])

    fc = dpf.core.FieldsContainer()
    fc.labels = ["time"]
    fc.add_field({"time": 1}, inpt)

    uc.inputs.fields(fc)
    fc2 = uc.outputs.fields_as_fields_container()
    assert np.allclose(fc2[0].data.flatten("C"), [1, 2, 3, 4, 5, 6])


def test_add_operator_operator():
    field = dpf.core.fields_factory.create_3d_vector_field(2)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    ####forward field
    # operator with field out
    forward = ops.utility.forward_field(field)
    add = forward + forward
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)

    # operator + field
    add = forward + field
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)

    # operator + list
    add = forward + [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(
        out[0].data, field.data + np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]])
    )

    # operator + float
    add = forward + 1.0
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))

    ####forward fields container
    # operator with field out
    forward = ops.utility.forward_fields_container(field)
    add = forward + forward
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)

    # operator + field
    add = forward + field
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)

    # operator + list
    add = forward + [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(
        out[0].data, field.data + np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]])
    )

    # operator + float
    add = forward + 1.0
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))


def test_minus_operator_operator():
    field = dpf.core.fields_factory.create_3d_vector_field(2)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    ####forward field
    # operator with field out
    forward = ops.utility.forward_field(field)
    add = forward - forward
    assert type(add) == ops.math.minus_fc
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.zeros((2, 3)))

    # operator - field
    add = forward - field
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.zeros((2, 3)))

    # operator - list
    add = forward - [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([[0.0, 0.0, 0.0], [3.0, 3.0, 3.0]]))

    # operator - float
    add = forward - 1.0
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([[-1.0, 0.0, 1.0], [2.0, 3.0, 4.0]]))

    ####forward fields container
    # operator with field out
    forward = ops.utility.forward_fields_container(field)
    add = forward - forward
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.zeros((2, 3)))

    # operator- field
    add = forward - field
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.zeros((2, 3)))

    # operator - list
    add = forward - [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([[0.0, 0.0, 0.0], [3.0, 3.0, 3.0]]))

    # operator - float
    add = forward - 1.0
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([[-1.0, 0.0, 1.0], [2.0, 3.0, 4.0]]))


def test_dot_operator_operator():
    field = dpf.core.fields_factory.create_3d_vector_field(2)
    field.data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    field.scoping.ids = [1, 2]

    ####forward field
    # operator with field out
    forward = ops.utility.forward_field(field)
    add = forward * forward
    assert type(add) == ops.math.generalized_inner_product_fc
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # operator * field
    add = forward * field
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # operator * list
    add = forward * [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([5.0, 14.0]))

    # operator * float
    add = forward * -1.0
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, -field.data)

    ####forward fields container
    # operator with field out
    forward = ops.utility.forward_fields_container(field)
    add = forward * forward
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # operator* field
    add = forward * field
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([5.0, 50.0]))

    # operator * list
    add = forward * [0.0, 1.0, 2.0]
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([5.0, 14.0]))

    # operator * float
    add = forward * -1.0
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, -field.data)
    
   
def test_add_operator_server_operator():
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.,1.,2.,3.,4.,5.]
    field.scoping.ids = [1,2]
    
    ####forward field
    #operator with field out
    forward = ops.utility.forward_field(field, server=local_server)    
    add = forward+forward
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out)==1
    assert out[0].scoping.ids == [1,2]
    assert np.allclose(out[0].data,np.array(field.data)*2.0)
    

def test_minus_operator_server_operator():
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.,1.,2.,3.,4.,5.]
    field.scoping.ids = [1,2]
    
    ####forward field
    #operator with field out
    forward = ops.utility.forward_field(field, server=local_server)    
    add = forward-forward
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out)==1
    assert out[0].scoping.ids == [1,2]
    assert np.allclose(out[0].data,np.zeros((2,3)))
     
    
def test_dot_operator_server_operator():
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0.,1.,2.,3.,4.,5.]
    field.scoping.ids = [1,2]
    
    ####forward field
    #operator with field out
    forward = ops.utility.forward_field(field, server=local_server)    
    add = forward*forward
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out)==1
    assert out[0].scoping.ids == [1,2]
    assert np.allclose(out[0].data,np.array([5.,50.]))


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0, reason='Requires server version higher than 3.0')
def test_list_operators():
    l = dpf.core.dpf_operator.available_operator_names()
    assert len(l)>400
    assert 'merge::result_info' in l    
    assert 'unit_convert' in l
    assert 'stream_provider' in l

@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0, reason='Requires server version higher than 3.0')
def test_get_static_spec_operator():
    l = dpf.core.dpf_operator.available_operator_names()
    for i,name in enumerate(l):
        spec = dpf.core.Operator.operator_specification(name)
        assert len(spec.operator_name)>0
        assert len(spec.inputs)>0
        assert len(spec.description)>0
    
@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0, reason='Requires server version higher than 3.0')
def test_with_progress_operator(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    op = model.results.stress()
    op.inputs.read_cyclic(3)    
    opnorm = dpf.core.operators.averaging.to_nodal_fc(op)
    add = dpf.core.operators.math.add_fc(opnorm,opnorm)
    add2 = dpf.core.operators.math.add_fc(add,add)
    add3 = dpf.core.operators.math.add_fc(add2)
    add4 = dpf.core.operators.math.add_fc(add3,add3)
    add4.progress_bar=True
    fc = add4.outputs.fields_container()
    assert len(fc)==2

def test_add_operator_server_operator():
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0., 1., 2., 3., 4., 5.]
    field.scoping.ids = [1, 2]

    ####forward field
    # operator with field out
    forward = ops.utility.forward_field(field, server=local_server)
    add = forward + forward
    assert isinstance(add, ops.math.add_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array(field.data) * 2.0)


def test_minus_operator_server_operator():
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0., 1., 2., 3., 4., 5.]
    field.scoping.ids = [1, 2]

    ####forward field
    # operator with field out
    forward = ops.utility.forward_field(field, server=local_server)
    add = forward - forward
    assert isinstance(add, ops.math.minus_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.zeros((2, 3)))


def test_dot_operator_server_operator():
    field = dpf.core.fields_factory.create_3d_vector_field(2, server=local_server)
    field.data = [0., 1., 2., 3., 4., 5.]
    field.scoping.ids = [1, 2]

    ####forward field
    # operator with field out
    forward = ops.utility.forward_field(field, server=local_server)
    add = forward * forward
    assert isinstance(add, ops.math.generalized_inner_product_fc)
    out = add.outputs.fields_container()
    assert len(out) == 1
    assert out[0].scoping.ids == [1, 2]
    assert np.allclose(out[0].data, np.array([5., 50.]))


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_list_operators():
    l = dpf.core.dpf_operator.available_operator_names()
    assert len(l) > 400
    assert 'merge::result_info' in l
    assert 'unit_convert' in l
    assert 'stream_provider' in l

@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_get_static_spec_operator():
    l = dpf.core.dpf_operator.available_operator_names()
    for i, name in enumerate(l):
        spec = dpf.core.Operator.operator_specification(name)
        assert len(spec.operator_name) > 0
        assert len(spec.inputs) > 0
        assert len(spec.description) > 0


def test_eval_operator(tmpdir):
    op = dpf.core.Operator("norm")
    inpt = dpf.core.Field(nentities=3)@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
    data = [0.0, 2.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0]
    scop = dpf.core.Scoping()
    for i, name in enumerate(l):
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    f = op.eval()
    data = f.data
    assert np.allclose(data, [2.0, 2.0, 2.0])

    csv = dpf.core.Operator("field_to_csv")
    csv.inputs.file_path.connect(str(tmpdir) + (r"/file.csv"))
    csv.inputs.field_or_fields_container.connect(f)
    assert csv.eval() == None


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_with_progress_operator(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    op = model.results.stress()
    op.inputs.read_cyclic(3)
    opnorm = dpf.core.operators.averaging.to_nodal_fc(op)
    add = dpf.core.operators.math.add_fc(opnorm, opnorm)
    add2 = dpf.core.operators.math.add_fc(add, add)
    add3 = dpf.core.operators.math.add_fc(add2)
    add4 = dpf.core.operators.math.add_fc(add3, add3)
    add4.progress_bar = True
    fc = add4.outputs.fields_container()
    assert len(fc) == 2


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
