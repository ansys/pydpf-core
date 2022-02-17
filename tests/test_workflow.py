import numpy as np
import pytest

import ansys.dpf.core.operators as op
import conftest
from ansys import dpf
from ansys.dpf.core.check_version import meets_version, get_server_version

SERVER_VERSION_HIGHER_THAN_3_0 = meets_version(get_server_version(dpf.core._global_server()), "3.0")


def test_create_workflow():
    wf = dpf.core.Workflow()
    assert wf._message.id


def test_connect_field_workflow():
    wf = dpf.core.Workflow()
    op = dpf.core.Operator("min_max")
    inpt = dpf.core.Field(nentities=3)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop

    wf.add_operator(op)
    wf.set_input_name("field", op, 0)
    wf.set_output_name("min", op, 0)
    wf.set_output_name("max", op, 1)
    wf.connect("field", inpt)
    fOut = wf.get_output("min", dpf.core.types.field)
    assert np.allclose(fOut.data, [1.0, 2.0, 3.0])
    fOut = wf.get_output("max", dpf.core.types.field)
    assert np.allclose(fOut.data, [7.0, 8.0, 9.0])

    wf = dpf.core.Workflow()
    wf.set_input_name("field", op.inputs.field)
    wf.set_output_name("min", op.outputs.field_min)
    wf.set_output_name("max", op.outputs.field_max)
    wf.connect("field", inpt)
    fOut = wf.get_output("min", dpf.core.types.field)
    assert np.allclose(fOut.data, [1.0, 2.0, 3.0])
    fOut = wf.get_output("max", dpf.core.types.field)
    assert np.allclose(fOut.data, [7.0, 8.0, 9.0])


def test_connect_list_workflow(velocity_acceleration):
    wf = dpf.core.Workflow()
    model = dpf.core.Model(velocity_acceleration)
    op = model.operator("U")
    wf.add_operator(op)
    wf.set_input_name("time_scoping", op, 0)
    wf.set_output_name("field", op, 0)
    wf.connect("time_scoping", [1, 2])
    fcOut = wf.get_output("field", dpf.core.types.fields_container)
    assert fcOut.get_available_ids_for_label() == [1, 2]

    wf.set_input_name("time_scoping", op.inputs.time_scoping)
    wf.set_output_name("field", op.outputs.fields_container)
    wf.connect("time_scoping", [1, 2])
    fcOut = wf.get_output("field", dpf.core.types.fields_container)
    assert fcOut.get_available_ids_for_label() == [1, 2]


def test_connect_fieldscontainer_workflow():
    wf = dpf.core.Workflow()
    op = dpf.core.Operator("min_max_fc")
    wf.add_operator(op)
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

    wf = dpf.core.Workflow()
    wf.set_input_name("fields_container", op, 0)
    wf.set_output_name("field", op, 0)
    wf.connect("fields_container", fc)
    fOut = wf.get_output("field", dpf.core.types.field)
    assert fOut.data.size == 60


def test_connect_fieldscontainer_2_workflow():
    wf = dpf.core.Workflow()
    op = dpf.core.Operator("min_max_fc")
    wf.add_operator(op)
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

    wf = dpf.core.Workflow()
    wf.set_input_name("fields_container", op.inputs.fields_container)
    wf.set_output_name("field", op.outputs.field_min)
    wf.connect("fields_container", fc)
    fOut = wf.get_output("field", dpf.core.types.field)
    assert fOut.data.size == 60


def test_connect_bool_workflow():
    op = dpf.core.Operator("S")
    wf = dpf.core.Workflow()
    wf.add_operator(op)
    wf.set_input_name("bool", op, 5)
    wf.connect("bool", True)

    wf = dpf.core.Workflow()
    wf.add_operator(op)
    wf.set_input_name("bool", op.inputs.bool_rotate_to_global)
    wf.connect("bool", True)


