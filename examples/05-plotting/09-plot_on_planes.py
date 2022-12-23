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
# Load model from examples and print information
model = dpf.Model(examples.find_static_rst())
print(model)

###############################################################################
# Create plane object
# ~~~~~~~~~~~~~~~~~~~
# Create plane passing through the mid point
plane1 = Plane(
    center=[0.015, 0.045, 0.015],
    normal=[1, 1, 0],
    width=0.03,
    height=0.03,
    n_cells_x=10,
    n_cells_y=10,
)

plane2 = Plane(
    center=[0.015, 0.045, 0.015],
    normal=[1, 1, 1],
    width=0.03,
    height=0.03,
    n_cells_x=10,
    n_cells_y=10,
)

###############################################################################
# Load mesh and show plane with the 3D mesh
mesh = model.metadata.meshed_region

###############################################################################
# Define the camera position
# (obtained with ``cpos=pl.show_figure(return_cpos=True)``)
cpos = [
    (0.07635352356975698, 0.1200500294271993, 0.041072502929096165),
    (0.015, 0.045, 0.015),
    (-0.16771051558419411, -0.1983722658245161, 0.9656715938216944),
]

###############################################################################
# Plot planes
plane1.plot(mesh, cpos=cpos)
plane2.plot(mesh, cpos=cpos)

###############################################################################
# Get plane's properties
print(f"Center of the plane = {plane1.center}")
print(f"Normal direction of the plane = {plane1.normal_dir}")
print(f"Number of cells in the x axis to discretize the plane = {plane1.n_cells_x}")
print(f"Number of cells in the y axis to discretize the plane = {plane1.n_cells_y}")
print(f"Height of the discretized plane = {plane1.height}")
print(f"Width of the discretized plane = {plane1.width}")

###############################################################################
# Map displacements to plane
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Map displacement field to points in plane object using
# :class:`on_coordinates <ansys.dpf.core.operators.mapping.on_coordinates.on_coordinates>`
disp = model.results.displacement
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=plane1.mesh.nodes.coordinates_field,
    create_support=True,
    mesh=mesh,
)
disp_plane1_fc = mapping_operator.outputs.fields_container()

###############################################################################
# Print ``disp_plane1_fc`` information
print(disp_plane1_fc)

###############################################################################
# Extract the only field (0th entry) available in ``disp_plane1_fc`` FieldsContainer
field_plane1 = disp_plane1_fc[0]

###############################################################################
# Repeat process for plane2
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=plane2.mesh.nodes.coordinates_field,
    create_support=True,
    mesh=mesh,
)
disp_plane2_fc = mapping_operator.outputs.fields_container()
field_plane2 = disp_plane2_fc[0]

###############################################################################
# Plot plane and display mesh in background.
pl = DpfPlotter()
pl.add_field(field_plane1, plane1.mesh, show_edges=False)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)

pl = DpfPlotter()
pl.add_field(field_plane2, plane2.mesh, show_edges=False)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)

###############################################################################
# Note that when the discretized plane contains nodes outside the geometry, some
# missing data leads to plotting artifacts.
#
# The alternative is presented in the following sections.
#
#   1. Compute levelset plane/mesh
#   2. Compute intersection plane / mesh
#   3. Map field to intersection plane / mesh

###############################################################################
# Compute levelset plane / mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Obtain the levelset of the plane with respect to the mesh using
# :class:`make_plane_levelset <ansys.dpf.core.operators.mesh.make_plane_levelset.
# make_plane_levelset>`
# A levelset is a scalar Field representing the normal distance between the plane
# and the nodes of the mesh.
# Note that origin and normal must be ``dpf.locations.overall`` 3D vectors.
origin1 = dpf.Field(1, dpf.natures.vector, dpf.locations.overall)
origin1.append(plane1.center, 0)
normal1 = dpf.Field(1, dpf.natures.vector, dpf.locations.overall)
normal1.append(plane1.normal_dir, 0)
origin2 = dpf.Field(1, dpf.natures.vector, dpf.locations.overall)
origin2.append(plane2.center, 0)
normal2 = dpf.Field(1, dpf.natures.vector, dpf.locations.overall)
normal2.append(plane2.normal_dir, 0)

###############################################################################
# Get levelsets
levelset1_op = ops.mesh.make_plane_levelset()
levelset1_op.inputs.coordinates.connect(mesh.nodes.coordinates_field)
levelset1_op.inputs.origin.connect(origin1)
levelset1_op.inputs.normal.connect(normal1)
levelset1 = levelset1_op.outputs.field()

levelset2_op = ops.mesh.make_plane_levelset()
levelset2_op.inputs.coordinates.connect(mesh.nodes.coordinates_field)
levelset2_op.inputs.origin.connect(origin2)
levelset2_op.inputs.normal.connect(normal2)
levelset2 = levelset2_op.outputs.field()

###############################################################################
# Plot levelsets on the mesh. The zero value marks the plane's location.
pl = DpfPlotter()
pl.add_mesh(mesh, scalars=levelset1.data)
pl.show_figure(show_axes=True, cpos=cpos)

pl = DpfPlotter()
pl.add_mesh(mesh, scalars=levelset2.data)
pl.show_figure(show_axes=True, cpos=cpos)

###############################################################################
# Compute intersection plane / mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use the :class:`mesh_cut <ansys.dpf.core.operators.mesh.mesh_cut.mesh_cut>`
# operator to obtain the intersection of the plane with the mesh from the levelset
mesh_cutter_op = ops.mesh.mesh_cut()
mesh_cutter_op.inputs.field.connect(levelset1)
mesh_cutter_op.inputs.iso_value.connect(float(0))
mesh_cutter_op.connect(2, 0)
mesh_cutter_op.connect(3, mesh)
mesh_cutter_op.inputs.slice_surfaces.connect(True)
intersection1 = mesh_cutter_op.outputs.mesh()

mesh_cutter_op = ops.mesh.mesh_cut()
mesh_cutter_op.inputs.field.connect(levelset2)
mesh_cutter_op.inputs.iso_value.connect(float(0))
mesh_cutter_op.connect(2, 0)
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
# Map field to intersection plane / mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Map the displacement field to the intersections
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
