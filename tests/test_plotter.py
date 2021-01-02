import unittest

from pyvista.plotting.renderer import CameraPosition
import pytest

from ansys import dpf
from ansys.dpf.core import Model, Operator
from ansys.dpf.core.plotter import Plotter as DpfPlotter
from ansys.dpf import core
from ansys.dpf.core import errors as dpf_errors


def test_chart_plotter(plate_msup):
    model = Model(plate_msup)
    mesh = model.metadata.meshed_region
    tfq = model.metadata.time_freq_support
    timeids = list(range(1, tfq.n_sets + 1))
    disp = model.results.displacement()
    disp.inputs.time_scoping.connect(timeids)
    new_fields_container = disp.get_output(0, dpf.core.types.fields_container)
    pl = DpfPlotter(model.metadata.meshed_region)
    ret = pl.plot_chart(new_fields_container)
    assert ret


def test_plotter_on_mesh(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    pl = DpfPlotter(model.metadata.meshed_region)
    cpos = pl.plot_mesh()
    assert isinstance(cpos, CameraPosition)


def test_plotter_on_field(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Elemental')
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    field = fc[1]
    pl = DpfPlotter(model.metadata.meshed_region)
    fields_container = dpf.core.FieldsContainer()
    fields_container.add_label('time')
    fields_container.add_field({'time': 1}, field)
    cpos = pl.plot_contour(fields_container)
    assert isinstance(cpos, CameraPosition)


def test_plotter_on_fields_container_elemental(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Elemental')
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    pl = DpfPlotter(model.metadata.meshed_region)
    cpos = pl.plot_contour(fc)
    assert isinstance(cpos, CameraPosition)


def test_plotter_on_fields_container_nodal(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Elemental')
    avg_op = Operator("to_nodal_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    pl = DpfPlotter(model.metadata.meshed_region)
    cpos = pl.plot_contour(fc)
    assert isinstance(cpos, CameraPosition)
    

def test_plot_fieldscontainer_on_mesh(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Elemental')
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    mesh.plot(fc)
    
    
def test_field_elemental_plot(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Elemental')
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    f = fc[1]
    f.plot()


def test_field_nodal_plot(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Elemental')
    avg_op = Operator("to_nodal_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    f = fc[1]
    f.plot()
    

def test_field_solid_plot(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Nodal')
    fc = stress.outputs.fields_container()
    f = fc[1]
    f.plot()


def test_field_shell_plot(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Nodal')
    fc = stress.outputs.fields_container()
    f = fc[0]
    f.plot()


def test_field_solid_plot_scoping_nodal(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Nodal')
    scoping = core.Scoping()
    scoping.location = 'Nodal'
    l = list(range(0, 400))
    l += list(range(1500, 2000))
    l += list(range(2200, 2600))
    scoping.ids = l
    stress.inputs.mesh_scoping.connect(scoping)
    s = stress.outputs.fields_container()
    f = s[0]
    f.plot()


def test_field_shell_plot_scoping_elemental(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    scoping = core.Scoping()
    scoping.location = 'Elemental'
    l = list(range(3000,4500))
    scoping.ids = l
    stress.inputs.mesh_scoping.connect(scoping)
    avg = core.Operator("to_elemental_fc")
    avg.inputs.fields_container.connect(stress.outputs.fields_container)
    s = avg.outputs.fields_container()
    f = s[1]
    f.plot(shell_layers = core.ShellLayers.TOP)


def test_plot_fieldscontainer_on_mesh_scoping(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Nodal')
    scoping = core.Scoping()
    scoping.location = 'Nodal'
    l = list(range(0, 400))
    l += list(range(1500, 2000))
    l += list(range(2200, 2600))
    scoping.ids = l
    stress.inputs.mesh_scoping.connect(scoping)
    s = stress.outputs.fields_container()
    mesh.plot(s, shell_layers = core.ShellLayers.TOP)


def test_plot_fields_on_mesh_scoping(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect('Nodal')
    scoping = core.Scoping()
    scoping.location = 'Nodal'
    l = list(range(0, 400))
    l += list(range(1500, 2000))
    l += list(range(2200, 2600))
    scoping.ids = l
    stress.inputs.mesh_scoping.connect(scoping)
    s = stress.outputs.fields_container()
    mesh.plot(s[0])


def test_throw_on_several_time_steps(plate_msup):
    model = core.Model(plate_msup)
    scoping = core.Scoping()
    scoping.ids = range(3, len(model.metadata.time_freq_support.frequencies) + 1)
    stress = model.results.displacement()
    stress.inputs.time_scoping.connect(scoping)
    fc = stress.outputs.fields_container()
    mesh = model.metadata.meshed_region
    with pytest.raises(dpf_errors.FieldContainerPlottingError):
        mesh.plot(fc)


def test_throw_complex_file(complex_model):
    model = core.Model(complex_model)
    stress = model.results.displacement()
    fc = stress.outputs.fields_container()
    mesh = model.metadata.meshed_region
    with pytest.raises(dpf_errors.ComplexPlottingError):
        mesh.plot(fc)
