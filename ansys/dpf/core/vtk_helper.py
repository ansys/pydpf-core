import numpy as np
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
    vtkVersion,
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
        4,
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
        0,
    ]
)  # kAnsBeam4 = 31,


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
        0,
    ]
)  # kAnsBeam4 = 31,


class PyVistaImportError(ModuleNotFoundError):
    """Error raised when PyVista could not be imported during plotting."""

    def __init__(
        self, msg="To use plotting capabilities, please install pyvista "
                  "with :\n pip install pyvista>=0.32.0"
    ):
        ModuleNotFoundError.__init__(self, msg)


def dpf_mesh_to_vtk(nodes, etypes, connectivity, as_linear=True):
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
        Unstructred grid of the DPF mesh.
    """
    # could make this more efficient in C...
    elem_size = SIZE_MAPPING[etypes]
    insert_ind = np.cumsum(elem_size)
    insert_ind = np.hstack(([0], insert_ind))[:-1]

    # TODO: Investigate why connectivity can be -1
    nullmask = connectivity == -1
    connectivity[nullmask] = 0
    if nullmask.any():
        nodes[0] = np.nan

    # partition cells in vtk format
    cells = np.insert(connectivity, insert_ind, elem_size)

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

    # different treatment depending on the version of vtk
    if VTK9:
        # compute offset array when < VTK v9
        return pv.UnstructuredGrid(cells, vtk_cell_type, nodes)

    # might be computed when checking for VTK quadratic bug
    if offset is None:
        offset = compute_offset()

    return pv.UnstructuredGrid(offset, cells, vtk_cell_type, nodes)
