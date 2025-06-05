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
Geometry Factory.

Geometry factory module containing functions to create the different geometries.
"""

import numpy as np

from ansys.dpf.core.geometry import (
    Line,
    Plane,
    Points,
    get_local_coords_from_global,
    get_plane_local_axis,
    normalize_vector,
)


def create_points(coordinates, server=None):
    """Construct points given its coordinates.

    Parameters
    ----------
    coordinates : list, array, Field
        3D coordinates of the points.
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf.core.geometry_factory import create_points
    >>> points = create_points([[1, 1, 1], [2, 1, 1], [0, 2, 0]])
    >>> print(points)
    DPF Points object:
    Number of points: 3
    Coordinates:
      [1. 1. 1.]
      [2. 1. 1.]
      [0. 2. 0.]
    >>> points.plot()
    """
    return Points(coordinates, server)


def create_line_from_points(points, n_points=100, server=None):
    """Construct line from two points.

    Parameters
    ----------
    points : list, array, Field, Points
        3D coordinates of the points.
    n_points : int
        Number of points in which the line will be discretized.
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf.core.geometry_factory import create_line_from_points
    >>> line = create_line_from_points([[0, 0, 0], [1, 1, 1]])
    >>> print(line)
    DPF Line object:
    Starting point: [0. 0. 0.]
    Ending point: [1. 1. 1.]
    Line discretized with 100 points
    >>> line.plot()

    """
    return Line(points, n_points, server)


def create_line_from_vector(ini, end=None, n_points=100, server=None):
    """Construct line from origin's coordinates and a vector direction.

    Parameters
    ----------
    ini : list, array, Line
        List 3D coordinates of the initial and ending points of the line.
    end : list, array, Line, optional
        3D coordinates of the ending point of the line (if ``ini`` only contains
        the initial point).
    n_points : int
        Number of points in which the line will be discretized.
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf.core.geometry_factory import create_line_from_vector
    >>> line = create_line_from_vector([0, 0, 0], [2, 2, 2])
    >>> print(line)
    DPF Line object:
    Starting point: [0. 0. 0.]
    Ending point: [2. 2. 2.]
    Line discretized with 100 points
    >>> line.plot()

    """
    # Input check
    if isinstance(ini[0], list):
        if not len(ini) == 2:
            raise ValueError("Exactly two points must be passed to define the vector")
        if not len(ini[0]) == len(ini[1]) == 3:
            raise ValueError("Each point must contain three coordinates 'x', 'y' and 'z'.")
        vect = ini
    else:
        if not len(ini) == 3:
            raise ValueError(
                "'ini' argument must be of length = 3 \
            representing the 3D coordinates of the origin of the vector."
            )
        if not len(end) == 3:
            raise ValueError(
                "'end' argument must be of length = 3 \
            representing the 3D coordinates of the end point of the vector."
            )
        vect = [ini, end]

    return Line(vect, n_points, server)


def create_plane_from_center_and_normal(
    center, normal, width=1, height=1, n_cells_x=20, n_cells_y=20, server=None
):
    """Create plane from its center and normal direction.

    Parameters
    ----------
    center : list, array, Points
        3D coordinates of the center point of the plane.
    normal : list, array, Line
        Normal direction to the plane.
    width : int, float
        Width of the discretized plane (default = 1).
    height : int, float
        Height of the discretized plane (default = 1).
    n_cells_x : int
        Number of cells in the x direction of the plane (default = 20).
    n_cells_y : int
        Number of cells in the y direction of the plane (default = 20).
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf.core.geometry_factory import create_plane_from_center_and_normal
    >>> plane = create_plane_from_center_and_normal([1, 1, 1], [0, 0, 1])
    >>> print(plane)
    DPF Plane object:
    Center point: [1, 1, 1]
    Normal direction: [0. 0. 1.]
    Plane discretizaton using:
      Width (x-dir): 1
      Height (y-dir): 1
      Num cells x-dir: 20
      Num cells y-dir: 20
    >>> plane.plot()

    """
    return Plane(center, normal, width, height, n_cells_x, n_cells_y, server)


def create_plane_from_points(points, n_cells_x=20, n_cells_y=20, server=None):
    """Create plane from three points.

    Note that when creating a plane using three points, the plane's width and height
    will be computed such that the three points are the corner points of the plane.

    Parameters
    ----------
    points : list, array, Points
        3D coordinates of the three points defining the plane.
    n_cells_x : int
        Number of cells in the x direction of the plane (default = 20).
    n_cells_y : int
        Number of cells in the y direction of the plane (default = 20).
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf.core.geometry_factory import create_plane_from_points
    >>> plane = create_plane_from_points([[0, 0, 0], [0, 0, 4], [0, 4, 0]])
    >>> print(plane)
    DPF Plane object:
    Center point: [0.0, 1.3333333333333333, 1.3333333333333333]
    Normal direction: [-1.  0.  0.]
    Plane discretizaton using:
      Width (x-dir): 4.0
      Height (y-dir): 4.0
      Num cells x-dir: 20
      Num cells y-dir: 20
    >>> plane.plot()

    """
    # Input check
    if isinstance(points, Points):
        if not len(points) == 3:
            raise ValueError(
                "Exactly three points must be passed to construct a plane from points."
            )
    else:
        if not len(points) == 3:
            raise ValueError("Exactly three coordinates must be provided to create a plane.")
        if not len(points[0]) == len(points[1]) == len(points[2]) == 3:
            raise ValueError("Each point must contain three coordinates.")

    # Get center and normal from points
    center = get_center_from_coords(points)
    normal_dir = get_normal_direction_from_coords(points)

    # Get width and height from points
    axes_plane = get_plane_local_axis(normal_dir)
    points_local = [get_local_coords_from_global(points[i], axes_plane, center) for i in range(3)]
    x_coords = np.array(points_local)[:, 0]
    y_coords = np.array(points_local)[:, 1]
    width = float(x_coords.max() - x_coords.min())
    height = float(y_coords.max() - y_coords.min())

    return Plane(center, normal_dir, width, height, n_cells_x, n_cells_y, server)


def create_plane_from_lines(
    line1, line2, width=1, height=1, n_cells_x=20, n_cells_y=20, server=None
):
    """Create plane from two lines.

    Parameters
    ----------
    line1 : list, array, Line
        3D coordinates of the two points defining a line.
    line2 : list, array, Line
        3D coordinates of the two points defining a line.
    width : int, float
        Width of the discretized plane (default = 1).
    height : int, float
        Height of the discretized plane (default = 1).
    n_cells_x : int
        Number of cells in the x direction of the plane (default = 20).
    n_cells_y : int
        Number of cells in the y direction of the plane (default = 20).
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf.core.geometry_factory import create_plane_from_lines
    >>> plane = create_plane_from_lines([[0, 0, 0], [1, 1, 1]], [[0, 1, 0], [2, 1, 0]])
    >>> print(plane)
    DPF Plane object:
    Center point: [-1.5, -0.5, -0.5]
    Normal direction: [ 0.          0.70710678 -0.70710678]
    Plane discretizaton using:
      Width (x-dir): 1
      Height (y-dir): 1
      Num cells x-dir: 20
      Num cells y-dir: 20
    >>> plane.plot()

    """
    # Input check
    if not isinstance(line1, Line) and not isinstance(line2, Line):
        if not len(line1) == len(line2) == 2:
            raise ValueError("Each line must contain two points.")
        if not len(line1[0]) == len(line1[1]) == len(line2[0]) == len(line2[1]) == 3:
            raise ValueError("Each point must contain three coordinates.")

    # Get center and normal from points
    vect1 = [x - y for x, y in zip(line1[0], line1[1])]
    vect2 = [x - y for x, y in zip(line2[0], line2[1])]
    center = get_center_from_coords([vect1, vect2])
    normal = get_cross_product([vect1, vect2])
    return Plane(center, normal, width, height, n_cells_x, n_cells_y, server)


def create_plane_from_point_and_line(
    point, line, width=1, height=1, n_cells_x=20, n_cells_y=20, server=None
):
    """Create plane from point and line.

    Raises a ValueError if the point is on the line.

    Parameters
    ----------
    point : list, array, Points
        3D coordinates of the point.
    line : list, array, Line
        3D coordinates of the two points defining a line.
    width : int, float
        Width of the discretized plane (default = 1).
    height : int, float
        Height of the discretized plane (default = 1).
    n_cells_x : int
        Number of cells in the x direction of the plane (default = 20).
    n_cells_y : int
        Number of cells in the y direction of the plane (default = 20).
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf.core.geometry_factory import create_plane_from_point_and_line
    >>> plane = create_plane_from_point_and_line([1, 2, 1], [[0, 0, 0], [1, 1, 1]])
    >>> print(plane)
    DPF Plane object:
    Center point: [0.6666666666666666, 1.0, 0.6666666666666666]
    Normal direction: [-0.70710678  0.          0.70710678]
    Plane discretizaton using:
      Width (x-dir): 1
      Height (y-dir): 1
      Num cells x-dir: 20
      Num cells y-dir: 20
    >>> plane.plot()

    """
    # Input check
    if isinstance(point, Points):
        if not len(point) == 1:
            raise ValueError("Only one point must be passed.")
    else:
        if not len(point) == 3:
            raise ValueError("A point must contain three coordinates 'x', 'y' and 'z'.")
    if not isinstance(line, Line):
        if not len(line) == 2:
            raise ValueError("'line' must be of length = 2 containing two points.")
        if not len(line[0]) == len(line[1]) == 3:
            raise ValueError("Each point in line must contain three coordinates 'x', 'y' and 'z'.")

    # Get center and normal from point and vector
    coords = [line[0], line[1], point]
    normal = get_normal_direction_from_coords(coords)
    if any(np.isnan(x) for x in normal) or (max(normal) == min(normal) == 0):
        raise ValueError(
            "create_plane_from_point_and_line: cannot create a plane from aligned point and line."
        )
    center = get_center_from_coords(coords)
    return Plane(center, normal, width, height, n_cells_x, n_cells_y, server)


def get_center_from_coords(coords):
    """Get average coordinates from several points."""
    n_points = len(coords)
    n_coords = len(coords[0])
    return [sum(coords[i][j] for i in range(n_points)) / n_points for j in range(n_coords)]


def get_normal_direction_from_coords(points):
    """Get normal direction between three points."""
    vects = [
        [points[1][i] - points[0][i] for i in range(len(points))],
        [points[2][i] - points[0][i] for i in range(len(points))],
    ]
    return normalize_vector(get_cross_product(vects))


def get_cross_product(vects):
    """Compute cross product between two vectors."""
    return np.cross(vects[0], vects[1])
