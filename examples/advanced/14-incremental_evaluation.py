# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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
.. _ref_incremental_evaluation:

Use incremental evaluation helper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows you how to use the incremental evaluation helper.
"""

# Import necessary modules
from ansys.dpf import core as dpf
from ansys.dpf.core import examples


#######################################################################################
# Retrieve an example to instantiate a DataSources object
path = examples.download_transient_result()
ds = dpf.DataSources(path)

# From the DataSources object we can retrieve the scoping
# In this example we want to compute the min/max for all the time sets
tf_provider = dpf.operators.metadata.time_freq_provider(data_sources=ds)
tf_support = tf_provider.get_output(output_type=dpf.types.time_freq_support)
scoping = dpf.time_freq_scoping_factory.scoping_on_all_time_freqs(tf_support)

# If you don't need to reuse TimeFreqSupport you could also use the DataSources
# scoping = dpf.time_freq_scoping_factory.scoping_on_all_time_freqs(ds)

#######################################################################################
# Defining the workflow to exploit

# Instantiating a streams_provider is important when dealing with incremental evaluation
# due to multiple reuses of operators
streams_provider = dpf.operators.metadata.streams_provider(data_sources=ds)

# Defining the main workflow
result_op = dpf.operators.result.stress(
    data_sources=ds, time_scoping=scoping, streams_container=streams_provider
)
norm_fc = dpf.operators.math.norm_fc(result_op)
final_op = dpf.operators.min_max.min_max_fc_inc(norm_fc)

#######################################################################################
# Obtain a new operator to retrieve outputs from

# Workflow is adapted from the first and the last operator in the current workflow
# Scoping is important to split the workload into chunks
new_end_op = dpf.split_workflow_in_chunks(result_op, final_op, scoping)


# Obtain results on the same pin numbers
min = new_end_op.get_output(0, dpf.types.field)
max = new_end_op.get_output(1, dpf.types.field)

# Plot results
import matplotlib.pyplot as plt

x = tf_support.time_frequencies.data
plt.plot(x, min.data, "b", label="Min")
plt.plot(x, max.data, "r", label="Max")
plt.xlabel("Time")
plt.ylabel("Stress")
plt.legend()
plt.show()
