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
.. _ref_tutorials_load_custom_data:

Load custom data in DPF
=======================

This tutorial shows how to represent your custom data in DPF data storage structures.

To import your custom data in DPF, you must create a DPF data structure to store it.
DPF uses :class:`Field<ansys.dpf.core.field.Field>` and
:class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>` objects to handle data.
The ``Field`` is a homogeneous array and a ``FieldsContainer`` is a labeled collection of
``Field`` objects. For more information on DPF data structures, see the
:ref:`ref_tutorials_data_structures` tutorials section.
"""
###############################################################################
# Define the data
# ---------------
#
# Create Python lists with the data to be stored in the Fields.

# Data for the scalar Fields (lists with 1 and 2 dimensions)
data_1 = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
data_2 = [[12.0, 7.0, 8.0], [9.0, 31.0, 1.0]]

# Data for the vector Fields (lists with 1 and 2 dimensions)
data_3 = [4.0, 1.0, 8.0, 5.0, 7.0, 9.0]
data_4 = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 9.0, 7.0, 8.0, 10.0]
data_5 = [[8.0, 4.0, 3.0], [31.0, 5.0, 7.0]]

# Data for the matrix Fields
data_6 = [3.0, 2.0, 1.0, 7.0]
data_7 = [15.0, 3.0, 9.0, 31.0, 1.0, 42.0, 5.0, 68.0, 13.0]
data_8 = [[12.0, 7.0, 8.0], [1.0, 4.0, 27.0], [98.0, 4.0, 6.0]]

###############################################################################
# Create Python lists with the data to be *appended* to the Fields.

# Data for the scalar Fields
data_9 = [24.0]

# Data for the vector Fields
data_10 = [47.0, 33.0, 5.0]

# Data for the matrix Fields
data_11 = [8.0, 2.0, 4.0, 64.0, 32.0, 47.0, 11.0, 23.0, 1.0]

###############################################################################
# Import the PyDPF-Core library
# -----------------------------
#
# Import the ``ansys.dpf.core`` module.

from ansys.dpf import core as dpf

###############################################################################
# Define the Fields sizing
# ------------------------
#
# A :class:`Field<ansys.dpf.core.field.Field>` must always be given:
#
# - A :class:`location<ansys.dpf.core.common.locations>` and a
#   :class:`Scoping<ansys.dpf.core.scoping.Scoping>`.
# - A :class:`nature<ansys.dpf.core.common.natures>` and a
#   :class:`dimensionality<ansys.dpf.core.dimensionality.Dimensionality>`
#   (number of data components for each entity).
#
# Define the number of entities for scalar, vector, and matrix Fields.

# Scalar Fields: 6 entities with 1 component each
num_entities_1 = 6

# Vector Fields: 2 entities with 3 or 5 components each
num_entities_2 = 2

# Matrix Fields: 1 entity
num_entities_3 = 1

###############################################################################
# Create scalar Fields
# --------------------
#
# **Create a scalar Field by instantiating the** ``Field`` **object**
#
# The default ``nature`` of the ``Field`` object is ``'vector'``. Use the
# ``nature`` argument or the
# :func:`Field.dimensionality<ansys.dpf.core.field.Field.dimensionality>` method
# to create a scalar Field.

# Instantiate the Field with a scalar nature
field_11 = dpf.Field(nentities=num_entities_1, nature=dpf.common.natures.scalar)

# Set the scoping ids
field_11.scoping.ids = range(num_entities_1)

# Print the Field
print("Scalar Field: ", "\n", field_11, "\n")

###############################################################################
# Instantiate the Field and use the ``dimensionality`` method to set scalar nature.

field_12 = dpf.Field(nentities=num_entities_1)
field_12.dimensionality = dpf.Dimensionality([1])
field_12.scoping.ids = range(num_entities_1)
print("Scalar Field: ", "\n", field_12, "\n")

###############################################################################
# **Create a scalar Field using the** ``fields_factory`` **module**
#
# Use the :func:`create_scalar_field()<ansys.dpf.core.fields_factory.create_scalar_field>`
# function. Its default ``nature`` is ``'scalar'`` with a ``'1D'`` dimensionality.

field_13 = dpf.fields_factory.create_scalar_field(num_entities=num_entities_1)
field_13.scoping.ids = range(num_entities_1)
print("Scalar Field: ", "\n", field_13, "\n")

###############################################################################
# Use the :func:`field_from_array()<ansys.dpf.core.fields_factory.field_from_array>`
# function, which takes the data directly as input.

field_14 = dpf.fields_factory.field_from_array(arr=data_1)
field_14.scoping.ids = range(num_entities_1)
print("Scalar Field from array: ", "\n", field_14, "\n")

###############################################################################
# Create vector Fields
# --------------------
#
# **Create vector Fields by instantiating the** ``Field`` **object**
#
# The default ``nature`` is ``'vector'`` and the default dimensionality is ``'3D'``.
# Use the :func:`Field.dimensionality<ansys.dpf.core.field.Field.dimensionality>`
# method to set a different dimensionality (here ``'5D'``).

# 3D vector Field (default dimensionality)
field_21 = dpf.Field(nentities=num_entities_2)
field_21.scoping.ids = range(num_entities_2)
print("3D vector Field: ", "\n", field_21, "\n")

# 5D vector Field
field_31 = dpf.Field(nentities=num_entities_2)
field_31.dimensionality = dpf.Dimensionality([5])
field_31.scoping.ids = range(num_entities_2)
print("5D vector Field: ", "\n", field_31, "\n")

###############################################################################
# **Create vector Fields using the** ``fields_factory`` **module**
#
# Use the :func:`create_vector_field()<ansys.dpf.core.fields_factory.create_vector_field>`
# function with the ``num_comp`` argument to set the dimensionality.

field_22 = dpf.fields_factory.create_vector_field(num_entities=num_entities_2, num_comp=3)
field_22.scoping.ids = range(num_entities_2)
print("3D vector Field: ", "\n", field_22, "\n")

field_32 = dpf.fields_factory.create_vector_field(num_entities=num_entities_2, num_comp=5)
field_32.scoping.ids = range(num_entities_2)
print("5D vector Field: ", "\n", field_32, "\n")

###############################################################################
# Use the
# :func:`create_3d_vector_field()<ansys.dpf.core.fields_factory.create_3d_vector_field>`
# function to create a 3D vector Field directly.

field_25 = dpf.fields_factory.create_3d_vector_field(num_entities=num_entities_2)
field_25.scoping.ids = range(num_entities_2)
print("3D vector Field: ", "\n", field_25, "\n")

###############################################################################
# Create matrix Fields
# --------------------
#
# Use the
# :func:`create_matrix_field()<ansys.dpf.core.fields_factory.create_matrix_field>`
# function from the ``fields_factory`` module. Use the ``num_lines`` and ``num_col``
# arguments to define the matrix dimensionality.

# (2, 2) matrix Field
field_41 = dpf.fields_factory.create_matrix_field(
    num_entities=num_entities_3, num_lines=2, num_col=2
)
field_41.scoping.ids = range(num_entities_3)
print("Matrix Field (2,2): ", "\n", field_41, "\n")

# (3, 3) matrix Fields
field_51 = dpf.fields_factory.create_matrix_field(
    num_entities=num_entities_3, num_lines=3, num_col=3
)
field_51.scoping.ids = range(num_entities_3)

field_52 = dpf.fields_factory.create_matrix_field(
    num_entities=num_entities_3, num_lines=3, num_col=3
)
field_52.scoping.ids = range(num_entities_3)

print("Matrix Field 1 (3,3): ", "\n", field_51, "\n")
print("Matrix Field 2 (3,3): ", "\n", field_52, "\n")

###############################################################################
# Set data to the Fields
# ----------------------
#
# Use the :attr:`Field.data<ansys.dpf.core.field_base._FieldBase.data>` attribute
# to set a data array to a ``Field``. The data can be a 1D or 2D Numpy array or
# Python list.

# Set data to the scalar Field
field_11.data = data_1
print("Scalar Field: ", "\n", field_11, "\n")
print("Data scalar Field: ", "\n", field_11.data, "\n")

###############################################################################
# Set data to the vector Fields.

field_21.data = data_3
print("3D vector Field: ", "\n", field_21, "\n")

field_31.data = data_4
print("5D vector Field: ", "\n", field_31, "\n")

# Set 2D data to a 3D vector Field
field_22.data = data_5
print("3D vector Field (from 2D list): ", "\n", field_22, "\n")

###############################################################################
# Set data to the matrix Fields.

field_41.data = data_6
print("Matrix Field (2,2): ", "\n", field_41.data, "\n")

field_51.data = data_7
print("Matrix Field 1 (3,3): ", "\n", field_51.data, "\n")

field_52.data = data_8
print("Matrix Field 2 (3,3): ", "\n", field_52.data, "\n")

###############################################################################
# Append data to the Fields
# -------------------------
#
# Use the :func:`append()<ansys.dpf.core.field.Field.append>` method to add a new
# entity with data to the Field. You must provide the ``scopingid`` that this entity
# will have.

# Append data to the scalar Field
field_11.append(scopingid=6, data=data_9)
print("Scalar Field after append: ", "\n", field_11, "\n")
print("Data scalar Field: ", "\n", field_11.data, "\n")

###############################################################################
# Append data to a vector Field.

field_21.append(scopingid=2, data=data_10)
print("Vector Field after append: ", "\n", field_21, "\n")

###############################################################################
# Append data to a matrix Field.

field_51.append(scopingid=1, data=data_11)
print("Matrix Field after append: ", "\n", field_51, "\n")

###############################################################################
# Create a ``FieldsContainer``
# ----------------------------
#
# A :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>` is a
# collection of ``Field`` objects ordered by labels. Each ``Field`` in the
# ``FieldsContainer`` has an ID for each label.
#
# The most common ``FieldsContainer`` use the label ``'time'`` with IDs corresponding
# to time sets.
#
# **Create a** ``FieldsContainer`` **by instantiating the object**
#
# After instantiation, set the labels and then add fields with their label space.

fc_1 = dpf.FieldsContainer()
fc_1.add_label(label="time")
fc_1.add_field(label_space={"time": 0}, field=field_21)
fc_1.add_field(label_space={"time": 1}, field=field_31)
print(fc_1)

###############################################################################
# **Create a** ``FieldsContainer`` **using the** ``fields_container_factory`` **module**
#
# Use the
# :func:`over_time_freq_fields_container()<ansys.dpf.core.fields_container_factory.over_time_freq_fields_container>`
# function to create a ``FieldsContainer`` with a predefined ``'time'`` label.

fc_2 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field_21, field_31])
print(fc_2)
