# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
.. _ref_distributed_stress_averaging:

Average Stress in distributed Workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how stress can be read from distributed files and
averaged from elemental nodal to nodal in parallel with a distributed workflow.
After remote post-processing, results are merged on the local process.

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
# started. Workflow instances will be created on each of these servers to
# address each a different result file.
# In this example, we will post process an analysis distributed in 2 files,
# we will consequently require 2 remote processes.
# To make this example easier, we will start local servers here,
# but we could get connected to any existing servers on the network.

files = examples.download_distributed_files()

config = dpf.ServerConfig(protocol=dpf.server.CommunicationProtocols.gRPC)
remote_servers = [dpf.start_local_server(as_global=False, config=config) for file in files]
ips = [remote_server.ip for remote_server in remote_servers]
ports = [remote_server.port for remote_server in remote_servers]

###############################################################################
# Print the ips and ports
print("ips:", ips)
print("ports:", ports)


###############################################################################
# Distributed Workflow
# ~~~~~~~~~~~~~~~~~~~~

# %%
# .. graphviz::
#
#    digraph foo {
#        graph [pad="0", nodesep="0.3", ranksep="0.3"]
#        node [shape=box, style=filled, fillcolor="#ffcc00", margin="0"];
#        rankdir=LR;
#        splines=line;
#
#        stress01 [label="stress"];
#        stress02 [label="stress"];
#        average01 [label="elemental_nodal_to_nodal_fc"];
#        average02 [label="elemental_nodal_to_nodal_fc"];
#
#        subgraph cluster_1 {
#            ds01 [label="data_src", shape=box, style=filled, fillcolor=cadetblue2];
#            no_extend_to_mid_nodes01 [label="no_extend_to_mid_nodes",
#                                      shape=box, style=filled, fillcolor=cadetblue2];
#
#            ds01 -> stress01 [style=dashed];
#            no_extend_to_mid_nodes01 -> stress01 [style=dashed];
#            stress01 -> average01;
#
#            label="Server 2";
#            style=filled;
#            fillcolor=lightgrey;
#        }
#
#        subgraph cluster_2 {
#            ds02 [label="data_src", shape=box, style=filled, fillcolor=cadetblue2];
#            no_extend_to_mid_nodes02 [label="no_extend_to_mid_nodes",
#                                      shape=box, style=filled, fillcolor=cadetblue2];
#
#            ds02 -> stress02 [style=dashed];
#            no_extend_to_mid_nodes02 -> stress02 [style=dashed];
#            stress02 -> average02;
#
#            label="Server 1";
#            style=filled;
#            fillcolor=lightgrey;
#        }
#        merge_weighted_fields_containers [label="merge_weighted_fields_containers"];
#        average01 -> merge_weighted_fields_containers;
#        average02 -> merge_weighted_fields_containers;
#        merge_weighted_fields_containers -> extend_to_mid_nodes;
#
#    }

###############################################################################
# Create a local workflow able to merge the results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
config = ops.utility.merge_weighted_fields_containers.default_config()
config.set_read_inputs_in_parallel_option(True)
merge = ops.utility.merge_weighted_fields_containers(config=config)
extend_to_mid_nodes = ops.averaging.extend_to_mid_nodes_fc(merge)

###############################################################################
# Send workflows on servers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Here we create new instances on the server by copies of the template workflow
# We also connect the data sources to those workflows
remote_workflows = []
for i, server in enumerate(remote_servers):
    ds = dpf.DataSources(files[i], server=server)
    stress = ops.result.stress(server=server)
    stress.inputs.connect(ds)
    average = ops.averaging.elemental_nodal_to_nodal_fc(stress)
    average.inputs.extend_to_mid_nodes(False)

    merge.connect(0 + i, average.outputs.fields_container)
    merge.connect(1000 + i, average, 1)

fc = extend_to_mid_nodes.outputs.fields_container()
fc[0].plot()
print(fc)
print(fc[0].min().data)
print(fc[0].max().data)

###############################################################################
# Compare with non distributed Workflow
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create DataSources with Domain id (one domain by distributed file).

ds = dpf.DataSources()
ds.set_domain_result_file_path(files[0], 0)
ds.set_domain_result_file_path(files[1], 1)

model = dpf.Model(ds)
stress = model.results.stress()
fc_single_process = ops.averaging.to_nodal_fc(stress).eval()

fc_single_process[0].plot()
print(fc_single_process[0].min().data)
print(fc_single_process[0].max().data)
