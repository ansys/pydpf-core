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
        self._path = self._discretize()

    def __getitem__(self, value):
        return self.coordinates.data[value]

    def __len__(self):
        return len(self._coordinates.data)

    def _discretize(self):
        origin = self._coordinates.data[0]
        diff = self._coordinates.data[1]-self._coordinates.data[0]
        i_points = np.linspace(0,1,self._num_points)
        path = [origin + i_point*diff for i_point in i_points]
        # return over_time_freq_fields_container(path)
        return field_from_array(path)

    @property
    def coordinates(self):
        """Coordinates fo the two points defining the line."""
        return self._coordinates

    @property
    def path(self):
        """Get discretized path"""
        return self._path

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
                normal_dir = normal
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

    def discretize(self, x_l, y_l, z_l, resolution):
        normal = self._normal_dir
        center = self._center
        x_delta = (1-normal[0])*x_l
        y_delta = (1-normal[1])*y_l
        z_delta = (1-normal[2])*z_l
        x_lim = [center[0]-x_delta, center[0] + x_delta]
        y_lim = [center[1]-y_delta, center[1] + y_delta]
        z_lim = [center[2]-z_delta, center[2] + z_delta]
        x_range = np.unique(np.linspace(x_lim[0], x_lim[1], resolution))
        y_range = np.unique(np.linspace(y_lim[0], y_lim[1], resolution))
        z_range = np.unique(np.linspace(z_lim[0], z_lim[1], resolution))
        meshgrid = np.meshgrid(x_range, y_range, z_range)
        # self.nodes = np.reshape(meshgrid, [25,3])
        self.grid = pv.StructuredGrid(meshgrid[0], meshgrid[1], meshgrid[2])
        # plotter = pv.Plotter()
        # plotter.add_mesh(self.grid, scalars=self.grid[:,-1], show_edges=True,
        #                 scalar_bar_args={'vertical': True})
        # plotter.show_grid()
        # plotter.show()
        # test = 1


    def _get_direction_from_vect(self, vect):
        """Normal direction to the plane."""
        direction = [x - y for x,y in zip(vect[1], vect[0])]
        return direction / np.linalg.norm(direction)

    def plot(self, **kwargs):
        pl = DpfPlotter(**kwargs)
        pl.add_plane(self._center, self._normal_dir)
        pl.show_figure()



