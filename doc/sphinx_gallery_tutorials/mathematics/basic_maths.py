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
.. _ref_basic_math:

Basic maths
===========

.. note::

    This tutorial requires DPF 9.1 or above (2025 R1).

This tutorial explains how to perform some basic mathematical operations with PyDPF-Core.

DPF exposes data through :class:`Field<ansys.dpf.core.field.Field>` objects (or other
specialized kinds of fields). A Field is a homogeneous array of floats.

A :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>` is a labeled
collection of Field objects that most operators can use, allowing you to operate on several
fields at once.

To perform mathematical operations, use the operators available in the
:mod:`math operators<ansys.dpf.core.operators.math>` module. First create an instance of the
operator of interest, then use the ``.eval()`` method to compute and retrieve the first output.

Most operators for mathematical operations can take in a Field or a FieldsContainer. Most
mathematical operators have a separate implementation for handling FieldsContainer objects
as input, and are recognizable by the suffix ``_fc`` appended to their name.

This tutorial first shows how to create the custom fields and field containers it uses. It then
provides a focus on the effect of the scoping of the fields on the result, as well as a focus on
the treatment of collections. It then explains how to use several of the mathematical operators
available, both with fields and with field containers.
"""
###############################################################################
# Imports
# -------

from ansys.dpf import core as dpf
from ansys.dpf.core.operators import math as maths

# .. _ref_basic_maths_create_custom_data:
###############################################################################
# Create fields and field collections
# ------------------------------------
#
# DPF exposes mathematical fields of floats through
# :class:`Field<ansys.dpf.core.field.Field>` and
# :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>` objects.
# A Field is a homogeneous array of floats and a FieldsContainer is a labeled collection
# of Field objects.
#
# Here, fields and field collections created from scratch are used to show how the
# mathematical operators work.
#
# For more information on creating a Field from scratch, see :ref:`ref_tutorials_data_structures`.
#
# Create the fields with the :class:`Field<ansys.dpf.core.field.Field>` class constructor.
# Each field is a nodal 3D vector field with two entities. The scoping of each field is
# set to the range ``[0, 1]`` (the node IDs). The data of each field is a flat list of
# floats of size ``num_entities * num_components = 2 * 3 = 6``.
#
# Helpers are also available in
# :mod:`fields_factory<ansys.dpf.core.fields_factory>` for easier creation of
# fields from scratch.

# Create four nodal 3D vector fields of size 2
num_entities = 2
field1 = dpf.Field(nentities=num_entities)
field2 = dpf.Field(nentities=num_entities)
field3 = dpf.Field(nentities=num_entities)
field4 = dpf.Field(nentities=num_entities)

# Set the scoping IDs
field1.scoping.ids = field2.scoping.ids = field3.scoping.ids = field4.scoping.ids = range(
    num_entities
)

# Set the data for each field using flat lists (of size = num_entities * num_components)
field1.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
field2.data = [7.0, 3.0, 5.0, 8.0, 1.0, 2.0]
field3.data = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
field4.data = [4.0, 1.0, 8.0, 5.0, 7.0, 9.0]

# Print the fields
print("Field 1", "\n", field1, "\n")
print("Field 2", "\n", field2, "\n")
print("Field 3", "\n", field3, "\n")
print("Field 4", "\n", field4, "\n")

###############################################################################
# Create field containers
# ^^^^^^^^^^^^^^^^^^^^^^^
#
# Create the collections of fields (called "field containers") using the
# :mod:`fields_container_factory<ansys.dpf.core.fields_container_factory>`.
# Use the
# :func:`over_time_freq_fields_container()<ansys.dpf.core.fields_container_factory.over_time_freq_fields_container>`
# helper to generate a FieldsContainer with *'time'* labels.

# Create the field containers
fc1 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field1, field2])
fc2 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field3, field4])

# Print the field containers
print("FieldsContainer1", "\n", fc1, "\n")
print("FieldsContainer2", "\n", fc2, "\n")

