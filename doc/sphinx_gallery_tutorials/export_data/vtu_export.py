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

# _order: 2
"""
.. _ref_tutorials_export_data_vtu_export:

Export DPF Objects to VTU
==========================

Export DPF data objects (mesh and fields) directly to VTU format using the
``vtu_export`` operator for fine-grained control over what gets exported.

The ``vtu_export`` operator is ideal when you have already processed or modified
data in DPF: filtered, averaged, transformed, or assembled from multiple sources.
Unlike ``migrate_to_vtu``, which exports directly from result files, this operator
works from DPF objects (|MeshedRegion| and |Field|/|FieldsContainer|).
You can use it to export custom computed fields as well as data that does not
come directly from simulation files.

.. note::

    Use ``vtu_export`` when working with processed DPF objects or custom
    workflows. To export entire result files without preprocessing, see
    :ref:`ref_tutorials_export_data_migrate_to_vtu`.
"""

###############################################################################
# Import Required Modules
# -----------------------
#
# Import the required modules.

from pathlib import Path

import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Set Up the Model
# ----------------
#
# Load a static structural result file and extract the |MeshedRegion| that
# will be reused throughout this tutorial.

# Load the result file and create a Model
result_file = examples.find_static_rst()
my_model = dpf.Model(data_sources=dpf.DataSources(result_path=result_file))

# Get the MeshedRegion
mesh = my_model.metadata.meshed_region

###############################################################################
# Basic VTU Export
# ----------------
#
# Export a mesh and |FieldsContainer| that you have already loaded in DPF.

# Get displacement results as a FieldsContainer for all time steps
displacement_fc = my_model.results.displacement.on_all_time_freqs.eval()

# Create the output directory
output_dir = "./dpf_objects_export"
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Create the vtu_export operator
export_op = ops.serialization.vtu_export(
    directory=output_dir,
    mesh=mesh,
    fields1=displacement_fc,
    base_name="displacement_results",
)

# Execute the export and retrieve the output DataSources
export_op.eval()

# List the exported files from the output directory
exported_files = list(Path(output_dir).glob("*.vtu"))
print(f"Exported {len(exported_files)} VTU file(s)")
for path in exported_files[:3]:
    print(f"  {path}")

###############################################################################
# Export Multiple Field Types
# ---------------------------
#
# Export multiple field types (displacement, stress, etc.) simultaneously by
# using both the ``fields1`` and ``fields2`` input pins.

# Create the output directory
output_dir_multi = "./multi_field_export"
Path(output_dir_multi).mkdir(parents=True, exist_ok=True)

# Get stress results for all time steps (elemental_nodal location)
stress_fc = my_model.results.stress.on_all_time_freqs.eval()

# Average elemental_nodal stress to nodal location — vtu_export requires
# Nodal or Elemental data, not elemental_nodal
stress_nodal_fc = ops.averaging.elemental_nodal_to_nodal_fc(fields_container=stress_fc).eval()

# Create the vtu_export operator with multiple fields
export_multi = ops.serialization.vtu_export(
    directory=output_dir_multi,
    mesh=mesh,
    fields1=displacement_fc,
    fields2=stress_nodal_fc,
    base_name="multi_field_results",
)

# Execute the export
export_multi.eval()

print(
    f"Exported {len(list(Path(output_dir_multi).glob('*.vtu')))} "
    "VTU file(s) with displacement and stress"
)

###############################################################################
# Export Processed Data
# ---------------------
#
# Export data that was processed through DPF operators. Here, the von Mises
# equivalent stress is computed from the stress |FieldsContainer| before export.

# Create the output directory
output_dir_processed = "./processed_export"
Path(output_dir_processed).mkdir(parents=True, exist_ok=True)

# Compute the Von Mises equivalent stress from the stress FieldsContainer
# von_mises_eqv_fc on elemental_nodal stress produces elemental_nodal scalars;
# average to nodal location before export
von_mises_en_fc = ops.invariant.von_mises_eqv_fc(fields_container=stress_fc).eval()
von_mises_fc = ops.averaging.elemental_nodal_to_nodal_fc(fields_container=von_mises_en_fc).eval()

# Export the processed Von Mises stress FieldsContainer
export_processed = ops.serialization.vtu_export(
    directory=output_dir_processed,
    mesh=mesh,
    fields1=von_mises_fc,
    base_name="von_mises_stress",
)

export_processed.eval()

print(
    f"Exported Von Mises stress to {len(list(Path(output_dir_processed).glob('*.vtu')))} VTU file(s)"
)

###############################################################################
# Export a Single Time Step
# -------------------------
#
# Export only a specific time step by working with an individual |Field|
# instead of a |FieldsContainer|.

# Create the output directory
output_dir_single = "./single_timestep_export"
Path(output_dir_single).mkdir(parents=True, exist_ok=True)

# Get displacement for only the first time step
time_scoping = dpf.Scoping(location=dpf.locations.time_freq)
time_scoping.ids = [1]

