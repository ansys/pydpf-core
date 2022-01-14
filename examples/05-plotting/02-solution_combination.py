from ansys.dpf import core as dpf
from ansys.dpf.core.plotter import DpfPlotter

model = dpf.Model(r"D:\SRs\2022\SRSS_SolutionCombination\Solution combination_files\dp0\SYS\MECH\file.rst")

# Instantiate S1
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
stress_tensor_lc2_sc = dpf.operators.math.scale(field=stress_tensor.outputs.fields_container.get_data()[1],
                                                ponderation=-1.0)
# Add load cases
stress_tensor_combi = dpf.operators.math.add(fieldA=stress_tensor.outputs.fields_container.get_data()[0],
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
plot.add_field(p_inv.outputs.field_eig_1(), meshed_region=mesh_set, show_max=True, show_min=True)
plot.show_figure(show_axes=True)