# .. _ref_basic_maths_scoping_handling:
###############################################################################
# Effect of the scoping
# ----------------------
#
# The scoping of a DPF field stores information about which entity the data is associated to.
# A scalar field containing data for three entities is, for example, linked to a scoping defining
# three entity IDs. The location of the scoping defines the type of entity the IDs refer to. This
# allows DPF to know what each data point of a field is associated to.
#
# Operators such as mathematical operators usually perform operations between corresponding
# entities of fields.
#
# For example, the addition of two scalar fields does not just add the two data arrays, which may
# not be of the same length or may not be ordered the same way. Instead it uses the scoping of
# each field to find corresponding entities, their data in each field, and perform the addition on
# those. This means that the operation is usually performed for entities in the intersection of
# the two field scopings.
#
# Some operators provide options to handle data for entities outside of this intersection, but
# most simply ignore the data for these entities not in the intersection of the scopings.
#
# The following examples illustrate this behavior.

# Instantiate two nodal 3D vector fields of length 3
field5 = dpf.Field(nentities=3)
field6 = dpf.Field(nentities=3)

# Set the data for each field
field5.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
field6.data = [5.0, 1.0, 6.0, 3.0, 8.0, 9.0, 7.0, 2.0, 4.0]

# Set the scoping IDs (here node IDs)
field5.scoping.ids = [1, 2, 3]
field6.scoping.ids = [3, 4, 5]

# Print the fields
print("Field 5", "\n", field5, "\n")
print("Field 6", "\n", field6, "\n")

###############################################################################
# Add operator with scoping
# ^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Here the only entities with matching IDs between the two fields are the third entity in
# field5 (ID=3) and the first entity in field6 (ID=3). Other entities are not taken into account.
#
# The resulting field only contains data for entities where a match is found in the other field.
# It has the size of the intersection of the two scopings. Here this means the addition returns
# a field with data only for the node with ID=3. This behavior is specific to each operator.

# Use the add operator
add_scop = dpf.operators.math.add(fieldA=field5, fieldB=field6).eval()

# Print the result
print(add_scop, "\n")

###############################################################################
# Inner product operator with scoping
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# The :class:`generalized_inner_product<ansys.dpf.core.operators.math.generalized_inner_product.generalized_inner_product>`
# operator returns zero for entities where no match is found in the other field.
# The resulting field is the size of the union of the two scopings.
# This behavior is specific to each operator.

# Use the dot product operator
dot_scop = dpf.operators.math.generalized_inner_product(fieldA=field5, fieldB=field6).eval()
# ID 3: (7. * 5.) + (8. * 1.) + (9. * 6.)

# Print the result
print(dot_scop, "\n")
print(dot_scop.data, "\n")

# .. _ref_basic_maths_handling_of_collections:
###############################################################################
# Handling of collections
# ------------------------
#
# Most mathematical operators have a separate implementation for handling FieldsContainer objects
# as input, and are recognizable by the suffix ``_fc`` appended to their name.
#
# These operators operate on fields with the same label space.
#
# Using the two collections of fields built previously, both have a *time* label with an
# associated value for each field. Operators working with FieldsContainer inputs match fields
# from each collection with the same value for all labels.
#
# In this case, ``field 0`` of ``fc1`` with label space ``{"time": 1}`` gets matched up with
# ``field 0`` of ``fc2`` also with label space ``{"time": 1}``. Then ``field 1`` of ``fc1`` with
# label space ``{"time": 2}`` gets matched up with ``field 1`` of ``fc2`` also with label space
# ``{"time": 2}``.

###############################################################################
# Addition
# --------
#
# Use the
# :class:`add<ansys.dpf.core.operators.math.add.add>` operator to compute the element-wise
# addition for each component of two fields. Use the
# :class:`accumulate<ansys.dpf.core.operators.math.accumulate.accumulate>` operator to compute
# the overall sum of data for each component of a field.

###############################################################################
# Element-wise addition
# ^^^^^^^^^^^^^^^^^^^^^

# Add the fields
add_field = maths.add(fieldA=field1, fieldB=field2).eval()
# id 0: [1.+7. 2.+3. 3.+5.] = [ 8.  5.  8.]
# id 1: [4.+8. 5.+1. 6.+2.] = [12.  6.  8.]

# Print the results
print("Addition field ", add_field, "\n")

###############################################################################
# Element-wise addition of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Add the two field collections
add_fc = maths.add_fc(fields_container1=fc1, fields_container2=fc2).eval()
# {time: 1}: field1 + field3
#           -->      id 0: [1.+6. 2.+5. 3.+4.] = [7. 7. 7.]
#                    id 1: [4.+3. 5.+2. 6.+1.] = [7. 7. 7.]
#
# {time: 2}: field2 + field4
#           -->      id 0: [7.+4. 3.+1. 5.+8.] = [11. 4. 13.]
#                    id 1: [8.+5. 1.+7. 2.+9.] = [13. 8. 11.]

