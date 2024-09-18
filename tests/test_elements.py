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

import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core.elements import element_types


@pytest.fixture()
def model_elements(allkindofcomplexity):
    model = dpf.Model(allkindofcomplexity)
    elements = model.metadata.meshed_region.elements
    return elements


@pytest.fixture()
def hexa_element_descriptor(model_elements):
    el_index = model_elements.scoping.index(251)
    descriptor = dpf.element_types.descriptor(model_elements[el_index].type)
    return descriptor


@pytest.fixture()
def quad_element_descriptor(model_elements):
    el_index = model_elements.scoping.index(10660)
    return dpf.element_types.descriptor(model_elements[el_index].type)


@pytest.fixture()
def tetra_element_descriptor(model_elements):
    el_index = model_elements.scoping.index(3905)
    return dpf.element_types.descriptor(model_elements[el_index].type)


@pytest.fixture()
def line_element_descriptor(model_elements):
    el_index = model_elements.scoping.index(10834)
    return dpf.element_types.descriptor(model_elements[el_index].type)


def check_element_attributes(
    descriptor,
    enum_id,
    description,
    name,
    shape,
    n_corner_nodes,
    n_mid_nodes,
    n_nodes,
    is_solid,
    is_shell,
    is_beam,
    is_quadratic,
):
    assert isinstance(descriptor, dpf.ElementDescriptor)
    assert descriptor.enum_id.value == enum_id
    assert descriptor.description == description
    assert descriptor.name == name
    assert descriptor.shape == shape
    assert descriptor.n_corner_nodes == n_corner_nodes
    assert descriptor.n_mid_nodes == n_mid_nodes
    assert descriptor.n_nodes == n_nodes
    assert descriptor.is_solid == is_solid
    assert descriptor.is_shell == is_shell
    assert descriptor.is_beam == is_beam
    assert descriptor.is_quadratic == is_quadratic


def test_hexa_element_descriptor(hexa_element_descriptor):
    check_element_attributes(
        hexa_element_descriptor,
        1,
        "Quadratic 20-nodes Hexa",
        "hex20",
        "solid",
        8,
        12,
        20,
        True,
        False,
        False,
        True,
    )


def test_quad_element_descriptor(quad_element_descriptor):
    check_element_attributes(
        quad_element_descriptor,
        16,
        "Linear 4-nodes Quadrangle",
        "quad4",
        "shell",
        4,
        0,
        4,
        False,
        True,
        False,
        False,
    )


def test_tetra_element_descriptor(tetra_element_descriptor):
    check_element_attributes(
        tetra_element_descriptor,
        0,
        "Quadratic 10-nodes Tetrahedron",
        "tet10",
        "solid",
        4,
        6,
        10,
        True,
        False,
        False,
        True,
    )


def test_line_element_descriptor(line_element_descriptor):
    check_element_attributes(
        line_element_descriptor,
        18,
        "Linear 2-nodes Line",
        "line2",
        "beam",
        2,
        0,
        2,
        False,
        False,
        True,
        False,
    )


def test_no_element_descriptor():
    # descriptor = dpf.element_types.descriptor(89)
    # assert not descriptor
    descriptor = dpf.element_types.descriptor(dpf.element_types.General)
    # print(descriptor)
    unknown_shape = "unknown_shape"
    assert descriptor.shape == unknown_shape
    assert dpf.element_types.descriptor(dpf.element_types.General).shape == unknown_shape


def test_descriptor_with_int_value():
    # int as attribute instead of element_types.VALUE
    descriptor = dpf.element_types.descriptor(1)
    check_element_attributes(
        descriptor,
        1,
        "Quadratic 20-nodes Hexa",
        "hex20",
        "solid",
        8,
        12,
        20,
        True,
        False,
        False,
        True,
    )


