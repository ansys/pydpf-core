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

import ansys.dpf.core as dpf
import conftest


def test_operator_mesh_plan_clip_rst(simple_bar):
    model = dpf.Model(simple_bar)
    main_mesh = model.metadata.meshed_region

    plane = dpf.fields_factory.create_3d_vector_field(1, dpf.locations.overall)
    plane.append([0, 1, 0], 1)

    origin = dpf.fields_factory.create_3d_vector_field(1, dpf.locations.overall)
    origin.append([0, 2.0, 0], 1)

    cut_mesh = dpf.operators.mesh.mesh_plan_clip(main_mesh, normal=plane, origin=origin).eval(2)
    node_scoping_ids = cut_mesh.nodes.scoping.ids
    assert len(node_scoping_ids) == 1331
    assert node_scoping_ids[-1] == 1331
    elements_scoping_ids = cut_mesh.elements.scoping.ids
    assert len(elements_scoping_ids) == 6000
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_2:
        assert elements_scoping_ids[-1] == 6000

    # Check clipping a field
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_2:
        disp = model.results.displacement.eval()[0]
        op = dpf.operators.mesh.mesh_plan_clip()
        op.inputs.mesh_or_field.connect(disp)
        op.inputs.normal.connect(plane)
        op.inputs.origin.connect(origin)
        field: dpf.Field = op.outputs.field()
        assert field.max().data[0] > 1.0e-7
