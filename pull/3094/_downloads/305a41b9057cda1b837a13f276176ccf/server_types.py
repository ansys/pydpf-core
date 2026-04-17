# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

# _order: 1
"""
.. _user_guide_server_types:

Working with DPF server configurations
======================================

This tutorial demonstrates how to work with different DPF server types and configurations
to optimize your workflow based on your specific needs.

DPF is based on a client-server architecture where PyDPF-Core acts as the Python client
API communicating with a DPF Server. Understanding server types is essential for choosing
the right configuration for your use case, whether you need maximum performance on a local
machine, secure remote access with mTLS authentication, or distributed computation across a network.
"""
###############################################################################
# Understanding DPF server types
# --------------------------------
#
# There are three main server configurations available in PyDPF-Core:
#
# - :class:`InProcessServer <ansys.dpf.core.server_types.InProcessServer>`: Direct communication
#   within the same Python process (fastest, default since Ansys 2023 R1). Requires compatible
#   runtime dependencies between Python packages and DPF plugins.
# - :class:`GrpcServer <ansys.dpf.core.server_types.GrpcServer>`: Network communication using
#   gRPC protocol (enables remote and distributed computation). Process isolation prevents
#   dependency conflicts with DPF plugins.
# - :class:`LegacyGrpcServer <ansys.dpf.core.server_types.LegacyGrpcServer>`: Legacy gRPC
#   communication for Ansys 2022 R1 and earlier versions.
#
# The choice of server type impacts performance, memory usage, dependency management, and
# distributed computing capabilities.

###############################################################################
# Starting a local InProcess server
# ----------------------------------
#
# The default and most efficient way to use PyDPF-Core is with an
# :class:`InProcessServer <ansys.dpf.core.server_types.InProcessServer>`.
# This configuration runs the DPF server directly within your Python process, eliminating data
# transfer overhead and providing the fastest performance.
#
# .. note::
#
#     While :class:`InProcessServer <ansys.dpf.core.server_types.InProcessServer>` offers the best
#     performance, it requires that all runtime dependencies are compatible between your Python
#     environment and DPF plugins. If any Python dependency clashes with a DPF plugin dependency,
#     that plugin will not be loaded, resulting in lost capabilities.
#
#     :class:`GrpcServer <ansys.dpf.core.server_types.GrpcServer>` does not have this limitation
#     because process isolation ensures dependency isolation between the client and server.
#
# Import the necessary modules:

###############################################################################
# Import the ansys.dpf.core module as ``dpf``
from ansys.dpf import core as dpf

# Import the examples module
from ansys.dpf.core import examples

###############################################################################
# Start a local DPF server with the default InProcess configuration:

local_server = dpf.start_local_server()
print(local_server)

###############################################################################
# The server is now ready to be used for creating DPF objects.
#
# Using the local server
# -----------------------
#
# Once you have started a local :class:`InProcessServer <ansys.dpf.core.server_types.InProcessServer>`,
# you can pass it to any DPF object constructor to ensure operations run on that specific server.
#
# Create an :class:`Operator <ansys.dpf.core.operator.Operator>` on the local server:

###############################################################################
# Instantiate a displacement Operator on the local server
local_operator = dpf.operators.result.displacement(server=local_server)
print(local_operator)

###############################################################################
# Create a :class:`Model <ansys.dpf.core.model.Model>` on the local server:

# Define the result file path using an example file
result_file = examples.find_simple_bar()

# Instantiate a Model on the local server
local_model = dpf.Model(result_file, server=local_server)
print(local_model)

###############################################################################
# Starting a gRPC server
# ----------------------
#
# For distributed computation or remote access scenarios, use a
# :class:`GrpcServer <ansys.dpf.core.server_types.GrpcServer>`.
# This configuration enables network communication using the gRPC protocol, allowing you to
# connect from different machines or leverage distributed computing capabilities.
#
# .. warning::
#
#     Starting with Ansys 2026 R1 (DPF 2026.1.0) and PyDPF-Core 0.15.0, DPF Server gRPC
#     connections default to using authenticated mTLS (mutual TLS) transport for enhanced security.
#     This change also applies to service packs for Ansys 2025 R2 SP03 and SP04, 2025 R1 SP04,
#     and 2024 R2 SP05.
#
#     For remote connections, you must configure mTLS certificates on both client and server machines.
#     See :ref:`ref_dpf_server_secure_mode` for detailed information on certificate configuration.
#
# Use the :class:`AvailableServerConfigs <ansys.dpf.core.server_factory.AvailableServerConfigs>`
# class to specify the server configuration:

###############################################################################
# Get the GrpcServer configuration
grpc_server_config = dpf.AvailableServerConfigs.GrpcServer

# Start a local server with gRPC configuration
grpc_server = dpf.start_local_server(config=grpc_server_config)
print(grpc_server)

###############################################################################
# Retrieve the server connection information:

# Get the server IP and port
server_ip = grpc_server.ip
server_port = grpc_server.port
print(f"Server IP: {server_ip}")
print(f"Server Port: {server_port}")

###############################################################################
# Connecting to a remote gRPC server
# -----------------------------------
#
# Once a :class:`GrpcServer <ansys.dpf.core.server_types.GrpcServer>` is running, you can connect
# to it from another machine or process using the
# :func:`connect_to_server <ansys.dpf.core.server.connect_to_server>` function.
# This enables distributed computation where data processing occurs on a remote server.

