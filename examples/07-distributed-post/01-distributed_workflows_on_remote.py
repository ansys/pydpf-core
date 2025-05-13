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
.. _ref_distributed_workflows_on_remote:

Create a custom workflow on distributed processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to read and postprocess distributed files on
distributed processes. After remote postprocessing, results are merged
on the local process. This example creates different operator
sequences directly on different servers. These operators are then
connected together so that you don't have to care that they are on
remote processes.

.. graphviz::

    digraph foo {
        graph [pad="0", nodesep="0.3", ranksep="0.3"]
        node [shape=box, style=filled, fillcolor="#ffcc00", margin="0"];
        rankdir=LR;
        splines=line;

        subgraph cluster_1 {
            ds01 [label="data_src", shape=box, style=filled, fillcolor=cadetblue2];

            ds01 -> stress1 [style=dashed];

            label="Server 1";
            style=filled;
            fillcolor=lightgrey;
        }

        subgraph cluster_2 {
            ds02 [label="data_src", shape=box, style=filled, fillcolor=cadetblue2];

            ds02 -> stress2 [style=dashed];
            stress2 -> mul;

            label="Server 2";
            style=filled;
            fillcolor=lightgrey;
        }

        stress1 -> "merge";
        mul -> "merge";
    }

"""
###############################################################################
# Import the ``dpf-core`` module and its examples files.

import os

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Configure the servers.
# To make it easier, this example starts local servers. However, you can
# connect to any existing servers on your network.

config = dpf.AvailableServerConfigs.InProcessServer
if "DPF_DOCKER" in os.environ.keys():
    # If running DPF on Docker, you cannot start an InProcessServer
    config = dpf.AvailableServerConfigs.GrpcServer
global_server = dpf.start_local_server(as_global=True, config=config)

remote_servers = [
    dpf.start_local_server(as_global=False, config=dpf.AvailableServerConfigs.GrpcServer),
    dpf.start_local_server(as_global=False, config=dpf.AvailableServerConfigs.GrpcServer),
]

###############################################################################
# Send files to the temporary directory if they are not in shared memory.

files = examples.download_distributed_files(return_local_path=True)
server_file_paths = [
    dpf.upload_file_in_tmp_folder(files[0], server=remote_servers[0]),
    dpf.upload_file_in_tmp_folder(files[1], server=remote_servers[1]),
]

###############################################################################
# Create the first operator chain.

remote_operators = []

stress1 = ops.result.stress(server=remote_servers[0])
remote_operators.append(stress1)
ds = dpf.DataSources(server_file_paths[0], server=remote_servers[0])
stress1.inputs.data_sources(ds)

###############################################################################
# Create the second operator chain.

stress2 = ops.result.stress(server=remote_servers[1])
mul = stress2 * 2.0
remote_operators.append(mul)
ds = dpf.DataSources(server_file_paths[1], server=remote_servers[1])
stress2.inputs.data_sources(ds)

###############################################################################
# Create the local merge operator.

merge = ops.utility.merge_fields_containers()

###############################################################################
# Connect the operator chains together and get the output.

nodal = ops.averaging.to_nodal_fc(merge)

merge.connect(0, remote_operators[0], 0)
merge.connect(1, remote_operators[1], 0)

fc = nodal.get_output(0, dpf.types.fields_container)
print(fc[0])
fc[0].meshed_region.plot(fc[0])
