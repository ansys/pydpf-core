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

"""
.. _ref_tutorials_collections:

DPF Collections
===============

This tutorial demonstrates how to create and work with some DPF collections:
:class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`,
:class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`, and
:class:`ScopingsContainer <ansys.dpf.core.scopings_container.ScopingsContainer>`.

You can store DPF entities of a given type as a DPF collection and further categorize them
according to labels and associated values, which allows you to organize and keep track of data.
Collections are essential for handling multiple time steps, frequency sets, or other labeled
datasets in your analysis workflows.

What You'll Learn
-----------------

This tutorial covers the following topics:

- Working with :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`:
  Extract results across time steps, access individual fields, and create custom containers
  with multiple labels
- Working with :class:`ScopingsContainer <ansys.dpf.core.scopings_container.ScopingsContainer>`:
  Create and manage selections, and use them with operators for targeted result extraction
- Working with :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`:
  Store and organize multiple mesh variations or time-dependent meshes
- Collection operations: Iterate through collections, filter by labels, and access metadata
- Advanced usage: Learn about other built-in collection types and create custom collections
  using the collection factory

By the end of this tutorial, you'll have a basic understanding of how to effectively organize
and manipulate DPF data using collections in your analysis workflows.

Introduction to Collections
----------------------------

Collections in DPF serve as containers that group related objects with labels.
The main collection types are:

- :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`:
  A collection of :class:`Field<ansys.dpf.core.field.Field>` objects, typically representing
  results over multiple time steps or frequency sets
- :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`:
  A collection of :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>` objects
  for different cases or time steps
- :class:`ScopingsContainer <ansys.dpf.core.scopings_container.ScopingsContainer>`:
  A collection of :class:`Scoping <ansys.dpf.core.scoping.Scoping>` objects for organizing
  entity selections

Each collection provides methods to:

- Add, retrieve, and iterate over contained objects
- Access objects by label (time, frequency, set ID, and so on)
- Perform operations across all contained objects

Collections are used in DPF workflows to provide operators with vectorized data,
allowing you to process the data in bulk or to process it in parallel whenever possible.

The LabelSpace
^^^^^^^^^^^^^^

DPF collections use **labels** to categorize and organize contained objects.
Labels can be thought of as categories or dimensions along which the objects in the collection
are organized. Each object in the collection is associated with an integer value for every
label/category/dimension of the collection.

A **LabelSpace** is a dictionary of one or more labels (e.g., ``"time"``, ``"frequency"``,
``"set ID"``), each associated with specific values. It is used to identify and access the
objects within the collection. It can be partial and target multiple objects in the collection,
or it can be complete and define a value for each label of the collection, resulting in a
unique object. It is similar to multi-dimensional indexing in arrays or dataframes, or to a
filter or query in databases.

Here are some examples:

- A collection of fields (a
  :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`) across time uses
  the label **time** with each field associated to a **time** integer value (the time step ID).
  The **LabelSpace** ``{"time": 3}`` would uniquely identify the field for time step 3.
- A collection of fields across frequency and stage uses the labels **frequency** and **stage**.
  The **LabelSpace** ``{"frequency": 2, "stage": 1}`` would uniquely identify the field for
  frequency ID 2 at stage ID 1.
- A collection of meshes (a
  :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`) across different
  parts, further split by element type, uses the labels **part** and **element_type**.
  The **LabelSpace** ``{"part": 2, "element_type": 1}`` would uniquely identify the mesh for
  part 2 with element type code 1.
- A collection of scopings (a
  :class:`ScopingsContainer <ansys.dpf.core.scopings_container.ScopingsContainer>`) across
  different fluid zones for a transient analysis uses the labels **zone** and **time**.
  The **LabelSpace** ``{"zone": 1}`` would identify the collection of scopings for zone 1
  only, for all time steps.
"""

###############################################################################
# Load an example file
# --------------------
#
# Import the required modules and load a transient analysis result file.
# A transient analysis is a typical example where collections are useful,
# as data is available at multiple time steps.

import ansys.dpf.core as dpf
from ansys.dpf.core import examples

# Load a transient analysis with multiple time steps
result_file_path = examples.find_msup_transient()

# Create a DataSources object
data_sources = dpf.DataSources(result_path=result_file_path)

# Create a Model from the data sources
model = dpf.Model(data_sources=data_sources)

# Display basic model information
print(model)

###############################################################################
# Working with FieldsContainer
# ----------------------------
#
# A :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>` is the most
# commonly used collection in DPF. It stores multiple
# :class:`Field<ansys.dpf.core.field.Field>` objects, each associated with a label such as
# time step or frequency.
#
# Extract results into a FieldsContainer
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Extract displacement results for all time steps, which automatically creates a
# :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`.

