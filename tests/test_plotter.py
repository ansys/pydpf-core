import os

import pytest

from ansys import dpf
from ansys.dpf import core
from ansys.dpf.core import Model, Operator
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core import misc
from ansys.dpf.core.helpers.streamlines import compute_streamlines
from ansys.dpf.core.plotter import plot_chart
from conftest import (
    running_docker,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0
)
from ansys.dpf.core import element_types

if misc.module_exists("pyvista"):
    HAS_PYVISTA = True
    from ansys.dpf.core.plotter import DpfPlotter, Plotter
    from pyvista.plotting.renderer import CameraPosition  # noqa: F401
else:
    HAS_PYVISTA = False


def remove_picture(picture):
    if os.path.exists(os.path.join(os.getcwd(), picture)):
        os.remove(os.path.join(os.getcwd(), picture))


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_on_model(plate_msup):
    model = Model(plate_msup)
    model.plot()
    picture = "model_plot.png"
    remove_picture(picture)
    model.plot(off_screen=True, screenshot=picture)
    assert os.path.exists(os.path.join(os.getcwd(), picture))
    remove_picture(picture)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_chart_plotter(plate_msup):
    model = Model(plate_msup)
    tfq = model.metadata.time_freq_support
    timeids = list(range(1, tfq.n_sets + 1))
    disp = model.results.displacement()
    disp.inputs.time_scoping.connect(timeids)
    new_fields_container = disp.get_output(0, dpf.core.types.fields_container)
    pl = Plotter(model.metadata.meshed_region)
    ret = pl.plot_chart(new_fields_container)
    assert ret


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_mesh_bare_plot(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    mesh.plot()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_mesh_field_plot(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Nodal")
    f = stress.outputs.fields_container()[0]
    mesh.plot(f)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_on_mesh(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    pl = DpfPlotter()
    pl.add_mesh(model.metadata.meshed_region)
    pl.show_figure()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_on_mesh_warning_notebook():
    pl = DpfPlotter()
    with pytest.warns(expected_warning=UserWarning, match="'notebook' is not a valid kwarg"):
        pl.show_figure(notebook=False)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_on_field(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Elemental")
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    field = fc[1]
    pl = Plotter(model.metadata.meshed_region)
    fields_container = dpf.core.FieldsContainer()
    fields_container.add_label("time")
    fields_container.add_field({"time": 1}, field)
    pl.plot_contour(fields_container)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_on_fields_container_elemental(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Elemental")
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    pl = Plotter(model.metadata.meshed_region)
    cpos = pl.plot_contour(fc)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_plotter_on_fields_container_nodal(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    stress = model.results.stress()
    stress.inputs.requested_location.connect("Elemental")
    avg_op = Operator("to_nodal_fc")
    avg_op.inputs.fields_container.connect(stress.outputs.fields_container)
    fc = avg_op.outputs.fields_container()
    pl = Plotter(model.metadata.meshed_region)
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
    picture = "mesh_plot.png"
    remove_picture(picture)
    mesh.plot(fc, off_screen=True, screenshot=picture)
    assert os.path.exists(os.path.join(os.getcwd(), picture))
    remove_picture(picture)


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
    picture = "field_plot.png"
    remove_picture(picture)
    f.plot(off_screen=True, screenshot=picture)
    assert os.path.exists(os.path.join(os.getcwd(), picture))
    remove_picture(picture)


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
def test_throw_shell_layers(multishells):
    model = core.Model(multishells)
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
    with pytest.raises(TypeError):
        f.plot(shell_layers="test")


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
    pl = Plotter(model.metadata.meshed_region)
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
    picture = "meshes_cont_plot.png"
    remove_picture(picture)
    meshes_cont.plot(disp_fc, off_screen=True, screenshot=picture)
    assert os.path.exists(os.path.join(os.getcwd(), picture))
    remove_picture(picture)


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
    coordinates = [
        [-0.02, 0.006, 0.014],
        [-0.02, 0.006, 0.012],
        [-0.018, 0.006, 0.012],
        [-0.018, 0.006, 0.014],
    ]
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
    pl.add_field(field, mesh, style="wireframe", show_edges=True, color="w", opacity=0.3)
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
    pl.add_field(field, mesh, style="wireframe", show_edges=True, color="w", opacity=0.3)
    pl.show_figure()


@pytest.mark.skipif(not HAS_PYVISTA, reason="This test requires pyvista")
def test_plot_min_max_labels(multishells):
    field, field_m, mesh, mesh_m = create_mesh_and_field_mapped_2(multishells)
    # create plotter, add fields and plot
    from ansys.dpf.core.plotter import DpfPlotter

    pl = DpfPlotter()
    pl.add_field(field_m, mesh_m)
    pl.add_field(
        field,
        mesh,
        style="wireframe",
        show_edges=True,
        color="w",
        opacity=0.3,
        show_max=True,
        show_min=True,
    )
    pl.show_figure()


@pytest.mark.skipif(not HAS_PYVISTA, reason="This test requires pyvista")
def test_plot_node_labels(multishells):
    field, field_m, mesh, mesh_m = create_mesh_and_field_mapped_2(multishells)
    # create plotter, add fields and plot
    from ansys.dpf.core.plotter import DpfPlotter

    pl = DpfPlotter()
    pl.add_field(field_m, mesh_m)
    my_nodes_1 = [mesh_m.nodes[0], mesh_m.nodes[10]]
    my_labels_1 = ["MyNode1"]
    pl.add_node_labels(
        my_nodes_1,
        mesh_m,
        my_labels_1,
        italic=True,
        bold=True,
        font_size=26,
        text_color="white",
        font_family="courier",
        shadow=True,
        point_color="grey",
        point_size=20,
    )
    a = pl.labels[0]
    assert len(a) == 2
    pl.show_figure()

    pl = DpfPlotter()
    my_labels_1 = ["MyNode1", None, "MyNode3"]
    pl.add_node_labels(
        mesh_m.nodes,
        mesh_m,
        my_labels_1,
    )
    pl.show_figure()


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_cpos_plot(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    mesh.plot(cpos="xy")


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_return_cpos_plot(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    ret = mesh.plot(return_cpos=True)
    assert ret


@pytest.mark.skipif(not HAS_PYVISTA, reason="This test requires pyvista")
def test_plot_chart(allkindofcomplexity):
    from ansys.dpf.core import types

    model = Model(allkindofcomplexity)
    tfq = model.metadata.time_freq_support
    timeids = list(range(1, tfq.n_sets + 1))
    disp = model.results.displacement()
    disp.inputs.time_scoping.connect(timeids)
    new_fields_container = disp.get_output(0, types.fields_container)
    plot_chart(new_fields_container)
    picture = "plot_chart.png"
    remove_picture(picture)
    plot_chart(new_fields_container, off_screen=True, screenshot=picture)
    assert os.path.exists(os.path.join(os.getcwd(), picture))
    remove_picture(picture)


@pytest.mark.skipif(not HAS_PYVISTA, reason="This test requires pyvista")
def test_plot_warped_mesh(multishells):
    model = core.Model(multishells)
    mesh = model.metadata.meshed_region
    disp_result = model.results.displacement.on_time_scoping([1])
    scale_factor = 0.001
    mesh.plot(deform_by=disp_result, scale_factor=scale_factor)
    disp_op = disp_result()
    mesh.plot(deform_by=disp_op, scale_factor=scale_factor)
    disp_fc = disp_result.eval()
    mesh.plot(deform_by=disp_fc, scale_factor=scale_factor)
    disp_field = disp_fc[0]
    mesh.plot(deform_by=disp_field, scale_factor=scale_factor)
    disp_field.plot(deform_by=disp_result, scale_factor=scale_factor)
    mesh.plot(disp_field, deform_by=disp_result, scale_factor=scale_factor)
    split_op = dpf.core.operators.mesh.split_mesh(mesh=mesh, property="mat")
    meshes_cont = split_op.get_output(output_type=dpf.core.types.meshes_container)
    meshes_cont.plot(deform_by=disp_result, scale_factor=scale_factor)
    disp_op = dpf.core.operators.result.displacement(
        data_sources=model.metadata.data_sources, mesh=meshes_cont
    )
    disp_fc = disp_op.outputs.fields_container()
    meshes_cont.plot(disp_fc, deform_by=disp_result, scale_factor=scale_factor)


@pytest.mark.skipif(not HAS_PYVISTA, reason="This test requires pyvista")
@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="Polygons are supported starting server version 5.0",
)
def test_plot_polygon():
    # Define polygon points
    polygon_points = [
        [0.02, 0.0, 0.0],
        [0.02, 0.01, 0.0],
        [0.03, 0.01, 0.0],
        [0.035, 0.005, 0.0],
        [0.03, 0.0, 0.0],
    ]
    # Define polygon connectivity
    connectivity = [0, 1, 2, 3, 4]
    # Create mesh object and add nodes and elements
    mesh = core.MeshedRegion()
    for index, node in enumerate(polygon_points):
        mesh.nodes.add_node(index, node)
    mesh.elements.add_shell_element(0, connectivity)
    mesh.plot()


@pytest.mark.skipif(not HAS_PYVISTA, reason="This test requires pyvista")
@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="Polyhedrons are supported starting server version 5.0",
)
def test_plot_polyhedron():
    # Define the coordinates
    polyhedron_points = [
        [0.02, 0.0, 0.02],
        [0.02, 0.01, 0.02],
        [0.03, 0.01, 0.02],
        [0.035, 0.005, 0.02],
        [0.03, 0.0, 0.02],
        [0.02, 0.0, 0.03],
        [0.02, 0.01, 0.03],
        [0.03, 0.01, 0.03],
        [0.035, 0.005, 0.03],
        [0.03, 0.0, 0.03],
    ]
    # Define the faces connectivity
    faces_connectivity = [
        [0, 1, 2, 3, 4],
        [0, 1, 6, 5],
        [0, 4, 9, 5],
        [4, 9, 8, 3],
        [3, 8, 7, 2],
        [2, 7, 6, 1],
        [5, 6, 7, 8, 9],
    ]
    # Define the element connectivity
    element_connectivity = [i for face in faces_connectivity for i in face]

    # Define the faces connectivity of the element
    elements_faces = [[0, 1, 2, 3, 4, 5, 6]]
    # Define the types of faces in the mesh
    faces_types = [[element_types.Polygon.value]] * 7
    # Define the types of elements in the mesh
    cell_types = [[element_types.Polyhedron.value]]

    # Create mesh object and add nodes and elements
    mesh = core.MeshedRegion()
    for index, node_coordinates in enumerate(polyhedron_points):
        mesh.nodes.add_node(index, node_coordinates)
    mesh.elements.add_solid_element(0, element_connectivity)

    # Set the "cell_types" PropertyField
    cell_types_f = core.PropertyField()
    for cell_index, cell_type in enumerate(cell_types):
        cell_types_f.append(cell_type, cell_index)
    mesh.set_property_field("eltype", cell_types_f)

    # Set the "faces_nodes_connectivity" PropertyField
    connectivity_f = core.PropertyField()
    for face_index, face_connectivity in enumerate(faces_connectivity):
        connectivity_f.append(face_connectivity, face_index)
    mesh.set_property_field("faces_nodes_connectivity", connectivity_f)

    # Set the "elements_faces_connectivity" PropertyField
    elements_faces_f = core.PropertyField()
    for element_index, element_faces in enumerate(elements_faces):
        elements_faces_f.append(element_faces, element_index)
    mesh.set_property_field("elements_faces_connectivity", elements_faces_f)

    # Set the "faces_types" PropertyField
    faces_types_f = core.PropertyField()
    for face_index, face_type in enumerate(faces_types):
        faces_types_f.append(face_type, face_index)
    mesh.set_property_field("faces_type", faces_types_f)

    # Plot the MeshedRegion
    mesh.plot()


@pytest.mark.skipif(not HAS_PYVISTA, reason="This test requires pyvista")
@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="Fluids results are supported starting server version 7.0",
)
def test_compute_and_plot_streamlines(fluent_mixing_elbow_steady_state, server_type):
    ds_fluent = fluent_mixing_elbow_steady_state(server=server_type)
    m_fluent = core.Model(data_sources=ds_fluent, server=server_type)
    meshed_region = m_fluent.metadata.meshed_region
    velocity_op = m_fluent.results.velocity()
    fc = velocity_op.outputs.fields_container()
    fc_av = core.operators.averaging.to_nodal_fc(server=server_type)
    fc_av.inputs.fields_container.connect(fc)
    field = fc_av.outputs.fields_container()[0]

    streamline_obj, src_obj = compute_streamlines(
        meshed_region=meshed_region,
        field=field,
        return_source=True,
        source_center=(0.56, 0.48, 0.0),
        n_points=10,
        source_radius=0.075,
        max_time=10.0,
    )

    # testing the StreamlinesSource
    # ------------------------------------
    src_as_data_set = src_obj._as_pyvista_data_set()
    src_as_field = src_obj.as_field(server=server_type)
    tmp = core.helpers.streamlines.StreamlinesSource(src_as_field)
    src_as_data_set_check = tmp._as_pyvista_data_set()
    src_obj = core.helpers.streamlines.StreamlinesSource(src_as_data_set_check)

    # check for pyvista objects
    assert src_as_data_set.n_points == src_as_data_set_check.n_points
    assert src_as_data_set.n_cells == src_as_data_set_check.n_cells
    array_names_check = src_as_data_set_check.array_names
    assert len(array_names_check) == 0
    for c_ind in range(0, src_as_data_set.n_cells):
        assert src_as_data_set.GetCellType(c_ind) == src_as_data_set_check.GetCellType(c_ind)

    # checks for field
    field = src_as_field
    mesh = field.meshed_region
    assert len(mesh.nodes.coordinates_field.scoping.ids) == src_as_data_set.n_points
    assert len(mesh.elements.element_types_field) == src_as_data_set.n_cells
    assert len(mesh.elements.connectivities_field.scoping.ids) == src_as_data_set.n_cells
    assert len(mesh.elements.connectivities_field.get_entity_data(0)) == 10
    assert len(array_names_check) == 0
    assert field.field_definition.name == ""

    # testing the Streamlines
    # ------------------------------------
    # get the pv_data_set and the fc for initial streamline
    # re-create a streamline from fc
    # get the pv_data_set for the new streamline and ensure
    # it's the same than the original one
    str_as_data_set = streamline_obj._as_pyvista_data_set()
    str_as_field = streamline_obj.as_field(server=server_type)
    tmp = core.helpers.streamlines.Streamlines(str_as_field)
    str_as_data_set_check = tmp._as_pyvista_data_set()
    streamline_obj = core.helpers.streamlines.Streamlines(str_as_data_set_check)

    # check for pyvista objects
    assert str_as_data_set.n_points == str_as_data_set_check.n_points
    assert str_as_data_set.n_cells == str_as_data_set_check.n_cells
    array_names = str_as_data_set.array_names
    array_names_check = str_as_data_set_check.array_names
    an = array_names_check[0]
    assert len(array_names_check) == 1
    assert len(str_as_data_set[an]) == len(str_as_data_set_check[an])
    for c_ind in range(0, str_as_data_set.n_cells):
        assert str_as_data_set.GetCellType(c_ind) == str_as_data_set_check.GetCellType(c_ind)

    # checks for field
    field = str_as_field
    mesh = field.meshed_region
    assert len(field.scoping.ids) == len(str_as_data_set[an])
    assert len(field.scoping.ids) == str_as_data_set.n_points
    assert len(mesh.nodes.coordinates_field.scoping.ids) == str_as_data_set.n_points
    assert len(mesh.elements.element_types_field) == str_as_data_set.n_cells
    assert len(mesh.elements.connectivities_field.scoping.ids) == str_as_data_set.n_cells
    for i in range(0, len(array_names)):
        array_n = array_names[i]
        if "streamlines" in array_n:
            array_check = array_n
    assert field.field_definition.name == array_check

    # plot
    # -----------------------
    pl = DpfPlotter()
    pl.add_field(field, meshed_region, opacity=0.2)
    pl.add_streamlines(
        streamlines=streamline_obj,
        source=src_obj,
        radius=0.001,
    )
