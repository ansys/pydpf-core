from pyvista.plotting.renderer import CameraPosition

from ansys import dpf
from ansys.dpf.core import Model, Operator
from ansys.dpf.core.plotter import Plotter as DpfPlotter


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
    mesh = model.metadata.meshed_region
    pl = DpfPlotter(model.metadata.meshed_region)
    cpos = pl.plot_mesh()
    assert isinstance(cpos, CameraPosition)


def test_plotter_on_field(allkindofcomplexity):
    model = Model(allkindofcomplexity)
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
    fields_container.add_field({'time': 1}, field)
    cpos = pl.plot_contour(fields_container)
    assert isinstance(cpos, CameraPosition)
