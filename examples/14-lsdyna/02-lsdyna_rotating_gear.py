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

"""
.. _lsdyna_rotating_gear:

Rotating gear, fragment containment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This generic rotating gear example demonstrate how to post process with PyDPF-Core in a
cylindrical coordinates system.  It monitors the velocity of a gear fragment in a radial
direction.

.. note::
    This example requires DPF 6.1 (ansys-dpf-server-2023-2-pre0) or above.
    For more information, see :ref:`ref_compatibility`.

"""

import matplotlib.pyplot as plt
from ansys.dpf import core as dpf
from ansys.dpf.core import operators as ops
from ansys.dpf.core import examples
###############################################################################
# d3plot file results extraction
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create the model and print its contents. This LS-DYNA d3plot file contains
# several individual results, each at different times. The d3plot file does not
# contain information related to Units.

# In this case, as the simulation was run  through Mechanical, a ''file.actunits''
# file is produced. If this file is supplemented in the data_sources, the units
# will be correctly fetched for all results in the file as well as for the mesh.

my_data_sources = dpf.DataSources()
ds2 = dpf.DataSources()
my_data_sources.set_result_file_path(
    filepath=r"D:\ANSYSdev\2-MODELISATION_WORKBENCH_EXAMPLES\ayush\aeronautic fragment velocity\GearContainment_IBP.wbpz_files\dp0\SYS-4\MECH\d3plot",
    key="d3plot",
)
my_data_sources.add_file_path(
    filepath=r"D:\ANSYSdev\2-MODELISATION_WORKBENCH_EXAMPLES\ayush\aeronautic fragment velocity\GearContainment_IBP.wbpz_files\dp0\SYS-4\MECH\file.actunits",
    key="actunits",
)
ds2.set_result_file_path(
    filepath=r"D:\ANSYSdev\2-MODELISATION_WORKBENCH_EXAMPLES\ayush\aeronautic fragment velocity\GearContainment_IBP.wbpz_files\dp0\SYS-4\MECH\binout",
    key="binout",
)
my_model = dpf.Model(data_sources=my_data_sources)
my_model2 = dpf.Model(data_sources=ds2)
# print(my_model)
# print(my_model2)
# For a faster performance, we will use streams, so we don't need to read all
# the result files for each operation

my_streams = ops.metadata.streams_provider(data_sources=my_data_sources).eval()

###############################################################################
# Exploring the model
# ~~~~~~~~~~~~~~~~~~~
#
# The model metadata gives us access to the mesh information before extracting the mesh.

# Define the MeshInfo object
my_model_info = my_model.metadata.mesh_info
# Print the available properties
# print(my_model_info)

###############################################################################
# Here, we see that the mesh is divided by parts. The gear broken part has a specific
# id (3) and name (Teeths 2(Mechanical Model)

# Display the mesh parts
print(my_model_info.parts)

###############################################################################
# You can verify the mesh parts in a plot. This part is not mandatory. You can directly extract
# the mesh part of interest.
#
# The :class:`mesh_provider<ansys.dpf.core.operators.mesh.meshes_provider.mesh_provider>` operator
# gets the mesh for the specified part. You can make a loop to obtain separated MeshedRegions for each
# part of the mesh

# Create a MeshesContainer to store the MeshedRegions
my_meshes = dpf.MeshesContainer()
my_meshes.add_label(label="part")

# Create the plot figure. Here each part of the mesh will have a different color
mesh_parts_plot = dpf.plotter.DpfPlotter()
colors = ["red", "green", "blue", "orange", "aqua"]

for i in my_model_info.part_scoping.ids:
    meshed_region_loop = ops.mesh.mesh_provider(
        data_sources=my_data_sources, region_scoping=[i]
    ).eval()
    my_meshes.add_mesh(label_space={"part": i}, mesh=meshed_region_loop)
    mesh_parts_plot.add_mesh(
        meshed_region=meshed_region_loop, color=colors[i - 1], show_edges=False, show_axes=True
    )

