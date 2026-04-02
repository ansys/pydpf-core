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

Projectile-Plate Impact: Post-Processing Element Erosion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example post-processes element erosion in an LS-DYNA d3plot result of a
tungsten-alloy projectile penetrating a steel plate, and plots the surviving mesh
deformed by displacement at the final time step.

Both parts use ``*MAT_PLASTIC_KINEMATIC`` with a failure strain of 0.8, so elements
are progressively deleted on impact. The simulation uses
``*CONTACT_ERODING_SURFACE_TO_SURFACE``, which causes LS-DYNA to write a per-step
element deletion flag to d3plot. DPF exposes that flag as the ``erosion_flag`` result
(active = 1, eroded = 0). The workflow filters the active elements, extracts the
corresponding sub-mesh, and visualizes the deformed geometry at the final time step
(t ≈ 70 µs).

.. note::
    This example requires DPF 8.0 (ansys-dpf-server-2024-R2) or above.
    For more information, see :ref:`ref_compatibility`.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Load the LS-DYNA result file
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The dataset contains 16 output states at roughly 5 µs intervals
# (units: gram, cm, microsecond). Each state is stored in a separate file
# (``ieverp = 1``), so all 17 paths returned by the download helper must be
# present in the same directory for DPF to read the full time history.

d3plot_paths = examples.download_d3plot_projectile()
ds = dpf.DataSources()
ds.set_result_file_path(filepath=d3plot_paths[0], key="d3plot")
my_model = dpf.Model(data_sources=ds)
print(my_model)

###############################################################################
# Extract the erosion flag at the final time step
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The erosion flag is an elemental result: active elements carry a value of 1,
# eroded elements carry a value of 0. State 16 corresponds to t ≈ 70 µs,
# when penetration is complete and erosion is most extensive.

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
sub_mesh.plot(title="Mesh with erosion at the final time step", cpos="xz")

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
# Displacement magnitude on the surviving mesh, deformed according to the
# displacement field. Eroded elements from both the projectile nose and the
# plate penetration zone are absent from the scene.

# sargs = dict(title="Displacement (cm)", fmt="%.2e", title_font_size=22, label_font_size=16)
active_disp_fc[0].plot(
    meshed_region=sub_mesh,
    deform_by=active_disp_fc[0],
    # scalar_bar_args=sargs,
    text="Displacement at t ≈ 70 µs",
    cpos="xz",
)
