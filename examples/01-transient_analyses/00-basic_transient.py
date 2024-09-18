# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# noqa: D400
"""
.. _ref_basic_transient:

Transient analysis result example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to postprocess a transient result and
visualize the outputs.

"""

# Import the necessary modules
import matplotlib.pyplot as plt
import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Download the transient result example. This example is
# not included in DPF-Core by default to speed up the installation.
# Downloading this example should take only a few seconds.
#
# Next, create the model and display the state of the result. This transient
# result file contains several individual results, each at a different timestamp.

transient = examples.download_transient_result()
model = dpf.Model(transient)
print(model)

###############################################################################
# Get the timestamps for each substep as a numpy array:
tf = model.metadata.time_freq_support
print(tf.time_frequencies.data)

###############################################################################
# Obtain minimum and maximum displacements for all results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create a displacement operator and set its time scoping request to
# the entire time frequency support:
disp = model.results.displacement()
timeids = range(1, tf.n_sets + 1)  # Must use 1-based indexing.
disp.inputs.time_scoping(timeids)

# Chain the displacement operator with ``norm`` and ``min_max`` operators.
min_max_op = ops.min_max.min_max_fc(ops.math.norm_fc(disp))

min_disp = min_max_op.outputs.field_min()
max_disp = min_max_op.outputs.field_max()
print(max_disp.data)

###############################################################################
# Plot the minimum and maximum displacements over time:

tdata = tf.time_frequencies.data
plt.plot(tdata, max_disp.data, "r", label="Max")
plt.plot(tdata, min_disp.data, "b", label="Min")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.show()

###############################################################################
# Plot the minimum and maximum displacements over time for the X
# component.
disp_z = disp.Z()
disp_z.inputs.time_scoping(timeids)
min_max_op = ops.min_max.min_max_fc(ops.math.norm_fc(disp_z))

min_disp_z = min_max_op.outputs.field_min()
max_disp_z = min_max_op.outputs.field_max()

tdata = tf.time_frequencies.data
plt.plot(tdata, max_disp_z.data, "r", label="Max")
plt.plot(tdata, min_disp_z.data, "b", label="Min")
plt.xlabel("Time (s)")
plt.ylabel("X Displacement (m)")
plt.legend()
plt.show()

###############################################################################
# Postprocessing stress
# ~~~~~~~~~~~~~~~~~~~~~
# Create an equivalent (von Mises) stress operator and set its time
# scoping to the entire time frequency support:

# Component stress operator (stress)
stress = model.results.stress()

# Equivalent stress operator
eqv = stress.eqv()
eqv.inputs.time_scoping(timeids)

# Connect to the min_max operator and return the minimum and maximum
# fields.
min_max_eqv = ops.min_max.min_max_fc(eqv)
eqv_min = min_max_eqv.outputs.field_min()
eqv_max = min_max_eqv.outputs.field_max()

print(eqv_min)

###############################################################################
# Plot the maximum stress over time:

plt.plot(tdata, eqv_min.data, "b", label="Minimum")
plt.plot(tdata, eqv_max.data, "r", label="Maximum")
plt.xlabel("Time (s)")
plt.ylabel("Equivalent Stress (Pa)")
plt.legend()
plt.show()

###############################################################################
# Scoping and stress field coordinates
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The scoping of the stress field can be used to extract the
# coordinates used for each result:

# Extract a single field from the equivalent stress operator.
field = eqv.outputs.fields_container()[28]

# Print the first node IDs from the field.
print(field.scoping.ids[:10])

################################################################################
# As you can see, these node IDs are not in order. Additionally,
# there may be fewer entries in the field than nodes in the model. For
# example, stresses are not computed at mid-side nodes.
#
# To extract the coordinates for these node IDs, load the mesh from
# the model and then extract a coordinate for each node index.
#
# Here is an inefficient way of getting the coordinates as each
# individual request must be sent to the DPF service:

# Load the mesh from the model.
meshed_region = model.metadata.meshed_region

# Print the first 10 coordinates for the field.
node_ids = field.scoping.ids
for node_id in node_ids[:10]:
    # Fetch each individual node by node ID.
    node_coord = meshed_region.nodes.node_by_id(node_id).coordinates
    print(f"Node ID {node_id} : %8.5f, %8.5f, %8.5f" % tuple(node_coord))

###############################################################################
# Rather than individually querying for each node coordinate of the
# field, you can use the :func:`map_scoping <ansys.dpf.core.nodes.Nodes.map_scoping>`
# to remap the field data to match the order of the nodes in the meshed region.
#
# Obtain the indices needed to get the data from ``field.data`` to match
# the order of nodes in the mesh:

nodes = meshed_region.nodes
ind, mask = nodes.map_scoping(field.scoping)

# Show that the order of the remapped node scoping matches the field scoping.
print("Scoping matches:", np.allclose(np.array(nodes.scoping.ids)[ind], field.scoping.ids))

# Now plot the von Mises stress relative to the Z coordinates.
z_coord = nodes.coordinates_field.data[ind, 2]

plt.plot(z_coord, field.data, ".")
plt.xlabel("Z Coordinate (m)")
plt.ylabel("Equivalent Stress (Pa)")
plt.show()