# Print the results
print("Addition FieldsContainers", "\n", add_fc, "\n")
print(add_fc.get_field({"time": 1}), "\n")
print(add_fc.get_field({"time": 2}), "\n")

###############################################################################
# Overall sum
# ^^^^^^^^^^^
#
# Use the :class:`accumulate<ansys.dpf.core.operators.math.accumulate.accumulate>` operator to
# compute the total sum of elementary data of a field, for each component of the field. You can
# give a scaling ("weights") argument.
#
# Keep in mind the Field dimension. The Field represents 3D vectors, so each elementary data is a
# 3D vector. The optional "weights" Field attribute is a scaling factor for each entity when
# performing the sum, so you must provide a 1D field.

# Compute the total sum of a field
tot_sum_field = maths.accumulate(fieldA=field1).eval()
# vector component 0 = 1. + 4. = 5.
# vector component 1 = 2. + 5. = 7.
# vector component 2 = 3. + 6. = 9.

# Print the results
print("Total sum fields", "\n", tot_sum_field, "\n")

###############################################################################
# Overall sum of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Find the total sum of the two field collections
tot_sum_fc = maths.accumulate_fc(fields_container=fc1).eval()
# {time: 1}: field1
#           -->      vector component 0 = 1.+ 4. = 5.
#                    vector component 1 = 2.+ 5. = 7.
#                    vector component 2 = 3.+ 6. = 9.
#
# {time: 2}: field2
#           -->      vector component 0 = 7.+ 8. = 15.
#                    vector component 1 = 3.+ 1. = 4.
#                    vector component 2 = 5.+ 2. = 7.

# Print the results
print("Total sum FieldsContainers", "\n", tot_sum_fc, "\n")
print(tot_sum_fc.get_field({"time": 1}), "\n")
print(tot_sum_fc.get_field({"time": 2}), "\n")

###############################################################################
# Weighted overall sum
# ^^^^^^^^^^^^^^^^^^^^
#
# Compute the total sum (accumulate) for each component of a given Field using a scale factor
# field.

# Define the scale factor field
scale_vect = dpf.Field(nentities=num_entities, nature=dpf.natures.scalar)
# Set the scale factor field scoping IDs
scale_vect.scoping.ids = range(num_entities)
# Set the scale factor field data
scale_vect.data = [5.0, 2.0]

# Compute the total sum of the field using a scaling field
tot_sum_field_scale = maths.accumulate(fieldA=field1, weights=scale_vect).eval()
# vector component 0 = (1.0 * 5.0) + (4.0 * 2.0) = 13.
# vector component 1 = (2.0 * 5.0) + (5.0 * 2.0) = 20.
# vector component 2 = (3.0 * 5.0) + (6.0 * 2.0) = 27.

# Print the results
print("Total weighted sum:", "\n", tot_sum_field_scale, "\n")

###############################################################################
# Weighted overall sum of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Total scaled sum of the two field collections (accumulate)
tot_sum_fc_scale = maths.accumulate_fc(fields_container=fc1, weights=scale_vect).eval()
# {time: 1}: field1
#           -->      vector component 0 = (1.0 * 5.0) + (4.0 * 2.0) = 13.
#                    vector component 1 = (2.0 * 5.0) + (5.0 * 2.0) = 20.
#                    vector component 2 = (3.0 * 5.0) + (6.0 * 2.0) = 27.
#
# {time: 2}: field2
#           -->      vector component 0 = (7.0 * 5.0) + (8.0 * 2.0) = 51.
#                    vector component 1 = (3.0 * 5.0) + (1.0 * 2.0) = 17.
#                    vector component 2 = (5.0 * 5.0) + (2.0 * 2.0) = 29.

# Print the results
print("Total sum FieldsContainers scale", "\n", tot_sum_fc_scale, "\n")
print(tot_sum_fc_scale.get_field({"time": 1}), "\n")
print(tot_sum_fc_scale.get_field({"time": 2}), "\n")

###############################################################################
# Subtraction
# -----------
#
# Use the :class:`minus<ansys.dpf.core.operators.math.minus.minus>` operator to compute the
# element-wise difference between each component of two fields.

