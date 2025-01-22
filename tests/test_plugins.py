# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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

from pathlib import Path

import pytest

from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0
from ansys.dpf import core as dpf
from ansys.dpf.core import examples


@pytest.fixture()
def try_load_lsdyna_operators():
    try:
        dpf.load_library("Ans.Dpf.LSDYNA.dll", "lsdyna")
        return True
    except:
        pytest.skip("Couldn't load lsdyna operators")
        return False


def test_lsdyna(d3plot_files, try_load_lsdyna_operators):
    dpf.load_library("Ans.Dpf.LSDYNA.dll", "lsdyna")
    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot_files[0], "d3plot")
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
    field_variable_provider = dpf.Operator("composite::inistate_field_variables_provider")
    field_variable_provider.connect(4, engineering_data_sources)
    field_variable_provider.inputs.mesh.connect(m.metadata.mesh_provider)
    field_variable_provider.run()


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="Requires server version higher than 5.0",
)
def test_lsdynahgp(d3plot_files, server_type):
    ds = dpf.DataSources(server=server_type)
    ds.set_result_file_path(d3plot_files[0], "d3plot")
    streams = dpf.operators.metadata.streams_provider(ds, server=server_type)
    u = dpf.operators.result.displacement(server=server_type)
    u.inputs.streams_container(streams)
    fc = u.outputs.fields_container()
    assert len(fc[0]) == 3195
    assert dpf.Operator("lsdyna::stream_provider") is not None


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="Requires server version higher than 5.0",
)
def test_cgns(server_type):
    assert dpf.Operator("cgns::stream_provider", server=server_type) is not None


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="Requires server version higher than 5.0",
)
def test_vtk(server_type, tmpdir):
    op = dpf.Operator("vtu_export", server=server_type)
    try:
        rst_file = dpf.upload_file_in_tmp_folder(
            examples.download_pontoon(return_local_path=True), server=server_type
        )
    except dpf.errors.ServerTypeError as e:
        print(e)
        rst_file = examples.download_pontoon(return_local_path=True)
        pass

    assert op is not None
    model = dpf.Model(rst_file, server=server_type)
    u = model.operator("U")
    op.inputs.fields1.connect(u)
    op.inputs.mesh.connect(model.metadata.mesh_provider)
    op.inputs.directory.connect(str(Path(rst_file).parent))
    # out_path = op.eval()
    # assert out_path.result_files is not []
    # try:
    #     out_path = dpf.core.download_file(
    #         out_path, tmp_path, server=server_type)
    # except dpf.errors.ServerTypeError as e:
    #     print(e)
    #     pass
    # assert os.path.exists(tmp_path)
