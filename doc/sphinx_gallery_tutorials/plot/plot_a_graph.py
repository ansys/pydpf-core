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

# _order: 4
"""
.. _ref_tutorials_plot_graph:

Plot a graph using matplotlib
==============================

This tutorial explains how to plot a graph with data from DPF using
`matplotlib <https://github.com/matplotlib/matplotlib>`_.

The current :class:`DpfPlotter<ansys.dpf.core.plotter.DpfPlotter>` module does not
support graph plots. Instead, use the
`matplotlib <https://github.com/matplotlib/matplotlib>`_ library to plot graphs with
PyDPF-Core.

There is a large range of graphs you can plot. Here, we showcase:

- :ref:`A graph of a result along a path <ref_graph_result_space>`
- :ref:`A graph of transient data <ref_graph_result_time>`
"""
###############################################################################
# .. _ref_graph_result_space:
#
# Result along a path
# --------------------
#
# In this section, we plot the norm of the displacement along a custom path
# represented by a
# :class:`Line<ansys.dpf.core.geometry.Line>`. We first get the data of interest,
# create a custom ``Line`` geometry for the path, map the result on the path, and
# finally create a 2D graph.
#
# Extract the data
# ^^^^^^^^^^^^^^^^^
#
# First, extract the data from a result file.
# For this tutorial we use a case available in the
# :mod:`examples<ansys.dpf.core.examples>` module.

import matplotlib.pyplot as plt

import ansys.dpf.core as dpf
from ansys.dpf.core import examples, geometry as geo, operators as ops

result_file_path_1 = examples.find_static_rst()
model_1 = dpf.Model(data_sources=result_file_path_1)

###############################################################################
# Extract the result of interest — the norm of the displacement field at the
# last step.

disp_results_1 = model_1.results.displacement.eval()
norm_disp = ops.math.norm_fc(fields_container=disp_results_1).eval()

###############################################################################
# Define the path
# ^^^^^^^^^^^^^^^^
#
# Create a path as a
# :class:`Line<ansys.dpf.core.geometry.Line>` passing through the diagonal of
# the mesh.

line_1 = geo.Line(coordinates=[[0.0, 0.06, 0.0], [0.03, 0.03, 0.03]], n_points=50)
line_1.plot(mesh=model_1.metadata.meshed_region)

###############################################################################
# Map the data on the path
# ^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Map the displacement norm field to the path using the
# :class:`on_coordinates<ansys.dpf.core.operators.mapping.on_coordinates.on_coordinates>`
# mapping operator. This operator interpolates field values at given node coordinates,
# using element shape functions.
#
# It takes a :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
# of data, a 3D vector :class:`Field<ansys.dpf.core.field.Field>` of coordinates to
# interpolate at, and an optional
# :class:`MeshedRegion<ansys.dpf.core.meshed_region.MeshedRegion>` to use for element
# shape functions if the first field in the data does not have an associated meshed
# support.

disp_norm_on_path_fc: dpf.FieldsContainer = ops.mapping.on_coordinates(
    fields_container=norm_disp,
    coordinates=line_1.mesh.nodes.coordinates_field,
).eval()
disp_norm_on_path: dpf.Field = disp_norm_on_path_fc[0]
print(disp_norm_on_path)

###############################################################################
# Plot the graph
# ^^^^^^^^^^^^^^
#
# Plot the norm of the displacement field along the path using matplotlib.
#
# Use the
# :py:attr:`Line.path<ansys.dpf.core.geometry.Line.path>` property to get the
# parametric coordinates of the nodes along the line for the X-axis.
# The values in the displacement norm field are in the same order as the parametric
# coordinates because the mapping operator orders output data the same as the input
# coordinates.

line_coordinates = line_1.path

plt.plot(line_coordinates, disp_norm_on_path.data)
plt.xlabel("Position on path")
plt.ylabel("Displacement norm")
plt.title("Displacement norm along the path")
plt.show()

###############################################################################
# .. _ref_graph_result_time:
#
# Transient data
# ---------------
#
# In this section, we plot the minimum and maximum displacement norm over time for a
# transient analysis. For more information about using PyDPF-Core with a transient
# analysis, see the :ref:`static_transient_examples` examples.
#
# We create data for the Y-axis, format the time information for the X-axis, and
# create a 2D graph using both.
#
# Prepare data
# ^^^^^^^^^^^^^
#
# Load a transient case from the
# :mod:`examples<ansys.dpf.core.examples>` module.

result_file_path_2 = examples.download_transient_result()
model_2 = dpf.Model(data_sources=result_file_path_2)

# Check the model is transient via its TimeFreqSupport
print(model_2.metadata.time_freq_support)

###############################################################################
# Extract the displacement field for every time step.

disp_results_2: dpf.FieldsContainer = model_2.results.displacement.on_all_time_freqs.eval()

###############################################################################
# Get the minimum and maximum of the norm of the displacement at each time step
# using the
# :class:`min_max_fc<ansys.dpf.core.operators.min_max.min_max_fc.min_max_fc>` operator.

min_max_op = ops.min_max.min_max_fc(fields_container=ops.math.norm_fc(disp_results_2))

max_disp: dpf.Field = min_max_op.outputs.field_max()
print(max_disp)

min_disp: dpf.Field = min_max_op.outputs.field_min()
print(min_disp)

###############################################################################
# Prepare time values
# ^^^^^^^^^^^^^^^^^^^^
#
# The time or frequency information associated to DPF objects is stored in
# :class:`TimeFreqSupport<ansys.dpf.core.time_freq_support.TimeFreqSupport>` objects.
#
# Use the ``TimeFreqSupport`` of a ``Field`` with location ``time_freq`` to retrieve
# the time or frequency values associated to the entities in its scoping.

time_steps_1: dpf.Field = disp_results_2.time_freq_support.time_frequencies
print(time_steps_1)

# Extract the data of the Field as a plain array
time_data = time_steps_1.data
print(time_data)

###############################################################################
# Plot the graph
# ^^^^^^^^^^^^^^
#
# Use the ``unit`` property of the fields to properly label the axes.

plt.plot(time_data, max_disp.data, "r", label="Max")
plt.plot(time_data, min_disp.data, "b", label="Min")
plt.xlabel(f"Time ({time_steps_1.unit})")
plt.ylabel(f"Displacement ({max_disp.unit})")
plt.legend()
plt.show()