# Subtraction of two 3D vector fields
minus_field = maths.minus(fieldA=field1, fieldB=field2).eval()
# id 0: [1.-7. 2.-3. 3.-5.] = [-6. -1. -2.]
# id 1: [4.-8. 5.-1. 6.-2.] = [-4. 4. 4.]

# Print the results
print("Subtraction field", "\n", minus_field, "\n")

###############################################################################
# Subtraction of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Subtraction of two field collections
minus_fc = maths.minus_fc(field_or_fields_container_A=fc1, field_or_fields_container_B=fc2).eval()
# {time: 1}: field1 - field3
#           -->      id 0: [1.-6. 2.-5. 3.-4.] = [-5. -3. -1.]
#                    id 1: [4.-3. 5.-2. 6.-1.] = [1. 3. 5.]
#
# {time: 2}: field2 - field4
#           -->      id 0: [7.-4. 3.-1. 5.-8.] = [3. 2. -3.]
#                    id 1: [8.-5. 1.-7. 2.-9.] = [3. -6. -7.]

# Print the results
print("Subtraction field collection", "\n", minus_fc, "\n")
print(minus_fc.get_field({"time": 1}), "\n")
print(minus_fc.get_field({"time": 2}), "\n")

###############################################################################
# Element-wise product
# --------------------
#
# Use the
# :class:`component_wise_product<ansys.dpf.core.operators.math.component_wise_product.component_wise_product>`
# operator to compute the element-wise product between each component of two fields. Also known
# as the `Hadamard product <https://en.wikipedia.org/wiki/Hadamard_product_(matrices)>`_, the
# *entrywise product* or *Schur product*.

# Compute the Hadamard product of two fields
element_prod_field = maths.component_wise_product(fieldA=field1, fieldB=field2).eval()
# id 0: [1.*7. 2.*3. 3.*5.] = [7. 6. 15.]
# id 1: [4.*8. 5.*1. 6.*2.] = [32. 5. 12.]

# Print the results
print("Element-wise product field", "\n", element_prod_field, "\n")

###############################################################################
# Element-wise product with a field collection
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# The current implementation of
# :class:`component_wise_product_fc<ansys.dpf.core.operators.math.component_wise_product_fc.component_wise_product_fc>`
# only performs the Hadamard product for each field in a collection with a distinct unique field.
# The element-wise product between two field collections is not implemented.

# Cross product of each field in a collection and a single unique field
element_prod_fc = maths.component_wise_product_fc(fields_container=fc1, fieldB=field3).eval()
# {time: 1}: field1 and field3
#           -->      id 0: [1.*6. 2.*5. 3.*4.] = [6. 10. 12.]
#                    id 1: [4.*3. 5.*2. 6.*1.] = [12. 10. 6.]
#
# {time: 2}: field2 and field3
#           -->      id 0: [7.*6. 3.*5. 5.*4.] = [42. 15. 20.]
#                    id 1: [8.*3. 1.*2. 2.*1.] = [24. 2. 2.]

# Print the results
print("Element product FieldsContainer", "\n", element_prod_fc, "\n")
print(element_prod_fc.get_field({"time": 1}), "\n")
print(element_prod_fc.get_field({"time": 2}), "\n")

###############################################################################
# Cross product
# -------------
#
# Use the :class:`cross_product<ansys.dpf.core.operators.math.cross_product.cross_product>`
# operator to compute the
# `cross product <https://en.wikipedia.org/wiki/Cross_product>`_ between two vector fields.

# Compute the cross product
cross_prod_field = maths.cross_product(fieldA=field1, fieldB=field2).eval()
# id 0: [(2.*5. - 3.*3.)  (3.*7. - 1.*5.)  (1.*3. - 2.*7.)] = [1. 16. -11.]
# id 1: [(5.*2. - 6.*1.)  (6.*8. - 4.*2.)  (4.*1. - 5.*8.)] = [4. 40. -36.]

# Print the results
print("Cross product field", "\n", cross_prod_field, "\n")

