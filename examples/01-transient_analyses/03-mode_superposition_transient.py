"""
.. _ref_msup_transient:

Mode superposition transient analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to postprocess a mode superposition transient result
and visualize the outputs. It also shows how to select modes for the modal expansion.

"""
# Import the necessary modules
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# Modal superposition on all modes available
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Download the mode superposition transient result example. This example is
# not included in DPF-Core by default to speed up the installation.
# Downloading this example should take only a few seconds.
#
# Next, create the model and display the state of the result. This mode superposition transient
# result file contains several individual results, each at a different timestamp, automatically
# expanded on all available modes.

# msup_transient = examples.download_transient_result()
msup_transient = {
    "rst": r"D:\ANSYSDev\Sandbox\UnitTestDataFiles\expansion\msup\Transient\plate1\file.rst",
    "rdsp": r"D:\ANSYSDev\Sandbox\UnitTestDataFiles\expansion\msup\Transient\plate1\file.rdsp",
    "mode": r"D:\ANSYSDev\Sandbox\UnitTestDataFiles\expansion\msup\Transient\plate1\modal\file.mode",
    "modal_rst": r"D:\ANSYSDev\Sandbox\UnitTestDataFiles\expansion\msup\Transient\plate1\modal\file.rst",
}
data_sources = dpf.DataSources(msup_transient["rdsp"])
up_stream_data_sources = dpf.DataSources(msup_transient["mode"])
up_stream_data_sources.add_file_path(msup_transient["modal_rst"])

data_sources.add_upstream(up_stream_data_sources)
model = dpf.Model(data_sources)
print(model)

###############################################################################
# Get the expanded displacement fields for each time-step
disp = model.results.displacement.on_all_time_freqs.eval()
print(disp)

###############################################################################
# Animate the result
disp.animate(scale_factor=5.0)

###############################################################################
# Get the expanded displacement fields on selected time-steps:
disp = model.results.displacement.on_time_scoping([1, 2, 3]).eval()
print(disp)

###############################################################################
# Get the expanded displacement fields on part of the mesh, for selected time-steps:
# TODO: NOT WORKING
# partial_scoping = dpf.mesh_scoping_factory.nodal_scoping(
#     model.metadata.meshed_region.nodes.scoping.ids[:200]
# )
# disp = model.results.displacement.on_time_scoping(
#     [1, 2, 3]
# ).on_mesh_scoping(
#     partial_scoping
# ).eval()
# print(disp)

###############################################################################
# Modal superposition on selected modes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# To select a subset of modes for expansion, you cannot use the source operators directly.
# Below is a workflow to extract results while specifying modes for expansion:

# First build a data source for the modal response factors
transient_response_ds = dpf.DataSources(result_path=msup_transient["rdsp"])

# Define the time-steps of interest
time_scoping = dpf.time_freq_scoping_factory.scoping_by_sets(list(range(1, 22)))

# Extract the result of interest
displacement_fc = dpf.operators.result.displacement(
    data_sources=transient_response_ds,  # Input here the modal response data source
    time_scoping=time_scoping,  # Input here the time-steps of interest
    mesh_scoping=None  # Specify here the region of interest
).eval()

# The FieldsContainer contains one field per time-step, with data for each mode (entity)
print(displacement_fc)

###############################################################################
# Now scope the FieldsContainer to the modes of interest
mode_scoping = dpf.Scoping(ids=list(range(1, 3)))  # Modes of interest
displacement_fc = dpf.operators.scoping.rescope_fc(
    fields_container=displacement_fc,
    mesh_scoping=mode_scoping,  # Input here the modes of interest
).eval()

# The FieldsContainer contains one field per time-step, with data for each selected mode (entity)
print(displacement_fc)

###############################################################################
# Get the modal basis of interest, with mode selection
modal_basis_ds = dpf.DataSources(result_path=msup_transient["mode"])
modal_basis_ds.add_file_path(msup_transient["modal_rst"])  # Associate mesh data to the mode shapes
modal_basis_fc = dpf.operators.result.modal_basis(
    data_sources=modal_basis_ds,
    time_scoping=mode_scoping,  # Input here the modes of interest
    mesh_scoping=None,  # Specify here the region of interest
).eval()

# The modal basis FieldsContainer contains one field per mode shape
print(modal_basis_fc)

###############################################################################
# Plot each mode shape
for n, modal_basis_f in enumerate(modal_basis_fc):
    modal_basis_f.plot(deform_by=modal_basis_f, text=f"mode shape {n+1}")

###############################################################################
# Apply modal superposition
modal_superposition_fc = dpf.operators.math.modal_superposition(
    modal_basis=modal_basis_fc,  # FieldsContainer obtained via the modal_basis operator
    solution_in_modal_space=displacement_fc,  # FieldsContainer obtained via the result operator
    time_scoping=time_scoping,  # Specify here the time-steps of interest
    mesh_scoping=None,  # Specify here the region of interest
).eval()

# We obtain the displacement fields at each time-step, with modal superposition
print(modal_superposition_fc)

###############################################################################
# Animate the result
modal_superposition_fc.animate(scale_factor=5.0)
