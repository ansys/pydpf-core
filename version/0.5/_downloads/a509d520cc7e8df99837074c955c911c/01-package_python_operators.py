"""
.. _ref_python_plugin_package:

Write user defined Operators as a package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how more complex DPF python plugins of Operators can be
created as standard python packages.
The benefits of writing packages instead of simple scripts are:
componentization (split the code in several
python modules or files), distribution (with packages,
standard python tools can be used to upload and
download packages) and documentation (READMEs, docs, tests and
examples can be added to the package).

This plugin will hold 2 different Operators:
  - One returning all the scoping ids having data higher than the average
  - One returning all the scoping ids having data lower than the average
"""

###############################################################################
# Write Operator
# --------------
# For this more advanced use case, a python package is created.
# Each Operator implementation derives from
# :class:`ansys.dpf.core.custom_operator.CustomOperatorBase`
# and a call to :py:func:`ansys.dpf.core.custom_operator.record_operator`
# records the Operators of the plugin.
# The python package `average_filter_plugin` is downloaded and displayed here:

import os
from ansys.dpf.core import examples

print('\033[1m average_filter_plugin')
file_list = ["__init__.py", "operators.py", "operators_loader.py", "common.py"]
plugin_folder = None
GITHUB_SOURCE_URL = "https://github.com/pyansys/pydpf-core/raw/" \
                    "examples/first_python_plugins/python_plugins/average_filter_plugin"

for file in file_list:
    EXAMPLE_FILE = GITHUB_SOURCE_URL + "/average_filter_plugin/" + file
    operator_file_path = examples.downloads._retrieve_file(
        EXAMPLE_FILE, file, "python_plugins/average_filter_plugin"
    )
    plugin_folder = os.path.dirname(operator_file_path)
    print(f'\033[1m {file}:\n \033[0m')
    with open(operator_file_path, "r") as f:
        for line in f.readlines():
            print('\t\t\t' + line)
    print("\n\n")


###############################################################################
# Load Plugin
# -----------
# Once a python plugin is written as a package, it can be loaded with the function
# :py:func:`ansys.dpf.core.core.load_library` taking as first argument the
# path to the directory of the plugin,
# as second argument ``py_`` + any name identifying the plugin,
# and as last argument the function's name exposed in the __init__ file
# and used to record operators.

import os
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# python plugins are not supported in process
dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer)

tmp = dpf.make_tmp_dir_server()
dpf.upload_files_in_folder(
    dpf.path_utilities.join(tmp, "average_filter_plugin"),
    plugin_folder
)
dpf.load_library(
    os.path.join(dpf.path_utilities.join(tmp, "average_filter_plugin")),
    "py_average_filter",
    "load_operators")

###############################################################################
# Once the Plugin loaded, Operators recorded in the plugin can be used with:

new_operator = dpf.Operator("ids_with_data_lower_than_average")

###############################################################################
# To use this new Operator, a workflow computing the norm of the displacement
# is connected to the "ids_with_data_lower_than_average" Operator.
# Methods of the class ``ids_with_data_lower_than_average`` are dynamically
# added thanks to the Operator's specification.

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
# Use the Custom Operator
# -----------------------

ds = dpf.DataSources(dpf.upload_file_in_tmp_folder(examples.static_rst))
displacement = dpf.operators.result.displacement(data_sources=ds)
norm = dpf.operators.math.norm(displacement)
new_operator.inputs.connect(norm)


new_scoping = new_operator.outputs.scoping()
print("scoping in was:", norm.outputs.field().scoping)
print("----------------------------------------------")
print("scoping out is:", new_scoping)
