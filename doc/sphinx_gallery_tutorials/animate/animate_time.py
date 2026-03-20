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
.. _ref_tutorials_animate_time:

Animate data over time
=======================

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

This tutorial demonstrates how to create 3D animations of data in time.

To animate data across time, the data must be stored in a
:class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>` with
a ``time`` label.
"""
###############################################################################
# Get the result files
# ---------------------
#
# For this tutorial, we use a case available in the
# :mod:`examples<ansys.dpf.core.examples>` module.
# For more information about how to import your own result file in DPF, see
# the :ref:`ref_tutorials_import_data` tutorial section.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

result_file_path = examples.find_msup_transient()
model = dpf.Model(data_sources=result_file_path)

###############################################################################
# Define a time scoping
# ----------------------
#
# To animate across time, define the time steps of interest.
# This tutorial retrieves all time steps available in
# :class:`TimeFreqSupport<ansys.dpf.core.time_freq_support.TimeFreqSupport>`,
# but you can also filter them. For more information on how to define a scoping,
# see the ``narrow_down_data`` tutorial in the :ref:`ref_tutorials_import_data`
# section.

time_steps = model.metadata.time_freq_support.time_frequencies

###############################################################################
# Extract the results
# --------------------
#
# Extract the results to animate. In this tutorial, we extract displacement and
# stress results.
#
# .. note::
#
#     Only the ``elemental``, ``nodal``, or ``faces`` locations are supported
#     for animations. ``overall`` and ``elemental_nodal`` locations are not
#     currently supported.
#
# Get the displacement fields (already on nodes) at all time steps.

disp_fc = model.results.displacement(time_scoping=time_steps).eval()
print(disp_fc)

###############################################################################
# Get the stress fields on nodes at all time steps.
# Request ``nodal`` location as the default ``elemental_nodal`` location is not
# supported for animations.

stress_fc = (
    model.results.stress.on_location(location=dpf.locations.nodal)
    .on_time_scoping(time_scoping=time_steps)
    .eval()
)
print(stress_fc)

###############################################################################
# Animate the results
# --------------------
#
# Animate the results with
# :func:`FieldsContainer.animate()<ansys.dpf.core.fields_container.FieldsContainer.animate>`.
# You can animate on a deformed mesh (color map + mesh deformation) or on a
# static mesh (color map only).
#
# Default behavior of ``animate()``:
#
# - Displays the norm of the data components.
# - Displays data at the top layer for shells.
# - Displays the deformed mesh when animating displacements.
# - Displays the static mesh for other result types.
# - Uses a constant uniform scale factor of 1.0 when deforming the mesh.
#
# You can animate any result on a deformed geometry by providing displacement
# results in the ``deform_by`` parameter. It accepts a result object, an
# :class:`Operator<ansys.dpf.core.dpf_operator.Operator>` (must evaluate to a
# ``FieldsContainer`` of the same length), or a ``FieldsContainer`` of the same
# length.
#
# .. note::
#
#     The behavior of ``animate()`` is defined by a
#     :class:`Workflow<ansys.dpf.core.workflow.Workflow>` that it creates
#     internally and feeds to an
#     :class:`Animator<ansys.dpf.core.animator.Animator>`.
#     This workflow loops over a field of frame indices and for each frame
#     generates a field of norm contours to render, as well as a displacement
#     field to deform the mesh if ``deform_by`` is provided.

###############################################################################
# Animate the displacement results — deformed mesh
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

disp_fc.animate()

###############################################################################
# Animate the displacement results — static mesh
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Use ``deform_by=False`` to animate on a static mesh.

disp_fc.animate(deform_by=False)

###############################################################################
# Animate the stress — deformed mesh
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Pass the displacement ``FieldsContainer`` to ``deform_by``.

stress_fc.animate(deform_by=disp_fc)

###############################################################################
# Animate the stress — static mesh

stress_fc.animate()

###############################################################################
# Change the scale factor
# ------------------------
#
# The scale factor can be:
#
# - A single number for uniform constant scaling.
# - A list of numbers (same length as the number of frames) for varying scaling.
#
# Uniform constant scaling
# ^^^^^^^^^^^^^^^^^^^^^^^^^

uniform_scale_factor = 10.0
disp_fc.animate(scale_factor=uniform_scale_factor)

###############################################################################
# Varying scaling
# ^^^^^^^^^^^^^^^^

varying_scale_factor = [float(i) for i in range(len(disp_fc))]
disp_fc.animate(scale_factor=varying_scale_factor)

###############################################################################
# Save the animation
# -------------------
#
# Use the ``save_as`` argument with a target file path. Accepted extensions are
# ``.gif``, ``.avi``, and ``.mp4``.
# For more information see
# `pyvista.Plotter.open_movie
# <https://docs.pyvista.org/api/plotting/_autosummary/pyvista.Plotter.open_movie.html>`_.

stress_fc.animate(deform_by=disp_fc, save_as="animate_stress.gif")

###############################################################################
# Control the camera
# -------------------
#
# Control the camera with the ``cpos`` argument.
#
# A camera position is a combination of a position, a focal point (target),
# and an upwards vector:
#
# .. code-block:: python
#
#    camera_position = [
#        [pos_x, pos_y, pos_z],   # position
#        [fp_x, fp_y, fp_z],      # focal point
#        [up_x, up_y, up_z],      # upwards vector
#    ]
#
# The ``animate()`` method accepts a single camera position or a list of camera
# positions (one per frame).
#
# .. note::
#
#     A useful technique for defining a camera position: do a first interactive
#     plot with ``return_cpos=True``, position the camera as desired, and
#     retrieve the output of the plotting command.
#
# Fixed camera
# ^^^^^^^^^^^^^

cam_pos = [[0.0, 2.0, 0.6], [0.05, 0.005, 0.5], [0.0, 0.0, 1.0]]
stress_fc.animate(cpos=cam_pos)

###############################################################################
# Moving camera
# ^^^^^^^^^^^^^^

import copy

cpos_list = [cam_pos]
for i in range(1, len(disp_fc)):
    new_pos = copy.deepcopy(cpos_list[i - 1])
    new_pos[0][0] += 0.1
    cpos_list.append(new_pos)

stress_fc.animate(cpos=cpos_list)

###############################################################################
# Additional options
# -------------------
#
# You can use additional PyVista arguments, such as:
#
# - ``show_axes=True`` / ``show_axes=False`` to show or hide the coordinate
#   system axis.
# - ``off_screen=True`` to render off-screen for batch animation creation.
# - ``framerate`` to change the frame rate.
# - ``quality`` to change the image quality.
