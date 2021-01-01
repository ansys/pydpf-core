"""
.. _ref_dpf_core:

Transient Analysis Result Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to post-process a transient result and
visualize the outputs.

"""
import numpy as np
import matplotlib.pyplot as plt

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.operators_helper import norm, min_max

###############################################################################
# Begin by downloading the example transient result.  This result is
# not included in the core module by default to speed up the install.
# Download should only take a few seconds.
#
# Next, create the model and display the state of the result.  Note
# that this transient result file contains several individual results,
# each at a different timestamp.

transient = examples.download_transient_result()
model = dpf.Model(transient)
print(model)


###############################################################################
# Get the timestamps for each substep as a numpy array
tf = model.metadata.time_freq_support
print(tf.frequencies.data)


###############################################################################
# Obtain Minimum and Maximum Displacement for all Results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create a displacement operator and set its time scoping request to
# the entire time freq support.
disp = model.results.displacement()
timeids = range(1, tf.n_sets + 1)  # must use 1-based indexing
disp.inputs.time_scoping(timeids)

# Then chain the displacement operator with norm and min_max operators
min_max_op = min_max(norm(disp))

min_disp = min_max_op.outputs.field_min()
max_disp = min_max_op.outputs.field_max()
print(max_disp.data)

###############################################################################
# Plot the minimum and maximum displacements over time

tdata = tf.frequencies.data
plt.plot(tdata, max_disp.data, 'r', label='Max')
plt.plot(tdata, min_disp.data, 'b', label="Min")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.show()

###############################################################################
# Plot the minimum and maximum displacements over time for the X
# component.
disp_z = disp.Z()
min_max_op = min_max(norm(disp_z))

min_disp_z = min_max_op.outputs.field_min()
max_disp_z = min_max_op.outputs.field_max()

tdata = tf.frequencies.data
plt.plot(tdata, max_disp_z.data, 'r', label='Max')
plt.plot(tdata, min_disp_z.data, 'b', label="Min")
plt.xlabel("Time (s)")
plt.ylabel("X Displacement (m)")
plt.legend()
plt.show()


###############################################################################
# Post-Processing Stress
# ~~~~~~~~~~~~~~~~~~~~~~
# Create a equivalent (von mises) stress operator and set its time
# scoping to the entire time freq support.

# Component stress operator (stress)
stress = model.results.stress()

# Equivalent stress operator
eqv = stress.eqv()
eqv.inputs.time_scoping(timeids)

# connect to the min_max operator and return the minimum and maximum
# fields
min_max_eqv = min_max(eqv)
eqv_min = min_max_eqv.outputs.field_min()
eqv_max = min_max_eqv.outputs.field_max()

print(eqv_min)

###############################################################################
# Plot the maximum stress over time

plt.plot(tdata, eqv_min.data, 'b', label="Minimum")
plt.plot(tdata, eqv_max.data, 'r', label='Maximum')
plt.xlabel("Time (s)")
plt.ylabel("Equivalent Stress (Pa)")
plt.legend()
plt.show()

###############################################################################
# Stress Field Coordinates
# ~~~~~~~~~~~~~~~~~~~~~~~~
# The scoping of the stress field can be used to extract the
# coordinates used for each result.

# extract a single field from the equivalent stress operator
field = eqv.outputs.fields_container()[28]

# print the first node IDs from the field
print(field.scoping.ids[:10])

################################################################################
# As you can see, these node numbers are not in order.  Additionally,
# there may be less entries in the field than nodes in the model.  For
# example, stresses are not computed at mid-side nodes.
#
# To extract the coordinates for these node ids, load the mesh from
# the model and then extract a coordinate for each node index.
#
# This is an inefficient way of getting the coordinates as each
# individual request must be sent to the DPF service.

# load the mesh from the model
mesh = model.meshed_region

# print the first 10 coordinates for the field
node_ids = field.scoping.ids
for node_id in node_ids[:10]:
    # fetch each individual node by node ID
    node_coord = mesh.nodes.node_by_id(node_id).coordinates
    print(f'Node ID {node_id} : %8.5f, %8.5f, %8.5f' % tuple(node_coord))

###############################################################################
#
#

# Get all the coordinate
mesh_node_ids = np.array(mesh.nodes.scoping.ids)

coord = mesh.nodes.coordinates_field.data

