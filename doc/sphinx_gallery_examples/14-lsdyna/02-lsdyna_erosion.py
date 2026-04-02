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

"""
.. _ref_examples_lsdyna_erosion:

Visualizing Element Erosion in LS-DYNA Impact Simulations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to post-process element erosion in an LS-DYNA d3plot result file,
isolate the surviving mesh, and plot the displacement field on it.

During high-velocity impact simulations, the solver progressively deletes (erodes)
heavily distorted elements. The ``erosion_flag`` result marks each element as active (1)
or eroded (0) at each time step. This workflow filters the active elements, extracts
the corresponding sub-mesh, and visualizes the deformed geometry at the final time step.

.. note::
    This example requires DPF 8.0 (ansys-dpf-server-2024-R2) or above.
    For more information, see :ref:`ref_compatibility`.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Load the LS-DYNA result file
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Load the d3plot file that contains element erosion data and print the model
# contents to inspect the available results and time steps.

d3plot_paths = examples.download_d3plot_erosion()
ds = dpf.DataSources()
ds.set_result_file_path(filepath=d3plot_paths[0], key="d3plot")
my_model = dpf.Model(data_sources=ds)
print(my_model)

###############################################################################
# Extract the erosion flag at the final time step
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The erosion flag is an elemental result: active elements carry a value of 1,
# eroded elements carry a value of 0.

last_step = my_model.metadata.time_freq_support.n_sets
erosion_fc = my_model.results.erosion_flag(time_scoping=[last_step]).eval()
print(erosion_fc)

###############################################################################
# Isolate the non-eroded elements
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Apply a high-pass filter to retain only elements whose flag exceeds 0.5,
# effectively selecting the active (non-eroded) elements.

active_fc = dpf.operators.filter.field_high_pass_fc(
    fields_container=erosion_fc, threshold=0.5
).eval()

# Retrieve the elemental scoping of the surviving elements
active_elemental_scoping = active_fc[0].scoping
print(active_elemental_scoping)

###############################################################################
# Build the non-eroded sub-mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extract the portion of the full mesh that corresponds to the active elements.

full_mesh = my_model.metadata.meshed_region
sub_mesh = dpf.operators.mesh.from_scoping(scoping=active_elemental_scoping, mesh=full_mesh).eval()
sub_mesh.plot(title="Non-eroded mesh at the final time step")

###############################################################################
# Rescope displacement to the non-eroded nodes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Transpose the elemental scoping to the equivalent nodal scoping, then extract
# the displacement and restrict it to the active nodes.

active_nodal_scoping = dpf.operators.scoping.transpose(
    mesh_scoping=active_elemental_scoping, meshed_region=full_mesh
).eval()

disp_fc = my_model.results.displacement(time_scoping=[last_step]).eval()
active_disp_fc = dpf.operators.scoping.rescope_fc(
    fields_container=disp_fc, mesh_scoping=active_nodal_scoping
).eval()

###############################################################################
# Plot the deformed non-eroded mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Display the displacement magnitude on the surviving mesh, deformed according
# to the displacement field. Eroded elements are no longer present in the scene.

sargs = dict(title="Displacement", fmt="%.2e", title_font_size=22, label_font_size=16)
active_disp_fc[0].plot(
    deform_by=active_disp_fc[0],
    scalar_bar_args=sargs,
    text="Non-eroded mesh — deformed by displacement",
)
