"""
.. _ref_distributed_total_disp:

Postprocessing of displacement on distributed processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This diagram helps you to understand this example. It shows
the operator chain that is used to compute the final result.

.. graphviz::

    digraph foo {
        graph [pad="0", nodesep="0.3", ranksep="0.3"]
        node [shape=box, style=filled, fillcolor="#ffcc00", margin="0"];
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
# Import the ``dpf-core`` module and its examples files.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Configure the servers.
# Make a list of IP addresses and port numbers that DPF servers start and
# listen on. Operator instances are created on each of these servers so that
# each can address a different result file.
#
# This example postprocesses an analysis distributed in two files.
# Consequently, it require two remote processes.
#
# To make it easier, this example starts local servers. However, you can
# connect to any existing servers on your network.

global_server = dpf.start_local_server(
    as_global=True, config=dpf.AvailableServerConfigs.InProcessServer
)

remote_servers = [
    dpf.start_local_server(as_global=False, config=dpf.AvailableServerConfigs.GrpcServer),
    dpf.start_local_server(as_global=False, config=dpf.AvailableServerConfigs.GrpcServer),
]
ips = [remote_server.ip for remote_server in remote_servers]
ports = [remote_server.port for remote_server in remote_servers]

###############################################################################
# Print the IP addresses and ports.
print("ips:", ips)
print("ports:", ports)

###############################################################################
# Send files to the temporary directory if they are not in shared memory.
files = examples.download_distributed_files()
server_file_paths = [
    dpf.upload_file_in_tmp_folder(files[0], server=remote_servers[0]),
    dpf.upload_file_in_tmp_folder(files[1], server=remote_servers[1]),
]

###############################################################################
# Create operators on each server
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# On each server, create two operators, one for displacement computations
# and one for norm computations. Define their data sources:

# - The displacement operator receives data from the data file in its respective
#   server.
# - The norm operator, which is chained to the displacement operator, receives
#   input from the output of the displacement operator.
#
remote_operators = []
for i, server in enumerate(remote_servers):
    displacement = ops.result.displacement(server=server)
    norm = ops.math.norm_fc(displacement, server=server)
    remote_operators.append(norm)
    ds = dpf.DataSources(server_file_paths[i], server=server)
    displacement.inputs.data_sources(ds)

###############################################################################
# Create an operator to merge results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create the ``merge_fields_containers`` operator to merge the results.

merge = ops.utility.merge_fields_containers()

###############################################################################
# Connect the operators together and get the output
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for i, server in enumerate(remote_servers):
    merge.connect(i, remote_operators[i], 0)

fc = merge.get_output(0, dpf.types.fields_container)
print(fc)
print(fc[0].min().data)
print(fc[0].max().data)
