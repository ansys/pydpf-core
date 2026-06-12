"""
.. _ref_distributed_msup:

Distributed modal superposition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how distributed files can be read and expanded
on distributed processes. The modal basis (2 distributed files) is read
on 2 remote servers and the modal response reading and the expansion is
done on a third server.

To help understand this example the following diagram is provided. It shows
the operator chain used to compute the final result.

.. image:: 02-operator-dep.svg
   :align: center
   :width: 800
"""

###############################################################################
# Import dpf module and its examples files.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Configure the servers
# ~~~~~~~~~~~~~~~~~~~~~
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
# Print the ips and ports.
print("ips:", ips)
print("ports:", ports)

###############################################################################
# Choose the file path.

base_path = examples.distributed_msup_folder
files = [base_path + r'/file0.mode', base_path + r'/file1.mode']
files_aux = [base_path + r'/file0.rst', base_path + r'/file1.rst']

###############################################################################
# Create the operators on the servers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# On each server we create two new operators, one for 'displacement' computations
# and a 'mesh_provider' operator and then define their data sources. The displacement
# and mesh_provider operators receive data from their respective data files on each server.
remote_displacement_operators = []
remote_mesh_operators = []
for i, server in enumerate(remote_servers):
    displacement = ops.result.displacement(server=server)
    mesh = ops.mesh.mesh_provider(server=server)
    remote_displacement_operators.append(displacement)
    remote_mesh_operators.append(mesh)
    ds = dpf.DataSources(files[i], server=server)
    ds.add_file_path(files_aux[i])
    displacement.inputs.data_sources(ds)
    mesh.inputs.data_sources(ds)

###############################################################################
# Create a local operators chain for expansion
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In the following series of operators we merge the modal basis, the meshes, read
# the modal response and expand the modal response with the modal basis.

merge_fields = ops.utility.merge_fields_containers()
merge_mesh = ops.utility.merge_meshes()

ds = dpf.DataSources(base_path + r'/file_load_1.rfrq')
response = ops.result.displacement(data_sources=ds)
response.inputs.mesh(merge_mesh.outputs.merges_mesh)

expansion = ops.math.modal_superposition(
    solution_in_modal_space=response,
    modal_basis=merge_fields
)
component = ops.logic.component_selector_fc(expansion, 1)

###############################################################################
# Connect the operator chains together and get the output
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i, server in enumerate(remote_servers):
    merge_fields.connect(i, remote_displacement_operators[i], 0)
    merge_mesh.connect(i, remote_mesh_operators[i], 0)

fc = component.get_output(0, dpf.types.fields_container)
merged_mesh = merge_mesh.get_output(0, dpf.types.meshed_region)

merged_mesh.plot(fc.get_field_by_time_complex_ids(1, 0))
merged_mesh.plot(fc.get_field_by_time_complex_ids(10, 0))
print(fc)
