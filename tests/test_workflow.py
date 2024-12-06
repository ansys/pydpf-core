# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

import numpy as np
import pytest
import platform

import ansys.dpf.core.operators as op
from ansys.dpf.core.workflow_topology import WorkflowTopology
import conftest
from ansys import dpf
from ansys.dpf.core import misc
from conftest import raises_for_servers_version_under

if misc.module_exists("graphviz"):
    HAS_GRAPHVIZ = True
else:
    HAS_GRAPHVIZ = False


def test_create_workflow(server_type):
    wf = dpf.core.Workflow(server=server_type)
    assert wf._internal_obj


@pytest.fixture()
def remove_dot_file(request):
    """Cleanup a testing directory once we are finished."""

    dot_path = os.path.join(os.getcwd(), "test.dot")
    png_path = os.path.join(os.getcwd(), "test.png")
    png_path1 = os.path.join(os.getcwd(), "test1.png")

    def remove_files():
        if os.path.exists(dot_path):
            os.remove(os.path.join(os.getcwd(), dot_path))
        if os.path.exists(png_path):
            os.remove(os.path.join(os.getcwd(), png_path))
        if os.path.exists(png_path1):
            os.remove(os.path.join(os.getcwd(), png_path1))

    request.addfinalizer(remove_files)


@pytest.mark.skipif(not HAS_GRAPHVIZ, reason="Please install pyvista")
def test_workflow_view(server_in_process, remove_dot_file):
    pre_wf = dpf.core.Workflow(server=server_in_process)
    pre_op = dpf.core.operators.utility.forward(server=server_in_process)
    pre_wf.add_operator(pre_op)
    pre_wf.set_input_name("prewf_input", pre_op.inputs.any)
    pre_wf.set_output_name("prewf_output", pre_op.outputs.any)

    wf = dpf.core.Workflow(server=server_in_process)
    forward_op = dpf.core.operators.utility.forward(server=server_in_process)
    wf.add_operator(forward_op)
    wf.set_input_name("wf_input", forward_op.inputs.any)
    wf.set_output_name("wf_output", forward_op.outputs.any)

    wf.connect_with(pre_wf, {"prewf_output": "wf_input"})
    wf.view(off_screen=True, title="test1")
    assert not os.path.exists("test1.dot")
    assert os.path.exists("test1.png")
    wf.view(off_screen=True, save_as="test.png", keep_dot_file=True)
    assert os.path.exists("test.dot")
    assert os.path.exists("test.png")


def test_connect_field_workflow(server_type):
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    op = dpf.core.Operator("min_max", server=server_type)
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop

    wf.add_operator(op)
    wf.set_input_name("field", op, 0)
    wf.set_output_name("min", op, 0)
    wf.set_output_name("max", op, 1)
    wf.connect("field", inpt)
    f_out = wf.get_output("min", dpf.core.types.field)
    assert np.allclose(f_out.data, [1.0, 2.0, 3.0])
    f_out = wf.get_output("max", dpf.core.types.field)
    assert np.allclose(f_out.data, [7.0, 8.0, 9.0])

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.set_input_name("field", op.inputs.field)
    wf.set_output_name("min", op.outputs.field_min)
    wf.set_output_name("max", op.outputs.field_max)
    wf.connect("field", inpt)
    f_out = wf.get_output("min", dpf.core.types.field)
    assert np.allclose(f_out.data, [1.0, 2.0, 3.0])
    f_out = wf.get_output("max", dpf.core.types.field)
    assert np.allclose(f_out.data, [7.0, 8.0, 9.0])


def test_connect_list_workflow(velocity_acceleration, server_type):
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    model = dpf.core.Model(velocity_acceleration, server=server_type)
    op = model.operator("U")
    wf.add_operator(op)
    wf.set_input_name("time_scoping", op, 0)
    wf.set_output_name("field", op, 0)
    wf.connect("time_scoping", [1, 2])
    f_out = wf.get_output("field", dpf.core.types.fields_container)
    assert f_out.get_available_ids_for_label() == [1, 2]

    wf.set_input_name("time_scoping", op.inputs.time_scoping)
    wf.set_output_name("field", op.outputs.fields_container)
    wf.connect("time_scoping", [1, 2])
    f_out = wf.get_output("field", dpf.core.types.fields_container)
    assert f_out.get_available_ids_for_label() == [1, 2]


