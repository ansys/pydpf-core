# noqa: D400
"""
.. _ref_basic_example:

Basic DPF-Core usage
~~~~~~~~~~~~~~~~~~~~

This example shows how to open a result file and do some
basic postprocessing.

If you have Ansys 2021 R1 or higher installed, starting DPF is quite easy
as DPF-Core takes care of launching all the services that
are required for postprocessing Ansys files.

"""

# First, import the DPF-Core module as ``dpf`` and import the included examples file.
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Next, open an example and print out the ``model`` object. The
# :class:`Model <ansys.dpf.core.model.Model>` class helps to organize access methods
# for the result by keeping track of the operators and data sources used by the result
# file.
#
# Printing the model displays:
#
# - Analysis type
# - Available results
# - Size of the mesh
# - Number of results
#
# Also, note that the first time you create a DPF object, Python
# automatically attempts to start the server in the background. If you
# want to connect to an existing server (either local or remote), use
# :func:`ansys.dpf.core.connect_to_server`.

model = dpf.Model(examples.find_simple_bar())
print(model)

###############################################################################
# Model metadata
# ~~~~~~~~~~~~~~
# Specific metadata can be extracted from the model by referencing the
# model's ``metadata`` property. For example, to print only the
# ``result_info``:

metadata = model.metadata
print(metadata.result_info)

###############################################################################
# Print the mesh region:

print(metadata.meshed_region)

###############################################################################
# Print the time or frequency of the results:

print(metadata.time_freq_support)

###############################################################################
# Extract displacement results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# All results of the model can be accessed through the ``results``
# property, which returns the :class:`ansys.dpf.core.results.Results`
# class. This class contains the DPF result operators available to a
# specific result file, which are listed when printing the object with
# ``print(results)``.
#
# Here, the ``'U'`` operator is connected with ``data_sources``, which
# takes place automatically when running ``results.displacement()``.
# By default, the ``'U'`` operator is connected to the first result set,
# which for this static result is the only result.
results = model.results
displacements = results.displacement()
fields = displacements.outputs.fields_container()

# Finally, extract the data of the displacement field:
disp = fields[0].data
disp

###############################################################################
model.metadata.meshed_region.plot(fields)
