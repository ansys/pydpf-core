"""
.. _ref_basic_operators_example:

Operators Overview
~~~~~~~~~~~~~~~~~~
Overview of the usage of operators in DPF.

Operators are primary method for interacting with and extracting
results.  Within DPF-Core, these operators are directly exposed with
the `Operators` class as well as wrapped within several other
convenience classes.

This example demonstrates how to work directly with operators and
compares it to wrapped approach.

For a full listing of all available operators, please see
:ref:`ref_dpf_operators_reference`.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# First, create a model object to establish a connection with an
# example result file.
model = dpf.Model(examples.static_rst)
print(model)

###############################################################################
# Next, create a raw displacement operator ``"U"``.  Each operator
# contains ``input`` and ``output`` pins that can be connected to
# various sources, to include other operators.  This allows operators
# to be "chained" to allow for highly efficient operations.
#
# Here, we print out the available inputs and outputs of the
# displacement operator.
disp_op = dpf.Operator('U')
print(disp_op.inputs)
print(disp_op.outputs)


###############################################################################
# Compute the Maximum Normalized Displacement
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Here, connect the input of the operator to the data sources
# contained within the ``model`` object and then the maximum of the
# norm of the operator to demonstrate how to chain various operators.

# connect to the data sources of the model
disp_op.inputs.data_sources.connect(model.metadata.data_sources)

# Create a field container norm operator and connect it to the
# displacement operator to chain the operators.
norm_op = dpf.Operator('norm_fc')
norm_op.inputs.connect(disp_op.outputs)

# create a field container min/max operator and connect it to the
# output of the norm operator
mm_op = dpf.Operator('min_max_fc')
mm_op.inputs.connect(norm_op.outputs)

# Finally, get the value of the maximum displacement
field_max = mm_op.outputs.field_max()
print(field_max)
print(field_max.data)

###############################################################################
# Wrapped Operators
# ~~~~~~~~~~~~~~~~~
# The ``model.results`` property contains all the wrapped operators
# available for a given result.  This is provided out of convenience
# as not all operators may be available for a given result and it is
# much easier to reference available operators by first running:
print(model.results)


###############################################################################
# Create the displacement operator directly from the ``results`` property
disp_op = model.results.displacement()

# Out of convenience, the operators module contains availabale operators
# Those operators can be created in chain to create a workflow in one line
from ansys.dpf.core import operators
mm_op = operators.min_max.min_max_fc(operators.math.norm_fc(disp_op))

# Finally, get the value of the maximum displacement.
field_max = mm_op.outputs.field_max()
print(field_max)
print(field_max.data)

###############################################################################
# Plot the displacement
print(model.metadata.meshed_region.plot(disp_op.outputs.fields_container()))

###############################################################################
# Scripting operators syntax
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# DPF is also providing a scripting syntax where knowing 
# the operator "string name" is not mandatory. 
# Here is a similar script as above using this syntax. 

###############################################################################
# Instead of using a model class instance, let's directly use a 
# datasources object. The DataSources constructor input is a path. 
ds = dpf.DataSources(examples.static_rst)
print(examples.static_rst)

###############################################################################
# Let's instantiate the operators and connect them together. 

disp_op = dpf.operators.result.displacement()
disp_op.inputs.data_sources.connect(ds)
norm_op = dpf.operators.math.norm_fc()
norm_op.inputs.connect(disp_op.outputs)
mm_op = dpf.operators.min_max.min_max_fc()
mm_op.inputs.connect(norm_op.outputs)

###############################################################################
# Let's get the output and print the result data. 

field_max = mm_op.outputs.field_max()
print(field_max.data)