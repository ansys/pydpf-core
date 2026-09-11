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
.. _ref_tutorials_server_context:

Server Context
==============

Control licensing behavior by configuring the |ServerContext| on a DPF server.

The |ServerContext| drives whether DPF capabilities requiring a license checkout
are allowed. Two licensing context types are available:

- **Premium**: The default context, which allows DPF to perform license checkouts
  and makes all licensed operators available.
- **Entry**: A restricted context that performs no license checkouts.
  Licensed operators are unavailable in this context.

This tutorial shows how to:

- Start a server with the **Entry** context.
- Upgrade a server from **Entry** to **Premium** at runtime.
- Change the default context for all new servers.

.. note::

    The **Entry** server context is available starting with DPF server version 6.0
    (Ansys 2023 R2). With earlier server versions, **Premium** is the only available
    context.
"""

###############################################################################
# Import Required Modules
# -----------------------
#
# Import the required modules.

from ansys.dpf import core as dpf
from ansys.dpf.core import server_context

###############################################################################
# Start a Server with Entry Context
# ----------------------------------
#
# Start a local insecure gRPC server in **Entry** context using
# :class:`AvailableServerContexts <ansys.dpf.core.server_context.AvailableServerContexts>`.
# Passing ``as_global=False`` keeps the global server unchanged so subsequent
# cells are not affected.

# Start a local insecure gRPC server with the Entry licensing context
entry_server = dpf.start_local_server(
    context=dpf.AvailableServerContexts.entry,
    as_global=False,
    config=dpf.AvailableServerConfigs.InsecureGrpcServer,
)

# Display the server context — shows LicensingContextType.entry
print(entry_server.context)

###############################################################################
# Upgrade the Server Context to Premium
# --------------------------------------
#
# Once a server is running in **Entry** context, it can be upgraded to
# **Premium** using
# :meth:`apply_context <ansys.dpf.core.server_types.BaseServer.apply_context>`.
#
# .. note::
#
#     Downgrading a server from **Premium** back to **Entry** is not supported.

# Apply the Premium context to the Entry server
entry_server.apply_context(dpf.AvailableServerContexts.premium)

# Display the server context — now shows LicensingContextType.premium
print(entry_server.context)

# Shut down the server to free resources
entry_server.shutdown()

###############################################################################
# Change the Default Server Context
# ----------------------------------
#
# The default context for all new servers is **Premium**. You can change it at
# runtime using
# :func:`set_default_server_context <ansys.dpf.core.server_context.set_default_server_context>`.
# It can also be set before starting your Python process via the
# ``ANSYS_DPF_SERVER_CONTEXT`` environment variable
# (accepted values: ``ENTRY``, ``PREMIUM``).
#
# .. warning::
#
#     Because an ``InProcess`` server links DPF binaries to the current Python
#     process, a second ``InProcess`` server cannot be started. If your local
#     ``InProcess`` server is already **Premium**, it cannot be set back to
#     **Entry**. Set the desired context at the very start of your script,
#     before the first server is created.

# Set Entry as the default context for new servers
dpf.set_default_server_context(dpf.AvailableServerContexts.entry)

# Display the new global default context
print(server_context.SERVER_CONTEXT)

# Restore Premium as the default context
dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

# Display the restored default context
print(server_context.SERVER_CONTEXT)
