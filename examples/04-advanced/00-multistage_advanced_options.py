"""
.. _ref_multi_stage_cyclic_advanced:

Multi-stage cyclic symmetry using advanced customization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to expand on selected sectors the mesh and results
from a multi-stage cyclic analysis. It also shows how to use the cyclic support
for advanced postprocessing
"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Create the model and display the state of the result.
cyc = examples.download_multi_stage_cyclic_result()
model = dpf.Model(cyc)
print(model)

###############################################################################
# Check the result info to verify that it's a multi-stage model
result_info = model.metadata.result_info
print(result_info.has_cyclic)
print(result_info.cyclic_symmetry_type)

###############################################################################
# Go over the cyclic support
cyc_support = result_info.cyclic_support
print("num stages:", cyc_support.num_stages)
print("num_sectors stage 0:", cyc_support.num_sectors(0))
print("num_sectors stage 1:", cyc_support.num_sectors(1))
print(
    "num nodes in the first stage's base sector: ",
    len(cyc_support.base_nodes_scoping(0)),
)

###############################################################################
# Expand displacement results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This example expands displacement results on chosen sectors.


# Create displacement cyclic operator
UCyc = dpf.operators.result.cyclic_expanded_displacement()
UCyc.inputs.data_sources(model.metadata.data_sources)
# Select the sectors to expand on the first stage
UCyc.inputs.sectors_to_expand([0, 1, 2])
# Or select the sectors to expand stage by stage
sectors_scopings = dpf.ScopingsContainer()
sectors_scopings.labels = ["stage"]
sectors_scopings.add_scoping({"stage": 0}, dpf.Scoping(ids=[0, 1, 2]))
sectors_scopings.add_scoping({"stage": 1}, dpf.Scoping(ids=[0, 1, 2, 3, 4, 5, 6]))
UCyc.inputs.sectors_to_expand(sectors_scopings)

# expand the displacements and get a total deformation
nrm = dpf.Operator("norm_fc")
nrm.inputs.connect(UCyc.outputs)
fields = nrm.outputs.fields_container()

# # get the expanded mesh
mesh_provider = model.metadata.mesh_provider
mesh_provider.inputs.read_cyclic(2)
mesh = mesh_provider.outputs.mesh()

###############################################################################
# Plot the expanded result on the expanded mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mesh.plot(fields)

###############################################################################
# Choose to expand only some sectors for the mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cyc_support_provider = ops.metadata.cyclic_support_provider(
    data_sources=model.metadata.data_sources
)
cyc_support_provider.inputs.sectors_to_expand(sectors_scopings)
mesh_exp = ops.metadata.cyclic_mesh_expansion(cyclic_support=cyc_support_provider)
selected_sectors_mesh = mesh_exp.outputs.meshed_region()

# # plot the expanded result on the expanded mesh
selected_sectors_mesh.plot(fields)

###############################################################################
# Check results precisely
# ~~~~~~~~~~~~~~~~~~~~~~~

# Print the time_freq_support to see the harmonic index
print(model.metadata.time_freq_support)
print(model.metadata.time_freq_support.get_harmonic_indices(stage_num=1).data)

# Harmonic index 0 means that the results are symmetric sectors by sector
# taking a node in the base sector of the first stage
node_id = cyc_support.base_nodes_scoping(0)[18]
print(node_id)

# Check what are the expanded ids of this node
expanded_ids = cyc_support.expand_node_id(node_id, [0, 1, 2], 0)
print(expanded_ids.ids)

# Verify that the displacement values are the same on all those nodes
for node in expanded_ids.ids:
    print(fields[0].get_entity_data_by_id(node))
