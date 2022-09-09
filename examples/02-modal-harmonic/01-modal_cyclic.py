"""
.. _ref_basic_cyclic:

Modal Cyclic symmetry Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to expand a cyclic mesh and its results.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create the model and display the state of the result.
model = dpf.Model(examples.simple_cyclic)
print(model)

###############################################################################
# Expand displacement results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In this example we expand displacement results, by default on all
# nodes and the first time step.

# Create displacement cyclic operator
u_cyc = model.operator("mapdl::rst::U_cyclic")

# expand the displacements
fields = u_cyc.outputs.fields_container()

# # get the expanded mesh
mesh_provider = model.metadata.mesh_provider
mesh_provider.inputs.read_cyclic(2)
mesh = mesh_provider.outputs.mesh()

# plot the expanded result on the expanded mesh
mesh.plot(fields[0])

###############################################################################
# Expand stresses at a given time step
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# define stress expansion operator and request stresses at time set = 8
scyc_op = model.operator("mapdl::rst::S_cyclic")
scyc_op.inputs.read_cyclic(2)
scyc_op.inputs.time_scoping.connect([8])

# request the results averaged on the nodes
scyc_op.inputs.requested_location.connect("Nodal")

# connect the base mesh and the expanded mesh, to avoid rexpanding the mesh
scyc_op.inputs.sector_mesh.connect(model.metadata.meshed_region)
# scyc_op.inputs.expanded_meshed_region.connect(mesh)

# request equivalent von mises operator and connect it to stress operator
eqv = dpf.Operator("eqv_fc")
eqv.inputs.connect(scyc_op.outputs)

# expand the results and get stress eqv
fields = eqv.outputs.fields_container()

# plot the expanded result on the expanded mesh
# mesh.plot(fields[0])


###############################################################################
# Expand stresses at given sectors
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# define stress expansion operator and request stresses at time set = 8
scyc_op = model.operator("mapdl::rst::S_cyclic")
scyc_op.inputs.read_cyclic(2)
scyc_op.inputs.time_scoping.connect([8])

# request the results averaged on the nodes
scyc_op.inputs.requested_location.connect("Nodal")

# connect the base mesh and the expanded mesh, to avoid rexpanding the mesh
scyc_op.inputs.sector_mesh.connect(model.metadata.meshed_region)
# scyc_op.inputs.expanded_meshed_region.connect(mesh)

# request results on sectors 1, 3 and 5
scyc_op.inputs.sectors_to_expand.connect([1, 3, 5])

# extract Sy (use component selector and select the component 1)
comp_sel = dpf.Operator("component_selector_fc")
comp_sel.inputs.fields_container.connect(scyc_op.outputs.fields_container)
comp_sel.inputs.component_number.connect(0)

# expand the displacements and get the resuls
fields = comp_sel.outputs.fields_container()

# plot the expanded result on the expanded mesh
# mesh.plot(fields[0])


###############################################################################
# Expand stresses and average to elemental location
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# define stress expansion operator and request stresses at time set = 8
scyc_op = model.operator("mapdl::rst::S_cyclic")
scyc_op.inputs.read_cyclic(2)
scyc_op.inputs.time_scoping.connect([8])

# request the results in the solver
scyc_op.inputs.bool_rotate_to_global.connect(False)

# connect the base mesh and the expanded mesh, to avoid rexpanding the mesh
scyc_op.inputs.sector_mesh.connect(model.metadata.meshed_region)
# scyc_op.inputs.expanded_meshed_region.connect(mesh)

# request to elemental averaging operator
to_elemental = dpf.Operator("to_elemental_fc")
to_elemental.inputs.fields_container.connect(scyc_op.outputs.fields_container)

# extract Sy (use component selector and select the component 1)
comp_sel = dpf.Operator("component_selector_fc")
comp_sel.inputs.fields_container.connect(to_elemental.outputs.fields_container)
comp_sel.inputs.component_number.connect(1)

# expand the displacements and get the resuls
fields = comp_sel.outputs.fields_container()

# # plot the expanded result on the expanded mesh
mesh.plot(fields)
