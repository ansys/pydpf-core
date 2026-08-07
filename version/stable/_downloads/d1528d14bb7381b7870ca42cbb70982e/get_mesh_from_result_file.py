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

# _order: 2
"""
.. _ref_tutorials_get_mesh_from_result_file:

Get a mesh from a result file
==============================

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

This tutorial explains how to extract a mesh from a result file.

The mesh object in DPF is a
:class:`MeshedRegion<ansys.dpf.core.meshed_region.MeshedRegion>`. You can obtain
a ``MeshedRegion`` by creating your own from scratch or by getting it from a
result file.

You can get the mesh from a result file using two approaches:

- Using the :class:`Model<ansys.dpf.core.model.Model>`
- Using the :class:`mesh_provider<ansys.dpf.core.operators.mesh.mesh_provider.mesh_provider>` operator

.. note::

    A ``Model`` extracts a large amount of information by default (results, mesh and
    analysis data). If using this helper takes a long time, consider using a
    ``DataSources`` object and instantiating operators directly with it.
"""
###############################################################################
# Import the necessary modules
# -----------------------------

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

###############################################################################
# MAPDL — import and get mesh
# ----------------------------
#
# Define result file path and create a
# :class:`DataSources<ansys.dpf.core.data_sources.DataSources>` object.

result_file_path_1 = examples.find_static_rst()
ds_1 = dpf.DataSources(result_path=result_file_path_1)

###############################################################################
# Get the mesh using the ``Model``.

model_1 = dpf.Model(data_sources=ds_1)
meshed_region_11 = model_1.metadata.meshed_region
print(meshed_region_11)

###############################################################################
# Get the mesh using the
# :class:`mesh_provider<ansys.dpf.core.operators.mesh.mesh_provider.mesh_provider>`
# operator.

meshed_region_12 = ops.mesh.mesh_provider(data_sources=ds_1).eval()
print(meshed_region_12)

###############################################################################
# LS-DYNA — import and get mesh
# ------------------------------
#
# The d3plot file requires an ``actunits`` file to get correct units when the
# simulation was run through Mechanical.

result_file_path_2 = examples.download_d3plot_beam()
ds_2 = dpf.DataSources()
ds_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
ds_2.add_file_path(filepath=result_file_path_2[3], key="actunits")

###############################################################################
# Get the mesh using the ``Model``.

model_2 = dpf.Model(data_sources=ds_2)
meshed_region_21 = model_2.metadata.meshed_region
print(meshed_region_21)

###############################################################################
# Get the mesh using the ``mesh_provider`` operator.

meshed_region_22 = ops.mesh.mesh_provider(data_sources=ds_2).eval()
print(meshed_region_22)

###############################################################################
# Fluent — import and get mesh
# -----------------------------

result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
ds_3 = dpf.DataSources(result_path=result_file_path_3)

###############################################################################
# Get the mesh using the ``Model``.

model_3 = dpf.Model(data_sources=ds_3)
meshed_region_31 = model_3.metadata.meshed_region
print(meshed_region_31)

###############################################################################
# Get the mesh using the ``mesh_provider`` operator.

meshed_region_32 = ops.mesh.mesh_provider(data_sources=ds_3).eval()
print(meshed_region_32)

###############################################################################
# CFX — import and get mesh
# --------------------------

result_file_path_4 = examples.download_cfx_mixing_elbow()
ds_4 = dpf.DataSources(result_path=result_file_path_4)

###############################################################################
# Get the mesh using the ``Model``.

model_4 = dpf.Model(data_sources=ds_4)
meshed_region_41 = model_4.metadata.meshed_region
print(meshed_region_41)

###############################################################################
# Get the mesh using the ``mesh_provider`` operator.

meshed_region_42 = ops.mesh.mesh_provider(data_sources=ds_4).eval()
print(meshed_region_42)
