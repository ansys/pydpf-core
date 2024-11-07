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

import time
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
ds2 = dpf.DataSources()
ds2.set_result_file_path(
    filepath=r"D:\ANSYSdev\2-MODELISATION_WORKBENCH_EXAMPLES\ayush\aeronautic fragment velocity\GearContainment_IBP.wbpz_files\dp0\SYS-4\MECH\binout",
    key="binout",
)
my_model = dpf.Model(data_sources=my_data_sources)
my_model2 = dpf.Model(data_sources=ds2)
print(my_model)
print(my_model2)
# For a faster performance, we will use streams, so we don't need to read all
# the result files for each operation

my_streams = ops.metadata.streams_provider(data_sources=my_data_sources).eval()

###############################################################################
# Exploring the model
# ~~~~~~~~~~~~~~~~~~~
# The model metadata gives us access to the mesh information. Here we see that the model
# is already divided by parts. Dividing the mesh is useful for the manipulations, here we
# will define the mesh for the studied gear tooth

my_model_info = my_model.metadata.mesh_info
# print(my_model_info.parts)
# print(my_model_info)

###############################################################################
# Here the gear broken part has a specific id and name. If the simulation model is known
# its evident that this part is the part with id '3' and name: Teeths 2(Mechanical Model).
# This can be verified by a plot
# print(my_model_info.part_names.get_entity_data_by_id(id=3))

###############################################################################
# Separate meshes for each part

# The :class:`meshes_provider<ansys.dpf.core.operators.mesh.meshes_provider.meshes_provider>` operator
# gets the mesh for the specified part. You can make a loop to obtain separate meshed regions for each
# part of the model
my_meshes = dpf.MeshesContainer()
my_meshes.add_label(label="part")

# Create the plot figure, here each part of the mesh will have a different color
mesh_parts_plot = dpf.plotter.DpfPlotter()
colors = ["red", "green", "blue", "orange", "aqua"]

# for i in my_model_info.part_scoping.ids:
#     teste = ops.mesh.mesh_provider(streams_container=my_streams, region_scoping=[i]).eval()
#     my_meshes.add_mesh(label_space={"part": i},
#                        mesh=ops.mesh.mesh_provider(data_sources=my_data_sources, region_scoping=[i]).eval())
#
#     mesh_parts_plot.add_mesh(meshed_region=my_meshes.get_mesh(label_space_or_index={"part": i}), color=colors[i-1], show_edges=False,show_axes=True)

# print(my_meshes)
# mesh_parts_plot.show_figure()

# We can confirm that the part 3 is the broken one.

###############################################################################
# Extract velocity results
# ~~~~~~~~~~~~~~~~~~~~~~~~
fragment_mesh = ops.mesh.mesh_provider(data_sources=my_data_sources, region_scoping=[3]).eval()
#
# # Define the fragment scoping
fragment_nodal_scop = ops.scoping.from_mesh(mesh=fragment_mesh).eval()
# fragment_v = ops.result.part_rigid_body_velocity(data_sources=my_data_sources, entity_scoping=dpf.Scoping(ids=[3],location=dpf.locations.zone) ).eval()
# print(fragment_v)
# print(fragment_v[0])
# print(fragment_v[2])
# norm_fc = ops.math.norm(field= fragment_v[0]).eval()
# max_fc = ops.min_max.min_max(field=norm_fc)
# print(max_fc.eval(pin=0))
# print(max_fc.eval(pin=1))
#
#
# # print(norm_fc)
# # cyl = ops.geo.rotate_in_cylindrical_cs_fc(field=fragment_v, mesh=fragment_mesh).eval()
# # print(cyl)
#
# global_v = my_model.results.global_velocity.eval()
#
# # print(global_v[0])
# norm_fc2 = ops.math.norm(field= global_v[0]).eval()
# max_fc2 = ops.min_max.min_max(field=norm_fc2)
# print(max_fc2.eval(pin=0))
# print(max_fc2.eval(pin=1))
#
# mudar_loc = ops.utility.extract_scoping(field_or_fields_container=fragment_v[0]).eval()
# print(mudar_loc)

# test_disp = my_model.results.displacement(mesh_scoping=fragment_nodal_scop).eval()
# temps = my_model.metadata.time_freq_support.time_frequencies

# print(test_disp)
# print(temps)

# nodout_vx = my_model.results.nodout_velocity_x.eval()
# max_nod = ops.min_max.min_max_fc(fields_container=nodout_vx).eval()
# # print(nodout_vx)
# print(max_nod)
