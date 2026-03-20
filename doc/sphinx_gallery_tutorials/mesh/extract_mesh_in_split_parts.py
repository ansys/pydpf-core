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

# _order: 5
"""
.. _ref_tutorials_extract_mesh_in_split_parts:

Extract a mesh in split parts
==============================

:bdg-fluent:`Fluent` :bdg-cfx:`CFX`

This tutorial shows how to extract meshes split on a given space or time from a
result file.

To accomplish this goal, use the
:class:`meshes_provider<ansys.dpf.core.operators.mesh.meshes_provider.meshes_provider>`
operator. The split meshes are given in a
:class:`MeshesContainer<ansys.dpf.core.meshes_container.MeshesContainer>` and can
be spatially or temporally varying.
"""
###############################################################################
# Import the necessary modules
# -----------------------------

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Define the ``DataSources``
# --------------------------
#
# Create :class:`DataSources<ansys.dpf.core.data_sources.DataSources>` objects so
# the ``meshes_provider`` operator can access the mesh. For this tutorial, use
# result files available in the :mod:`examples<ansys.dpf.core.examples>` module.
# For more information on importing result files, see the
# :ref:`ref_tutorials_import_data` tutorials section.

# Fluent
result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
ds_3 = dpf.DataSources(result_path=result_file_path_3)

# CFX
result_file_path_4 = examples.download_cfx_mixing_elbow()
ds_4 = dpf.DataSources(result_path=result_file_path_4)

###############################################################################
# Extract all mesh parts — Fluent
# --------------------------------
#
# Instantiate and evaluate the ``meshes_provider`` operator.

meshes_31 = ops.mesh.meshes_provider(data_sources=ds_3).eval()
print(meshes_31)

###############################################################################
# Extract all mesh parts — CFX

meshes_41 = ops.mesh.meshes_provider(data_sources=ds_4).eval()
print(meshes_41)

###############################################################################
# Scope the mesh regions to extract — Fluent
# -------------------------------------------
#
# A region corresponds to a zone for Fluid and CFX results. Specify the mesh
# regions you want to get by passing zone ids to the ``region_scoping`` argument.

meshes_32 = ops.mesh.meshes_provider(data_sources=ds_3, region_scoping=[3, 12]).eval()
print(meshes_32)

###############################################################################
# Scope the mesh regions to extract — CFX

meshes_42 = ops.mesh.meshes_provider(data_sources=ds_4, region_scoping=[5, 8]).eval()
print(meshes_42)
