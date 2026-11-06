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
# Import Matplotlib for plotting
import matplotlib.pyplot as plt

from ansys.dpf import core as dpf

# Import the examples and operators modules
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Load model
# ----------
# Download the crankshaft result file and create a
# :class:`Model<ansys.dpf.core.model.Model>` object.

result_file = examples.download_crankshaft()
model = dpf.Model(data_sources=result_file)
print(model)

###############################################################################
# Define the input support
# ------------------------
# The input support is the mesh from which results will be mapped. Use
# :meth:`bounding_box<ansys.dpf.core.meshed_region.MeshedRegion.bounding_box>`
# to inspect the spatial extent of the crankshaft before choosing a filter radius.

input_mesh = model.metadata.meshed_region
bb_data = input_mesh.bounding_box.data[0]  # [xmin, ymin, zmin, xmax, ymax, zmax]
print(
    f"Bounding box: x=[{bb_data[0]:.4f}, {bb_data[3]:.4f}] "
    f"y=[{bb_data[1]:.4f}, {bb_data[4]:.4f}] "
    f"z=[{bb_data[2]:.4f}, {bb_data[5]:.4f}] m"
)

###############################################################################
# Define the output support
# --------------------------
# The output support is the target mesh onto which results will be mapped.
# To demonstrate RBF mapping between non-conforming meshes with genuinely
# different topologies, the output mesh is built in two steps:
#
# 1. Extract the external surface of the crankshaft using the ``skin`` operator.
# 2. Decimate that surface to ~30 % of its original faces using
#    :class:`decimate_mesh<ansys.dpf.core.operators.mesh.decimate_mesh>`,
#    which produces a coarser triangulated mesh.
#
# This gives a source (solid, hexahedral) / target (surface, triangulated)
# pair with entirely different topology — exactly the scenario RBF-based
# mapping is designed for.

skin_mesh = ops.mesh.skin(mesh=input_mesh).outputs.mesh()
output_mesh = ops.mesh.decimate_mesh(
    mesh=skin_mesh,
    preservation_ratio=0.3,
).outputs.mesh()

print(
    f"Source mesh:          {input_mesh.nodes.n_nodes} nodes, {input_mesh.elements.n_elements} elements (solid)"
)
print(
    f"Skin mesh:            {skin_mesh.nodes.n_nodes} nodes, {skin_mesh.elements.n_elements} elements (surface)"
)
print(
    f"Decimated target mesh:{output_mesh.nodes.n_nodes} nodes, {output_mesh.elements.n_elements} elements (triangles)"
)
input_mesh.plot(title="Source mesh (crankshaft solid)")
output_mesh.plot(title="Target mesh (decimated surface)")

###############################################################################
# Prepare the mapping workflow
# -----------------------------
# Call ``prepare_mapping_workflow`` to build an RBF-based
# :class:`Workflow<ansys.dpf.core.workflow.Workflow>` that maps fields from the input
# support to the output support. The filter radius controls the RBF smoothing scale.
# A value of 5 mm (0.005 m) is appropriate for the crankshaft which spans ~60 mm
# in its narrowest dimension.

filter_radius = 0.005

prepare_op = ops.mapping.prepare_mapping_workflow(
    input_support=input_mesh,
    output_support=output_mesh,
    filter_radius=filter_radius,
)
mapping_workflow = prepare_op.eval()
mapping_workflow.progress_bar = False
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
input_mesh.plot(field_or_fields_container=displacement_fc, title="Source displacement (crankshaft)")

input_pin_name = "source"
output_pin_name = "target"

mapping_workflow.connect(pin_name=input_pin_name, inpt=displacement_field)
mapped_displacement_field = mapping_workflow.get_output(
    pin_name=output_pin_name,
    output_type=dpf.types.field,
)
output_mesh.plot(
    field_or_fields_container=mapped_displacement_field,
    title="Mapped displacement on decimated surface",
)

print(f"Source field:  {len(displacement_field.data)} entities (solid nodes)")
print(f"Mapped field:  {len(mapped_displacement_field.data)} entities (surface nodes)")

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
output_mesh.plot(
    field_or_fields_container=mapped_stress_field, title="Mapped stress on decimated surface"
)

###############################################################################
# Add the influence box parameter
# ---------------------------------
# The influence box further limits the RBF search window and can improve performance
# for sparse or asymmetric meshes.

