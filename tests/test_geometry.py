# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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

import numpy as np
import pytest

from ansys.dpf.core.geometry import (
    Line,
    Plane,
    Points,
    get_global_coords_from_local,
    get_local_coords_from_global,
    get_plane_local_axis,
    normalize_vector,
)
from ansys.dpf.core.geometry_factory import (
    create_line_from_points,
    create_line_from_vector,
    create_plane_from_center_and_normal,
    create_plane_from_lines,
    create_plane_from_point_and_line,
    create_plane_from_points,
    create_points,
    get_center_from_coords,
)


def test_create_points():
    n_points = 1000
    rng = np.random.default_rng()
    points = rng.random((n_points, 3))
    points = create_points(points)
    points.plot()
    # print(points)
    assert points.dimension == 3
    assert len(points) == points.n_points == n_points


points_data = [
    ([[0.4, 0.1, 0.0], [0.1, 0.0, 0.5]]),
    ([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]]),
    lambda: (Points([[0.4, 0.1, 0], [0.1, 0.0, 0.5]])),
    pytest.param(
        [[0.4, 0.1, 0.0], [0.1, 0, 0.5], [0.1, 0.0, 0.5]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [[0.4, 0.1, 0.0], [0.1, 0.0, 0.5, 0.0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
]


@pytest.mark.parametrize("points_param", points_data)
def test_create_line_from_points(points_param):
    points = points_param() if callable(points_param) else points_param
    line = create_line_from_points(points)
    line.plot()
    info = "DPF Line object:\n"
    info += f"Starting point: {np.array(points[0])}\n"
    info += f"Ending point: {np.array(points[1])}\n"
    info += f"Line discretized with {line.n_points} points\n"
    assert str(line) == str(info)
    assert line.length == np.linalg.norm(points)
    diff = np.array(points[1]) - np.array(points[0])
    assert all(line.direction) == all(diff / np.linalg.norm(diff))
    assert (line.path == np.linspace(0, line.length, line.n_points)).all()


vects_data = [
    ([[0.4, 0.1, 0.0], [0.1, 0.0, 0.5]], None),
    ([0.4, 0.1, 0.0], [0.1, 0.0, 0.5]),
    pytest.param(
        [[0.4, 0.1, 0.0], [0.1, 0.0, 0.5, 0.0], [0.0, 0.0, 0.0]],
        None,
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [[0.4, 0.1, 0.0], [0.1, 0.0, 0.5, 0.0, 0.0]],
        None,
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [0.4, 0.1, 0.0, 0.0],
        [0.1, 0.0, 0.5],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [0.4, 0.1, 0.0],
        [0.1, 0.0, 0.5, 0.0],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
]


@pytest.mark.parametrize(("ini", "end"), vects_data)
def test_create_line_from_vectors(ini, end):
    line = create_line_from_vector(ini, end)
    line.plot()


planes_data = [
    ([0.0, 0.0, 0.0], [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]], 1, 1, 20, 20),
    ([0.0, 0.0, 0.0], [0.0, 0.0, 1.0], 1, 1, 20, 20),
    ([1.0, 1.0, 1.0], [1.0, -1.0, 0.0], 1, 1, 20, 20),
    ([0.0, 0.0, 0.0], lambda: Line([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]]), 1, 1, 20, 20),
    pytest.param(
        [0.0, 0.0],
        [0.0, 0.0, 1.0],
        1,
        1,
        20,
        20,
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [0.0, 0.0, 0.0],
        [[0.0, 0.0], [0.0, 0.0, 1.0]],
        1,
        1,
        20,
        20,
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [0.0, 0.0, 0.0],
        [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
        1,
        1.5,
        5.5,
        5.5,
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [0.0, 0.0, 0.0],
        [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
        "testing",
        1.5,
        20,
        20,
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
]


@pytest.mark.parametrize(
    ("center", "normal_arg", "width", "height", "n_cells_x", "n_cells_y"), planes_data
)
def test_create_plane_from_center_and_normal(
    center, normal_arg, width, height, n_cells_x, n_cells_y
):
    normal = normal_arg() if callable(normal_arg) else normal_arg
    plane = create_plane_from_center_and_normal(center, normal, width, height, n_cells_x, n_cells_y)
    plane.plot()
    assert plane.center == center
    if len(normal) == 2:
        normal_vect = normalize_vector(np.array(normal))
        diff = np.array(normal[1]) - np.array(normal[0])
        normal_dir = normalize_vector(diff)
    else:
        normal_vect = [np.array([0.0, 0.0, 0.0]), normalize_vector(np.array(normal))]
        normal_dir = normalize_vector(np.array(normal))
    assert (plane.normal_vect[0] == normal_vect[0]).all()
    assert (plane.normal_vect[1] == normal_vect[1]).all()
    assert (plane.normal_dir == normal_dir).all()


plane_data = [
    ([[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]),
    lambda: (Points([[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]])),
    pytest.param(
        [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]], marks=pytest.mark.xfail(strict=True, raises=ValueError)
    ),
    pytest.param(
        lambda: Points([[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]]),
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [[0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
]


@pytest.mark.parametrize(("points"), plane_data)
def test_create_plane_from_points(points):
    plane = create_plane_from_points(points() if callable(points) else points)
    plane.plot()


plane_lines_data = [
    ([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]], [[2.0, 1.0, 0.0], [0.0, 1.0, 0.0]]),
    (
        lambda: Line([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]]),
        lambda: Line([[2.0, 1.0, 0.0], [0.0, 1.0, 0.0]]),
    ),
    pytest.param(
        [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 1.0, 0.0]],
        [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
        [[0.0, 0.0, 0.0], [0.0, 0.0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
]


@pytest.mark.parametrize(("line1", "line2"), plane_lines_data)
def test_create_plane_from_lines(line1, line2):
    plane = create_plane_from_lines(
        line1() if callable(line1) else line1, line2() if callable(line2) else line2
    )
    plane.plot()


plane_point_line_data = [
    ([0.0, 0.0, 0.0], [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]]),
    (lambda: Points([0.0, 0.0, 0.0]), [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]]),
    ([0.0, 0.0, 0.0], lambda: Line([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])),
    pytest.param(
        lambda: Points([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]]),
        [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [0.0, 0.0, 0.0, 0.0],
        [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [0.0, 0.0, 0.0],
        [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
    pytest.param(
        [0.0, 0.0, 0.0],
        [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
        marks=pytest.mark.xfail(strict=True, raises=ValueError),
    ),
]


@pytest.mark.parametrize(("point", "line"), plane_point_line_data)
def test_create_plane_from_point_and_line(point, line):
    plane = create_plane_from_point_and_line(
        point() if callable(point) else point, line() if callable(line) else line
    )
    plane.plot()


coords_data = [
    ([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]], [1.0 / 3.0, 0.0, 1.0 / 3.0]),
    ([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]], [1.0 / 3.0, 1.0 / 3.0]),
]


@pytest.mark.parametrize(("coords", "expected"), coords_data)
def test_get_center_from_coords(coords, expected):
    center = get_center_from_coords(coords)
    assert center == expected


def test_line_discretization():
    line = Line([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]])
    assert line.mesh.nodes.n_nodes == 100
    assert line.mesh.elements.n_elements == 99

    line = Line([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]], n_points=1200)
    assert line.mesh.nodes.n_nodes == 1200
    assert line.mesh.elements.n_elements == 1199


plane_discretization_data = [0, 1, 2]


@pytest.mark.parametrize(("component"), plane_discretization_data)
def test_plane_discretization(component):
    normal = np.zeros(3)
    center = np.zeros(3)
    normal[component] = 1
    width = height = 1
    n_cells_x = n_cells_y = 30
    plane = create_plane_from_center_and_normal(
        center=center,
        normal=normal,
        width=width,
        height=height,
        n_cells_x=n_cells_x,
        n_cells_y=n_cells_y,
    )
    assert plane.mesh.elements.n_elements == 30 * 30
    assert all(plane.mesh.nodes.coordinates_field.data[:, component] == 0.0)
    info_discretization = "DPF Plane object:\n"
    info_discretization += f"Center point: {center}\n"
    info_discretization += f"Normal direction: {normal}\n"
    info_discretization += "Plane discretizaton using:\n"
    info_discretization += f"  Width (x-dir): {width}\n"
    info_discretization += f"  Height (y-dir): {height}\n"
    info_discretization += f"  Num cells x-dir: {n_cells_x}\n"
    info_discretization += f"  Num cells y-dir: {n_cells_y}\n"
    assert str(plane) == str(info_discretization)


plane_mapping_data = [
    ([0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [[1.0, 0.0, 1.0], [0.5, 0.0, 0.5], [2.0, 0.0, 1.0]]),
    ([0.2, -0.6, 2.0], [0.0, 1.0, 0.0], [[1.0, 0.0, 1.0], [0.5, 0.0, 0.5], [2.0, 0.0, 1.0]]),
    ([0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [[1.0, 1.0, 0.0], [2.0, 1.0, 0.0], [-2.0, -1.0, 0.0]]),
    ([0.3, 0.5, -1.0], [1.0, 0.0, 0.0], [[0.0, 1.0, 1.0], [0.0, -1.0, 1.0], [0.0, 4.0, -2.0]]),
]


@pytest.mark.parametrize(("center", "normal", "global_ref"), plane_mapping_data)
def test_plane_axes_and_coords_mapping(center, normal, global_ref):
    normal = normalize_vector(np.array(normal))
    axes_plane = get_plane_local_axis(normal)
    for i in range(len(global_ref)):
        local = get_local_coords_from_global(global_ref[i], axes_plane, center)
        assert np.isclose(local[2], -center[np.where(normal == 1.0)[0][0]])
        glob = get_global_coords_from_local(local, axes_plane, center)
        assert np.isclose(glob, global_ref[i]).all()


def test_plotting_with_mesh():
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples

    model = dpf.Model(examples.find_static_rst())
    mesh = model.metadata.meshed_region

    points = Points([[0.03, 0.06, 0.03], [0.03, 0.03, 0.0], [0.0, 0.0, 0.0]])
    points.plot(mesh)

    line = Line([[0.03, 0.03, 0.05], [0.0, 0.06, 0.0]])
    line.plot(mesh)

    plane = Plane([0.015, 0.045, 0.015], [1.0, 1.0, 0.0])
    plane.plot(mesh)
