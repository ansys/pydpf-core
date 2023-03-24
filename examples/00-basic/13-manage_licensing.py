"""
.. _ref_manage_licensing:

Manage the DPF licensing logic via the server context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This examples shows how to manage the licensing logic of a DPF server using a `ServerContext`.

Preventing DPF from checking licenses out and blocking increments is possible
with the **Entry** context.

.. warning::
    As starting an ``InProcess`` server means linking the DPF binaries to your current python
    process, you cannot start a new ``InProcess`` server. Thus, if your local ``InProcess`` server
    is already **Premium**, you cannot set it back as **Entry**.
    ``InProcess`` being the default server type, the proper commands to work as **Entry** should be
    set right at the beginning of your script.

"""

# Import necessary modules
from ansys.dpf import core as dpf
from ansys.dpf.core.core import errors

#######################################################################################
# Start a server as Entry to prevent using licensed operators
server = dpf.start_local_server(context=dpf.AvailableServerContexts.entry)
# The context is shown as Entry
print(server.context)

# A server of type InProcess being linked to the current python process,
# if an InProcess server already exists as Premium, you cannot set it back as Entry.

#######################################################################################
# Create a dummy Field
field = dpf.Field()
field.append([0.0, 0.0, 0.0], 1)
print(field)

# Instantiate an Entry (not licensed) DPF operator
op_entry = dpf.operators.math.add_constant(field=field, ponderation=2.0)

# Instantiate a Premium (licensed) DPF operator
op_premium = dpf.operators.filter.field_high_pass(field=field, threshold=0.0)

#######################################################################################
# Operators with the Entry context

# Using unlicensed DPF operators is possible
out = op_entry.eval()
print(out)

# While using license ones is blocked, raising an error
try:
    op_premium.eval()
except errors.DPFServerException as e:
    print(e)

#######################################################################################
# Operators with the Premium context

# Set the default server context as Premium
dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
# or apply the Premium context to the current server
server.apply_context(dpf.AvailableServerContexts.premium)

# Licensed operators can now check a license out and run
out = op_premium.eval()
print(out)

###############################################################################################
# When Premium, using a LicenseContextManaged allows to control your interaction with a license

# Use the LicenseContextManager to block a specific increment for a limited duration
with dpf.LicenseContextManager(increment_name="preppost", license_timeout_in_seconds=1.0) as lic:
    # Instantiate the licensed operator
    out = op_premium.eval()
    print(out)
