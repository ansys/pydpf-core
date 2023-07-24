"""
.. _compute_streamlines:

Compute streamline
~~~~~~~~~~~~~~~~~~
This example shows you how to plot compute streamlines of fluid simulation results.

"""

###############################################################################
# Compute 3D streamlines
# ~~~~~~~~~~~~~~~~~~~~~~

###############################################################################
# Import modules, create the data sources and the model
# -----------------------------------------------------
# Import modules:

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.helpers.streamlines import compute_streamlines
from ansys.dpf.core.plotter import DpfPlotter

###############################################################################
# Create data sources for fluids simulation result:
fluent_files = examples.download_fluent_mixing_elbow_steady_state()
ds_fluent = dpf.DataSources()
ds_fluent.set_result_file_path(fluent_files["cas"][0], "cas")
ds_fluent.add_file_path(fluent_files["dat"][1], "dat")

###############################################################################
# Create model from fluid simulation result data sources:
m_fluent = dpf.Model(ds_fluent)

###############################################################################
# Get meshed region and velocity data
# -----------------------------------
# Meshed region is used as geometric base to compute the streamlines.
# Velocity data is used to compute the streamlines. The velocity data must be nodal.

# Get the meshed region:
meshed_region = m_fluent.metadata.meshed_region

# Get the velocity result at nodes:
velocity_op = m_fluent.results.velocity()
fc = velocity_op.outputs.fields_container()
field = dpf.operators.averaging.to_nodal_fc(fields_container=fc).outputs.fields_container()[0]

###############################################################################
# Compute the streamlines
# -----------------------

streamlines_fc_3D = compute_streamlines(
    meshed_region=meshed_region,
    field=field,
    source_center=(0.56, 0.48, 0.0),
    n_points=10,
    source_radius=0.075,
    max_time=10.0,
)

###############################################################################
# Plot the computed the streamlines
# ---------------------------------

pl = DpfPlotter()
pl.add_field(field, meshed_region, opacity=0.2)
pl.add_streamlines(
    computed_streamlines=streamlines_fc_3D,
    radius=0.001,
)
pl.show_figure(show_axes=True)

###############################################################################
# Compute 2D streamlines
# ~~~~~~~~~~~~~~~~~~~~~~

###############################################################################
# Create data sources for fluids simulation result:
fluent_files = examples.download_fluent_multi_species()
ds_fluent = dpf.DataSources()
ds_fluent.set_result_file_path(fluent_files["cas"], "cas")
ds_fluent.add_file_path(fluent_files["dat"], "dat")

###############################################################################
# Create model from fluid simulation result data sources:
m_fluent = dpf.Model(ds_fluent)

###############################################################################
# Get meshed region and velocity data
# -----------------------------------
# Meshed region is used as the geometric base to compute the streamlines.
# Velocity data is used to compute the streamlines. The velocity data must be nodal.

# Get the meshed region:
meshed_region = m_fluent.metadata.meshed_region

# Get the velocity result at nodes:
velocity_op = m_fluent.results.velocity()
fc = velocity_op.outputs.fields_container()
field = dpf.operators.averaging.to_nodal_fc(fields_container=fc).outputs.fields_container()[0]

###############################################################################
# Compute and plot single streamline
# ----------------------------------

streamlines_fc_2D_single = compute_streamlines(
    meshed_region=meshed_region,
    field=field,
    start_position=(0.005, 0.0005, 0.0),
    surface_streamlines=True
)

pl_single = DpfPlotter()
pl_single.add_field(field, meshed_region, opacity=0.2)
pl_single.add_streamlines(
    computed_streamlines=streamlines_fc_2D_single,
    radius=0.00002,
)
pl_single.show_figure(show_axes=True)

###############################################################################
# Compute and plot multiple streamlines
# -------------------------------------

streamlines_fc_2D_multiple = compute_streamlines(
    meshed_region=meshed_region,
    field=field,
    pointa=(0.005, 0.0001, 0.0),
    pointb=(0.005, 0.001, 0.0),
    n_points=10,
    surface_streamlines=True
)

pl_multiple = DpfPlotter()
pl_multiple.add_field(field, meshed_region, opacity=0.2)
pl_multiple.add_streamlines(
    computed_streamlines=streamlines_fc_2D_multiple,
    radius=0.000015,
)
pl_multiple.show_figure(plane="xy", show_axes=True)