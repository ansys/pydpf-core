"""
.. _ref_data_reordering_example:

Data ordering and scopings
~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to extract results and manipulate the order the data is shown in.

"""

# First, import the DPF-Core module as ``dpf`` and import the included examples file.
from ansys.dpf import core as dpf
from ansys.dpf.core import examples


###############################################################################
# Create a model object to establish a connection with an example result file.
model = dpf.Model(examples.find_simple_bar())

# Extract results
displacements = model.results.displacement()
fields = displacements.outputs.fields_container()
disp_field_0 = fields[0]

# To improve performance, the result data comes ordered the same way it is stored on the server,
# which is not necessarily by node or element ID.
# The link between data position and corresponding entity ID is defined by the field's scoping.
scoping = disp_field_0.scoping
# This scoping is Nodal with several thousand entities (node IDs):
print(scoping)
# The first 10 node IDs in the scoping:
print(scoping.ids[:10])
# You can see that the node IDs are not in ascending, descending, or any particular order.

# We can compare it to the order the mesh's nodes are in:
nodes_scoping = model.metadata.meshed_region.nodes.scoping
print(nodes_scoping)
print(nodes_scoping.ids[:10])

# The mesh's node scoping is, in this case, in ascending order.
# To force the field's date to follow the same ordering, use the rescope operator with the target
# scoping as input:
reordered_fields = dpf.operators.scoping.rescope_fc(
    fields_container=fields,
    mesh_scoping=nodes_scoping,
).outputs.fields_container()
reordered_disp_field_0 = reordered_fields[0]

# The field's data is now ordered based on its new scoping, same as the mesh:
print(reordered_disp_field_0.scoping.ids[:10])

# We can compare the values returned for the first entity of each field:
print(f"Displacement values for first entity of initial field: {disp_field_0.data[0]}")
print(f"Displacement values for first entity of rescoped field: {reordered_disp_field_0.data[0]}")
