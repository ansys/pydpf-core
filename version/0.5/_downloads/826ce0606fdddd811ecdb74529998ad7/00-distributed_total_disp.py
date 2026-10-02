"""
.. _ref_distributed_total_disp:

Post processing of displacement on distributed processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To help understand this example the following diagram is provided. It shows
the operator chain used to compute the final result.

.. image:: 00-operator-dep.svg
   :align: center
   :width: 400
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
# we will consequently require 2 remote processes.
# To make this example easier, we will start local servers here,
# but we could get connected to any existing servers on the network.

global_server = dpf.start_local_server(
    as_global=True, config=dpf.AvailableServerConfigs.InProcessServer
)

remote_servers = [
    dpf.start_local_server(
        as_global=False, config=dpf.AvailableServerConfigs.GrpcServer),
    dpf.start_local_server(
        as_global=False, config=dpf.AvailableServerConfigs.GrpcServer),
]
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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
