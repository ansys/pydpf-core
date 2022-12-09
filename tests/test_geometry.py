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
    assert len(points) == points.num_points == num_points

points_data = [
    ([[0.4, 0.1, 0], [0.1, 0, 0.5]]),
    (Points([[0.4, 0.1, 0], [0.1, 0, 0.5]])),
    pytest.param(
        [[0.4, 0.1, 0], [0.1, 0, 0.5], [0.1, 0, 0.5]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
    pytest.param(
        [[0.4, 0.1, 0], [0.1, 0, 0.5, 0]],
        marks=pytest.mark.xfail(strict=True, raises=TypeError)
    ),
]
@pytest.mark.parametrize("points", points_data)
def test_create_line_from_points(points):
    line = create_line_from_points(points)
    line.plot()

vects_data = [
    ([[0.4, 0.1, 0], [0.1, 0, 0.5]], None),
    ([0.4, 0.1, 0], [0.1, 0, 0.5]),
    pytest.param(
        [[0.4, 0.1, 0], [0.1, 0, 0.5, 0], [0, 0, 0]],
        None,
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
    pytest.param(
        [[0.4, 0.1, 0], [0.1, 0, 0.5, 0, 0]],
        None,
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
    pytest.param(
        [0.4, 0.1, 0, 0],
        [0.1, 0, 0.5],
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
    pytest.param(
        [0.4, 0.1, 0],
        [0.1, 0, 0.5, 0],
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
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
        [0, 0],
        [0, 0, 1],
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
    pytest.param(
        [0, 0, 0],
        [[0, 0], [0, 0, 1]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
]
@pytest.mark.parametrize(("center", "normal"), planes_data)
def test_create_plane_from_center_and_normal(center, normal):
    plane = create_plane_from_center_and_normal(center, normal)
    plane.plot()

plane_data = [
    ([[0, 0, 0], [0, 1, 0],[1, 0, 0]]),
    (Points([[0, 0, 0], [0, 1, 0],[1, 0, 0]])),
    pytest.param(
        [[0, 0, 0], [0, 1, 0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
    pytest.param(
        [[0, 0], [0, 1, 0], [0, 0, 1]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
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
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
    pytest.param(
        [[0, 0, 0], [0, 1, 0]],
        [[0, 0, 0], [0, 0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError)
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
    ([[0, 0, 0], [0, 0, 1], [1, 0, 0]], [1/3, 0, 1/3]),
    ([[0, 0], [1, 0], [0, 1]], [1/3, 1/3]),
]
@pytest.mark.parametrize(("coords", "expected"), coords_data)
def test_get_center_from_coords(coords, expected):
    center = get_center_from_coords(coords)
    assert center == expected