"""
.. _ref_basic_load_file_example:

Write/load and upload/download a result file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ansys.dpf.core module is able to upload files to 
the server machine, and dowload files from there. 

This example shows how to write and upload files 
on the server machine, then how to download it back 
on the cient side. 

The result fields container will be exported under 
.csv format.
"""

###############################################################################
# Let's first load a ``Model`` from the ``Examples`` provided by 
# ``ansys.dpf.core`` module. 

from ansys.dpf import core
from ansys.dpf.core import examples

model = core.Model(examples.simple_bar)
mesh = model.metadata.meshed_region

###############################################################################
# Get the result
# ~~~~~~~~~~~~~~
# Get the result fields container and plot (in order to compare later)

displacement_operator = model.results.displacement()
fc_out = displacement_operator.outputs.fields_container()
mesh.plot(fc_out)

###############################################################################
# Export result
# ~~~~~~~~~~~~~
# Let's get the result fields container and export
# it using .csv format. 

import os
file_path = os.getcwd() + '\\simple_bar_fc.csv'

export_csv_operator = core.operators.serialization.field_to_csv()
export_csv_operator.inputs.field_or_fields_container.connect(fc_out)
export_csv_operator.inputs.file_path.connect(file_path)
export_csv_operator.run()

###############################################################################
# Upload .csv result file
# ~~~~~~~~~~~~~~~~~~~~~~~
# Let's upload the simple_bar_fc.csv file 
# on the server side. The upload_file_in_tmp_folder()
# method will be used here, because we assume we don't
# know the server machine architecture. However, the 
# upload_file() method can be used the same way wil a 
# know "server file path". 

server_file_path = core.upload_file_in_tmp_folder(file_path)
print(server_file_path)

# remove file to avoid polluting
os.remove(file_path)

###############################################################################
# Download .csv result file
# ~~~~~~~~~~~~~~~~~~~~~~~
# Let's now download the simple_bar_fc.csv file.

downloaded_client_file_path = os.getcwd() + '\\simple_bar_fc_downloaded.csv'
core.download_file(server_file_path, downloaded_client_file_path)

###############################################################################
# Load .csv result file as operators input
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Let's now load the fields container contained in 
# the .csv file.

my_data_sources = core.DataSources(downloaded_client_file_path)
import_csv_operator = core.operators.serialization.csv_to_field()
import_csv_operator.inputs.data_sources.connect(my_data_sources)
downloaded_fc_out = import_csv_operator.outputs.fields_container()
mesh.plot(downloaded_fc_out)

# remove file to avoid polluting
os.remove(downloaded_client_file_path)

###############################################################################
# Make operations over the imported fields container
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This fields container can be used as it was introduced 
# in the basics examples. 

min_max_op = core.operators.min_max.min_max_fc()
min_max_op.inputs.fields_container.connect(downloaded_fc_out)
min_field = min_max_op.outputs.field_min()
min_field.data