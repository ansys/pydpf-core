"""
.. _ref_distributed_workflows_on_remote:

Connect workflows on different processes implicitly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how distributed files can be read and post processed 
on distributed processes. After remote post processing,
results a merged on the local process. In this example, different workflows are
directly created on different servers. Those workflows are then connected
together without having to care that they are on remote processes.

"""
###############################################################################
# Import dpf module and its examples files

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops


###############################################################################
# Configure the servers
# ~~~~~~~~~~~~~~~~~~~~~~
# To make this example easier, we will start local servers here, 
# but we could get connected to any existing servers on the network.

remote_servers = [dpf.start_local_server(as_global=False),dpf.start_local_server(as_global=False)]

###############################################################################
# Create template workflows on remote servers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# For the purpose of this example, we will create 2 workflows computing 
# elemental nodal stresses on different servers. The second workflow will 
# multiply by 2.0 the stresses. A last workflow will merge the outputs

files = examples.download_distributed_files()


###############################################################################
# first workflow S
workflow1 = dpf.Workflow(server=remote_servers[0])
model = dpf.Model(files[0],server=remote_servers[0])
stress1 = model.results.stress()
workflow1.add_operator(stress1)
workflow1.set_output_name("out1", stress1.outputs.fields_container)

###############################################################################
# second workflow S*2.0
workflow2 = dpf.Workflow(server=remote_servers[1])
model = dpf.Model(files[1],server=remote_servers[1])
stress2 = model.results.stress()
mul = stress2*2.0
workflow2.add_operator(mul)
workflow2.set_output_name("out2", mul.outputs.fields_container)

###############################################################################
# third workflow merge
local_workflow = dpf.Workflow()
merge = ops.utility.merge_fields_containers()
nodal = ops.averaging.to_nodal_fc(merge)
local_workflow.add_operators([merge,nodal])
local_workflow.set_input_name("in1", merge,0)
local_workflow.set_input_name("in2", merge,1)
local_workflow.set_output_name("merged", nodal.outputs.fields_container)

###############################################################################
# Connect the workflows together and get the output
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
local_workflow.connect_with(workflow1,("out1", "in1"))
local_workflow.connect_with(workflow2,("out2", "in2"))
    
fc = local_workflow.get_output("merged", dpf.types.fields_container)
fc[0].meshed_region.plot(fc[0])
