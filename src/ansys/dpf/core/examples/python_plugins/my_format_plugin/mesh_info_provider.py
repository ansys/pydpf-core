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

"""mesh_info_provider operator for MyFormat files.

Returns a :class:`~ansys.dpf.core.generic_data_container.GenericDataContainer`
with the mesh metadata (node count, element count, element types, zone info).
DPF wraps this container into a :class:`~ansys.dpf.core.mesh_info.MeshInfo`
object on the client side.
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

# Map MyFormat element type strings to DPF element_types enum values.
_ELEMENT_TYPE_MAP = {
    "HEX8": dpf.element_types.Hex8,
    "HEX20": dpf.element_types.Hex20,
    "TET4": dpf.element_types.Tet4,
    "TET10": dpf.element_types.Tet10,
    "QUAD4": dpf.element_types.Quad4,
    "TRI3": dpf.element_types.Tri3,
    "WEDGE6": dpf.element_types.Wedge6,
    "PYRAMID5": dpf.element_types.Pyramid5,
}


class mesh_info_provider(CustomOperatorBase):
    """Return mesh metadata for a MyFormat file.

    Outputs a :class:`~ansys.dpf.core.generic_data_container.GenericDataContainer`
    with the standard ``mesh_info`` schema consumed by
    DPF's built-in ``mesh_info_provider`` routing.

    Inputs
    ------
    pin 3 : StreamsContainer, optional
        Streams container returned by the streams_provider.
    pin 4 : DataSources
        DataSources with a path to a ``.myf`` file (used when pin 3 is absent).

    Outputs
    -------
    pin 0 : GenericDataContainer  (mesh_info)
        Mesh metadata including node count, element count, zone names, and
        available element types.
    """

    def run(self):
        """Run the operator."""
        file_path = _get_file_path(self)

        model = reader.read(file_path)
        gdc = _build_mesh_info(model)

        self.set_output(0, gdc)
        self.set_succeeded()

    @property
    def specification(self) -> CustomSpecification:
        """Return the operator specification."""
        spec = CustomSpecification("Reads mesh metadata from a MyFormat (.myf) result file.")
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
                name="mesh_info",
                type_names=dpf.GenericDataContainer,
                optional=False,
                document="GenericDataContainer with mesh metadata.",
                name_derived_class="mesh_info",
            ),
        }
        spec.properties = SpecificationProperties(
            user_name="MyFormat mesh info provider", category="myformat"
        )
        return spec

    @property
    def name(self) -> str:
        """Return the operator scripting name."""
        return "myformat::mesh_info_provider"


def _build_mesh_info(model: reader.MyFormatModel) -> dpf.GenericDataContainer:
    """Build a GenericDataContainer with the ``mesh_info`` schema."""
    num_nodes = len(model.node_coords)
    num_elements = len(model.elements)

    # Collect unique element types present in the file.
    elem_type_ids = []
    for elem in model.elements.values():
        et = _ELEMENT_TYPE_MAP.get(elem["type"].upper(), dpf.element_types.General)
        if et.value not in elem_type_ids:
            elem_type_ids.append(et.value)

    # Build zone information.  The MyFormat file has a single "body" zone.
    zone_id = 1
    zone_names = dpf.StringField(nentities=1)
    zone_names.append(data=["body_1"], scopingid=zone_id)
    zone_names.location = dpf.locations.zone

    zone_scoping = dpf.Scoping(location="zone", ids=[zone_id])
    cell_zone_scoping = dpf.Scoping(location="zone", ids=[zone_id])
    face_zone_scoping = dpf.Scoping(location="zone", ids=[])

    cell_zone_names = dpf.StringField(nentities=1)
    cell_zone_names.append(data=["body_1"], scopingid=zone_id)
    cell_zone_names.location = dpf.locations.zone

    face_zone_names = dpf.StringField()
    face_zone_names.location = dpf.locations.zone

    available_elem_types = dpf.Scoping(location=dpf.locations.overall, ids=elem_type_ids)

    gdc = dpf.GenericDataContainer()
    gdc.set_property(property_name="num_nodes", prop=num_nodes)
    gdc.set_property(property_name="num_elements", prop=num_elements)
    gdc.set_property(property_name="zone_names", prop=zone_names)
    gdc.set_property(property_name="zone_scoping", prop=zone_scoping)
    gdc.set_property(property_name="available_elem_types", prop=available_elem_types)
    gdc.set_property(property_name="cell_zone_names", prop=cell_zone_names)
    gdc.set_property(property_name="cell_zone_scoping", prop=cell_zone_scoping)
    gdc.set_property(property_name="face_zone_names", prop=face_zone_names)
    gdc.set_property(property_name="face_zone_scoping", prop=face_zone_scoping)
    return gdc
