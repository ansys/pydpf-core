import numpy as np
import pytest

from ansys.dpf.core import (
    fields_container_factory,
    fields_factory,
    mesh_scoping_factory,
    time_freq_scoping_factory,
)
from ansys.dpf.core import Model
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core.common import locations


def test_create_matrix_field():
    f = fields_factory.create_matrix_field(3, 2, 5)
    assert f is not None
    comp_count = f.component_count
    assert comp_count == 10


def test_create_tensor_field():
    f = fields_factory.create_tensor_field(4)
    assert f is not None
    assert f.component_count == 6


def test_create_scalar_field():
    f = fields_factory.create_scalar_field(4)
    assert f is not None
    assert f.component_count == 1


def _vector_comparison(f):
    assert f is not None
    assert f.component_count == 3
    ids = [1, 2]
    f.scoping.ids = ids
    d = [0, 1, 2, 3, 4, 5]
    f.data = d
    entity_data = f.get_entity_data_by_id(1)
    assert entity_data[0][0] == 0
    assert entity_data[0][1] == 1
    assert entity_data[0][2] == 2
    entity_data = f.get_entity_data_by_id(2)
    assert entity_data[0][0] == 3
    assert entity_data[0][1] == 4
    assert entity_data[0][2] == 5
    assert f.size == 6
    assert f.elementary_data_count == 2


def test_create_vector_field():
    f = fields_factory.create_vector_field(2, 3)
    _vector_comparison(f)


def test_create_3d_vector_field():
    f = fields_factory.create_3d_vector_field(2)
    _vector_comparison(f)


def test_over_time_freq_fields_container_1():
    f1 = fields_factory.create_scalar_field(25)
    f2 = fields_factory.create_scalar_field(31)
    fc = fields_container_factory.over_time_freq_fields_container([f1, f2])
    labels = fc.labels
    assert labels == ["time"]
    assert len(fc) == 2
    f1_result = fc.get_field_by_time_complex_ids(1)
    f2_result = fc.get_field_by_time_complex_ids(2)
    assert f1_result.location == locations.nodal
    assert f2_result.location == locations.nodal


def test_over_time_freq_fields_container_2(server_type):
    f1 = fields_factory.create_vector_field(24, 4, server=server_type)
    f2 = fields_factory.create_vector_field(32, 4, location=locations.elemental, server=server_type)
    fc = fields_container_factory.over_time_freq_fields_container(
        {0.43: f1, 1.12: f2}, "Hz", server=server_type
    )
    labels = fc.labels
    assert labels == ["time"]
    assert len(fc) == 2
    f1_result = fc.get_field_by_time_complex_ids(1)
    f2_result = fc.get_field_by_time_complex_ids(2)
    assert f1_result.location == locations.nodal
    assert f2_result.location == locations.elemental
    support = fc.time_freq_support
    assert len(support.time_frequencies) == 2
    assert support.time_frequencies.data[0] == 0.43
    assert support.time_frequencies.data[1] == 1.12


def test_over_time_freq_complex_fields_container_1():
    f1 = fields_factory.create_scalar_field(25)
    f2 = fields_factory.create_scalar_field(31)
    f1_im = fields_factory.create_scalar_field(25)
    f2_im = fields_factory.create_scalar_field(31)
    fc = fields_container_factory.over_time_freq_complex_fields_container([f1, f2], [f1_im, f2_im])
    labels = fc.labels
    assert labels == ["complex", "time"]
    assert len(fc) == 4
    f1_result = fc.get_field_by_time_complex_ids(1, 0)
    f2_result = fc.get_field_by_time_complex_ids(2, 0)
    f1_result_im = fc.get_field_by_time_complex_ids(1, 1)
    f2_result_im = fc.get_field_by_time_complex_ids(2, 1)
    assert f1_result.location == locations.nodal
    assert f2_result.location == locations.nodal
    assert f1_result_im.location == locations.nodal
    assert f2_result_im.location == locations.nodal
    f1_result = fc.get_field_by_time_id(1)
    f2_result = fc.get_field_by_time_id(2)
    f1_result_im = fc.get_imaginary_field(1)
    f2_result_im = fc.get_imaginary_field(2)
    assert f1_result.location == locations.nodal
    assert f2_result.location == locations.nodal
    assert f1_result_im.location == locations.nodal
    assert f2_result_im.location == locations.nodal


def test_over_time_freq_complex_fields_container_2():
    f1 = fields_factory.create_scalar_field(25, locations.elemental)
    f2 = fields_factory.create_scalar_field(31)
    f1_im = fields_factory.create_scalar_field(25, locations.elemental)
    f2_im = fields_factory.create_scalar_field(31)
    fc = fields_container_factory.over_time_freq_complex_fields_container(
        {0.42: f1, 1.10: f2}, {0.42: f1_im, 1.10: f2_im}, "Hz"
    )
    labels = fc.labels
    assert labels == ["complex", "time"]
    assert len(fc) == 4
    f1_result = fc.get_field_by_time_id(1)
    f2_result = fc.get_field_by_time_id(2)
    f1_result_im = fc.get_imaginary_field(1)
    f2_result_im = fc.get_imaginary_field(2)
    assert f1_result.location == locations.elemental
    assert f2_result.location == locations.nodal
    assert f1_result_im.location == locations.elemental
    assert f2_result_im.location == locations.nodal
    support = fc.time_freq_support
    assert len(support.time_frequencies) == 2
    assert len(support.complex_frequencies) == 2
    assert support.time_frequencies.data[0] == 0.42
    assert support.time_frequencies.data[1] == 1.1
    assert support.complex_frequencies.data[0] == 0.42
    assert support.complex_frequencies.data[1] == 1.1


