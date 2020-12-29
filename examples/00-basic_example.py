"""
.. _ref_dpf_core:

Basic DPF-Core Usage
~~~~~~~~~~~~~~~~~~~~
This example shows how to open an example result file and do some
basic post-processing.

If you have ANSYS 2021R1 installed, getting running DPF is quite easy
as `ansys.dpf.core` takes care of launching all the services required
to start post-processing ANSYS files.

First, import the DPF-Core module as `dpf_core` and also import the
included examples file.


"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Next, open an example and then print out the ``model`` object.  The
# ``Model`` class helps to organize access methods for the result by
# keeping track of the operators and data sources used by the result
# file.
#
# Printing the model displays:
# - Analysis type
# - Available results
# - Size of the mesh
# - Number of results
#
# Also, note that the first time you create a DPF object, Python will
# automatically attempt to start the server in the background.  If you
# wish to connect to an existing server (either local or remote), use
# ``dpf.connect_to_server()``

model = dpf.Model(examples.simple_bar)
print(model)


###############################################################################
# Model Metadata
# ~~~~~~~~~~~~~~
# Specific metadata can be extracted from the model by referencing the
# ``metadata`` property of the model.  For example, just the
# result_info can be printed with:

metadata = model.metadata
print(metadata.result_info)


###############################################################################
# The mesh region can be printed with

print(metadata.meshed_region)


###############################################################################
# and the time or frequency of the results can be printed with:

print(metadata.time_freq_support)


###############################################################################
# Extracting Displacement Results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# All results of the model can be accessed through the ``results``
# property, which returns the ``Results`` class.  This class contains
# the DPF result operators available to a specific result file, which
# are listed when printing the object with ``print(results)``
#
# Here, we connect the ``'U'`` operator with the data_sources, which
# takes place automatically when running ``results.displacement()``.

results = model.results
displacements = results.displacement()
fields = displacements.outputs.fields_container()

# finally, extract the data of the displacement field
disp = fields[0].data
