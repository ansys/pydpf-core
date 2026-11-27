"""
.. _labels:

Add Nodal Labels on Plots
~~~~~~~~~~~~~~~~~~~~~~~~~
You can custom labels to specific nodes with specific label properties.
If label for a node is missing, by default nodal scalar value is shown.
"""

###############################################################################
# First, import the DPF-Core module as ``dpf_core`` and import the
# included examples file and ``DpfPlotter``
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.plotter import DpfPlotter

###############################################################################
# Next, open an example and print out the ``model`` object.  The
# :class:`Model <ansys.dpf.core.model.Model>` class helps to organize access
# methods for the result by keeping track of the operators and data sources
# used by the result
# file.
#
# Printing the model displays:
#
# - Analysis type
# - Available results
# - Size of the mesh
# - Number of results
#
model = dpf.Model(examples.msup_transient)
print(model)

###############################################################################
# Get the stress tensor and connect time scoping.
# Make sure to define the scoping as ``"Nodal"`` as the requested location,
# as the labels are supported only for Nodal results.
#
stress_tensor = model.results.stress()
time_scope = dpf.Scoping()
time_scope.ids = [20]  # [1, 2]
stress_tensor.inputs.time_scoping.connect(time_scope)
stress_tensor.inputs.requested_location.connect("Nodal")
# field = stress_tensor.outputs.fields_container.get_data()[0]

norm_op = dpf.Operator("norm_fc")
norm_op.inputs.connect(stress_tensor.outputs)
field_norm_stress = norm_op.outputs.fields_container()[0]
print(field_norm_stress)

norm_op2 = dpf.Operator("norm_fc")
disp = model.results.displacement()
disp.inputs.time_scoping.connect(time_scope)
norm_op2.inputs.connect(disp.outputs)
field_norm_disp = norm_op2.outputs.fields_container()[0]
print(field_norm_disp)
###############################################################################
#  Get the meshed region
#
mesh_set = model.metadata.meshed_region

###############################################################################
# Plot the results on the mesh, show the minimum and maximum.
#
plot = DpfPlotter()
plot.add_field(
    field_norm_stress,
    meshed_region=mesh_set,
    show_max=True,
    show_min=True,
    label_text_size=15,
    label_point_size=5,
)


# Add custom labels to specific nodes with specific label properties.
# If label for a node is missing, by default nodal value is shown.

my_nodes_1 = [mesh_set.nodes[0], mesh_set.nodes[10]]
my_labels_1 = ["MyNode1", "MyNode2"]
plot.add_node_labels(
    my_nodes_1,
    mesh_set,
    my_labels_1,
    italic=True,
    bold=True,
    font_size=26,
    text_color="white",
    font_family="courier",
    shadow=True,
    point_color="grey",
    point_size=20,
)

my_nodes_2 = [mesh_set.nodes[18], mesh_set.nodes[30]]
my_labels_2 = []  # ["MyNode3"]
plot.add_node_labels(
    my_nodes_2,
    mesh_set,
    my_labels_2,
    font_size=15,
    text_color="black",
    font_family="arial",
    shadow=False,
    point_color="white",
    point_size=15,
)

# Show figure
# You can set the camera positions using the `cpos` argument
# The three tuples in the list `cpos` represent camera position-
# focal point, and view up respectively.
plot.show_figure(
    show_axes=True,
    cpos=[(0.123, 0.095, 1.069), (-0.121, -0.149, 0.825), (0.0, 0.0, 1.0)],
)
