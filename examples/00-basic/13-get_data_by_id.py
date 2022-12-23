"""
.. _ref_get_data_by_id:

Retrieve field by ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to scope a field for a given named selection,
obtain the mesh for that scoped selection and to retrieve data from the field
by node ID.

"""

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
# Extract displacements on the entire geometry. Note that this is just for
# demonstration purposes. On a real simulation, the user should not evaluate
# (request from the server) data that is not needed.
disp_fc = model.results.displacement().eval()
print(disp_fc)

###############################################################################
# The displacement FieldsContainer contains a total of 15113 entities.

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
# Note how the number of entities has decreased from 15113 to 12970 entities
# after applying the scoping on ``my_named_selection``.

###############################################################################
# Get the only Field available
disp_selection = disp_selection_fc[0]

###############################################################################
# Scope mesh only for that named selection
mesh_from_scoping_op = ops.mesh.from_scoping()
mesh_from_scoping_op.inputs.scoping.connect(mesh_scoping)
mesh_from_scoping_op.inputs.mesh.connect(model.metadata.meshed_region)
mesh_selection = mesh_from_scoping_op.outputs.mesh()

###############################################################################
# Plot ``mesh_selection``
mesh_selection.plot()

###############################################################################
# The plot shows only one of the two cubes from the total geometry shown before.

###############################################################################
# Identify the location of the Field
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Check the location of the scoping to see what is the information associated
# to the IDs. The displacement field is defined at ``"nodal"`` location. Other fields
# may have other locations such as ``"elemental"`` or ``"elementalNodal"``.
# Note that this way of retrieving data by ID is only valid for locations that
# are either ``"nodal"`` or ``"elemental"``.
print(disp_selection.scoping.location)

###############################################################################
# Another way to check that ``disp_selection`` contains nodal data is to check that
# the number of entities in the displacement FieldsContainer (12970) matches the
# number of nodes of the scoped mesh ``mesh_selection``
print(mesh_selection.nodes.n_nodes)

###############################################################################
# Instead, the number of elements does not match
print(mesh_selection.elements.n_elements)

###############################################################################
# Access data in ``disp_selection`` by ID
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get the list of nodal IDs
ids = disp_selection.scoping.ids

###############################################################################
# Retrieve data of ``disp_selection`` from the server. Note that this is done before the
# loop below so only one call is made to the server.
data = disp_selection.data

###############################################################################
# Loop over ``ids`` to have access to both, the node ID and the displacement
# for that node
for idx, node_id in enumerate(ids):
    node_disp = data[idx]
