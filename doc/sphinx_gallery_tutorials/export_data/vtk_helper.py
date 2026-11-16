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
.. _ref_tutorials_export_data_vtk_helper:

Convert DPF data to PyVista objects
===================================

Convert DPF meshes and fields to PyVista ``UnstructuredGrid`` objects for
in-memory manipulation and custom visualization.

Unlike the VTU export operators, which write files to disk, the
:mod:`vtk_helper <ansys.dpf.core.vtk_helper>` module works entirely in memory:
it converts |MeshedRegion|, |Field|, |FieldsContainer|, and |PropertyField| objects to
``pyvista.UnstructuredGrid`` objects that you can plot, filter, combine, or save
to any format that PyVista supports.

This tutorial demonstrates how to convert a mesh, validate it, enrich it with
multiple fields incrementally, and batch-convert all time steps of a transient
result at once.
"""

###############################################################################
# Import required modules
# -----------------------
#
# Import the required modules and the helper functions from
# :mod:`vtk_helper <ansys.dpf.core.vtk_helper>`.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.vtk_helper import (
    append_field_to_grid,
    dpf_field_to_vtk,
    dpf_fieldscontainer_to_vtk,
    dpf_mesh_to_vtk,
    vtk_mesh_is_valid,
)

###############################################################################
# Load the result file
# --------------------
#
# Load a static structural result file and extract the |MeshedRegion| and
# |Model| that are reused throughout the first part of this tutorial.

# Find and load the static structural result file
result_file = examples.find_static_rst()

# Create a DataSources object
ds = dpf.DataSources(result_path=result_file)

# Create a Model for result access
my_model = dpf.Model(data_sources=ds)

# Get the MeshedRegion
mesh = my_model.metadata.meshed_region

###############################################################################
# Convert a mesh to a PyVista grid
# ---------------------------------
#
# Use :func:`dpf_mesh_to_vtk <ansys.dpf.core.vtk_helper.dpf_mesh_to_vtk>` to
# convert a |MeshedRegion| to a ``pyvista.UnstructuredGrid``.
# The resulting object contains only the geometry (nodes and connectivity); no
# field data is attached yet.

# Convert the MeshedRegion to a PyVista UnstructuredGrid
grid = dpf_mesh_to_vtk(mesh=mesh)
print(grid)

###############################################################################
# Validate the mesh
# -----------------
#
# Use :func:`vtk_mesh_is_valid <ansys.dpf.core.vtk_helper.vtk_mesh_is_valid>`
# to check whether the converted grid passes VTK's built-in cell validator.
# For a valid mesh it prints a confirmation; for an invalid one it lists the
# elements that fail each geometric check.

# Run the cell validity check and print the result
validity = vtk_mesh_is_valid(grid=grid, verbose=True)

###############################################################################
# Convert a field to a PyVista grid
# ----------------------------------
#
# Use :func:`dpf_field_to_vtk <ansys.dpf.core.vtk_helper.dpf_field_to_vtk>` to
# convert a displacement |Field| and its associated mesh in a single call.
# Nodal data is automatically stored in ``grid.point_data``; elemental data
# goes into ``grid.cell_data``.
# Elemental-nodal data is not supported by VTK objects.

# Extract the displacement FieldsContainer and get the first time step
disp_fc = my_model.results.displacement.eval()
disp_field = disp_fc[0]

# Convert the Field and its mesh to a single UnstructuredGrid
disp_grid = dpf_field_to_vtk(field=disp_field, field_name="displacement")
print(disp_grid.point_data)

###############################################################################
# Visualize the displacement magnitude
# ------------------------------------
#
# Use the DPF :class:`norm <ansys.dpf.core.operators.math.norm>` operator to
# compute the Euclidean norm of the displacement vector at each node, then
# append the resulting scalar |Field| to the grid and plot it.

# Compute the displacement magnitude using the DPF norm operator
norm_field = dpf.operators.math.norm(field=disp_field).eval()

# Append the scalar magnitude field to the displacement grid
disp_grid = append_field_to_grid(
    field=norm_field, meshed_region=mesh, grid=disp_grid, field_name="displacement_magnitude"
)

# Plot the magnitude on the mesh
disp_grid.plot(scalars="displacement_magnitude", show_edges=True)

###############################################################################
# Build a grid incrementally with multiple fields
# ------------------------------------------------
#
# Use :func:`append_field_to_grid <ansys.dpf.core.vtk_helper.append_field_to_grid>`
# to enrich an existing grid with additional field data.
# This approach is useful when you want to attach several results to the same
# ``UnstructuredGrid`` — for example nodal and elemental quantities together.

# Create a bare grid from the MeshedRegion
rich_grid = dpf_mesh_to_vtk(mesh=mesh)

# Append the displacement field (nodal location — stored in point_data)
rich_grid = append_field_to_grid(
    field=disp_field, meshed_region=mesh, grid=rich_grid, field_name="displacement"
)

# Append the element-type property field (elemental location — stored in cell_data)
eltype_pf = mesh.property_field(property_name="eltype")
rich_grid = append_field_to_grid(
    field=eltype_pf, meshed_region=mesh, grid=rich_grid, field_name="element_type"
)

# Inspect the resulting data arrays on the grid
print("Nodal arrays:    ", list(rich_grid.point_data.keys()))
print("Elemental arrays:", list(rich_grid.cell_data.keys()))

###############################################################################
# Convert all time steps of a FieldsContainer
# --------------------------------------------
#
# Use
# :func:`dpf_fieldscontainer_to_vtk <ansys.dpf.core.vtk_helper.dpf_fieldscontainer_to_vtk>`
# to convert every |Field| in a |FieldsContainer| to a single
# ``UnstructuredGrid``.
# Each time step becomes a separate data array keyed by its label space, so
# all time steps are accessible from the same object.

# Load a transient result file with multiple time steps
transient_result = examples.download_transient_result()
trans_ds = dpf.DataSources(result_path=transient_result)
trans_model = dpf.Model(data_sources=trans_ds)

# Extract displacement for all time steps
all_disp_fc = trans_model.results.displacement.on_all_time_freqs.eval()

# Convert the entire FieldsContainer to a single UnstructuredGrid
fc_grid = dpf_fieldscontainer_to_vtk(fields_container=all_disp_fc, field_name="displacement")

# Each time step is stored as a separate point-data array
print(f"Number of time-step arrays: {len(fc_grid.point_data)}")
print("Array names (first 3):", list(fc_grid.point_data.keys())[:3])
