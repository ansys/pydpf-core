"""Module containing the different geometry objects."""

from ansys.dpf import core as dpf
from ansys.dpf.core import Field
from ansys.dpf.core.fields_factory import create_3d_vector_field, field_from_array
from ansys.dpf.core.plotter import DpfPlotter

import numpy as np
import pyvista as pv

class Points():
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
        return self._coordinates.shape[0] if isinstance(self._coordinates.shape, tuple) else 1

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

class Line():
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
    def __init__(self, coordinates, num_points = 100, server=None):
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
        diff = self._coordinates.data[1]-self._coordinates.data[0]
        i_points = np.linspace(0,1,self._num_points)
        path = [origin + i_point*diff for i_point in i_points]

        # Create mesh for a line
        mesh = dpf.MeshedRegion(
            num_nodes=self._num_points, num_elements=self._num_points-1, server=self._server
        )
        for i, node in enumerate(mesh.nodes.add_nodes(self._num_points)):
            node.id = i+1
            node.coordinates = path[i]

        [mesh.elements.add_beam_element(i+1, [i, i+1]) for i in range(self._num_points-1)]
        return mesh, i_points

    @property
    def coordinates(self):
        """Coordinates fo the two points defining the line."""
        return self._coordinates

    @property
    def mesh(self):
        """Get line mesh."""
        return self._mesh

    @property
    def length(self):
        """Get line length coordiante in 1D."""
        return self._length

    @property
    def direction(self):
        """Normalized direction vector between the two points defining the line."""
        diff =  [x - y for x,y in zip(self._coordinates.data[1], self._coordinates.data[0])]
        return diff / np.linalg.norm(diff)

    def plot(self, **kwargs):
        pl = DpfPlotter(**kwargs)
        pl.add_line(self._coordinates.data)
        pl.show_figure()


class Plane():
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
        self.grid = None
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

    def discretize(self, x_l, y_l, z_l, resolution):
        normal = self._normal_dir
        center = self._center

        axis_ref = np.array([np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])])
        axis_plane = normal - np.dot(normal, axis_ref)*normal

        # Get rotation-translation matrix
        R0 = np.array([
            [np.cos(axis_plane[0]), -np.sin(axis_plane[0]), 0],
            [np.sin(axis_plane[0]), np.cos(axis_plane[0]), 0],
            [0, 0, 1],
        ])
        R1 = np.array([
            [np.cos(axis_plane[1]), 0, np.sin(axis_plane[1])],
            [0, 1, 0],
            [-np.sin(axis_plane[1]), 0, np.cos(axis_plane[1])],
        ])
        R2 = np.array([
            [1, 0, 0],
            [0, np.cos(axis_plane[2]), -np.sin(axis_plane[2])],
            [0, np.sin(axis_plane[2]), np.cos(axis_plane[2])],
        ])
        R = R0*R1*R2

        point_ref = np.array([1, 1, 1])
        point_plane = np.dot(R, point_ref) + center

        # x_delta = (1-normal[0])*x_l
        # y_delta = (1-normal[1])*y_l
        # z_delta = (1-normal[2])*z_l
        # x_lim = [center[0]-x_delta, center[0] + x_delta]
        # y_lim = [center[1]-y_delta, center[1] + y_delta]
        # z_lim = [center[2]-z_delta, center[2] + z_delta]
        # x_range = np.unique(np.linspace(x_lim[0], x_lim[1], resolution))
        # y_range = np.unique(np.linspace(y_lim[0], y_lim[1], resolution))
        # z_range = np.unique(np.linspace(z_lim[0], z_lim[1], resolution))
        # meshgrid = np.meshgrid(x_range, y_range, z_range)
        # self.grid = pv.StructuredGrid(meshgrid[0], meshgrid[1], meshgrid[2])

        num_points = self.grid.n_points
        num_elems = self.grid.n_cells

        # Create mesh
        mesh = dpf.MeshedRegion(
            num_nodes=num_points, num_elements=num_elems, server=self._server
        )
        for i, node in enumerate(mesh.nodes.add_nodes(num_points)):
            node.id = i+1
            node.coordinates = self.grid.points[i]

        # plot = pv.Plotter()
        # plot.add_points(mesh.nodes.coordinates_field.data)
        # plot.show()

        mesh.elements.add_solid_element(1, [0, 1, 3, 4])
        mesh.elements.add_solid_element(2, [1, 2, 4, 5])
        mesh.elements.add_solid_element(3, [3, 4, 6, 7])
        mesh.elements.add_solid_element(4, [4, 5, 7, 8])
        self._mesh = mesh
        # plot = DpfPlotter()
        # plot.add_mesh(mesh)
        # plot.show_figure()
        # test = 1



    def _get_direction_from_vect(self, vect):
        """Normal direction to the plane."""
        direction = [x - y for x,y in zip(vect[1], vect[0])]
        return direction / np.linalg.norm(direction)

    def plot(self, **kwargs):
        pl = DpfPlotter(**kwargs)
        pl.add_plane(self._center, self._normal_dir)
        pl.show_figure()



