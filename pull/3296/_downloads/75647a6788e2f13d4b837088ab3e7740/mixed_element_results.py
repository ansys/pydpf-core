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
.. _ref_tutorials_mixed_element_results:

Process elemental nodal results on mixed-element meshes
=======================================================

Iterate an elemental nodal result on a mixed-element mesh and process each
element shape separately with numpy.

When a mesh combines several element types (for example ``Tet10``, ``Hex20``
and ``Quad4``), an ``ElementalNodal`` |Field| stores a different number of
rows per element because each shape uses a different storage convention
(typically the corner nodes of solids, or the nodes-times-layers of shells).
This tutorial shows how to discover the element types in bulk via the
|PropertyField| returned by |Elements|, how
:func:`get_entity_data_by_id() <ansys.dpf.core.field.Field.get_entity_data_by_id>`
exposes the variable shape per element, how to obtain a uniform per-shape
|Field| by restricting the result operator to a per-shape |Scoping| so the
data is ready for vectorised numpy operations, and how to extend a
corner-only field to the mid-side nodes of quadratic elements.
"""
###############################################################################
# Load a mixed-element result file
# --------------------------------
#
# Use the ``allKindOfComplexity`` static result file from the |Examples| module.
# This dataset contains a mesh that combines solid, shell and beam elements of
# different orders, which is what makes it useful for this tutorial.

# Import the ansys.dpf.core module as ``dpf``
import numpy as np

from ansys.dpf import core as dpf

# Import the examples and operators modules
from ansys.dpf.core import examples, operators as ops

# Create a DataSources object pointing at the result file
my_data_sources = dpf.DataSources(result_path=examples.download_all_kinds_of_complexity())

# Create a Model
my_model = dpf.Model(data_sources=my_data_sources)
print(my_model)

###############################################################################
# Discover the element types in bulk
# ----------------------------------
#
# The |Elements| helper exposes
# :attr:`element_types_field <ansys.dpf.core.elements.Elements.element_types_field>`,
# a |PropertyField| that stores the element type ID of every element in the
# mesh as an integer array. This is the recommended way to inspect the element
# composition of the mesh: it is a single server call instead of one call per
# element.
#
# Each integer value matches an entry of the
# :class:`element_types <ansys.dpf.core.elements.element_types>` enum, and the
# associated :class:`ElementDescriptor <ansys.dpf.core.element_descriptor.ElementDescriptor>`
# exposes useful properties such as ``n_nodes``, ``is_solid``, ``is_shell``,
# ``is_beam`` and ``is_quadratic``.

# Get the Elements helper from the meshed region
my_elements = my_model.metadata.meshed_region.elements

# Bulk retrieval of element type IDs as a PropertyField
el_types_pf = my_elements.element_types_field
print(el_types_pf)

# Expose the PropertyField data and the matching element IDs as numpy arrays
type_data = np.asarray(el_types_pf.data)
mesh_eids = np.asarray(el_types_pf.scoping.ids)

# Identify which element types are present in the mesh using numpy on the
# PropertyField data array, then describe each type via its descriptor
unique_type_ids = np.unique(type_data)
print(f"{'name':>12s}  n_nodes  solid  shell  beam  quadratic")
for type_id in unique_type_ids:
    type_enum = dpf.element_types(int(type_id))
    descriptor = dpf.element_types.descriptor(type_enum)
    print(
        f"{descriptor.name:>12s}  "
        f"{descriptor.n_nodes:7d}  "
        f"{str(descriptor.is_solid):>5s}  "
        f"{str(descriptor.is_shell):>5s}  "
        f"{str(descriptor.is_beam):>4s}  "
        f"{str(descriptor.is_quadratic):>9s}"
    )

###############################################################################
# Read an elemental nodal result on the mixed mesh
# ------------------------------------------------
#
# Extract the stress result at the ``elemental_nodal`` location. On a mixed
# mesh, every element of the underlying |Field| holds a different number of
# rows because each element shape has a different node count.

# Request the stress result at the elemental nodal location
stress_op = ops.result.stress(
    data_sources=my_model.metadata.data_sources,
    requested_location=dpf.locations.elemental_nodal,
)
stress_fc = stress_op.eval()
stress_field = stress_fc[0]
print(stress_field)

###############################################################################
# :func:`get_entity_data_by_id() <ansys.dpf.core.field.Field.get_entity_data_by_id>`
# returns a 2D array with shape ``(n_rows, n_components)`` for the requested
# element. The row count depends on the solver's storage convention for that
# element type: solid elements typically store stress at the corner nodes only
# (``n_corner_nodes``), while shells store stress at the nodes times the
# through-thickness layer count, so the row count does not always equal
# ``n_nodes``.

# For each element type, take one representative element from the result
# scoping (via numpy on the PropertyField data) and show its data shape
result_eids = np.asarray(stress_field.scoping.ids)
in_result = np.isin(mesh_eids, result_eids)
print(f"{'element':>9s}  {'type':>12s}  {'shape':>10s}  n_nodes  n_corner_nodes")
for type_id in unique_type_ids:
    descriptor = dpf.element_types.descriptor(dpf.element_types(int(type_id)))
    eid_candidates = mesh_eids[(type_data == int(type_id)) & in_result]
    if len(eid_candidates) == 0:
        continue
    eid = int(eid_candidates[0])
    entity_data = stress_field.get_entity_data_by_id(eid)
    print(
        f"{eid:9d}  {descriptor.name:>12s}  {str(entity_data.shape):>10s}  "
        f"{descriptor.n_nodes:7d}  {descriptor.n_corner_nodes:14d}"
    )

###############################################################################
# Get a uniform per-shape field via a per-shape scoping
# -----------------------------------------------------
#
# Iterating element by element to handle the variable row count is rarely what
# you want. To obtain a uniform per-shape result instead, build a |Scoping|
# that contains only the element IDs of one geometric element type (using a
# numpy mask on the |PropertyField| data array), then re-evaluate the result
# operator with that |Scoping| connected to its ``mesh_scoping`` input. All
# elements of the resulting |Field| then share the same row count, so the flat
# ``data`` array reshapes naturally to ``(n_elements, rows_per_element,
# n_components)`` and is ready for vectorised numpy operations.
#
# Pick the ``Tet10`` element shape (a quadratic solid) so the next step can
# demonstrate ``extend_to_mid_nodes`` on its output.

# Build a per-shape Elemental Scoping from the PropertyField data
target_descriptor = dpf.element_types.descriptor(dpf.element_types.Tet10)
target_type_id = int(dpf.element_types.Tet10.value)
target_eids = mesh_eids[type_data == target_type_id].tolist()
target_scoping = dpf.Scoping(ids=target_eids, location=dpf.locations.elemental)
print(f"Per-shape scoping: {target_descriptor.name}, {len(target_scoping.ids)} elements")

# Request the stress restricted to those elements
shape_fc = ops.result.stress(
    data_sources=my_model.metadata.data_sources,
    requested_location=dpf.locations.elemental_nodal,
    mesh_scoping=target_scoping,
).eval()
shape_field = shape_fc[0]
print(shape_field)

# Verify the row count is uniform across all elements of this shape
n_elements = len(shape_field.scoping.ids)
n_components = shape_field.component_count
total_rows = np.asarray(shape_field.data).size // n_components
rows_per_element = total_rows // n_elements
assert (
    n_elements * rows_per_element * n_components == np.asarray(shape_field.data).size
), "Per-shape field data is not uniform across elements"
print(
    f"{target_descriptor.name}: rows_per_element={rows_per_element} "
    f"(n_corner_nodes={target_descriptor.n_corner_nodes}, n_nodes={target_descriptor.n_nodes})"
)

# Reshape the flat data array to (n_elements, rows_per_element, n_components)
shape_data = np.asarray(shape_field.data).reshape(n_elements, rows_per_element, n_components)
print(f"Reshaped data: {shape_data.shape}")

# Compute the mean stress tensor over the storage rows of each element
mean_stress_per_element = shape_data.mean(axis=1)
print(f"Per-element mean stress shape: {mean_stress_per_element.shape}")

###############################################################################
# Extend a corner-only field to the mid-side nodes
# ------------------------------------------------
#
# For quadratic solids such as ``Tet10`` and ``Hex20``, the ``ElementalNodal``
# stress field above holds one row per **corner** node, not per geometric
# node. To obtain values at all geometric nodes (including the mid-side ones),
# apply the
# :class:`extend_to_mid_nodes <ansys.dpf.core.operators.averaging.extend_to_mid_nodes.extend_to_mid_nodes>`
# operator (or its
# :class:`extend_to_mid_nodes_fc <ansys.dpf.core.operators.averaging.extend_to_mid_nodes_fc.extend_to_mid_nodes_fc>`
# variant for a |FieldsContainer|). It fills the missing mid-side values by
# interpolation, so the per-element row count grows from ``n_corner_nodes`` to
# ``n_nodes``.

# Use the per-shape Tet10 field obtained above as the corner-only input
first_eid = int(shape_field.scoping.ids[0])
before_shape = shape_field.get_entity_data_by_id(first_eid).shape
print(
    f"Before extend_to_mid_nodes: element {first_eid} "
    f"({target_descriptor.name}) data shape = {before_shape} "
    f"(n_corner_nodes = {target_descriptor.n_corner_nodes})"
)

# Apply extend_to_mid_nodes_fc to fill the mid-side node values
extended_fc = ops.averaging.extend_to_mid_nodes_fc(
    fields_container=shape_fc,
    mesh=my_model.metadata.meshed_region,
).eval()
extended_field = extended_fc[0]
after_shape = extended_field.get_entity_data_by_id(first_eid).shape
print(
    f"After  extend_to_mid_nodes: element {first_eid} "
    f"({target_descriptor.name}) data shape = {after_shape} "
    f"(n_nodes = {target_descriptor.n_nodes})"
)
