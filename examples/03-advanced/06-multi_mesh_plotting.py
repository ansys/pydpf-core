"""
.. _multi_mesh_plotting:

Advanced plotting
~~~~~~~~~~~~~~~~~
This example shows how to plot several meshes from a meshes container, 
or directly using the DpfPlotter.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Multi-mesh plotting
# ~~~~~~~~~~~~~~~~~~~
# In this example we will use a DpfPlotter to plot several meshes. 

# Create the model and get its mesh
model = dpf.Model(examples.multishells_rst)
mesh = model.metadata.meshed_region

# split the mesh
split_mesh_op = dpf.Operator("split_mesh")
split_mesh_op.connect(7, mesh)
split_mesh_op.connect(13, "mat")
meshes_cont = split_mesh_op.outputs.mesh_controller()

# Select the meshes to plot and add them to the DpfPlotter
from ansys.dpf.core.plotter import DpfPlotter
pl = DpfPlotter()
pl.add_mesh(meshes_cont[0], style="surface", show_edges=True,
             color="y", opacity=0.3)
pl.add_mesh(meshes_cont[1], style="surface", show_edges=True,
             color="b", opacity=0.3)

# plot the result
pl.show_figure()

###############################################################################
# Multi-mesh plotting with results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In this example we will plot the data over a meshes container.

# Create the model and get its mesh
model = dpf.Model(examples.multishells_rst)
mesh = model.metadata.meshed_region

# split the mesh
split_mesh_op = dpf.Operator("split_mesh")
split_mesh_op.connect(7, mesh)
split_mesh_op.connect(13, "mat")
meshes_cont = split_mesh_op.outputs.mesh_controller()

# get the meshes_container associated displacement data
disp_op = dpf.Operator("U")
disp_op.connect(7, meshes_cont)
ds = dpf.DataSources(examples.multishells_rst)
disp_op.connect(4, ds)
disp_fc = disp_op.outputs.fields_container()

# plot the meshes container
meshes_cont.plot(disp_fc)

###############################################################################
# Path plotting
# ~~~~~~~~~~~~~
# Now we will use a DpfPlotter to plot a mapped result over a defined path of
# coordinates.

# create the model, request its mesh and its displacement data
model = dpf.Model(examples.multishells_rst)
mesh = model.metadata.meshed_region
disp_fc = model.results.displacement().outputs.fields_container()
field = disp_fc[0]

# create a coordinates field to map on
i = 0
coordinates = []
ref = [-0.0155, 0.00600634, -0.0025]
coordinates.append(ref)
while i < 20:
    i += 1
    coord_copy = ref.copy()
    coord_copy[0] = coord_copy[0] + i * 0.0003
    coordinates.append(coord_copy)
field_coord = dpf.fields_factory.create_3d_vector_field(len(coordinates))
field_coord.data = coordinates
field_coord.scoping.ids = list(range(1, len(coordinates) + 1))

# compute the mapped data using the mapping operator
mapping_operator = dpf.Operator("mapping")
mapping_operator.inputs.fields_container.connect(disp_fc)
mapping_operator.inputs.coordinates.connect(field_coord)
mapping_operator.inputs.mesh.connect(mesh)
mapping_operator.inputs.create_support.connect(True)
fields_mapped = mapping_operator.outputs.fields_container()

# gte mapped field data and mesh
field_m = fields_mapped[0]
mesh_m = field_m.meshed_region

# create the plotter and add fields and meshes
from ansys.dpf.core.plotter import DpfPlotter
pl = DpfPlotter()

pl.add_field(field_m, mesh_m)
pl.add_mesh(mesh, style="surface", show_edges=True,
             color="w", opacity=0.3)

# plot the result
pl.show_figure()