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
.. _ref_tutorials_mapping_solid_to_skin:

Solid-to-skin mapping
======================

Transfer field data from a volume mesh to a surface mesh.

This tutorial demonstrates how to use the
:class:`solid_to_skin<ansys.dpf.core.operators.mapping.solid_to_skin>` operator to map
field data defined on solid (volume) elements to field data on skin (surface) elements.
This is useful for visualizing or analyzing results on the external surface of a model,
or for transferring data between different mesh representations.

The operator supports three field data locations:

- **Elemental**: Values from solid elements are copied to the overlying skin elements.
- **Nodal**: The field is rescoped to the nodes of the skin mesh.
- **ElementalNodal**: Values are copied for each element face and its associated nodes.

The example file used is a crankshaft model with 39 315 solid elements and 3 time steps.
"""

###############################################################################
# Import modules and load the model
# ----------------------------------
# Import the required modules and load a result file.

# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf

# Import the examples and operators modules
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Load model
# ----------
# Download the crankshaft result file and create a
# :class:`Model<ansys.dpf.core.model.Model>` object.
# The model contains a static structural analysis of a crankshaft with
# 39 315 solid elements and 3 time steps.

result_file = examples.download_crankshaft()
model = dpf.Model(data_sources=result_file)
print(model)

###############################################################################
# Extract the solid mesh
# -----------------------
# Retrieve the full volume mesh of the crankshaft and visualize its geometry.

solid_mesh = model.metadata.meshed_region
print(f"Total elements: {solid_mesh.elements.n_elements}")
print(f"Total nodes:    {solid_mesh.nodes.n_nodes}")
solid_mesh.plot(title="Crankshaft solid mesh")

###############################################################################
# Create the skin mesh
# --------------------
# Build a skin mesh representing the external surface of the model using the
# ``skin`` operator. Unlike ``external_layer``, the ``skin`` operator includes
# the ``facets`` and ``facets_to_ele`` property fields that link each surface
# element back to its parent solid element—these are required by ``solid_to_skin``.

skin_mesh_op = ops.mesh.skin(mesh=solid_mesh)
skin_mesh = skin_mesh_op.outputs.mesh()
print(f"Skin elements:  {skin_mesh.elements.n_elements}")
print(f"Solid elements: {solid_mesh.elements.n_elements}")
print(f"Skin nodes:     {skin_mesh.nodes.n_nodes}")
print(f"Solid nodes:    {solid_mesh.nodes.n_nodes}")
skin_mesh.plot(title="Crankshaft skin mesh")

###############################################################################
# Map elemental stress to the skin mesh
# ---------------------------------------
# Retrieve element-averaged stress on the solid mesh and transfer it to skin elements.
# The result is evaluated at the last available time step (time set 3).

stress_elemental_fc = model.results.stress.on_location(dpf.locations.elemental).eval()
stress_elemental_field = stress_elemental_fc[0]

mapped_stress_op = ops.mapping.solid_to_skin(
    field=stress_elemental_field,
    mesh=skin_mesh,
    solid_mesh=solid_mesh,
)
mapped_stress_field = mapped_stress_op.eval()
print(
    f"Solid elements: {len(stress_elemental_field.data)}, skin elements: {len(mapped_stress_field.data)}"
)
skin_mesh.plot(
    field_or_fields_container=mapped_stress_field, title="Elemental stress on crankshaft skin"
)

###############################################################################
# Map nodal displacement to the skin mesh
# ----------------------------------------
# Transfer nodal displacement from the solid mesh to the skin mesh. The field is
# rescoped to the nodes that belong to the skin mesh.

displacement_fc = model.results.displacement.eval()
displacement_field = displacement_fc[0]

mapped_displacement_op = ops.mapping.solid_to_skin(
    field=displacement_field,
    mesh=skin_mesh,
    solid_mesh=solid_mesh,
)
mapped_displacement_field = mapped_displacement_op.eval()
print(
    f"Solid nodes: {len(displacement_field.scoping)}, skin nodes: {len(mapped_displacement_field.scoping)}"
)
skin_mesh.plot(
    field_or_fields_container=mapped_displacement_field,
    title="Nodal displacement on crankshaft skin",
)

###############################################################################
# Map elemental-nodal stress to the skin mesh
# --------------------------------------------
# For ``ElementalNodal`` data, values are copied for each skin element face
# together with its associated nodes.

stress_en_fc = model.results.stress.on_location(dpf.locations.elemental_nodal).eval()
stress_en_field = stress_en_fc[0]

mapped_stress_en_field = ops.mapping.solid_to_skin(
    field=stress_en_field,
    mesh=skin_mesh,
    solid_mesh=solid_mesh,
).eval()
skin_mesh.plot(
    field_or_fields_container=mapped_stress_en_field,
    title="ElementalNodal stress on crankshaft skin",
)

###############################################################################
# Omit the solid mesh when it is available from the field support
# ---------------------------------------------------------------
# If the field already carries its supporting mesh, the ``solid_mesh`` pin can
# be omitted—the operator reads it directly from the field support.

stress_fc = model.results.stress.eval()
stress_field_solid = stress_fc[0]

mapped_stress_simple = ops.mapping.solid_to_skin(
    field=stress_field_solid,
    mesh=skin_mesh,
).eval()
skin_mesh.plot(
    field_or_fields_container=mapped_stress_simple,
    title="Stress mapped to skin (mesh from field support)",
)

###############################################################################
# Use with FieldsContainer
# -------------------------
# The operator also accepts a
# :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
# containing a single field.
# This is useful when your workflow already produces a ``FieldsContainer``
# (for example, from a preceding operator) and you want to pass it directly.

# Retrieve all three time steps and pick the first one
stress_fc_all = model.results.stress.on_all_time_freqs().eval()
stress_field_t1 = stress_fc_all[0]

single_field_fc = dpf.FieldsContainer()
single_field_fc.labels = ["time"]
single_field_fc.add_field(label_space={"time": 1}, field=stress_field_t1)

mapped_fc = ops.mapping.solid_to_skin(
    field=single_field_fc,
    mesh=skin_mesh,
    solid_mesh=solid_mesh,
).eval()
skin_mesh.plot(
    field_or_fields_container=mapped_fc,
    title="Stress at time step 1 mapped from FieldsContainer",
)
