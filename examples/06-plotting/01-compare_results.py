# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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
.. _compare_results:

Compare results using the plotter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to plot several mesh/result combinations on the
same plot so that you can compare results at different time steps.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.plotter import DpfPlotter

###############################################################################
# Compare two results
# ~~~~~~~~~~~~~~~~~~~
# Use the :class:`ansys.dpf.core.plotter.DpfPlotter` class to plot two different
# results over the same mesh and compare them.

# Here we create a Model and request its mesh
model = dpf.Model(examples.find_msup_transient())
mesh_set2 = model.metadata.meshed_region

# Then we need to request the displacement for two different time steps
displacement_operator = model.results.displacement()
displacement_operator.inputs.time_scoping.connect([2, 15])
displacement_set2 = displacement_operator.outputs.fields_container()[0]
displacement_set15 = displacement_operator.outputs.fields_container()[1]

###############################################################################
# Use the :class:`ansys.dpf.core.plotter.DpfPlotter` class to add plots for the
# first mesh and the first result.
pl = DpfPlotter()
pl.add_field(displacement_set2, mesh_set2)

# Create a new mesh and translate it along the x axis.
mesh_set15 = mesh_set2.deep_copy()
overall_field = dpf.fields_factory.create_3d_vector_field(1, dpf.locations.overall)
overall_field.append([0.2, 0.0, 0.0], 1)
coordinates_to_update = mesh_set15.nodes.coordinates_field
add_operator = dpf.operators.math.add(coordinates_to_update, overall_field)
coordinates_updated = add_operator.outputs.field()
coordinates_to_update.data = coordinates_updated.data

# Use the :class:`ansys.dpf.core.plotter.DpfPlotter` class to add plots for the
# second mesh and the second result.
pl.add_field(displacement_set15, mesh_set15)
pl.show_figure(show_axes=True)
