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
.. _ref_tutorials_animate_meshes:

Animate a MeshesContainer
==========================

This tutorial shows how to animate a |MeshesContainer|, stepping through its
entries frame by frame. A |MeshesContainer| is a collection of
:class:`MeshedRegion<ansys.dpf.core.MeshedRegion>` objects indexed by one or
more labels. Each entry may have a completely different topology — different
node positions, node counts, or element connectivity.

The tutorial demonstrates how to:

- Retrieve a |MeshesContainer| from a result file.
- Inspect the per-entry mesh topology.
- Plot a single mesh entry.
- Animate all entries, optionally deformed by a nodal result.
"""
###############################################################################
# Load the model
# --------------
#
# Load a structural result file. This example uses a compact-tension specimen
# from a MAPDL fatigue crack-growth analysis where MAPDL remeshes the
# crack-front region at every substep, producing a |MeshesContainer| with a
# different topology at each time set. The model originates from
# `Technology Showcase Example: Fatigue Crack Initiation and Propagation
# <https://ansyshelp.ansys.com/public/account/secured?returnurl=//Views/Secured/corp/v261/en/ans_tec/teccrackinitprop.html>`_
# in the MAPDL documentation.
# The result file is available from the
# :mod:`examples<ansys.dpf.core.examples>` module.
# For more information on loading your own result files, see
# :ref:`ref_tutorials_import_data`.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# result_file = examples.download_ct_crack_growth(return_local_path=True)
result_file = r"D:\ANSYSDev\resources\MAPDL\Technology showcases\td-70\reduced\file.rst"
my_model = dpf.Model(data_sources=result_file)
print(my_model)

###############################################################################
# Retrieve the MeshesContainer
# ----------------------------
#
# When a result file contains per-step topology changes, DPF exposes one
# :class:`MeshedRegion<ansys.dpf.core.MeshedRegion>` per time set inside a
# |MeshesContainer| indexed by the ``"time"`` label. The container is available
# directly from the model metadata. Printing it lists each entry with its node
# and element count, making it easy to see whether the topology varies between
# steps.

my_mc = my_model.metadata.meshes_container
print(my_mc)

###############################################################################
# Plot a single mesh entry
# ------------------------
#
# Retrieve and render one :class:`MeshedRegion<ansys.dpf.core.MeshedRegion>`
# from the container to inspect the geometry before animating.

initial_mesh = my_mc.get_mesh({"time": 1})
initial_mesh.plot(text="Initial mesh", cpos="xy", parallel_projection=True)

###############################################################################
# Extract nodal displacements
# ---------------------------
#
# Retrieve nodal displacements for all time sets. The resulting
# |FieldsContainer| is indexed by the same ``"time"`` label as the
# |MeshesContainer|, so ``animate()`` can automatically match each
# displacement field to its corresponding mesh frame.

disp_fc = my_model.results.displacement.on_all_time_freqs().eval()
print(disp_fc)
import numpy as np

for i, f in enumerate(disp_fc):
    norm = float(np.linalg.norm(f.data))
    print(f"  field {i:2d}: norm={norm:.4e}, n_nodes={f.scoping.size}")
exit()
###############################################################################
# Animate the MeshesContainer
# ---------------------------
#
# Call :func:`MeshesContainer.animate()<ansys.dpf.core.MeshesContainer.animate>`
# to step through all entries. Pass ``deform_by`` to warp each frame by its
# displacement field, and ``scale_factor`` to amplify the deformation so it is
# visually apparent. Pass ``time_freq_support`` to overlay the actual simulation
# time instead of the raw label ID on each frame.

my_mc.animate(
    deform_by=disp_fc,
    scale_factor=10000.0,
    cpos="xy",
    parallel_projection=True,
    time_freq_support=my_model.metadata.time_freq_support,
    # off_screen=True,  # Use ``off_screen`` to run without rendering to the display (e.g. on a headless server)
    save_as="animate_meshes_crack_growth.mp4",  # Use `save_as` to write the animation to disk
)
