"""
.. _ref_distributed_workflows_on_remote:

Create custom workflow on distributed processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how distributed files can be read and post processed
on distributed processes. After remote post processing,
results are merged on the local process. In this example, different operator
sequences are directly created on different servers. These operators are then
connected together without having to care that they are on remote processes.

.. image:: 01-operator-dep.svg
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
# ~~~~~~~~~~~~~~~~~~~~~
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

###############################################################################
# Here we show how we could send files in temporary directory if we were not
# in shared memory

files = examples.download_distributed_files()
server_file_paths = [dpf.upload_file_in_tmp_folder(files[0], server=remote_servers[0]),
                     dpf.upload_file_in_tmp_folder(files[1], server=remote_servers[1])]

###############################################################################
# First operator chain.

remote_operators = []

stress1 = ops.result.stress(server=remote_servers[0])
remote_operators.append(stress1)
ds = dpf.DataSources(server_file_paths[0], server=remote_servers[0])
stress1.inputs.data_sources(ds)

###############################################################################
# Second operator chain.

stress2 = ops.result.stress(server=remote_servers[1])
mul = stress2 * 2.0
remote_operators.append(mul)
ds = dpf.DataSources(server_file_paths[1], server=remote_servers[1])
stress2.inputs.data_sources(ds)

###############################################################################
# Local merge operator.

merge = ops.utility.merge_fields_containers()

###############################################################################
# Connect the operator chains together and get the output
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

nodal = ops.averaging.to_nodal_fc(merge)

merge.connect(0, remote_operators[0], 0)
merge.connect(1, remote_operators[1], 0)

fc = nodal.get_output(0, dpf.types.fields_container)
print(fc[0])
fc[0].meshed_region.plot(fc[0])