###############################################################################
# Cross product of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Cross product of two field collections
cross_prod_fc = maths.cross_product_fc(
    field_or_fields_container_A=fc1, field_or_fields_container_B=fc2
).eval()
# {time: 1}: field1 X field3
#           -->      id 0: [(2.*4. - 3.*5.)  (3.*6. - 1.*4.)  (1.*5. - 2.*6.)] = [-7. 14. -7.]
#                    id 1: [(5.*1. - 6.*2.)  (6.*3. - 4.*1.)  (4.*2. - 5.*3.)] = [-7. 14. -7.]
#
# {time: 2}: field2 X field4
#           -->      id 0: [(3.*8. - 5.*1.)  (5.*4. - 7.*8.)  (7.*1. - 3.*4.)] = [19. -36. -5]
#                    id 1: [(1.*9. - 2.*7.)  (2.*5. - 8.*9.)  (8.*7. - 1.*5.)] = [-5. -62. 51.]

# Print the results
print("Cross product FieldsContainer", "\n", cross_prod_fc, "\n")
print(cross_prod_fc.get_field({"time": 1}), "\n")
print(cross_prod_fc.get_field({"time": 2}), "\n")

###############################################################################
# Dot product
# -----------
#
# DPF provides two dot product operations:
#
# - Use the
#   :class:`generalized_inner_product<ansys.dpf.core.operators.math.generalized_inner_product.generalized_inner_product>`
#   operator to compute the `inner product <https://en.wikipedia.org/wiki/Dot_product>`_ (also
#   known as *dot product* or *scalar product*) between vector data of entities in two fields.
# - Use the :class:`overall_dot<ansys.dpf.core.operators.math.overall_dot.overall_dot>` operator
#   to compute the sum over all entities of the inner product of two vector fields.

###############################################################################
# Inner product
# ^^^^^^^^^^^^^
#
# The :class:`generalized_inner_product<ansys.dpf.core.operators.math.generalized_inner_product.generalized_inner_product>`
# operator computes a general notion of inner product between two vector fields.
# In Cartesian coordinates it is equivalent to the dot/scalar product.

# Generalized inner product of two fields
dot_prod_field = maths.generalized_inner_product(fieldA=field1, fieldB=field2).eval()
# id 0: (1. * 7.) + (2. * 3.) + (3. * 5.) = 28.
# id 1: (4. * 8.) + (5. * 1.) + (6. * 2.) = 49.

# Print the results
print("Dot product field", "\n", dot_prod_field, "\n")

###############################################################################
# Inner product of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Generalized inner product of two field collections
dot_prod_fc = maths.generalized_inner_product_fc(
    field_or_fields_container_A=fc1, field_or_fields_container_B=fc2
).eval()
# {time: 1}: field1 X field3
#           -->      id 0: (1. * 6.) + (2. * 5.) + (3. * 4.) = 28.
#                    id 1: (4. * 3.) + (5. * 2.) + (6. * 1.) = 28.
#
# {time: 2}: field2 X field4
#           -->      id 0: (7. * 4.) + (3. * 1.) + (5. * 8.) = 71.
#                    id 1: (8. * 5.) + (1. * 7.) + (2. * 9.) = 65.

# Print the results
print("Dot product FieldsContainer", "\n", dot_prod_fc, "\n")
print(dot_prod_fc.get_field({"time": 1}), "\n")
print(dot_prod_fc.get_field({"time": 2}), "\n")

###############################################################################
# Overall dot product
# ^^^^^^^^^^^^^^^^^^^^
#
# The :class:`overall_dot<ansys.dpf.core.operators.math.overall_dot.overall_dot>` operator
# creates two manipulations to give the result:
#
# 1. It first computes a dot product between data of corresponding entities for two vector
#    fields, resulting in a scalar field.
# 2. It then sums the result obtained previously over all entities to return a scalar.

# Overall dot product of two fields
overall_dot_result = maths.overall_dot(fieldA=field1, fieldB=field2).eval()
# id 1: (1. * 7.) + (2. * 3.) + (3. * 5.) + (4. * 8.) + (5. * 1.) + (6. * 2.) = 77.

# Print the results
print("Overall dot", "\n", overall_dot_result, "\n")

###############################################################################
# Division
# --------
#
# Use the
# :class:`component_wise_divide<ansys.dpf.core.operators.math.component_wise_divide.component_wise_divide>`
# operator to compute the
# `Hadamard division <https://en.wikipedia.org/wiki/Hadamard_product_(matrices)#Analogous_operations>`_
# between each component of two fields.

