import pytest
import os
import platform
import numpy as np
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0
from ansys.dpf import core as dpf
import conftest
from ansys.dpf.core.errors import DPFServerException
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    SpecificationProperties,
    CustomConfigOptionSpec,
    PinSpecification,
)

if not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0:
    pytest.skip("Requires server version higher than 4.0", allow_module_level=True)
# if platform.python_version().startswith("3.7"):
#     pytest.skip(
#         "Known failures in the GitHub pipelines for 3.7",
#         allow_module_level=True
#     )
if platform.system() == "Linux":
    pytest.skip(
        "Known failures for the Ubuntu-latest GitHub pipelines", allow_module_level=True
    )


@pytest.fixture(scope="module")
def load_all_types_plugin(testfiles_dir):
    return dpf.load_library(
        dpf.path_utilities.to_server_os(
            os.path.join(testfiles_dir, "pythonPlugins", "all_types")
        ),
        "py_test_types",
        "load_operators",
    )


def load_all_types_plugin_with_serv(my_server, testfiles_dir):
    return dpf.load_library(
        dpf.path_utilities.to_server_os(
            os.path.join(testfiles_dir, "pythonPlugins", "all_types"), my_server
        ),
        "py_test_types",
        "load_operators",
        server=my_server,
    )


def test_integral_types(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    op = dpf.Operator("custom_forward_int", server=server_type_remote_process)
    op.connect(0, 1)
    assert op.get_output(0, dpf.types.int) == 1

    op = dpf.Operator("custom_forward_float", server=server_type_remote_process)
    op.connect(0, 1.5)
    assert op.get_output(0, dpf.types.double) == 1.5

    op = dpf.Operator("custom_forward_bool", server=server_type_remote_process)
    op.connect(0, True)
    assert op.get_output(0, dpf.types.bool) == True

    op = dpf.Operator("custom_forward_str", server=server_type_remote_process)
    op.connect(0, "hello")
    assert op.get_output(0, dpf.types.string) == "hello"


def test_lists(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    op = dpf.Operator("custom_forward_vec_int", server=server_type_remote_process)
    op.connect(0, [1, 2, 3])
    assert np.allclose(op.get_output(0, dpf.types.vec_int), [1, 2, 3])
    op = dpf.Operator("custom_set_out_vec_double", server=server_type_remote_process)
    assert np.allclose(op.get_output(0, dpf.types.vec_double), [1.0, 2.0, 3.0])
    op = dpf.Operator("custom_set_out_np_int", server=server_type_remote_process)
    assert np.allclose(
        op.get_output(0, dpf.types.vec_int), np.ones((200), dtype=np.int)
    )
    op = dpf.Operator("custom_set_out_np_double", server=server_type_remote_process)
    assert np.allclose(op.get_output(0, dpf.types.vec_double), np.ones((200)))


def test_field(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.fields_factory.create_3d_vector_field(
        3, "Elemental", server=server_type_remote_process
    )
    f.data = np.ones((3, 3), dtype=np.float)
    op = dpf.Operator("custom_forward_field", server=server_type_remote_process)
    op.connect(0, f)
    assert np.allclose(
        op.get_output(0, dpf.types.field).data, np.ones((3, 3), dtype=np.float)
    )
    assert op.get_output(0, dpf.types.field).location == "Elemental"


def test_property_field(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.PropertyField(server=server_type_remote_process)
    f.data = np.ones((9), dtype=np.int32)
    op = dpf.Operator(
        "custom_forward_property_field", server=server_type_remote_process
    )
    op.connect(0, f)
    assert np.allclose(
        op.get_output(0, dpf.types.property_field).data,
        np.ones((9), dtype=np.int32),
    )


@conftest.raises_for_servers_version_under("5.0")
def test_string_field(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.StringField(server=server_type_remote_process)
    f.data = ["hello", "good"]
    op = dpf.Operator("custom_forward_string_field", server=server_type_remote_process)
    op.connect(0, f)
    assert op.get_output(0, dpf.types.string_field).data == ["hello", "good"]


@conftest.raises_for_servers_version_under("5.0")
def test_custom_type_field(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.CustomTypeField(np.uint64, server=server_type_remote_process)
    f.data = np.array([1000000000000, 200000000000000], dtype=np.uint64)
    op = dpf.Operator(
        "custom_forward_custom_type_field", server=server_type_remote_process
    )
    op.connect(0, f)
    assert np.allclose(
        op.get_output(0, dpf.types.custom_type_field).data,
        [1000000000000, 200000000000000],
    )


def test_scoping(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.Scoping(location="Elemental", server=server_type_remote_process)
    op = dpf.Operator("custom_forward_scoping", server=server_type_remote_process)
    op.connect(0, f)
    assert op.get_output(0, dpf.types.scoping).location == "Elemental"


def test_fields_container(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.fields_factory.create_3d_vector_field(
        3, "Elemental", server=server_type_remote_process
    )
    f.data = np.ones((3, 3), dtype=np.float)
    fc = dpf.fields_container_factory.over_time_freq_fields_container(
        [f], server=server_type_remote_process
    )
    op = dpf.Operator(
        "custom_forward_fields_container", server=server_type_remote_process
    )
    op.connect(0, fc)
    assert np.allclose(
        op.get_output(0, dpf.types.fields_container)[0].data,
        np.ones((3, 3), dtype=np.float),
    )
    assert op.get_output(0, dpf.types.fields_container)[0].location == "Elemental"


def test_scopings_container(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.Scoping(location="Elemental", server=server_type_remote_process)
    sc = dpf.ScopingsContainer(server=server_type_remote_process)
    sc.add_scoping({}, f)
    op = dpf.Operator(
        "custom_forward_scopings_container", server=server_type_remote_process
    )
    op.connect(0, sc)
    assert op.get_output(0, dpf.types.scopings_container)[0].location == "Elemental"


def test_meshes_container(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.MeshedRegion(server=server_type_remote_process)
    sc = dpf.MeshesContainer(server=server_type_remote_process)
    sc.add_mesh({}, f)
    op = dpf.Operator(
        "custom_forward_meshes_container", server=server_type_remote_process
    )
    op.connect(0, sc)
    assert len(op.get_output(0, dpf.types.meshes_container)) == 1


def test_data_sources(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.DataSources("file.rst", server=server_type_remote_process)
    op = dpf.Operator("custom_forward_data_sources", server=server_type_remote_process)
    op.connect(0, f)
    assert op.get_output(0, dpf.types.data_sources).result_files == ["file.rst"]


@pytest.mark.skipif(
    platform.system() == "Windows" and platform.python_version().startswith("3.8"),
    reason="Random SEGFAULT in the GitHub pipeline for 3.8 on Windows",
)
def test_workflow(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.Workflow(server=server_type_remote_process)
    op = dpf.Operator("custom_forward_workflow", server=server_type_remote_process)
    op.connect(0, f)
    assert op.get_output(0, dpf.types.workflow) is not None


def test_data_tree(server_type_remote_process, testfiles_dir):
    load_all_types_plugin_with_serv(server_type_remote_process, testfiles_dir)
    f = dpf.DataTree(server=server_type_remote_process)
    f.add(name="Paul")
    op = dpf.Operator("custom_forward_data_tree", server=server_type_remote_process)
    op.connect(0, f)
    dt = op.get_output(0, dpf.types.data_tree)
    assert dt is not None
    assert dt.get_as("name") == "Paul"


@conftest.raises_for_servers_version_under("4.0")
def test_syntax_error(server_type_remote_process, testfiles_dir):
    dpf.load_library(
        dpf.path_utilities.to_server_os(
            os.path.join(testfiles_dir, "pythonPlugins", "syntax_error_plugin"),
            server_type_remote_process,
        ),
        "py_raising",
        "load_operators",
        server=server_type_remote_process,
    )
    op = dpf.Operator("raising", server=server_type_remote_process)
    with pytest.raises(DPFServerException) as ex:
        op.run()
        assert "SyntaxError" in str(ex.args)
        assert "set_ouuuuuutput" in str(ex.args)


@conftest.raises_for_servers_version_under("4.0")
def test_create_op_specification(server_in_process):
    spec = CustomSpecification(server=server_in_process)
    spec.description = "Add a custom value to all the data of an input Field"
    spec.inputs = {
        0: PinSpecification(
            "field", [dpf.Field], "Field on which float value is added."
        ),
        1: PinSpecification("to_add", [float], "Data to add."),
    }
    spec.outputs = {
        0: PinSpecification(
            "field", [dpf.Field], "Field on which the float value is added."
        )
    }
    spec.properties = SpecificationProperties("custom add to field", "math")
    spec.config_specification = [
        CustomConfigOptionSpec("work_by_index", False, "iterate over indices")
    ]
    assert spec.description == "Add a custom value to all the data of an input Field"
    assert len(spec.inputs) == 2
    assert spec.inputs[0].name == "field"
    assert spec.inputs[0].type_names == ["field"]
    assert spec.inputs[1].document == "Data to add."
    assert spec.outputs[0] == PinSpecification(
        "field", [dpf.Field], "Field on which the float value is added."
    )
    assert spec.properties["exposure"] == "public"
    assert spec.properties["category"] == "math"
    assert spec.config_specification["work_by_index"].document == "iterate over indices"
    assert spec.config_specification["work_by_index"].default_value_str == "false"


@conftest.raises_for_servers_version_under("4.0")
def test_create_config_op_specification(server_in_process):
    spec = CustomSpecification(server=server_in_process)
    spec.config_specification = [
        CustomConfigOptionSpec("work_by_index", False, "iterate over indices")
    ]
    spec.config_specification = [CustomConfigOptionSpec("other", 1, "bla")]
    spec.config_specification = [CustomConfigOptionSpec("other2", 1.5, "blo")]
    spec.config_specification = [CustomConfigOptionSpec("other3", 1.0, "blo")]
    assert spec.config_specification["work_by_index"].document == "iterate over indices"
    assert spec.config_specification["work_by_index"].default_value_str == "false"
    assert spec.config_specification["other"].document == "bla"
    assert spec.config_specification["other"].default_value_str == "1"
    assert spec.config_specification["other"].type_names == ["int32"]
    assert spec.config_specification["other2"].document == "blo"
    assert spec.config_specification["other2"].default_value_str == "1.5"
    assert spec.config_specification["other2"].type_names == ["double"]


@conftest.raises_for_servers_version_under("4.0")
def test_create_properties_specification(server_in_process):
    spec = CustomSpecification(server=server_in_process)
    spec.properties = SpecificationProperties("custom add to field", "math")
    assert spec.properties["exposure"] == "public"
    assert spec.properties["category"] == "math"
    assert spec.properties.exposure == "public"
    assert spec.properties.category == "math"
    spec = CustomSpecification(server=server_in_process)
    spec.properties["exposure"] = "public"
    spec.properties["category"] = "math"
    assert spec.properties.exposure == "public"
    assert spec.properties.category == "math"


@conftest.raises_for_servers_version_under("4.0")
def test_custom_op_with_spec(server_type_remote_process, testfiles_dir):
    dpf.load_library(
        dpf.path_utilities.to_server_os(
            os.path.join(testfiles_dir, "pythonPlugins"), server_type_remote_process
        ),
        "py_operator_with_spec",
        "load_operators",
        server=server_type_remote_process,
    )
    op = dpf.Operator("custom_add_to_field", server=server_type_remote_process)
    assert "Add a custom value to all the data of an input Field" in str(op)
    assert "Field on which float value is added" in str(op.inputs)
    assert "Field on which the float value is added" in str(op.outputs.field)
    f = dpf.fields_factory.create_3d_vector_field(
        3, "Elemental", server=server_type_remote_process
    )
    f.data = np.ones((3, 3), dtype=np.float)
    op.inputs.field(f)
    op.inputs.to_add(3.0)
    outf = op.outputs.field()
    expected = np.ones((3, 3), dtype=np.float) + 3.0
    assert np.allclose(outf.data, expected)
    op = dpf.Operator("custom_add_to_field", server=server_type_remote_process)
    op.inputs.connect(f)
    op.inputs.to_add(4.0)
    f.data = np.ones((3, 3), dtype=np.float)
    outf = op.outputs.field()
    expected = np.ones((3, 3), dtype=np.float) + 4.0
    assert np.allclose(outf.data, expected)
