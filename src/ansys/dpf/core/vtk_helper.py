import numpy as np
import pyvista as pv
from typing import Union
from vtk import (
    VTK_HEXAHEDRON,
    VTK_LINE,
    VTK_POLYGON,
    VTK_POLYHEDRON,
    VTK_PYRAMID,
    VTK_QUAD,
    VTK_QUADRATIC_EDGE,
    VTK_QUADRATIC_HEXAHEDRON,
    VTK_QUADRATIC_POLYGON,
    VTK_QUADRATIC_PYRAMID,
    VTK_QUADRATIC_QUAD,
    VTK_QUADRATIC_TETRA,
    VTK_QUADRATIC_TRIANGLE,
    VTK_TETRA,
    VTK_TRIANGLE,
    VTK_VERTEX,
    VTK_WEDGE,
    vtkVersion,
)

import ansys.dpf.core as dpf
from ansys.dpf.core import errors
from ansys.dpf.core.check_version import server_meet_version_and_raise
from ansys.dpf.core.elements import element_types

VTK9 = vtkVersion().GetVTKMajorVersion() >= 9


# DPF --> VTK mapping
# any cells not mapped will be empty cells
VTK_MAPPING = np.array(
    [
        VTK_QUADRATIC_TETRA,  # kAnsTet10 = 0,
        VTK_QUADRATIC_HEXAHEDRON,  # kAnsHex20 = 1,
        # VTK_QUADRATIC_WEDGE,  # kAnsWedge15 = 2,
        VTK_WEDGE,  # kAnsWedge15 = 2,
        VTK_QUADRATIC_PYRAMID,  # kAnsPyramid13 = 3,
        VTK_QUADRATIC_TRIANGLE,  # kAnsTri6 = 4,
        VTK_QUADRATIC_TRIANGLE,  # kAnsTriShell6 = 5,
        VTK_QUADRATIC_QUAD,  # kAnsQuad8 = 6,
        VTK_QUADRATIC_QUAD,  # kAnsQuadShell8 = 7,
        VTK_QUADRATIC_EDGE,  # kAnsLine3 = 8,
        VTK_VERTEX,  # kAnsPoint1 = 9,
        VTK_TETRA,  # kAnsTet4 = 10,
        VTK_HEXAHEDRON,  # kAnsHex8 = 11,
        VTK_WEDGE,  # kAnsWedge6 = 12,
        VTK_PYRAMID,  # kAnsPyramid5 = 13,
        VTK_TRIANGLE,  # kAnsTri3 = 14,
        VTK_TRIANGLE,  # kAnsTriShell3 = 15,
        VTK_QUAD,  # kAnsQuad4 = 16,
        VTK_QUAD,  # kAnsQuadShell4 = 17,
        VTK_LINE,  # kAnsLine2 = 18,
        0,  # kAnsNumElementTypes = 19,
        0,  # kAnsUnknown = 20,
        0,  # kAnsEMagLine = 21,
        0,  # kAnsEMagArc = 22,
        0,  # kAnsEMagCircle = 23,
        VTK_TRIANGLE,  # kAnsSurface3 = 24,
        VTK_QUAD,  # kAnsSurface4 = 25,
        VTK_QUADRATIC_TRIANGLE,  # kAnsSurface6 = 26,
        VTK_QUADRATIC_QUAD,  # kAnsSurface8 = 27,
        0,  # kAnsEdge2 = 28,
        0,  # kAnsEdge3 = 29,
        0,  # kAnsBeam3 = 30,
        0,  # kAnsBeam4 = 31,
        0,  # kAnsGeneralPlaceholder = 32,
        VTK_QUADRATIC_POLYGON,  # kAnsPolygon = 33,
        VTK_POLYHEDRON,  # kAnsPolyhedron = 34,
    ]
)


