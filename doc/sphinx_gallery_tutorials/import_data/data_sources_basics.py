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

# _order: 7
"""
.. _ref_tutorials_import_data_data_sources_basics:

Build and use a DataSources object
===================================

Learn how to describe result files to DPF with a |DataSources| object.

|DataSources| is the container that tells DPF which files contain the data to
read. This tutorial shows how to register a main result file, attach a
secondary file from the same analysis, and pass the object to a |Model| or an
individual result operator.

When a file extension is ambiguous or has no extension, provide an explicit
file key. For distributed result files, provide a domain ID as well. When files
belong to different analyses, use an upstream |DataSources| object instead of
adding every file to one flat collection.

.. seealso::

    :ref:`ref_tutorials_import_data_data_sources_upstream`
        Learn how to connect DataSources objects for multi-analysis workflows.
"""
###############################################################################
# Import the PyDPF-Core modules
# -----------------------------
#
# Import the DPF API, result operators, and example-file helpers.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Register a main result file
# ---------------------------
#
# A DataSources object represents the files that make up one analysis. The
# constructor can register the main result file immediately. The explicit
# ``d3plot`` key selects the LS-DYNA result reader because this file has no
# conventional result extension.

# Download a result file and its accessory units file
result_file_paths = examples.download_d3plot_beam()
main_result_file = result_file_paths[0]
units_file = result_file_paths[3]

# Create the DataSources object with its main result file
my_data_sources = dpf.DataSources(result_path=main_result_file, key="d3plot")

###############################################################################
# Add a secondary file from the same analysis
# --------------------------------------------
#
# Secondary files contain supporting information that is not stored in the main
# result file. Attach them with ``add_file_path()`` and use their file key when
# the extension must be specified explicitly.

# Add the units file belonging to the same analysis
my_data_sources.add_file_path(filepath=units_file, key="actunits")

# Inspect the main result key and its registered path
print("Main result key:", my_data_sources.result_key)
print("Main result files:", my_data_sources.result_files)

###############################################################################
# Give DataSources to a Model
# ---------------------------
#
# Pass the DataSources object to a Model when you want DPF to expose common
# metadata, mesh, and result helpers for the analysis.

# Create a Model from the DataSources object
my_model = dpf.Model(data_sources=my_data_sources)
print("Model:", my_model)

###############################################################################
# Give DataSources to an operator
# -------------------------------
#
# You can also connect the same DataSources object directly to an operator. This
# is useful when you need one focused result without creating a full Model.

# Create a displacement operator and connect its data source input
displacement_op = ops.result.displacement()
displacement_op.inputs.data_sources.connect(my_data_sources)
displacement_fc = displacement_op.outputs.fields_container()
print("Displacement fields:", displacement_fc)

###############################################################################
# Use an explicit key and domain IDs
# ----------------------------------
#
# A key identifies which reader should interpret a file. A domain ID identifies
# which part of a distributed solve produced a file. Set both when a result set
# is split across domain-specific files.

# Download two domain result files
domain_files = examples.download_distributed_files()

# Register one result file per domain with an explicit key
distributed_data_sources = dpf.DataSources()
distributed_data_sources.set_domain_result_file_path(path=domain_files[0], key="rst", domain_id=0)
distributed_data_sources.set_domain_result_file_path(path=domain_files[1], key="rst", domain_id=1)
print("Distributed DataSources:", distributed_data_sources)
