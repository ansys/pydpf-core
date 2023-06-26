"""
.. _ref_basic_load_file_example:

Write/Load and Upload/Download a Result File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DPF-Core can upload files to and download files from the server machine.

This example shows how to write and upload files on the server machine and then
download them back on the client side. The resulting fields container is exported
in CSV format.
"""

###############################################################################
# Load a model from the DPF-Core examples:
# ``ansys.dpf.core`` module.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

model = dpf.Model(examples.simple_bar)
mesh = model.metadata.meshed_region

###############################################################################
# Get and Plot the Fields Container for the Result
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get the fields container for the result and plot it so you can compare it later:

displacement_operator = model.results.displacement()
fc_out = displacement_operator.outputs.fields_container()
mesh.plot(fc_out)

###############################################################################
# Export Result
# ~~~~~~~~~~~~~
# Get the fields container for the result and export it in the CSV format:

import os

file_path = os.getcwd() + "\\simple_bar_fc.csv"

export_csv_operator = dpf.operators.serialization.field_to_csv()
export_csv_operator.inputs.field_or_fields_container.connect(fc_out)
export_csv_operator.inputs.file_path.connect(file_path)
export_csv_operator.run()

###############################################################################
# Upload CSV Result File
# ~~~~~~~~~~~~~~~~~~~~~~~
# Upload the file ``simple_bar_fc.csv`` on the server side.
# Here, :func:`upload_file_in_tmp_folder` is used because
# it is assumed that the server machine architecture is unknown.
# However, when the server file path is known, :func:`upload_file`
# can be used.

if not dpf.SERVER.local_server:
    server_file_path = dpf.upload_file_in_tmp_folder(file_path)
    print(server_file_path)

    # Remove file to avoid polluting.
    os.remove(file_path)

###############################################################################
# Download CSV Result File
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Download the file ``simple_bar_fc.csv``:

if not dpf.SERVER.local_server:
    downloaded_client_file_path = os.getcwd() + "\\simple_bar_fc_downloaded.csv"
    dpf.download_file(server_file_path, downloaded_client_file_path)
else:
    downloaded_client_file_path = file_path

###############################################################################
# Load CSV Result File as Operator Input
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Load the fields container contained in the CSV file as an operator input:

my_data_sources = dpf.DataSources(downloaded_client_file_path)
import_csv_operator = dpf.operators.serialization.csv_to_field()
import_csv_operator.inputs.data_sources.connect(my_data_sources)
downloaded_fc_out = import_csv_operator.outputs.fields_container()
mesh.plot(downloaded_fc_out)

# Remove file to avoid polluting.
os.remove(downloaded_client_file_path)

###############################################################################
# Make Operations Over the Imported Fields Container
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use this fields container:

min_max_op = dpf.operators.min_max.min_max_fc()
min_max_op.inputs.fields_container.connect(downloaded_fc_out)
min_field = min_max_op.outputs.field_min()
min_field.data
