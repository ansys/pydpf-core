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
.. _ref_tutorials_plot_deformed_mesh:

Plot with mesh deformation
==========================

This tutorial shows different commands for plotting a deformed mesh without data.

A mesh is represented in DPF by a
:class:`MeshedRegion<ansys.dpf.core.meshed_region.MeshedRegion>`.
You can store multiple ``MeshedRegion`` objects in a DPF collection called
:class:`MeshesContainer<ansys.dpf.core.meshes_container.MeshesContainer>`.

You can obtain a ``MeshedRegion`` by creating your own from scratch or by getting it
from a result file. For more information, see the
:ref:`ref_tutorials_create_a_mesh_from_scratch` and
:ref:`ref_tutorials_get_mesh_from_result_file` tutorials.

PyDPF-Core has a variety of plotting methods for generating 3D plots with Python.
These methods use VTK and leverage the `PyVista <https://github.com/pyvista/pyvista>`_ library.
"""
###############################################################################
# Load data to plot
# ------------------

import ansys.dpf.core as dpf
from ansys.dpf.core import examples, operators as ops

# Download and get the path to an example result file
result_file_path_1 = examples.download_piston_rod()

# Create a model from the result file
model_1 = dpf.Model(data_sources=result_file_path_1)

###############################################################################
# Get the deformation field
# --------------------------
#
# To deform the mesh, a nodal 3D vector field specifying the translation of each node
# in the mesh is needed.
#
# The following DPF objects can represent such a field and are accepted as inputs for
# the ``deform_by`` parameter of all plot methods:
#
# - A :class:`Field<ansys.dpf.core.field.Field>`
# - A :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
# - A result object
# - An :class:`Operator<ansys.dpf.core.dpf_operator.Operator>`
#
# Here, we use the
# :py:class:`displacement<ansys.dpf.core.operators.result.displacement.displacement>`
# operator, which outputs a nodal 3D vector field of distances.
# One can get the operator from the :class:`Model<ansys.dpf.core.model.Model>` with
# the data source already connected.
# For more information about extracting results from a result file, see the
# :ref:`ref_tutorials_import_data` tutorials section.

disp_op = model_1.results.displacement()

# Define the scale factor to apply to the deformation
scl_fct = 2.0

###############################################################################
# .. _ref_plot_deformed_mesh_with_model:
#
# Plot a deformed model
# ----------------------
#
# Plot the overall mesh loaded by the model with
# :py:meth:`Model.plot()<ansys.dpf.core.model.Model.plot>`.
# To add deformation, pass the displacement operator to the ``deform_by`` argument.
#
# .. note::
#
#     The :class:`DpfPlotter<ansys.dpf.core.plotter.DpfPlotter>` displays the mesh
#     with edges, lighting and axis widget enabled by default. You can pass additional
#     PyVista arguments to all plotting methods to change the default behavior (see options
#     for `pyvista.plot()
#     <https://docs.pyvista.org/api/plotting/_autosummary/pyvista.plot.html#pyvista.plot>`_).

model_1.plot(deform_by=disp_op, scale_factor=scl_fct)

###############################################################################
# .. _ref_plot_deformed_mesh_with_meshed_region:
#
# Plot a single mesh
# -------------------
#
# Get the mesh
# ^^^^^^^^^^^^^

meshed_region_1 = model_1.metadata.meshed_region

###############################################################################
# Plot the deformed mesh using ``MeshedRegion.plot()``
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Use the
# :py:meth:`MeshedRegion.plot()<ansys.dpf.core.meshed_region.MeshedRegion.plot>`
# method and pass the displacement operator to the ``deform_by`` argument.

meshed_region_1.plot(deform_by=disp_op, scale_factor=scl_fct)

###############################################################################
# Plot the deformed mesh using ``DpfPlotter``
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# 1. Create an instance of
#    :class:`DpfPlotter<ansys.dpf.core.plotter.DpfPlotter>`.
# 2. Add the mesh to the scene using
#    :py:meth:`add_mesh()<ansys.dpf.core.plotter.DpfPlotter.add_mesh>`,
#    passing the displacement operator to the ``deform_by`` argument.
# 3. Render and show the figure using
#    :py:meth:`show_figure()<ansys.dpf.core.plotter.DpfPlotter.show_figure>`.

plotter_1 = dpf.plotter.DpfPlotter()
plotter_1.add_mesh(meshed_region=meshed_region_1, deform_by=disp_op, scale_factor=scl_fct)
plotter_1.show_figure()

###############################################################################
# You can also plot data contours on a deformed mesh. For more information,
# see :ref:`ref_tutorials_plot_contour`.

###############################################################################
# .. _ref_plot_deformed_mesh_with_meshes_container:
#
# Plot several meshes
# --------------------
#
# Build a collection of meshes
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Use the
# :class:`split_mesh<ansys.dpf.core.operators.mesh.split_mesh.split_mesh>` operator
# to split the mesh based on the material of each element.
# This operator returns a
# :class:`MeshesContainer<ansys.dpf.core.meshes_container.MeshesContainer>` with meshes
# labeled according to the split criterion. For more information, see the
# :ref:`ref_tutorials_split_mesh` and :ref:`ref_tutorials_extract_mesh_in_split_parts`
# tutorials.

meshes = ops.mesh.split_mesh(mesh=meshed_region_1, property="mat").eval()
print(meshes)

###############################################################################
# Plot the deformed meshes
# ^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Use
# :py:meth:`MeshesContainer.plot()<ansys.dpf.core.meshes_container.MeshesContainer.plot>`
# and pass the displacement operator to ``deform_by``.
# This plots all ``MeshedRegion`` objects in the ``MeshesContainer`` and colors them based
# on the split criterion.

meshes.plot(deform_by=disp_op, scale_factor=scl_fct)

###############################################################################
# You can also plot data on a collection of deformed meshes. For more information,
# see :ref:`ref_tutorials_plot_contour`.
