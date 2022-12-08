import numpy as np
import pytest

from ansys.dpf.core.geometry import Points, Line
from ansys.dpf.core.geometry_factory import (
    create_points,
    create_line_from_points,
    create_line_from_vector,
    create_plane_from_center_and_normal,
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
def test_create_lines_from_points(points):
    line = create_line_from_points(points)
    line.plot()

vects_data = [
    ([[0.4, 0.1, 0], [0.1, 0, 0.5]], None),
    ([0.4, 0.1, 0], [0.1, 0, 0.5]),
]
@pytest.mark.parametrize(("ini", "end"), vects_data)
def test_create_lines_from_vectors(ini, end):
    line = create_line_from_vector(ini, end)
    line.plot()

def test_create_plane_from_center_and_normal():
    center = [0, 0, 0]
    normal = Line([[0, 0, 0], [0, 0, 1]])
    create_plane_from_center_and_normal(center, normal)