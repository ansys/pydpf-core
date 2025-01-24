# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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

# noqa: D400
"""
.. _solution_combination:

Load case combination for principal stress
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to get a principal stress load case combination using DPF
And highlight min/max values in the plot.

"""

###############################################################################
# Import the ``ansys.dpf.core`` module, included examples file, and the ``DpfPlotter``
# module.
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.plotter import DpfPlotter

###############################################################################
# Open an example and print the ``Model`` object. The
# :class:`Model <ansys.dpf.core.model.Model>` class helps to organize access
# methods for the result by keeping track of the operators and data sources
# used by the result file.
#
# Printing the model displays this metadata:
#
# - Analysis type
# - Available results
# - Size of the mesh
# - Number of results
#
model = dpf.Model(examples.find_msup_transient())
print(model)

###############################################################################
# Get the stress tensor and ``connect`` time scoping.
# Make sure that you define ``dpf.locations.nodal`` as the scoping location because
# labels are supported only for nodal results.
#
stress_tensor = model.results.stress()
time_scope = dpf.Scoping()
time_scope.ids = [1, 2]
stress_tensor.inputs.time_scoping.connect(time_scope)
stress_tensor.inputs.requested_location.connect(dpf.locations.nodal)

###############################################################################
# This code performs solution combination on two load cases, LC1 and LC2.
# You can access individual load cases as the fields of a fields container for
# the stress tensor.
field_lc1 = stress_tensor.outputs.fields_container()[0]
field_lc2 = stress_tensor.outputs.fields_container()[1]

# Scale LC2 to -1.
stress_tensor_lc2_sc = dpf.operators.math.scale(field=field_lc2, ponderation=-1.0)

###############################################################################
# Add load cases.
stress_tensor_combi = dpf.operators.math.add(fieldA=field_lc1, fieldB=stress_tensor_lc2_sc)

###############################################################################
# Principal stresses are the Eigenvalues of the stress tensor.
# Use principal invariants to get S1, S2, and S3.
#
p_inv = dpf.operators.invariant.principal_invariants()
p_inv.inputs.field.connect(stress_tensor_combi)

###############################################################################
# Print S1 (maximum principal stress).
#
print(p_inv.outputs.field_eig_1().data)

###############################################################################
# Get the meshed region.
#
mesh_set = model.metadata.meshed_region

###############################################################################
# Plot the results on the mesh.
# The ``label_text_size`` and ``label_point_size`` arguments control the font
# size of the label.
#
plot = DpfPlotter()
plot.add_field(p_inv.outputs.field_eig_1(), meshed_region=mesh_set)

# You can set the camera positions using the ``cpos`` argument.
# The three tuples in the list for the ``cpos`` argument represent the camera
# position, focal point, and view respectively.
plot.show_figure(show_axes=True)
