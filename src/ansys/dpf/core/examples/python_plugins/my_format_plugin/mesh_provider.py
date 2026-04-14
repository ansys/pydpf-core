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

"""mesh_provider operator for MyFormat files.

Returns a :class:`~ansys.dpf.core.meshed_region.MeshedRegion` built from
the ``NODES`` and ``ELEMENTS`` blocks of the file.
"""

import my_format_reader as reader
from result_info_provider import _get_file_path

from ansys.dpf import core as dpf
from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    PinSpecification,
    SpecificationProperties,
)

# Map MyFormat element type strings to DPF add_*_element helpers.
_ADD_ELEMENT = {
    "HEX8": "add_solid_element",
    "HEX20": "add_solid_element",
    "TET4": "add_solid_element",
    "TET10": "add_solid_element",
    "QUAD4": "add_shell_element",
    "TRI3": "add_shell_element",
    "WEDGE6": "add_solid_element",
    "PYRAMID5": "add_solid_element",
}


class mesh_provider(CustomOperatorBase):
    """Return a :class:`~ansys.dpf.core.meshed_region.MeshedRegion` for a MyFormat file.

    Inputs
    ------
    pin 3 : StreamsContainer, optional
        Streams container returned by the streams_provider.
    pin 4 : DataSources
        DataSources with a path to a ``.myf`` file (used when pin 3 is absent).

    Outputs
    -------
    pin 0 : MeshedRegion
        The mesh with nodes and elements read from the file.
    """

    def run(self):
        """Run the operator."""
        file_path = _get_file_path(self)

        model = reader.read(file_path)
        mesh = _build_mesh(model)

        self.set_output(0, mesh)
        self.set_succeeded()

    @property
    def specification(self) -> CustomSpecification:
        """Return the operator specification."""
        spec = CustomSpecification("Reads the mesh from a MyFormat (.myf) result file.")
        spec.inputs = {
            3: PinSpecification(
                name="streams_container",
                type_names=dpf.StreamsContainer,
                optional=True,
                document="Streams container (optional); takes priority over pin 4.",
            ),
            4: PinSpecification(
                name="data_sources",
                type_names=dpf.DataSources,
                optional=True,
                document="DataSources with a path to a .myf file.",
            ),
        }
        spec.outputs = {
            0: PinSpecification(
                name="mesh",
                type_names=dpf.MeshedRegion,
                optional=False,
                document="MeshedRegion with nodes and elements from the file.",
            ),
        }
        spec.properties = SpecificationProperties(
            user_name="MyFormat mesh provider", category="myformat"
        )
        return spec

    @property
    def name(self) -> str:
        """Return the operator scripting name."""
        return "myformat::myformat::mesh_provider"


def _build_mesh(model: reader.MyFormatModel) -> dpf.MeshedRegion:
    """Build a :class:`~ansys.dpf.core.meshed_region.MeshedRegion` from a parsed model."""
    mesh = dpf.MeshedRegion()
    mesh.unit = "m"

    # Add nodes.
    for node_id, coords in model.node_coords.items():
        mesh.nodes.add_node(node_id, coords)

    # Map node IDs to 0-based indices (required by add_*_element connectivity).
    node_id_list = list(model.node_coords.keys())
    node_id_to_index = {nid: idx for idx, nid in enumerate(node_id_list)}

    # Add elements.
    for elem_id, elem in model.elements.items():
        elem_type = elem["type"].upper()
        connectivity_indices = [node_id_to_index[nid] for nid in elem["connectivity"]]

        add_method_name = _ADD_ELEMENT.get(elem_type, "add_solid_element")
        add_method = getattr(mesh.elements, add_method_name)
        add_method(elem_id, connectivity_indices)

    return mesh