def test_connect_fieldscontainer_workflow(server_type):
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    op = dpf.core.Operator("min_max_fc", server=server_type)
    wf.add_operator(op)
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

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.set_input_name("fields_container", op, 0)
    wf.set_output_name("field", op, 0)
    wf.connect("fields_container", fc)
    f_out = wf.get_output("field", dpf.core.types.field)
    assert f_out.data.size == 60


def test_connect_fieldscontainer_2_workflow(server_type):
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    op = dpf.core.Operator("min_max_fc", server=server_type)
    wf.add_operator(op)
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

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.set_input_name("fields_container", op.inputs.fields_container)
    wf.set_output_name("field", op.outputs.field_min)
    wf.connect("fields_container", fc)
    f_out = wf.get_output("field", dpf.core.types.field)
    assert f_out.data.size == 60


def test_connect_bool_workflow(server_type):
    op = dpf.core.Operator("S", server=server_type)
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operator(op)
    wf.set_input_name("bool", op, 5)
    wf.connect("bool", True)

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operator(op)
    wf.set_input_name("bool", op.inputs.bool_rotate_to_global)
    wf.connect("bool", True)


def test_connect_scoping_workflow(server_type):
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

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operator(op)
    wf.set_input_name("field", op, 0)
    wf.connect("field", field)
    wf.set_input_name("mesh_scoping", op, 1)
    wf.connect("mesh_scoping", scop2)
    wf.set_output_name("field", op, 0)
    f_out = wf.get_output("field", dpf.core.types.field)
    scop_out = f_out.scoping
    assert np.allclose(scop_out.ids, list(range(1, 5)))


def test_connect_scoping_2_workflow(server_type):
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

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operator(op)
    wf.set_input_name("field", op.inputs.fields)
    wf.connect("field", field)
    wf.set_input_name("mesh_scoping", op.inputs.mesh_scoping)
    wf.connect("mesh_scoping", scop2)
    wf.set_output_name("field", op, 0)
    f_out = wf.get_output("field", dpf.core.types.field)
    scop_out = f_out.scoping
    assert np.allclose(scop_out.ids, list(range(1, 5)))


def test_connect_datasources_workflow(fields_container_csv, server_type):
    op = dpf.core.Operator("csv_to_field", server=server_type)
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(fields_container_csv)

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operator(op)
    wf.set_input_name("data_sources", op, 4)
    wf.connect("data_sources", data_sources)
    wf.set_output_name("fields_container", op, 0)

    f_out = wf.get_output("fields_container", dpf.core.types.fields_container)
    assert len(f_out.get_available_ids_for_label()) == 4

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operator(op)
    wf.set_input_name("data_sources", op.inputs.data_sources)
    wf.connect("data_sources", data_sources)
    wf.set_output_name("fields_container", op, 0)

    f_out = wf.get_output("fields_container", dpf.core.types.fields_container)
    assert len(f_out.get_available_ids_for_label()) == 4


def test_connect_operator_workflow(server_type):
    op = dpf.core.Operator("norm", server=server_type)
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    op2 = dpf.core.Operator("component_selector", server=server_type)

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operator(op2)
    wf.set_input_name("fields_container", op2, 0)
    wf.set_input_name("comp", op2, 1)
    wf.connect("fields_container", op, 0)
    wf.set_output_name("field", op, 0)

    wf.connect("comp", 0)
    f_out = wf.get_output("field", dpf.core.types.field)
    assert len(f_out.data) == 3


