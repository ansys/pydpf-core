import numpy as np
import vtkmodules.vtkCommonDataModel
from vtk import (
    VTK_VERTEX,
    VTK_LINE,
    VTK_TRIANGLE,
    VTK_QUAD,
    VTK_TETRA,
    VTK_HEXAHEDRON,
    VTK_WEDGE,
    VTK_PYRAMID,
    VTK_QUADRATIC_EDGE,
    VTK_QUADRATIC_TRIANGLE,
    VTK_QUADRATIC_QUAD,
    VTK_QUADRATIC_TETRA,
    VTK_QUADRATIC_HEXAHEDRON,
    VTK_QUADRATIC_PYRAMID,
    VTK_POLYGON,
    VTK_QUADRATIC_POLYGON,
    VTK_POLYHEDRON,
    vtkVersion,
)
from vtkmodules.vtkCommonCore import (
    vtkIdList, vtkIdTypeArray,
)
from vtkmodules.util.numpy_support import (
    numpy_to_vtk,
    numpy_to_vtkIdTypeArray,
)
import pyvista as pv

VTK9 = vtkVersion().GetVTKMajorVersion() >= 9

# Maps dpf cell sizes (based on array order) to the number of nodes per cell
SIZE_MAPPING = np.array(
    [
        10,  # kAnsTet10
        20,  # kAnsHex20
        15,  # kAnsWedge15
        13,  # kAnsPyramid13
        6,  # kAnsTri6
        6,  # kAnsTriShell6
        8,  # kAnsQuad8
        8,  # kAnsQuadShell8
        3,  # kAnsLine3
        1,  # kAnsPoint1
        4,  # kAnsTet4
        8,  # kAnsHex8
        6,  # kAnsWedge6
        5,  # kAnsPyramid5
        3,  # kAnsTri3
        3,  # kAnsTriShell3
        4,  # kAnsQuad4
        4,  # kAnsQuadShell4
        2,  # kAnsLine2
        0,  # kAnsNumElementTypes
        0,  # kAnsUnknown
        0,  # kAnsEMagLine
        0,  # kAnsEMagArc
        0,  # kAnsEMagCircle
        3,  # kAnsSurface3
        4,  # kAnsSurface4
        6,  # kAnsSurface6
        8,  # kAnsSurface8
        2,  # kAnsEdge2
        3,  # kAnsEdge3
        3,  # kAnsBeam3
        4,  # kAnsBeam4
        0,  # kAnsGeneralPlaceholder
        -1,  # kAnsPolygon
        -1,  # kAnsPolyhedron
    ]
)  # kAnsBeam4


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
        self, msg="To use plotting capabilities, please install pyvista "
                  "with :\n pip install pyvista>=0.32.0"
    ):
        ModuleNotFoundError.__init__(self, msg)


