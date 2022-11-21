import pytest
import os
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0
from ansys.dpf import core as dpf


@pytest.fixture()
def try_load_lsdyna_operators():
    try:
        dpf.load_library("Ans.Dpf.LSDYNA.dll", "lsdyna")
        return True
    except:
        pytest.skip("Couldn't load lsdyna operators")
        return False


def test_lsdyna(d3plot, try_load_lsdyna_operators):
    dpf.load_library("Ans.Dpf.LSDYNA.dll", "lsdyna")
    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot, "d3plot")
    streams = dpf.operators.metadata.streams_provider(ds)
    u = dpf.operators.result.displacement()
    u.inputs.streams_container(streams)
    fc = u.outputs.fields_container()
    assert len(fc[0]) == 3195


@pytest.fixture()
def try_load_composites_operators():
    try:
        dpf.load_library("composite_operators.dll", "compo")
        dpf.load_library("Ans.Dpf.EngineeringData.dll", "eng")
        return True
    except:
        pytest.skip("Couldn't load composites operators")
        return False


def test_eng(engineering_data_sources, try_load_composites_operators):
    dpf.load_library("composite_operators.dll", "compo")
    dpf.load_library("Ans.Dpf.EngineeringData.dll", "eng")
    m = dpf.Model(engineering_data_sources)
    stress_op = dpf.operators.result.stress()
    stress_op.inputs.data_sources.connect(engineering_data_sources)
    result_info_provider = dpf.operators.metadata.result_info_provider()
    result_info_provider.inputs.data_sources.connect(engineering_data_sources)
    mat_support_operator = dpf.operators.metadata.material_support_provider()
    mat_support_operator.inputs.data_sources.connect(engineering_data_sources)
    ans_mat_operator = dpf.Operator("eng_data::ans_mat_material_provider")
    ans_mat_operator.connect(0, mat_support_operator, 0)
    ans_mat_operator.connect(1, result_info_provider, 0)
    ans_mat_operator.connect(4, engineering_data_sources)
    field_variable_provider = dpf.Operator(
        "composite::inistate_field_variables_provider"
    )
    field_variable_provider.connect(4, engineering_data_sources)
    field_variable_provider.inputs.mesh.connect(m.metadata.mesh_provider)
    field_variable_provider.run()


@pytest.mark.skipif(not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
                    reason='Requires server version higher than 5.0')
def test_vtk(server_type, simple_bar, tmpdir):
    op = dpf.Operator("vtu_export", server=server_type)
    try:
        rst_file = dpf.upload_file_in_tmp_folder(simple_bar, server=server_type)
    except dpf.errors.ServerTypeError as e:
        print(e)
        rst_file = simple_bar
        pass
    assert op is not None
    tmp_path = str(tmpdir.join("simple_bar.vtu"))
    model = dpf.Model(rst_file, server=server_type)
    u = model.operator("U")
    op.inputs.fields1.connect(u)
    op.inputs.mesh.connect(model.metadata.mesh_provider)
    op.inputs.directory.connect(os.path.dirname(rst_file))
    data_sources = op.eval()
    print(data_sources)
    out_path = data_sources.result_files[0]
    print(out_path)
    assert out_path is not None
    try:
        out_path = dpf.core.download_file(
            out_path, tmp_path, server=server_type)
    except dpf.errors.ServerTypeError as e:
        print(e)
        pass
    print(tmp_path)
    assert os.path.exists(tmp_path)