# Get displacement results for all time steps
displacement_fc = model.results.displacement.on_all_time_freqs.eval()

# Display FieldsContainer information
print(displacement_fc)

###############################################################################
# Access individual fields
# ^^^^^^^^^^^^^^^^^^^^^^^^
#
# You can access individual fields by their label or index.

# Access field by index (first time step)
first_field = displacement_fc[0]
print("First field info:")
print(first_field)

# Access field by label (specific time step)
second_time_field = displacement_fc.get_field({"time": 2})
# Equivalent to:
second_time_field = displacement_fc.get_field_by_time_id(2)
print("\nSecond time step field:")
print(second_time_field)

###############################################################################
# Create a custom FieldsContainer
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# You can create your own
# :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>` and add fields
# with custom labels.

# Create an empty FieldsContainer
custom_fc = dpf.FieldsContainer()

# Set up labels for the container
custom_fc.labels = ["time", "zone"]

# Create sample fields for different time steps and zones
field1 = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)
field2 = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)
field3 = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)
field4 = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)

# Add some sample nodes and data
field1.scoping.ids = [1, 2, 3, 4, 5]
field1.data = [float(1 * i) for i in range(1, 6)]
field2.scoping.ids = [1, 2, 3, 4, 5]
field2.data = [float(2 * i) for i in range(1, 6)]
field3.scoping.ids = [1, 2, 3, 4, 5]
field3.data = [float(3 * i) for i in range(1, 6)]
field4.scoping.ids = [1, 2, 3, 4, 5]
field4.data = [float(4 * i) for i in range(1, 6)]

# Add fields to the container with their label spaces
custom_fc.add_field({"time": 1, "zone": 1}, field1)
custom_fc.add_field({"time": 2, "zone": 1}, field2)
custom_fc.add_field({"time": 1, "zone": 2}, field3)
custom_fc.add_field({"time": 2, "zone": 2}, field4)

# Display the custom FieldsContainer
print(custom_fc)

###############################################################################
# Working with ScopingsContainer
# --------------------------------
#
# A :class:`ScopingsContainer <ansys.dpf.core.scopings_container.ScopingsContainer>` holds
# multiple :class:`Scoping <ansys.dpf.core.scoping.Scoping>` objects, which define sets of
# entity IDs (nodes, elements, etc.).
#
# Create and populate a ScopingsContainer
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Create different node selections and organize them in a
# :class:`ScopingsContainer <ansys.dpf.core.scopings_container.ScopingsContainer>`.

# Get the mesh from our model
mesh = model.metadata.meshed_region

# Create a ScopingsContainer
scopings_container = dpf.ScopingsContainer()

# Set labels for different selections
scopings_container.labels = ["selection_type"]

# Selection 0: First 10 nodes
first_nodes = dpf.Scoping(location=dpf.locations.nodal)
first_nodes.ids = list(range(1, 11))
scopings_container.add_scoping(label_space={"selection_type": 0}, scoping=first_nodes)

# Selection 1: Every 10th node (sample)
all_node_ids = mesh.nodes.scoping.ids
every_tenth = dpf.Scoping(location=dpf.locations.nodal)
every_tenth.ids = all_node_ids[::10]
scopings_container.add_scoping(label_space={"selection_type": 1}, scoping=every_tenth)

# Selection 2: Last 10 nodes
last_nodes = dpf.Scoping(location=dpf.locations.nodal)
last_nodes.ids = all_node_ids[-10:]
scopings_container.add_scoping(label_space={"selection_type": 2}, scoping=last_nodes)

# Display ScopingsContainer information
print(scopings_container)

###############################################################################
# Use ScopingsContainer with operators
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# :class:`ScopingsContainer <ansys.dpf.core.scopings_container.ScopingsContainer>` objects
# can be connected to operator inputs to apply operations to multiple selections at once.

# Create a displacement operator
displacement_op = dpf.operators.result.displacement()
# Connect the data source
displacement_op.inputs.data_sources(data_sources)
# Connect the scopings container which defines the node selections
displacement_op.inputs.mesh_scoping(scopings_container)

# Evaluate to get results for all scopings
scoped_displacements = displacement_op.eval()

print("Displacement results for different node selections:")
print(scoped_displacements)

###############################################################################
# Working with MeshesContainer
# ----------------------------
#
# A :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>` stores
# multiple :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>` objects.
# This is useful when working with different mesh variations or time-dependent meshes.
#
# Create a MeshesContainer
# ^^^^^^^^^^^^^^^^^^^^^^^^
#
# Create a :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>` with
# mesh data for different cases.