def check_from_enum_id(
    hardcoded_id,
    enum_id,
    description,
    name,
    shape,
    n_corner_nodes,
    n_mid_nodes,
    n_nodes,
    is_solid,
    is_shell,
    is_beam,
    is_quadratic,
):
    des = dpf.element_types.descriptor(enum_id)
    assert hardcoded_id == enum_id.value
    check_element_attributes(
        des,
        enum_id.value,
        description,
        name,
        shape,
        n_corner_nodes,
        n_mid_nodes,
        n_nodes,
        is_solid,
        is_shell,
        is_beam,
        is_quadratic,
    )


# test all element's types
def test_general():
    check_from_enum_id(
        -2,
        element_types.General,
        "General",
        "general",
        "unknown_shape",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_all():
    check_from_enum_id(
        -1,
        element_types.All,
        "Unknown",
        "unknown",
        "unknown_shape",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_tet10():
    check_from_enum_id(
        0,
        element_types.Tet10,
        "Quadratic 10-nodes Tetrahedron",
        "tet10",
        "solid",
        4,
        6,
        10,
        True,
        False,
        False,
        True,
    )


def test_hex20():
    check_from_enum_id(
        1,
        element_types.Hex20,
        "Quadratic 20-nodes Hexa",
        "hex20",
        "solid",
        8,
        12,
        20,
        True,
        False,
        False,
        True,
    )


def test_wedge15():
    check_from_enum_id(
        2,
        element_types.Wedge15,
        "Quadratic 15-nodes Wedge",
        "wedge15",
        "solid",
        6,
        9,
        15,
        True,
        False,
        False,
        True,
    )


def test_pyramid13():
    check_from_enum_id(
        3,
        element_types.Pyramid13,
        "Quadratic 13-nodes Pyramid",
        "pyramid13",
        "solid",
        5,
        8,
        13,
        True,
        False,
        False,
        True,
    )


def test_tri6():
    check_from_enum_id(
        4,
        element_types.Tri6,
        "Quadratic 6-nodes Triangle",
        "tri6",
        "shell",
        3,
        3,
        6,
        False,
        True,
        False,
        True,
    )


def test_triShell6():
    check_from_enum_id(
        5,
        element_types.TriShell6,
        "Quadratic 6-nodes Triangle Shell",
        "triShell6",
        "shell",
        3,
        3,
        6,
        False,
        True,
        False,
        True,
    )


def test_quad8():
    check_from_enum_id(
        6,
        element_types.Quad8,
        "Quadratic 8-nodes Quadrangle",
        "quad8",
        "shell",
        4,
        4,
        8,
        False,
        True,
        False,
        True,
    )


def test_quadShell8():
    check_from_enum_id(
        7,
        element_types.QuadShell8,
        "Quadratic 8-nodes Quadrangle Shell",
        "quadShell8",
        "shell",
        4,
        4,
        8,
        False,
        True,
        False,
        True,
    )


def test_line3():
    check_from_enum_id(
        8,
        element_types.Line3,
        "Quadratic 3-nodes Line",
        "line3",
        "beam",
        2,
        1,
        3,
        False,
        False,
        True,
        True,
    )


def test_point1():
    check_from_enum_id(
        9,
        element_types.Point1,
        "Point",
        "point1",
        "point",
        1,
        0,
        1,
        False,
        False,
        False,
        False,
    )


def test_tet4():
    check_from_enum_id(
        10,
        element_types.Tet4,
        "Linear 4-nodes Tetrahedron",
        "tet4",
        "solid",
        4,
        0,
        4,
        True,
        False,
        False,
        False,
    )


def test_hex8():
    check_from_enum_id(
        11,
        element_types.Hex8,
        "Linear 8-nodes Hexa",
        "hex8",
        "solid",
        8,
        0,
        8,
        True,
        False,
        False,
        False,
    )


def test_wedge6():
    check_from_enum_id(
        12,
        element_types.Wedge6,
        "Linear 6-nodes Wedge",
        "wedge6",
        "solid",
        6,
        0,
        6,
        True,
        False,
        False,
        False,
    )


def test_pyramid5():
    check_from_enum_id(
        13,
        element_types.Pyramid5,
        "Linear 5-nodes Pyramid",
        "pyramid5",
        "solid",
        5,
        0,
        5,
        True,
        False,
        False,
        False,
    )


def test_tri3():
    check_from_enum_id(
        14,
        element_types.Tri3,
        "Linear 3-nodes Triangle",
        "tri3",
        "shell",
        3,
        0,
        3,
        False,
        True,
        False,
        False,
    )


def test_triShell3():
    check_from_enum_id(
        15,
        element_types.TriShell3,
        "Linear 3-nodes Triangle Shell",
        "triShell3",
        "shell",
        3,
        0,
        3,
        False,
        True,
        False,
        False,
    )


def test_quad4():
    check_from_enum_id(
        16,
        element_types.Quad4,
        "Linear 4-nodes Quadrangle",
        "quad4",
        "shell",
        4,
        0,
        4,
        False,
        True,
        False,
        False,
    )


def test_quadShell4():
    check_from_enum_id(
        17,
        element_types.QuadShell4,
        "Linear 4-nodes Quadrangle Shell",
        "quadShell4",
        "shell",
        4,
        0,
        4,
        False,
        True,
        False,
        False,
    )


def test_line2():
    check_from_enum_id(
        18,
        element_types.Line2,
        "Linear 2-nodes Line",
        "line2",
        "beam",
        2,
        0,
        2,
        False,
        False,
        True,
        False,
    )


def test_numElementTypes():
    check_from_enum_id(
        19,
        element_types.NumElementTypes,
        "NumElementTypes",
        "numElementTypes",
        "unknown_shape",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_unknown():
    check_from_enum_id(
        20,
        element_types.Unknown,
        "Unknown",
        "unknown",
        "unknown_shape",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_eMagLine():
    check_from_enum_id(
        21,
        element_types.EMagLine,
        "EMagLine",
        "EMagLine",
        "beam",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_eMagArc():
    check_from_enum_id(
        22,
        element_types.EMagArc,
        "EMagArc",
        "EMagArc",
        "beam",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_eMagCircle():
    check_from_enum_id(
        23,
        element_types.EMagCircle,
        "EMagCircle",
        "EMagCircle",
        "shell",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_surface3():
    check_from_enum_id(
        24,
        element_types.Surface3,
        "Surface3",
        "surface3",
        "shell",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_surface4():
    check_from_enum_id(
        25,
        element_types.Surface4,
        "Surface4",
        "surface4",
        "shell",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_surface6():
    check_from_enum_id(
        26,
        element_types.Surface6,
        "Surface6",
        "surface6",
        "shell",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_surface8():
    check_from_enum_id(
        27,
        element_types.Surface8,
        "Surface8",
        "surface8",
        "shell",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_edge2():
    check_from_enum_id(
        28,
        element_types.Edge2,
        "Edge2",
        "edge2",
        "beam",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_edge3():
    check_from_enum_id(
        29,
        element_types.Edge3,
        "Edge3",
        "edge3",
        "beam",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_beam3():
    check_from_enum_id(
        30,
        element_types.Beam3,
        "Beam3",
        "beam3",
        "beam",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_beam4():
    check_from_enum_id(
        31,
        element_types.Beam4,
        "Beam4",
        "beam4",
        "beam",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_polygon():
    check_from_enum_id(
        33,
        element_types.Polygon,
        "Polygon",
        "polygon",
        "shell",
        -1,
        0,
        -1,
        False,
        True,
        False,
        None,
    )


def test_polyhedron():
    check_from_enum_id(
        34,
        element_types.Polyhedron,
        "Polyhedron",
        "polyhedron",
        "solid",
        -1,
        0,
        -1,
        True,
        False,
        False,
        None,
    )
