"""
.. _ref_get_data_by_id:

Retrieve field data by ID
~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to scope a field for a given named selection,
obtain the mesh for that scoped selection and to retrieve data from the field
by node ID.

.. note::
    This example requires the Premium ServerContext.
    For more information, see :ref:`user_guide_server_context`.

"""

###############################################################################
# Imports and load model
# ~~~~~~~~~~~~~~~~~~~~~~
# Import modules and set context as Premium.
import time
import numpy as np
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
# The displacement FieldsContainer contains a total of 15113 entities, i.e.
# nodal values.

###############################################################################
# Plot the entire mesh
disp_fc[0].meshed_region.plot()

###############################################################################
# Get mesh and field scoped only for a certain named selection
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# Check that the named selection requested contains IDs information
if len(mesh_scoping.ids) == 0:
    raise ValueError("No IDs information for the requested named selection.")

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
# to the IDs. The displacement field is defined at ``"nodal"`` location. Other
# fields may have other locations such as ``"elemental"`` or ``"elementalNodal"``.
print(disp_selection.scoping.location)

###############################################################################
# Another way to check that ``disp_selection`` contains nodal data is to check
# that the number of entities in the displacement FieldsContainer (12970)
# matches the number of nodes of the scoped mesh ``mesh_selection``
print(mesh_selection.nodes.n_nodes)

###############################################################################
# Instead, the number of elements does not match
print(mesh_selection.elements.n_elements)

###############################################################################
# Access data in ``disp_selection`` by ID (index approach)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get the list of nodal IDs
ids = disp_selection.scoping.ids

###############################################################################
# Retrieve data of ``disp_selection`` from the server. Note that this is done
# before the loop below so only one call is made to the server.
start = time.time()
data = disp_selection.data

###############################################################################
# Loop over ``ids`` to have access to both, the node ID and the displacement
# for that node
nodal_disp_index = np.zeros([mesh_selection.nodes.n_nodes, 3])
for idx, node_id in enumerate(ids):
    node_disp = data[idx]
    nodal_disp_index[idx, :] = node_disp

index_time = time.time() - start

###############################################################################
# .. note::
#     Note that this way of retrieving data by ID is only valid for locations that
#     are either ``"nodal"`` or ``"elemental"``.


###############################################################################
# Access data in ``disp_selection`` by ID (get entity approach)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# An alternative to the index approach is to use the ``get_entity_data_by_id``
# method to get the nodal displacement given a certain node ID.
start = time.time()
nodal_disp_get_entity = np.zeros([mesh_selection.nodes.n_nodes, 3])
for idx, node_id in enumerate(ids):
    node_disp = disp_selection.get_entity_data_by_id(node_id)
    nodal_disp_get_entity[idx, :] = node_disp

get_entity_time = time.time() - start

###############################################################################
# .. note::
#    This approach is not efficient to retrieve data for all nodes, since it would
#    make one server request per node. Instead, this approach is useful when
#    we are only interesed on requesting data on one or a few nodes.

###############################################################################
# Assess both approaches to get data by node ID
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Find below the difference of the arrays obtained with both methods. The zero
# value indicates that the two approaches are completely equivalent.
diff = np.sum(nodal_disp_index - nodal_disp_get_entity)
print(f"Difference between the two approaches: {diff}")

###############################################################################
# In terms of performance, the index approach is found to be an order of magnitude
# faster for this particular example. The time difference can be attributed to the
# fact that only one server call is required for the index approach.
# Instead, the get entity strategy requires one server call per node in the mesh.
# The difference in performance is likely to scale with the number of nodes in the mesh.
print(f"Time taken using index approach: {index_time}")
print(f"Time taken using get_entity_data_by_id approach: {get_entity_time}")