displacement_single_fc = my_model.results.displacement.on_time_scoping(time_scoping).eval()

# Get the first Field from the FieldsContainer
disp_field = displacement_single_fc[0]

# Export the single Field
export_single = ops.serialization.vtu_export(
    directory=output_dir_single,
    mesh=mesh,
    fields1=disp_field,
    base_name="displacement_timestep_1",
)

# Execute the export
export_single.eval()

print(
    f"Exported single time step to {len(list(Path(output_dir_single).glob('*.vtu')))} VTU file(s)"
)

###############################################################################
# Export with Mesh Property Fields
# ---------------------------------
#
# Include mesh |PropertyField| data (such as material IDs) in the VTU output
# by passing it to the ``fields2`` input pin.

# Create the output directory
output_dir_props = "./property_export"
Path(output_dir_props).mkdir(parents=True, exist_ok=True)

# Get the material property field from the MeshedRegion
mat_prop = mesh.property_field("mat")

# Export displacement results together with the material property field
export_props = ops.serialization.vtu_export(
    directory=output_dir_props,
    mesh=mesh,
    fields1=displacement_fc,
    fields2=mat_prop,
    base_name="results_with_material",
)

# Execute the export
export_props.eval()

print(
    f"Exported results with material properties to "
    f"{len(list(Path(output_dir_props).glob('*.vtu')))} VTU file(s)"
)

###############################################################################
# Control Output Format
# ---------------------
#
# Choose different write modes for different trade-offs between file size and
# readability. The ``write_mode`` parameter accepts:
#
# - ``rawbinarycompressed`` (default): Smallest file size
# - ``rawbinary``: Binary format without compression
# - ``base64appended``: Base64-encoded binary data appended to XML
# - ``base64inline``: Base64-encoded binary data inline with XML
# - ``ascii``: Human-readable text format (useful for debugging)

# Create the output directory for format comparison
output_dir_fmt = "./format_comparison"
Path(output_dir_fmt).mkdir(parents=True, exist_ok=True)

# Get a single Field for this comparison
disp_field_fmt = displacement_fc[0]

# Export in compressed binary mode (default)
export_binary = ops.serialization.vtu_export(
    directory=output_dir_fmt,
    mesh=mesh,
    fields1=disp_field_fmt,
    base_name="displacement_binary",
    write_mode="rawbinarycompressed",
)

# Export in ASCII mode for comparison
export_ascii = ops.serialization.vtu_export(
    directory=output_dir_fmt,
    mesh=mesh,
    fields1=disp_field_fmt,
    base_name="displacement_ascii",
    write_mode="ascii",
)

# Execute both exports
export_binary.eval()
export_ascii.eval()

# Compare file sizes
binary_file = next(Path(output_dir_fmt).glob("*binary*.vtu"))
ascii_file = next(Path(output_dir_fmt).glob("*ascii*.vtu"))

print(f"Compressed binary file size: {binary_file.stat().st_size / 1024:.2f} KB")
print(f"ASCII file size:             {ascii_file.stat().st_size / 1024:.2f} KB")

###############################################################################
# Export as Point Cloud
# ---------------------
#
# Set ``as_point_cloud=True`` to export only mesh nodes without element
# connectivity. This is useful for sparse data or particle simulations.

# Create the output directory
output_dir_cloud = "./point_cloud_export"
Path(output_dir_cloud).mkdir(parents=True, exist_ok=True)

# Export displacement as a point cloud (nodes only, no element connectivity)
export_cloud = ops.serialization.vtu_export(
    directory=output_dir_cloud,
    mesh=mesh,
    fields1=disp_field_fmt,
    base_name="displacement_points",
    as_point_cloud=True,
)

# Execute the export
export_cloud.eval()

print(f"Exported point cloud to {len(list(Path(output_dir_cloud).glob('*.vtu')))} VTU file(s)")
print("Note: File contains only point data without element connectivity")

###############################################################################
# Create and Export Custom Data
# -----------------------------
#
# Create a custom scalar |Field| and export it alongside the mesh. Custom fields
# can represent any nodal quantity not available in the original result file.

# Create the output directory
output_dir_custom = "./custom_data_export"
Path(output_dir_custom).mkdir(parents=True, exist_ok=True)

# Create a custom scalar Field associated to mesh nodes
custom_field = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)
custom_field.scoping = mesh.nodes.scoping

# Compute the distance from origin for each node
coords = mesh.nodes.coordinates_field.data
distances = np.sqrt(np.sum(coords**2, axis=1))
custom_field.data = distances

# Name the field so it is identifiable in ParaView or VisIt
custom_field.name = "distance_from_origin"

# Export the custom Field
export_custom = ops.serialization.vtu_export(
    directory=output_dir_custom,
    mesh=mesh,
    fields1=custom_field,
    base_name="custom_distance_field",
)

# Execute the export
export_custom.eval()

print(f"Exported custom field to {len(list(Path(output_dir_custom).glob('*.vtu')))} VTU file(s)")
