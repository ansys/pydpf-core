import pytest
import os
import numpy as np
from ansys.dpf import core as dpf
from ansys.dpf.core.errors import DPFServerException
from ansys.dpf.core.check_version import meets_version, get_server_version


SERVER_VERSION_HIGHER_THAN_5_0 = meets_version(get_server_version(dpf._global_server()), "5.0")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_5_0,
                    reason='Requires server version higher than 5.0')
@pytest.fixture(scope="module")
def load_all_types_plugin():
    current_dir = os.getcwd()
    return dpf.load_library(os.path.join(current_dir, "testfiles", "pythonPlugins", "all_types"), "py_test_types", "load_operators")


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


def test_field(load_all_types_plugin):
    f = dpf.fields_factory.create_3d_vector_field(3, "Elemental")
    f.data = np.ones((3,3), dtype=np.float)
    op = dpf.Operator("custom_forward_field")
    op.connect(0, f)
    assert np.allclose(op.get_output(0, dpf.types.field).data, np.ones((3,3), dtype=np.float))
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
    assert len(op.get_output(0, dpf.types.meshes_container))==1


def test_data_sources(load_all_types_plugin):
    f = dpf.DataSources("file.rst")
    op = dpf.Operator("custom_forward_data_sources")
    op.connect(0, f)
    assert op.get_output(0, dpf.types.data_sources).result_files == ["file.rst"]


def test_syntax_error():
    current_dir = os.getcwd()
    dpf.load_library(os.path.join(current_dir, "testfiles", "pythonPlugins", "syntax_error_plugin"), "py_raising",
                     "load_operators")
    op = dpf.Operator("raising")
    with pytest.raises(DPFServerException) as ex:
        op.run()
        assert "SyntaxError" in str(ex.args)
        assert "set_ouuuuuutput" in str(ex.args)

