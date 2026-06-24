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
.. _ref_tutorials_extract_and_explore_results_metadata:

Extract and explore results metadata
=====================================

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

This tutorial shows how to extract and explore results metadata from a result file.
"""
###############################################################################
# Get the result file
# -------------------
#
# Import a result file. For this tutorial, use one available in the
# :mod:`examples<ansys.dpf.core.examples>` module. For more information about how
# to import your own result file in DPF, see the
# :ref:`ref_tutorials_import_result_file` tutorial.

# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf

# Import the operators and examples module
from ansys.dpf.core import examples

# Define the result file path
result_file_path_1 = examples.download_transient_result()

# Create the model
model_1 = dpf.Model(data_sources=result_file_path_1)

###############################################################################
# Explore the results general metadata
# -------------------------------------
#
# Use the :class:`ResultInfo<ansys.dpf.core.result_info.ResultInfo>` object and its
# methods to explore the general results metadata before extracting results.
# This metadata includes:
#
# - Analysis type
# - Physics type
# - Number of results
# - Unit system
# - Solver version, date, and time
# - Job name

result_info_1 = model_1.metadata.result_info

# Get the analysis type
analysis_type = result_info_1.analysis_type
print("Analysis type: ", analysis_type, "\n")

# Get the physics type
physics_type = result_info_1.physics_type
print("Physics type: ", physics_type, "\n")

# Get the number of available results
number_of_results = result_info_1.n_results
print("Number of available results: ", number_of_results, "\n")

###############################################################################
# .. seealso::
#
#     :ref:`ref_tutorials_import_data_streams_for_multiple_operators`
#         If you plan to iterate over ``available_results`` and evaluate each
#         result operator in a loop, use a ``StreamsContainer`` to avoid
#         repeated file reads and mesh reloads.

# Get the unit system
unit_system = result_info_1.unit_system
print("Unit system: ", unit_system, "\n")

# Get the solver version, date, and time
solver_version = result_info_1.solver_version
solver_date = result_info_1.solver_date
solver_time = result_info_1.solver_time
print("Solver version: ", solver_version, "\n")
print("Solver date: ", solver_date, "\n")
print("Solver time: ", solver_time, "\n")

# Get the job name
job_name = result_info_1.job_name
print("Job name: ", job_name, "\n")

###############################################################################
# Explore a result's metadata
# ----------------------------
#
# When you extract a result from a result file, DPF stores it in a
# :class:`Field<ansys.dpf.core.field.Field>`. This ``Field`` contains metadata
# describing the result, including:
#
# - Location
# - Scoping (type and quantity of entities)
# - Elementary data count (number of entities, i.e. how many data vectors)
# - Components count (vectors dimension)
# - Shape of the stored data (tuple of elementary data count and components count)
# - Fields size (length of the entire data vector)
# - Units of the data
#
# Extract the displacement results.

disp_results = model_1.results.displacement.eval()
disp_field = disp_results[0]

###############################################################################
# Explore the displacement results metadata.

# Get the location of the displacement data
location = disp_field.location
print("Location: ", location, "\n")

# Get the displacement Field scoping
scoping = disp_field.scoping
print("Scoping: ", "\n", scoping, "\n")

# Get the displacement Field scoping ids
scoping_ids = disp_field.scoping.ids
print("Scoping ids: ", scoping_ids, "\n")

# Get the displacement Field elementary data count
elementary_data_count = disp_field.elementary_data_count
print("Elementary data count: ", elementary_data_count, "\n")

# Get the displacement Field components count
components_count = disp_field.component_count
print("Components count: ", components_count, "\n")

# Get the displacement Field size
field_size = disp_field.size
print("Size: ", field_size, "\n")

# Get the displacement Field shape
shape = disp_field.shape
print("Shape: ", shape, "\n")

# Get the displacement Field unit
unit = disp_field.unit
print("Unit: ", unit, "\n")