def test_connect_operator_2_workflow(server_type):
    op = dpf.core.Operator("norm", server=server_type)
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op.connect(0, inpt)
    op2 = dpf.core.Operator("component_selector", server=server_type)

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operator(op2)
    wf.set_input_name("field", op2.inputs.field)
    wf.set_input_name("comp", op2.inputs.component_number)
    wf.connect("field", op.outputs.field)
    wf.set_output_name("field", op, 0)

    wf.connect("comp", 0)
    f_out = wf.get_output("field", dpf.core.types.field)
    assert len(f_out.data) == 3


def test_output_mesh_workflow(cyclic_lin_rst, cyclic_ds, server_type):
    data_sources = dpf.core.DataSources(cyclic_lin_rst, server=server_type)
    data_sources.add_file_path(cyclic_ds)
    model = dpf.core.Model(data_sources, server=server_type)
    op = model.operator("mapdl::rst::U")
    assert "data_sources" in str(op.inputs)
    assert "fields_container" in str(op.outputs)

    support = model.operator("mapdl::rst::support_provider_cyclic")
    expand = model.operator("cyclic_expansion")

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
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


def test_outputs_bool_workflow(server_type):
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op = dpf.core.Operator("AreFieldsIdentical", server=server_type)

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operators([op])
    wf.set_input_name("fieldA", op.inputs.fieldA)
    wf.set_input_name("fieldB", op.inputs.fieldB)
    wf.connect("fieldA", inpt)
    wf.connect("fieldB", inpt)
    wf.set_output_name("bool", op, 0)

    out = wf.get_output("bool", dpf.core.types.bool)
    assert out is True


@conftest.raises_for_servers_version_under("3.0")
def test_connect_get_output_int_list_workflow(server_type):
    d = list(range(0, 1000000))
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    op = dpf.core.operators.utility.forward(d, server=server_type)
    wf.add_operators([op])
    wf.set_input_name("in", op, 0)
    wf.set_output_name("out", op, 0)
    d_out = wf.get_output("out", dpf.core.types.vec_int)
    assert np.allclose(d, d_out)


@conftest.raises_for_servers_version_under("3.0")
def test_connect_get_output_double_list_workflow(server_type):
    d = list(np.ones(500000))
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    op = dpf.core.operators.utility.forward(d, server=server_type)
    wf.add_operators([op])
    wf.set_input_name("in", op, 0)
    wf.set_output_name("out", op, 0)
    d_out = wf.get_output("out", dpf.core.types.vec_double)
    assert np.allclose(d, d_out)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="Copying data is " "supported starting server version 5.0",
)
def test_connect_label_space_workflow(server_type):
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    op = dpf.core.operators.utility.forward(server=server_type)
    wf.add_operators([op])
    wf.set_input_name("in", op, 0)
    dic = {"time": 1, "complex": 0}
    wf.connect("in", dic)


@conftest.raises_for_servers_version_under("5.0")
def test_connect_get_output_string_field_workflow(server_type):
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    op = dpf.core.operators.utility.forward(server=server_type)
    wf.add_operators([op])
    wf.set_input_name("in", op, 0)
    str_field = dpf.core.StringField(server=server_type)
    str_field.data = ["hello"]
    wf.connect("in", str_field)
    wf.set_output_name("out", op, 0)
    d_out = wf.get_output("out", dpf.core.types.string_field)
    assert d_out.data == ["hello"]


@conftest.raises_for_servers_version_under("5.0")
def test_connect_get_output_custom_type_field_workflow(server_type):
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    op = dpf.core.operators.utility.forward(server=server_type)
    wf.add_operators([op])
    wf.set_input_name("in", op, 0)
    str_field = dpf.core.CustomTypeField(np.int16, server=server_type)
    str_field.data = [-1]
    wf.connect("in", str_field)
    wf.set_output_name("out", op, 0)
    d_out = wf.get_output("out", dpf.core.types.custom_type_field)
    assert d_out.data == [-1]
    assert d_out._type == np.int16


