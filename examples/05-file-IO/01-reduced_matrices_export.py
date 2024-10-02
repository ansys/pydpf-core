# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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

"""
.. _ref_reduced_matrices_export:

Get reduced matrices and make export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to get reduced matrices and
export them to HDF5 and CSV files.

"""

###############################################################################
# Import the ``dpf-core`` module and its examples files, and then create a
# temporary directory.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, operators as ops

###############################################################################
# Create the operator and connect data sources.

ds = dpf.DataSources(examples.download_sub_file())

matrices_provider = ops.result.cms_matrices_provider()
matrices_provider.inputs.data_sources.connect(ds)

###############################################################################
# Get result fields container that contains the reduced matrices.

fields = matrices_provider.outputs.fields_container()

len(fields)

fields[0].data

###############################################################################
# Define a temporary folder for outputs
tmpdir = dpf.core.make_tmp_dir_server(dpf.SERVER)

###############################################################################
# Export the result fields container to an HDF5 file.

h5_op = ops.serialization.serialize_to_hdf5()
h5_op.inputs.data1.connect(matrices_provider.outputs)
h5_op.inputs.file_path.connect(dpf.path_utilities.join(tmpdir, "matrices.h5"))
h5_op.run()

###############################################################################
# Export the result fields container to a CSV file.

csv_op = ops.serialization.field_to_csv()
csv_op.inputs.field_or_fields_container.connect(matrices_provider.outputs)
csv_op.inputs.file_path.connect(dpf.path_utilities.join(tmpdir, "matrices.csv"))
csv_op.run()
