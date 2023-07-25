# noqa: D400
"""
.. _ref_basic_hdf5:

HDF5 export and compare precision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to use HDF5 format to export and
compare simple precision versus double precision.

"""

###############################################################################
# Import the ``dpf-core`` module and its examples files, and then create a
# temporary directory.

import os

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Create the model and get the stresses, displacements, and mesh.

transient = examples.download_transient_result()
model = dpf.Model(transient)

stress = model.results.stress()
displacement = model.results.displacement()
mesh = model.metadata.meshed_region

###############################################################################
# Create the HDF5 export operator. The HDF5 module should already be loaded.

h5op = ops.serialization.serialize_to_hdf5()
print(h5op)

###############################################################################
# Connect the correct time scoping to the results operators (stress
# and displacement).

timeIds = list(range(1, model.metadata.time_freq_support.n_sets + 1))

stress.inputs.time_scoping.connect(timeIds)
displacement.inputs.time_scoping.connect(timeIds)

###############################################################################
# Connect inputs of the HDF5 export operator.

h5op.inputs.data1.connect(stress.outputs)
h5op.inputs.data2.connect(displacement.outputs)
h5op.inputs.data3.connect(mesh)

###############################################################################
# Define a temporary folder for outputs
tmpdir = dpf.core.make_tmp_dir_server(dpf.SERVER)
files = [
    dpf.path_utilities.join(tmpdir, "dpf_float.h5"),
    dpf.path_utilities.join(tmpdir, "dpf_double.h5"),
]
###############################################################################
# Export with simple precision.

h5op.inputs.file_path.connect(files[0])
h5op.run()

###############################################################################
# Export with double precision.

h5op.inputs.export_floats.connect(False)
h5op.inputs.file_path.connect(files[1])
h5op.run()

###############################################################################
# Download the resulting .h5 files if necessary

if not dpf.SERVER.local_server:
    float_file_path = os.path.join(os.getcwd(), "dpf_float.h5")
    double_file_path = os.path.join(os.getcwd(), "dpf_double.h5")
    dpf.download_file(files[0], float_file_path)
    dpf.download_file(files[1], double_file_path)
else:
    float_file_path = files[0]
    double_file_path = files[1]


###############################################################################
# Compare simple precision versus double precision.
float_precision = os.stat(float_file_path).st_size
double_precision = os.stat(double_file_path).st_size
print(
    f"size with float precision: {float_precision}\n"
    f"size with double precision: {double_precision}"
)
