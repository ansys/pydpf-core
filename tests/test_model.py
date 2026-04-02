# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

import functools
import gc
from unittest.mock import patch

import numpy as np
import pytest

from ansys import dpf
from ansys.dpf.core import examples, misc
from ansys.dpf.core.check_version import server_meet_version
from ansys.dpf.core.errors import ServerTypeError

NO_PLOTTING = True

if misc.module_exists("pyvista"):
    from pyvista.plotting import system_supports_plotting

    NO_PLOTTING = not system_supports_plotting()


@pytest.fixture()
def static_model():
    try:
        path = dpf.core.upload_file_in_tmp_folder(examples.find_static_rst(return_local_path=True))
    except ServerTypeError:
        path = examples.find_static_rst()
    return dpf.core.Model(path)


def test_model_from_data_source(simple_bar):
    data_source = dpf.core.DataSources(simple_bar)
    model = dpf.core.Model(data_source)
    assert "displacement" in model.metadata.result_info


def test_model_metadata_from_data_source(simple_bar):
    data_source = dpf.core.DataSources(simple_bar)
    model = dpf.core.Model(data_source)
    assert model.metadata.result_info is not None
    assert model.metadata.time_freq_support is not None
    assert model.metadata.meshed_region is not None
    assert model.metadata.data_sources is not None


def test_displacements_eval(static_model):
    disp = static_model.results.displacement()
    fc = disp.outputs.fields_container()
    disp_field_from_eval = fc[0]

    fc_from_outputs = disp.outputs.fields_container()[0]
    assert np.allclose(disp_field_from_eval.data, fc_from_outputs.data)


def test_extract_component(static_model):
    disp = static_model.results.displacement()
    disp = disp.X()
    disp_field = disp.outputs.fields_container()[0]
    assert isinstance(disp_field.data, np.ndarray)


def test_kinetic(static_model):
    e = static_model.results.kinetic_energy()
    energy = e.outputs.fields_container()[0]
    assert isinstance(energy.data, np.ndarray)


def test_str_model(static_model):
    assert "Static" in str(static_model)
    assert "81" in str(static_model)
    assert "Unit: m" in str(static_model)


def test_connect_inputs_in_constructor_model(plate_msup):
    model = dpf.core.Model(plate_msup)
    u = model.results.displacement(0.015)
    fc = u.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [5.12304110e-14, 3.64308310e-04, 5.79805917e-06])
    scop = dpf.core.Scoping()
    scop.ids = list(range(1, 21))
    u = model.results.displacement(0.015, scop)
    fc = u.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [9.66814331e-16, 6.82591973e-06, 1.35911110e-06])
    assert fc[0].shape == (20, 3)