# Create a MeshesContainer
meshes_container = dpf.MeshesContainer()

# Set labels for different mesh variations
meshes_container.labels = ["variation"]

# Get the original mesh
original_mesh = model.metadata.meshed_region

# Add the original mesh
meshes_container.add_mesh({"variation": 0}, original_mesh)

# Get element scoping for the first half of elements to create a subset mesh
all_element_ids = original_mesh.elements.scoping.ids
subset_element_ids = all_element_ids[: len(all_element_ids) // 2]

# Create element scoping for the subset
element_scoping = dpf.Scoping(location=dpf.locations.elemental)
element_scoping.ids = subset_element_ids

# Extract the subset mesh using an operator
mesh_extract_op = dpf.operators.mesh.from_scoping()
mesh_extract_op.inputs.mesh(original_mesh)
mesh_extract_op.inputs.scoping(element_scoping)
subset_mesh = mesh_extract_op.eval()

# Add the subset mesh to the container
meshes_container.add_mesh({"variation": 1}, subset_mesh)

# Display MeshesContainer information
print(meshes_container)

###############################################################################
# Collection operations and iteration
# -------------------------------------
#
# Collections support various operations for data manipulation and analysis.
#
# Iterate through collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# You can iterate through collections using different methods.

# Iterate through a FieldsContainer by index
print("Iterating through displacement fields by index:")
for i in range(3):  # Show the first three fields in the collection
    field = displacement_fc[i]
    label_space = displacement_fc.get_label_space(i)
    max_value = field.data.max()
    print(f"  Field {i}: {label_space}, max value: {max_value:.6f}")

# Enumerate the scopings in a ScopingsContainer
print("\nEnumerate the scopings in a ScopingsContainer:")
for i, scoping in enumerate(scopings_container):
    label_space = scopings_container.get_label_space(i)
    print(f"  Scoping {i}: {label_space}, size: {scoping.size}")

###############################################################################
# Filter and select from collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# You can filter collections based on label values to retrieve subsets of items.

# Get all fields from custom_fc where zone=1
zone_1_fields = custom_fc.get_fields({"zone": 1})
print("Fields in custom_fc with zone=1:")
for field in zone_1_fields:
    print(field)

###############################################################################
# Other built-in collection types
# ---------------------------------
#
# DPF provides several built-in collection types for common DPF objects:
#
# - :class:`ansys.dpf.core.fields_container.FieldsContainer` for fields
# - :class:`ansys.dpf.core.meshes_container.MeshesContainer` for meshes
# - :class:`ansys.dpf.core.scopings_container.ScopingsContainer` for scopings
#
# Additionally, the following specialized collection types are available:
#
# - :class:`ansys.dpf.core.collection_base.IntegralCollection` for integral types
# - :class:`ansys.dpf.core.collection_base.IntCollection` for integers
# - :class:`ansys.dpf.core.collection_base.FloatCollection` for floats
# - :class:`ansys.dpf.core.collection_base.StringCollection` for strings
#
# These built-in collections are optimized for their respective DPF types and should be
# preferred when working with fields, meshes, scopings, or basic types.
# For other supported types, you can use the
# :py:meth:`ansys.dpf.core.collection.Collection.collection_factory` method to create a
# custom collection class at runtime.

###############################################################################
# Using the collection factory
# ----------------------------
#
# .. note::
#
#    Collections can only be made for types supported by DPF. Attempting to use unsupported
#    or arbitrary Python types will result in an error.
#
# The :py:meth:`ansys.dpf.core.collection.Collection.collection_factory` method allows you
# to create a collection class for any supported DPF type at runtime. This is useful when you
# want to group and manage objects that are not covered by the built-in collection types.
#
# For example, you can create a collection of
# :class:`DataSources<ansys.dpf.core.data_sources.DataSources>` objects:

from ansys.dpf.core.collection import Collection

# Create a collection class for DataSources at runtime
DataSourcesCollection = Collection.collection_factory(dpf.DataSources)
ds_collection = DataSourcesCollection()
ds_collection.labels = ["case"]

# Add DataSources objects to the collection (paths are illustrative)
ds1 = dpf.DataSources("path/to/first/result/file.rst")
ds2 = dpf.DataSources("path/to/second/result/file.rst")
ds_collection.add_entry({"case": 0}, ds1)
ds_collection.add_entry({"case": 1}, ds2)

# Display the collection
print(ds_collection)
