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
.. _ref_tutorials_main_steps:

Postprocessing main steps
=========================

There are four main steps to transform simulation data into output data that can
be used to visualize and analyze simulation results:

1. Import and open results files
2. Access and extract results
3. Transform available data
4. Visualize the data
"""
###############################################################################
# 1- Import and open results files
# ---------------------------------
#
# First, import the DPF-Core module as ``dpf`` and import the included examples file.

# Import the ansys.dpf.core module as ``dpf``
from ansys.dpf import core as dpf

# Import the examples module
# Import the operators module
from ansys.dpf.core import examples, operators as ops

###############################################################################
# :class:`DataSources <ansys.dpf.core.data_sources.DataSources>` is a class that
# manages paths to their files. Use this object to declare data inputs for DPF
# and define their locations.

# Define the DataSources object
my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())

###############################################################################
# The :class:`Model <ansys.dpf.core.model.Model>` class creates and evaluates
# common readers for the files it is given, such as a mesh provider, a result
# info provider, and a streams provider. It provides dynamically built methods
# to extract the results available in the files, as well as many shortcuts to
# facilitate exploration of the available data.
#
# Printing the model displays:
#
#   - Analysis type
#   - Available results
#   - Size of the mesh
#   - Number of results

# Define the Model object
my_model = dpf.Model(data_sources=my_data_sources)
print(my_model)

###############################################################################
# 2- Access and extract results
# -----------------------------
#
# We see in the model that a displacement result is available. You can access
# this result by:

# Define the displacement results through the model property `results`
my_displacements = my_model.results.displacement.eval()
print(my_displacements)

###############################################################################
# The displacement data can be extracted by:

# Extract the data of the displacement field
my_displacements_0 = my_displacements[0].data
print(my_displacements_0)

###############################################################################
# 3- Transform available data
# ---------------------------
#
# Several transformations can be made with the data. They can be a single
# operation, by using only one operator, or they can represent a succession of
# operations, by defining a workflow with chained operators.
#
# Here we start by computing the displacements norm.

# Define the norm operator (here for a fields container) for the displacement
my_norm = ops.math.norm_fc(fields_container=my_displacements).eval()
print(my_norm[0].data)

###############################################################################
# Then we compute the maximum values of the normalised displacement.

# Define the maximum operator and chain it to the norm operator
my_max = ops.min_max.min_max_fc(fields_container=my_norm).outputs.field_max()
print(my_max)

###############################################################################
# 4- Visualize the data
# ----------------------
#
# Plot the transformed displacement results.

# Define the support of the plot (here we plot the displacement over the mesh)
my_model.metadata.meshed_region.plot(field_or_fields_container=my_displacements)
