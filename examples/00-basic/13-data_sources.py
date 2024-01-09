"""
.. _ref_data_sources:

How-to: define DataSources
~~~~~~~~~~~~~~~~~~~~~~~~~~

DPF uses the DataSources object to keep track of files to read data from.
It is given as input to the ``dpf.Model`` constructor or to operators.

This example shows the different ways to explain to DPF how to treat the different files available.
It gives several use-cases from basic to complex, with their associated best practices.

"""

# Import necessary modules
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Concepts
# ~~~~~~~~
# A few concepts are required to understand the different use-cases.
###############################################################################
# - file ``key``:
#       DPF associates a ``key`` to each file to know which reader to use and format to expect.
#       The default is the file's extension, such as ``rst`` for ``file.rst``
#       or ``cas`` for ``file.cas``.
#       DPF also automatically associates a key to some common solver output files despite them
#       having no file extension, such as ``d3plot`` and ``binout`` files for LS-DYNA.
#       As shown in the examples, you can force DPF to associate a key to a file when required.
###############################################################################
# - result files vs secondary files:
#       Files given to DPF are considered either as result files containing simulation data,
#       for which DPF must select the right source operator (reader), or as accessory files such as
#       files defining units, materials, modes... etc, for which other treatments are necessary.
#       The logic defining which files are result files and which files are secondary is defined
#       for each plugin.
###############################################################################
# - ``result key``:
#       The result key is the file key (extension) DPF will treat as result files.
#       Files with other keys are treated as accessory (secondary) files.
#       It defaults to the key of the first file declared as result file.
#       For multi-solver results, it is possible to declare additional result keys.
###############################################################################
# - ``namespace``:
#       DPF uses the namespace associated to each result key to know which plugin to use
#       readers from.
#       This usually does not require user intervention.
###############################################################################
# - ``domain``:
#       For multi-domain distributed results, the spatial domain ID associated to a result file.
###############################################################################
# - ``upstream`` data source:
#       Each result key can have an associated ``upstream`` DataSources object.
#       DPF uses these upstream DataSources to gather additional data enabling proper treatment of
#       the result data, such as for results obtained using CMS superelements, where DPF
#       requires knowledge of the CMS analysis result files.

###############################################################################
# Single result file
# ~~~~~~~~~~~~~~~~~~
single_result_file_path = examples.find_simple_bar()
###############################################################################
# The most simple case is when data is held in a single output file from a solver.
ds = dpf.DataSources(result_path=single_result_file_path)
print(ds)
###############################################################################
# In this case you can also give the file path to the Model constructor directly.
model = dpf.Model(data_sources=single_result_file_path)
print(model.metadata.data_sources)
###############################################################################
# Force another key than the default for the result file.
ds = dpf.DataSources()
ds.set_result_file_path(filepath=single_result_file_path, key="test")
ds.set_result_file_path(filepath=single_result_file_path, key="test2")
print(ds)
###############################################################################
# Print the current result key for the DataSources
print(ds.result_key)
###############################################################################
# Get the list of current result files in the DataSources
print(ds.result_files)

###############################################################################
# Secondary files
# ~~~~~~~~~~~~~~~
secondary_file_path = examples.download_binout_matsum()
# Declare secondary files such as units or materials files.
ds = dpf.DataSources(result_path=single_result_file_path)
ds.add_file_path(filepath=secondary_file_path)

###############################################################################
# Multi-domain distributed files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
distributed_files = examples.download_distributed_files()
print(distributed_files)

###############################################################################
# Upstream result files (CMS)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

###############################################################################
# Multi-solver results
# ~~~~~~~~~~~~~~~~~~~~
#
ds = dpf.DataSources()
ds.add_file_path_for_specified_result()
