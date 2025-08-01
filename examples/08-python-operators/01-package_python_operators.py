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
.. _ref_python_plugin_package:

Create a plug-in package with multiple operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to create a plug-in package with multiple operators.
The benefits of writing a package rather than simple scripts are:

- **Componentization:** You can split the code into several Python modules or files.
- **Distribution:** You can use standard Python tools to upload and download packages.
- **Documentation:** You can add README files, documentation, tests, and examples to the package.

For this example, the plug-in package contains two different operators:

- One that returns all scoping IDs having data higher than the average
- One that returns all scoping IDs having data lower than the average

.. note::
    This example requires DPF 5.0 (Ansys 2023R1) or above.
    For more information, see :ref:`ref_compatibility`.

"""

###############################################################################
# Create the plug-in package
# --------------------------
# Each operator implementation derives from the
# :class:`ansys.dpf.core.custom_operator.CustomOperatorBase` class
# and a call to the :py:func:`ansys.dpf.core.custom_operator.record_operator`
# method, which records the operators of the plug-in package.
#
# Download the ``average_filter_plugin`` plug-in package that has already been
# created for you.
from ansys.dpf.core import examples

plugin_folder = examples.download_average_filter_plugin()

###############################################################################
# Load the plug-in package
# ------------------------
# You use the function :py:func:`ansys.dpf.core.core.load_library` to load the
# plug-in package.
#
# - The first argument is the path to the directory where the plug-in package
#   is located.
# - The second argument is ``py_<package>``, where ``<package>`` is the name
#   identifying the plug-in package.
# - The third argument is the name of the function exposed in the ``__init__`` file
#   for the plug-in package that is used to record operators.
#

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# Python plugins are not supported in process.
dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer)

tmp = dpf.make_tmp_dir_server()
dpf.upload_files_in_folder(dpf.path_utilities.join(tmp, "average_filter_plugin"), plugin_folder)
dpf.load_library(
    dpf.path_utilities.join(tmp, "average_filter_plugin"),
    "py_average_filter",
    "load_operators",
)

###############################################################################
# Instantiate the operator.

new_operator = dpf.Operator("ids_with_data_lower_than_average")

###############################################################################
# Connect a workflow
# ------------------
# Connect a workflow that computes the norm of the displacement
# to the ``ids_with_data_lower_than_average`` operator.
# Methods of the ``ids_with_data_lower_than_average`` class are dynamically
# added because specifications for the operator are defined in the plug-in
# package.

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
#       norm -> ids_with_data_lower_than_average;
#    }

###############################################################################
# Use the operator
# ----------------

ds = dpf.DataSources(dpf.upload_file_in_tmp_folder(examples.find_static_rst()))
displacement = dpf.operators.result.displacement(data_sources=ds)
norm = dpf.operators.math.norm(displacement)
new_operator.inputs.connect(norm)


new_scoping = new_operator.outputs.scoping()
print("scoping in was:", norm.outputs.field().scoping)
print("----------------------------------------------")
print("scoping out is:", new_scoping)
