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
.. _ref_tutorials_export_data_migrate_to_vtu:

Translate Result Files to VTU Format
=====================================

Translate simulation result files to VTU format using the ``migrate_to_vtu``
operator for visualization in VTK-compatible tools like ParaView.

VTU (VTK Unstructured Grid) is an XML-based format that stores mesh geometry
(nodes and element connectivity), field data (displacement, stress, temperature,
etc.), and time series information. The ``migrate_to_vtu`` operator provides a
streamlined workflow to export complete simulation results directly from result
files — it automatically handles mesh conversion, field mapping, and time series
organization.

.. note::

    Use ``migrate_to_vtu`` for quick export of entire result files. To export
    objects you have already processed in DPF, see
    :ref:`ref_tutorials_export_data_vtu_export`.
"""

###############################################################################
# Import Required Modules
# -----------------------
#
# Import the required modules.

from pathlib import Path

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Set Up the Result File
# ----------------------
#
# Download an example result file, create a |DataSources| object, and load a
# |Model| to query result metadata later in this tutorial.

# Download the crankshaft result file
result_file = examples.download_crankshaft()

# Create a DataSources object
ds = dpf.DataSources(result_path=result_file)

# Load a Model to query result metadata
my_model = dpf.Model(data_sources=ds)

###############################################################################
# Export All Results to VTU
# -------------------------
#
# The simplest export provides a |DataSources| object and an output directory.
# The operator exports all available results for all time steps.

# Create the output directory
output_dir = "./crankshaft_export"
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Create the migrate_to_vtu operator
migrate_op = ops.serialization.migrate_to_vtu(
    data_sources=ds,
    directory=output_dir,
)

# Execute the export
migrate_op.eval()

# List the exported VTU files from the output directory
exported_files = list(Path(output_dir).glob("*.vtu"))
print(f"Number of VTU files exported: {len(exported_files)}")
print("\nExported files:")
for path in exported_files:
    print(f"  {path}")

###############################################################################
# Export Specific Time Steps
# --------------------------
#
# Filter which time steps to export by providing a |Scoping| with
# ``location=dpf.locations.time_freq``. This is useful when only specific
# time points from a transient analysis are needed.

# Create the output directory for the filtered export
output_dir_filtered = "./crankshaft_export_filtered"
Path(output_dir_filtered).mkdir(parents=True, exist_ok=True)

# Create a Scoping that targets only the first time step
time_scoping = dpf.Scoping(location=dpf.locations.time_freq)
time_scoping.ids = [1]

# Create the migrate_to_vtu operator with time filtering
migrate_op_filtered = ops.serialization.migrate_to_vtu(
    data_sources=ds,
    time_scoping=time_scoping,
    directory=output_dir_filtered,
    base_name="crankshaft_t1",
)

# Execute the export
migrate_op_filtered.eval()

print(f"Exported {len(list(Path(output_dir_filtered).glob('*.vtu')))} file(s) for time step 1")

###############################################################################
# Customize Output File Naming
# ----------------------------
#
# The ``base_name`` parameter lets you specify a custom prefix for the exported
# VTU files. This is helpful when organizing multiple exports or when you want
# meaningful file names.

# Create the output directory with custom naming
output_dir_custom = "./crankshaft_custom_name"
Path(output_dir_custom).mkdir(parents=True, exist_ok=True)

# Create a Scoping for the first three time steps
time_scoping_3 = dpf.Scoping(location=dpf.locations.time_freq)
time_scoping_3.ids = [1, 2, 3]

# Create the operator with a custom base name
migrate_op_custom = ops.serialization.migrate_to_vtu(
    data_sources=ds,
    time_scoping=time_scoping_3,
    directory=output_dir_custom,
    base_name="my_simulation_results",
)

# Execute the export
migrate_op_custom.eval()

print(f"Exported {len(list(Path(output_dir_custom).glob('*.vtu')))} file(s) with custom naming")

###############################################################################
# Control Output Format
# ---------------------
#
# The ``write_mode`` parameter controls how VTU data is written. Available
# write modes are:
#
# - ``rawbinarycompressed`` (default): Best compression, smallest file size
# - ``rawbinary``: Binary format without compression
# - ``base64appended``: Base64-encoded binary data appended to XML
# - ``base64inline``: Base64-encoded binary data inline with XML
# - ``ascii``: Human-readable text format (useful for debugging, but large files)

# Create the output directory for ASCII export
output_dir_ascii = "./crankshaft_ascii"
Path(output_dir_ascii).mkdir(parents=True, exist_ok=True)

# Export in ASCII mode for debugging
migrate_op_ascii = ops.serialization.migrate_to_vtu(
    data_sources=ds,
    time_scoping=time_scoping,
    directory=output_dir_ascii,
    base_name="crankshaft_ascii",
    write_mode="ascii",
)

# Execute the export
migrate_op_ascii.eval()

# Compare file sizes between the binary and ASCII outputs
binary_file = next(Path(output_dir_filtered).glob("*.vtu"))
ascii_file = next(Path(output_dir_ascii).glob("*.vtu"))

print(f"Binary file size: {binary_file.stat().st_size / 1024:.2f} KB")
print(f"ASCII file size:  {ascii_file.stat().st_size / 1024:.2f} KB")

###############################################################################
# Discover Available Results
# --------------------------
#
# Before exporting specific results, query the result file to see what results
# are available and their corresponding operator names. The operator name is
# the identifier used in the export step below.

# Query available results from the Model metadata
result_info = my_model.metadata.result_info

# Display all available results and their operator names
print(f"{'Result name':<30} {'Operator name':<20} {'Components'}")
print("-" * 60)
for result in result_info.available_results:
    print(f"{result.name:<30} {result.operator_name:<20} {result.n_components}")

###############################################################################
# Export Specific Results
# -----------------------
#
# Select specific results to export by connecting string result identifiers
# (the operator names from the step above) to the ``result1`` and ``result2``
# input pins.

# Create the output directory for selective export
output_dir_selective = "./crankshaft_selective"
Path(output_dir_selective).mkdir(parents=True, exist_ok=True)

# Create the migrate_to_vtu operator
migrate_op_selective = ops.serialization.migrate_to_vtu(
    data_sources=ds,
    time_scoping=time_scoping,
    directory=output_dir_selective,
    base_name="selected_results",
)

# Connect specific results by their operator names
migrate_op_selective.inputs.result1.connect("U")
migrate_op_selective.inputs.result2.connect("S")

# Execute the export
migrate_op_selective.eval()

print(
    f"Exported {len(list(Path(output_dir_selective).glob('*.vtu')))} file(s) with selected results"
)
print("Included results: Displacement (U) and Stress (S)")