###############################################################################
# Connect to the remote gRPC server
remote_server = dpf.connect_to_server(ip=server_ip, port=server_port, as_global=False)
print(remote_server)

###############################################################################
# Create DPF objects on the remote server:

# Instantiate an Operator on the remote server
remote_operator = dpf.operators.result.displacement(server=remote_server)
print(remote_operator)

###############################################################################
# Instantiate a Model on the remote server:

remote_model = dpf.Model(result_file, server=remote_server)
print(remote_model)

###############################################################################
# Through the network using gRPC, a DPF server enables distributed computation capabilities.
# For examples of distributed workflows, see the gallery of examples.
#
# Configuring mTLS certificates for secure gRPC connections
# ----------------------------------------------------------
#
# When connecting to a remote gRPC server (starting with DPF 2026 R1 and PyDPF-Core 0.15.0),
# you need to configure mTLS certificates for secure communication. This applies to both the
# server machine and the client machine.
#
# Set the certificate location using an environment variable
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# The location of mTLS certificates is specified using the ``ANSYS_GRPC_CERTIFICATES`` environment
# variable. This must be set on both the server machine and the client machine.
#
# On Windows (run in PowerShell or Command Prompt):

# os.environ['ANSYS_GRPC_CERTIFICATES'] = r'C:\path\to\certificates'

###############################################################################
# On Linux (run in terminal):

# export ANSYS_GRPC_CERTIFICATES=/path/to/certificates

###############################################################################
# For detailed information on generating mTLS certificates, see the
# `Generating certificates for mTLS <https://tools.docs.pyansys.com/version/stable/user_guide/secure_grpc.html#generating-certificates-for-mtls>`_
# documentation.
#
# Disable mTLS for insecure mode (not recommended)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# If you need to disable mTLS authentication and fall back to the previous insecure behavior,
# you can set the ``DPF_DEFAULT_GRPC_MODE`` environment variable to ``insecure`` on both
# client and server sides.
#
# .. warning::
#
#     Disabling mTLS removes authentication and encryption, making your connection vulnerable
#     to security threats. Only use insecure mode in trusted, isolated network environments.
#
# On Windows:

# os.environ['DPF_DEFAULT_GRPC_MODE'] = 'insecure'

###############################################################################
# On Linux:

# export DPF_DEFAULT_GRPC_MODE=insecure

###############################################################################
# Comparing server configurations
# --------------------------------
#
# You can explicitly choose different server configurations using the
# :class:`AvailableServerConfigs <ansys.dpf.core.server_factory.AvailableServerConfigs>` class.
# This is useful when you need to test performance or compatibility with different server types.

###############################################################################
# Get InProcessServer configuration and start an InProcess server
in_process_config = dpf.AvailableServerConfigs.InProcessServer
in_process_server = dpf.start_local_server(config=in_process_config, as_global=False)
print(f"InProcess server: {in_process_server}")

###############################################################################
# Get GrpcServer configuration and start a gRPC server
grpc_config = dpf.AvailableServerConfigs.GrpcServer
grpc_server_2 = dpf.start_local_server(config=grpc_config, as_global=False)
print(f"gRPC server: {grpc_server_2}")

###############################################################################
# Get LegacyGrpcServer configuration (for compatibility with older versions)
legacy_grpc_config = dpf.AvailableServerConfigs.LegacyGrpcServer
legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config, as_global=False)
print(f"Legacy gRPC server: {legacy_grpc_server}")

###############################################################################
# Key takeaways
# -------------
#
# The choice of DPF server configuration depends on your specific requirements:
#
# - Use :class:`InProcessServer <ansys.dpf.core.server_types.InProcessServer>` for local computations
#   requiring maximum performance and minimal memory overhead (default since Ansys 2023 R1).
#
#   - Provides the fastest performance by eliminating data transfer between client and server.
#   - **Limitation**: Requires compatible runtime dependencies between Python packages and DPF plugins.
#     Incompatibilities between dependencies can prevent plugins from loading.
#   - Best suited for environments with controlled dependencies and standard DPF plugins.
#
# - Use :class:`GrpcServer <ansys.dpf.core.server_types.GrpcServer>` when you need distributed
#   computation, remote access, or when running DPF on a different machine (available since Ansys 2022 R2).
#
#   - Process isolation ensures dependency isolation, avoiding clashes between Python environment and plugins.
#   - Starting with DPF 2026 R1, gRPC connections use mTLS authentication by default for enhanced security.
#   - Configure the ``ANSYS_GRPC_CERTIFICATES`` environment variable on both client and server for mTLS.
#   - For more information, see :ref:`ref_dpf_server_secure_mode`.
#
# - Use :class:`LegacyGrpcServer <ansys.dpf.core.server_types.LegacyGrpcServer>` only for compatibility
#   with Ansys 2022 R1 and earlier versions.
#
# All configurations use the same
# :func:`start_local_server <ansys.dpf.core.server.start_local_server>` function with different
# :class:`ServerConfig <ansys.dpf.core.server_factory.ServerConfig>` parameters, making it easy
# to switch between server types as your needs change.
