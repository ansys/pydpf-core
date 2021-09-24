"""
.. _ref_basic_harmonic:

Multi-Harmonic Response Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to compute a multi-harmonic response
using fft transforms.

"""
import matplotlib.pyplot as pyplot

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Begin by downloading the example harmonic result.  This result is
# not included in the core module by default to speed up the install.
# Download should only take a few seconds.
#
# Next, create the model and display the state of the result.  Note
# that this harmonic result file contains several rpms,
# each rpm has several frequencies.

# this file is 66Mb size, it may take time to download
harmonic = examples.download_multi_harmonic_result()
model = dpf.Model(harmonic)
print(model)


###############################################################################
# Read the analysis domain support
tf = model.metadata.time_freq_support
print("Number of solution sets", tf.n_sets)


###############################################################################
# Compute multi harmonic response
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In this example we compute the Rz multi harmonic responses based on
# a selected nodes and a set of EOs (multiple engine orders).

# Create a total displacement operator and set its time scoping to
# the entire time freq support and its nodes scoping into a user defined nodes.
disp_op = ops.result.raw_displacement(data_sources=model)
time_ids = list(range(1, model.metadata.time_freq_support.n_sets + 1))

# define nodal scoping
nodes = dpf.Scoping()
nodes.ids = [2, 18]

# connect the frequencies and the nodes scopings to the result
# provider operator
disp_op.inputs.mesh_scoping.connect(nodes)
disp_op.inputs.time_scoping.connect(time_ids)

# extract Rz component using the component selector operator
comp = dpf.Operator("component_selector_fc")
comp.inputs.connect(disp_op.outputs)
comp.inputs.component_number.connect(5)

# Compute the multi-harmonic response based on Rz and a set of RPMs
rpms = dpf.Scoping()
rpms.ids = [1, 2, 3]

fft = ops.math.fft_multi_harmonic_minmax()

fft.inputs.connect(comp.outputs)
fft.inputs.rpm_scoping.connect(rpms)


fields = fft.outputs.field_max()
len(fields)  # one multi-harmonic field response per node

field1 = fields[0]
field2 = fields[1]

###############################################################################
# Plot the minimum and maximum displacements over time

pyplot.plot(field1.data, "r", label="Field 1")
pyplot.plot(field2.data, "b", label="Field 2")
pyplot.xlabel("Frequency (Hz)")
pyplot.ylabel("Displacement (m)")
pyplot.legend()
pyplot.show()
