# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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
.. _ref_basic_field_example:

Field and field containers overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In DPF, the field is the main simulation data container. During a numerical
simulation, the result data is defined by values associated to entities
(scoping). These entities are a subset of a model (support).

Because the field data is always associated to its scoping and support,
the field is a self-describing piece of data. A field is also
defined by its parameters, such as dimensionality, unit, and location.
For example, a field can describe any of the following:

- Displacement vector
- Norm, stress, or strain tensor
- Stress or strain equivalent
- Minimum or maximum over time of any result.

A field can be defined on a complete model or on only certain entities
of the model based on its scoping. The data is stored as a vector of
double values, and each elementary entity has a number of components.
For example, a displacement has three components, and a symmetrical
stress matrix has six components.

In DPF, a fields container is simply a collection of fields that can be
indexed, just like a Python list. Operators applied to a fields
container have each individual field operated on. Fields
containers are outputs from operators.

"""

# First, import necessary modules
import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create a model object to establish a connection with an
# example result file and then extract:
model = dpf.Model(examples.find_static_rst())
print(model)

###############################################################################
# Create the displacement operator directly from the ``results``
# property and extract the displacement fields container:
disp_op = model.results.displacement()
fields = disp_op.outputs.fields_container()
print(fields)

###############################################################################
# A field can be extracted from a fields container by simply indexing
# the requested field:
field = fields[0]
print(field)

###############################################################################
# Extract data from a field
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# You can extract all the data from a given field using the ``data``
# property. This returns a ``numpy`` array.

print(field.data)

###############################################################################
# While it might seem preferable to work entirely within ``numpy``,
# DPF runs outside of Python and potentially even on a
# remote machine. Therefore, the transfer of unnecessary data between
# the DPF instance and the Python client leads to inefficient
# operations on large models. Instead, you should use DPF operators to
# assemble the necessary data before recalling the data from DPF.
#
# For example, if you want the maximum displacement for a given
# result, use the min/max operator:
#
min_max_op = dpf.operators.min_max.min_max(field)
print(min_max_op.outputs.field_max().data)

# Out of conveience, you can simply take the max of the field with:
print(field.max().data)

# The above yields a result identical to:
print(np.max(field.data, axis=0))

###############################################################################
# Note that the numpy array does not retain any information about the
# field it describes. Using the DPF ``max`` operator of the field does
# retain this information.
max_field = field.max()
print(max_field)
