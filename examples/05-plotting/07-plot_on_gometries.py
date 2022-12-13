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
# Import modules
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops
from ansys.dpf.core.geometry import Line, Plane
from ansys.dpf.core.plotter import DpfPlotter
from ansys.dpf.core.fields_factory import field_from_array

###############################################################################
# Load model from examples and print information
model = dpf.Model(examples.find_static_rst())
print(model)

###############################################################################
# Create line and plane objects
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create line passing through the geometry's diagional and a plane in the middle
line = Line([[0.0, 0.06, 0.0], [0.03, 0.03, 0.03]])
plane = Plane([0.015, 0.045, 0.015], [0, 1, 0])
plane.discretize(0.015, 0.015, 0.015, resolution=60)

###############################################################################
# Map displacement field to geometry objects
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get displacement field and model's mesh
disp = model.results.displacement
mesh = model.metadata.meshed_region

###############################################################################
# Map values to Line and Plane objects
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp, coordinates=line.path, create_support=True, mesh=mesh
)
fields_mapped = mapping_operator.outputs.fields_container()
field_line = fields_mapped[0]

mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp, coordinates=field_from_array(plane.grid.points), create_support=True, mesh=mesh
)
fields_mapped = mapping_operator.outputs.fields_container()
field_plane = fields_mapped[0]

###############################################################################
# Plotting
# ~~~~~~~~
# Plot displacement field on the geometries and display mesh in background
pl = DpfPlotter()
pl.add_field(field_line)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True)

pl = DpfPlotter()
pl.add_mesh(field_plane.meshed_region, scalars=field_plane.data)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True)

