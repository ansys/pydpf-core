import os

import pytest

from ansys.dpf import core as dpf


def try_load_cff_operators():
    try:
        if os.name == "posix":
            return False
        dpf.load_library("Ans.Dpf.CFF.dll", "cff")
        return True
    except:
        return False
    # TODO: add loading for linux


def try_load_lsdyna_operators():
    try:
        dpf.load_library("Ans.Dpf.LSDYNA.dll", "lsdyna")
        return True
    except:
        return False


@pytest.mark.skipif(
    not try_load_lsdyna_operators(), reason="Couldn't load lsdyna operators"
)
def test_lsdyna(d3plot):
    dpf.load_library("Ans.Dpf.LSDYNA.dll", "lsdyna")
    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot, "d3plot")
    streams = dpf.operators.metadata.streams_provider(ds)
    u = dpf.operators.result.displacement()
    u.inputs.streams_container(streams)
    fc = u.outputs.fields_container()
    assert len(fc[0]) == 3195


def try_load_composites_operators():
    try:
        dpf.load_library("composite_operators.dll", "compo")
        dpf.load_library("Ans.Dpf.EngineeringData.dll", "eng")
        return True
    except:
        return False


@pytest.mark.skipif(
    not try_load_composites_operators(), reason="Couldn't load composites operators"
)
def test_eng(engineering_data_sources):
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
