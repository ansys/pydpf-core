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
.. _ref_transient_easy_time_scoping:

Choose a time scoping for a transient analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to use a model's result to choose a time scoping.

"""

import matplotlib.pyplot as plt

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Create the model and display the state of the result. This transient result
# file contains several individual results, each at a different times.

transient = examples.find_msup_transient()
model = dpf.Model(transient)
print(model)

###############################################################################
# Obtain minimum and maximum displacements at all times
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# Use time extrapolation
# ~~~~~~~~~~~~~~~~~~~~~~~
# A local maximum can be seen on the plot between 0.05 and 0.075 seconds.
# Displacement is evaluated every 0.0005 seconds in this range
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