# map all cells to linear
VTK_LINEAR_MAPPING = np.array(
    [
        VTK_TETRA,  # kAnsTet10 = 0,
        VTK_HEXAHEDRON,  # kAnsHex20 = 1,
        VTK_WEDGE,  # kAnsWedge15 = 2,
        VTK_PYRAMID,  # kAnsPyramid13 = 3,
        VTK_TRIANGLE,  # kAnsTri6 = 4,
        VTK_TRIANGLE,  # kAnsTriShell6 = 5,
        VTK_QUAD,  # kAnsQuad8 = 6,
        VTK_QUAD,  # kAnsQuadShell8 = 7,
        VTK_LINE,  # kAnsLine3 = 8,
        VTK_VERTEX,  # kAnsPoint1 = 9,
        VTK_TETRA,  # kAnsTet4 = 10,
        VTK_HEXAHEDRON,  # kAnsHex8 = 11,
        VTK_WEDGE,  # kAnsWedge6 = 12,
        VTK_PYRAMID,  # kAnsPyramid5 = 13,
        VTK_TRIANGLE,  # kAnsTri3 = 14,
        VTK_TRIANGLE,  # kAnsTriShell3 = 15,
        VTK_QUAD,  # kAnsQuad4 = 16,
        VTK_QUAD,  # kAnsQuadShell4 = 17,
        VTK_LINE,  # kAnsLine2 = 18,
        0,  # kAnsNumElementTypes = 19,
        0,  # kAnsUnknown = 20,
        0,  # kAnsEMagLine = 21,
        0,  # kAnsEMagArc = 22,
        0,  # kAnsEMagCircle = 23,
        VTK_TRIANGLE,  # kAnsSurface3 = 24,
        VTK_QUAD,  # kAnsSurface4 = 25,
        VTK_QUADRATIC_TRIANGLE,  # kAnsSurface6 = 26,
        VTK_QUADRATIC_QUAD,  # kAnsSurface8 = 27,
        0,  # kAnsEdge2 = 28,
        0,  # kAnsEdge3 = 29,
        0,  # kAnsBeam3 = 30,
        0,  # kAnsBeam4 = 31,
        0,  # kAnsGeneralPlaceholder = 32,
        VTK_POLYGON,  # kAnsPolygon = 33,
        VTK_POLYHEDRON,  # kAnsPolyhedron = 34,
    ]
)


class PyVistaImportError(ModuleNotFoundError):
    """Error raised when PyVista could not be imported during plotting."""

    def __init__(
        self,
        msg="To use plotting capabilities, please install pyvista "
        "with :\n pip install pyvista>=0.32.0",
    ):
        ModuleNotFoundError.__init__(self, msg)


def dpf_mesh_to_vtk_op(mesh, nodes=None, as_linear=True):
    """Return a pyvista unstructured grid given DPF node and element
    definitions from operators (server > 6.2)

    Parameters
    ----------
    mesh : dpf.MeshedRegion
        Meshed Region to export to pyVista format

    nodes : dpf.Field
        Field containing the node coordinates of the mesh.

    as_linear : bool
        Export quadratic surface elements as linear.

    Returns
    -------
    grid : pyvista.UnstructuredGrid
        Unstructured grid of the DPF mesh.
    """
    mesh_to_pyvista = dpf.operators.mesh.mesh_to_pyvista(server=mesh._server)
    mesh_to_pyvista.inputs.mesh.connect(mesh)
    mesh_to_pyvista.inputs.as_linear.connect(as_linear)
    mesh_to_pyvista.inputs.vtk_updated.connect(VTK9)
    if nodes is not None:
        mesh_to_pyvista.inputs.coordinates.connect(nodes)

    nodes_pv = mesh_to_pyvista.outputs.nodes().data
    cells_pv = mesh_to_pyvista.outputs.cells()
    celltypes_pv = mesh_to_pyvista.outputs.cell_types()
    if VTK9:
        grid = pv.UnstructuredGrid(cells_pv, celltypes_pv, nodes_pv)
        setattr(grid, "_dpf_cache_op", [cells_pv, celltypes_pv, nodes_pv])
        return grid
    else:
        offsets_pv = mesh_to_pyvista.outputs.offsets()
        grid = pv.UnstructuredGrid(offsets_pv, cells_pv, celltypes_pv, nodes_pv)
        setattr(grid, "_dpf_cache_op", [cells_pv, celltypes_pv, nodes_pv, offsets_pv])
        return grid


