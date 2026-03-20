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
.. _ref_tutorials_mapping_prepare_workflow:

RBF-based workflow mapping
===========================

Generate a reusable workflow for mapping results using Radial Basis Function (RBF) filters.

This tutorial demonstrates how to use the
:class:`prepare_mapping_workflow<ansys.dpf.core.operators.mapping.prepare_mapping_workflow>`
operator to generate a reusable
:class:`Workflow<ansys.dpf.core.workflow.Workflow>` that maps results between meshes with
different topologies using RBF filters.

Unlike shape-function interpolation (used by ``on_coordinates`` and ``on_reduced_coordinates``),
RBF-based mapping can transfer data between non-conforming meshes where element boundaries do
not align. It evaluates target values by weighting surrounding source nodes based on distance.
The filter radius acts like a standard deviation in Gaussian weighting—small radii capture
local gradients while larger radii produce smoother trends. The optional influence box limits
the spatial search window as a computational optimization.

The resulting workflow accepts a source field and returns the interpolated target field; it can
be reused for multiple field types without repeating the setup step.
"""

###############################################################################
# Import modules and load the model
# ----------------------------------
# Import the required modules and load a result file.

# Import the ``ansys.dpf.core`` module
# Import NumPy for coordinate operations
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
# Define the input support
# ------------------------
# The input support is the mesh from which results will be mapped. Here we use the
# full solid mesh as the source.

input_mesh = model.metadata.meshed_region
print("Input support (mesh):")
print(input_mesh)

###############################################################################
# Define the output support
# --------------------------
# The output support is the target mesh where results should be evaluated. To demonstrate
# RBF mapping between non-conforming meshes, a coarser mesh is built by selecting every
# third node from the original mesh and extracting the connected elements.

original_node_ids = input_mesh.nodes.scoping.ids
coarse_node_ids = original_node_ids[::3]

coarse_node_scoping = dpf.Scoping(ids=coarse_node_ids, location=dpf.locations.nodal)
output_mesh = ops.mesh.from_scoping(
    mesh=input_mesh,
    scoping=coarse_node_scoping,
    inclusive=1,
).eval()

print("Output support (coarser mesh):")
print(output_mesh)
print(f"\nInput mesh:  {input_mesh.nodes.n_nodes} nodes, {input_mesh.elements.n_elements} elements")
print(f"Output mesh: {output_mesh.nodes.n_nodes} nodes, {output_mesh.elements.n_elements} elements")

###############################################################################
# Prepare the mapping workflow
# -----------------------------
# Call ``prepare_mapping_workflow`` to build an RBF-based
# :class:`Workflow<ansys.dpf.core.workflow.Workflow>` that maps fields from the input
# support to the output support. The filter radius controls the RBF smoothing scale.

filter_radius = 0.02

prepare_op = ops.mapping.prepare_mapping_workflow(
    input_support=input_mesh,
    output_support=output_mesh,
    filter_radius=filter_radius,
)
mapping_workflow = prepare_op.eval()
print("Generated mapping workflow:")
print(mapping_workflow)

###############################################################################
# Examine the generated workflow
# --------------------------------
# The workflow exposes a ``"source"`` input pin and a ``"target"`` output pin.

print("Workflow operator names:")
for i, name in enumerate(mapping_workflow.operator_names):
    print(f"  {i + 1}. {name}")

###############################################################################
# Map displacement using the workflow
# -------------------------------------
# Connect a displacement field to the workflow ``"source"`` pin and retrieve the
# interpolated result from the ``"target"`` pin.

displacement_fc = model.results.displacement.eval()
displacement_field = displacement_fc[0]
print("Input displacement field:")
print(displacement_field)

input_pin_name = "source"
output_pin_name = "target"

mapping_workflow.connect(pin_name=input_pin_name, inpt=displacement_field)
mapped_displacement_field = mapping_workflow.get_output(
    pin_name=output_pin_name,
    output_type=dpf.types.field,
)
print("\nMapped displacement field:")
print(mapped_displacement_field)

###############################################################################
# Compare input and output
# -------------------------
# The output field has as many entities as the output mesh has nodes.

print(f"Input field size:  {len(displacement_field.data)}")
print(f"Output field size: {len(mapped_displacement_field.data)}")
print(f"\nSample input displacement (first 3 entities):")
print(displacement_field.data[:3])
print(f"\nSample mapped displacement (first 3 entities):")
print(mapped_displacement_field.data[:3])

###############################################################################
# Reuse the workflow for a different result type
# -----------------------------------------------
# The same workflow can be reconnected to map another field type without rebuilding
# the RBF setup.

stress_fc = model.results.stress.on_location(dpf.locations.nodal).eval()
stress_field = stress_fc[0]

mapping_workflow.connect(pin_name=input_pin_name, inpt=stress_field)
mapped_stress_field = mapping_workflow.get_output(
    pin_name=output_pin_name,
    output_type=dpf.types.field,
)
print("Mapped stress field:")
print(mapped_stress_field)
print(f"\nSample mapped stress values:")
print(mapped_stress_field.data[:2])

###############################################################################
# Add the influence box parameter
# ---------------------------------
# The influence box further limits the RBF search window and can improve performance
# for sparse or asymmetric meshes.

influence_box = 0.03

prepare_op_with_box = ops.mapping.prepare_mapping_workflow(
    input_support=input_mesh,
    output_support=output_mesh,
    filter_radius=filter_radius,
    influence_box=influence_box,
)
mapping_workflow_with_box = prepare_op_with_box.eval()
print("Mapping workflow with influence box:")
print(mapping_workflow_with_box)

###############################################################################
# Effect of filter radius on mapping quality
# -------------------------------------------
# A larger filter radius produces smoother interpolation but may lose fine details.
# Compare the displacement range across several radii.

filter_radii = [0.01, 0.02, 0.04]

for radius in filter_radii:
    prep_op = ops.mapping.prepare_mapping_workflow(
        input_support=input_mesh,
        output_support=output_mesh,
        filter_radius=radius,
    )
    workflow = prep_op.eval()
    workflow.connect(pin_name=input_pin_name, inpt=displacement_field)
    result = workflow.get_output(pin_name=output_pin_name, output_type=dpf.types.field)
    mean_mag = np.mean(np.linalg.norm(result.data, axis=1))
    print(
        f"filter_radius={radius}: mapped range [{result.min().data}, {result.max().data}], "
        f"mean magnitude = {mean_mag:.6e}"
    )
