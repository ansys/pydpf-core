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

# _order: 3
"""
.. _ref_tutorials_explore_mesh_metadata:

Explore a mesh metadata
========================

:bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

.. note::

    This tutorial requires DPF 9.1 or above (2025 R1).

This tutorial explains how to read mesh metadata (data about the elements, nodes,
faces, regions, zones, ...) before extracting the mesh from a result file.

The mesh metadata information is stored in a
:class:`PropertyField<ansys.dpf.core.property_field.PropertyField>` or in a
:class:`StringField<ansys.dpf.core.string_field.StringField>`. It describes the
mesh composition and is mapped to the entity it is defined at. Available metadata
includes:

- Properties, parts, faces, bodies, zones
- Number of nodes and elements
- Element types
"""
###############################################################################
# Import the necessary modules
# -----------------------------

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# LS-DYNA — explore mesh metadata
# ---------------------------------
#
# Import the result file and create the
# :class:`Model<ansys.dpf.core.model.Model>`.

result_file_path_2 = examples.download_d3plot_beam()
ds_2 = dpf.DataSources()
ds_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
ds_2.add_file_path(filepath=result_file_path_2[3], key="actunits")
model_2 = dpf.Model(data_sources=ds_2)

###############################################################################
# Access the :class:`MeshInfo<ansys.dpf.core.mesh_info.MeshInfo>` object to
# explore available metadata before extracting the mesh.

mesh_info_2 = model_2.metadata.mesh_info
print(mesh_info_2)

###############################################################################
# Extract specific metadata — here the part names.

cell_zones_2 = mesh_info_2.get_property("part_names")
print(cell_zones_2)

###############################################################################
# Fluent — explore mesh metadata
# --------------------------------

result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
model_3 = dpf.Model(data_sources=result_file_path_3)

mesh_info_3 = model_3.metadata.mesh_info
print(mesh_info_3)

###############################################################################
# Extract the cell zone names.

cell_zones_3 = mesh_info_3.get_property("cell_zone_names")
print(cell_zones_3)

###############################################################################
# CFX — explore mesh metadata
# ----------------------------

result_file_path_4 = examples.download_cfx_mixing_elbow()
model_4 = dpf.Model(data_sources=result_file_path_4)

mesh_info_4 = model_4.metadata.mesh_info
print(mesh_info_4)

###############################################################################
# Extract the cell zone names.

cell_zones_4 = mesh_info_4.get_property("cell_zone_names")
print(cell_zones_4)