def test_connect_scoping_workflow():
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

    wf = dpf.core.Workflow()
    wf.add_operator(op)
    wf.set_input_name("field", op, 0)
    wf.connect("field", field)
    wf.set_input_name("mesh_scoping", op, 1)
    wf.connect("mesh_scoping", scop2)
    wf.set_output_name("field", op, 0)
    fOut = wf.get_output("field", dpf.core.types.field)
    scopOut = fOut.scoping
    assert scopOut.ids == list(range(1, 5))


def test_connect_scoping_2_workflow():
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

    wf = dpf.core.Workflow()
    wf.add_operator(op)
    wf.set_input_name("field", op.inputs.fields)
    wf.connect("field", field)
    wf.set_input_name("mesh_scoping", op.inputs.mesh_scoping)
    wf.connect("mesh_scoping", scop2)
    wf.set_output_name("field", op, 0)
    fOut = wf.get_output("field", dpf.core.types.field)
    scopOut = fOut.scoping
    assert scopOut.ids == list(range(1, 5))


def test_connect_datasources_workflow(fields_container_csv):
    op = dpf.core.Operator("csv_to_field")
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(fields_container_csv)

    wf = dpf.core.Workflow()
    wf.add_operator(op)
    wf.set_input_name("data_sources", op, 4)
    wf.connect("data_sources", data_sources)
    wf.set_output_name("fields_container", op, 0)

    fcOut = wf.get_output("fields_container", dpf.core.types.fields_container)
    assert len(fcOut.get_available_ids_for_label()) == 4

    wf = dpf.core.Workflow()
    wf.add_operator(op)
    wf.set_input_name("data_sources", op.inputs.data_sources)
    wf.connect("data_sources", data_sources)
    wf.set_output_name("fields_container", op, 0)

    fcOut = wf.get_output("fields_container", dpf.core.types.fields_container)
    assert len(fcOut.get_available_ids_for_label()) == 4


def test_connect_operator_workflow():
    op = dpf.core.Operator("norm")
    inpt = dpf.core.Field(nentities=3)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    op2 = dpf.core.Operator("component_selector")

    wf = dpf.core.Workflow()
    wf.add_operator(op2)
    wf.set_input_name("fields_container", op2, 0)
    wf.set_input_name("comp", op2, 1)
    wf.connect("fields_container", op, 0)
    wf.set_output_name("field", op, 0)

    wf.connect("comp", 0)
    fOut = wf.get_output("field", dpf.core.types.field)
    assert len(fOut.data) == 3


def test_connect_operator_2_workflow():
    op = dpf.core.Operator("norm")
    inpt = dpf.core.Field(nentities=3)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    op2 = dpf.core.Operator("component_selector")

    wf = dpf.core.Workflow()
    wf.add_operator(op2)
    wf.set_input_name("field", op2.inputs.field)
    wf.set_input_name("comp", op2.inputs.component_number)
    wf.connect("field", op.outputs.field)
    wf.set_output_name("field", op, 0)

    wf.connect("comp", 0)
    fOut = wf.get_output("field", dpf.core.types.field)
    assert len(fOut.data) == 3


