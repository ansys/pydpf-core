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
.. _ref_tutorials_data_arrays:

Data Arrays
===========

To process your data with DPF, you must format it according to the DPF data model.
You can achieve this either by using DPF data readers on result files, or by using
data to build DPF data storage containers.

It is important to be aware of how the data is structured in those containers to understand
how to create them and how operators process them.

The data containers can be:

  - **Raw data storage structures**: data arrays (such as a :class:`Field <ansys.dpf.core.field.Field>`) or data maps (such as a ``DataTree``)
  - **Collections**: homogeneous groups of labeled raw data storage structures (such as a :class:`FieldsContainer <ansys.dpf.core.fields_container.FieldsContainer>` for a group of labeled fields)

This tutorial presents how to define and manipulate DPF data arrays specifically.
"""
###############################################################################
# Introduction
# ------------
#
# A data array in DPF usually represents a mathematical field, hence the base name :class:`Field <ansys.dpf.core.field.Field>`.
#
# Different types of :class:`Field <ansys.dpf.core.field.Field>` store different data types:
#
#   - a :class:`Field <ansys.dpf.core.field.Field>` stores float values
#   - a :class:`StringField <ansys.dpf.core.string_field.StringField>` stores string values
#   - a :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>` stores integer values
#   - a :class:`CustomTypeField <ansys.dpf.core.custom_type_field.CustomTypeField>` stores values of a custom type (among valid ``numpy.dtype``)
#
# A :class:`Field <ansys.dpf.core.field.Field>` is always associated to:
#
#   - a ``location``, which defines the type of entity the data applies to.
#     Check the :class:`locations <ansys.dpf.core.common.locations>` list to know what is available.
#     Locations related to mesh entities include: ``nodal``, ``elemental``, ``elemental_nodal``,
#     ``zone``, and ``faces``. Locations related to time, frequency, or mode are ``modal``,
#     ``time_freq``, and ``time_freq_step``.
#
#   - a ``scoping``, which is the list of entity IDs each data point in the :class:`Field <ansys.dpf.core.field.Field>` relates to.
#     For example, the ``scoping`` of a ``nodal`` :class:`Field <ansys.dpf.core.field.Field>` represents a list of node IDs.
#     It can represent a subset of the ``support`` of the field.
#     The data in a :class:`Field <ansys.dpf.core.field.Field>` is ordered the same way as the IDs in its ``scoping``.
#
#   - a ``support``, which is a data container holding information about the model for the type
#     of entity the ``location`` targets. If the ``location`` relates to mesh entities such as
#     nodes or elements, the ``support`` of the :class:`Field <ansys.dpf.core.field.Field>` is a :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`.
#
#   - a ``dimensionality``, which gives the structure of the data based on the number of
#     components and dimensions. A DPF :class:`Field <ansys.dpf.core.field.Field>` can store data for a 3D vector field, a scalar
#     field, a matrix field, or a multi-component field (for example, a symmetrical matrix field
#     for each component of the stress field).
#
#   - a ``data`` array, which holds the actual data in a vector, accessed according to the
#     ``dimensionality``.

###############################################################################
# Create fields based on result files
# ------------------------------------
#
# In this section we use the result file from a fluid analysis to showcase the
# :class:`Field <ansys.dpf.core.field.Field>`, :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`, and :class:`StringField <ansys.dpf.core.string_field.StringField>`.
#
# The :class:`Model <ansys.dpf.core.model.Model>` class creates and evaluates common readers
# for the files it is given, such as a mesh provider, a result info provider, and a streams
# provider. It provides dynamically built methods to extract the results available in the
# files, as well as many shortcuts to facilitate exploration of the available data.

# Import the ansys.dpf.core module as ``dpf``
from ansys.dpf import core as dpf

# Import the examples module
from ansys.dpf.core import examples

# Create a data source targeting the example file
my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
# Create a model from the data source
my_model = dpf.Model(data_sources=my_data_sources)
# Print information available for the analysis
print(my_model)

###############################################################################
# The :class:`MeshInfo <ansys.dpf.core.mesh_info.MeshInfo>` class stores information relative to the :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>` of the analysis.
# It stores some of its data as fields of strings or fields of integers, which we extract next.

# Get the mesh metadata
my_mesh_info = my_model.metadata.mesh_info
print(my_mesh_info)

###############################################################################
# The following shows how to obtain the three field types from an existing analysis.
#
# Field
# ^^^^^
#
# You can obtain a :class:`Field <ansys.dpf.core.field.Field>` from a model by requesting a
# result. The field is located on nodes since it stores the temperature at each node.

# Request the collection of temperature result fields from the model and take the first one.
my_temp_field = my_model.results.temperature.eval()[0]
print(my_temp_field)

###############################################################################
# StringField
# ^^^^^^^^^^^
#
# You can obtain a :class:`StringField <ansys.dpf.core.string_field.StringField>` from a
# :class:`MeshInfo <ansys.dpf.core.mesh_info.MeshInfo>` by requesting the names of the zones
# in the model. The field is located on zones since it stores the name of each zone.

# Request the name of the face zones in the fluid analysis
my_string_field = my_mesh_info.get_property(property_name="face_zone_names")
print(my_string_field)

###############################################################################
# PropertyField
# ^^^^^^^^^^^^^
#
# You can obtain a :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>` from a
# :class:`MeshInfo <ansys.dpf.core.mesh_info.MeshInfo>` by requesting the element types in the
# mesh. The field is located on elements since it stores the element type ID for each element.

# Get the body_face_topology property field
my_property_field = my_mesh_info.get_property(property_name="body_face_topology")
print(my_property_field)

###############################################################################
# Create fields from scratch
# --------------------------
#
# You can also create a :class:`Field <ansys.dpf.core.field.Field>`,
# :class:`StringField <ansys.dpf.core.string_field.StringField>`, or
# :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>` from scratch based on
# your data.
#
# Field
# ^^^^^
#
# Create a 3D vector field defined for two nodes:

# Create a 3D vector field ready to hold data for two entities
# The constructor creates 3D vector fields by default
my_scratch_field = dpf.Field(nentities=2)
# Set the data values as a flat vector
my_scratch_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
# Associate the data to nodes
my_scratch_field.location = dpf.locations.nodal
# Set the IDs of the nodes the data applies to
my_scratch_field.scoping.ids = [1, 2]
# Define the unit (only available for the Field type)
my_scratch_field.unit = "m"
print(my_scratch_field)

###############################################################################
# Create a 3x3 symmetric matrix field defined for a single element:

# Set the nature to symmatrix
my_symmatrix_field = dpf.Field(nentities=1, nature=dpf.natures.symmatrix)
# The symmatrix dimensions default to 3x3
my_symmatrix_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
my_symmatrix_field.location = dpf.locations.elemental
my_symmatrix_field.scoping.ids = [1]
my_symmatrix_field.unit = "Pa"
print(my_symmatrix_field)

###############################################################################
# Create a 2x3 matrix field defined for a single fluid element face:

# Set the nature to matrix
my_matrix_field = dpf.Field(nentities=1, nature=dpf.natures.matrix)
my_matrix_field.dimensionality = dpf.Dimensionality(dim_vec=[2, 3], nature=dpf.natures.matrix)
my_matrix_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
my_matrix_field.location = dpf.locations.faces
my_matrix_field.scoping.ids = [1]
my_matrix_field.unit = "mm"
print(my_matrix_field)

###############################################################################
# StringField
# ^^^^^^^^^^^

# Create a string field with data for two elements
my_scratch_string_field = dpf.StringField(nentities=2)
my_scratch_string_field.data = ["string_1", "string_2"]
my_scratch_string_field.location = dpf.locations.elemental
my_scratch_string_field.scoping.ids = [1, 2]
print(my_scratch_string_field)

###############################################################################
# PropertyField
# ^^^^^^^^^^^^^

# Create a property field with data for two modes
from ansys.dpf.core.check_version import meets_version

my_scratch_property_field = dpf.PropertyField(nentities=2)
my_scratch_property_field.data = [12, 25]
# For DPF 26R1 and above, directly set the location of the PropertyField
if meets_version(dpf.SERVER.version, "11.0"):
    my_scratch_property_field.location = dpf.locations.modal
# For DPF older than 26R1, you must set the location with a Scoping
else:
    my_scratch_property_field.scoping = dpf.Scoping(location=dpf.locations.modal)
my_scratch_property_field.scoping.ids = [1, 2]
print(my_scratch_property_field)

###############################################################################
# Create fields with the fields_factory
# --------------------------------------
#
# The :mod:`fields_factory <ansys.dpf.core.fields_factory>` module provides helpers to
# create a :class:`Field <ansys.dpf.core.field.Field>`.
#
# Scalar field
# ^^^^^^^^^^^^
#
# Use :func:`create_scalar_field <ansys.dpf.core.fields_factory.create_scalar_field>`
# to create a scalar field:

my_scalar_field = dpf.fields_factory.create_scalar_field(num_entities=2)
my_scalar_field.data = [1.0, 2.0]
my_scalar_field.scoping.ids = [1, 2]
print(my_scalar_field)

###############################################################################
# Generic vector field
# ^^^^^^^^^^^^^^^^^^^^
#
# Use :func:`create_vector_field <ansys.dpf.core.fields_factory.create_vector_field>`
# to create a generic vector field with a custom number of components:

my_vector_field = dpf.fields_factory.create_vector_field(num_entities=2, num_comp=2)
my_vector_field.data = [1.0, 2.0, 3.0, 4.0]
my_vector_field.scoping.ids = [1, 2]
print(my_vector_field)

###############################################################################
# 3D vector field
# ^^^^^^^^^^^^^^^
#
# Use :func:`create_3d_vector_field <ansys.dpf.core.fields_factory.create_3d_vector_field>`
# to create a 3D vector field (3 components per entity):

my_3d_field = dpf.fields_factory.create_3d_vector_field(num_entities=2)
my_3d_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
my_3d_field.scoping.ids = [1, 2]
print(my_3d_field)

###############################################################################
# Generic matrix field
# ^^^^^^^^^^^^^^^^^^^^
#
# Use :func:`create_matrix_field <ansys.dpf.core.fields_factory.create_matrix_field>`
# to create a generic matrix field with custom dimensions:

my_matrix_ff_field = dpf.fields_factory.create_matrix_field(num_entities=2, num_lines=2, num_col=3)
my_matrix_ff_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
my_matrix_ff_field.scoping.ids = [1, 2]
print(my_matrix_ff_field)

###############################################################################
# 3x3 matrix field (tensor)
# ^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Use :func:`create_tensor_field <ansys.dpf.core.fields_factory.create_tensor_field>`
# to create a 3x3 matrix field:

my_tensor_field = dpf.fields_factory.create_tensor_field(num_entities=2)
my_tensor_field.data = [
    1.0,
    2.0,
    3.0,
    4.0,
    5.0,
    6.0,
    7.0,
    8.0,
    9.0,
    10.0,
    11.0,
    12.0,
    13.0,
    14.0,
    15.0,
    16.0,
    17.0,
    18.0,
]
my_tensor_field.scoping.ids = [1, 2]
print(my_tensor_field)

###############################################################################
# Overall field
# ^^^^^^^^^^^^^
#
# Use :func:`create_overall_field <ansys.dpf.core.fields_factory.create_overall_field>`
# to create a field with a single value applied to the whole support:

my_overall_field = dpf.fields_factory.create_overall_field(value=1.0)
print(my_overall_field)

###############################################################################
# Field from array
# ^^^^^^^^^^^^^^^^
#
# Use :func:`field_from_array <ansys.dpf.core.fields_factory.field_from_array>` to
# create a scalar, 3D vector, or symmetric matrix field directly from a numpy array
# or a Python list:

# Scalar field from a 1D list
arr = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
my_field_from_array = dpf.fields_factory.field_from_array(arr=arr)
print(my_field_from_array)

###############################################################################
# 3D vector field from a 2D list:

arr = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
my_field_from_array = dpf.fields_factory.field_from_array(arr=arr)
print(my_field_from_array)

###############################################################################
# Symmetric matrix field from a 2D list:

arr = [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]]
my_field_from_array = dpf.fields_factory.field_from_array(arr=arr)
print(my_field_from_array)

###############################################################################
# Access the field metadata
# -------------------------
#
# The metadata associated to a field includes its location, its scoping,
# the shape of the data stored, its number of components, and its unit.
#
# Field
# ^^^^^

# Location of the field's data
print("location\n", my_temp_field.location, "\n")
# Field scoping (entity type and IDs)
print("scoping\n", my_temp_field.scoping, "\n")
# Available IDs of location entities
print("scoping.ids\n", my_temp_field.scoping.ids, "\n")
# Number of location entities (how many data vectors we have)
print("elementary_data_count\n", my_temp_field.elementary_data_count, "\n")
# Number of components per entity (e.g. 1 for temperature)
print("components_count\n", my_temp_field.component_count, "\n")
# Total length of data (elementary_data_count * component_count)
print("size\n", my_temp_field.size, "\n")
# Shape as (elementary_data_count, component_count)
print("shape\n", my_temp_field.shape, "\n")
# Unit (only available on Field, not StringField or PropertyField)
print("unit\n", my_temp_field.unit, "\n")

###############################################################################
# StringField
# ^^^^^^^^^^^

print("location\n", my_string_field.location, "\n")
print("scoping\n", my_string_field.scoping, "\n")
print("scoping.ids\n", my_string_field.scoping.ids, "\n")
print("elementary_data_count\n", my_string_field.elementary_data_count, "\n")
print("components_count\n", my_string_field.component_count, "\n")
print("size\n", my_string_field.size, "\n")
print("shape\n", my_string_field.shape, "\n")

###############################################################################
# PropertyField
# ^^^^^^^^^^^^^

print("location\n", my_property_field.location, "\n")
print("scoping\n", my_property_field.scoping, "\n")
print("scoping.ids\n", my_property_field.scoping.ids, "\n")
print("elementary_data_count\n", my_property_field.elementary_data_count, "\n")
print("components_count\n", my_property_field.component_count, "\n")
print("size\n", my_property_field.size, "\n")
print("shape\n", my_property_field.shape, "\n")

###############################################################################
# Access the field data
# ---------------------
#
# A :class:`Field <ansys.dpf.core.field.Field>` object is a client-side representation of the field on the server side.
# When a remote DPF server is used, the data of the field is also stored remotely.
#
# To build efficient remote postprocessing workflows, the amount of data exchanged between
# the client and the remote server has to be minimal. This is managed with operators and a
# completely remote workflow, requesting only the initial data needed to build the workflow,
# and the output of the workflow.
#
# It is important when interacting with remote data to remember that any PyDPF request for
# ``Field.data`` downloads the whole array to your local machine.
#
# This is particularly inefficient within scripts handling large amounts of data where the
# request is made to perform an action locally which could have been made remotely with a
# DPF operator. For example, if you want the entity-wise maximum of the field, prefer the
# ``min_max.min_max_by_entity`` operator to ``array.max()`` from NumPy.

###############################################################################
# Get the complete array
# ^^^^^^^^^^^^^^^^^^^^^^
#
# The field's ``data`` is ordered with respect to its ``scoping ids``.
# To access the entire data in the field as a NumPy array:
#
# Field
# '''''

# For a Field, .data returns a DPFArray (a local numpy array)
my_data_array = my_temp_field.data
print(my_data_array)
# Note: this array is a genuine, local numpy array (overloaded as DPFArray).
print(type(my_data_array))

###############################################################################
# StringField
# '''''''''''

my_string_data_array = my_string_field.data
print(my_string_data_array)

###############################################################################
# PropertyField
# '''''''''''''

my_property_data_array = my_property_field.data
print(my_property_data_array)

###############################################################################
# Get data for a single entity
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# If you need to access an individual node or element, request it using either
# :func:`get_entity_data()<ansys.dpf.core.field.Field.get_entity_data>` or
# :func:`get_entity_data_by_id()<ansys.dpf.core.field.Field.get_entity_data_by_id>`:

# Get the data from the element at index 3 in the field
entity_data = my_temp_field.get_entity_data(index=3)
print(entity_data)

###############################################################################

# Get the data from the element with ID 533
entity_data_by_id = my_temp_field.get_entity_data_by_id(id=533)
print(entity_data_by_id)

###############################################################################
# Note that this would correspond to an index of 2 within the
# field. Be aware that scoping IDs are not sequential. You would
# get the index of element 532 in the field with:

# Get the index of element 533 in the field
entity_index = my_temp_field.scoping.index(id=533)
print(entity_index)

###############################################################################
# While these methods are acceptable when requesting data for a few elements or nodes,
# they should not be used when looping over the entire array. For efficiency, a field's
# data can be recovered locally before sending a large number of requests:

# Create a deep copy of the field that can be accessed and modified locally.
with my_temp_field.as_local_field() as f:
    for i in range(1, 100):
        f.get_entity_data_by_id(i)

###############################################################################
# .. tip::
#
#     When using a remote DPF server, accessing a field's data within the ``with`` context
#     manager ensures deletion of local data when exiting the ``with`` block. Following this
#     approach is advisable for efficient remote processing workflows since it guarantees
#     non-persistence of unnecessary local data, especially if the data is not needed beyond
#     the code being executed within the ``with`` block.