# Divide a field by another field
comp_wise_div = maths.component_wise_divide(fieldA=field1, fieldB=field2).eval()
# id 0: [1./7. 2./3. 3./5.] = [0.143 0.667 0.6]
# id 1: [4./8. 5./1. 6./2.] = [0.5 5. 3.]

# Print the results
print("Component-wise division field", "\n", comp_wise_div, "\n")

###############################################################################
# Component-wise division of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Component-wise division between two field collections
comp_wise_div_fc = maths.component_wise_divide_fc(
    fields_containerA=fc1, fields_containerB=fc2
).eval()
# {time: 1}: field1 / field3
#           -->      id 0: [1./6. 2./5. 3./4.] = [0.167 0.4 0.75]
#                    id 1: [4./3. 5./2. 6./1.] = [1.333 2.5 6.]
#
# {time: 2}: field2 / field4
#           -->      id 0: [7./4. 3./1. 5./8.] = [1.75 3. 0.625]
#                    id 1: [8./5. 1./7. 2./9.] = [1.6 0.143 0.222]

# Print the results
print("Component-wise division FieldsContainer", "\n", comp_wise_div_fc, "\n")
print(comp_wise_div_fc.get_field({"time": 1}), "\n")
print(comp_wise_div_fc.get_field({"time": 2}), "\n")

###############################################################################
# Power
# -----
#
# Use:
#
# - the :class:`pow<ansys.dpf.core.operators.math.pow.pow>` operator to compute the
#   element-wise power of each component of a Field
# - the :class:`sqr<ansys.dpf.core.operators.math.sqr.sqr>` operator to compute the
#   `Hadamard power <https://en.wikipedia.org/wiki/Hadamard_product_(matrices)#Analogous_operations>`_
#   of each component of a Field
# - the :class:`sqrt<ansys.dpf.core.operators.math.sqrt.sqrt>` operator to compute the
#   `Hadamard root <https://en.wikipedia.org/wiki/Hadamard_product_(matrices)#Analogous_operations>`_
#   of each component of a Field

###############################################################################
# Element-wise power
# ^^^^^^^^^^^^^^^^^^
#
# The :class:`pow<ansys.dpf.core.operators.math.pow.pow>` operator computes the element-wise
# power of each component of a Field to a given factor. This example computes the power of three.

# Define the power factor
pow_factor = 3.0
# Compute the power of three of a field
pow_field = maths.pow(field=field1, factor=pow_factor).eval()
# id 0: [(1.^3.) (2.^3.) (3.^3.)] = [1. 8. 27.]
# id 1: [(4.^3.) (5.^3.) (6.^3.)] = [64. 125. 216.]

# Print the results
print("Power field", "\n", pow_field, "\n")

###############################################################################
# Element-wise power of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Compute the power of three of a field collection
pow_fc = maths.pow_fc(fields_container=fc1, factor=pow_factor).eval()
# {time: 1}: field1
#           -->      id 0: [(1.^3.) (2.^3.) (3.^3.)] = [1. 8. 27.]
#                    id 1: [(4.^3.) (5.^3.) (6.^3.)] = [64. 125. 216.]
#
# {time: 2}: field2
#           -->      id 0: [(7.^3.) (3.^3.) (5.^3.)] = [343. 27. 125.]
#                    id 1: [(8.^3.) (1.^3.) (2.^3.)] = [512. 1. 8.]

# Print the results
print("Power FieldsContainer", "\n", pow_fc, "\n")
print(pow_fc.get_field({"time": 1}), "\n")
print(pow_fc.get_field({"time": 2}), "\n")

###############################################################################
# Element-wise square
# ^^^^^^^^^^^^^^^^^^^^
#
# The :class:`sqr<ansys.dpf.core.operators.math.sqr.sqr>` operator computes the element-wise
# power of two
# (`Hadamard power <https://en.wikipedia.org/wiki/Hadamard_product_(matrices)#Analogous_operations>`_)
# for each component of a Field. It is a shortcut for the ``pow`` operator with factor 2.

# Compute the power of two of a field
sqr_field = maths.sqr(field=field1).eval()
# id 0: [(1.^2.) (2.^2.) (3.^2.)] = [1. 4. 9.]
# id 1: [(4.^2.) (5.^2.) (6.^2.)] = [16. 25. 36.]

