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

# _order: 3
"""
.. _ref_tutorials_plot_contour:

Plot contours
=============

This tutorial shows different commands for plotting data contours on meshes.

PyDPF-Core has a variety of plotting methods for generating 3D plots with Python.
These methods use VTK and leverage the `PyVista <https://github.com/pyvista/pyvista>`_ library.
"""
###############################################################################
# Load data to plot
# ------------------
#
# Load a result file in a model
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

import ansys.dpf.core as dpf
from ansys.dpf.core import examples, operators as ops

result_file_path_1 = examples.download_piston_rod()
model_1 = dpf.Model(data_sources=result_file_path_1)

###############################################################################
# Extract data for the contour
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# For more information about extracting results from a result file, see the
# :ref:`ref_tutorials_import_data` tutorials section.
#
# .. note::
#
#     Only the ``elemental`` or ``nodal`` locations are supported for plotting.
#
# Here, we choose to plot the XX component of the stress tensor.

stress_XX_op = ops.result.stress_X(data_sources=model_1)

# The default behavior is to return data as ElementalNodal
print(stress_XX_op.eval())

###############################################################################
# Request the stress in a ``nodal`` location (the default ``ElementalNodal``
# location is not supported for plotting). We define the new location using
# the operator input. Another option would be using the
# :class:`to_nodal_fc<ansys.dpf.core.operators.averaging.to_nodal_fc.to_nodal_fc>`
# averaging operator on the output of the stress operator.

stress_XX_op.inputs.requested_location(dpf.locations.nodal)
stress_XX_fc = stress_XX_op.eval()

###############################################################################
# Extract the mesh
# ^^^^^^^^^^^^^^^^

meshed_region_1 = model_1.metadata.meshed_region

###############################################################################
# Plot a contour of a single field
# ---------------------------------
#
# There are three methods to plot a single
# :class:`Field<ansys.dpf.core.field.Field>`:
#
# - :py:meth:`Field.plot()<ansys.dpf.core.field.Field.plot>`
# - :py:meth:`MeshedRegion.plot()<ansys.dpf.core.meshed_region.MeshedRegion.plot>`
#   with the field as argument
# - :class:`DpfPlotter<ansys.dpf.core.plotter.DpfPlotter>` with
#   :py:meth:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>`
#   (more performant)
#
# Get a single field from the ``FieldsContainer``.

stress_XX = stress_XX_fc[0]

###############################################################################
# Plot using ``Field.plot()``
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# If the :class:`Field<ansys.dpf.core.field.Field>` does not have an associated
# mesh support (see
# :py:attr:`Field.meshed_region<ansys.dpf.core.field.Field.meshed_region>`),
# provide a mesh with the ``meshed_region`` argument.

stress_XX.plot(meshed_region=meshed_region_1)

###############################################################################
# Plot using ``MeshedRegion.plot()``
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Use the ``field_or_fields_container`` argument to pass the field.

meshed_region_1.plot(field_or_fields_container=stress_XX)

###############################################################################
# Plot using ``DpfPlotter``
# ^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# 1. Create an instance of
#    :class:`DpfPlotter<ansys.dpf.core.plotter.DpfPlotter>`.
# 2. Add the field using
#    :py:meth:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>`.
#    If the field has no associated mesh support, provide a mesh with the
#    ``meshed_region`` argument.
# 3. Render and show the figure using
#    :py:meth:`show_figure()<ansys.dpf.core.plotter.DpfPlotter.show_figure>`.
#
# You can also first call
# :py:meth:`add_mesh()<ansys.dpf.core.plotter.DpfPlotter.add_mesh>` to add the
# mesh and then call ``add_field()`` without the ``meshed_region`` argument.

plotter_1 = dpf.plotter.DpfPlotter()
plotter_1.add_field(field=stress_XX, meshed_region=meshed_region_1)
plotter_1.show_figure()

###############################################################################
# Plot a contour of multiple fields
# ----------------------------------
#
# Prepare a collection of fields
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# .. warning::
#
#     The fields should not have conflicting data — you cannot build a contour for
#     two fields with two different sets of data for the same mesh entities
#     (intersecting scopings). These methods are therefore not available for a
#     collection of fields varying across time, or for different shell layers of
#     the same elements.
#
# Here we split the field for XX stress based on material to get a collection of
# fields with non-conflicting associated mesh entities.
#
# We use the
# :class:`split_fields<ansys.dpf.core.operators.mesh.split_fields.split_fields>`
# operator together with the
# :class:`split_mesh<ansys.dpf.core.operators.mesh.split_mesh.split_mesh>`
# operator. For MAPDL results, a split on material is equivalent to a split on
# bodies.

fields = (
    ops.mesh.split_fields(
        field_or_fields_container=stress_XX_fc,
        meshes=ops.mesh.split_mesh(mesh=meshed_region_1, property="mat"),
    )
).eval()
print(fields)

###############################################################################
# Plot the contour using ``FieldsContainer.plot()``
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Use
# :py:meth:`FieldsContainer.plot()<ansys.dpf.core.fields_container.FieldsContainer.plot>`.

fields.plot()

###############################################################################
# The ``label_space`` argument provides further field filtering capabilities.

fields.plot(label_space={"mat": 1})

###############################################################################
# Plot the contour using ``MeshedRegion.plot()``
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Use the ``field_or_fields_container`` argument.

meshed_region_1.plot(field_or_fields_container=fields)

###############################################################################
# Plot the contour using ``DpfPlotter``
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Add each field individually using
# :py:meth:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>`.

plotter_2 = dpf.plotter.DpfPlotter()
plotter_2.add_field(field=fields[0])
plotter_2.add_field(field=fields[1])
plotter_2.show_figure()
