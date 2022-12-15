import numpy as np
import pytest

from ansys.dpf.core.geometry import Points, Line
from ansys.dpf.core.geometry_factory import (
    create_points,
    create_line_from_points,
    create_line_from_vector,
    create_plane_from_center_and_normal,
    create_plane_from_points,
    create_plane_from_lines,
    create_plane_from_point_and_line,
    get_center_from_coords,
)


def test_create_points():
    num_points = 1000
    rng = np.random.default_rng()
    points = rng.random((num_points, 3))
    points = create_points(points)
    points.plot()
    print(points)
    assert points.dimension == 3
    assert len(points) == points.num_points == num_points


points_data = [
    ([[0.4, 0.1, 0], [0.1, 0, 0.5]]),
    (Points([[0.4, 0.1, 0], [0.1, 0, 0.5]])),
    pytest.param(
        [[0.4, 0.1, 0], [0.1, 0, 0.5], [0.1, 0, 0.5]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [[0.4, 0.1, 0], [0.1, 0, 0.5, 0]],
        marks=pytest.mark.xfail(strict=True, raises=TypeError),
    ),
]


@pytest.mark.parametrize("points", points_data)
def test_create_line_from_points(points):
    line = create_line_from_points(points)
    line.plot()
    info = "DPF Line object:\n"
    info += f"Starting point: {np.array(points[0])}\n"
    info += f"Ending point: {np.array(points[1])}\n"
    info += f"Line discretized with {line._num_points} points\n"
    assert print(line) == print(info)
    assert line.length == np.linalg.norm(points)
    diff = np.array(points[1]) - np.array(points[0])
    assert all(line.direction) == all(diff / np.linalg.norm(diff))


vects_data = [
    ([[0.4, 0.1, 0], [0.1, 0, 0.5]], None),
    ([0.4, 0.1, 0], [0.1, 0, 0.5]),
    pytest.param(
        [[0.4, 0.1, 0], [0.1, 0, 0.5, 0], [0, 0, 0]],
        None,
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [[0.4, 0.1, 0], [0.1, 0, 0.5, 0, 0]],
        None,
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [0.4, 0.1, 0, 0],
        [0.1, 0, 0.5],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [0.4, 0.1, 0],
        [0.1, 0, 0.5, 0],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
]


@pytest.mark.parametrize(("ini", "end"), vects_data)
def test_create_line_from_vectors(ini, end):
    line = create_line_from_vector(ini, end)
    line.plot()


planes_data = [
    ([0, 0, 0], [[0, 0, 0], [0, 0, 1]]),
    ([0, 0, 0], [0, 0, 1]),
    ([0, 0, 0], Line([[0, 0, 0], [0, 0, 1]])),
    pytest.param(
        [0, 0], [0, 0, 1], marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
    pytest.param(
        [0, 0, 0],
        [[0, 0], [0, 0, 1]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
]


@pytest.mark.parametrize(("center", "normal"), planes_data)
def test_create_plane_from_center_and_normal(center, normal):
    plane = create_plane_from_center_and_normal(center, normal)
    plane.plot()
    assert plane.center == center
    if len(normal) == 2:
        normal_vect = np.array(normal)
        diff = np.array(normal[1]) - np.array(normal[0])
        normal_dir = diff / np.linalg.norm(diff)
    else:
        normal_vect = [np.array([0, 0, 0]), np.array(normal)]
        normal_dir = np.array(normal)
    assert [(plane.normal_vect[i] == normal_vect[i]).all() for i in range(2)]
    assert (plane.normal_dir == normal_dir).all()


plane_data = [
    ([[0, 0, 0], [0, 1, 0], [1, 0, 0]]),
    (Points([[0, 0, 0], [0, 1, 0], [1, 0, 0]])),
    pytest.param(
        [[0, 0, 0], [0, 1, 0]], marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
    pytest.param(
        [[0, 0], [0, 1, 0], [0, 0, 1]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
]


@pytest.mark.parametrize(("points"), plane_data)
def test_create_plane_from_points(points):
    plane = create_plane_from_points(points)
    plane.plot()


plane_lines_data = [
    ([[0, 0, 0], [1, 0, 0]], [[2, 1, 0], [0, 1, 0]]),
    (Line([[0, 0, 0], [1, 0, 0]]), Line([[2, 1, 0], [0, 1, 0]])),
    pytest.param(
        [[0, 0, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 0, 0], [0, 0, 1]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [[0, 0, 0], [0, 1, 0]],
        [[0, 0, 0], [0, 0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
]


@pytest.mark.parametrize(("line1", "line2"), plane_lines_data)
def test_create_plane_from_lines(line1, line2):
    plane = create_plane_from_lines(line1, line2)
    plane.plot()


plane_point_line_data = [
    ([0, 0, 0], [[0, 0, 0], [0, 0, 1]]),
    (Points([0, 0, 0]), [[0, 0, 0], [0, 0, 1]]),
    ([0, 0, 0], Line([[0, 0, 0], [0, 0, 1]])),
]


@pytest.mark.parametrize(("point", "line"), plane_point_line_data)
def test_create_plane_from_point_and_line(point, line):
    plane = create_plane_from_point_and_line(point, line)
    plane.plot()


coords_data = [
    ([[0, 0, 0], [0, 0, 1], [1, 0, 0]], [1 / 3, 0, 1 / 3]),
    ([[0, 0], [1, 0], [0, 1]], [1 / 3, 1 / 3]),
]


@pytest.mark.parametrize(("coords", "expected"), coords_data)
def test_get_center_from_coords(coords, expected):
    center = get_center_from_coords(coords)
    assert center == expected


def test_line_discretization():
    line = Line([[0, 0, 0], [1, 1, 1]])
    assert line.mesh.nodes.n_nodes == 100
    assert line.mesh.elements.n_elements == 99

    line = Line([[0, 0, 0], [1, 1, 1]], num_points=1200)
    assert line.mesh.nodes.n_nodes == 1200
    assert line.mesh.elements.n_elements == 1199


plane_discretization_data = [0, 1, 2]


@pytest.mark.parametrize(("component"), plane_discretization_data)
def test_plane_discretization(component):
    normal = np.zeros(3)
    center = np.zeros(3)
    normal[component] = 1
    plane = create_plane_from_center_and_normal(center, normal)
    info_no_discretization = "DPF Plane object:\n"
    info_no_discretization += f"Center point: {center}\n"
    info_no_discretization += f"Normal direction: {normal}\n"
    info_no_discretization += "Plane has not been discretized.\n"
    info_no_discretization += (
        "  Use plane.discretize(width, height, num_cells_x, num_cells_y)\n"
    )
    assert print(plane) == print(info_no_discretization)
    width = height = 1
    num_cells_x = num_cells_y = 30
    plane.discretize(
        width=width, height=height, num_cells_x=num_cells_x, num_cells_y=num_cells_y
    )
    assert plane.mesh.elements.n_elements == 30 * 30
    assert all(plane.mesh.nodes.coordinates_field.data[:, component] == 0.0)
    info_discretization = "DPF Plane object:\n"
    info_discretization += f"Center point: {center}\n"
    info_discretization += f"Normal direction: {normal}\n"
    info_discretization += "Plane discretizaton using:\n"
    info_discretization += f"  Width (x-dir): {width}\n"
    info_discretization += f"  Height (y-dir): {height}\n"
    info_discretization += f"  Num cells x-dir: {num_cells_x}\n"
    info_discretization += f"  Num cells y-dir: {num_cells_y}\n"
    assert print(plane) == print(info_discretization)
