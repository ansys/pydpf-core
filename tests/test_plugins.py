
from ansys.dpf import core as dpf
import pytest
import os


# def try_load_cff_operators():
    # try:
        # dpf.load_library("libAns.Dpf.CFF.so", "cff")
        # print("cff loaded, Linux")
        # return True
    # except:
        # try:
            # dpf.load_library("Ans.Dpf.CFF.dll","cff")
            # print("cff loaded, Windows")
        # except: 
            # print("cff failed to load")
            # return False
    #TODO: add loading for linux
    
def try_load_cff_operators():
    if os.name == "posix":
        try: 
            dpf.load_library("libAns.Dpf.CFF.so", "cff")
            return True
        except: 
            return False
    else:
        try: 
            dpf.load_library("Ans.Dpf.CFF.dll", "cff")
            return True
        except: 
            return False
        
@pytest.mark.skipif(not try_load_cff_operators(), reason="Couldn't load cff operators")
def test_cff_model(cff_data_sources):
    m = dpf.Model(cff_data_sources)
    assert m.metadata.meshed_region.nodes.n_nodes ==1430
    op = dpf.Operator("cff::cas::SV_DENSITY")
    op.connect(4, m.metadata.data_sources)
    fc= op.get_output(0, dpf.types.fields_container)
    assert len(fc[0])==1380

@pytest.mark.skipif(not try_load_cff_operators(), reason="Couldn't load cff operators")
def test_cff_stream_operator(cff_data_sources):
    stream_op = dpf.Operator("cff::stream_provider")
    stream_op.connect(4, cff_data_sources)
    res_info = dpf.Operator("ResultInfoProvider")
    res_info.connect(3, stream_op, 0)
    info = res_info.outputs.result_info()
    assert info.analysis_type == 'unknown_analysis'
    assert info.physics_type == 'unknown_physics'
    assert info.n_results == 15
    assert info.unit_system == "unknown"
    res_info_2 = dpf.Operator("cff::cas::ResultInfoProvider")
    res_info_2.connect(3, stream_op, 0)
    info_2 = res_info_2.outputs.result_info()
    assert info_2.analysis_type == 'unknown_analysis'
    assert info_2.physics_type == 'unknown_physics'
    assert info_2.n_results == 15
    assert info_2.unit_system == "unknown"
    op = dpf.Operator("cff::cas::SV_V")
    op.connect(3, stream_op, 0)
    field = op.get_output(0, dpf.types.fields_container)[0]
    data = field.data
    assert len(data) == 1450
    assert field.location == dpf.locations.elemental
    

def try_load_lsdyna_operators():
    try:
        dpf.load_library("Ans.Dpf.LSDYNA.dll","lsdyna")
        return True
    except:
        return False
    
@pytest.mark.skipif(not try_load_lsdyna_operators(), reason="Couldn't load lsdyna operators")
def test_lsdyna(d3plot):
    dpf.load_library("Ans.Dpf.LSDYNA.dll","lsdyna")
    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot,"d3plot")
    streams = dpf.operators.metadata.streams_provider(ds)
    u = dpf.operators.result.displacement()
    u.inputs.streams_container(streams)
    fc = u.outputs.fields_container()
    assert len(fc)==22
    assert len(fc[0])==3195
    
def try_load_composites_operators():
    try:
        dpf.load_library("composite_operators.dll","compo")
        dpf.load_library("Ans.Dpf.EngineeringData.dll","eng")
        return True
    except:
        return False
        
@pytest.mark.skipif(not try_load_composites_operators(), reason="Couldn't load composites operators")
def test_eng(engineering_data_sources):    
    dpf.load_library("composite_operators.dll","compo")
    dpf.load_library("Ans.Dpf.EngineeringData.dll","eng")
    m=dpf.Model(engineering_data_sources)
    stress_op = dpf.operators.result.stress()
    stress_op.inputs.data_sources.connect(engineering_data_sources)
    result_info_provider = dpf.operators.metadata.result_info_provider()
    result_info_provider.inputs.data_sources.connect(engineering_data_sources)
    mat_support_operator = dpf.operators.metadata.material_support_provider()
    mat_support_operator.inputs.data_sources.connect(engineering_data_sources)
    ans_mat_operator = dpf.Operator("eng_data::ans_mat_material_provider")
    ans_mat_operator.connect(0, mat_support_operator, 0)
    ans_mat_operator.connect(1, result_info_provider, 0)
    ans_mat_operator.connect(4,engineering_data_sources)
    field_variable_provider = dpf.Operator("composite::inistate_field_variables_provider")
    field_variable_provider.connect(4, engineering_data_sources)
    field_variable_provider.inputs.mesh.connect(m.metadata.mesh_provider)
    field_variable_provider.run()
