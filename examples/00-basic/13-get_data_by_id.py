from ansys.dpf import core as dpf
from ansys.dpf.core import examples

model = dpf.Model(examples.download_all_kinds_of_complexity())
disp_selection_fc = model.results.displacement.on_named_selection(
    named_selection="_CM82"
).eval()
print(disp_selection_fc[0].location)


###############################################################################
# Imports and load model
# ~~~~~~~~~~~~~~~~~~~~~~
# Import modules and set context as Premium.
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

###############################################################################
# Load model from examples and print information:
model = dpf.Model(examples.download_all_kinds_of_complexity())
print(model)

###############################################################################
# Print available named selections:
print(model.metadata.available_named_selections)

###############################################################################
# Visualize the entire mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Extract displacements on the entire geometry
# .. note::
#     Note that this is just for demonstration purposes. On a real simulation, the
#     user shouldn't evaluate (request from the server) data that is not needed.
disp_fc = model.results.displacement().eval()
print(disp_fc)

###############################################################################
# Plot the entire mesh
disp_fc[0].meshed_region.plot()

###############################################################################
# Get mesh and results for only a certain named selection
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define named selection
my_named_selection = "_CM82"

###############################################################################
# Get nodal mesh scoping for ``my_named_selection``
scoping_op = ops.scoping.on_named_selection()
scoping_op.inputs.requested_location.connect("nodal")
scoping_op.inputs.named_selection_name.connect(my_named_selection)
scoping_op.inputs.data_sources.connect(
    dpf.DataSources(examples.download_all_kinds_of_complexity())
)
mesh_scoping = scoping_op.outputs.mesh_scoping()

###############################################################################
# Extract displacements by applying the ``mesh_scoping``
disp_selection_fc = model.results.displacement.on_mesh_scoping(mesh_scoping).eval()
print(disp_selection_fc)

###############################################################################
# Get the only Field available
disp_selection = disp_selection_fc[0]

###############################################################################
# Scope mesh only for that named selection
# mesh_scoping = model.metadata.named_selection(my_named_selection)  ## Force location == nodal
mesh_from_scoping_op = ops.mesh.from_scoping()
mesh_from_scoping_op.inputs.scoping.connect(mesh_scoping)
mesh_from_scoping_op.inputs.mesh.connect(model.metadata.meshed_region)
mesh_selection = mesh_from_scoping_op.outputs.mesh()

###############################################################################
# Plot ``mesh_selection``
mesh_selection.plot()

###############################################################################
# Identify the location of the Field
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Check the location of the scoping to see what is the information associated
# to the IDs. For this example, the displacement field is defined at ``"nodal"`` level.
# Note that this example is only valid for locations that are either ``"nodal"`` or
# ``"elemental"``.
print(disp_selection.scoping.location)

###############################################################################
# Another way to check that ``disp_selection`` contains nodal data is to check that
# the number of entities in the displacement FieldsContainer (=12970) matches the
# number of nodes of the scoped mesh ``mesh_selection``
print(mesh_selection.nodes.n_nodes)

###############################################################################
# Instead, the number of elements does not match
print(mesh_selection.elements.n_elements)

###############################################################################
# Access data in ``disp_selection`` by ID
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get the list of IDs (associated to each element)
ids = disp_selection.scoping.ids

###############################################################################
# Retrieve data of ``disp_selection`` from the server. Note that this is done before the
# loop below so only one call is made to the server.
data = disp_selection.data

###############################################################################
# Loop over ``ids`` to have access to both, the ID value and the displacement
# for that ID (associated to elements for this example)
for idx, id in enumerate(ids):
    node_disp = data[idx]
    node_id = id