def test_over_time_freq_complex_fields_container_3():
    f1 = fields_factory.create_scalar_field(25, locations.elemental)
    f2 = fields_factory.create_scalar_field(31)
    f1_im = fields_factory.create_scalar_field(25, locations.elemental)
    f2_im = fields_factory.create_scalar_field(31)
    with pytest.raises(dpf_errors.DpfValueError):
        fields_container_factory.over_time_freq_complex_fields_container(
            {0.42: f1, 1.10: f2}, [f1_im, f2_im], "Hz"
        )
    with pytest.raises(dpf_errors.DpfValueError):
        fields_container_factory.over_time_freq_complex_fields_container(
            [f1, f2], {0.42: f1_im, 1.10: f2_im}, "Hz"
        )


def test_over_time_freq_complex_int_fields_container():
    freq = [25, 50, 100, 200, 400]
    reals = {}
    ims = {}
    for k, f in enumerate(freq):
        reals[f] = fields_factory.create_scalar_field(1)
        ims[f] = fields_factory.create_scalar_field(1)
    cplx_fc = fields_container_factory.over_time_freq_complex_fields_container(
        reals, ims, time_freq_unit="Hz"
    )
    assert np.allclose(cplx_fc.time_freq_support.time_frequencies.data, freq)


def test_complex_fields_container():
    freal = fields_factory.create_scalar_field(25)
    fim = fields_factory.create_scalar_field(25)
    fc = fields_container_factory.complex_fields_container(freal, fim)
    assert fc.labels == ["complex"]
    assert len(fc) == 2
    freal_result = fc.get_field_by_time_complex_ids(complexid=0)
    fim_result = fc.get_field_by_time_complex_ids(complexid=1)
    assert freal_result.component_count == 1
    assert fim_result.component_count == 1


def test_scoping_by_set():
    scop = time_freq_scoping_factory.scoping_by_set(2)
    assert scop is not None
    assert len(scop.ids) == 1
    assert scop.ids[0] == 2
    assert scop.location == locations.time_freq


def test_scoping_by_sets():
    scop = time_freq_scoping_factory.scoping_by_sets([2, 5])
    assert scop is not None
    assert len(scop.ids) == 2
    assert scop.ids[0] == 2
    assert scop.ids[1] == 5
    assert scop.location == locations.time_freq


def test_scoping_by_load_step():
    scop = time_freq_scoping_factory.scoping_by_load_step(2)
    assert scop is not None
    assert len(scop.ids) == 1
    assert scop.ids[0] == 2
    assert scop.location == locations.time_freq_step


def test_scoping_by_load_steps():
    scop = time_freq_scoping_factory.scoping_by_load_steps([2, 5])
    assert scop is not None
    assert len(scop.ids) == 2
    assert scop.ids[0] == 2
    assert scop.ids[1] == 5
    assert scop.location == locations.time_freq_step


def test_scoping_by_step_and_substep(plate_msup):
    model = Model(plate_msup)
    scop = time_freq_scoping_factory.scoping_by_step_and_substep(
        1, 2, model.metadata.time_freq_support
    )
    assert scop is not None
    assert len(scop.ids) == 1
    assert scop.ids[0] == 2
    assert scop.location == locations.time_freq


def test_scoping_by_step_and_substep_from_model(plate_msup):
    model = Model(plate_msup)
    scop = time_freq_scoping_factory.scoping_by_step_and_substep_from_model(1, 2, model)
    assert scop is not None
    assert len(scop.ids) == 1
    assert scop.ids[0] == 2
    assert scop.location == locations.time_freq


def test_scoping_on_all_freqs(plate_msup):
    model = Model(plate_msup)
    scop = time_freq_scoping_factory.scoping_on_all_time_freqs(model)
    assert scop is not None
    assert np.allclose(scop.ids, range(1, 21))
    scop = time_freq_scoping_factory.scoping_on_all_time_freqs(model.metadata.time_freq_support)
    assert scop is not None
    assert np.allclose(scop.ids, range(1, 21))


def test_nodal_scoping():
    scop = mesh_scoping_factory.nodal_scoping([2, 5, 10])
    assert scop is not None
    assert len(scop.ids) == 3
    assert scop.ids[0] == 2
    assert scop.ids[1] == 5
    assert scop.ids[2] == 10
    assert scop.location == locations.nodal


def test_elemental_scoping():
    scop = mesh_scoping_factory.elemental_scoping([2, 7, 11])
    assert scop is not None
    assert len(scop.ids) == 3
    assert scop.ids[0] == 2
    assert scop.ids[1] == 7
    assert scop.ids[2] == 11
    assert scop.location == locations.elemental


def test_named_selection_scoping(model_with_ns):
    model = Model(model_with_ns)
    print(model.metadata.available_named_selections)
    scop = mesh_scoping_factory.named_selection_scoping("SELECTION", model)
    assert scop is not None
    assert len(scop.ids) != 0
