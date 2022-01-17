"""
.. _solution_combination:

Loadcase combination for principal stress and show max/min label.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to get a principal stress loadcase combination using DPF
And highlight min/max values in the plot.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.plotter import DpfPlotter

model = dpf.Model(examples.msup_transient)

# Instantiate stress
stress_tensor = model.results.stress()
time_scope = dpf.Scoping()
time_scope.ids = [1, 2]
stress_tensor.inputs.time_scoping.connect(time_scope)
stress_tensor.inputs.requested_location.connect("Nodal")

u"""
This code performs solution combination on two load cases.
=>LC1 - LC2
You can access individual loadcases as the fields of a fields_container for `stress_tensor`

LC1: stress_tensor.outputs.fields_container.get_data()[0]
LC2: stress_tensor.outputs.fields_container.get_data()[1]
"""

# Scale LC2 to -1
field_lc2 = stress_tensor.outputs.fields_container.get_data()[1]
stress_tensor_lc2_sc = dpf.operators.math.scale(field=field_lc2,
                                                ponderation=-1.0)
# Add load cases
field_lc1 = stress_tensor.outputs.fields_container.get_data()[0]
stress_tensor_combi = dpf.operators.math.add(fieldA=field_lc1,
                                             fieldB=stress_tensor_lc2_sc)

# Principal Stresses => Eigenvalues of the new stress tensor
p_inv = dpf.operators.invariant.principal_invariants()
p_inv.inputs.field.connect(stress_tensor_combi)

# Print S1 - Maximum Principal stress
print(p_inv.outputs.field_eig_1().data)

# Get the meshed region
mesh_set = model.metadata.meshed_region

# Plot the results on the mesh.
plot = DpfPlotter()
plot.add_field(p_inv.outputs.field_eig_1(),
               meshed_region=mesh_set,
               show_min=True,
               label_text_size=40,
               label_point_size=15,
               )
plot.show_figure(show_axes=True)
