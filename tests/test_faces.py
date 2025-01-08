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

import pytest
import conftest
from ansys.dpf import core as dpf
from ansys.dpf.core.elements import element_types
from ansys.dpf.core import mesh_scoping_factory


@pytest.fixture()
def model_faces(fluent_axial_comp):
    model = dpf.Model(fluent_axial_comp())
    faces = model.metadata.meshed_region.faces
    return faces


@pytest.fixture()
def mesh_wo_faces(simple_bar):
    model = dpf.Model(simple_bar)
    return model.metadata.meshed_region


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="mesh faces were not supported before 7.0",
)
def test_faces(model_faces):
    assert str(model_faces) == "DPF Faces object with 44242 faces"
    assert len(model_faces) == 44242
    assert model_faces.n_faces == 44242
    assert model_faces.scoping.location == dpf.locations.faces
    assert model_faces.scoping.size == 44242
    assert model_faces.faces_type_field.scoping.ids[45] == model_faces.scoping.ids[45]
    assert model_faces.faces_type_field.get_entity_data(789)[0] == model_faces[789].type.value
    for n in range(model_faces[2000].n_nodes):
        assert (
            model_faces.faces_nodes_connectivity_field.get_entity_data(2000)[n]
            == model_faces[2000].connectivity[n]
        )

    my_sco = mesh_scoping_factory.face_scoping([1100, 2400])
    ind, mask = model_faces.map_scoping(my_sco)

    assert ind[0] == 97
    assert mask[1] == True


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="mesh faces were not supported before 7.0",
)
def test_face(model_faces):
    face = model_faces.face_by_id(4500)
    ref_str = """DPF Face 4500
\tIndex:         3497
\tNodes:            4
\tType:       element_types.Quad4
"""
    assert str(face) == ref_str
    assert face.node_ids == [4688, 4679, 4663, 4677]
    assert face.id == 4500
    assert face.type == element_types.Quad4
    assert face.n_nodes == 4
    assert face.index == 3497
    assert len(face.nodes) == 4

    ref_node_str = """DPF Node        4677
Index:         4676
Location: [-0.022856459489947675, -0.08534214957826106, -0.013310679234564304]
"""

    assert str(face.nodes[3]) == ref_node_str


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="faces location was not supported before 7.0",
)
def test_face_scoping():
    faces_sco = mesh_scoping_factory.face_scoping([56, 78, 4])
    assert faces_sco.location == dpf.locations.faces
    assert faces_sco.size == 3
    assert faces_sco.ids[2] == 4


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="faces location was not supported before 7.0",
)
def test_mesh_without_faces(mesh_wo_faces):
    assert mesh_wo_faces.faces.n_faces == 0
    assert mesh_wo_faces.faces.scoping.size == 0
    assert mesh_wo_faces.faces.faces_type_field.size == 0
    assert mesh_wo_faces.faces.faces_nodes_connectivity_field.size == 0
    with pytest.raises(ValueError) as e:
        mesh_wo_faces.faces.face_by_id(1)
        assert "face not found" in e
    with pytest.raises(ValueError) as e:
        mesh_wo_faces.faces.face_by_index(1)
        assert "face not found" in e
