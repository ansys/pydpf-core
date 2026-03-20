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

# _order: 1
"""
.. _ref_tutorials_mapping_on_coordinates:

Interpolation at coordinates
=============================

Interpolate field values at arbitrary spatial coordinates using element shape functions.

This tutorial demonstrates how to use the
:class:`on_coordinates<ansys.dpf.core.operators.mapping.on_coordinates>` operator to extract
result values at specific locations in a model. The operator interpolates field values at
arbitrary coordinates using the mesh shape functions, enabling you to extract results
along paths, at sensor locations, or on custom grids.

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
# Extract displacement results
# ----------------------------
# Get the displacement results from the model as a
# :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`.

displacement_fc = model.results.displacement.eval()
print(displacement_fc)
print(displacement_fc[0])

###############################################################################
# Define coordinates of interest
# --------------------------------
# Define the spatial coordinates where field values should be interpolated, then
# create a :class:`Field<ansys.dpf.core.field.Field>` from the array using
# :mod:`fields_factory<ansys.dpf.core.fields_factory>`.

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
# Map displacement to coordinates
# --------------------------------
# Use the ``on_coordinates`` operator to interpolate displacement values
# at the defined coordinates.

mapping_op = ops.mapping.on_coordinates(
    fields_container=displacement_fc,
    coordinates=coords_field,
)
mapped_displacement_fc = mapping_op.eval()
print(mapped_displacement_fc)

###############################################################################
# Access mapped results
# ----------------------
# Extract and display the interpolated displacement values.

mapped_field = mapped_displacement_fc[0]
print(mapped_field)

# Extract the data as a NumPy array
mapped_data = mapped_field.data
print("Interpolated displacement values:")
print(mapped_data)

###############################################################################
# Provide mesh explicitly
# -----------------------
# If the input fields do not have a mesh in their support, you can provide the
# mesh explicitly via the ``mesh`` pin.

mesh = model.metadata.meshed_region
mapping_op_with_mesh = ops.mapping.on_coordinates(
    fields_container=displacement_fc,
    coordinates=coords_field,
    mesh=mesh,
)
mapped_displacement_with_mesh = mapping_op_with_mesh.eval()
print(mapped_displacement_with_mesh[0])

###############################################################################
# Adjust tolerance for coordinate search
# ----------------------------------------
# Control the tolerance used in the iterative algorithm that locates coordinates
# inside the mesh. The default value is ``5e-5``.

mapping_op_with_tol = ops.mapping.on_coordinates(
    fields_container=displacement_fc,
    coordinates=coords_field,
    tolerance=1e-4,
)
mapped_displacement_with_tol = mapping_op_with_tol.eval()
print(mapped_displacement_with_tol[0])

###############################################################################
# Map multiple result types
# --------------------------
# The same coordinates can be reused to map different result types.

stress_fc = model.results.stress.eval()
mapped_stress_fc = ops.mapping.on_coordinates(
    fields_container=stress_fc,
    coordinates=coords_field,
).eval()
print(mapped_stress_fc[0])
