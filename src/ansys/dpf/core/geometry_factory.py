"""Geometry factory module containing functions to create the different geometries."""

import numpy as np

from ansys.dpf.core.geometry import Points, Line, Plane


def create_points(coordinates, server=None):
    """Construct points given its coordinates."""
    return Points(coordinates, server)


def create_line_from_points(points, num_points=100, server=None):
    """Construct line from two DPF points."""
    return Line(points, num_points, server)


def create_line_from_vector(ini, end=None, num_points=100, server=None):
    """Construct line from origin's coordinates and a vector direction."""
    # Input check
    if isinstance(ini[0], list):
        if not len(ini) == 2:
            raise ValueError("Exactly two points must be passed to define the vector")
        if not len(ini[0]) == len(ini[1]) == 3:
            raise ValueError(
                "Each point must contain three coordinates 'x', 'y' and 'z'."
            )
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

    return Line(vect, num_points, server)


def create_plane_from_center_and_normal(center, normal, server=None):
    return Plane(center, normal, server)


def create_plane_from_points(points, server=None):
    """Create plane from three points."""
    # Input check
    if isinstance(points, Points):
        if not len(points) == 3:
            raise ValueError(
                "Exactly three points must be passed to construct a plane from points."
            )
    else:
        if not len(points) == 3:
            raise ValueError(
                "Exactly three coordinates must be provided to create a plane."
            )
        if not len(points[0]) == len(points[1]) == len(points[2]) == 3:
            raise ValueError("Each point must contain three coordinates.")

    # Get center and normal from points
    center = get_center_from_coords(points)
    normal_dir = get_normal_direction_from_coords(points)
    return Plane(center, normal_dir, server)


def create_plane_from_lines(line1, line2, server=None):
    """Create plane from two lines."""
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
    return Plane(center, normal, server)


def create_plane_from_point_and_line(point, line, server=None):
    """Create plane from point and line."""
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
            raise ValueError(
                "Each point in line must contain three coordinates 'x', 'y' and 'z'."
            )

    # Get center and normal from point and vector
    coords = [line[0], line[1], point]
    vects = [line, [line[0], point]]
    center = get_center_from_coords(coords)
    normal = get_cross_product(vects)
    return Plane(center, normal, server)


def get_center_from_coords(coords):
    """Get average coordinates from several points."""
    n_points = len(coords)
    n_coords = len(coords[0])
    return [
        sum(coords[i][j] for i in range(n_points)) / n_points for j in range(n_coords)
    ]


def get_normal_direction_from_coords(points):
    """Get normal direction between three points."""
    vects = [
        [points[1][i] - points[0][i] for i in range(len(points))],
        [points[2][i] - points[0][i] for i in range(len(points))],
    ]
    return get_cross_product(vects)


def get_cross_product(vects):
    """Compute cross product between two vectors."""
    return np.cross(vects[0], vects[1])
