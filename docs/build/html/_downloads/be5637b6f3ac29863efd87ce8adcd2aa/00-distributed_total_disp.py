"""
.. _ref_distributed_total_disp:

Distributed post without client connection to remote processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how distributed files can be read and post processed 
on distributed processes. After remote post processing, results a merged
on the local process.

"""

###############################################################################
# Import dpf module and its examples files

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Create the template workflow of total displacement
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create displacement and norm operators

template_workflow = dpf.Workflow()
displacement = ops.result.displacement()
norm = ops.math.norm_fc(displacement)

###############################################################################
# Add the operators to the template workflow and name its inputs and outputs
# Once workflow's inputs and outputs are named, they can be connected later on
template_workflow.add_operators([displacement, norm])
template_workflow.set_input_name("data_sources", displacement.inputs.data_sources)
template_workflow.set_output_name("out", norm.outputs.fields_container)


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

remote_servers = [dpf.start_local_server(as_global=False),dpf.start_local_server(as_global=False)]
ips = [remote_server.ip for remote_server in remote_servers]
ports = [remote_server.port for remote_server in remote_servers]

###############################################################################
# Print the ips and ports
print("ips:", ips)
print("ports:", ports)

###############################################################################
# Here we show how we could send files in temporary directory if we were not
# in shared memory
files = examples.download_distributed_files()
server_file_paths = [dpf.upload_file_in_tmp_folder(files[0], server=remote_servers[0]),
                     dpf.upload_file_in_tmp_folder(files[1], server=remote_servers[1])]


###############################################################################
# Send workflows on servers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Here we create new instances on the server by copies of the template workflow
# We also connect the data sources to those workflows 
remote_workflows =[]
for i,server in enumerate(remote_servers) :
    remote_workflows.append(template_workflow.create_on_other_server(server))
    ds = dpf.DataSources(server_file_paths[i])
    remote_workflows[i].connect("data_sources", ds)
        
    
###############################################################################
# Create a local workflow able to merge the results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

local_workflow = dpf.Workflow()
merge = ops.utility.merge_fields_containers()
local_workflow.add_operator(merge)
local_workflow.set_input_name("in0", merge,0)
local_workflow.set_input_name("in1", merge,1)
local_workflow.set_output_name("merged", merge.outputs.merged_fields_container)
    
###############################################################################
# Connect the workflows together and get the output
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for i,server in enumerate(remote_servers) :
    local_workflow.connect_with(remote_workflows[i],("out", "in"+str(i)))
    
fc = local_workflow.get_output("merged", dpf.types.fields_container)
print(fc)
print(fc[0].min().data)
print(fc[0].max().data)

###############################################################################
# Shutdown the servers
# ~~~~~~~~~~~~~~~~~~~~~
dpf.server.shutdown_all_session_servers()
