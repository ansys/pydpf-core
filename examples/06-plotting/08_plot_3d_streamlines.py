"""
.. _plot_3d_streamlines:

Plot 3D streamlines
~~~~~~~~~~~~~~~~~~~
This example shows how to plot streamlines of fluid simulation results,
for 3D models.

"""

###############################################################################
# Plot streamlines from single source
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###############################################################################
# Import modules, create the data sources and the model
# -----------------------------------------------------
# Import modules:

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
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
# Plot the streamlines adjusting the request
# ------------------------------------------
# The following steps show you how to create streamlines using DpfPlotter, with several sets
# of parameters. It shows the issues that can happen, the adjustments that can be done.

# First, a DpfPlotter is created and the streamline is created with default values.
pl0 = DpfPlotter()
try:
    pl0.add_mesh(meshed_region=meshed_region, opacity=0.3)
    pl0.add_streamlines(meshed_region=meshed_region, field=field)
    pl0.show_figure(show_axes=True)
except:
    # It throws and ends here, because source point are not correctly set.
    # They don't match with the mesh coordinates velocity values
    # are known for.
    # To fix this issue, the source_center parameter is used to move
    # the streamlines source center.
    pass

# Then, using "source_center" argument that moves the source center,
# the "return_source" arguments that displays the source, and
# "permissive" option that allows the display of the source even if the computed
# streamline size is zero, the source coordinates can be correctly set:
pl1 = DpfPlotter()
pl1.add_mesh(meshed_region=meshed_region, opacity=0.3)
pl1.add_streamlines(
    meshed_region=meshed_region,
    field=field,
    return_source=True,
    source_center=(0.1, 0.1, 0.2),
    permissive=True,
)
pl1.show_figure(show_axes=True)

# After adjustment, correct values for "source_center" argument is set.
# The "permissive" option can be removed.
# Velocity data with small opacity to avoid to hide the streamlines can be displayed.
# More settings are added to adapt the streamlines creation to the geometry and
# the data of the model:
# - radius: streamlines radius
# - n_points: source number of points
# - source_radius
# - max_time: allows the streamline to be computed along a certain length
pl2 = DpfPlotter()
pl2.add_field(field, meshed_region, opacity=0.2)
pl2.add_streamlines(
    meshed_region=meshed_region,
    field=field,
    return_source=True,
    source_center=(0.56, 0.48, 0.0),
    radius=0.001,
    n_points=10,
    source_radius=0.075,
    max_time=10.0,
)
pl2.show_figure(show_axes=True)

###############################################################################
# Plot streamlines from several sources
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###############################################################################
# Get data to plot
# ----------------
# Create data sources for fluid simulation result:

files_cfx = examples.download_cfx_heating_coil()
ds_cfx = dpf.DataSources()
ds_cfx.set_result_file_path(files_cfx["cas"], "cas")
ds_cfx.add_file_path(files_cfx["dat"], "dat")

###############################################################################
# Create model from fluid simulation result data sources:
m_cfx = dpf.Model(ds_cfx)

###############################################################################
# Get meshed region and velocity data
meshed_region = m_cfx.metadata.meshed_region
velocity_op = m_cfx.results.velocity()
field = velocity_op.outputs.fields_container()[0]

###############################################################################
# Compute streamlines from different sources and plot
# ---------------------------------------------------

# Add streamlines from different sources:
pl = DpfPlotter()
pl.add_field(field, meshed_region, opacity=0.2)
pl.add_streamlines(
    meshed_region=meshed_region,
    field=field,
    radius=0.007,
    return_source=True,
    source_radius=0.25,
    source_center=(0.75, 0.0, 0.0),
)
pl.add_streamlines(
    meshed_region=meshed_region,
    field=field,
    radius=0.007,
    return_source=True,
    source_radius=0.25,
    source_center=(0.0, 0.75, 0.0),
)
pl.add_streamlines(
    meshed_region=meshed_region,
    field=field,
    radius=0.007,
    return_source=True,
    source_radius=0.25,
    source_center=(-0.75, 0.0, 0.0),
)
pl.add_streamlines(
    meshed_region=meshed_region,
    field=field,
    radius=0.007,
    return_source=True,
    source_radius=0.25,
    source_center=(0.0, -0.75, 0.0),
)

# Plot:
pl.show_figure(show_axes=True)