def dpf_mesh_to_vtk(nodes, etypes, connectivity, as_linear=True, mesh=None):
    """Return a pyvista unstructured grid given DPF node and element
    definitions.

    Parameters
    ----------
    nodes : np.ndarray
        Numpy array containing the nodes of the mesh.

    etypes : np.ndarray
        ANSYS DPF element types.

    connectivity : np.ndarray
        Array containing the nodes used by each element.

    Returns
    -------
    grid : pyvista.UnstructuredGrid
        Unstructured grid of the DPF mesh.
    """
    elem_size = np.ediff1d(np.append(connectivity._data_pointer, connectivity.shape))

    polys_mask = etypes == 34
    polys_indices = np.nonzero(polys_mask)
    global_etypes = etypes
    etypes = np.delete(etypes, polys_indices)
    polys_types = np.delete(global_etypes, np.nonzero(polys_mask == 0))

    # elem_size[polys_mask] = 0
    faces_nodes_connectivity = mesh.property_field("faces_nodes_connectivity")
    faces_nodes_connectivity_dp = faces_nodes_connectivity._data_pointer
    elements_faces_connectivity = mesh.property_field("elements_faces_connectivity")
    #
    n_faces_per_element = np.ediff1d(elements_faces_connectivity._data_pointer)
    n_points_per_face = np.ediff1d(faces_nodes_connectivity._data_pointer)

    insert_ind = np.cumsum(elem_size)
    insert_ind = np.hstack(([0], insert_ind))[:-1]

    # TODO: Investigate why connectivity can be -1
    nullmask = connectivity.data == -1
    connectivity.data[nullmask] = 0
    if nullmask.any():
        nodes[0] = np.nan

    # For each polyhedron, cell = [nCellFaces, nFace0pts, i, j, k, ..., nFace1pts, i, j, k, ...]
    # partition cells in vtk format
    cells = np.insert(connectivity.data, insert_ind, elem_size)
    polys_ind = insert_ind[polys_mask]
    cells = np.take(cells, sorted(set(insert_ind)-set(polys_ind)))

    def compute_offset():
        """Return the starting point of a cell in the cells array"""
        return insert_ind + np.arange(insert_ind.size)

    # convert kAns to VTK cell type
    offset = None
    if as_linear:
        vtk_cell_type = VTK_LINEAR_MAPPING[etypes]

        # visualization bug within VTK with quadratic surf cells
        ansquad8_mask = etypes == 6
        if np.any(ansquad8_mask):  # kAnsQuad8

            # simply copy the edge node indices to the midside points
            offset = compute_offset()
            cell_pos = offset[ansquad8_mask]
            cells[cell_pos + 5] = cells[cell_pos + 1]
            cells[cell_pos + 6] = cells[cell_pos + 2]
            cells[cell_pos + 7] = cells[cell_pos + 3]
            cells[cell_pos + 8] = cells[cell_pos + 4]

        anstri6_mask = etypes == 4  # kAnsTri6 = 4
        if np.any(anstri6_mask):
            if offset is None:
                offset = compute_offset()
            cell_pos = offset[anstri6_mask]
            cells[cell_pos + 4] = cells[cell_pos + 1]
            cells[cell_pos + 5] = cells[cell_pos + 2]
            cells[cell_pos + 6] = cells[cell_pos + 3]

    else:
        vtk_cell_type = VTK_MAPPING[etypes]
    vtk_polys_types = VTK_MAPPING[polys_types]
    # different treatment depending on the version of vtk
    if VTK9:
        # compute offset array when < VTK v9
        grid = pv.UnstructuredGrid(cells, vtk_cell_type, nodes)
        # Add polyhedrons
        for poly_index in polys_indices[0]:
            faces_vtk = vtkIdList()
            face_vtkIdList = vtkIdList()
            n_faces = n_faces_per_element[poly_index]  # The number of faces for the element.
            face_vtkIdList.InsertNextId(n_faces)
            face_connectivity = elements_faces_connectivity.data[
                                elements_faces_connectivity._data_pointer[poly_index]:elements_faces_connectivity._data_pointer[poly_index+1]]

            faces_vtk = []
            points_vtk = []
            for face_i in range(n_faces):

                face_index = face_connectivity[face_i]
                # n_points = n_points_per_face[face_index]
                face_nodes = faces_nodes_connectivity.data[
                             faces_nodes_connectivity_dp[face_index]:faces_nodes_connectivity_dp[face_index+1]]
                face_vtkIdList.InsertNextId(len(face_nodes))  # The number of points in the face.
                [face_vtkIdList.InsertNextId(i) for i in face_nodes]

                face_as_list = [len(face_nodes)]
                face_as_list.extend(face_nodes)
                face_as_array = np.asarray(face_as_list, dtype=np.int64)
                face_vtk = numpy_to_vtkIdTypeArray(face_as_array)
                # faces_vtk.InsertNextId(face_vtk.)
                points_vtk.extend([len(face_nodes)])
                points_vtk.extend(face_nodes)
                faces_vtk.extend([face_index])

            ptIds = connectivity.data[connectivity._data_pointer[poly_index]:connectivity._data_pointer[poly_index+1]]
            # grid.InsertNextCell(polys_types[poly_index], len(ptIds), points_vtk, n_faces, faces_vtk)
            grid.InsertNextCell(polys_types[poly_index], face_vtkIdList)
            break
        return grid

    # might be computed when checking for VTK quadratic bug
    if offset is None:
        offset = compute_offset()

    return pv.UnstructuredGrid(offset, cells, vtk_cell_type, nodes)
