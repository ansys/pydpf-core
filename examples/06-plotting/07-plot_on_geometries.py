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
.. _plot_on_geometries:

Plot on geometry elements
~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to plot a certain field in different geometric
objects such as points, lines and planes.

"""


###############################################################################
# Imports and load model
# ~~~~~~~~~~~~~~~~~~~~~~
# Import modules and set context as Premium.

import matplotlib.pyplot as plt
import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops
from ansys.dpf.core.fields_factory import field_from_array
from ansys.dpf.core.geometry import Line, Plane, Points
from ansys.dpf.core.plotter import DpfPlotter

###############################################################################
# Load model from examples and print information:
model = dpf.Model(examples.find_static_rst())
print(model)

###############################################################################
# Load model's mesh and define camera position
# (obtained with ``cpos=pl.show_figure(return_cpos=True)``). This will be used
# later for plotting.
mesh = model.metadata.meshed_region
cpos = [
    (0.07635352356975698, 0.1200500294271993, 0.041072502929096165),
    (0.015, 0.045, 0.015),
    (-0.16771051558419411, -0.1983722658245161, 0.9656715938216944),
]

###############################################################################
# Create points, line and plane objects
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create 8 points in the corners and one in the middle:
points = Points(
    [
        [0.0, 0.03, 0.0],
        [0.0, 0.03, 0.03],
        [0.0, 0.06, 0.00],
        [0.0, 0.06, 0.03],
        [0.03, 0.03, 0.0],
        [0.03, 0.03, 0.03],
        [0.03, 0.06, 0.00],
        [0.03, 0.06, 0.03],
        [0.015, 0.045, 0.015],
    ]
)

###############################################################################
# Show points together with the mesh
points.plot(mesh, cpos=cpos, point_size=15, color="blue")

###############################################################################
# Create line passing through the geometry's diagonal:
line = Line([[0.03, 0.03, 0.05], [0.0, 0.06, 0.0]], n_points=50)

###############################################################################
# Show line with the 3D mesh
line.plot(mesh, cpos=cpos, color="black")

###############################################################################
# Create vertical plane passing through the mid point:
plane = Plane(
    [0.015, 0.045, 0.015],
    [1, 1, 0],
    width=0.03,
    height=0.03,
    n_cells_x=10,
    n_cells_y=10,
)

###############################################################################
# Show plane with the 3D mesh
plane.plot(mesh, cpos=cpos, color="red")

###############################################################################
# Map displacement field to geometry objects
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get displacement field from model:
disp = model.results.displacement

###############################################################################
# Map displacement to points in Points object:
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=field_from_array(points.coordinates.data),
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_points = fields_mapped[0]

###############################################################################
# Map displacement to points in Line object:
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=line.mesh.nodes.coordinates_field,
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_line = fields_mapped[0]

###############################################################################
# Map displacement to points in Plane object:
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=plane.mesh.nodes.coordinates_field,
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_plane = fields_mapped[0]

###############################################################################
# Plotting displacement field on the geometry objects
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3D plot of Points and display mesh:
pl = DpfPlotter()
pl.add_field(field_points, render_points_as_spheres=True, point_size=10)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)

###############################################################################
# 3D plot of Line and mesh.
# Note that the line is only displayed if some points are found inside the mesh:
pl = DpfPlotter()
if not len(field_line) == 0:
    pl.add_field(field_line, line.mesh, line_width=5)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)

###############################################################################
# Plot Plane and display mesh in background.
# Note that the plane is only displayed if some points are found inside the mesh:
pl = DpfPlotter()
if not len(field_plane) == 0:
    pl.add_field(field_plane, plane.mesh, show_edges=False)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)

###############################################################################
# 2D plot (graph) of Line (line length vs displacement field):
norm_disp = [np.linalg.norm(field_line.data[i]) for i in range(len(field_line.data))]
path = line.path[field_line.scoping.ids - 1]
plt.plot(path, norm_disp)
plt.xlabel("Line length")
plt.ylabel("Displacement norm field")
plt.show()
