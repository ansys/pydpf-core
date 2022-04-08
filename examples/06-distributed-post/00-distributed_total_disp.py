"""
Distributed post without client connection to remote processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To help understand this example the following diagram is provided. It shows 
the operator chain used to compute the final result.

.. graphviz::
   :align: center

   digraph foo {
        size="6,6";
        node [shape=box, style=filled, fillcolor="#ffcc00"];
        rankdir=LR;
        splines=line;

        disp01 [label="displacement"];
        disp02 [label="displacement"];
        norm01 [label="norm"];
        norm02 [label="norm"];

        subgraph cluster_1 {
            ds01 [label="data_src", shape=box, style=filled, fillcolor=cadetblue2];
            
            ds01 -> disp01 [style=dashed];
            disp01 -> norm01;
            
            label="Server 1";
            style=filled;
            fillcolor=lightgrey;
        }
        
        subgraph cluster_2 {
            ds02 [label="data_src", shape=box, style=filled, fillcolor=cadetblue2];
            
            ds02 -> disp02 [style=dashed];
            disp02 -> norm02;

            label="Server 2";
            style=filled;
            fillcolor=lightgrey;
        }

        norm01 -> "merge";
        norm02 -> "merge";
   }
"""

###############################################################################
# Import dpf module and its examples files

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Configure the servers
# ~~~~~~~~~~~~~~~~~~~~~~
# Make a list of ip addresses and port numbers on which dpf servers are
# started. Operator instances will be created on each of those servers to
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
# Here we show how we could send files in temporary directory if we were not
# in shared memory
files = examples.download_distributed_files()
server_file_paths = [dpf.upload_file_in_tmp_folder(files[0], server=remote_servers[0]),
                     dpf.upload_file_in_tmp_folder(files[1], server=remote_servers[1])]

###############################################################################
# Create the operators on the servers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# On each server we create two new operators for 'displacement' and 'norm' 
# computations and define their data sources. The displacement operator 
# receives data from the data file in its respective server. And the norm 
# operator, being chained to the displacement operator, receives input from the 
# output of this one.
remote_operators = []
for i, server in enumerate(remote_servers):
    displacement = ops.result.displacement(server=server)
    norm = ops.math.norm_fc(displacement, server=server)
    remote_operators.append(norm)
    ds = dpf.DataSources(server_file_paths[i], server=server)
    displacement.inputs.data_sources(ds)

###############################################################################
# Create a merge_fields_containers operator able to merge the results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

merge = ops.utility.merge_fields_containers()

###############################################################################
# Connect the operators together and get the output
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for i, server in enumerate(remote_servers):
    merge.connect(i, remote_operators[i], 0)

fc = merge.get_output(0, dpf.types.fields_container)
print(fc)
print(fc[0].min().data)
print(fc[0].max().data)
