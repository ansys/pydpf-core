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

When a mesh combines several element types (for example ``Tet4``, ``Hex20`` and
``Quad4``), an ``ElementalNodal`` |Field| has a different number of rows per
element because each shape has a different node count. This tutorial shows how
to discover the element types in bulk via the |PropertyField| returned by
|Elements|, how :func:`get_entity_data_by_id() <ansys.dpf.core.field.Field.get_entity_data_by_id>`
exposes the variable shape per element, how to split the result by element
shape into a uniform per-shape |FieldsContainer| ready for numpy operations,
and how to extend a corner-only field to the mid-side nodes of quadratic
elements.
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
# returns a 2D array with shape ``(n_integration_nodes, n_components)`` for the
# requested element. On a mixed mesh, the row count of the returned array
# matches the ``n_nodes`` of that element's type.

# For each element type, take one representative element from the result
# scoping (via numpy on the PropertyField data) and show its data shape
result_eids = np.asarray(stress_field.scoping.ids)
in_result = np.isin(mesh_eids, result_eids)
print(f"{'element':>9s}  {'type':>12s}  {'shape':>10s}  expected n_nodes")
for type_id in unique_type_ids:
    descriptor = dpf.element_types.descriptor(dpf.element_types(int(type_id)))
    eid_candidates = mesh_eids[(type_data == int(type_id)) & in_result]
    if len(eid_candidates) == 0:
        continue
    eid = int(eid_candidates[0])
    entity_data = stress_field.get_entity_data_by_id(eid)
    print(
        f"{eid:9d}  {descriptor.name:>12s}  {str(entity_data.shape):>10s}  " f"{descriptor.n_nodes}"
    )

###############################################################################
# Split the result by element shape
# ---------------------------------
#
# Iterating element by element to handle the variable row count is rarely what
# you want. Many result operators expose a ``split_shells`` boolean input that
# splits the output |FieldsContainer| by element shape. When ``split_shells``
# is ``True``, the output container carries an additional ``elshape`` label and
# holds one |Field| per element shape. Within each per-shape sub-field, every
# element has the same node count, so the flat ``data`` array reshapes
# naturally to ``(n_elements, n_nodes, n_components)`` and is ready for
# vectorised numpy operations.

# Request the same stress result split by element shape
stress_per_shape_op = ops.result.stress(
    data_sources=my_model.metadata.data_sources,
    requested_location=dpf.locations.elemental_nodal,
    split_shells=True,
)
stress_per_shape_fc = stress_per_shape_op.eval()
print(stress_per_shape_fc)

###############################################################################
# Pick one per-shape sub-field and run a vectorised numpy operation on it. For
# each element of that shape, compute the mean stress over its integration
# nodes - a single reshape plus one ``mean`` call replaces a per-element loop.

# Get the first sub-field (one element shape) and its descriptor
shape_field = stress_per_shape_fc[0]
shape_label = stress_per_shape_fc.get_label_scoping("elshape").ids[0]
shape_descriptor = dpf.element_types.descriptor(dpf.element_types(int(shape_label)))
print(f"Working on shape: {shape_descriptor.name} (n_nodes={shape_descriptor.n_nodes})")
print(shape_field)

# Reshape the flat data array to (n_elements, n_nodes, n_components)
n_elements = len(shape_field.scoping.ids)
n_components = shape_field.component_count
shape_data = np.asarray(shape_field.data).reshape(
    n_elements, shape_descriptor.n_nodes, n_components
)
print(f"Reshaped data: {shape_data.shape}")

# Compute the mean stress tensor over the integration nodes of each element
mean_stress_per_element = shape_data.mean(axis=1)
print(f"Per-element mean stress shape: {mean_stress_per_element.shape}")

###############################################################################
# Extend a corner-only field to the mid-side nodes
# ------------------------------------------------
#
# Some workflows produce an ``ElementalNodal`` field that only holds values at
# the corner nodes of quadratic elements (for example, projecting a nodal
# result back to the element nodes without copying the mid-side values). The
# :class:`extend_to_mid_nodes <ansys.dpf.core.operators.averaging.extend_to_mid_nodes.extend_to_mid_nodes>`
# operator (or its
# :class:`extend_to_mid_nodes_fc <ansys.dpf.core.operators.averaging.extend_to_mid_nodes_fc.extend_to_mid_nodes_fc>`
# variant for a |FieldsContainer|) fills those missing mid-side values by
# interpolation, so the field becomes consistent with the geometric node count
# of the elements.
#
# To set up a clean demonstration, project the nodal von Mises stress back to
# ``ElementalNodal`` with
# :class:`nodal_to_elemental_nodal_fc <ansys.dpf.core.operators.averaging.nodal_to_elemental_nodal_fc.nodal_to_elemental_nodal_fc>`
# and ``extend_to_mid_nodes=False``. Then call ``extend_to_mid_nodes`` on a
# quadratic per-shape sub-field and observe the per-element row count growing
# from ``n_corner_nodes`` to ``n_nodes``.

# Extract a nodal scalar result (von Mises stress at nodes)
vm_op = ops.result.stress_von_mises(
    data_sources=my_model.metadata.data_sources,
    requested_location=dpf.locations.nodal,
)
vm_nodal_fc = vm_op.eval()

# Project the nodal result back to elemental nodal on corner nodes only
corner_only_fc = ops.averaging.nodal_to_elemental_nodal_fc(
    fields_container=vm_nodal_fc,
    mesh=my_model.metadata.meshed_region,
    extend_to_mid_nodes=False,
).eval()
corner_only_field = corner_only_fc[0]

# Pick one quadratic element from the corner-only field via numpy filtering
quadratic_descriptor = None
quadratic_eid = None
corner_only_eids = np.asarray(corner_only_field.scoping.ids)
in_corner_only = np.isin(mesh_eids, corner_only_eids)
for type_id in unique_type_ids:
    descriptor = dpf.element_types.descriptor(dpf.element_types(int(type_id)))
    if not descriptor.is_quadratic:
        continue
    candidates = mesh_eids[(type_data == int(type_id)) & in_corner_only]
    if len(candidates) > 0:
        quadratic_descriptor = descriptor
        quadratic_eid = int(candidates[0])
        break

if quadratic_eid is None:
    print("No quadratic element shape found in this dataset.")
else:
    # Show the row count of the chosen element before extension
    before_shape = corner_only_field.get_entity_data_by_id(quadratic_eid).shape
    print(
        f"Before extend_to_mid_nodes: element {quadratic_eid} "
        f"({quadratic_descriptor.name}) data shape = {before_shape} "
        f"(n_corner_nodes = {quadratic_descriptor.n_corner_nodes})"
    )

    # Apply extend_to_mid_nodes to fill the mid-side node values
    extended_field = ops.averaging.extend_to_mid_nodes(
        field=corner_only_field,
        mesh=my_model.metadata.meshed_region,
    ).eval()
    after_shape = extended_field.get_entity_data_by_id(quadratic_eid).shape
    print(
        f"After  extend_to_mid_nodes: element {quadratic_eid} "
        f"({quadratic_descriptor.name}) data shape = {after_shape} "
        f"(n_nodes = {quadratic_descriptor.n_nodes})"
    )
