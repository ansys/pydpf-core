"""
.. _ref_python_plugin_package:

Write user defined Operators as a package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how more complex DPF python plugins of Operators can be created as standard python packages.
The benefits of writing packages instead of simple scripts are: componentization (split the code in several
python modules or files), distribution (with packages, standard python tools can be used to upload and
download packages) and documentation (READMEs, docs, tests and examples can be added to the package).

This plugin will hold 2 different Operators:
  - One returning all the scoping ids having data higher than the average
  - One returning all the scoping ids having data lower than the average
"""

###############################################################################
# Write Operator
# --------------
# For this more advanced use case, a python package is created.
# Each Operator implementation derives from :class:`ansys.dpf.core.custom_operator.CustomOperatorBase`
# and a call to :py:func:`ansys.dpf.core.custom_operator.record_operator` records the Operators of the plugin.
# The complete package looks like:

# %%
# .. card:: average_filter_plugin
#
#    .. dropdown:: __init__.py
#
#       .. literalinclude:: plugins/average_filter_plugin/__init__.py
#
#    .. dropdown:: operators.py
#
#       .. literalinclude:: plugins/average_filter_plugin/operators.py
#
#    .. dropdown:: operators_loader.py
#
#       .. literalinclude:: plugins/average_filter_plugin/operators_loader.py
#
#    .. dropdown:: common.py
#
#       .. literalinclude:: plugins/average_filter_plugin/common.py
#


###############################################################################
# Load Plugin
# -----------
# Once a python plugin is written as a package, it can be loaded with the function
# :py:func:`ansys.dpf.core.core.load_library` taking as first argument the path to the directory of the plugin,
# as second argument ``py_`` + any name identifying the plugin,
# and as last argument the function's name exposed in the __init__ file and used to record operators.

import os
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

#dpf.connect_to_server(port=50052)
tmp = dpf.make_tmp_dir_server()
dpf.upload_files_in_folder(
    dpf.path_utilities.join(tmp, "average_filter_plugin"),
    os.path.join(os.getcwd(), "..", "..", "docs", "source", "examples",
                 "07-python-operators", "plugins", "average_filter_plugin")
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
# Methods of the class ``ids_with_data_lower_than_average`` are dynamically added thanks to the Operator's
# specification.

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
