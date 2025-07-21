"""
.. _ref_basic_operators_example:

Operators overview
~~~~~~~~~~~~~~~~~~

In DPF, operators provide the primary method for interacting with and extracting
results. Within DPF-Core, operators are directly exposed with
the ``Operators`` class as well as wrapped within several other
convenience classes.

For a list of all operators, see :ref:`ref_dpf_operators_reference`.

This example demonstrates how to work directly with operators and
compares this method to a wrapped approach.

Import the necessary modules:
"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create a model object to establish a connection with an
# example result file:
model = dpf.Model(examples.find_static_rst())
print(model)

###############################################################################
# Next, create a raw displacement operator ``"U"``.  Each operator
# contains ``input`` and ``output`` pins that can be connected to
# various sources to include other operators. This allows operators
# to be "chained" to allow for highly efficient operations.
#
# To print out the available inputs and outputs of the
# displacement operator:
disp_op = dpf.Operator("U")
print(disp_op.inputs)
print(disp_op.outputs)

###############################################################################
# Compute the maximum normalized displacement
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This example demonstrate how to chain various operators. It connects the input
# of the operator to the data sources contained within the ``model`` object and
# then the maximum of the norm of the operator.

# Connect to the data sources of the model.
disp_op.inputs.data_sources.connect(model.metadata.data_sources)

# Create a field container norm operator and connect it to the
# displacement operator to chain the operators.
norm_op = dpf.Operator("norm_fc")
norm_op.inputs.connect(disp_op.outputs)

# Create a field container min/max operator and connect it to the
# output of the norm operator.
mm_op = dpf.Operator("min_max_fc")
mm_op.inputs.connect(norm_op.outputs)

# Finally, get the value of the maximum displacement.
field_max = mm_op.outputs.field_max()
print(field_max)
print(field_max.data)

###############################################################################
# Wrapped operators
# ~~~~~~~~~~~~~~~~~
# The ``model.results`` property contains all the wrapped operators
# available for a given result. This is provided out of convenience
# because all operators may not be available for a given result. Consequently,
# it is much easier to reference available operators by first running:
print(model.results)

###############################################################################
# Create the displacement operator directly from the ``results`` property:
disp_op = model.results.displacement()

# Out of convenience, the ``operators`` module contains available operators.
# These operators can be chained to create a workflow in one line.
from ansys.dpf.core import operators

mm_op = operators.min_max.min_max_fc(operators.math.norm_fc(disp_op))

# Finally, get the value of the maximum displacement.
field_max = mm_op.outputs.field_max()
print(field_max)
print(field_max.data)

###############################################################################
# Plot the displacement:
print(model.metadata.meshed_region.plot(disp_op.outputs.fields_container()))

###############################################################################
# Scripting operator syntax
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Because DPF provides a scripting syntax, knowing
# an operator's "string name" is not mandatory.
# While this example is similar to the above script, it uses the DPF
# scripting syntax.

###############################################################################
# Instead of using a ``model`` class instance, use a
# ``DdataSources`` object directly. The ``DataSources`` constructor input is a path.
ds = dpf.DataSources(examples.find_static_rst())
print(examples.find_static_rst())

###############################################################################
# Instantiate the operators and connect them:

disp_op = dpf.operators.result.displacement()
disp_op.inputs.data_sources.connect(ds)
norm_op = dpf.operators.math.norm_fc()
norm_op.inputs.connect(disp_op.outputs)
mm_op = dpf.operators.min_max.min_max_fc()
mm_op.inputs.connect(norm_op.outputs)

###############################################################################
# Get the output and print the result data:

field_max = mm_op.outputs.field_max()
print(field_max.data)