def dpf_mesh_to_vtk_py(mesh, nodes, as_linear):
    """Return a pyvista unstructured grid given DPF node and element
    definitions in pure Python (server <= 6.2)

    Parameters
    ----------
    mesh : dpf.MeshedRegion
        Meshed Region to export to pyVista format

    nodes : dpf.Field
        Field containing the node coordinates of the mesh.

    as_linear : bool
        Export quadratic surface elements as linear.

    Returns
    -------
    grid : pyvista.UnstructuredGrid
        Unstructured grid of the DPF mesh.
    """
    etypes = mesh.elements.element_types_field.data
    connectivity = mesh.elements.connectivities_field
    if nodes is None:
        coordinates_field = mesh.nodes.coordinates_field
        node_coordinates = coordinates_field.data
    else:
        coordinates_field = nodes
        node_coordinates = nodes.data

    elem_size = np.ediff1d(np.append(connectivity._data_pointer, connectivity.shape))

    faces_nodes_connectivity = mesh.property_field("faces_nodes_connectivity")
    faces_nodes_connectivity_dp = np.append(
        faces_nodes_connectivity._data_pointer, len(faces_nodes_connectivity)
    )
    elements_faces_connectivity = mesh.property_field("elements_faces_connectivity")
    elements_faces_connectivity_dp = np.append(
        elements_faces_connectivity._data_pointer, len(elements_faces_connectivity)
    )

    insert_ind = np.cumsum(elem_size)
    insert_ind = np.hstack(([0], insert_ind))[:-1]

    # partition cells in vtk format
    cells = np.insert(connectivity.data, insert_ind, elem_size)

    # Check if polyhedrons are present
    if element_types.Polyhedron.value in etypes:
        cells = np.array(cells)
        nodes = np.array(node_coordinates)
        insert_ind = insert_ind + np.asarray(list(range(len(insert_ind))))
        # Replace in cells values for polyhedron format
        # [NValuesToFollow,
        # NFaces, Face1NPoints, Face1Point1, Face1Point2..., Face1PointN, FaceNNPoints,...]]
        for i, ind in reversed(list(enumerate(insert_ind))):
            # Check if this is a polyhedron
            if etypes[i] == element_types.Polyhedron.value:
                # Construct the connectivity for the poly element
                poly_connectivity = []
                faces = elements_faces_connectivity.data[
                    elements_faces_connectivity_dp[i] : elements_faces_connectivity_dp[i + 1]
                ]
                for face in faces:
                    face_connectivity = faces_nodes_connectivity.data[
                        faces_nodes_connectivity_dp[face] : faces_nodes_connectivity_dp[face + 1]
                    ]
                    face_fmt = [len(face_connectivity)] + list(face_connectivity)
                    poly_connectivity += face_fmt
                polyhedron = [len(faces)] + poly_connectivity
                polyhedron = [len(polyhedron)] + polyhedron
                # Replace the whole sequence between this index and the next
                r = list(range(ind, ind + elem_size[i] + 1))
                cells = np.delete(cells, r)
                cells = np.insert(cells, ind, polyhedron)

    def compute_offset():
        """Return the starting point of a cell in the cells array"""
        return insert_ind + np.arange(insert_ind.size)

    cells_insert_ind = compute_offset()
    # convert kAns to VTK cell type
    offset = None
    if as_linear:
        # Map the vtk_cell_type to linear versions of the initial elements types
        vtk_cell_type = VTK_LINEAR_MAPPING[etypes]

        # Create a global mask of connectivity values to take
        mask = np.full(cells.shape, True)

        # Get a mask of quad8 elements in etypes
        quad8_mask = etypes == 6
        # If any quad8
        if np.any(quad8_mask):  # kAnsQuad8
            # Get the starting indices of quad8 elements in cells
            insert_ind_quad8 = cells_insert_ind[quad8_mask]
            # insert_ind_quad8 += np.arange(insert_ind_quad8.size)
            mask[insert_ind_quad8 + 5] = False
            mask[insert_ind_quad8 + 6] = False
            mask[insert_ind_quad8 + 7] = False
            mask[insert_ind_quad8 + 8] = False
            cells[insert_ind_quad8] //= 2

        tri6_mask = etypes == 4  # kAnsTri6 = 4
        if np.any(tri6_mask):
            insert_ind_tri6 = cells_insert_ind[tri6_mask]
            # insert_ind_tri6 += np.arange(insert_ind_tri6.size)
            mask[insert_ind_tri6 + 4] = False
            mask[insert_ind_tri6 + 5] = False
            mask[insert_ind_tri6 + 6] = False
            cells[insert_ind_tri6] //= 2
        cells = cells[mask]

    else:
        vtk_cell_type = VTK_MAPPING[etypes]

        # Handle semi-parabolic elements
        semi_mask = cells == -1
        if semi_mask.any():
            cells_insert_ind = compute_offset()
            # Create a global mask of connectivity values to take
            mask = np.full(cells.shape, True)
            # Build a map of size cells with repeated element beginning index
            repeated_insert_ind = cells_insert_ind.repeat(repeats=elem_size + 1)
            # Apply the semi-mask to get a unique set of indices of semi-parabolic elements in cells
            semi_indices_in_cells = np.array(list(set(repeated_insert_ind[semi_mask])))
            semi_sizes = cells[semi_indices_in_cells]
            semi_quad8 = semi_sizes == 8
            if semi_quad8.any():
                mask[semi_indices_in_cells[semi_quad8] + 5] = False
                mask[semi_indices_in_cells[semi_quad8] + 6] = False
                mask[semi_indices_in_cells[semi_quad8] + 7] = False
                mask[semi_indices_in_cells[semi_quad8] + 8] = False
                cells[semi_indices_in_cells[semi_quad8]] //= 2

                quad8_mask = etypes == 6
                semi_quad8_mask = (cells[cells_insert_ind] == 4) & quad8_mask
                vtk_cell_type[semi_quad8_mask] = VTK_LINEAR_MAPPING[6]
            semi_tri6 = semi_sizes == 6
            if semi_tri6.any():
                mask[semi_indices_in_cells[semi_tri6] + 4] = False
                mask[semi_indices_in_cells[semi_tri6] + 5] = False
                mask[semi_indices_in_cells[semi_tri6] + 6] = False
                cells[semi_indices_in_cells[semi_tri6]] //= 2

                tri6_mask = etypes == 4
                semi_tri6_mask = (cells[cells_insert_ind] == 3) & tri6_mask
                vtk_cell_type[semi_tri6_mask] = VTK_LINEAR_MAPPING[4]
            # Update cells with the mask
            cells = cells[mask]

    # different treatment depending on the version of vtk
    if VTK9:
        # compute offset array when < VTK v9
        grid = pv.UnstructuredGrid(cells, vtk_cell_type, node_coordinates)

        # Quick fix required to hold onto the data as PyVista does not make a copy.
        # All of those now return DPFArrays
        setattr(grid, "_dpf_cache", [node_coordinates, coordinates_field])

        return grid

    # might be computed when checking for VTK quadratic bug
    if offset is None:
        offset = compute_offset()

    return pv.UnstructuredGrid(offset, cells, vtk_cell_type, node_coordinates)


