"""
.. _plot_on_geometries:

Plot on geometry elements
~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to plot a certain field in different geometric
objects such as points, lines and planes.

.. note::
    This example requires the Premium ServerContext.
    For more information, see :ref:`user_guide_server_context`.

"""


###############################################################################
# Imports and load model
# ~~~~~~~~~~~~~~~~~~~~~~
# Import modules and set context as Premium.

import numpy as np
import matplotlib.pyplot as plt

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops
from ansys.dpf.core.geometry import Line, Plane, Points
from ansys.dpf.core.plotter import DpfPlotter
from ansys.dpf.core.fields_factory import field_from_array

dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

###############################################################################
# Load model from examples and print information:
model = dpf.Model(examples.find_static_rst())
print(model)

###############################################################################
# Load model's mesh and displacement field. Also, define the camera position
# (obtained with ``cpos=pl.show_figure(return_cpos=True)``). This will be used
# later for plotting.
disp = model.results.displacement
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
# points.plot(mesh, cpos=cpos)

###############################################################################
# Create line passing through the geometry's diagonal:
line = Line([[0.03, 0.03, 0.05], [0.0, 0.06, 0.0]], n_points=50)

###############################################################################
# Show line with the 3D mesh
# line.plot(mesh, cpos=cpos)

###############################################################################
# Create vertical plane passing through the mid point:
plane = Plane(
    [0.015, 0.045, 0.015],
    [1, 1, 1],
    width=0.03,
    height=0.03,
    n_cells_x=10,
    n_cells_y=10,
)

###############################################################################
# Show plane with the 3D mesh
# plane.plot(mesh, cpos=cpos)

###############################################################################
# Map displacement field to Points
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use ``on_coordinates`` mapping opretor:
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=field_from_array(points.coordinates.data),
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_points = fields_mapped[0]

###############################################################################
# Map displacement field to Line
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use ``on_coordinates`` mapping opretor:
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=line.mesh.nodes.coordinates_field,
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_line = fields_mapped[0]

###############################################################################
# Map displacement field to Plane
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Steps to get the displacements on the plane are:
#
# 1. Get the levelset of the plane with respect to the mesh nodes
# 2. Use the plane's levelset to obtain intersection with the 3D mesh
# 3. Add the intersection to the plane
# 4. Map displacement field to all points (the ones inside the mesh and the ones
# in the intersection)
#
# Obtain the levelset of the plane with respect to the mesh nodes
origin = dpf.Field(1, dpf.natures.vector)
origin.append(plane.center, 0)

change_location_op = ops.utility.change_location()
change_location_op.inputs.field.connect(origin)
change_location_op.inputs.new_location.connect("overall")
origin_overall = change_location_op.outputs.field()

normal = dpf.Field(1, dpf.natures.vector, dpf.locations.overall)
normal.append(plane.normal_dir, 0)

change_location_op = ops.utility.change_location()
change_location_op.inputs.field.connect(normal)
change_location_op.inputs.new_location.connect("overall")
normal_overall = change_location_op.outputs.field()

levelset_op = ops.mesh.make_plane_levelset()
levelset_op.inputs.coordinates.connect(mesh.nodes.coordinates_field)
levelset_op.inputs.origin.connect(origin_overall)
levelset_op.inputs.normal.connect(normal_overall)
levelset = levelset_op.outputs.field()

###############################################################################
# Use the plane's levelset to obtain intersection with the 3D mesh
mesh_cutter_op = ops.mesh.mesh_cut()
mesh_cutter_op.inputs.field.connect(levelset)
mesh_cutter_op.inputs.iso_value.connect(float(0))
mesh_cutter_op.inputs.closed_surface.connect(float(0))
mesh_cutter_op.inputs.slice_surfaces.connect(True)
intersection = mesh_cutter_op.outputs.mesh()


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