def test_named_selection_model(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    ns = model.metadata.available_named_selections
    assert ns == [
        "_CM82",
        "_CM86UX_XP",
        "_DISPNONZEROUX",
        "_DISPZEROUZ",
        "_ELMISC",
        "_FIXEDSU",
    ]
    scop = model.metadata.named_selection("_CM86UX_XP")
    assert len(scop) == 481
    assert scop.location == dpf.core.locations().nodal


def test_all_result_operators_exist(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    res = model.results
    for key in res.__dict__:
        if isinstance(res.__dict__[key], functools.partial):
            res.__dict__[key]()


def test_iterate_results_model(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    res = model.results
    for key in res:
        key()


def test_result_not_overrided(plate_msup):
    model1 = dpf.core.Model(examples.find_electric_therm())
    size = len(model1.results)
    model2 = dpf.core.Model(plate_msup)
    assert len(model1.results) == size
    assert len(model2.results) > len(model1.results)


def test_result_displacement_model():
    model = dpf.core.Model(examples.download_all_kinds_of_complexity_modal())
    results = model.results
    assert isinstance(results.displacement(), dpf.core.Operator)
    assert len(results.displacement.on_all_time_freqs.eval()) == 45
    assert results.displacement.on_first_time_freq.eval().get_label_scoping().ids == [1]
    assert results.displacement.on_last_time_freq.eval().get_label_scoping().ids == [45]
    if server_meet_version("9.0", model._server):
        assert len(results.displacement.split_by_body.eval()) == 44
    else:
        assert len(results.displacement.split_by_body.eval()) == 32
    if server_meet_version("12.0", model._server):
        assert len(results.displacement.split_by_shape.eval()) == 6
    else:
        assert len(results.displacement.split_by_shape.eval()) == 4
    assert len(results.displacement.on_named_selection("_FIXEDSU").eval()[0].scoping) == 222
    all_time_ns = results.displacement.on_named_selection("_FIXEDSU").on_all_time_freqs.eval()
    assert len(all_time_ns) == 45
    assert len(all_time_ns[0].scoping) == 222
    assert len(all_time_ns[19].scoping) == 222


def test_result_stress_model():
    model = dpf.core.Model(examples.download_all_kinds_of_complexity_modal())
    results = model.results
    assert isinstance(results.stress(), dpf.core.Operator)
    assert len(results.stress.on_all_time_freqs.eval()) == 45
    assert results.stress.on_first_time_freq.eval().get_label_scoping().ids == [1]
    assert results.stress.on_last_time_freq.eval().get_label_scoping().ids == [45]
    if server_meet_version("9.0", model._server):
        assert len(results.stress.split_by_body.eval()) == 44
    else:
        assert len(results.stress.split_by_body.eval()) == 32
        if server_meet_version("12.0", model._server):
            assert len(results.stress.split_by_shape.eval()) == 6
        else:
            assert len(results.stress.split_by_shape.eval()) == 4
    assert len(results.stress.on_named_selection("_FIXEDSU").eval()[0].scoping) == 222
    all_time_ns = results.stress.on_named_selection("_FIXEDSU").on_all_time_freqs.eval()
    assert len(all_time_ns) == 45
    assert len(all_time_ns[0].scoping) == 222
    assert len(all_time_ns[19].scoping) == 222


def test_result_no_memory(plate_msup):
    model = dpf.core.Model(plate_msup)
    assert len(model.results.elastic_strain.on_all_time_freqs.eval()) == 20
    assert len(model.results.elastic_strain.eval()) == 1


def test_result_stress_location_model(plate_msup):
    model = dpf.core.Model(plate_msup)
    stress = model.results.stress
    fc = (
        stress.on_mesh_scoping(dpf.core.Scoping(ids=[1, 2], location=dpf.core.locations.elemental))
        .on_location(dpf.core.locations.nodal)
        .eval()
    )
    assert fc[0].location == "Nodal"


def test_result_time_scoping(plate_msup):
    model = dpf.core.Model(plate_msup)
    stress = model.results.stress
    fc = stress.on_time_scoping([1, 2, 3, 19]).eval()
    assert len(fc) == 4
    fc = stress.on_time_scoping([0.115, 0.125]).eval()
    assert len(fc) == 2
    assert np.allclose(fc.time_freq_support.time_frequencies.data, np.array([0.115, 0.125]))


def test_result_split_subset(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    vol = model.results.elemental_volume
    if server_meet_version("9.0", model._server):
        assert len(vol.split_by_body.eval()) == 13
    else:
        assert len(vol.split_by_body.eval()) == 11
    assert len(vol.split_by_body.eval()[0].scoping) == 105
    assert len(vol.on_mesh_scoping([1, 2, 3, 10992]).split_by_body.eval()) == 2
    assert len(vol.eval()[0].scoping) == 3
    assert len(vol.eval()[1].scoping) == 1


def test_result_not_dynamic(plate_msup):
    dpf.core.settings.set_dynamic_available_results_capability(False)
    model = dpf.core.Model(plate_msup)
    assert isinstance(model.results, dpf.core.results.CommonResults)
    stress = model.results.stress
    fc = stress.on_time_scoping([1, 2, 3, 19]).eval()
    assert len(fc) == 4
    fc = stress.on_time_scoping([0.115, 0.125]).eval()
    assert len(fc) == 2
    assert np.allclose(fc.time_freq_support.time_frequencies.data, np.array([0.115, 0.125]))
    assert fc[0].unit == "Pa"
    dis = model.results.displacement().eval()
    dpf.core.settings.set_dynamic_available_results_capability(True)


def test_model_meshes_container(simple_bar):
    data_source = dpf.core.DataSources(simple_bar)
    model = dpf.core.Model(data_source)
    assert len(model.metadata.meshes_container) == 1
    assert model.metadata.meshes_container[0].nodes.n_nodes == 3751


def test_model_meshes_provider(simple_bar):
    data_source = dpf.core.DataSources(simple_bar)
    model = dpf.core.Model(data_source)
    meshes = model.metadata.meshes_provider.eval()
    assert len(meshes) == 1
    assert meshes[0].nodes.n_nodes == 3751


# ---------------------------------------------------------------------------
# StreamsContainer-based construction
# ---------------------------------------------------------------------------


def _get_streams_container(path):
    """Helper: open a path with a plain Model and return its StreamsContainer."""
    base_model = dpf.core.Model(path)
    return base_model.metadata.streams_provider.outputs.streams_container()


def test_model_from_streams_container(simple_bar):
    sc = _get_streams_container(simple_bar)
    model = dpf.core.Model(sc)
    assert model is not None
    assert "displacement" in model.metadata.result_info


def test_model_metadata_from_streams_container(simple_bar):
    sc = _get_streams_container(simple_bar)
    model = dpf.core.Model(sc)
    assert model.metadata.result_info is not None
    assert model.metadata.time_freq_support is not None
    assert model.metadata.meshed_region is not None
    # data_sources is populated from the StreamsContainer's own DataSources
    assert model.metadata.data_sources is not None
    assert len(model.metadata.data_sources.result_files) > 0


def test_model_meshed_region_from_streams_container(simple_bar):
    sc = _get_streams_container(simple_bar)
    model = dpf.core.Model(sc)
    mesh = model.metadata.meshed_region
    assert mesh.nodes.n_nodes == 3751


def test_model_results_from_streams_container(simple_bar):
    sc = _get_streams_container(simple_bar)
    model = dpf.core.Model(sc)
    # results should be queryable and give correct data
    disp_fc = model.results.displacement.eval()
    assert len(disp_fc) > 0
    assert disp_fc[0].data.shape[1] == 3  # 3-component displacement


def test_model_operator_from_streams_container(simple_bar):
    sc = _get_streams_container(simple_bar)
    model = dpf.core.Model(sc)
    op = model.operator("U")
    fc = op.outputs.fields_container()
    assert len(fc) > 0


def test_model_streams_provider_is_none_for_direct_streams(simple_bar):
    """When a StreamsContainer is passed directly no extra streams_provider is created."""
    sc = _get_streams_container(simple_bar)
    model = dpf.core.Model(sc)
    assert model.metadata.streams_provider is None
    assert model.metadata._streams_container_direct is sc
    # data_sources must be populated from the StreamsContainer, not empty
    assert len(model.metadata.data_sources.result_files) > 0


def test_model_results_match_between_datasources_and_streams_container(simple_bar):
    """Results produced from a StreamsContainer must match those from a DataSources."""
    model_ds = dpf.core.Model(dpf.core.DataSources(simple_bar))
    sc = model_ds.metadata.streams_provider.outputs.streams_container()
    model_sc = dpf.core.Model(sc)

    field_ds = model_ds.results.displacement.eval()[0]
    field_sc = model_sc.results.displacement.eval()[0]
    iden = dpf.core.operators.logic.identical_fields(field_ds, field_sc)
    assert iden.outputs.boolean()


def test_model_release_streams_from_streams_container(simple_bar):
    """release_streams() must not raise when using a direct StreamsContainer."""
    sc = _get_streams_container(simple_bar)
    model = dpf.core.Model(sc)
    # Should not raise
    model.metadata.release_streams()


def test_model_del_releases_internally_created_streams(simple_bar):
    """Model.__del__ must release streams created internally (from path / DataSources)."""
    model = dpf.core.Model(simple_bar)
    metadata = model.metadata  # ensure lazy-init is done
    with patch.object(metadata, "release_streams") as mock_release:
        del model
        gc.collect()
        mock_release.assert_called_once()


def test_model_del_does_not_release_external_streams(simple_bar):
    """Model.__del__ must NOT release a StreamsContainer that was provided by the caller."""
    sc = _get_streams_container(simple_bar)
    model = dpf.core.Model(sc)
    metadata = model.metadata  # ensure lazy-init is done
    with patch.object(metadata, "release_streams") as mock_release:
        del model
        gc.collect()
        mock_release.assert_not_called()


# @pytest.mark.skipif(NO_PLOTTING, reason="Requires system to support plotting")
# def test_displacements_plot(static_model):
#     from pyvista import CameraPosition
#     disp = static_model.results.displacement()
#     cpos = disp.outputs.fields_container()[0].plot('x')
#     assert isinstance(cpos, CameraPosition)