def dpf_mesh_to_vtk(
        mesh: dpf.MeshedRegion,
        nodes: Union[dpf.Field, None] = None,
        as_linear: bool = True
) -> pv.UnstructuredGrid:
    """Return a pyvista UnstructuredGrid given a pydpf MeshedRegion.

    Parameters
    ----------
    mesh : dpf.MeshedRegion
        Meshed Region to export to pyVista format.

    nodes : dpf.Field, optional
        Field containing the node coordinates of the mesh (useful to get a deformed geometry).

    as_linear : bool, optional
        Export quadratic surface elements as linear.

    Returns
    -------
    grid:
        UnstructuredGrid corresponding to the DPF mesh.
    """
    try:
        return dpf_mesh_to_vtk_op(mesh, nodes, as_linear)
    except (AttributeError, KeyError, errors.DPFServerException):
        return dpf_mesh_to_vtk_py(mesh, nodes, as_linear)


def vtk_update_coordinates(vtk_grid, coordinates_array):
    from copy import copy

    vtk_grid.points = copy(coordinates_array)


def dpf_meshes_to_vtk(
        meshes_container: dpf.MeshesContainer,
        nodes: Union[dpf.FieldsContainer, None] = None,
        as_linear: bool = True
) -> pv.UnstructuredGrid:
    """Return a pyvista UnstructuredGrid given a pydpf MeshedRegion.

    Parameters
    ----------
    meshes_container:
        MeshesContainer to export to pyVista format.

    nodes:
        FieldsContainer containing the node coordinates for each mesh
        (useful to get a deformed geometry). The labels must match a field to a mesh.

    as_linear : bool, optional
        Export quadratic surface elements as linear.

    Returns
    -------
    grid:
        UnstructuredGrid corresponding to the DPF meshes.
    """
    grids = []
    for i, mesh in enumerate(meshes_container):
        nodes_i = None
        if nodes:
            nodes_i = nodes[i]
        grids.append(dpf_mesh_to_vtk(mesh, nodes_i, as_linear))
    return pv.MultiBlock(grids).combine()


