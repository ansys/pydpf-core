"""
.. _ref_reduced_matrices_export:

Get reduced matrices and make export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to get reduced matrices and
export them to hdf5 and csv format.

"""

###############################################################################
# Import dpf module and its examples files, and create a temporary directory

import os
import tempfile

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

tmpdir = tempfile.mkdtemp()

###############################################################################
# Create the operator and connect dataSources

ds = dpf.DataSources(examples.download_sub_file())

matrices_provider = ops.result.cms_matrices_provider()
matrices_provider.inputs.data_sources.connect(ds)

###############################################################################
# Get result fields container that contains the reduced matrices

fields = matrices_provider.outputs.fields_container()

len(fields)

fields[0].data

###############################################################################
# Export the result fields container in hdf5 format

h5_op = ops.serialization.serialize_to_hdf5()
h5_op.inputs.data1.connect(matrices_provider.outputs)
h5_op.inputs.file_path.connect(os.path.join(tmpdir, "matrices.h5"))
h5_op.run()

###############################################################################
# Export the result fields container in csv format

csv_op = ops.serialization.field_to_csv()
csv_op.inputs.field_or_fields_container.connect(matrices_provider.outputs)
csv_op.inputs.file_path.connect(os.path.join(tmpdir, "matrices.csv"))
csv_op.run()