influence_box = 0.01

prepare_op_with_box = ops.mapping.prepare_mapping_workflow(
    input_support=input_mesh,
    output_support=output_mesh,
    filter_radius=filter_radius,
    influence_box=influence_box,
)
mapping_workflow_with_box = prepare_op_with_box.eval()
mapping_workflow_with_box.progress_bar = False
mapping_workflow_with_box.connect(pin_name=input_pin_name, inpt=displacement_field)
mapped_disp_with_box = mapping_workflow_with_box.get_output(
    pin_name=output_pin_name, output_type=dpf.types.field
)
output_mesh.plot(
    field_or_fields_container=mapped_disp_with_box,
    title="Mapped displacement with influence box (decimated surface)",
)

###############################################################################
# Effect of filter radius on mapping quality
# -------------------------------------------
# A larger filter radius produces smoother interpolation but may lose fine details.
# Compare the displacement range across several radii.
#
# A reference value is first obtained by running the mapping without setting
# ``filter_radius``, so the operator uses its built-in default.  The swept
# values are then plotted against this untuned baseline.

ref_prep_op = ops.mapping.prepare_mapping_workflow(
    input_support=input_mesh,
    output_support=output_mesh,
)
ref_workflow: dpf.Workflow = ref_prep_op.eval()
ref_workflow.progress_bar = False
ref_workflow.connect(pin_name=input_pin_name, inpt=displacement_field)
ref_result = ref_workflow.get_output(pin_name=output_pin_name, output_type=dpf.types.field)

filter_radii = [0.001, 0.003, 0.006, 0.01, 0.02, 0.03, 0.04, 0.05]

mean_mags = []
min_mags = []
max_mags = []
for radius in filter_radii:
    prep_op = ops.mapping.prepare_mapping_workflow(
        input_support=input_mesh,
        output_support=output_mesh,
        filter_radius=radius,
    )
    workflow: dpf.Workflow = prep_op.eval()
    workflow.connect(pin_name=input_pin_name, inpt=displacement_field)
    workflow.progress_bar = False
    result = workflow.get_output(pin_name=output_pin_name, output_type=dpf.types.field)
    norm_field = ops.math.norm(field=result).outputs.field()
    min_max_op = ops.min_max.min_max(field=norm_field)
    min_mags.append(min_max_op.outputs.field_min().data[0])
    max_mags.append(min_max_op.outputs.field_max().data[0])
    mean_mags.append(
        ops.math.accumulate(fieldA=norm_field).outputs.field().data[0] / norm_field.scoping.size
    )

ref_norm_field = ops.math.norm(field=ref_result).outputs.field()
ref_min_max_op = ops.min_max.min_max(field=ref_norm_field)
ref_min_mag = ref_min_max_op.outputs.field_min().data[0]
ref_max_mag = ref_min_max_op.outputs.field_max().data[0]
reference_mean_mag = (
    ops.math.accumulate(fieldA=ref_norm_field).outputs.field().data[0] / ref_norm_field.scoping.size
)
print(f"Reference mean displacement magnitude (no filter_radius set): {reference_mean_mag:.4e} m")

fig, ax = plt.subplots()
ax.fill_between(filter_radii, min_mags, max_mags, alpha=0.2, label="Min-max range")
ax.plot(filter_radii, mean_mags, "o-", label="Mean magnitude")
ax.plot(filter_radii, min_mags, "v--", color="tab:blue", alpha=0.6, label="Min magnitude")
ax.plot(filter_radii, max_mags, "^--", color="tab:blue", alpha=0.6, label="Max magnitude")
ax.axhline(
    reference_mean_mag,
    color="gray",
    linestyle="-",
    label=f"Default - mean ({reference_mean_mag:.2e} m)",
)
ax.axhline(ref_min_mag, color="gray", linestyle=":", label=f"Default - min ({ref_min_mag:.2e} m)")
ax.axhline(ref_max_mag, color="gray", linestyle=":", label=f"Default - max ({ref_max_mag:.2e} m)")
ax.set_xlabel("Filter radius (m)")
ax.set_ylabel("Displacement magnitude (m)")
ax.set_title(
    "Effect of filter radius on mapped displacement\n(narrowing min-max band = loss of fine detail)"
)
ax.legend(fontsize="small")
plt.tight_layout()
plt.show()
