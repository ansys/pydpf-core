# noqa: D400
"""
.. _ref_multi_stage_cyclic:

Multi-stage cyclic symmetry example
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
# This example expands displacement results, by default on all
# nodes and the first time step. Note that the displacements are expanded using
# the :func:`read_cyclic
# <ansys.dpf.core.operators.mesh.mesh_provider.InputsMeshProvider.read_cyclic>`
# property with 2 as an argument (1 would ignore the cyclic symmetry).

# Create displacement cyclic operator
UCyc = model.results.displacement()
UCyc.inputs.read_cyclic(2)

# expand the displacements and get a total deformation
nrm = dpf.Operator("norm_fc")
nrm.inputs.connect(UCyc.outputs)
fields = nrm.outputs.fields_container()

# # get the expanded mesh
mesh_provider = model.metadata.mesh_provider
mesh_provider.inputs.read_cyclic(2)
mesh = mesh_provider.outputs.mesh()

# # plot the expanded result on the expanded mesh
mesh.plot(fields)

###############################################################################
# Expand stresses at a given time step
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# define stress expansion operator and request stresses at time set = 3
SCyc = model.results.stress()
SCyc.inputs.read_cyclic(2)
SCyc.inputs.time_scoping.connect([3])

# request the results averaged on the nodes
SCyc.inputs.requested_location.connect("Nodal")

# request equivalent von mises operator and connect it to stress
# operator
eqv = dpf.Operator("eqv_fc")
eqv.inputs.connect(SCyc.outputs)

# expand the results and get stress eqv
fields = eqv.outputs.fields_container()

# plot the expanded result on the expanded mesh
mesh.plot(fields)
