import numpy as np
import pytest
from pyvista.plotting import system_supports_plotting

from ansys import dpf
from ansys.dpf.core import examples
import functools

NO_PLOTTING = not system_supports_plotting()


@pytest.fixture()
def static_model():
    return dpf.core.Model(examples.static_rst)


def test_model_from_data_source(simple_bar):
    data_source = dpf.core.DataSources(simple_bar)
    model = dpf.core.Model(data_source)
    assert 'displacement' in model.metadata.result_info


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
    assert 'Physics Type: mecanic' in str(static_model)
    assert '81' in str(static_model)
    assert 'Unit: m' in str(static_model)
    
    
def test_connect_inputs_in_constructor_model(plate_msup):
    model = dpf.core.Model(plate_msup)
    u = model.results.displacement(0.015)
    fc =  u.outputs.fields_container()
    assert len(fc) ==1
    assert np.allclose(fc[0].data[0],[5.12304110e-14, 3.64308310e-04, 5.79805917e-06])
    scop = dpf.core.Scoping()
    scop.ids=list(range(1,21))
    u = model.results.displacement(0.015, scop)
    fc = u.outputs.fields_container()
    assert len(fc) ==1
    assert np.allclose(fc[0].data[0],[9.66814331e-16, 6.82591973e-06, 1.35911110e-06])
    assert fc[0].shape == (20, 3)


def test_named_selection_model(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    ns = model.metadata.available_named_selections
    assert ns ==  ['_CM82', '_CM86UX_XP', '_DISPNONZEROUX', '_DISPZEROUZ', '_ELMISC', '_FIXEDSU']
    scop = model.metadata.named_selection("_CM86UX_XP")
    assert len(scop)==481
    assert scop.location == dpf.core.locations().nodal

def test_all_result_operators_exist(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    res = model.results
    for key in res.__dict__:
        if isinstance(res.__dict__[key], functools.partial):
            res.__dict__[key]()

# @pytest.mark.skipif(NO_PLOTTING, reason="Requires system to support plotting")
# def test_displacements_plot(static_model):
#     from pyvista import CameraPosition
#     disp = static_model.results.displacement()
#     cpos = disp.outputs.fields_container()[0].plot('x')
#     assert isinstance(cpos, CameraPosition)
