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

# _order: 2
"""
.. _ref_tutorials_operator_license:

Operator License Requirements
==============================

Identify which DPF operators require a license checkout and which ones do not.

Each DPF operator exposes a
:attr:`specification <ansys.dpf.core.dpf_operator.Operator.specification>`
property that documents its inputs, outputs, and properties.
The ``properties`` dictionary of a |Specification| contains a ``license`` key
when the operator requires a product-specific license checkout at evaluation
time.

- **Operators without a** ``license`` **property**: no additional product
  license is checked out when they are evaluated. They work in both **Entry**
  and **Premium** server contexts.
- **Operators with a** ``license`` **property**: require DPF to perform a
  license checkout during evaluation. They are only available in the
  **Premium** server context. Evaluating them in **Entry** context raises an
  exception with a clear message.

This tutorial shows how to:

- Inspect the |Specification| of a single operator for licensing information.
- Enumerate all operators and separate them into licensed and unlicensed groups.
- Observe the licensing error raised when a licensed operator is evaluated in
  **Entry** context.
"""

###############################################################################
# Import Required Modules
# -----------------------
#
# Import the required modules.

from ansys.dpf import core as dpf
from ansys.dpf.core import operators as ops

###############################################################################
# Retrieve All Available Operator Names
# --------------------------------------
#
# Use :func:`available_operator_names <ansys.dpf.core.dpf_operator.available_operator_names>`
# to get the full list of operators registered on the server. This function
# requires a server version of 3.0 or later and is only available for
# InProcess servers.

# Get all operator names available on the global InProcess server
all_operator_names = dpf.available_operator_names()

print(f"Total operators available: {len(all_operator_names)}")

###############################################################################
# Inspect an Operator Specification
# ----------------------------------
#
# The |Specification| of an operator documents its properties in a dictionary.
# The presence or absence of the ``license`` key tells you whether evaluating
# the operator requires a product-specific license checkout.

# Inspect the Specification of the displacement result operator (no license required)
spec_displacement = ops.result.displacement().specification
print("Displacement operator properties:")
print(spec_displacement.properties)
print()

# Inspect the Specification of an operator that requires a license checkout
spec_licensed = ops.logic.ascending_sort().specification
print("ascending_sort operator properties:")
print(spec_licensed.properties)

###############################################################################
# Separate Operators into Licensed and Unlicensed Groups
# -------------------------------------------------------
#
# Iterate over all operator names and check for the ``license`` key in their
# specification properties. Each operator's specification is accessed via
# a :class:`dpf.Operator <ansys.dpf.core.dpf_operator.Operator>` instance.
# Operators that have this key require a product license checkout in **Premium**
# context; those without it do not.

licensed_operators = []
unlicensed_operators = []

for name in all_operator_names:
    try:
        spec = dpf.Operator(name).specification
        if "license" in spec.properties:
            licensed_operators.append(name)
        else:
            unlicensed_operators.append(name)
    except Exception:
        # Skip operators whose Specification cannot be retrieved
        pass

print(f"Operators requiring a license checkout:  {len(licensed_operators)}")
print(f"Operators requiring no license checkout: {len(unlicensed_operators)}")

###############################################################################
# Examine a Sample of Unlicensed Operators
# -----------------------------------------
#
# Most DPF operators do not require any product-specific license checkout.
# Below are a few representative examples filtered to those with
# ``exposure='public'`` and a human-readable ``user_name``.

# Collect public unlicensed operators that have a user_name
unlicensed_public = []
for name in unlicensed_operators:
    try:
        spec = dpf.Operator(name).specification
        props = spec.properties
        if props.get("exposure") == "public" and "user_name" in props:
            unlicensed_public.append((name, props["user_name"]))
    except Exception:
        pass

print(f"Public operators with no license requirement: {len(unlicensed_public)}")
print()
print("A few examples:")
for op_name, user_name in unlicensed_public[:8]:
    print(f"  {op_name:<40}  {user_name}")

###############################################################################
# Observe the Behavior in Entry Context
# --------------------------------------
#
# In **Entry** context, DPF performs no license checkouts. Evaluating a
# licensed operator in that context raises a
# :class:`DPFServerException <ansys.dpf.gate.errors.DPFServerException>`
# with a message that explicitly states the licensing context issue.

# Start a separate server in Entry context (as_global=False keeps it isolated)
entry_server = dpf.start_local_server(
    context=dpf.AvailableServerContexts.entry,
    as_global=False,
    config=dpf.AvailableServerConfigs.InsecureGrpcServer,
)

print(f"Entry server context: {entry_server.context}")
print()

# Instantiate a licensed operator on the Entry server — instantiation succeeds
licensed_op = dpf.Operator(name="ascending_sort", server=entry_server)
print("Operator instantiated successfully in Entry context.")

# Evaluate it — this triggers the license checkout and raises an exception
try:
    licensed_op.eval()
except Exception as licensing_error:
    print(f"Evaluation error (expected): {licensing_error}")

# Shut down the Entry server
entry_server.shutdown()
