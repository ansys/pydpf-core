"""Module containing the different geometry objects."""

from ansys.dpf import core as dpf

from ansys.dpf.core import Field
from ansys.dpf.core.fields_factory import field_from_array
from ansys.dpf.core.plotter import DpfPlotter

import numpy as np


class Points:
    """
    Collection of DPF points.

    This can be a single point or a cloud of points.

    Parameters
    ----------
    coordinates: Field
        Coordinates of the points in a 3D space.

    Examples
    --------
    TO DO

    """

    def __init__(self, coordinates, server=None):
        # Input check
        if not isinstance(coordinates, Field):
            coordinates = field_from_array(coordinates, server=server)

        self._coordinates = coordinates
        self._server = server

    def __getitem__(self, value):
        return self.coordinates.data[value]

    def __len__(self):
        return self.num_points

    @property
    def coordinates(self):
        """Coordinates of the Points."""
        return self._coordinates

    @property
    def num_points(self):
        return (
            self._coordinates.shape[0]
            if isinstance(self._coordinates.shape, tuple)
            else 1
        )

    @property
    def dimension(self):
        return 3

    def __str__(self):
        """Print Points information."""
        txt = "DPF Points object:\n"
        txt += f"Coordinates: {self.coordinates}\n"
        return txt

    def plot(self, **kwargs):
        """Visualize Points object."""
        pl = DpfPlotter(**kwargs)
        pl.add_points(self._coordinates.data)
        pl.show_figure()


class Line:
    """
    Line object.

    Parameters
    ----------
    coordinates: Field
        Coordinates of the two points defining the line.

    Examples
    --------
    TO DO

    """

    def __init__(self, coordinates, num_points=100, server=None):
        if not isinstance(coordinates, Field):
            coordinates = field_from_array(coordinates)
        if not len(coordinates.data) == 2:
            raise ValueError("Only two points have to be introduced to define a line")

        self._coordinates = coordinates
        self._server = server
        self._num_points = num_points
        self._mesh, self._length = self._discretize()

    def __getitem__(self, value):
        return self.coordinates.data[value]

    def __len__(self):
        return len(self._coordinates.data)

    def _discretize(self):
        origin = self._coordinates.data[0]
        diff = self._coordinates.data[1] - self._coordinates.data[0]
        i_points = np.linspace(0, 1, self._num_points)
        path = [origin + i_point * diff for i_point in i_points]

        # Create mesh for a line
        mesh = dpf.MeshedRegion(
            num_nodes=self._num_points,
            num_elements=self._num_points - 1,
            server=self._server,
        )
        for i, node in enumerate(mesh.nodes.add_nodes(self._num_points)):
            node.id = i + 1
            node.coordinates = path[i]

        [
            mesh.elements.add_beam_element(i + 1, [i, i + 1])
            for i in range(self._num_points - 1)
        ]
        return mesh, i_points

    @property
    def coordinates(self):
        """Coordinates of the two points defining the line."""
        return self._coordinates

    @property
    def mesh(self):
        """Get line mesh."""
        return self._mesh

    @property
    def length(self):
        """Get line length coordinate in 1D."""
        return self._length

    @property
    def direction(self):
        """Normalized direction vector between the two points defining the line."""
        diff = [
            x - y for x, y in zip(self._coordinates.data[1], self._coordinates.data[0])
        ]
        return diff / np.linalg.norm(diff)

    def plot(self, **kwargs):
        pl = DpfPlotter(**kwargs)
        pl.add_line(self._coordinates.data)
        pl.show_figure()


class Plane:
    """
    Plane object.

    Parameters
    ----------

    Examples
    --------

    """

    def __init__(self, center, normal, server=None):
        # Input check
        if not len(center) == 3:
            raise ValueError("'center' of the plane must have length 3")
        if not isinstance(normal, Line):
            if len(normal) == 2:
                if not len(normal[0]) == len(normal[1]) == 3:
                    raise ValueError("Each point must contain 3 coordinates.")
                normal_vect = normal
                normal_dir = self._get_direction_from_vect(normal_vect)
            elif len(normal) == 3:
                normal_dir = normal / np.linalg.norm(normal)
                normal_vect = [[0, 0, 0], normal_dir]
        else:
            normal_vect = [normal.coordinates.data[0], normal.coordinates.data[1]]
            normal_dir = self._get_direction_from_vect(normal_vect)

        self._center = center
        self._normal_vect = normal_vect
        self._normal_dir = normal_dir
        self._server = server
        self._mesh = None
        self.nodes = None

    @property
    def center(self):
        """Center of the plane."""
        return self._center

    @property
    def normal_vect(self):
        """Normal vector to the plane."""
        return self._normal_vect

    @property
    def normal_dir(self):
        """Normal direction to the plane."""
        return self._normal_dir

    @property
    def mesh(self):
        """Get discretized mesh for the plane."""
        return self._mesh

    def _normalize_vector(self, vector):
        return vector / np.linalg.norm(vector)

    def discretize(self, width, height, num_cells_x, num_cells_y):
        # Get plane axis (local) from reference axis (global) and plane's normal
        normal = self._normal_dir
        axis_ref = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
        if np.allclose(normal, [1.0, 0.0, 0.0]):
            plane_x = np.cross(axis_ref[1], normal)
            plane_y = np.cross(normal, plane_x)
        else:
            plane_y = np.cross(axis_ref[0], normal)
            plane_x = np.cross(normal, plane_y)
        plane_z = normal

        plane_x = self._normalize_vector(plane_x)
        plane_y = self._normalize_vector(plane_y)
        plane_z = self._normalize_vector(plane_z)
        axis_plane = [plane_x, plane_y, plane_z]

        # Create grid on plane coordinates
        num_nodes = (num_cells_x + 1) * (num_cells_y + 1)
        x_range = np.linspace(-width / 2, width / 2, num_cells_x + 1)
        y_range = np.linspace(-height / 2, height / 2, num_cells_y + 1)
        meshgrid = np.meshgrid(x_range, y_range)
        plane_coords = [
            meshgrid[0].flatten(),
            meshgrid[1].flatten(),
            np.zeros(num_nodes),
        ]

        # Map coordinates from plane to global coordinates system
        global_coords = np.zeros([num_nodes, 3])
        for i in range(num_nodes):
            node_coords = np.array(
                [plane_coords[0][i], plane_coords[1][i], plane_coords[2][i]]
            )
            global_coords[i, :] = np.dot(node_coords, axis_plane) + self._center

        # Create mesh
        num_elems = num_cells_x * num_cells_y
        mesh = dpf.MeshedRegion(
            num_nodes=num_nodes, num_elements=num_elems, server=self._server
        )
        for i, node in enumerate(mesh.nodes.add_nodes(num_nodes)):
            node.id = i + 1
            node.coordinates = global_coords[i]

        # Build connectivity
        for i in range(num_elems):
            i_col = i // num_cells_x
            element_connectivity = [
                i_col + i,
                i_col + i + 1,
                i_col + num_cells_x + 1 + i + 1,
                i_col + num_cells_x + 1 + i,
            ]
            mesh.elements.add_solid_element(i + 1, element_connectivity)

        # Store mesh
        self._mesh = mesh

    def _get_direction_from_vect(self, vect):
        """Normal direction to the plane."""
        direction = [x - y for x, y in zip(vect[1], vect[0])]
        return self._normalize_vector(direction)

    def plot(self, **kwargs):
        pl = DpfPlotter(**kwargs)
        pl.add_plane(self._center, self._normal_dir)
        pl.show_figure()
