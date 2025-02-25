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

# noqa: D400
"""
.. _ref_server_types_example:

Communicate in process or via gRPC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting with Ansys 2022 R2, PyDPF can communicate either via In Process or via gRPC
with DPF C++ core server (``Ans.Dpf.Grpc.exe``). To choose which type of
:class:`ansys.dpf.core.server_types.BaseServer` (object defining the type of communication
and the server instance to communicate with) to use, a
:class:`ansys.dpf.core.server_factory.ServerConfig` class should be used.
Until Ansys 2022R1, only gRPC communication using python module ``ansys.grpc.dpf`` is supported
(now called :class:`ansys.dpf.core.server_types.LegacyGrpcServer`), starting with Ansys 2022 R2,
three types of servers are supported:

- :class:`ansys.dpf.core.server_types.InProcessServer` loading DPF in process. Cannot run on Docker.

- :class:`ansys.dpf.core.server_types.GrpcServer` using gRPC communication through the DPF
  gRPC CLayer ``Ans.Dpf.GrpcClient``.

- :class:`ansys.dpf.core.server_types.LegacyGrpcServer` using gRPC communication through the
  Python module ``ansys.grpc.dpf``.

To change the default type of server's configuration used by DPF change:

- the global variable ``SERVER_CONFIGURATION`` at the beginning of the python script.
- the environment variable ``DPF_SERVER_TYPE`` before running the python executable, see
  :class:`ansys.dpf.core.server_factory.ServerConfig` for more information.

"""

import os

from ansys.dpf import core as dpf

###############################################################################
# Start servers with custom server configuration
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

in_process_config = dpf.AvailableServerConfigs.InProcessServer
grpc_config = dpf.AvailableServerConfigs.GrpcServer
legacy_grpc_config = dpf.AvailableServerConfigs.LegacyGrpcServer

if "DPF_DOCKER" not in os.environ.keys():
    in_process_server = dpf.start_local_server(config=in_process_config)
grpc_server = dpf.start_local_server(config=grpc_config)
legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config)

###############################################################################
# Equivalent to:

in_process_config = dpf.ServerConfig(protocol=None, legacy=False)
grpc_config = dpf.ServerConfig(
    protocol=dpf.server_factory.CommunicationProtocols.gRPC, legacy=False
)
legacy_grpc_config = dpf.ServerConfig(
    protocol=dpf.server_factory.CommunicationProtocols.gRPC, legacy=True
)

if "DPF_DOCKER" not in os.environ.keys():
    in_process_server = dpf.start_local_server(config=in_process_config, as_global=False)
grpc_server = dpf.start_local_server(config=grpc_config, as_global=False)
legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config, as_global=False)

###############################################################################
# Create data on different servers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if "DPF_DOCKER" not in os.environ.keys():
    in_process_field = dpf.fields_factory.create_scalar_field(2, server=in_process_server)
    in_process_field.append([1.0], 1)
    in_process_field.append([2.0], 2)
grpc_field = dpf.fields_factory.create_scalar_field(2, server=grpc_server)
grpc_field.append([1.0], 1)
grpc_field.append([2.0], 2)
legacy_grpc_field = dpf.fields_factory.create_scalar_field(2, server=legacy_grpc_server)
legacy_grpc_field.append([1.0], 1)
legacy_grpc_field.append([2.0], 2)

if "DPF_DOCKER" not in os.environ.keys():
    print(in_process_field, type(in_process_field._server), in_process_field._server)
print(grpc_field, type(grpc_field._server), grpc_field._server)
print(legacy_grpc_field, type(legacy_grpc_field._server), legacy_grpc_field._server)

###############################################################################
# Choose default configuration
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Once a default configuration is chosen, a server of the chosen type is
# automatically started when a DPF object is created:

initial_config = dpf.SERVER_CONFIGURATION

dpf.SERVER_CONFIGURATION = dpf.AvailableServerConfigs.GrpcServer
grpc_field = dpf.fields_factory.create_scalar_field(2)
grpc_field.append([1.0], 1)
grpc_field.append([2.0], 2)
print(grpc_field, type(grpc_field._server), grpc_field._server)

# Go back to default config:
dpf.SERVER_CONFIGURATION = initial_config
