# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

# Tests the serialization.vtu_export operator

import pytest

import ansys.dpf.core as dpf
import conftest


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_12_0,
    reason="vtu_export DataSources output requires server version >= 12.0",
)
def test_operator_vtu_export(server_type, tmp_path):
    # --- Mesh: single HEX8 element (unit cube) ---
    mesh = dpf.MeshedRegion(server=server_type)
    mesh.unit = "m"

    node_coords = [
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 1.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 1.0],
        [1.0, 1.0, 1.0],
        [0.0, 1.0, 1.0],
    ]
    for node_id, coords in enumerate(node_coords, start=1):
        mesh.nodes.add_node(node_id, coords)

    # Connectivity: scoping indices (0-based) of the 8 corner nodes
    mesh.elements.add_solid_element(1, [0, 1, 2, 3, 4, 5, 6, 7])

    node_ids = list(range(1, 9))

    # --- fields1: temperature (scalar, nodal), 3 time steps ---
    fields1 = dpf.FieldsContainer(server=server_type)
    fields1.labels = ["time"]
    for time_id in range(1, 4):
        field = dpf.Field(nentities=8, nature=dpf.common.natures.scalar, server=server_type)
        field.location = dpf.locations.nodal
        field.scoping.ids = node_ids
        field.scoping.location = dpf.locations.nodal
        field.data = [20.0 + time_id + i for i in range(8)]
        fields1.add_field({"time": time_id}, field)

    # --- fields2: displacement (vector, nodal), 3 time steps ---
    fields2 = dpf.FieldsContainer(server=server_type)
    fields2.labels = ["time"]
    for time_id in range(1, 4):
        field = dpf.Field(nentities=8, nature=dpf.common.natures.vector, server=server_type)
        field.location = dpf.locations.nodal
        field.scoping.ids = node_ids
        field.scoping.location = dpf.locations.nodal
        field.data = [
            float(time_id) * 0.001 * (i + 1) for i in range(8) for _ in range(3)
        ]
        fields2.add_field({"time": time_id}, field)

    vtu_export_op = dpf.operators.serialization.vtu_export(
        directory=str(tmp_path),
        base_name="simple_bar_export",
        mesh=mesh,
        fields1=fields1,
        fields2=fields2,
        server=server_type,
    )
    output_ds = vtu_export_op.eval()
    assert isinstance(output_ds, dpf.DataSources)
    assert len(output_ds.result_files) == 3
    for path in output_ds.result_files:
        assert path.endswith(".vtu")
