import pytest
import os
import numpy as np
from conftest import SERVER_VERSION_HIGHER_THAN_4_0
from ansys.dpf import core as dpf
from ansys.dpf.core.errors import DPFServerException
from ansys.dpf.core import server_types
from ansys.dpf.core.operator_specification import CustomSpecification, SpecificationProperties, CustomConfigOptionSpec, \
    PinSpecification

if not SERVER_VERSION_HIGHER_THAN_4_0:
    pytest.skip('Requires server version higher than 4.0', allow_module_level=True)


@pytest.fixture(scope="module")
def load_all_types_plugin():
    current_dir = os.getcwd()
    return dpf.load_library(os.path.join(current_dir, "testfiles", "pythonPlugins", "all_types"), "py_test_types",
                            "load_operators")


def test_integral_types(load_all_types_plugin):
    op = dpf.Operator("custom_forward_int")
    op.connect(0, 1)
    assert op.get_output(0, dpf.types.int) == 1

    op = dpf.Operator("custom_forward_float")
    op.connect(0, 1.5)
    assert op.get_output(0, dpf.types.double) == 1.5

    op = dpf.Operator("custom_forward_bool")
    op.connect(0, True)
    assert op.get_output(0, dpf.types.bool) == True

    op = dpf.Operator("custom_forward_str")
    op.connect(0, "hello")
    assert op.get_output(0, dpf.types.string) == "hello"


def test_lists(load_all_types_plugin):
    op = dpf.Operator("custom_forward_vec_int")
    op.connect(0, [1, 2, 3])
    assert np.allclose(op.get_output(0, dpf.types.vec_int), [1, 2, 3])
    op = dpf.Operator("custom_set_out_vec_double")
    assert np.allclose(op.get_output(0, dpf.types.vec_double), [1., 2., 3.])
    op = dpf.Operator("custom_set_out_np_int")
    assert np.allclose(op.get_output(0, dpf.types.vec_int), np.ones((200), dtype=np.int))
    op = dpf.Operator("custom_set_out_np_double")
    assert np.allclose(op.get_output(0, dpf.types.vec_double), np.ones((200)))


def test_field(load_all_types_plugin):
    f = dpf.fields_factory.create_3d_vector_field(3, "Elemental")
    f.data = np.ones((3, 3), dtype=np.float)
    op = dpf.Operator("custom_forward_field")
    op.connect(0, f)
    assert np.allclose(op.get_output(0, dpf.types.field).data, np.ones((3, 3), dtype=np.float))
    assert op.get_output(0, dpf.types.field).location == "Elemental"


def test_property_field(load_all_types_plugin):
    f = dpf.PropertyField()
    f.data = np.ones((9), dtype=np.int32)
    op = dpf.Operator("custom_forward_property_field")
    op.connect(0, f)
    assert np.allclose(op.get_output(0, dpf.types.property_field).data, np.ones((9), dtype=np.int32))


def test_scoping(load_all_types_plugin):
    f = dpf.Scoping(location="Elemental")
    op = dpf.Operator("custom_forward_scoping")
    op.connect(0, f)
    assert op.get_output(0, dpf.types.scoping).location == "Elemental"


def test_fields_container(load_all_types_plugin):
    f = dpf.fields_factory.create_3d_vector_field(3, "Elemental")
    f.data = np.ones((3, 3), dtype=np.float)
    fc = dpf.fields_container_factory.over_time_freq_fields_container([f])
    op = dpf.Operator("custom_forward_fields_container")
    op.connect(0, fc)
    assert np.allclose(op.get_output(0, dpf.types.fields_container)[0].data, np.ones((3, 3), dtype=np.float))
    assert op.get_output(0, dpf.types.fields_container)[0].location == "Elemental"


def test_scopings_container(load_all_types_plugin):
    f = dpf.Scoping(location="Elemental")
    sc = dpf.ScopingsContainer()
    sc.add_scoping({}, f)
    op = dpf.Operator("custom_forward_scopings_container")
    op.connect(0, sc)
    assert op.get_output(0, dpf.types.scopings_container)[0].location == "Elemental"


def test_meshes_container(load_all_types_plugin):
    f = dpf.MeshedRegion()
    sc = dpf.MeshesContainer()
    sc.add_mesh({}, f)
    op = dpf.Operator("custom_forward_meshes_container")
    op.connect(0, sc)
    assert len(op.get_output(0, dpf.types.meshes_container)) == 1


def test_data_sources(load_all_types_plugin):
    f = dpf.DataSources("file.rst")
    op = dpf.Operator("custom_forward_data_sources")
    op.connect(0, f)
    assert op.get_output(0, dpf.types.data_sources).result_files == ["file.rst"]


