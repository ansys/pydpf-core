"""
.. _plot_on_path:

Plot results on a specific path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to get a result mapped over a specific path,
and how to plot it.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Path plotting
# ~~~~~~~~~~~~~
# We will use an :class:`ansys.dpf.core.plotter.DpfPlotter` to plot a mapped result over
# a defined path of coordinates.

# First, we need to create the model, request its mesh and its
# displacement data
model = dpf.Model(examples.static_rst)
mesh = model.metadata.meshed_region
disp_fc = model.results.displacement().outputs.fields_container()
field = disp_fc[0]

###############################################################################
# Then, we create a coordinates field to map on
coordinates = []
ref = [0.024, 0.03, 0.003]
coordinates.append(ref)
for i in range(1, 51):
    coord_copy = ref.copy()
    coord_copy[1] = coord_copy[0] + i * 0.001
    coordinates.append(coord_copy)
field_coord = dpf.fields_factory.create_3d_vector_field(len(coordinates))
field_coord.data = coordinates
field_coord.scoping.ids = list(range(1, len(coordinates) + 1))

###############################################################################
# Let's now compute the mapped data using the mapping operator
mapping_operator = dpf.Operator("mapping")
mapping_operator.inputs.fields_container.connect(disp_fc)
mapping_operator.inputs.coordinates.connect(field_coord)
mapping_operator.inputs.mesh.connect(mesh)
mapping_operator.inputs.create_support.connect(True)
fields_mapped = mapping_operator.outputs.fields_container()

###############################################################################
# Here, we request the mapped field data and its mesh
field_m = fields_mapped[0]
mesh_m = field_m.meshed_region

###############################################################################
# Now we create the plotter and add fields and meshes
from ansys.dpf.core.plotter import DpfPlotter
pl = DpfPlotter()

pl.add_field(field_m, mesh_m)
pl.add_mesh(mesh, style="surface", show_edges=True,
             color="w", opacity=0.3)

# Finally we plot the result
pl.show_figure(show_axes=True)