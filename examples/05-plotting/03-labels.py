"""
.. _labels:

Add Nodal Labels on Plots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
One can custom labels to specific nodes with specific label properties.
If label for a node is missing, by default nodal scalar value is shown.
"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.plotter import DpfPlotter

model = dpf.Model(examples.msup_transient)

# Get stress tensor
stress_tensor = model.results.stress()
time_scope = dpf.Scoping()
time_scope.ids = [1, 2]
stress_tensor.inputs.time_scoping.connect(time_scope)
stress_tensor.inputs.requested_location.connect("Nodal")

# Get the meshed region
mesh_set = model.metadata.meshed_region

# Plot the results on the mesh, show Min and Max
plot = DpfPlotter()
plot.add_field(stress_tensor.outputs.fields_container.get_data()[1], meshed_region=mesh_set,
               show_max=True, show_min=True,
               label_text_size=15,
               label_point_size=5,
               )

"""
Add custom labels to specific nodes with specific label properties.
If label for a node is missing, by default nodal value is shown.
"""

my_nodes_1 = [mesh_set.nodes[0], mesh_set.nodes[10]]
my_labels_1 = ["MyNode1", "MyNode2"]
plot.add_node_labels(my_nodes_1, mesh_set, my_labels_1, italic=True, bold=True,
                     font_size=26, text_color="white",
                     font_family="courier", shadow=True,
                     point_color="grey", point_size=20)

my_nodes_2 = [mesh_set.nodes[20], mesh_set.nodes[30]]
my_labels_2 = ["MyNode3"]
plot.add_node_labels(my_nodes_2, mesh_set, my_labels_2,
                     font_size=30, text_color="yellow",
                     font_family="arial", shadow=False,
                     point_color="white", point_size=30)

# Show figure
plot.show_figure(show_axes=True)
