# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Geometry.

Module containing the different geometry objects.

"""

import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import Field
from ansys.dpf.core.fields_factory import field_from_array
from ansys.dpf.core.plotter import DpfPlotter


def normalize_vector(vector):
    """Normalize vector."""
    return vector / np.linalg.norm(vector)


class Points:
    """
    Collection of DPF points.

    This can be a single point or a cloud of points.

    Parameters
    ----------
    coordinates: array, list, Field
        Coordinates of the points in a 3D space.
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Create Points object with two points, print object information and plot.

    >>> from ansys.dpf.core.geometry import Points
    >>> points = Points([[0, 0, 0], [1, 0, 0]])
    >>> print(points)
    DPF Points object:
    Number of points: 2
    Coordinates:
      [0. 0. 0.]
      [1. 0. 0.]
    >>> points.plot()

    """

    def __init__(self, coordinates, server=None):
        # Input check
        if not isinstance(coordinates, Field):
            coordinates = field_from_array(coordinates, server=server)

        self._coordinates = coordinates
        self._server = server

    def __getitem__(self, value):
        """Retrieve coordinates data corresponding to a given value."""
        return self.coordinates.data[value]

    def __len__(self):
        """Retrieve the number of points."""
        return self.n_points

    def __str__(self):
        """Print Points information."""
        txt = "DPF Points object:\n"
        txt += f"Number of points: {self.n_points}\n"
        txt += f"Coordinates:\n"
        for point in self._coordinates.data:
            txt += f"  {point}\n"
        return txt

    @property
    def coordinates(self):
        """Coordinates of the Points."""
        return self._coordinates

    @property
    def n_points(self):
        """Total number of points."""
        return self._coordinates.shape[0] if isinstance(self._coordinates.shape, tuple) else 1

    @property
    def dimension(self):
        """Dimension of the Points object space."""
        return 3

    def plot(self, mesh=None, **kwargs):
        """Visualize Points object. If provided, ``mesh`` will be also plotted."""
        cpos = kwargs.pop("cpos", None)
        pl = DpfPlotter(**kwargs)
        pl.add_points(self._coordinates.data, render_points_as_spheres=True, **kwargs)
        if mesh:
            pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
        pl.show_figure(show_axes=True, cpos=cpos)


class Line:
    """
    Create Line object from two 3D points.

    Parameters
    ----------
    coordinates: array, list, Field, Points
        3D coordinates of the two points defining the line.
    n_points: int
        Number of points used to discretize the line (optional).
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Create a line from two points, print object information and plot.

    >>> from ansys.dpf.core.geometry import Line
    >>> line = Line([[0, 0, 0], [1, 0, 0]])
    >>> print(line)
    DPF Line object:
    Starting point: [0. 0. 0.]
    Ending point: [1. 0. 0.]
    Line discretized with 100 points
    >>> line.plot()

    """

    def __init__(self, coordinates, n_points=100, server=None):
        """Initialize line object from two 3D points and discretize."""
        if not isinstance(coordinates, Field):
            coordinates = np.asarray(coordinates, dtype=np.number)
            coordinates = field_from_array(coordinates)
        if not len(coordinates.data) == 2:
            raise ValueError("Only two points must be introduced to define a line")

        self._coordinates = coordinates
        self._server = server
        self._n_points = n_points
        self._length = np.linalg.norm(coordinates.data)
        self._mesh, self._path = self._discretize()

    def __getitem__(self, value):
        """Overwrite getitem so coordinates.data is iterable."""
        return self.coordinates.data[value]

    def __len__(self):
        """Overwrite len so it returns the number of points."""
        return len(self._coordinates.data)

    def __str__(self):
        """Print line information."""
        txt = "DPF Line object:\n"
        txt += f"Starting point: {self._coordinates.data[0]}\n"
        txt += f"Ending point: {self._coordinates.data[-1]}\n"
        txt += f"Line discretized with {self._n_points} points\n"
        return txt

    def _discretize(self):
        """Discretize line."""
        origin = self._coordinates.data[0]
        diff = self._coordinates.data[1] - self._coordinates.data[0]
        path_1D = np.linspace(0, self.length, self._n_points)
        path_3D = [origin + i_point * diff / self._n_points for i_point in range(self._n_points)]

        # Create mesh for a line
        mesh = dpf.MeshedRegion(
            num_nodes=self._n_points,
            num_elements=self._n_points - 1,
            server=self._server,
        )
        for i, node in enumerate(mesh.nodes.add_nodes(self._n_points)):
            node.id = i + 1
            node.coordinates = path_3D[i]

        for i in range(self._n_points - 1):
            mesh.elements.add_beam_element(i + 1, [i, i + 1])

        return mesh, path_1D

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
        """Get line length."""
        return self._length

    @property
    def path(self):
        """Get line path (1D line coordinate)."""
        return self._path

    @property
    def n_points(self):
        """Get number of points for the line discretization."""
        return self._n_points

    @property
    def direction(self):
        """Normalized direction vector between the two points defining the line."""
        diff = [x - y for x, y in zip(self._coordinates.data[1], self._coordinates.data[0])]
        return diff / np.linalg.norm(diff)

    def plot(self, mesh=None, **kwargs):
        """Visualize line. If provided, ``mesh`` will be also plotted."""
        cpos = kwargs.pop("cpos", None)
        if not cpos:
            # Check if line is along the [1, 1, 1] direction to change camera position
            if np.isclose(np.abs(self.direction), normalize_vector(np.array([1, 1, 1]))).all():
                cpos = "xy"
            else:
                cpos = None

        # Plot line object
        pl = DpfPlotter(**kwargs)
        pl.add_line(self._coordinates.data, **kwargs)
        if mesh:
            pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
        pl.show_figure(show_axes=True, cpos=cpos)


class Plane:
    """
    Plane object.

    Parameters
    ----------
    center : array, list
        3D coordinates of the center point of the plane.
    normal : array, list, Line
        Normal direction to the plane.
    width : int, float
        Width of the discretized plane (default = 1).
    height : int, float
        Height of the discretized plane (default = 1).
    n_cells_x : int
        Number of cells in the x direction of the plane.
    n_cells_y : int
        Number of cells in the y direction of the plane.
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Create a plane from its center and normal direction, print object information and plot.

    >>> from ansys.dpf.core.geometry import Plane
    >>> plane = Plane([0, 0, 0], [1, 0, 0])
    >>> print(plane)
    DPF Plane object:
    Center point: [0, 0, 0]
    Normal direction: [1. 0. 0.]
    Plane discretizaton using:
      Width (x-dir): 1
      Height (y-dir): 1
      Num cells x-dir: 20
      Num cells y-dir: 20
    >>> plane.plot()

    """

    def __init__(self, center, normal, width=1, height=1, n_cells_x=20, n_cells_y=20, server=None):
        """Initialize Plane object from its center and normal direction."""
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
                normal_vect = [np.array([0, 0, 0]), normal_dir]
        else:
            normal_vect = [normal.coordinates.data[0], normal.coordinates.data[1]]
            normal_dir = self._get_direction_from_vect(normal_vect)
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise ValueError("Width and height must be either integers of floats.")
        if not isinstance(n_cells_x, int) or not isinstance(n_cells_y, int):
            raise ValueError("Number of cells x and y must be either integers.")

        self._center = center
        self._normal_vect = normal_vect
        self._normal_dir = normal_dir
        self._server = server
        self._mesh = None
        self._width = width
        self._height = height
        self._n_cells_x = n_cells_x
        self._n_cells_y = n_cells_y
        self._axes_plane = None
        self._discretize()

    def __str__(self):
        """Print plane information."""
        txt = "DPF Plane object:\n"
        txt += f"Center point: {self._center}\n"
        txt += f"Normal direction: {self._normal_dir}\n"
        if self._mesh:
            txt += "Plane discretizaton using:\n"
            txt += f"  Width (x-dir): {self.width}\n"
            txt += f"  Height (y-dir): {self.height}\n"
            txt += f"  Num cells x-dir: {self.n_cells_x}\n"
            txt += f"  Num cells y-dir: {self.n_cells_y}\n"
        else:
            txt += "Plane has not been discretized.\n"
            txt += "  Use plane.discretize(width, height, n_cells_x, n_cells_y)\n"
        return txt

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

    @property
    def width(self):
        """Get width of the discretized plane."""
        return self._width

    @property
    def height(self):
        """Get height of the discretized plane."""
        return self._height

    @property
    def n_cells_x(self):
        """Get number of cells in the x direction of the plane."""
        return self._n_cells_x

    @property
    def n_cells_y(self):
        """Get number of cells in the y direction of the plane."""
        return self._n_cells_y

    def _discretize(self):
        """Discretize plane with a certain size and number of cells per direction."""
        # Get plane axis (local) from reference axis (global) and plane's normal
        self._axes_plane = get_plane_local_axis(self._normal_dir)

        # Create grid on plane coordinates
        num_nodes = (self._n_cells_x + 1) * (self._n_cells_y + 1)
        x_range = np.linspace(-self._width / 2, self._width / 2, self._n_cells_x + 1)
        y_range = np.linspace(-self._height / 2, self._height / 2, self._n_cells_y + 1)
        meshgrid = np.meshgrid(x_range, y_range)
        plane_coords = [
            meshgrid[0].flatten(),
            meshgrid[1].flatten(),
            np.zeros(num_nodes),
        ]

        # Map coordinates from plane to global coordinates system
        global_coords = np.zeros([num_nodes, 3])
        for i in range(num_nodes):
            node_coords = np.array([plane_coords[0][i], plane_coords[1][i], plane_coords[2][i]])
            global_coords[i, :] = np.dot(node_coords, self._axes_plane) + self._center

        # Create mesh
        num_elems = self._n_cells_x * self._n_cells_y
        mesh = dpf.MeshedRegion(num_nodes=num_nodes, num_elements=num_elems, server=self._server)
        for i, node in enumerate(mesh.nodes.add_nodes(num_nodes)):
            node.id = i + 1
            node.coordinates = global_coords[i]

        # Build connectivity
        for i in range(num_elems):
            i_col = i // self._n_cells_x
            element_connectivity = [
                i_col + i,
                i_col + i + 1,
                i_col + self._n_cells_x + 1 + i + 1,
                i_col + self._n_cells_x + 1 + i,
            ]
            mesh.elements.add_solid_element(i + 1, element_connectivity)

        # Store mesh
        self._mesh = mesh

    def _get_direction_from_vect(self, vect):
        """Get normal direction to the plane."""
        direction = [x - y for x, y in zip(vect[1], vect[0])]
        return normalize_vector(direction)

    def plot(self, mesh=None, **kwargs):
        """Visualize plane object. If provided, ``mesh`` will be also plotted."""
        cpos = kwargs.pop("cpos", None)
        if not cpos:
            # Check if normal is in [1, -1, 0] direction to change camera position
            no_vision_normal = normalize_vector(np.array([1, -1, 0]))
            if (
                np.isclose(self.normal_dir, no_vision_normal).all()
                or np.isclose(self.normal_dir, -no_vision_normal).all()
            ):
                cpos = "xz"
            else:
                cpos = None

        # Plot plane object
        pl = DpfPlotter(**kwargs)
        pl.add_plane(self, **kwargs)
        if mesh:
            pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
        pl.show_figure(show_axes=True, cpos=cpos)


def get_plane_local_axis(normal_dir):
    """Determine local axis of the plane."""
    axis_ref = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
    if np.allclose(abs(normal_dir), [1.0, 0.0, 0.0]):
        plane_x = np.cross(axis_ref[1], normal_dir)
        plane_y = np.cross(normal_dir, plane_x)
    else:
        plane_y = np.cross(axis_ref[0], normal_dir)
        plane_x = np.cross(normal_dir, plane_y)
    plane_z = normal_dir

    plane_x = normalize_vector(plane_x)
    plane_y = normalize_vector(plane_y)
    plane_z = normalize_vector(plane_z)
    return [plane_x, plane_y, plane_z]


def get_global_coords_from_local(local_coords, axes_plane, center):
    """Determine global coordinates from local coordinates."""
    return np.dot(local_coords, axes_plane) + center


def get_local_coords_from_global(global_coords, axes_plane, center):
    """Determine local coordinates from global coordinates."""
    return np.dot(axes_plane, (global_coords - np.array(center)))
