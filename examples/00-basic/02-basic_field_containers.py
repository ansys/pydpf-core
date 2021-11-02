"""
.. _ref_basic_field_example:

Field and Field Containers Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Overview of the usage of fields and field containers in DPF.

The field is the main simulation data container. In numerical
simulations, results data are defined by values associated to entities
(scoping), and these entities are a subset of a model (support).

In DPF, field data is always associated to its scoping and support,
making the field a self-describing piece of data. A field is also
defined by its dimensionnality, unit, location, etc.  A field can for
example, describe a displacement vector or norm, stresses and strains
tensors, stresses and strains equivalent, or the minimum and maximum
over time of any result.  It can be defined on a complete model or
just on certain entities of the model based on its scoping. The data
is stored as a vector of double values and each elementary entity has
a number of components.  For example, displacement will have 3
components, a symmetrical stress matrix will have 6.

A fields container is simply a collection of fields that can be
indexed just like a Python list.  Operators applied to a fields
container will have each individual field operated on.  Fields
containers are output from operators.

"""
import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators

###############################################################################
# First, create a model object to establish a connection with an
# example result file and then extract
model = dpf.Model(examples.static_rst)
print(model)

###############################################################################
# Create the displacement operator directly from the ``results``
# property and extract the displacement fields container.
disp_op = model.results.displacement()
fields = disp_op.outputs.fields_container()
print(fields)

###############################################################################
# A field can be extracted from a fields container by simply indexing
# the requested field
field = fields[0]
print(field)

###############################################################################
# Extracting data from a field
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# You can extract all the data from a given field using the ``data``
# property.  This returns a ``numpy`` array.

print(field.data)

###############################################################################
# While it might seem preferable to work entirely within ``numpy``,
# realize that DPF runs outside of Python and potentially even on a
# remote machine.  Therefore, the transfer of unnecessary data between
# the DPF instance and the Python client will lead to inefficient
# operations on large models.  Instead, use DPF operators to assemble
# the necessary data before recalling the data from DPF.
#
# For example, if you want the maximum displacement for a given
# result, use the min/max operator:
#
min_max_op = dpf.operators.min_max.min_max(field)
print(min_max_op.outputs.field_max().data)

# Out of conveience, you can simply take the max of the field with:
print(field.max().data)

# Which all yield an identical result as:
print(np.max(field.data, axis=0))

###############################################################################
# Note that the numpy array does not retain any information about the
# field it describes.  Using the DPF max operator of the field does
# retain this information.
max_field = field.max()
print(max_field)