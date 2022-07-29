"""
.. _solution_combination:

Load Case Combination for Principal Stress
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to get a principal stress loadcase combination using DPF
And highlight min/max values in the plot.

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
# Make sure to define ``Nodal`` as the requested location,
# as the labels are supported only for Nodal results.
#
stress_tensor = model.results.stress()
time_scope = dpf.Scoping()
time_scope.ids = [1, 2]
stress_tensor.inputs.time_scoping.connect(time_scope)
stress_tensor.inputs.requested_location.connect("Nodal")

###############################################################################
# This code performs solution combination on two load cases.
# =>LC1 - LC2
# You can access individual loadcases as the fields of a fields_container for ``stress_tensor``.
# LC1: stress_tensor.outputs.fields_container.get_data()[0]
# LC2: stress_tensor.outputs.fields_container.get_data()[1]
#
# Scale LC2 to -1
field_lc2 = stress_tensor.outputs.fields_container.get_data()[1]
stress_tensor_lc2_sc = dpf.operators.math.scale(field=field_lc2, ponderation=-1.0)

###############################################################################
# Add load cases
#
field_lc1 = stress_tensor.outputs.fields_container.get_data()[0]
stress_tensor_combi = dpf.operators.math.add(
    fieldA=field_lc1, fieldB=stress_tensor_lc2_sc
)

###############################################################################
# Principal Stresses are the Eigenvalues of the stress tensor.
# Use ``principal_invariants`` to get S1, S2 and S3
#
p_inv = dpf.operators.invariant.principal_invariants()
p_inv.inputs.field.connect(stress_tensor_combi)

###############################################################################
# Print S1 - Maximum Principal stress
#
print(p_inv.outputs.field_eig_1().data)

###############################################################################
# Get the meshed region
#
mesh_set = model.metadata.meshed_region

###############################################################################
# Plot the results on the mesh.
# ``label_text_size`` and ``label_point_size`` control font size of the label.
#
plot = DpfPlotter()
plot.add_field(p_inv.outputs.field_eig_1(), meshed_region=mesh_set)

# You can set the camera positions using the `cpos` argument
# The three tuples in the list `cpos` represent camera position-
# focal point, and view up respectively.
plot.show_figure(show_axes=True)
