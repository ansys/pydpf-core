# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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
.. _ref_math_operators_example:

Mathematical Operations
~~~~~~~~~~~~~~~~~~~~~~~

DPF provides operators for implementing mathematical operations,
ranging from addition and multiplication to FFT and QR solving.

For a complete list, see :ref:`ref_dpf_operators_reference`, under the math section.

"""

# Import the necessary modules
import ansys.dpf.core as dpf

###############################################################################
# Addition
# ~~~~~~~~

# Initialize Fields
num_entities = 2
field1 = dpf.Field(nentities=2)
field2 = dpf.Field(nentities=2)

# By default, Fields contain 3d vectors.
# So with three entities we need nine values.
field1.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
field2.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

field1.scoping.ids = range(num_entities)
field2.scoping.ids = range(num_entities)
###############################################################################
# Once the fields are ready, we can instantiate an operator.
add_op = dpf.operators.math.add(field1, field2)

###############################################################################
# Finally, we use eval() to compute and retrieve the result.
field3 = add_op.eval()

# = [[2. 4. 6.] [8. 10. 12.]]
print(field3.data)

###############################################################################
# Dot product
# ~~~~~~~~~~~
dot_op = dpf.operators.math.generalized_inner_product(field1, field2)

# (1. * 1.) + (2. * 2.) + (3. * 3.) = 14.
# (4. * 4.) + (5. * 5.) + (6. * 6.) = 77.
field3 = dot_op.eval()
print(field3.data)


###############################################################################
# Power
# ~~~~~
field = dpf.Field(nentities=1)
field1.data = [1.0, 2.0, 3.0]
field1.scoping.ids = [1]

pow_op = dpf.operators.math.pow(field1, 3.0)

# [1. 8. 27.]
field3 = pow_op.eval()
print(field3.data)


###############################################################################
# L2 norm
# ~~~~~~~
field1.data = [16.0, -8.0, 2.0]
norm_op = dpf.operators.math.norm(field1)

# [ 18. ]
field3 = norm_op.eval()
print(field3.data)


###############################################################################
# Accumulate
# ~~~~~~~~~~
# First we define fields. By default, fields represent 3D vectors
# so one elementary data is a 3D vector.
# The optional ponderation field is a field which takes one value per entity,
# so we need to change its dimensionality (1D).
num_entities = 3
input_field = dpf.Field(nentities=num_entities)
ponderation_field = dpf.Field(num_entities)
ponderation_field.dimensionality = dpf.Dimensionality([1])

input_field.scoping.ids = range(num_entities)
ponderation_field.scoping.ids = range(num_entities)

###############################################################################
# Fill fields with data.
# Add nine values because there are three entities.
input_field.data = [-2.0, 2.0, 4.0, -5.0, 0.5, 1.0, 7.0, 3.0, -3.0]
###############################################################################
# Three weights, one per entity.
ponderation_field.data = [0.5, 2.0, 0.5]

###############################################################################
# Retrieve the result.
acc = dpf.operators.math.accumulate(fieldA=input_field, ponderation=ponderation_field)
output_field = acc.outputs.field()

# (-2.0 * 0.5) + (-5.0 * 2.0) + (7.0 * 0.5)  = -7.5
# (2.0  * 0.5) + (0.5  * 2.0) + (3.0 * 0.5)  = 3.5
# (4.0  * 0.5) + (1.0  * 2.0) + (-3.0 * 0.5) = 2.5
print(output_field.data)

###############################################################################
# With scoping
# ~~~~~~~~~~~~
field1.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
field2.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

###############################################################################
# Next, we need to provide information about the scoping.
# DPF needs to know the IDs of the data we just provided,
# so that it can apply an operator on a subset of the original data.
#
# By providing these integers we only select the data with an ID in common.
# Here we are selecting the third elementary data of the first field,
# and the first elementary data of the second field,
# Other elementary data is not taken into account when using an operator that needs two operands.
field1.scoping.ids = [1, 2, 3]
field2.scoping.ids = [3, 4, 5]

add_op = dpf.operators.math.add(field1, field2)
field3 = add_op.eval()

# Only the third entity was changed
# because it is the only operator where two operands were provided.
print(field3.data)
# [[8. 10. 12.]]
print(field3.get_entity_data_by_id(3))

###############################################################################
# Dot product

dot_op = dpf.operators.math.generalized_inner_product(field1, field2)

# We obtain zeros for IDs where there could not be two operands.
# (7. * 1.) + (8. * 2.) + (9. * 3.) = 50.
# [0. 0. 50. 0. 0.]
field3 = dot_op.eval()
print(field3.data)