def test_workflow(load_all_types_plugin):
    f = dpf.Workflow()
    op = dpf.Operator("custom_forward_workflow")
    op.connect(0, f)
    assert op.get_output(0, dpf.types.workflow) is not None


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 5.0')
def test_syntax_error():
    current_dir = os.getcwd()
    dpf.load_library(os.path.join(current_dir, "testfiles", "pythonPlugins", "syntax_error_plugin"), "py_raising",
                     "load_operators")
    op = dpf.Operator("raising")
    with pytest.raises(DPFServerException) as ex:
        op.run()
        assert "SyntaxError" in str(ex.args)
        assert "set_ouuuuuutput" in str(ex.args)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_create_op_specification():
    local_server = server_types.InProcessServer(as_global=False)
    spec = CustomSpecification(server=local_server)
    spec.description = "Add a custom value to all the data of an input Field"
    spec.inputs = {0: PinSpecification("field", [dpf.Field], "Field on which float value is added."),
                   1: PinSpecification("to_add", [float], "Data to add.")}
    spec.outputs = {0: PinSpecification("field", [dpf.Field], "Field on which the float value is added.")}
    spec.properties = SpecificationProperties("custom add to field", "math")
    spec.config_specification = [CustomConfigOptionSpec("work_by_index", False, "iterate over indices")]
    assert spec.description == "Add a custom value to all the data of an input Field"
    assert len(spec.inputs) == 2
    assert spec.inputs[0].name == "field"
    assert spec.inputs[0].type_names == ["field"]
    assert spec.inputs[1].document == "Data to add."
    assert spec.outputs[0] == PinSpecification("field", [dpf.Field], "Field on which the float value is added.")
    assert spec.properties["exposure"] == "public"
    assert spec.properties["category"] == "math"
    assert spec.config_specification["work_by_index"].document == "iterate over indices"
    assert spec.config_specification["work_by_index"].default_value_str == "false"


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_create_config_op_specification():
    local_server = server_types.InProcessServer(as_global=False)
    spec = CustomSpecification(server=local_server)
    spec.config_specification = [CustomConfigOptionSpec("work_by_index", False, "iterate over indices")]
    spec.config_specification = [CustomConfigOptionSpec("other", 1, "bla")]
    spec.config_specification = [CustomConfigOptionSpec("other2", 1.5, "blo")]
    spec.config_specification = [CustomConfigOptionSpec("other3", 1., "blo")]
    assert spec.config_specification["work_by_index"].document == "iterate over indices"
    assert spec.config_specification["work_by_index"].default_value_str == "false"
    assert spec.config_specification["other"].document == "bla"
    assert spec.config_specification["other"].default_value_str == "1"
    assert spec.config_specification["other"].type_names == ["int32"]
    assert spec.config_specification["other2"].document == "blo"
    assert spec.config_specification["other2"].default_value_str == "1.5"
    assert spec.config_specification["other2"].type_names == ["double"]


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_create_properties_specification():
    local_server = server_types.InProcessServer(as_global=False)
    spec = CustomSpecification(server=local_server)
    spec.properties = SpecificationProperties("custom add to field", "math")
    assert spec.properties["exposure"] == "public"
    assert spec.properties["category"] == "math"
    assert spec.properties.exposure == "public"
    assert spec.properties.category == "math"
    spec = CustomSpecification(server=local_server)
    spec.properties["exposure"] = "public"
    spec.properties["category"] = "math"
    assert spec.properties.exposure == "public"
    assert spec.properties.category == "math"


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_custom_op_with_spec():
    current_dir = os.getcwd()
    dpf.load_library(os.path.join(current_dir, "testfiles", "pythonPlugins"), "py_operator_with_spec",
                     "load_operators")
    op = dpf.Operator("custom_add_to_field")
    assert "Add a custom value to all the data of an input Field" in str(op)
    assert "Field on which float value is added" in str(op.inputs)
    assert "Field on which the float value is added" in str(op.outputs.field)
    f = dpf.fields_factory.create_3d_vector_field(3, "Elemental")
    f.data = np.ones((3, 3), dtype=np.float)
    op.inputs.field(f)
    op.inputs.to_add(3.0)
    outf = op.outputs.field()
    expected = np.ones((3, 3), dtype=np.float) + 3.
    assert np.allclose(outf.data, expected)
    op = dpf.Operator("custom_add_to_field")
    op.inputs.connect(f)
    op.inputs.to_add(4.0)
    f.data = np.ones((3, 3), dtype=np.float)
    outf = op.outputs.field()
    expected = np.ones((3, 3), dtype=np.float) + 4.
    assert np.allclose(outf.data, expected)
