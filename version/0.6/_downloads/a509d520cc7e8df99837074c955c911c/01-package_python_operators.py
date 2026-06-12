"""
.. _ref_python_plugin_package:

Create a plug-in package with multiple operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to create a plug-in package with multiple operators.
The benefits of writing packages rather than simple scripts are:

- **Componentization:** You can split the code into several Python modules or files.
- **Distribution:** You can use standard Python tools to upload and download packages.
- **Documentation:** You can add README files, documentation, tests, and examples to the package.

For this example, the plug-in package contains two different operators:

- One that returns all scoping ID having data higher than the average
- One that returns all scoping IDs having data lower than the average

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
# Load the plug-in package
# ------------------------
# You use the function :py:func:`ansys.dpf.core.core.load_library` to load the
# plug-in package.
#
# - The first argument is the path to the directory where the plug-in package
#   is located.
# - The second argument is ``py_`` plus any name identifying the plug-in package.
# - The third argument is the name of the function exposed in the ``__init__ file``
#   for the plug-in package that is used to record operators.
#

import os
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# Python plugins are not supported in process.
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
