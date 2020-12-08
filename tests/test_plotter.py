from ansys import dpf
from ansys.dpf.core import Model, Operator
from ansys.dpf.core.plotter import Plotter as DpfPlotter
import pyvista as pv
import os

if not dpf.core.has_local_server():
    dpf.core.start_local_server()
    

if 'AWP_UNIT_TEST_FILES' in os.environ:
    unit_test_files = os.environ['AWP_UNIT_TEST_FILES']
else:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')
    
FILE_PATH = os.path.join(unit_test_files, 'DataProcessing', 'rst_operators',
                              'allKindOfComplexity.rst')

TRANSIENT_FILE_PATH = os.path.join(unit_test_files, 'DataProcessing', 'expansion', 
                                   'msup', 'Transient', 'plate1','file.rst')


def test_chart_plotter():
    model = Model(TRANSIENT_FILE_PATH)
    mesh = model.metadata.meshed_region
    tfq = model.metadata.time_freq_support
    timeids = list(range(1,tfq.n_sets+1))
    disp = model.results.displacement()
    disp.inputs.time_scoping.connect(timeids)
    new_fields_container = disp.get_output(0, dpf.core.types.fields_container)
    pl = DpfPlotter(model.metadata.meshed_region)
    ret = pl.plot_chart(new_fields_container)
    assert ret

def test_plotter_on_mesh():
    model = Model(FILE_PATH)
    mesh = model.metadata.meshed_region
    pl = DpfPlotter(model.metadata.meshed_region)
    cpos = pl.plot_mesh()
    cpos_check = [(0.06757782231616599, 0.052577822316165986, 0.05304657231616599),
                 (0.02, 0.005, 0.005468749999999999),
                 (0.0, 0.0, 1.0)]
    assert cpos==cpos_check

def test_plotter_on_field():
    model = Model(FILE_PATH)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Elemental')
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    field = fc[1]
    pl = DpfPlotter(model.metadata.meshed_region)
    fields_container = dpf.core.FieldsContainer()
    fields_container.add_label('time')
    fields_container.add_field({'time':1}, field)    
    cpos = pl.plot_contour(fields_container)
    cpos_check = [(0.06757782231616599, 0.052577822316165986, 0.05304657231616599),
     (0.02, 0.005, 0.005468749999999999),
     (0.0, 0.0, 1.0)]
    assert cpos == cpos_check
