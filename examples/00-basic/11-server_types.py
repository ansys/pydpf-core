"""
.. _ref_server_types_example:

Communicate In Process or via gRPC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Starting with Ansys 2022R2, pyDPF can communication either In Process or via gRPC
with DPF C++ core server (Ans.Dpf.Grpc.exe). To choose which type of
:class:`ansys.dpf.core.server_types.BaseServer` (object defining the type of communication
and the server instance to communicate with) to use, a
:class:`ansys.dpf.core.server_factory.ServerConfig` should be used.
Until Ansys 2022R1, only gRPC communication using python module ansys.grpc.dpf is supported
(now called :class:`ansys.dpf.core.server_types.LegacyGrpcServer`), starting with Ansys 2022R2,
3 types of servers are supported:

- :class:`ansys.dpf.core.server_types.InProcessServer` loading DPF in Process.

- :class:`ansys.dpf.core.server_types.GrpcServer` using gRPC communication through DPF
  gRPC CLayer Ans.Dpf.GrpcClient.

- :class:`ansys.dpf.core.server_types.LegacyGrpcServer` using gRPC communication through the python
  module ansys.grpc.dpf.

"""

from ansys.dpf import core as dpf

###############################################################################
# Start Servers with custom ServerConfig
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

in_process_config = dpf.AvailableServerConfigs.InProcessServer
grpc_config = dpf.AvailableServerConfigs.GrpcServer
legacy_grpc_config = dpf.AvailableServerConfigs.LegacyGrpcServer

in_process_server = dpf.start_local_server(config=in_process_config)
grpc_server = dpf.start_local_server(config=grpc_config)
legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config)

###############################################################################
# Equivalent to:

in_process_config = dpf.ServerConfig(
    protocol=None, legacy=False
)
grpc_config = dpf.ServerConfig(
    protocol=dpf.server_factory.CommunicationProtocols.gRPC, legacy=False
)
legacy_grpc_config = dpf.ServerConfig(
    protocol=dpf.server_factory.CommunicationProtocols.gRPC, legacy=True
)

in_process_server = dpf.start_local_server(config=in_process_config, as_global=False)
grpc_server = dpf.start_local_server(config=grpc_config, as_global=False)
legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config, as_global=False)

###############################################################################
# Create Data on different servers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

in_process_field = dpf.fields_factory.create_scalar_field(2, server=in_process_server)
in_process_field.append([1.], 1)
in_process_field.append([2.], 2)
grpc_field = dpf.fields_factory.create_scalar_field(2, server=grpc_server)
grpc_field.append([1.], 1)
grpc_field.append([2.], 2)
legacy_grpc_field = dpf.fields_factory.create_scalar_field(2, server=legacy_grpc_server)
legacy_grpc_field.append([1.], 1)
legacy_grpc_field.append([2.], 2)

print(in_process_field, type(in_process_field._server), in_process_field._server)
print(grpc_field, type(grpc_field._server), grpc_field._server)
print(legacy_grpc_field, type(legacy_grpc_field._server), legacy_grpc_field._server)

###############################################################################
# Choose default configuration
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Once a default configuration is chosen, a server of the chosen type is automatically started
# when a DPF object is created:

initial_config = dpf.SERVER_CONFIGURATION

dpf.SERVER_CONFIGURATION = dpf.AvailableServerConfigs.GrpcServer
grpc_field = dpf.fields_factory.create_scalar_field(2)
grpc_field.append([1.], 1)
grpc_field.append([2.], 2)
print(grpc_field, type(grpc_field._server), grpc_field._server)

# Go back to default config:
dpf.SERVER_CONFIGURATION = initial_config