def test_inputs_outputs_inputs_outputs_scopings_container_workflow(
    allkindofcomplexity, server_type
):
    data_sources = dpf.core.DataSources(allkindofcomplexity, server=server_type)
    model = dpf.core.Model(data_sources, server=server_type)
    op = dpf.core.Operator("scoping::by_property", server=server_type)

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operators([op])
    wf.set_input_name("mesh", op.inputs.mesh)
    wf.set_input_name("prop", op.inputs.label1)
    wf.connect("mesh", model.metadata.meshed_region)
    wf.connect("prop", "elshape")
    wf.set_output_name("scopings", op, 0)

    sc = wf.get_output("scopings", dpf.core.types.scopings_container)

    op = dpf.core.Operator("forward", server=server_type)
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operators([op])
    wf.set_input_name("a", op, 0)
    wf.set_output_name("a", op, 0)
    wf.connect("a", sc)
    out = wf.get_output("a", dpf.core.types.scopings_container)

    assert len(out) == len(sc)


def test_inputs_outputs_inputs_outputs_meshes_container_workflow(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(allkindofcomplexity, server=server_type)
    model = dpf.core.Model(data_sources, server=server_type)
    op = dpf.core.Operator("split_mesh", server=server_type)

    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operators([op])
    wf.set_input_name("mesh", op.inputs.mesh)
    wf.set_input_name("prop", op.inputs.property)
    wf.connect("mesh", model.metadata.meshed_region)
    wf.connect("prop", "elshape")
    wf.set_output_name("meshes", op, 0)

    mc = wf.get_output("meshes", dpf.core.types.meshes_container)

    op = dpf.core.Operator("forward", server=server_type)
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    wf.add_operators([op])
    wf.set_input_name("a", op, 0)
    wf.set_output_name("a", op, 0)
    wf.connect("a", mc)
    out = wf.get_output("a", dpf.core.types.meshes_container)

    assert len(out) == len(mc)


@conftest.raises_for_servers_version_under("4.0")
def test_connect_get_output_data_tree_operator(server_type):
    d = dpf.core.DataTree({"name": "Paul"}, server=server_type)
    wf = dpf.core.Workflow(server=server_type)
    wf.progress_bar = False
    op = dpf.core.operators.utility.forward(server=server_type)
    wf.set_input_name("in", op.inputs.any)
    wf.set_output_name("out", op.outputs.any)
    wf.connect("in", d)
    d_out = wf.get_output("out", dpf.core.types.data_tree)
    assert d_out.get_as("name") == "Paul"


@conftest.raises_for_servers_version_under("7.0")
def test_connect_get_output_generic_data_container_operator(server_type):
    inpt = dpf.core.GenericDataContainer(server=server_type)
    wf = dpf.core.Workflow(server=server_type)
    op = dpf.core.operators.utility.forward(server=server_type)
    wf.set_input_name("in", op.inputs.any)
    wf.set_output_name("out", op.outputs.any)
    wf.connect("in", inpt)
    d_out = wf.get_output("out", dpf.core.types.generic_data_container)
    assert type(d_out) == dpf.core.GenericDataContainer


def test_record_workflow(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(allkindofcomplexity, server=server_type)
    model = dpf.core.Model(data_sources, server=server_type)
    op = dpf.core.Operator("scoping::by_property", server=server_type)

    wf = dpf.core.Workflow(server=server_type)
    wf.add_operators([op])
    wf.set_input_name("mesh", op.inputs.mesh)
    wf.set_input_name("prop", op.inputs.label1)
    wf.connect("mesh", model.metadata.meshed_region)
    wf.connect("prop", "elshape")
    wf.set_output_name("scopings", op, 0)
    id = wf.record()

    op = dpf.core.Operator("forward", server=server_type)
    wf2 = dpf.core.Workflow(server=server_type)
    wf2.add_operators([op])
    wf2.set_input_name("a", op, 0)
    wf2.set_output_name("a", op, 0)
    id2 = wf2.record()

    wf_copy = dpf.core.Workflow.get_recorded_workflow(id, server=server_type)
    wf2_copy = dpf.core.Workflow.get_recorded_workflow(id2, server=server_type)
    sc = wf_copy.get_output("scopings", dpf.core.types.scopings_container)

    wf2_copy.connect("a", sc)
    out = wf2_copy.get_output("a", dpf.core.types.scopings_container)

    assert len(out) == len(sc)


@pytest.mark.xfail(raises=dpf.core.errors.ServerTypeError)
def test_transfer_owner_workflow(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(allkindofcomplexity, server=server_type)
    model = dpf.core.Model(data_sources, server=server_type)
    op = dpf.core.Operator("scoping::by_property", server=server_type)

    wf = dpf.core.Workflow(server=server_type)
    wf.add_operators([op])
    wf.set_input_name("mesh", op.inputs.mesh)
    wf.set_input_name("prop", op.inputs.label1)
    wf.connect("mesh", model.metadata.meshed_region)
    wf.connect("prop", "elshape")
    wf.set_output_name("scopings", op, 0)
    id = wf.record(transfer_ownership=True)
    wf_copy = dpf.core.Workflow.get_recorded_workflow(id, server=server_type)

    with pytest.raises(Exception):
        wf_copy = dpf.core.Workflow.get_recorded_workflow(id, server=server_type)

    id = wf.record(transfer_ownership=False)
    wf_copy = dpf.core.Workflow.get_recorded_workflow(id, server=server_type)
    wf_copy = dpf.core.Workflow.get_recorded_workflow(id, server=server_type)


@conftest.raises_for_servers_version_under("3.0")
def test_connect_with_workflow(cyclic_lin_rst, cyclic_ds, server_type):
    data_sources = dpf.core.DataSources(cyclic_lin_rst, server=server_type)
    data_sources.add_file_path(cyclic_ds)
    model = dpf.core.Model(data_sources, server=server_type)
    support = model.operator("mapdl::rst::support_provider_cyclic")
    mesh = model.operator("cyclic_expansion_mesh")

    wf = dpf.core.Workflow(server=server_type)
    wf.add_operators([support, mesh])
    wf.set_input_name("support", mesh.inputs.cyclic_support)
    wf.connect("support", support.outputs.cyclic_support)
    wf.set_output_name("mesh_expand", mesh, 0)
    wf.set_output_name("support", mesh, 1)

    op = model.operator("mapdl::rst::U")
    expand = model.operator("cyclic_expansion")
    expand.connect(0, op, 0)

    wf2 = dpf.core.Workflow(server=server_type)
    wf2.add_operators([op, expand])
    wf2.set_input_name("support", expand.inputs.cyclic_support)
    wf2.set_output_name("u", op, 0)

    wf2.connect_with(wf)
    meshed_region = wf2.get_output("mesh_expand", dpf.core.types.meshed_region)
    fc = wf2.get_output("u", dpf.core.types.fields_container)


@conftest.raises_for_servers_version_under("3.0")
def test_connect_with_2_workflow(cyclic_lin_rst, cyclic_ds, server_type):
    data_sources = dpf.core.DataSources(cyclic_lin_rst, server=server_type)
    data_sources.add_file_path(cyclic_ds)
    model = dpf.core.Model(data_sources, server=server_type)
    support = model.operator("mapdl::rst::support_provider_cyclic")
    mesh = model.operator("cyclic_expansion_mesh")

    wf = dpf.core.Workflow(server=server_type)
    wf.add_operators([support, mesh])
    wf.set_input_name("support", mesh.inputs.cyclic_support)
    wf.connect("support", support.outputs.cyclic_support)
    wf.set_output_name("mesh_expand", mesh, 0)
    wf.set_output_name("support1", mesh, 1)

    op = model.operator("mapdl::rst::U")
    expand = model.operator("cyclic_expansion")
    expand.connect(0, op, 0)

    wf2 = dpf.core.Workflow(server=server_type)
    wf2.add_operators([op, expand])
    wf2.set_input_name("support2", expand.inputs.cyclic_support)
    wf2.set_output_name("u", op, 0)

    wf2.connect_with(wf, ("support1", "support2"))
    meshed_region = wf2.get_output("mesh_expand", dpf.core.types.meshed_region)
    fc = wf2.get_output("u", dpf.core.types.fields_container)


@conftest.raises_for_servers_version_under("3.0")
def test_connect_with_dict_workflow(cyclic_lin_rst, cyclic_ds, server_type):
    data_sources = dpf.core.DataSources(cyclic_lin_rst, server=server_type)
    data_sources.add_file_path(cyclic_ds)
    model = dpf.core.Model(data_sources, server=server_type)
    support = model.operator("mapdl::rst::support_provider_cyclic")
    mesh = model.operator("cyclic_expansion_mesh")

    wf = dpf.core.Workflow(server=server_type)
    wf.add_operators([support, mesh])
    wf.set_input_name("support", mesh.inputs.cyclic_support)
    wf.connect("support", support.outputs.cyclic_support)
    wf.set_output_name("mesh_expand", mesh, 0)
    wf.set_output_name("support1", mesh, 1)

    op = model.operator("mapdl::rst::U")
    expand = model.operator("cyclic_expansion")
    expand.connect(0, op, 0)

    wf2 = dpf.core.Workflow(server=server_type)
    wf2.add_operators([op, expand])
    wf2.set_input_name("support2", expand.inputs.cyclic_support)
    wf2.set_output_name("u", op, 0)

    wf2.connect_with(wf, {"support1": "support2"})
    meshed_region = wf2.get_output("mesh_expand", dpf.core.types.meshed_region)
    fc = wf2.get_output("u", dpf.core.types.fields_container)


@pytest.mark.xfail(raises=dpf.core.errors.ServerTypeError)
def test_info_workflow(allkindofcomplexity, server_type):
    model = dpf.core.Model(allkindofcomplexity, server=server_type)
    op = dpf.core.Operator("scoping::by_property", server=server_type)

    wf = dpf.core.Workflow(server=server_type)
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


def test_print_workflow(server_type):
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop
    op = dpf.core.Operator("AreFieldsIdentical", server=server_type)

    wf = dpf.core.Workflow(server=server_type)
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


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Bug with server's version older than 3.0",
)
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


@pytest.mark.xfail(raises=dpf.core.errors.ServerTypeError)
@conftest.raises_for_servers_version_under("3.0")
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
    wf._server.session.flush_workflows()


@pytest.mark.xfail(raises=dpf.core.errors.ServerTypeError)
@conftest.raises_for_servers_version_under("3.0")
@pytest.mark.skipif(
    platform.system() == "Linux" and platform.python_version().startswith("3.8"),
    reason="Random SEGFAULT in the GitHub pipeline for 3.8 on Ubuntu",
)
def test_create_on_other_server_workflow(local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(local_server)
    assert new_workflow.input_names == ["data_sources"]
    assert new_workflow.output_names == ["max", "min"]


@pytest.mark.xfail(raises=dpf.core.errors.ServerTypeError)
@conftest.raises_for_servers_version_under("3.0")
@pytest.mark.skipif(
    platform.system() == "Linux" and platform.python_version().startswith("3.8"),
    reason="Random SEGFAULT in the GitHub pipeline for 3.8 on Ubuntu",
)
def test_create_on_other_server2_workflow(local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(server=local_server)
    assert new_workflow.input_names == ["data_sources"]
    assert new_workflow.output_names == ["max", "min"]


@pytest.mark.xfail(raises=dpf.core.errors.ServerTypeError)
@conftest.raises_for_servers_version_under("3.0")
@pytest.mark.skipif(
    platform.system() == "Linux" and platform.python_version().startswith("3.8"),
    reason="Random SEGFAULT in the GitHub pipeline for 3.8 on Ubuntu",
)
def test_create_on_other_server_with_ip_workflow(local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(ip=local_server.ip, port=local_server.port)
    assert new_workflow.input_names == ["data_sources"]
    assert new_workflow.output_names == ["max", "min"]


@pytest.mark.xfail(raises=dpf.core.errors.ServerTypeError)
@conftest.raises_for_servers_version_under("3.0")
@pytest.mark.skipif(
    platform.system() == "Linux" and platform.python_version().startswith("3.8"),
    reason="Random SEGFAULT in the GitHub pipeline for 3.8 on Ubuntu",
)
def test_create_on_other_server_with_address_workflow(local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(
        address=local_server.ip + ":" + str(local_server.port)
    )
    assert new_workflow.input_names == ["data_sources"]
    assert new_workflow.output_names == ["max", "min"]


@pytest.mark.xfail(raises=dpf.core.errors.ServerTypeError)
@conftest.raises_for_servers_version_under("3.0")
def test_create_on_other_server_with_address2_workflow(local_server):
    disp_op = op.result.displacement()
    max_fc_op = op.min_max.min_max_fc(disp_op)
    workflow = dpf.core.Workflow()
    workflow.add_operators([disp_op, max_fc_op])
    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", max_fc_op.outputs.field_min)
    workflow.set_output_name("max", max_fc_op.outputs.field_max)
    new_workflow = workflow.create_on_other_server(local_server.ip + ":" + str(local_server.port))
    assert new_workflow.input_names == ["data_sources"]
    assert new_workflow.output_names == ["max", "min"]


@pytest.mark.skipif(
    platform.system() == "Linux" and platform.python_version().startswith("3.10"),
    reason="Known failure in the GitHub pipeline for 3.10 on Ubuntu",
)
@pytest.mark.skipif(
    platform.system() == "Linux"
    and platform.python_version().startswith("3.8")
    and not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Known failure in the GitHub pipeline for 3.8 on Ubuntu for 221",
)
@pytest.mark.xfail(raises=dpf.core.errors.ServerTypeError)
@conftest.raises_for_servers_version_under("3.0")
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
    assert np.allclose(max.data, [[8.50619058e04, 1.04659292e01, 3.73620870e05]])


def deep_copy_using_workflow(dpf_entity, server, stream_type=1):
    from ansys.dpf.core.operators.serialization import serializer_to_string, string_deserializer
    from ansys.dpf.core.common import types_enum_to_types, types

    entity_server = dpf_entity._server if hasattr(dpf_entity, "_server") else None
    serializer_wf = dpf.core.Workflow(server=entity_server)
    serializer = serializer_to_string(server=entity_server)
    serializer.connect(1, dpf_entity)
    serializer.connect(-1, stream_type)  # binary
    serializer_wf.set_output_name("out", serializer, 0)
    if stream_type == 1:
        out = serializer_wf.get_output("out", types.bytes)
    else:
        out = serializer_wf.get_output("out", types.string)
    deserializer_wf = dpf.core.Workflow(server=server)
    deserializer = string_deserializer(server=server)
    deserializer_wf.set_input_name("in", 0, deserializer)
    deserializer_wf.connect("in", out)
    deserializer.connect(-1, stream_type)  # binary
    type_map = types_enum_to_types()
    output_type = list(type_map.keys())[list(type_map.values()).index(dpf_entity.__class__)]
    return deserializer.get_output(1, output_type)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0, reason="Available for servers >=8.0"
)
def test_connect_get_output_big_strings(server_type, server_in_process):
    data = np.random.random(100000)
    field_a = dpf.core.field_from_array(data, server=server_type)
    assert np.allclose(field_a.data, data)

    out = deep_copy_using_workflow(field_a, server_in_process)
    assert np.allclose(out.data, data)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0, reason="Available for servers >=8.0"
)
def test_connect_get_output_big_strings(server_type, server_type_remote_process):
    data = np.random.random(100000)
    field_a = dpf.core.field_from_array(data, server=server_type)
    assert np.allclose(field_a.data, data)

    out = deep_copy_using_workflow(field_a, server_type_remote_process)
    assert np.allclose(out.data, data)


@conftest.raises_for_servers_version_under("8.0")
def test_connect_get_non_ascii_string(server_type):
    str = "\N{GREEK CAPITAL LETTER DELTA}"
    str_out = deep_copy_using_workflow(str, server_type)
    assert str == str_out


def test_connect_get_non_ascii_string_str(server_type):
    str = "\N{GREEK CAPITAL LETTER DELTA}"
    str_out = deep_copy_using_workflow(str, server_type, 0)
    assert str == str_out


def test_output_any(server_type):
    inpt = dpf.core.Field(nentities=3, server=server_type)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    scop = dpf.core.Scoping(server=server_type)
    scop.ids = [1, 2, 3]
    inpt.data = data
    inpt.scoping = scop

    fwd = dpf.core.Operator("forward", server=server_type)
    fwd.connect(0, inpt)

    wf = dpf.core.Workflow(server=server_type)
    wf.add_operator(fwd)
    wf.set_output_name("field", fwd, 0)

    output_field = wf.get_output("field", dpf.core.types.any).cast(dpf.core.Field)
    assert isinstance(output_field, dpf.core.Field)
    assert output_field.data.size == 9
    assert output_field.scoping.size == 3


@pytest.mark.skipif(
    condition=not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
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
    fwd = dpf.core.Operator(name="forward", server=server_type)

    wf = dpf.core.Workflow(server=server_type)
    wf.add_operator(fwd)
    wf.set_input_name("in", fwd, 0)
    wf.set_output_name("out", fwd, 0)

    wf.connect(pin_name="in", inpt=inpt)
    output = wf.get_output(pin_name="out", output_type=dpf.core.types.field)
    assert isinstance(output, dpf.core.Field)


@pytest.mark.skipif(
    condition=not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="Input/output of Streams requires DPF 6.0 or above.",
)
def test_workflow_input_output_streams(server_in_process, simple_bar):
    data_source = dpf.core.DataSources(simple_bar, server=server_in_process)
    streams_op = dpf.core.operators.metadata.streams_provider(server=server_in_process)
    streams_op.inputs.data_sources.connect(data_source)
    wf_1 = dpf.core.Workflow(server=server_in_process)
    wf_1.add_operator(streams_op)
    wf_1.set_output_name("output_streams", streams_op.outputs.streams_container)

    streams = wf_1.get_output("output_streams", dpf.core.types.streams_container)

    time_provider = dpf.core.operators.metadata.time_freq_provider(server=server_in_process)

    wf_2 = dpf.core.Workflow(server=server_in_process)
    wf_2.add_operator(time_provider)
    wf_2.set_input_name("input_streams", time_provider.inputs.streams_container)
    wf_2.set_output_name("output_tfs", time_provider.outputs.time_freq_support)
    wf_2.connect("input_streams", streams)
    times = wf_2.get_output("output_tfs", dpf.core.types.time_freq_support)
    assert times


@raises_for_servers_version_under("10.0")
def test_workflow_get_output_derived_class(server_type):
    workflow = dpf.core.Workflow(server=server_type)

    workflow_to_workflow_topology_op = dpf.core.Operator(
        "workflow_to_workflow_topology", server=server_type
    )
    dpf_workflow_wrapper = dpf.core.Workflow(server=server_type)
    dpf_workflow_wrapper.add_operator(workflow_to_workflow_topology_op)
    dpf_workflow_wrapper.set_input_name("input", workflow_to_workflow_topology_op, 0)
    dpf_workflow_wrapper.set_output_name("output", workflow_to_workflow_topology_op, 0)
    dpf_workflow_wrapper.connect("input", workflow)

    workflow_topology = dpf_workflow_wrapper.get_output("output", WorkflowTopology)
    assert workflow_topology


def main():
    test_connect_field_workflow()
    velocity_acceleration = conftest.resolve_test_file("velocity_acceleration.rst", "rst_operators")
    test_connect_list_workflow(velocity_acceleration)
    test_connect_fieldscontainer_workflow()
    test_connect_fieldscontainer_2_workflow()
    test_connect_bool_workflow()
    test_connect_scoping_workflow()
    test_connect_scoping_2_workflow()
    fields_container_csv = conftest.resolve_test_file("fields_container.csv", "csvToField")
    test_connect_datasources_workflow(fields_container_csv)
    test_connect_operator_workflow()
    test_connect_operator_2_workflow()


if __name__ == "__main__":
    main()
