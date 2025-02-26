"""
.. _ref_wrapping_numpy_capabilities:

Write user defined Operator
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to create a simple DPF python plugin holding a single Operator.
This Operator called "easy_statistics" computes simple statistics quantities on a scalar Field with
the help of numpy.
It's a simple example displaying how routines can be wrapped in DPF python plugins.
"""

###############################################################################
# Write Operator
# --------------
# To write the simplest DPF python plugins, a single python script is necessary.
# An Operator implementation deriving from
# :class:`ansys.dpf.core.custom_operator.CustomOperatorBase`
# and a call to :py:func:`ansys.dpf.core.custom_operator.record_operator`
# are the 2 necessary steps to create a plugin.
# The "easy_statistics" Operator will take a Field in input and return
# the first quartile, the median,
# the third quartile and the variance. The python Operator and its recording seat in the
# file plugins/easy_statistics.py. This file `easy_statistics.py` is downloaded
# and displayed here:

from ansys.dpf.core import examples

GITHUB_SOURCE_URL = "https://github.com/pyansys/pydpf-core/" \
                    "raw/examples/first_python_plugins/python_plugins"
EXAMPLE_FILE = GITHUB_SOURCE_URL + "/easy_statistics.py"
operator_file_path = examples.downloads._retrieve_file(
    EXAMPLE_FILE, "easy_statistics.py", "python_plugins"
)

with open(operator_file_path, "r") as f:
    for line in f.readlines():
        print('\t\t\t' + line)

###############################################################################
# Load Plugin
# -----------
# Once a python plugin is written, it can be loaded with the function
# :py:func:`ansys.dpf.core.core.load_library`
# taking as first argument the path to the directory of the plugin, as second argument
# ``py_`` + the name of
# the python script, and as last argument the function's name used to record operators.

import os
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# python plugins are not supported in process
dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer)

operator_server_file_path = dpf.upload_file_in_tmp_folder(operator_file_path)
dpf.load_library(os.path.dirname(operator_server_file_path), "py_easy_statistics", "load_operators")

###############################################################################
# Once the Operator loaded, it can be instantiated with:

new_operator = dpf.Operator("easy_statistics")

###############################################################################
# To use this new Operator, a workflow computing the norm of the displacement
# is connected to the "easy_statistics" Operator.
# Methods of the class ``easy_statistics`` are dynamically added thanks to the Operator's
# specification defined in the plugin.

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
# Use the Custom Operator
# -----------------------

ds = dpf.DataSources(dpf.upload_file_in_tmp_folder(examples.static_rst))
displacement = dpf.operators.result.displacement(data_sources=ds)
norm = dpf.operators.math.norm(displacement)
new_operator.inputs.connect(norm)

print("first quartile is", new_operator.outputs.first_quartile())
print("median is", new_operator.outputs.median())
print("third quartile is", new_operator.outputs.third_quartile())
print("variance is", new_operator.outputs.variance())
