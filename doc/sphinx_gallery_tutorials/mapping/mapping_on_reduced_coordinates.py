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
.. _ref_tutorials_mapping_on_reduced_coordinates:

Reduced coordinates mapping
=============================

Perform high-precision interpolation using a two-step element-local coordinate approach.

This tutorial demonstrates the ``find_reduced_coordinates`` / ``on_reduced_coordinates``
workflow for mapping field values. In the first step,
:class:`find_reduced_coordinates<ansys.dpf.core.operators.mapping.find_reduced_coordinates>`
locates which element contains each target point and computes the element-local (reference)
coordinates. In the second step,
:class:`on_reduced_coordinates<ansys.dpf.core.operators.mapping.on_reduced_coordinates>`
uses those element-local coordinates to perform the interpolation.

Compared to direct :ref:`ref_tutorials_mapping_on_coordinates` mapping, this approach
gives explicit access to element-local positions, enables efficient reuse for multiple
field types, and supports higher-accuracy quadratic element interpolation.

Any target point outside the source mesh returns an empty value.
"""

###############################################################################
# Import modules and load the model
# ----------------------------------
# Import the required modules and load a result file.

# Import the ``ansys.dpf.core`` module
# Import NumPy for coordinate manipulation
import numpy as np

from ansys.dpf import core as dpf

# Import the examples and operators modules
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Load model
# ----------
# Download and load a result file, then create a
# :class:`Model<ansys.dpf.core.model.Model>` object.

result_file = examples.find_static_rst()
model = dpf.Model(data_sources=result_file)
print(model)

###############################################################################
# Extract the mesh
# ----------------
# The mesh is needed by both ``find_reduced_coordinates`` and
# ``on_reduced_coordinates``.

mesh = model.metadata.meshed_region
print(mesh)

###############################################################################
# Define target coordinates
# --------------------------
# Create a :class:`Field<ansys.dpf.core.field.Field>` that holds the points
# at which field values should be interpolated.

# Each row is one point with [x, y, z] coordinate values
points = np.array(
    [
        [0.01, 0.04, 0.01],
        [0.02, 0.05, 0.02],
    ]
)
coords_field = dpf.fields_factory.field_from_array(arr=points)
print(coords_field)

###############################################################################
# Step 1: Find reduced coordinates and element IDs
# -------------------------------------------------
# Use ``find_reduced_coordinates`` to determine which element contains each
# target point and the corresponding element-local (reference) coordinates.

find_op = ops.mapping.find_reduced_coordinates(
    coordinates=coords_field,
    mesh=mesh,
)
reduced_coords_fc = find_op.outputs.reduced_coordinates()
element_ids_sc = find_op.outputs.element_ids()

print("Reduced coordinates:")
print(reduced_coords_fc)
print("\nElement IDs:")
print(element_ids_sc)

###############################################################################
# Examine the reduced coordinates
# ---------------------------------
# Reduced coordinates represent positions within the reference element coordinate system.

reduced_coords_field = reduced_coords_fc[0]
print("Reduced coordinates data:")
print(reduced_coords_field.data)

element_ids = element_ids_sc[0]
print("\nElement IDs for each coordinate:")
print(element_ids.ids)

###############################################################################
# Step 2: Map displacement to reduced coordinates
# ------------------------------------------------
# Use ``on_reduced_coordinates`` to interpolate displacement values at the
# reduced coordinates found in step 1.

displacement_fc = model.results.displacement.eval()
print(displacement_fc)

mapping_op = ops.mapping.on_reduced_coordinates(
    fields_container=displacement_fc,
    reduced_coordinates=reduced_coords_fc,
    element_ids=element_ids_sc,
    mesh=mesh,
)
mapped_displacement_fc = mapping_op.eval()
print(mapped_displacement_fc)

###############################################################################
# Access mapped results
# ----------------------
# Extract and display the interpolated displacement values.

mapped_field = mapped_displacement_fc[0]
mapped_data = mapped_field.data
print("\nInterpolated displacement values:")
for i, point in enumerate(points):
    elem_id = element_ids.ids[i]
    print(f"  Point {i + 1} at {point} in element {elem_id}: {mapped_data[i]}")

###############################################################################
# Reuse reduced coordinates for stress
# --------------------------------------
# Once the reduced coordinates and element IDs are available they can be reused
# to map additional result types efficiently without repeating the search step.

stress_fc = model.results.stress.eval()
mapped_stress_fc = ops.mapping.on_reduced_coordinates(
    fields_container=stress_fc,
    reduced_coordinates=reduced_coords_fc,
    element_ids=element_ids_sc,
    mesh=mesh,
).eval()
print(mapped_stress_fc[0])

stress_data = mapped_stress_fc[0].data
print("\nInterpolated stress values:")
for i, point in enumerate(points):
    elem_id = element_ids.ids[i]
    print(f"  Point {i + 1} at {point} in element {elem_id}: {stress_data[i]}")

###############################################################################
# Use quadratic elements for higher precision
# -------------------------------------------
# For meshes with quadratic elements, enable the ``use_quadratic_elements`` option
# in both operators for higher-order interpolation accuracy.

find_op_quad = ops.mapping.find_reduced_coordinates(
    coordinates=coords_field,
    mesh=mesh,
    use_quadratic_elements=True,
)
reduced_coords_quad_fc = find_op_quad.outputs.reduced_coordinates()
element_ids_quad_sc = find_op_quad.outputs.element_ids()

mapped_disp_quad_fc = ops.mapping.on_reduced_coordinates(
    fields_container=displacement_fc,
    reduced_coordinates=reduced_coords_quad_fc,
    element_ids=element_ids_quad_sc,
    mesh=mesh,
    use_quadratic_elements=True,
).eval()

print("Displacement with quadratic interpolation:")
print(mapped_disp_quad_fc[0].data)
