"""
.. _plot_on_planes:

Plot on Plane object
~~~~~~~~~~~~~~~~~~~~
This example shows how to plot a Field on a Plane object.

.. note::
    This example requires the Premium ServerContext.
    For more information, see :ref:`user_guide_server_context`.

"""


###############################################################################
# Imports and load model
# ~~~~~~~~~~~~~~~~~~~~~~
# Import modules and set context as Premium.
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops
from ansys.dpf.core.geometry import Plane
from ansys.dpf.core.plotter import DpfPlotter

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
# Create plane passing through the mid point:
plane1 = Plane(
    [0.015, 0.045, 0.015],
    [1, 1, 0],
    width=0.03,
    height=0.03,
    n_cells_x=10,
    n_cells_y=10,
)

plane2 = Plane(
    [0.015, 0.045, 0.015],
    [1, 1, 1],
    width=0.03,
    height=0.03,
    n_cells_x=10,
    n_cells_y=10,
)

###############################################################################
# Show plane with the 3D mesh
plane1.plot(mesh, cpos=cpos)
plane2.plot(mesh, cpos=cpos)

###############################################################################
# Compute intersection plane / mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# First, obtain the levelset of the plane with respect to the mesh using
# :class:`Result <ansys.dpf.core.operators.mesh.make_plane_levelset.make_plane_levelset>:
# A levelset is a scalar Field representing the normal distance between the plane
# and the nodes of the mesh.
# Note that origin and normal must be ``dpf.locations.overall`` 3D vectors.
origin1 = dpf.Field(1, dpf.natures.vector, dpf.locations.overall)
origin1.append(plane1.center, 0)
normal1 = dpf.Field(1, dpf.natures.vector, dpf.locations.overall)
normal1.append(plane1.normal_dir, 0)
origin2 = dpf.Field(2, dpf.natures.vector, dpf.locations.overall)
origin2.append(plane2.center, 0)
normal2 = dpf.Field(1, dpf.natures.vector, dpf.locations.overall)
normal2.append(plane2.normal_dir, 0)

###############################################################################
# Get levelsets
levelset_op = ops.mesh.make_plane_levelset()
levelset_op.inputs.coordinates.connect(mesh.nodes.coordinates_field)
levelset_op.inputs.origin.connect(origin1)
levelset_op.inputs.normal.connect(normal1)
levelset1 = levelset_op.outputs.field()

levelset_op.inputs.origin.connect(origin2)
levelset_op.inputs.normal.connect(normal2)
levelset2 = levelset_op.outputs.field()

###############################################################################
# Plot levelsets on the mesh. The zero value marks the plane's location.
pl = DpfPlotter()
pl.add_field(levelset1, mesh)
pl.show_figure(show_axes=True, cpos=cpos)
pl = DpfPlotter()
pl.add_field(levelset2, mesh)
pl.show_figure(show_axes=True, cpos=cpos)

###############################################################################
# Use levelsets to obtain intersection with the 3D mesh:
mesh_cutter_op = ops.mesh.mesh_cut()
mesh_cutter_op.inputs.field.connect(levelset1)
mesh_cutter_op.inputs.iso_value.connect(float(0))
mesh_cutter_op.connect(2, 0)
# mesh_cutter_op.inputs.mesh.connect(mesh)
mesh_cutter_op.connect(3, mesh)
mesh_cutter_op.inputs.slice_surfaces.connect(True)
intersection1 = mesh_cutter_op.outputs.mesh()

mesh_cutter_op = ops.mesh.mesh_cut()
mesh_cutter_op.inputs.field.connect(levelset2)
mesh_cutter_op.inputs.iso_value.connect(float(0))
mesh_cutter_op.connect(2, 0)
# mesh_cutter_op.inputs.mesh.connect(mesh)
mesh_cutter_op.connect(3, mesh)
mesh_cutter_op.inputs.slice_surfaces.connect(True)
intersection2 = mesh_cutter_op.outputs.mesh()

###############################################################################
# Plot intsersections
pl = DpfPlotter()
pl.add_mesh(intersection1)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)

pl = DpfPlotter()
pl.add_mesh(intersection2)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)

###############################################################################
# Map the displacement field to the intersections:
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=intersection1.nodes.coordinates_field,
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_plane_intersection1 = fields_mapped[0]

mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=intersection2.nodes.coordinates_field,
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_plane_intersection2 = fields_mapped[0]


###############################################################################
# Plot intsersection and display mesh in background.
pl = DpfPlotter()
pl.add_field(field_plane_intersection1, intersection1, show_edges=False)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)

pl = DpfPlotter()
pl.add_field(field_plane_intersection2, intersection2, show_edges=False)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)


###############################################################################
# Map displacements to plane
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Map displacement field to points in plane object using
# :class:`Result <ansys.dpf.core.operators.mapping.on_coordinates.on_coordinates>:`
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=plane1.mesh.nodes.coordinates_field,
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_plane1 = fields_mapped[0]

mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=plane2.mesh.nodes.coordinates_field,
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_plane2 = fields_mapped[0]

###############################################################################
# Plot plane and display mesh in background.
pl = DpfPlotter()
if not len(field_plane1) == 0:
    pl.add_field(field_plane1, plane1.mesh, show_edges=False)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)

pl = DpfPlotter()
if not len(field_plane2) == 0:
    pl.add_field(field_plane2, plane1.mesh, show_edges=False)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)
