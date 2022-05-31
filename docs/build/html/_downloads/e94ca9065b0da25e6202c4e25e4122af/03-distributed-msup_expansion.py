"""
.. _ref_distributed_msup:

Distributed modal superposition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how distributed files can be read and expanded
on distributed processes. The modal basis (2 distributed files) is read
on 2 remote servers and the modal response reading and the expansion is
done on a third server.
"""

###############################################################################
# Import dpf module and its examples files

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Create the template workflow
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this workflow will provide the modal basis and the mesh for each domain

template_workflow = dpf.Workflow()
displacement = ops.result.displacement()
mesh = ops.mesh.mesh_provider()

###############################################################################
# Add the operators to the template workflow and name its inputs and outputs
# Once workflow's inputs and outputs are named, they can be connected later on
template_workflow.add_operators([displacement])
template_workflow.set_input_name("data_sources", displacement.inputs.data_sources)
template_workflow.set_input_name("data_sources", mesh.inputs.data_sources)
template_workflow.set_output_name("out", displacement.outputs.fields_container)
template_workflow.set_output_name("outmesh", mesh.outputs.mesh)

###############################################################################
# Configure the servers
# ~~~~~~~~~~~~~~~~~~~~~~
# Make a list of ip addresses an port numbers on which dpf servers are
# started. Workflows instances will be created on each of those servers to
# address each a different result file.
# In this example, we will post process an analysis distributed in 2 files,
# we will consequently require 2 remote processes
# To make this example easier, we will start local servers here,
# but we could get connected to any existing servers on the network.

remote_servers = [dpf.start_local_server(as_global=False), dpf.start_local_server(as_global=False)]
ips = [remote_server.ip for remote_server in remote_servers]
ports = [remote_server.port for remote_server in remote_servers]

###############################################################################
# Print the ips and ports
print("ips:", ips)
print("ports:", ports)

###############################################################################
# Choose the file path

base_path = examples.distributed_msup_folder
files = [base_path + r'/file0.mode', base_path + r'/file1.mode']
files_aux = [base_path + r'/file0.rst', base_path + r'/file1.rst']

###############################################################################
# Send workflows on servers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Here we create new instances on the server by copies of the template workflow
# We also connect the data sources to those workflows
remote_workflows = []
for i, server in enumerate(remote_servers):
    remote_workflows.append(template_workflow.create_on_other_server(server))
    ds = dpf.DataSources(files[i])
    ds.add_file_path(files_aux[i])
    remote_workflows[i].connect("data_sources", ds)

###############################################################################
# Create a local workflow for expansion
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In this workflow we merge the modal basis, the meshes, read the modal response
# and expand the modal response with the modal basis

local_workflow = dpf.Workflow()
merge = ops.utility.merge_fields_containers()
merge_mesh = ops.utility.merge_meshes()

ds = dpf.DataSources(base_path + r'/file_load_1.rfrq')
response = ops.result.displacement(data_sources=ds)
response.inputs.mesh(merge_mesh.outputs.merges_mesh)

expansion = ops.math.modal_superposition(solution_in_modal_space=response, modal_basis=merge)
component = ops.logic.component_selector_fc(expansion, 1)

local_workflow.add_operators([merge, response, expansion, merge_mesh, component])
local_workflow.set_input_name("in0", merge, 0)
local_workflow.set_input_name("in1", merge, 1)
local_workflow.set_input_name("inmesh0", merge_mesh, 0)
local_workflow.set_input_name("inmesh1", merge_mesh, 1)

local_workflow.set_output_name("expanded", component.outputs.fields_container)
local_workflow.set_output_name("mesh", merge_mesh.outputs.merges_mesh)

###############################################################################
# Connect the workflows together and get the output
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for i, server in enumerate(remote_servers):
    local_workflow.connect_with(remote_workflows[i],
                                {"out": "in" + str(i), "outmesh": "inmesh" + str(i)})

fc = local_workflow.get_output("expanded", dpf.types.fields_container)
merged_mesh = local_workflow.get_output("mesh", dpf.types.meshed_region)
merged_mesh.plot(fc.get_field_by_time_complex_ids(1, 0))
merged_mesh.plot(fc.get_field_by_time_complex_ids(10, 0))
print(fc)

dpf.server.shutdown_all_session_servers()