def dpf_field_to_vtk(
        field: dpf.Field,
        meshed_region: Union[dpf.MeshedRegion, None] = None,
        nodes: Union[dpf.Field, None] = None,
        as_linear: bool = True
) -> pv.UnstructuredGrid:
    """Return a pyvista UnstructuredGrid given a DPF Field.

    Parameters
    ----------
    field:
        Field to export to pyVista format.

    meshed_region:
        Mesh to associate to the field.
        Useful for fluid results where the field is not automatically associated to its mesh.

    nodes:
        Field containing the node coordinates of the mesh (useful to get a deformed geometry).

    as_linear:
        Export quadratic surface elements as linear.

    Returns
    -------
    grid:
        UnstructuredGrid corresponding to the DPF Field.
    """
    # Check Field location
    supported_locations = [
        dpf.locations.nodal, dpf.locations.elemental, dpf.locations.faces, dpf.locations.overall
    ]
    if field.location not in supported_locations:
        raise ValueError(
            f"Supported field locations for translation to VTK are: {supported_locations}."
        )

    # Associate the provided mesh with the field
    if meshed_region:
        field.meshed_region = meshed_region
    else:
        try:
            meshed_region = field.meshed_region
        except errors.DPFServerException as e:
            if "the field doesn't have this support type" in str(e):
                raise ValueError("The field does not have a meshed_region.")
            else:
                raise e
        except RuntimeError as e:
            if "The field's support is not a mesh" in str(e):
                raise ValueError("The field does not have a meshed_region.")
            else:
                raise e

    # Initialize the bare UnstructuredGrid
    if meshed_region.nodes.n_nodes == 0:
        raise ValueError("The field does not have a meshed_region.")
    grid = dpf_mesh_to_vtk(mesh=meshed_region, nodes=nodes, as_linear=as_linear)

    # Map Field.data to the VTK mesh
    overall_data = _map_field_to_mesh(field=field, meshed_region=meshed_region)

    # Update the UnstructuredGrid
    if field.location == dpf.locations.nodal:
        grid.point_data[field.name] = overall_data
    else:
        grid.cell_data[field.name] = overall_data
    return grid


def dpf_fieldscontainer_to_vtk(
        fields_container: dpf.FieldsContainer,
        meshes_container: Union[dpf.MeshesContainer, None] = None,
        nodes: Union[dpf.Field, None] = None,
        as_linear: bool = True
) -> pv.UnstructuredGrid:
    """Return a pyvista UnstructuredGrid given a DPF FieldsContainer.

    If the fields have different mesh supports, a global merged mesh support is created.

    Parameters
    ----------
    fields_container:
        FieldsContainer to export to pyVista format.

    meshes_container:
        MeshesContainer with meshes to associate to the fields in the FieldsContainer.
        Useful for fluid results where the fields are not automatically associated to their mesh.

    nodes:
        Field containing the node coordinates of the mesh (useful to get a deformed geometry).

    as_linear:
        Export quadratic surface elements as linear.

    Returns
    -------
    grid:
        UnstructuredGrid corresponding to the DPF Field.
    """
    # Check Field location
    supported_locations = [
        dpf.locations.nodal, dpf.locations.elemental, dpf.locations.faces, dpf.locations.overall
    ]
    if fields_container[0].location not in supported_locations:
        raise ValueError(
            f"Supported field locations for translation to VTK are: {supported_locations}."
        )

    # Associate the meshes in meshes_container to the corresponding fields if provided
    if meshes_container:
        for i, mesh in enumerate(meshes_container):
            label_space = meshes_container.get_label_space(i)
            fields_container.get_field(
                label_space_or_index=label_space
            ).meshed_region = meshes_container.get_mesh(label_space_or_index=label_space)

    # Initialize the bare UnstructuredGrid
    # Loop on the fields to check if merging supports is necessary
    meshes = []
    for field in fields_container:
        if field.meshed_region not in meshes:
            meshes.append(field.meshed_region)
    if len(meshes)>1:
        # Merge the meshed_regions
        merge_op = dpf.operators.utility.merge_meshes(server=fields_container._server)
        for i, mesh in enumerate(meshes):
            merge_op.connect(i, mesh)
        meshed_region = merge_op.eval()
    else:
        meshed_region = meshes[0]
    if meshed_region.nodes.n_nodes == 0:
        raise ValueError("The meshed_region of the fields contains no nodes.")
    grid = dpf_mesh_to_vtk(mesh=meshed_region, nodes=nodes, as_linear=as_linear)

    for i, field in enumerate(fields_container):
        # Map Field.data to the VTK mesh
        overall_data = _map_field_to_mesh(field=field, meshed_region=meshed_region)
        label_space = fields_container.get_label_space(i)
        label_space = dict([(k, label_space[k]) for k in sorted(label_space.keys())])
        field.name = field.name+f" {label_space}"
        # Update the UnstructuredGrid
        if field.location == dpf.locations.nodal:
            grid.point_data[field.name] = overall_data
        else:
            grid.cell_data[field.name] = overall_data

    return grid


