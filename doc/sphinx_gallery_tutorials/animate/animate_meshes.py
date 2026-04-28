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

:bdg-mapdl:`MAPDL`

This tutorial shows how to animate a |MeshesContainer| — a collection of
mesh subdomains indexed by a label — so that each frame renders one subdomain.

A common use case is visualizing how a mesh is partitioned: for example, by
material or by element shape. The animation reveals each partition in sequence,
which is useful for model inspection and quality control. Optionally, a matching
|FieldsContainer| can be supplied to color each subdomain by a result quantity.
"""
###############################################################################
# Load the model and extract the mesh
# ------------------------------------
#
# This tutorial uses a multi-shell model available in the
# :mod:`examples<ansys.dpf.core.examples>` module.
# For more information on loading your own result files, see the
# :ref:`ref_tutorials_import_data` section.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# switch to model from Ricardo with adaptive remeshing
result_file = examples.find_multishells_rst()
my_model = dpf.Model(data_sources=result_file)
my_mesh = my_model.metadata.meshed_region
print(my_mesh)

###############################################################################
# Split the mesh by material
# ---------------------------
#
# Use :class:`split_mesh<ansys.dpf.core.operators.mesh.split_mesh>` to
# partition the full mesh by the ``"mat"`` property. The result is a
# |MeshesContainer| with one :class:`MeshedRegion<ansys.dpf.core.MeshedRegion>`
# entry per distinct material ID.

split_op = dpf.operators.mesh.split_mesh(mesh=my_mesh, property="mat")
my_mc = split_op.eval()
print(my_mc)

###############################################################################
# Inspect the container
# ----------------------
#
# Check the label and the number of sub-meshes to understand the structure
# of the container before animating it.

label = my_mc.labels[0]
label_scoping = my_mc.get_label_scoping(label=label)
print(f"Label: '{label}',  IDs: {label_scoping.ids}")

###############################################################################
# Animate the geometry
# ---------------------
#
# Call :func:`MeshesContainer.animate()<ansys.dpf.core.MeshesContainer.animate>`
# with the label to animate over. Each frame renders the mesh subdomain for one
# label ID. When no |FieldsContainer| is provided, every subdomain is rendered
# with a distinct random color.
#
# .. note::
#
#     ``animate()`` constructs an internal DPF
#     :class:`Workflow<ansys.dpf.core.workflow.Workflow>` that runs on the
#     server side. Each frame extracts the sub-mesh for one label ID and merges
#     it into a single :class:`MeshedRegion<ansys.dpf.core.MeshedRegion>` for
#     rendering.

my_mc.animate(label=label)

###############################################################################
# Animate colored by a result
# ----------------------------
#
# Supply a |FieldsContainer| to the ``fields_container`` parameter to color each
# mesh subdomain by a result quantity. The container must share the same label
# and IDs as ``my_mc``.
#
# Here the displacement is evaluated on the split mesh so that every
# per-material sub-mesh has a corresponding displacement field.

disp_op = dpf.operators.result.displacement(
    data_sources=my_model.metadata.data_sources,
    mesh=my_mc,
)
disp_fc = disp_op.outputs.fields_container()
print(disp_fc)

my_mc.animate(label=label, fields_container=disp_fc)

###############################################################################
# Save the animation
# -------------------
#
# Pass a file path to ``save_as`` to write the animation to disk. Accepted
# extensions are ``.gif``, ``.avi``, and ``.mp4``.

my_mc.animate(
    label=label,
    fields_container=disp_fc,
    save_as="animate_meshes.gif",
)
