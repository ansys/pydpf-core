"""
.. _ref_reduced_matrices_export:

Get reduced matrices and make export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to get reduced matrices and
export them to HDF5 and CSV files.

.. note::
    This example requires the Premium ServerContext.
    For more information, see :ref:`user_guide_server_context`.

"""

###############################################################################
# Import the ``dpf-core`` module and its examples files, and then create a
# temporary directory.

import os
import tempfile

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops


dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

tmpdir = tempfile.mkdtemp()

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
# Export the result fields container to an HDF5 file.

h5_op = ops.serialization.serialize_to_hdf5()
h5_op.inputs.data1.connect(matrices_provider.outputs)
h5_op.inputs.file_path.connect(os.path.join(tmpdir, "matrices.h5"))
h5_op.run()

###############################################################################
# Export the result fields container to a CSV file.

csv_op = ops.serialization.field_to_csv()
csv_op.inputs.field_or_fields_container.connect(matrices_provider.outputs)
csv_op.inputs.file_path.connect(os.path.join(tmpdir, "matrices.csv"))
csv_op.run()
