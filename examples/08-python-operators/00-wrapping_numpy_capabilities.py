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
.. _ref_wrapping_numpy_capabilities:

Create a basic operator plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to create a basic operator plugin, which is for
a single custom operator. This custom operator, ``easy_statistics``,
computes simple statistics quantities on a scalar field with the help of
the ``numpy`` package.

The objective of this simple example is to show how routines for DPF can
be wrapped in Python plugins.

.. note::
    This example requires DPF 5.0 (Ansys 2023R1) or above.
    For more information, see :ref:`ref_compatibility`.

"""

###############################################################################
# Create the operator
# -------------------
# Creating a basic operator plugin consists of writing a single Python script.
# An operator implementation derives from the
# :class:`ansys.dpf.core.custom_operator.CustomOperatorBase` class
# and a call to the :py:func:`ansys.dpf.core.custom_operator.record_operator`
# method.
#
# The ``easy_statistics`` operator takes a field as an input and returns
# the first quartile, the median, the third quartile, and the variance.
# The Python operator and its recording are available in the
# ``easy_statistics.py`` file.
#
# Download and display the Python script.

from pathlib import Path

from ansys.dpf.core.examples import download_easy_statistics

operator_file_path = Path(download_easy_statistics())

with operator_file_path.open() as file:
    for line in file.readlines():
        print("\t\t\t" + line)

###############################################################################
# Load the plugin
# ---------------
# You use the :py:func:`ansys.dpf.core.core.load_library` method to load the
# plugin.

# - The first argument is the path to the directory where the plugin
#   is located.
# - The second argument is ``py_`` plus the name of the Python script.
# - The third argument is the name of the function used to record operators.
#

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# Python plugins are not supported in process.
dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer)

operator_server_file_path = Path(dpf.upload_file_in_tmp_folder(operator_file_path))
dpf.load_library(operator_server_file_path.parent, "py_easy_statistics", "load_operators")

###############################################################################
# Instantiate the operator.

new_operator = dpf.Operator("easy_statistics")

###############################################################################
# Connect a workflow
# ------------------
# Connect a workflow that computes the norm of the displacement to the
# ``easy_statistics`` operator. Methods of the ``easy_statistics`` class
# are dynamically added because specifications for the operator are
# defined in the plugin.

# %%
# .. graphviz::
#
#    digraph foo {
#       graph [pad="0.5", nodesep="0.3", ranksep="0.3"]
#       node [shape=box, style=filled, fillcolor="#ffcc00", margin="0"];
#       rankdir=LR;
#       splines=line;
#       ds [label="ds", shape=box, style=filled, fillcolor=cadetblue2];
#       ds -> displacement [style=dashed];
#       displacement -> norm;
#       norm -> easy_statistics;
#    }

###############################################################################
# Use the operator
# ----------------

ds = dpf.DataSources(dpf.upload_file_in_tmp_folder(examples.find_static_rst()))
displacement = dpf.operators.result.displacement(data_sources=ds)
norm = dpf.operators.math.norm(displacement)
new_operator.inputs.connect(norm)

print("first quartile is", new_operator.outputs.first_quartile())
print("median is", new_operator.outputs.median())
print("third quartile is", new_operator.outputs.third_quartile())
print("variance is", new_operator.outputs.variance())
