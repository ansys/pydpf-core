import pytest
import ansys.dpf.core as dpf
from ansys.dpf.core import misc
from ansys.dpf.core.vtk_helper import \
    dpf_mesh_to_vtk, dpf_field_to_vtk, dpf_meshes_to_vtk, dpf_fieldscontainer_to_vtk

if misc.module_exists("pyvista"):
    HAS_PYVISTA = True
    import pyvista as pv
else:
    HAS_PYVISTA = False


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_dpf_mesh_to_vtk(simple_rst):
    model = dpf.Model(simple_rst)
    mesh = model.metadata.meshed_region
    # Mesh to VTK
    ug = dpf_mesh_to_vtk(mesh=mesh)
    assert isinstance(ug, pv.UnstructuredGrid)
    pv.plot(ug)
    # With deformation
    field = model.results.displacement.on_last_time_freq().eval()[0]
    initial_coord = mesh.nodes.coordinates_field
    updated_coord = (initial_coord + field).eval()
    ug = dpf_mesh_to_vtk(mesh=mesh, nodes=updated_coord)
    assert isinstance(ug, pv.UnstructuredGrid)
    pv.plot(ug)
    # As linear
    ug = dpf_mesh_to_vtk(mesh=mesh, as_linear=True)
    assert isinstance(ug, pv.UnstructuredGrid)
    pv.plot(ug)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_dpf_field_to_vtk(simple_rst, fluent_mixing_elbow_steady_state):
    model = dpf.Model(simple_rst)
    mesh = model.metadata.meshed_region
    field = model.results.displacement.on_last_time_freq().eval()[0]
    field.name = "disp"
    # Nodal Field to VTK
    ug = dpf_field_to_vtk(field=field)
    assert isinstance(ug, pv.UnstructuredGrid)
    assert "disp" in ug.point_data.keys()
    pv.plot(ug)
    # With deformation
    initial_coord = mesh.nodes.coordinates_field
    updated_coord = (initial_coord + field).eval()
    ug = dpf_field_to_vtk(field=field, nodes=updated_coord)
    assert isinstance(ug, pv.UnstructuredGrid)
    pv.plot(ug)
    # As linear
    ug = dpf_field_to_vtk(field=field, as_linear=True)
    assert isinstance(ug, pv.UnstructuredGrid)
    pv.plot(ug)
    # Elemental Field to VTK
    model = dpf.Model(fluent_mixing_elbow_steady_state())
    field = model.results.dynamic_viscosity.on_last_time_freq().eval()[0]
    field.name = "DV"
    ug = dpf_field_to_vtk(field=field)
    assert isinstance(ug, pv.UnstructuredGrid)
    assert "DV" in ug.cell_data.keys()
    pv.plot(ug)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_dpf_field_to_vtk_errors(simple_rst):
    model = dpf.Model(simple_rst)
    # Elemental Field to VTK
    field = model.results.elemental_volume.on_last_time_freq().eval()[0]
    with pytest.raises(ValueError, match="The field.meshed_region contains no nodes."):
        _ = dpf_field_to_vtk(field=field)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_dpf_meshes_to_vtk(fluent_axial_comp):
    model = dpf.Model(fluent_axial_comp())
    meshes_container = dpf.operators.mesh.meshes_provider(
        data_sources=model,
        region_scoping=dpf.Scoping(ids=[13, 28], location=dpf.locations.zone)
    ).eval()
    assert len(meshes_container) == 2
    ug = dpf_meshes_to_vtk(meshes_container=meshes_container)
    assert ug.GetNumberOfCells() == 13856
    pv.plot(ug)
