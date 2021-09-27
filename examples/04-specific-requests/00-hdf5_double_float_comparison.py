"""
.. _ref_basic_hdf5:

Hdf5 export and compare precision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to use hdf5 format to export and
make a comparison between simple/double precision.

"""

###############################################################################
# Import dpf module and its examples files, and create a temporary directory

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops
import os

import tempfile

tmpdir = tempfile.mkdtemp()

###############################################################################
# Create the model and get stresses, displacements and mesh.

transient = examples.download_transient_result()
model = dpf.Model(transient)

stress = model.results.stress()
displacement = model.results.displacement()
mesh = model.metadata.meshed_region

###############################################################################
# Create the hdf5 export operator. Hdf5 module should already be loaded.

h5op = ops.serialization.serialize_to_hdf5()
print(h5op)

###############################################################################
# Connect the correct time scoping to the results operators (stress
# and displacement).

timeIds = list(range(1, model.metadata.time_freq_support.n_sets + 1))
timeIds

stress.inputs.time_scoping.connect(timeIds)
displacement.inputs.time_scoping.connect(timeIds)

###############################################################################
# Connect inputs of the hdf5 export operator.

h5op.inputs.data1.connect(stress.outputs)
h5op.inputs.data2.connect(displacement.outputs)
h5op.inputs.data3.connect(mesh)

###############################################################################
# Export with simple precision

h5op.inputs.file_path.connect(os.path.join(tmpdir, "c:/temp/dpf_float.h5"))
h5op.run()

###############################################################################
# Export with simple precision

h5op.inputs.export_floats.connect(False)
h5op.inputs.file_path.connect(os.path.join(tmpdir, "c:/temp/dpf_double.h5"))
h5op.run()

###############################################################################
# Comparison
float_precision = os.stat(os.path.join(tmpdir, "c:/temp/dpf_float.h5")).st_size
double_precision = os.stat(os.path.join(tmpdir, "c:/temp/dpf_double.h5")).st_size
print(
    f"size with float precision: {float_precision}\n"
    f"size with double precision: {double_precision}"
)
