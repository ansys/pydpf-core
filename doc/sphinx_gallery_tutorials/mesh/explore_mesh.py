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

# _order: 4
"""
.. _ref_tutorials_explore_mesh:

Explore a mesh
==============

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

This tutorial explains how to access a mesh data and metadata so it can be
manipulated.

The mesh object in DPF is a
:class:`MeshedRegion<ansys.dpf.core.meshed_region.MeshedRegion>`. You can
obtain a ``MeshedRegion`` by creating your own from scratch or by getting it
from a result file. For more information, see the
:ref:`ref_tutorials_create_a_mesh_from_scratch` and
:ref:`ref_tutorials_get_mesh_from_result_file` tutorials.
"""
###############################################################################
# Import the necessary modules
# -----------------------------

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Define the mesh
# ---------------
#
# For this tutorial, we get a
# :class:`MeshedRegion<ansys.dpf.core.meshed_region.MeshedRegion>` from a result
# file. For more information see the :ref:`ref_tutorials_get_mesh_from_result_file`
# tutorial.

###############################################################################
# MAPDL
result_file_path_1 = examples.find_static_rst()
model_1 = dpf.Model(data_sources=result_file_path_1)
meshed_region_1 = model_1.metadata.meshed_region

###############################################################################
# LS-DYNA

result_file_path_2 = examples.download_d3plot_beam()
ds_2 = dpf.DataSources()
ds_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
ds_2.add_file_path(filepath=result_file_path_2[3], key="actunits")
model_2 = dpf.Model(data_sources=ds_2)
meshed_region_2 = model_2.metadata.meshed_region

###############################################################################
# Fluent

result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
model_3 = dpf.Model(data_sources=result_file_path_3)
meshed_region_3 = model_3.metadata.meshed_region

###############################################################################
# CFX

result_file_path_4 = examples.download_cfx_mixing_elbow()
model_4 = dpf.Model(data_sources=result_file_path_4)
meshed_region_4 = model_4.metadata.meshed_region

###############################################################################
# Explore the mesh data
# ----------------------
#
# Access the mesh data by manipulating the ``MeshedRegion`` object methods.
# The mesh data includes:
#
# - Unit
# - Nodes, elements, and faces
# - Named selections
#
# The :attr:`MeshedRegion.nodes<ansys.dpf.core.meshed_region.MeshedRegion.nodes>`,
# :attr:`MeshedRegion.elements<ansys.dpf.core.meshed_region.MeshedRegion.elements>`,
# :attr:`MeshedRegion.faces<ansys.dpf.core.meshed_region.MeshedRegion.faces>`, and
# :attr:`MeshedRegion.named_selections<ansys.dpf.core.meshed_region.MeshedRegion.named_selections>`
# properties return corresponding DPF objects:
# :class:`Nodes<ansys.dpf.core.nodes.Nodes>`,
# :class:`Elements<ansys.dpf.core.elements.Elements>`,
# :class:`Faces<ansys.dpf.core.faces.Faces>`, and
# :class:`Scoping<ansys.dpf.core.scoping.Scoping>`.
#
# Here, we explore the data about the mesh nodes for each solver.

nodes_1 = meshed_region_1.nodes
print("Object type: ", type(nodes_1), "\n")
print("Nodes (MAPDL): ", nodes_1)

###############################################################################

nodes_2 = meshed_region_2.nodes
print("Nodes (LSDYNA): ", nodes_2)

###############################################################################

nodes_3 = meshed_region_3.nodes
print("Nodes (Fluent): ", nodes_3)

###############################################################################

nodes_4 = meshed_region_4.nodes
print("Nodes (CFX): ", nodes_4)

###############################################################################
# Get the mesh bounding box
# --------------------------
#
# Use the
# :attr:`MeshedRegion.bounding_box<ansys.dpf.core.meshed_region.MeshedRegion.bounding_box>`
# property to get the bounding box. It is a 6D
# :class:`Field<ansys.dpf.core.field.Field>` with 1 entity containing the
# bounding box data in the format ``[x_min, y_min, z_min, x_max, y_max, z_max]``.

bbox_1 = meshed_region_1.bounding_box
print("Bounding box (MAPDL): ", bbox_1)

bbox_2 = meshed_region_2.bounding_box
print("Bounding box (LSDYNA): ", bbox_2)

bbox_3 = meshed_region_3.bounding_box
print("Bounding box (Fluent): ", bbox_3)

bbox_4 = meshed_region_4.bounding_box
print("Bounding box (CFX): ", bbox_4)

###############################################################################
# Explore the mesh metadata
# --------------------------
#
# Access the mesh metadata by manipulating the ``MeshedRegion`` object properties.
# Check which metadata properties are available for each result file.

available_props_1 = meshed_region_1.available_property_fields
print("Available properties (MAPDL): ", available_props_1)

available_props_2 = meshed_region_2.available_property_fields
print("Available properties (LSDYNA): ", available_props_2)

available_props_3 = meshed_region_3.available_property_fields
print("Available properties (Fluent): ", available_props_3)

available_props_4 = meshed_region_4.available_property_fields
print("Available properties (CFX): ", available_props_4)

###############################################################################
# Extract a specific property — the element types for each mesh.
#
# The element type is given as a number. See
# :class:`element_types<ansys.dpf.core.elements.element_types>` for the
# corresponding element names.

el_types_1 = meshed_region_1.elements.element_types_field
print("Element types (MAPDL): ", el_types_1)

el_types_2 = meshed_region_2.property_field(property_name="eltype")
print("Element types (LSDYNA): ", el_types_2)

el_types_3 = meshed_region_3.property_field(property_name="eltype")
print("Element types (Fluent): ", el_types_3)

el_types_4 = meshed_region_4.property_field(property_name="eltype")
print("Element types (CFX): ", el_types_4)
