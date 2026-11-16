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

# _order: 6
"""
.. _ref_tutorials_split_mesh:

Split a mesh
============

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

This tutorial shows how to split a mesh on a given property.

There are two approaches:

- :ref:`Use the split_mesh operator <ref_first_approach_split_mesh>` to split an
  already existing :class:`MeshedRegion<ansys.dpf.core.meshed_region.MeshedRegion>`.
- :ref:`Split the mesh scoping <ref_second_approach_split_mesh>` and create the
  split ``MeshedRegion`` objects.
"""
###############################################################################
# Import the necessary modules
# -----------------------------

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Define the mesh
# ----------------
#
# For this tutorial, we get a ``MeshedRegion`` from a result file for each solver.
# For more information see the :ref:`ref_tutorials_get_mesh_from_result_file`
# tutorial.
#
# MAPDL — use a multi-shell result file.

result_file_path_1 = examples.find_multishells_rst()
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
# .. _ref_first_approach_split_mesh:
#
# First approach — use the ``split_mesh`` operator
# -------------------------------------------------
#
# Use the
# :class:`split_mesh<ansys.dpf.core.operators.mesh.split_mesh.split_mesh>` operator
# to split an already existing ``MeshedRegion`` based on a given property.
# Currently you can split a mesh by material (``"mat"``) or element type
# (``"eltype"``).
#
# The split mesh parts are stored in a
# :class:`MeshesContainer<ansys.dpf.core.meshes_container.MeshesContainer>`,
# ordered by ``labels``. When using the ``split_mesh`` operator, each split mesh
# part has two labels: a ``"body"`` label and a label for the property used to
# split the mesh.
#
# Here, we split the ``MeshedRegion`` by material.

meshes_11 = ops.mesh.split_mesh(mesh=meshed_region_1, property="mat").eval()
print("Split mesh MAPDL:", meshes_11)

meshes_21 = ops.mesh.split_mesh(mesh=meshed_region_2, property="mat").eval()
print("Split mesh LSDYNA:", meshes_21)

meshes_31 = ops.mesh.split_mesh(mesh=meshed_region_3, property="mat").eval()
print("Split mesh Fluent:", meshes_31)

meshes_41 = ops.mesh.split_mesh(mesh=meshed_region_4, property="mat").eval()
print("Split mesh CFX:", meshes_41)

###############################################################################
# .. _ref_second_approach_split_mesh:
#
# Second approach — split the scoping then build meshes
# ------------------------------------------------------
#
# This approach:
#
# 1. Uses the
#    :class:`split_on_property_type<ansys.dpf.core.operators.scoping.split_on_property_type.split_on_property_type>`
#    operator to split the mesh
#    :class:`Scoping<ansys.dpf.core.scoping.Scoping>` on a given property.
#    The split scoping is stored in a
#    :class:`ScopingsContainer<ansys.dpf.core.scopings_container.ScopingsContainer>`,
#    ordered by labels for the split property.
#
# 2. Creates the split ``MeshedRegion`` objects using the
#    :class:`from_scopings<ansys.dpf.core.operators.mesh.from_scopings.from_scopings>`
#    operator for each ``Scoping`` of interest.
#    The split parts are stored in a ``MeshesContainer``.
#
# Here, we split the mesh scoping by material and create a ``MeshedRegion`` for all
# split ``Scoping`` objects in the ``ScopingsContainer``.

split_scoping_1 = ops.scoping.split_on_property_type(mesh=meshed_region_1, label1="mat").eval()
meshes_12 = ops.mesh.from_scopings(scopings_container=split_scoping_1, mesh=meshed_region_1).eval()
print("Split via scoping MAPDL:", meshes_12)

split_scoping_2 = ops.scoping.split_on_property_type(mesh=meshed_region_2, label1="mat").eval()
meshes_22 = ops.mesh.from_scopings(scopings_container=split_scoping_2, mesh=meshed_region_2).eval()
print("Split via scoping LSDYNA:", meshes_22)

split_scoping_3 = ops.scoping.split_on_property_type(mesh=meshed_region_3, label1="mat").eval()
meshes_32 = ops.mesh.from_scopings(scopings_container=split_scoping_3, mesh=meshed_region_3).eval()
print("Split via scoping Fluent:", meshes_32)

split_scoping_4 = ops.scoping.split_on_property_type(mesh=meshed_region_4, label1="mat").eval()
meshes_42 = ops.mesh.from_scopings(scopings_container=split_scoping_4, mesh=meshed_region_4).eval()
print("Split via scoping CFX:", meshes_42)
