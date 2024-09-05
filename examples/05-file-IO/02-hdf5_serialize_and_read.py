"""
.. _ref_io_hdf5_import_export:

HDF5 export and import operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows you how to use the HDF5 format to export results
and meshed regions in an H5 file.
It also demonstrates how to read results and meshed regions from the
created H5 file.

First, it exports all the results for all time frequencies,
then it exports all the time sets for the results, per time set.
Finally, it reads the results and compares them.
For the example to run correctly, ensure you do not have an existing H5 file.

.. note::
    This example requires DPF 7.0 (ansys-dpf-server-2024-1-pre0) or above.
    For more information, see :ref:`ref_compatibility`.

"""

###############################################################################
# Import modules, instantiate model and create temporary folder
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import the ``dpf-core`` module and its examples files.

import ansys.dpf.core as dpf
from ansys.dpf.core import examples

###############################################################################
# Instantiate the model and the provider operators:

model = dpf.Model(examples.download_transient_result())
streams_cont = model.metadata.streams_provider.outputs.streams_container
time_freq_op = dpf.operators.metadata.time_freq_provider(streams_container=streams_cont)
time_freq_support = time_freq_op.outputs.time_freq_support()
time_freqs = time_freq_support.time_frequencies

result_names_on_all_time_steps = []
result_names_time_per_time = []

num_res = len(model.results)
num_sets = len(time_freqs.data)

###############################################################################
# Define a temporary folder for outputs:
tmpdir = dpf.core.make_tmp_dir_server(dpf.SERVER)
files = [
    dpf.path_utilities.join(tmpdir, "file_on_all_time_steps.h5"),
    dpf.path_utilities.join(tmpdir, "file_time_per_time.h5"),
]

###############################################################################
# Use H5 serialization operator
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Export all results on all time frequencies:
h5_serialization_op_all_times = dpf.operators.serialization.hdf5dpf_generate_result_file()
h5_serialization_op_all_times.inputs.filename.connect(files[0])
h5_serialization_op_all_times.inputs.mesh_provider_out.connect(model.metadata.meshed_region)
h5_serialization_op_all_times.inputs.time_freq_support_out.connect(time_freq_support)

for i, res in enumerate(model.results):
    res_name = "result_" + res().name
    result_names_on_all_time_steps.append(res_name)
    h5_serialization_op_all_times.connect(2 * i + 4, res_name)
    h5_serialization_op_all_times.connect(2 * i + 5, res.on_all_time_freqs())

h5_all_times_ds = h5_serialization_op_all_times.outputs.data_sources()

###############################################################################
# Export all the results, time set per time set:
h5_serialization_op_set_per_set = dpf.operators.serialization.hdf5dpf_generate_result_file()
h5_serialization_op_set_per_set.inputs.filename.connect(files[1])
h5_serialization_op_set_per_set.inputs.mesh_provider_out.connect(model.metadata.meshed_region)
h5_serialization_op_set_per_set.inputs.time_freq_support_out.connect(time_freq_support)

for j, freq in enumerate(time_freqs.data):
    for i, res in enumerate(model.results):
        res_name = "result_" + res().name + "_time_" + str(freq)
        result_names_time_per_time.append(res_name)
        h5_serialization_op_set_per_set.connect(2 * (j * num_res + i) + 4, res_name)
        h5_serialization_op_set_per_set.connect(
            2 * (j * num_res + i) + 5, res.on_time_scoping(j + 1).eval()
        )

h5_set_per_set_ds = h5_serialization_op_set_per_set.outputs.data_sources()

###############################################################################
# Use H5 reading operator
# ~~~~~~~~~~~~~~~~~~~~~~~
# Read the results from all time steps files:
h5_stream_prov_op = dpf.operators.metadata.streams_provider()
h5_stream_prov_op.inputs.data_sources.connect(h5_all_times_ds)
res_deser_all_times_list = []
h5_read_op = dpf.operators.serialization.hdf5dpf_custom_read()
h5_read_op.inputs.streams.connect(h5_stream_prov_op.outputs)
h5_read_op.inputs.time_scoping.connect(dpf.Scoping(ids=list(range(1, 54)), location="time"))
for i, res_name in enumerate(result_names_on_all_time_steps):
    h5_read_op.inputs.result_name.connect(res_name)
    res_deser = h5_read_op.outputs.field_or_fields_container_as_fields_container()
    res_deser_all_times_list.append(res_deser)

###############################################################################
# Read the meshed region from all time steps file:
mesh_prov_op = dpf.operators.mesh.mesh_provider()
mesh_prov_op.inputs.streams_container.connect(h5_stream_prov_op.outputs)
mesh_deser_all_times = mesh_prov_op.outputs.mesh()

###############################################################################
# Read the results from the time set per set file:
h5_stream_prov_op_2 = dpf.operators.metadata.streams_provider()
h5_stream_prov_op_2.inputs.data_sources.connect(h5_set_per_set_ds)
res_deser_set_per_set_list = []
h5_read_op_2 = dpf.operators.serialization.hdf5dpf_custom_read()
h5_read_op_2.inputs.streams.connect(h5_stream_prov_op_2.outputs)
for i, res_name in enumerate(result_names_time_per_time):
    h5_read_op_2.inputs.result_name.connect(res_name)
    res_deser = h5_read_op_2.outputs.field_or_fields_container_as_fields_container()
    res_deser_set_per_set_list.append(res_deser)

###############################################################################
# Read the meshed region from all time steps files:
mesh_prov_op_2 = dpf.operators.mesh.mesh_provider()
mesh_prov_op_2.inputs.streams_container.connect(h5_stream_prov_op_2.outputs)
mesh_deser_set_per_set = mesh_prov_op_2.outputs.mesh()

###############################################################################
# Compare results
# ~~~~~~~~~~~~~~~

###############################################################################
# Print global data:
print("Number of results is: " + str(num_res))
print("Number of time sets is: " + str(num_sets))
print("Results names for 'all time steps' file: ")
print(result_names_on_all_time_steps)
print("Results names for 'set per set' file: ")
print(result_names_time_per_time)

###############################################################################
# compare first result at second time set:
fc_all_steps_first_step_first_res = res_deser_all_times_list[0].get_field_by_time_id(2)  # set 1
mesh_deser_all_times.plot(fc_all_steps_first_step_first_res)

mesh_deser_set_per_set.plot(res_deser_set_per_set_list[num_res * 1 + 0])

###############################################################################
# compare 4th result at 6 time set:
to_nodal_op = dpf.operators.averaging.to_nodal_fc()

fc_all_steps_first_step_first_res = res_deser_all_times_list[3].get_field_by_time_id(6)  # set 6
mesh_deser_all_times.plot(
    dpf.operators.averaging.to_nodal(fc_all_steps_first_step_first_res).outputs.field()
)

mesh_deser_set_per_set.plot(
    dpf.operators.averaging.to_nodal(res_deser_set_per_set_list[num_res * 5 + 3]).outputs.field()
)
