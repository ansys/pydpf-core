import numpy as np

from ansys.dpf.core.geometry import Points, Line, Plane

def create_points(coordinates, server=None):
    """Construct points given its coordinates."""
    return Points(coordinates, server)

def create_line_from_points(points, server=None):
    """Construct line from two DPF points."""
    # Input check
    if isinstance(points, Points):
        if not points.num_points == 2:
            raise ValueError("Only two points must be used to define a line")
        points = points.coordinates.data
    return Line(points, server)

def create_line_from_vector(ini, end=None, server=None):
    """Construct line from origin's coordinates and a vector direction."""
    # Input check
    if isinstance(ini[0], list):
        if not len(ini) == 2:
            raise ValueError("Exactly two points must be passed to define the vector")
        if not len(ini[0]) == len(ini[1]) == 3:
            raise ValueError("Each point must contain three coordinates 'x', 'y' and 'z'.")
        vect = ini
    else:
        if not len(ini) == 3:
            raise ValueError("'ini' argument must be of length = 3 \
            representing the 3D coordinates of the origin of the vector.")
        if not len(end) == 3:
            raise ValueError("'end' argument must be of length = 3 \
            representing the 3D coordinates of the end point of the vector.")
        vect = [ini, end]
    return Line(vect, server)

def create_plane_from_center_and_normal(center, normal, server=None):
    return Plane(center, normal, server)

def create_plane_from_points(points, server=None):
    """Create plane from three points."""
    # Input check
    if isinstance(points, Points):
        if not len(points) == 3:
            raise ValueError("Exactly three points must be passed to construct a plane from points.")
    else:
        if not len(points) == 3:
            raise ValueError("Exactly three coordinates must be provided to create a plane.")
        if not len(points[0]) == len(points[1]) == len(points[2]) == 3:
            raise ValueError("Each point must contain three coordinates.")

    # Get center and normal from points
    center = get_center_from_coords(points)
    normal_dir = get_normal_direction_from_coords(points)
    return Plane(center, normal_dir, server)

def create_plane_from_lines(line1, line2, server=None):
    """Create plane from two lines."""
    # Input check
    if not isinstance(line1, Line) == isinstance(line2, Line):
        if not len(line1) == len(line2) == 2:
            raise ValueError("Each line must contain two points.")
        if not len(line1[0]) == len(line1[1]) == len(line2[0]) == len(line2[1]) == 3:
            raise ValueError("Each point must contain three coordinates.")

    # Get center and normal from points
    vect1 = [x-y for x,y in zip(line1[0], line1[1])]
    vect2 = [x-y for x,y in zip(line2[0], line2[1])]
    center = get_center_from_coords([vect1, vect2])
    normal = get_cross_product([vect1, vect2])

    return Plane(center, normal, server)

def create_plane_from_point_and_line(point, vector, server=None):
    """Create plane from point and line"""
    # Input check
    if isinstance(point, Points):
        if not len(point) == 1:
            raise ValueError("Only one point must be passed.")
    else:
        if not len(point) == 3:
            raise ValueError("A point must contain 3 coordinates 'x', 'y' and 'z'.")
    if not len(vector) == 3:
        raise ValueError("'vector' must contain 3 coordinates.")

    # Get center and normal from point and vector
    vects = [point, vector]
    center = get_center_from_coords(vects)
    normal = get_cross_product(vects)

    return Plane(center, normal, server)

def get_center_from_coords(coords):
    n_points = len(coords)
    n_coords = len(coords[0])
    return [sum(coords[i][j] for i in range(n_points))/n_points for j in range(n_coords)]

def get_normal_direction_from_coords(coords):
    vects = [
        [coords[1][i]-coords[0][i] for i in range(len(coords))],
        [coords[2][i]-coords[0][i] for i in range(len(coords))],
    ]
    return get_cross_product(vects)

def get_cross_product(vects):
    return np.cross(vects[0], vects[1])


if __name__ == "__main__":
    ######################### CREATE POINTS ####################################
    points = create_points([[0.3, 0.2, 0.5], [1, 1, 1]])
    # points.plot()

    ######################### CREATE LINES #####################################
    line_from_coords = create_line_from_points([[0.3, 0.2, 0.5], [1, 1, 1]])
    # line_from_coords.plot()
    line_from_points = create_line_from_points(points)
    # line_from_points.plot()
    line_from_origin_and_dir = create_line_from_vector(
        ini = [0.3, 0.2, 0.5],
        end = [0.7, 0.8, 0.5]
    )
    # line_from_origin_and_dir.plot()
    line_from_origin_and_dir = create_line_from_vector([[0.3, 0.2, 0.5], [0.7, 0.8, 0.5]])
    # line_from_origin_and_dir.plot()

    ######################### CREATE PLANES #####################################
    plane_from_center_and_normal = create_plane_from_center_and_normal(
        center = [0, 0, 0],
        normal = [[0, 0, 0], [0, 0, 1]],
    )
    # plane_from_center_and_normal.plot()
    plane_from_center_and_normal = create_plane_from_center_and_normal(
        center = [0, 0, 0],
        normal = Line([[0, 0, 0], [0, 0, 1]]),
    )
    # plane_from_center_and_normal.plot()
    plane_from_coords = create_plane_from_points(
        [[0, 0, 0],
        [0, 1, 0],
        [1, 0, 0]]
    )
    # plane_from_coords.plot()

    points = create_points([[0, 0, 0],[0, 1, 0], [1, 0, 0]])
    plane_from_coords = create_plane_from_points(points)
    # plane_from_coords.plot()

    line1 = [[0, 0, 0], [1, 0, 0]]
    line2 = [[2, 1, 0], [0, 1, 0]]
    plane_from_vects = create_plane_from_lines(line1, line2)
    plane_from_vects.plot()

    plane_from_vects = create_plane_from_lines(Line(line1), Line(line2))
    plane_from_vects.plot()

