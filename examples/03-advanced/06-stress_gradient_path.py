"""
.. _stress_gradient_path:

Stress gradient normal to a defined node.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to plot a stress gradient normal to a selected node.
A path is created of a defined length.

"""

###############################################################################
# First, import the DPF-Core module as ``dpf_core`` and import the
# included examples file and ``DpfPlotter``
#
from ansys.dpf import core as dpf
from ansys.dpf.core import operators as ops
from ansys.dpf.core.plotter import DpfPlotter
from ansys.dpf.core import examples
###############################################################################
# Next, open an example and print out the ``model`` object.  The
# :class:`Model <ansys.dpf.core.model.Model> class helps to organize access
# methods for the result by keeping track of the operators and data sources
# used by the result
# file.
#
# Printing the model displays:
#
# - Analysis type
# - Available results
# - Size of the mesh
# - Number of results
# - Unit
#
model = dpf.Model(examples.hemisphere)
print(model)
###############################################################################
# Define the `node_id` normal to which a stress gradient should be plotted.
#
node_id = 1928
###############################################################################
# The following command prints the mesh unit
#
unit = model.metadata.meshed_region.unit
print("Unit: %s" % unit)
###############################################################################
# `depth` defines the path length / depth to which the path will penetrate.
# While defining `depth` make sure you use the correct mesh unit.
#
depth = 10  # in mm
###############################################################################
# Get the meshed region
#
mesh = model.metadata.meshed_region
###############################################################################
# Get Equivalent stress fields container.
#
stress_fc = model.results.stress().eqv().outputs.fields_container()
###############################################################################
# Define Nodal scoping.
# Make sure to define ``"Nodal"`` as the requested location, important for the
# `normals` operator.
#
nodal_scoping = dpf.Scoping(location="Nodal")
nodal_scoping.ids = [node_id]
###############################################################################
# Get Skin Mesh because `normals` operator required Shells as input.
#
skin_mesh = ops.mesh.skin(mesh=mesh)
skin_meshed_region = skin_mesh.outputs.mesh.get_data()
###############################################################################
# Get Skin Mesh because `normals` operator requires Shells as input.
#
normal = ops.geo.normals()
normal.inputs.mesh.connect(skin_meshed_region)
normal.inputs.mesh_scoping.connect(nodal_scoping)
normal_vec_out_field = normal.outputs.field.get_data()
###############################################################################
# Normal vector is along the surface normal. We need to invert the vector
# using `math.scale` operator inwards in the geometry, to get the path
# direction.
#
normal_vec_in_field = ops.math.scale(field=normal_vec_out_field,
                                     ponderation=-1.0)
normal_vec_in = normal_vec_in_field.outputs.field.get_data().data[0]
###############################################################################
# Get Nodal coordinates, they serve as the first point on the line.
#
node = mesh.nodes.node_by_id(node_id)
line_fp = node.coordinates
###############################################################################
# Create 3D line equation.
#
fx = lambda t: line_fp[0] + normal_vec_in[0] * t
fy = lambda t: line_fp[1] + normal_vec_in[1] * t
fz = lambda t: line_fp[2] + normal_vec_in[2] * t
###############################################################################
# Create coordinates using 3D line equation-
#
coordinates = [[fx(t / 10.0), fy(t / 10.0), fz(t / 10.0)] for t in
               range(int(depth
                         * 10))]
flat_coordinates = [entry for data in coordinates for entry in data]
###############################################################################
# Create Field for coordinates of the path.
#
field_coord = dpf.fields_factory.create_3d_vector_field(len(coordinates))
field_coord.data = flat_coordinates
field_coord.scoping.ids = list(range(1, len(coordinates) + 1))
###############################################################################
# Let's now map results on the path.
mapping_operator = ops.mapping.on_coordinates(
    fields_container=stress_fc,
    coordinates=field_coord,
    create_support=True,
    mesh=mesh)
fields_mapped = mapping_operator.outputs.fields_container()
###############################################################################
# Here, we request the mapped field data and its mesh
field_m = fields_mapped[0]
mesh_m = field_m.meshed_region
###############################################################################
# Now we create the plotter and add fields and meshes
pl = DpfPlotter()

pl.add_field(field_m, mesh_m)
pl.add_mesh(mesh, style="surface", show_edges=True,
            color="w", opacity=0.3)

pl.show_figure(show_axes=True, cpos=[
    (62.687, 50.119, 67.247),
    (5.135, 6.458, -0.355),
    (-0.286, 0.897, -0.336)])