def test_output_mesh_workflow(cyclic_lin_rst, cyclic_ds):
    data_sources = dpf.core.DataSources(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    model = dpf.core.Model(data_sources)
    op = model.operator("mapdl::rst::U")
    assert "data_sources" in str(op.inputs)
    assert "fields_container" in str(op.outputs)

    support = model.operator("mapdl::rst::support_provider_cyclic")
    expand = model.operator("cyclic_expansion")

    wf = dpf.core.Workflow()
    wf.add_operators([support, expand])
    wf.set_input_name("support", expand.inputs.cyclic_support)
    wf.set_input_name("fields", expand.inputs.fields_container)
    wf.connect("fields", op.outputs.fields_container)
    wf.connect("support", support.outputs.cyclic_support)
    wf.set_output_name("fields", op, 0)

    mesh = model.operator("cyclic_expansion_mesh")

    wf.add_operator(mesh)
    wf.set_input_name("support", mesh.inputs.cyclic_support)
    wf.connect("support", support.outputs.cyclic_support)
    wf.set_output_name("mesh", mesh, 0)
    meshed_region = wf.get_output("mesh", dpf.core.types.meshed_region)
    coord = meshed_region.nodes.coordinates_field
    assert coord.shape == (meshed_region.nodes.n_nodes, 3)
    assert (
            meshed_region.elements.connectivities_field.data.size
            == meshed_region.elements.connectivities_field.size
    )

    fields = wf.get_output("fields", dpf.core.types.fields_container)


def test_outputs_bool_workflow():
    inpt = dpf.core.Field(nentities=3)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op = dpf.core.Operator("AreFieldsIdentical")

    wf = dpf.core.Workflow()
    wf.add_operators([op])
    wf.set_input_name("fieldA", op.inputs.fieldA)
    wf.set_input_name("fieldB", op.inputs.fieldB)
    wf.connect("fieldA", inpt)
    wf.connect("fieldB", inpt)
    wf.set_output_name("bool", op, 0)

    out = wf.get_output("bool", dpf.core.types.bool)
    assert out == True


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_connect_get_output_int_list_workflow():
    d = list(range(0, 1000000))
    wf = dpf.core.Workflow()
    op = dpf.core.operators.utility.forward(d)
    wf.add_operators([op])
    wf.set_input_name("in", op, 0)
    wf.set_output_name("out", op, 0)
    dout = wf.get_output("out", dpf.core.types.vec_int)
    assert np.allclose(d, dout)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_connect_get_output_double_list_workflow():
    d = list(np.ones(500000))
    wf = dpf.core.Workflow()
    op = dpf.core.operators.utility.forward(d)
    wf.add_operators([op])
    wf.set_input_name("in", op, 0)
    wf.set_output_name("out", op, 0)
    dout = wf.get_output("out", dpf.core.types.vec_double)
    assert np.allclose(d, dout)


def test_inputs_outputs_inputs_outputs_scopings_container_workflow(allkindofcomplexity):
    data_sources = dpf.core.DataSources(allkindofcomplexity)
    model = dpf.core.Model(data_sources)
    op = dpf.core.Operator("scoping::by_property")

    wf = dpf.core.Workflow()
    wf.add_operators([op])
    wf.set_input_name("mesh", op.inputs.mesh)
    wf.set_input_name("prop", op.inputs.label1)
    wf.connect("mesh", model.metadata.meshed_region)
    wf.connect("prop", "elshape")
    wf.set_output_name("scopings", op, 0)

    sc = wf.get_output("scopings", dpf.core.types.scopings_container)

    op = dpf.core.Operator("forward")
    wf = dpf.core.Workflow()
    wf.add_operators([op])
    wf.set_input_name("a", op, 0)
    wf.set_output_name("a", op, 0)
    wf.connect("a", sc)
    out = wf.get_output("a", dpf.core.types.scopings_container)

    assert len(out) == len(sc)


def test_inputs_outputs_inputs_outputs_meshes_container_workflow(allkindofcomplexity):
    data_sources = dpf.core.DataSources(allkindofcomplexity)
    model = dpf.core.Model(data_sources)
    op = dpf.core.Operator("split_mesh")

    wf = dpf.core.Workflow()
    wf.add_operators([op])
    wf.set_input_name("mesh", op.inputs.mesh)
    wf.set_input_name("prop", op.inputs.property)
    wf.connect("mesh", model.metadata.meshed_region)
    wf.connect("prop", "elshape")
    wf.set_output_name("meshes", op, 0)

    mc = wf.get_output("meshes", dpf.core.types.meshes_container)

    op = dpf.core.Operator("forward")
    wf = dpf.core.Workflow()
    wf.add_operators([op])
    wf.set_input_name("a", op, 0)
    wf.set_output_name("a", op, 0)
    wf.connect("a", mc)
    out = wf.get_output("a", dpf.core.types.meshes_container)

    assert len(out) == len(mc)


def test_record_workflow(allkindofcomplexity):
    data_sources = dpf.core.DataSources(allkindofcomplexity)
    model = dpf.core.Model(data_sources)
    op = dpf.core.Operator("scoping::by_property")

    wf = dpf.core.Workflow()
    wf.add_operators([op])
    wf.set_input_name("mesh", op.inputs.mesh)
    wf.set_input_name("prop", op.inputs.label1)
    wf.connect("mesh", model.metadata.meshed_region)
    wf.connect("prop", "elshape")
    wf.set_output_name("scopings", op, 0)
    id = wf.record()

    op = dpf.core.Operator("forward")
    wf2 = dpf.core.Workflow()
    wf2.add_operators([op])
    wf2.set_input_name("a", op, 0)
    wf2.set_output_name("a", op, 0)
    id2 = wf2.record()

    wf_copy = dpf.core.Workflow.get_recorded_workflow(id)
    wf2_copy = dpf.core.Workflow.get_recorded_workflow(id2)
    sc = wf_copy.get_output("scopings", dpf.core.types.scopings_container)

    wf2_copy.connect("a", sc)
    out = wf2_copy.get_output("a", dpf.core.types.scopings_container)

    assert len(out) == len(sc)


def test_transfer_owner_workflow(allkindofcomplexity):
    data_sources = dpf.core.DataSources(allkindofcomplexity)
    model = dpf.core.Model(data_sources)
    op = dpf.core.Operator("scoping::by_property")

    wf = dpf.core.Workflow()
    wf.add_operators([op])
    wf.set_input_name("mesh", op.inputs.mesh)
    wf.set_input_name("prop", op.inputs.label1)
    wf.connect("mesh", model.metadata.meshed_region)
    wf.connect("prop", "elshape")
    wf.set_output_name("scopings", op, 0)
    id = wf.record(transfer_ownership=True)
    wf_copy = dpf.core.Workflow.get_recorded_workflow(id)

    with pytest.raises(Exception):
        wf_copy = dpf.core.Workflow.get_recorded_workflow(id)

    id = wf.record(transfer_ownership=False)
    wf_copy = dpf.core.Workflow.get_recorded_workflow(id)
    wf_copy = dpf.core.Workflow.get_recorded_workflow(id)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_connect_with_workflow(cyclic_lin_rst, cyclic_ds):
    data_sources = dpf.core.DataSources(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    model = dpf.core.Model(data_sources)
    support = model.operator("mapdl::rst::support_provider_cyclic")
    mesh = model.operator("cyclic_expansion_mesh")

    wf = dpf.core.Workflow()
    wf.add_operators([support, mesh])
    wf.set_input_name("support", mesh.inputs.cyclic_support)
    wf.connect("support", support.outputs.cyclic_support)
    wf.set_output_name("mesh_expand", mesh, 0)
    wf.set_output_name("support", mesh, 1)

    op = model.operator("mapdl::rst::U")
    expand = model.operator("cyclic_expansion")
    expand.connect(0, op, 0)

    wf2 = dpf.core.Workflow()
    wf2.add_operators([op, expand])
    wf2.set_input_name("support", expand.inputs.cyclic_support)
    wf2.set_output_name("u", op, 0)

    wf2.connect_with(wf)
    meshed_region = wf2.get_output("mesh_expand", dpf.core.types.meshed_region)
    fc = wf2.get_output("u", dpf.core.types.fields_container)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_connect_with_2_workflow(cyclic_lin_rst, cyclic_ds):
    data_sources = dpf.core.DataSources(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    model = dpf.core.Model(data_sources)
    support = model.operator("mapdl::rst::support_provider_cyclic")
    mesh = model.operator("cyclic_expansion_mesh")

    wf = dpf.core.Workflow()
    wf.add_operators([support, mesh])
    wf.set_input_name("support", mesh.inputs.cyclic_support)
    wf.connect("support", support.outputs.cyclic_support)
    wf.set_output_name("mesh_expand", mesh, 0)
    wf.set_output_name("support1", mesh, 1)

    op = model.operator("mapdl::rst::U")
    expand = model.operator("cyclic_expansion")
    expand.connect(0, op, 0)

    wf2 = dpf.core.Workflow()
    wf2.add_operators([op, expand])
    wf2.set_input_name("support2", expand.inputs.cyclic_support)
    wf2.set_output_name("u", op, 0)

    wf2.connect_with(wf, ("support1", "support2"))
    meshed_region = wf2.get_output("mesh_expand", dpf.core.types.meshed_region)
    fc = wf2.get_output("u", dpf.core.types.fields_container)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_connect_with_dict_workflow(cyclic_lin_rst, cyclic_ds):
    data_sources = dpf.core.DataSources(cyclic_lin_rst)
    data_sources.add_file_path(cyclic_ds)
    model = dpf.core.Model(data_sources)
    support = model.operator("mapdl::rst::support_provider_cyclic")
    mesh = model.operator("cyclic_expansion_mesh")

    wf = dpf.core.Workflow()
    wf.add_operators([support, mesh])
    wf.set_input_name("support", mesh.inputs.cyclic_support)
    wf.connect("support", support.outputs.cyclic_support)
    wf.set_output_name("mesh_expand", mesh, 0)
    wf.set_output_name("support1", mesh, 1)

    op = model.operator("mapdl::rst::U")
    expand = model.operator("cyclic_expansion")
    expand.connect(0, op, 0)

    wf2 = dpf.core.Workflow()
    wf2.add_operators([op, expand])
    wf2.set_input_name("support2", expand.inputs.cyclic_support)
    wf2.set_output_name("u", op, 0)

    wf2.connect_with(wf, {"support1": "support2"})
    meshed_region = wf2.get_output("mesh_expand", dpf.core.types.meshed_region)
    fc = wf2.get_output("u", dpf.core.types.fields_container)


def test_info_workflow(allkindofcomplexity):
    data_sources = dpf.core.DataSources(allkindofcomplexity)
    model = dpf.core.Model(data_sources)
    op = dpf.core.Operator("scoping::by_property")

    wf = dpf.core.Workflow()
    wf.add_operators([op])
    wf.set_input_name("mesh", op.inputs.mesh)
    wf.set_input_name("prop", op.inputs.label1)
    wf.connect("mesh", model.metadata.meshed_region)
    wf.connect("prop", "elshape")
    wf.set_output_name("scopings", op, 0)

    assert wf.info["operator_names"] == ["scoping::by_property"]
    assert wf.info["input_names"] == ["mesh", "prop"]
    assert wf.info["output_names"] == ["scopings"]
    assert wf.operator_names == ["scoping::by_property"]
    assert wf.input_names == ["mesh", "prop"]
    assert wf.output_names == ["scopings"]


def test_print_workflow():
    inpt = dpf.core.Field(nentities=3)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op = dpf.core.Operator("AreFieldsIdentical")

    wf = dpf.core.Workflow()
    wf.add_operators([op])
    wf.set_input_name("fieldA", op.inputs.fieldA)
    wf.set_input_name("fieldB", op.inputs.fieldB)
    wf.connect("fieldA", inpt)
    wf.connect("fieldB", inpt)
    wf.set_output_name("bool", op, 0)
    assert "AreFieldsIdentical" in str(wf)
    assert "input pins" in str(wf)
    assert "fieldA" in str(wf)
    assert "fieldB" in str(wf)
    assert "output pins" in str(wf)
    assert "bool" in str(wf)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_throws_error(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    wf = dpf.core.Workflow()
    op = model.results.stress()
    op.inputs.read_cyclic(3)
    opnorm = dpf.core.operators.averaging.to_nodal_fc(op)
    add = dpf.core.operators.math.add_fc(opnorm, opnorm)
    add2 = dpf.core.operators.math.add_fc(add, add)
    add3 = dpf.core.operators.math.add_fc(add2)
    add4 = dpf.core.operators.math.add_fc(add3, add3)
    wf.add_operators([op, opnorm, add, add2, add3, add4])
    wf.set_output_name("output", add4, 0)
    fc = wf.get_output("output", dpf.core.types.fields_container)
    assert len(fc) == 2
    add4.connect(1, 1)
    with pytest.raises(Exception):
        fc = wf.get_output("output", dpf.core.types.fields_container)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_flush_workflows_session(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    wf = dpf.core.Workflow()
    op = model.results.stress()
    op.inputs.read_cyclic(3)
    opnorm = dpf.core.operators.averaging.to_nodal_fc(op)
    add = dpf.core.operators.math.add_fc(opnorm, opnorm)
    add2 = dpf.core.operators.math.add_fc(add, add)
    add3 = dpf.core.operators.math.add_fc(add2)
    add4 = dpf.core.operators.math.add_fc(add3, add3)
    wf.add_operators([op, opnorm, add, add2, add3, add4])
    wf.set_output_name("output", add4, 0)
    fc = wf.get_output("output", dpf.core.types.fields_container)
    assert len(fc) == 2
    wf = dpf.core.Workflow()
    op = model.results.stress()
    op.inputs.read_cyclic(3)
    opnorm = dpf.core.operators.averaging.to_nodal_fc(op)
    add = dpf.core.operators.math.add_fc(opnorm, opnorm)
    add2 = dpf.core.operators.math.add_fc(add, add)
    add3 = dpf.core.operators.math.add_fc(add2)
    add4 = dpf.core.operators.math.add_fc(add3, add3)
    wf.add_operators([op, opnorm, add, add2, add3, add4])
    wf.set_output_name("output", add4, 0)
    fc = wf.get_output("output", dpf.core.types.fields_container)
    assert len(fc) == 2
    wf._server._session.flush_workflows()


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_create_on_other_server_workflow(local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(local_server)
    assert new_workflow.input_names == ['data_sources']
    assert new_workflow.output_names == ['max', 'min']


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_create_on_other_server2_workflow(local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(server=local_server)
    assert new_workflow.input_names == ['data_sources']
    assert new_workflow.output_names == ['max', 'min']


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_create_on_other_server_with_ip_workflow(local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(
        ip=local_server.ip,
        port=local_server.port)
    assert new_workflow.input_names == ['data_sources']
    assert new_workflow.output_names == ['max', 'min']


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_create_on_other_server_with_address_workflow(local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(
        address=local_server.ip + ":" + str(local_server.port))
    assert new_workflow.input_names == ['data_sources']
    assert new_workflow.output_names == ['max', 'min']


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_create_on_other_server_with_address2_workflow(local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(
        local_server.ip + ":" + str(local_server.port))
    assert new_workflow.input_names == ['data_sources']
    assert new_workflow.output_names == ['max', 'min']


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0,
                    reason='Requires server version higher than 3.0')
def test_create_on_other_server_and_connect_workflow(allkindofcomplexity, local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(local_server)
    new_workflow.connect("data_sources", dpf.core.DataSources(allkindofcomplexity))
    max = new_workflow.get_output("max", dpf.core.types.field)
    assert np.allclose(max.data, [[8.50619058e+04, 1.04659292e+01, 3.73620870e+05]])


def main():
    test_connect_field_workflow()
    velocity_acceleration = conftest.resolve_test_file(
        "velocity_acceleration.rst", "rst_operators"
    )
    test_connect_list_workflow(velocity_acceleration)
    test_connect_fieldscontainer_workflow()
    test_connect_fieldscontainer_2_workflow()
    test_connect_bool_workflow()
    test_connect_scoping_workflow()
    test_connect_scoping_2_workflow()
    fields_container_csv = conftest.resolve_test_file(
        "fields_container.csv", "csvToField"
    )
    test_connect_datasources_workflow(fields_container_csv)
    test_connect_operator_workflow()
    test_connect_operator_2_workflow()


if __name__ == "__main__":
    main()
