import pytest
import conftest
import ansys.dpf.core as dpf
from ansys.dpf.core import errors, misc
from ansys.dpf.core.vtk_helper import \
    dpf_mesh_to_vtk, dpf_field_to_vtk, dpf_meshes_to_vtk, \
    dpf_fieldscontainer_to_vtk, dpf_property_field_to_vtk, \
    append_field_to_grid, append_fieldscontainer_to_grid

if misc.module_exists("pyvista"):
    HAS_PYVISTA = True
    import pyvista as pv
else:
    HAS_PYVISTA = False


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_dpf_mesh_to_vtk(simple_rst, server_type):
    model = dpf.Model(simple_rst, server=server_type)
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


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_dpf_field_to_vtk(simple_rst, fluent_mixing_elbow_steady_state, server_type):
    model = dpf.Model(simple_rst, server=server_type)
    mesh = model.metadata.meshed_region
    field = model.results.displacement.on_last_time_freq().eval()[0]
    # Nodal Field to VTK
    ug = dpf_field_to_vtk(field=field, field_name="disp")
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
    model = dpf.Model(fluent_mixing_elbow_steady_state(server=server_type), server=server_type)
    field = model.results.dynamic_viscosity.on_last_time_freq().eval()[0]
    ug = dpf_field_to_vtk(
        field=field, meshed_region=model.metadata.meshed_region, field_name="DV"
    )
    assert isinstance(ug, pv.UnstructuredGrid)
    assert "DV" in ug.cell_data.keys()
    pv.plot(ug)


@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_dpf_field_to_vtk_errors(simple_rst, server_type):
    model = dpf.Model(simple_rst, server=server_type)
    # Elemental Field to VTK
    field = model.results.elemental_volume.on_last_time_freq().eval()[0]
    with pytest.raises(ValueError, match="The field does not have a meshed_region."):
        _ = dpf_field_to_vtk(field=field)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_dpf_meshes_to_vtk(fluent_axial_comp, server_type):
    model = dpf.Model(fluent_axial_comp(server=server_type), server=server_type)
    meshes_container = dpf.operators.mesh.meshes_provider(
        data_sources=model,
        server=server_type,
        region_scoping=dpf.Scoping(ids=[13, 28], location=dpf.locations.zone, server=server_type)
    ).eval()
    assert len(meshes_container) == 2
    ug = dpf_meshes_to_vtk(meshes_container=meshes_container)
    assert ug.GetNumberOfCells() == 13856
    pv.plot(ug)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_dpf_fieldscontainer_to_vtk(fluent_axial_comp, server_type):
    model = dpf.Model(fluent_axial_comp(server=server_type), server=server_type)
    zone_scoping = dpf.Scoping(ids=[13, 28], location=dpf.locations.zone, server=server_type)
    # Elemental
    fields_container = dpf.operators.result.enthalpy(
        data_sources=model,
        server=server_type,
        region_scoping=zone_scoping,
    ).eval()
    assert len(fields_container) == 2
    meshes_container = dpf.operators.mesh.meshes_provider(
        data_sources=model,
        server=server_type,
        region_scoping=zone_scoping,
    ).eval()
    ug = dpf_fieldscontainer_to_vtk(
        fields_container=fields_container, meshes_container=meshes_container
    )
    assert ug.GetNumberOfCells() == 13856
    assert sorted(list(ug.cell_data.keys())) == ["h {'time': 1, 'zone': 13}",
                                                 "h {'time': 1, 'zone': 28}"]
    pv.plot(ug)
    zone_scoping = dpf.Scoping(ids=[3, 4, 7], location=dpf.locations.zone, server=server_type)
    # Faces
    fields_container = dpf.operators.result.wall_shear_stress(
        data_sources=model,
        server=server_type,
        region_scoping=zone_scoping,
    ).eval()
    assert len(fields_container) == 3
    meshes_container = dpf.operators.mesh.meshes_provider(
        data_sources=model,
        server=server_type,
        region_scoping=zone_scoping
    ).eval()
    ug = dpf_fieldscontainer_to_vtk(
        fields_container=fields_container, meshes_container=meshes_container
    )
    assert ug.GetNumberOfCells() == 1144
    assert sorted(list(ug.cell_data.keys())) == [
        "tau_w {'time': 1, 'zone': 3}",
        "tau_w {'time': 1, 'zone': 4}",
        "tau_w {'time': 1, 'zone': 7}"]
    pv.plot(ug)


@pytest.mark.xfail(raises=errors.DpfVersionNotSupported)
@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_dpf_property_field_to_vtk(simple_rst, server_type):
    model = dpf.Model(simple_rst, server=server_type)
    mesh = model.metadata.meshed_region
    property_field = mesh.property_field(property_name="mat")
    print(property_field)
    # PropertyField to VTK
    ug = dpf_property_field_to_vtk(
        property_field=property_field, meshed_region=mesh, field_name="mat_id"
    )
    assert isinstance(ug, pv.UnstructuredGrid)
    assert "mat_id" in ug.cell_data.keys()
    pv.plot(ug)


@pytest.mark.xfail(raises=errors.DpfVersionNotSupported)
@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_append_field_to_grid(simple_rst, server_type):
    model = dpf.Model(simple_rst, server=server_type)
    mesh = model.metadata.meshed_region
    field = model.results.displacement.on_last_time_freq().eval()[0]
    # Nodal Field to VTK
    ug = dpf_field_to_vtk(field=field, field_name="disp")
    assert isinstance(ug, pv.UnstructuredGrid)
    assert "disp" in ug.point_data.keys()
    # Append Elemental Field
    field = model.results.elemental_volume.on_last_time_freq().eval()[0]
    ug = append_field_to_grid(field=field, meshed_region=mesh, grid=ug, field_name="volume")
    assert isinstance(ug, pv.UnstructuredGrid)
    assert "disp" in ug.point_data.keys()
    assert "volume" in ug.cell_data.keys()


@pytest.mark.xfail(raises=errors.DpfVersionNotSupported)
@pytest.mark.skipif(not HAS_PYVISTA, reason="Please install pyvista")
def test_append_fields_container_to_grid(simple_rst, server_type):
    model = dpf.Model(simple_rst, server=server_type)
    mesh = model.metadata.meshed_region
    fc = model.results.displacement.eval()
    # Nodal Field to VTK
    ug = dpf_fieldscontainer_to_vtk(fields_container=fc, field_name="disp")
    assert isinstance(ug, pv.UnstructuredGrid)
    assert "disp {'time': 1}" in ug.point_data.keys()
    # Append Elemental Field
    fc = model.results.elemental_volume.eval()
    ug = append_fieldscontainer_to_grid(
        fields_container=fc, meshed_region=mesh, grid=ug, field_name="volume"
    )
    assert isinstance(ug, pv.UnstructuredGrid)
    assert "disp {'time': 1}" in ug.point_data.keys()
    assert "volume {'time': 1}" in ug.cell_data.keys()