def _map_field_to_mesh(
        field: Union[dpf.Field, dpf.PropertyField],
        meshed_region: dpf.MeshedRegion
) -> np.ndarray:
    """Return an NumPy array of 'Field.data' mapped to the mesh on the field's location."""
    location = field.location
    if location == dpf.locations.nodal:
        mesh_location = meshed_region.nodes
    elif location == dpf.locations.elemental:
        mesh_location = meshed_region.elements
    elif location == dpf.locations.faces:
        mesh_location = meshed_region.faces
        if len(mesh_location) == 0:
            raise ValueError("No faces found to plot on")
    elif location == dpf.locations.overall:
        mesh_location = meshed_region.elements
    else:
        raise ValueError("Only elemental, nodal or faces location are supported for plotting.")
    component_count = field.component_count
    if component_count > 1:
        overall_data = np.full((len(mesh_location), component_count), np.nan)
    else:
        overall_data = np.full(len(mesh_location), np.nan)
    if location != dpf.locations.overall:
        ind, mask = mesh_location.map_scoping(field.scoping)
        overall_data[ind] = field.data[mask]
    else:
        overall_data[:] = field.data[0]
    return overall_data


def dpf_property_field_to_vtk(
        property_field: dpf.PropertyField,
        meshed_region: dpf.MeshedRegion,
        nodes: Union[dpf.Field, None] = None,
        as_linear: bool = True
) -> pv.UnstructuredGrid:
    """Return a pyvista UnstructuredGrid given a DPF PropertyField.

    ..note:
        Available starting with DPF 2024.2.pre1.

    Parameters
    ----------
    property_field:
        PropertyField to export to pyVista format.

    meshed_region:
        Mesh to associate to the property field.

    nodes:
        Field containing the node coordinates of the mesh (useful to get a deformed geometry).

    as_linear:
        Export quadratic surface elements as linear.

    Returns
    -------
    grid:
        UnstructuredGrid corresponding to the DPF PropertyField.
    """
    server_meet_version_and_raise(
        required_version="8.1",
        server=meshed_region._server,
        msg="Use of dpf_property_field_to_vtk requires DPF 2024.2.pre1 or above."
    )
    # Check Field location
    supported_locations = [
        dpf.locations.nodal, dpf.locations.elemental, dpf.locations.faces, dpf.locations.overall
    ]
    if property_field.location not in supported_locations:
        raise ValueError(
            f"Supported field locations for translation to VTK are: {supported_locations}."
        )

    # Initialize the bare UnstructuredGrid
    if meshed_region.nodes.n_nodes == 0:
        raise ValueError("The property field does not have a meshed_region.")
    grid = dpf_mesh_to_vtk(mesh=meshed_region, nodes=nodes, as_linear=as_linear)

    # Map Field.data to the VTK mesh
    overall_data = _map_field_to_mesh(field=property_field, meshed_region=meshed_region)

    # Update the UnstructuredGrid
    if property_field.location == dpf.locations.nodal:
        grid.point_data[property_field.name] = overall_data
    else:
        grid.cell_data[property_field.name] = overall_data
    return grid