mesh_parts_plot.show_figure()
print(my_meshes)
###############################################################################
# The blue part is the one with id=3.  We can confirm that the part 3 is the broken one
###############################################################################
# Extracting only the part of the mesh of interest is useful for the manipulations.
# Thus, we extract the MeshedRegion for the studied gear tooth.
#
# The :class:`mesh_provider<ansys.dpf.core.operators.mesh.meshes_provider.mesh_provider>` operator
# gets the mesh for the specified part.

# Define the MeshedRegion
broken_part_mesh = ops.mesh.mesh_provider(data_sources=my_data_sources, region_scoping=[3]).eval()

###############################################################################
# Extract velocity results
# ~~~~~~~~~~~~~~~~~~~~~~~~
#
# First, extract the mesh scoping from the broken part.

# Define the mesh scoping
broken_part_scoping = ops.scoping.from_mesh(mesh=broken_part_mesh).eval()

###############################################################################
# From the bd3plot file
#
# We have to calculate the velocity as we can't extract it directly from the result file.

# Extract the displacement reesults
disp = my_model.results.displacement(mesh_scoping=broken_part_scoping).eval()

# Extract the displacement reesults time frequencies
my_time_freq_support = my_model.metadata.time_freq_support
time_freqs = my_time_freq_support.time_frequencies

# Inversion of the time
inverso_time_freq = ops.math.pow(field=time_freqs, factor=-1.0).eval()
inverso_time_freq.location = dpf.locations.nodal

# Get the times data and change the first value (so we dont have a division by zero)
list_times = inverso_time_freq.data_as_list
list_times[0] = 0.0


# Change locations
scop_elemental = ops.scoping.transpose(
    mesh_scoping=broken_part_scoping, meshed_region=broken_part_mesh
).eval()
mesh_elemental = ops.mesh.from_scoping(scoping=scop_elemental, mesh=broken_part_mesh).eval()

displacement_elemental = my_model.results.displacement(mesh_scoping=scop_elemental).eval()

vitesse_broken_part_el = dpf.FieldsContainer()
vitesse_broken_part_el.set_labels(["time"])
for i in displacement_elemental.get_time_scoping().ids:
    time = list_times[i - 1]
    field_disp = displacement_elemental.get_field(label_space_or_index={"time": i})
    field_v = ops.math.scale(field=field_disp, ponderation=time).eval()
    vitesse_broken_part_el.add_field(label_space={"time": i}, field=field_v)

# Change coordinates system
v_broken_frag_cyl_coords = ops.geo.rotate_in_cylindrical_cs_fc(field=vitesse_broken_part_el).eval()

# Average by time step

volume_per_element = ops.geo.elements_volume(
    mesh_scoping=scop_elemental, mesh=mesh_elemental
).eval()
volume_total = ops.math.accumulate(fieldA=volume_per_element).eval()
volume_total_int = volume_total.data_as_list[0]
volume_total_inverso = ops.math.pow(field=volume_total, factor=-1.0).eval()

sum_scaled = ops.math.accumulate_fc(
    fields_container=v_broken_frag_cyl_coords, ponderation=volume_per_element
).eval()
v_averaged = ops.math.scale_by_field_fc(
    field_or_fields_container_A=sum_scaled, field_or_fields_container_B=volume_total_inverso
).eval()

# Make a Field by time step instead of a Fields container

time_freqs_n_sets = my_time_freq_support.n_sets
v_part_by_time = dpf.fields_factory.create_3d_vector_field(num_entities=time_freqs_n_sets)
v_part_by_time.location = dpf.locations.time_freq
for i in v_averaged.get_time_scoping().ids:
    v_to_append = v_averaged.get_field(label_space_or_index={"time": i}).data
    v_part_by_time.append(data=v_to_append, scopingid=i)
