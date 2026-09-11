"""
.. _compare_results:

Compare Results Using the Plotter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to plot several meshes/results combination
over the same plotter, in order to compare them. The usecase will be
to compare results at different time steps.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.plotter import DpfPlotter

###############################################################################
# Compare two results
# ~~~~~~~~~~~~~~~~~~~
# Now we will use an :class:`ansys.dpf.core.plotter.DpfPlotter` to plot two different
# results over the same mesh and make a comparison.

# Here we create a Model and request its mesh
model = dpf.Model(examples.msup_transient)
mesh_set2 = model.metadata.meshed_region

# Then we need to request the displacement for two different time steps
displacement_operator = model.results.displacement()
displacement_operator.inputs.time_scoping.connect([2, 15])
displacement_set2 = displacement_operator.outputs.fields_container()[0]
displacement_set15 = displacement_operator.outputs.fields_container()[1]

###############################################################################
# Now we create an :class:`ansys.dpf.core.plotter.DpfPlotter` and add the
# first mesh and the first result
pl = DpfPlotter()
pl.add_field(displacement_set2, mesh_set2)

# Then it is needed to create a new mesh and translate it along x axis
mesh_set15 = mesh_set2.deep_copy()
overall_field = dpf.fields_factory.create_3d_vector_field(1, dpf.locations.overall)
overall_field.append([0.2, 0.0, 0.0], 1)
coordinates_to_update = mesh_set15.nodes.coordinates_field
add_operator = dpf.operators.math.add(coordinates_to_update, overall_field)
coordinates_updated = add_operator.outputs.field()
coordinates_to_update.data = coordinates_updated.data

# Finally we feed the DpfPlotter with the second mesh and the second result
# and we plot the result
pl.add_field(displacement_set15, mesh_set15)
pl.show_figure(show_axes=True)
