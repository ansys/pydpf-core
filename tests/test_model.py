import os

import numpy as np
import pytest

from ansys import dpf

# enable off_screen plotting
import pyvista as pv
pv.OFF_SCREEN = True

# without xserver
from pyvista.plotting import system_supports_plotting
NO_PLOTTING = not system_supports_plotting()



if 'AWP_UNIT_TEST_FILES' in os.environ:
    unit_test_files = os.environ['AWP_UNIT_TEST_FILES']
else:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')


TEST_FILE_PATH = os.path.join(unit_test_files, 'DataProcessing', 'rst_operators',
                              'ASimpleBar.rst')

# start server
if not dpf.core.has_local_server():
    dpf.core.start_local_server()


@pytest.fixture(scope='module')
def simple_bar_model():
    return dpf.core.Model(TEST_FILE_PATH)


def test_model_from_data_source():
    data_source = dpf.core.DataSources(TEST_FILE_PATH)
    model = dpf.core.Model(data_source)
    assert 'displacement' in model.metadata.result_info
    


def test_model_metadata_from_data_source():
    data_source = dpf.core.DataSources(TEST_FILE_PATH)
    model = dpf.core.Model(data_source)
    assert model.metadata.result_info != None
    assert model.metadata.time_freq_support != None
    assert model.metadata.meshed_region != None
    assert model.metadata.data_sources != None


def test_displacements_eval(simple_bar_model):
    disp = simple_bar_model.results.displacement()
    fc = disp.outputs.fields_container()
    disp_field_from_eval = fc[0]

    fc_from_outputs = disp.outputs.fields_container()[0]
    assert np.allclose(disp_field_from_eval.data, fc_from_outputs.data)


def test_extract_component(simple_bar_model):
    disp = simple_bar_model.results.displacement()
    disp = disp.X()
    disp_field = disp.outputs.fields_container()[0]
    assert isinstance(disp_field.data, np.ndarray)
    
def test_kinetic(simple_bar_model):
    e = simple_bar_model.results.kinetic_energy()
    energy = e.outputs.fields_container()[0]
    assert isinstance(energy.data, np.ndarray)

def test_print_model(simple_bar_model):
    print(simple_bar_model)
    
@pytest.mark.skipif(NO_PLOTTING, reason="Requires system to support plotting")
def test_displacements_plot(simple_bar_model):
    disp = simple_bar_model.displacement()
    cpos = disp.outputs.fields_container()[0].plot('x')
    assert isinstance(cpos, pv.CameraPosition)
