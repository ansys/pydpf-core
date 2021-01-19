"""
.. _ref_multi_stage_cyclic:

Multi-stage Cyclic Symmetry Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to expand the mesh and results from a
multi-stage cyclic analysis.

"""
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create the model and display the state of the result.
cyc = examples.download_multi_stage_cyclic_result()
model = dpf.Model(cyc)
print(model)


###############################################################################
# Expand displacement results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In this example we expand displacement results, by default on all
# nodes and the first time step.

# Create displacement cyclic operator
UCyc = model.operator("mapdl::rst::U_cyclic")

# expand the displacements and get a total deformation
nrm = dpf.Operator("norm_fc")
nrm.inputs.connect(UCyc.outputs)
fields = nrm.outputs.fields_container()

# get the expanded mesh
mesh = UCyc.outputs.expanded_meshed_region.get_data()

# plot the expanded result on the expanded mesh
mesh.plot(fields)

###############################################################################
# Expand stresses at a given time step
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# define stress expansion operator and request stresses at time set = 3
SCyc = model.operator("mapdl::rst::S_cyclic")
SCyc.inputs.time_scoping.connect([3])

# request the results averaged on the nodes
SCyc.inputs.requested_location.connect("Nodal")

# connect the base mesh and the expanded mesh, to avoid rexpanding the
# mesh
SCyc.inputs.sector_mesh.connect(model.metadata.meshed_region)
SCyc.inputs.expanded_meshed_region.connect(mesh)

# request equivalent von mises operator and connect it to stress
# operator
eqv = dpf.Operator("eqv_fc")
eqv.inputs.connect(SCyc.outputs)

# expand the results and get stress eqv
fields = eqv.outputs.fields_container()

# plot the expanded result on the expanded mesh
mesh.plot(fields)