print("^2 field", "\n", sqr_field, "\n")

###############################################################################
# Element-wise square of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Compute the power of two of a field collection
sqr_fc = maths.sqr_fc(fields_container=fc1).eval()
# {time: 1}: field1
#           -->      id 0: [(1.^2.) (2.^2.) (3.^2.)] = [1. 4. 9.]
#                    id 1: [(4.^2.) (5.^2.) (6.^2.)] = [16. 25. 36.]
#
# {time: 2}: field2
#           -->      id 0: [(7.^2.) (3.^2.) (5.^2.)] = [49. 9. 25.]
#                    id 1: [(8.^2.) (1.^2.) (2.^2.)] = [64. 1. 4.]

# Print the results
print("^2 FieldsContainer", "\n", sqr_fc, "\n")
print(sqr_fc.get_field({"time": 1}), "\n")
print(sqr_fc.get_field({"time": 2}), "\n")

###############################################################################
# Element-wise square root
# ^^^^^^^^^^^^^^^^^^^^^^^^^
#
# The :class:`sqrt<ansys.dpf.core.operators.math.sqrt.sqrt>` operator computes the element-wise
# square-root
# (`Hadamard root <https://en.wikipedia.org/wiki/Hadamard_product_(matrices)#Analogous_operations>`_)
# for each component of a Field. It is a shortcut for the ``pow`` operator with factor *0.5*.

# Compute the square-root of a field
sqrt_field = maths.sqrt(field=field1).eval()
# id 0: [(1.^0.5) (2.^0.5) (3.^0.5)] = [1. 1.414 1.732]
# id 1: [(4.^0.5) (5.^0.5) (6.^0.5)] = [2. 2.236 2.449]

print("^0.5 field", "\n", sqrt_field, "\n")

###############################################################################
# Element-wise square root of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Compute the square-root of a field collection
sqrt_fc = maths.sqrt_fc(fields_container=fc1).eval()
# {time: 1}: field1
#           -->      id 0: [(1.^.5) (2.^.5) (3.^.5)] = [1. 1.414 1.732]
#                    id 1: [(4.^.5) (5.^.5) (6.^.5)] = [2. 2.236 2.449]
#
# {time: 2}: field2
#           -->      id 0: [(7.^.5) (3.^.5) (5.^.5)] = [2.645 1.732 2.236]
#                    id 1: [(8.^.5) (1.^.5) (2.^.5)] = [2.828 1. 1.414]

# Print the results
print("Sqrt FieldsContainer", "\n", sqrt_fc, "\n")
print(sqrt_fc.get_field({"time": 1}), "\n")
print(sqrt_fc.get_field({"time": 2}), "\n")

###############################################################################
# Norm
# ----
#
# Use the :class:`norm<ansys.dpf.core.operators.math.norm.norm>` operator to compute the
# `Lp norm <https://en.wikipedia.org/wiki/Norm_(mathematics)#p-norm>`_ of the elementary data
# for each entity of a Field. The default *Lp* norm is *Lp=L2*.

# Compute the L2 norm of a field
norm_field = maths.norm(field=field1, scalar_int=2).eval()
# id 0: [(1.^2.) + (2.^2.) + (3.^2.)] ^1/2 = 3.742
# id 1: [(4.^2.) + (5.^2.) + (6.^2.)] ^1/2 = 8.775

# Print the results
print("Norm field", "\n", norm_field, "\n")

###############################################################################
# Norm of field collections
# ^^^^^^^^^^^^^^^^^^^^^^^^^^

# Define the L2 norm of a field collection
norm_fc = maths.norm_fc(fields_container=fc1).eval()
# {time: 1}: field1
#           -->      id 0: [(1.^2.) + (2.^2.) + (3.^2.)] ^1/2 = 3.742
#                    id 1: [(4.^2.) + (5.^2.) + (6.^2.)] ^1/2 = 8.775
#
# {time: 2}: field2
#           -->      id 0: [(7.^2.) + (3.^2.) + (5.^2.)] ^1/2 = 9.110
#                    id 1: [(8.^2.) + (1.^2.) + (2.^2.)] ^1/2 = 8.307

# Print the results
print("Norm FieldsContainer", "\n", norm_fc, "\n")
print(norm_fc.get_field({"time": 1}), "\n")
print(norm_fc.get_field({"time": 2}), "\n")
