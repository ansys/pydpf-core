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

"""
.. _ref_basic_harmonic:

Multi-harmonic response example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to compute a multi-harmonic response
using ``fft`` transformations.

"""

import matplotlib.pyplot as pyplot

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops


###############################################################################
# Begin by downloading the example harmonic result. This result is
# not included in the core module by default to speed up the install.
# Download should only take a few seconds.
#
# Next, create the model and display the state of the result.
# This harmonic result file contains several RPMs, and
# each RPM has several frequencies.

# The size of this file is 66 MB. Downloading it might take some time.
harmonic = examples.download_multi_harmonic_result()
model = dpf.Model(harmonic)
print(model)

###############################################################################
# Read the analysis domain support
tf = model.metadata.time_freq_support
print("Number of solution sets", tf.n_sets)

###############################################################################
# Compute multi-harmonic response
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This example computes the Rz multi-harmonic responses based on
# selected nodes and a set of EOs (engine orders).

# Create a total displacement operator and set its time scoping to
# the entire time frequency support and its nodes scoping to user-defined nodes.
disp_op = ops.result.raw_displacement(data_sources=model)
time_ids = list(range(1, model.metadata.time_freq_support.n_sets + 1))

# Define nodal scoping
nodes = dpf.Scoping()
nodes.ids = [2, 18]

# Connect the frequencies and the nodes scopings to the result
# provider operator.
disp_op.inputs.mesh_scoping.connect(nodes)
disp_op.inputs.time_scoping.connect(time_ids)

# Extract the Rz component using the component selector operator.
comp = dpf.Operator("component_selector_fc")
comp.inputs.connect(disp_op.outputs)
comp.inputs.component_number.connect(5)

# Compute the multi-harmonic response based on Rz and a set of RPMs.
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
# Plot the maximum displacements over time for Node ID 2 and 18

pyplot.plot(field1.data, "r", label="NODE-ID 2")
pyplot.plot(field2.data, "b", label="NODE-ID 18")
pyplot.xlabel("Frequency (Hz)")
pyplot.ylabel("Displacement (m)")
pyplot.legend()
pyplot.show()
