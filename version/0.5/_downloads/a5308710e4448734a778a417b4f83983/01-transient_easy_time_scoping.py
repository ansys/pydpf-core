"""
.. _ref_transient_easy_time_scoping:

Choose a Time Scoping for a Transient Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to use a model's results to easily
choose a time scoping.

"""
import matplotlib.pyplot as plt

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Create the model and display the state of the result. This transient result
# file contains several individual results, each at a different times.

transient = examples.msup_transient
model = dpf.Model(transient)
print(model)

###############################################################################
# Obtain Minimum and Maximum Displacements at All Times
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create a displacement operator and set its time scoping request to
# the entire time frequency support:
disp = model.results.displacement
disp_op = disp.on_all_time_freqs()

# Chain the displacement operator with norm and min_max operators.
min_max_op = ops.min_max.min_max_fc(ops.math.norm_fc(disp_op))

min_disp = min_max_op.outputs.field_min()
max_disp = min_max_op.outputs.field_max()
print(max_disp.data)

###############################################################################
# Plot the minimum and maximum displacements over time:

tdata = model.metadata.time_freq_support.time_frequencies.data
plt.plot(tdata, max_disp.data, "r", label="Max")
plt.plot(tdata, min_disp.data, "b", label="Min")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.show()

###############################################################################
# Use Time Extrapolation
# ~~~~~~~~~~~~~~~~~~~~~~~
# A local maximum can be seen on the plot between 0.05 and 0.075 seconds.
# Displacement will be evaluated every 0.0005s in this range
# to draw a nicer plot on this range.

offset = 0.0005
time_scoping = [0.05 + offset * i for i in range(0, int((0.08 - 0.05) / offset))]
print(time_scoping)

###############################################################################
# Create a displacement operator and set its time scoping request:
disp = model.results.displacement
disp_op = disp.on_time_scoping(time_scoping)()

# Chain the displacement operator with norm and min_max operators.
min_max_op = ops.min_max.min_max_fc(ops.math.norm_fc(disp_op))

min_disp = min_max_op.outputs.field_min()
max_disp = min_max_op.outputs.field_max()
print(max_disp.data)

###############################################################################
# Plot the minimum and maximum displacements over time:

plt.plot(time_scoping, max_disp.data, "rx", label="Max")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.show()
