import pytest

from ansys import dpf
from ansys.dpf import core
from ansys.dpf.core import Model, Operator
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core import misc
from conftest import running_docker

if misc.module_exists("pyvista"):
    HAS_PYVISTA = True
    from ansys.dpf.core.plotter import Plotter as DpfPlotter
    from pyvista.plotting.renderer import CameraPosition  # noqa: F401
else:
    HAS_PYVISTA = False


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
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


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_on_mesh(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    pl = DpfPlotter(model.metadata.meshed_region)
    cpos = pl.plot_mesh()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_on_field(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Elemental")
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    field = fc[1]
    pl = DpfPlotter(model.metadata.meshed_region)
    fields_container = dpf.core.FieldsContainer()
    fields_container.add_label("time")
    fields_container.add_field({"time": 1}, field)
    cpos = pl.plot_contour(fields_container)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_on_fields_container_elemental(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Elemental")
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    pl = DpfPlotter(model.metadata.meshed_region)
    cpos = pl.plot_contour(fc)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_on_fields_container_nodal(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Elemental")
    avg_op = Operator("to_nodal_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    pl = DpfPlotter(model.metadata.meshed_region)
    cpos = pl.plot_contour(fc)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plot_fieldscontainer_on_mesh(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Elemental")
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    mesh.plot(fc)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_field_elemental_plot(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Elemental")
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    f = fc[1]
    f.plot()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_field_nodal_plot(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Elemental")
    avg_op = Operator("to_nodal_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    f = fc[1]
    f.plot()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_field_solid_plot(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Nodal")
    fc = stress.outputs.fields_container()
    f = fc[1]
    f.plot()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_field_shell_plot(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Nodal")
    fc = stress.outputs.fields_container()
    f = fc[0]
    f.plot()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_field_solid_plot_scoping_nodal(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Nodal")
    scoping = core.Scoping()
    scoping.location = "Nodal"
    l = list(range(0, 400))
    l += list(range(1500, 2000))
    l += list(range(2200, 2600))
    scoping.ids = l
    stress.inputs.mesh_scoping.connect(scoping)
    s = stress.outputs.fields_container()
    f = s[0]
    f.plot()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_field_shell_plot_scoping_elemental(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    scoping = core.Scoping()
    scoping.location = "Elemental"
    l = list(range(3000, 4500))
    scoping.ids = l
    stress.inputs.mesh_scoping.connect(scoping)
    avg = core.Operator("to_elemental_fc")
    avg.inputs.fields_container.connect(stress.outputs.fields_container)
    s = avg.outputs.fields_container()
    f = s[1]
    f.plot(shell_layers=core.shell_layers.top)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plot_fieldscontainer_on_mesh_scoping(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Nodal")
    scoping = core.Scoping()
    scoping.location = "Nodal"
    l = list(range(0, 400))
    l += list(range(1500, 2000))
    l += list(range(2200, 2600))
    scoping.ids = l
    stress.inputs.mesh_scoping.connect(scoping)
    s = stress.outputs.fields_container()
    mesh.plot(s, shell_layers=core.shell_layers.top)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plot_fields_on_mesh_scoping(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Nodal")
    scoping = core.Scoping()
    scoping.location = "Nodal"
    l = list(range(0, 400))
    l += list(range(1500, 2000))
    l += list(range(2200, 2600))
    scoping.ids = l
    stress.inputs.mesh_scoping.connect(scoping)
    s = stress.outputs.fields_container()
    mesh.plot(s[0])


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plot_fields_on_mesh_scoping_title(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Nodal")
    scoping = core.Scoping()
    scoping.location = "Nodal"
    l = list(range(0, 400))
    l += list(range(1500, 2000))
    l += list(range(2200, 2600))
    scoping.ids = l
    stress.inputs.mesh_scoping.connect(scoping)
    s = stress.outputs.fields_container()
    mesh.plot(s[0], text="test")


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_throw_on_several_time_steps(plate_msup):
    model = core.Model(plate_msup)
    scoping = core.Scoping()
    scoping.ids = range(3, len(model.metadata.time_freq_support.time_frequencies) + 1)
    stress = model.results.displacement()
    stress.inputs.time_scoping.connect(scoping)
    fc = stress.outputs.fields_container()
    mesh = model.metadata.meshed_region
    with pytest.raises(dpf_errors.FieldContainerPlottingError):
        mesh.plot(fc)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_throw_complex_file(complex_model):
    model = core.Model(complex_model)
    stress = model.results.displacement()
    fc = stress.outputs.fields_container()
    mesh = model.metadata.meshed_region
    with pytest.raises(dpf_errors.ComplexPlottingError):
        mesh.plot(fc)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
@pytest.mark.skipif(running_docker, reason="Path hidden within docker container")
def test_plot_contour_using_vtk_file(complex_model):
    model = core.Model(complex_model)
    stress = model.results.displacement()
    fc = stress.outputs.fields_container()
    pl = DpfPlotter(model.metadata.meshed_region)
    pl._plot_contour_using_vtk_file(fc)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plot_meshes_container_1(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    split_mesh_op = core.Operator("split_mesh")
    split_mesh_op.connect(7, mesh)
    split_mesh_op.connect(13, "mat")
    meshes_cont = split_mesh_op.get_output(0, core.types.meshes_container)
    disp_op = core.Operator("U")
    disp_op.connect(7, meshes_cont)
    ds = core.DataSources(multishells)
    disp_op.connect(4, ds)
    disp_fc = disp_op.outputs.fields_container()
    meshes_cont.plot(disp_fc)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plot_meshes_container_2(multishells):
    from ansys.dpf import core
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    split_mesh_op = core.Operator("split_mesh")
    split_mesh_op.connect(7, mesh)
    split_mesh_op.connect(13, "mat")
    meshes_cont = split_mesh_op.get_output(0, core.types.meshes_container)
    disp_op = core.Operator("U")
    disp_op.connect(7, meshes_cont)
    ds = core.DataSources(multishells)
    disp_op.connect(4, ds)
    disp_fc = disp_op.outputs.fields_container()
    meshes_cont_2 = core.MeshesContainer()
    meshes_cont_2.labels = meshes_cont.labels
    disp_fc_2 = core.FieldsContainer()
    disp_fc_2.labels = meshes_cont.labels
    for i in range(len(meshes_cont) - 10):
        lab = meshes_cont.get_label_space(i)
        meshes_cont_2.add_mesh(lab, meshes_cont.get_mesh(lab))
        disp_fc_2.add_field(lab, disp_fc.get_field(lab))
    meshes_cont_2.plot(disp_fc_2)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plot_meshes_container_only(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    split_mesh_op = core.Operator("split_mesh")
    split_mesh_op.connect(7, mesh)
    split_mesh_op.connect(13, "mat")
    meshes_cont = split_mesh_op.get_output(0, core.types.meshes_container)
    meshes_cont.plot()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_add_mesh(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    split_mesh_op = core.Operator("split_mesh")
    split_mesh_op.connect(7, mesh)
    split_mesh_op.connect(13, "mat")
    meshes_cont = split_mesh_op.get_output(0, core.types.meshes_container)
    from ansys.dpf.core.plotter import DpfPlotter
    pl = DpfPlotter()
    for i in range(len(meshes_cont) - 10):
        pl.add_mesh(meshes_cont[i])
    pl.show_figure()


def create_mesh_and_field_mapped(multishells):
    # get metadata
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    disp_fc = model.results.displacement().outputs.fields_container()
    field = disp_fc[0]
    # coordinates field to map
    coordinates = [[-0.02, 0.006, 0.014], [-0.02, 0.006, 0.012],
                   [-0.018, 0.006, 0.012], [-0.018, 0.006, 0.014]]
    field_coord = core.Field()
    field_coord.location = core.locations.nodal
    field_coord.data = coordinates
    scoping = core.Scoping()
    scoping.location = core.locations.nodal
    scoping.ids = list(range(1, len(coordinates) + 1))
    field_coord.scoping = scoping
    # mapping operator
    mapping_operator = core.Operator("mapping")
    mapping_operator.inputs.fields_container.connect(disp_fc)
    mapping_operator.inputs.coordinates.connect(field_coord)
    mapping_operator.inputs.mesh.connect(mesh)
    mapping_operator.inputs.create_support.connect(True)
    fields_mapped = mapping_operator.outputs.fields_container()
    # mesh path
    assert len(fields_mapped) == 1
    field_m = fields_mapped[0]
    mesh_m = field_m.meshed_region
    return field, field_m, mesh, mesh_m


def create_mesh_and_field_mapped_2(multishells):
    # get metadata
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    disp_fc = model.results.displacement().outputs.fields_container()
    field = disp_fc[0]
    # coordinates field to map
    coordinates = [[-0.0195, 0.006, -0.0025]]
    for i in range(1, 101):
        coord_copy = []
        coord_copy.append(coordinates[0][0])
        coord_copy.append(coordinates[0][1])
        coord_copy.append(coordinates[0][2])
        coord_copy[0] = coord_copy[0] + i * 0.0003
        coordinates.append(coord_copy)
    ref = [-0.0155, 0.00600634, -0.0025]
    coordinates.append(ref)
    for i in range(1, 101):
        coord_copy = []
        coord_copy.append(ref[0])
        coord_copy.append(ref[1])
        coord_copy.append(ref[2])
        coord_copy[0] = coord_copy[0] + i * 0.0003
        coordinates.append(coord_copy)
    ref = [-0.0125, 0.00600507, -0.0025]
    coordinates.append(ref)
    for i in range(1, 101):
        coord_copy = []
        coord_copy.append(ref[0])
        coord_copy.append(ref[1])
        coord_copy.append(ref[2])
        coord_copy[0] = coord_copy[0] + i * 0.0003
        coordinates.append(coord_copy)
    ref = [-0.0125, 0.00600444, -0.0025]
    coordinates.append(ref)
    for i in range(1, 101):
        coord_copy = []
        coord_copy.append(ref[0])
        coord_copy.append(ref[1])
        coord_copy.append(ref[2])
        coord_copy[0] = coord_copy[0] + i * 0.0003
        coordinates.append(coord_copy)
    field_coord = core.Field()
    field_coord.location = core.locations.nodal
    field_coord.data = coordinates
    scoping = core.Scoping()
    scoping.location = core.locations.nodal
    scoping.ids = list(range(1, len(coordinates) + 1))
    field_coord.scoping = scoping
    # mapping operator
    mapping_operator = core.Operator("mapping")
    mapping_operator.inputs.fields_container.connect(disp_fc)
    mapping_operator.inputs.coordinates.connect(field_coord)
    mapping_operator.inputs.mesh.connect(mesh)
    mapping_operator.inputs.create_support.connect(True)
    fields_mapped = mapping_operator.outputs.fields_container()
    # mesh path
    assert len(fields_mapped) == 1
    field_m = fields_mapped[0]
    mesh_m = field_m.meshed_region
    return field, field_m, mesh, mesh_m


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plot_path_1(multishells):
    field, field_m, mesh, mesh_m = create_mesh_and_field_mapped(multishells)
    # create meshes container, fields container and plot
    meshes_cont = core.MeshesContainer()
    meshes_cont.labels = ["path"]
    meshes_cont.add_mesh({"path": 0}, mesh)
    meshes_cont.add_mesh({"path": 1}, mesh_m)
    fields_cont = core.FieldsContainer()
    fields_cont.labels = ["path"]
    fields_cont.add_field({"path": 0}, field)
    fields_cont.add_field({"path": 1}, field_m)
    meshes_cont.plot(fields_cont)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plot_path_2(multishells):
    field, field_m, mesh, mesh_m = create_mesh_and_field_mapped(multishells)
    # create plotter, add fields and plot
    from ansys.dpf.core.plotter import DpfPlotter
    pl = DpfPlotter()
    # to use outside of the window:
    # pl = DpfPlotter(notebook=False)
    pl.add_field(field_m, mesh_m, show_max=True, show_min=True)
    pl.add_field(field, mesh, style="wireframe", show_edges=True,
                 color="w", opacity=0.3)
    pl.show_figure()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plot_path_3(multishells):
    field, field_m, mesh, mesh_m = create_mesh_and_field_mapped_2(multishells)
    # create plotter, add fields and plot
    from ansys.dpf.core.plotter import DpfPlotter
    pl = DpfPlotter()
    # to use outside of the window:
    # pl = DpfPlotter(notebook=False)
    pl.add_field(field_m, mesh_m)
    pl.add_field(field, mesh, style="wireframe", show_edges=True,
                 color="w", opacity=0.3)
    pl.show_figure()


@pytest.mark.skipif(not HAS_PYVISTA, reason="This test requires pyvista")
def test_plot_min_max_labels(multishells):
    field, field_m, mesh, mesh_m = create_mesh_and_field_mapped_2(multishells)
    # create plotter, add fields and plot
    from ansys.dpf.core.plotter import DpfPlotter
    pl = DpfPlotter()
    pl.add_field(field_m, mesh_m)
    pl.add_field(field, mesh, style="wireframe", show_edges=True,
                 color="w", opacity=0.3, show_max=True, show_min=True)
    pl.show_figure()


@pytest.mark.skipif(not HAS_PYVISTA, reason="This test requires pyvista")
def test_plot_node_labels(multishells):
    field, field_m, mesh, mesh_m = create_mesh_and_field_mapped_2(multishells)
    # create plotter, add fields and plot
    from ansys.dpf.core.plotter import DpfPlotter
    pl = DpfPlotter()
    pl.add_field(field_m, mesh_m)
    my_nodes_1 = [mesh_m.nodes[0], mesh_m.nodes[10]]
    my_labels_1 = ["MyNode1", "MyNode2"]
    pl.add_node_labels(my_nodes_1, mesh_m, my_labels_1,
                       italic=True, bold=True,
                       font_size=26, text_color="white",
                       font_family="courier", shadow=True,
                       point_color="grey", point_size=20)
    pl.show_figure()
