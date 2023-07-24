"""
.. _ref_fluids_isosurface:

Compute iso-surfaces on fluid models
------------------------------------------------------

This example shows how to compute iso-surfaces on fluid models.
"""

###############################################################################
# Import the ``dpf-core`` module and its examples files.
# ------------------------------

import ansys.dpf.core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.plotter import DpfPlotter

###############################################################################
# Specify the file path.
# We first work on a cas/dat.h5 file with only nodal variable.
# ------------------------------

path = examples.download_cfx_heating_coil()
ds = dpf.DataSources()
ds.set_result_file_path(path["cas"], "cas")
ds.add_file_path(path["dat"], "dat")
streams = dpf.operators.metadata.streams_provider(data_sources=ds)

###############################################################################
# Evaluate the mesh with mesh_provider operator in order to scope the mesh_cut operator
# with the mesh.
# ------------------------------

whole_mesh = dpf.operators.mesh.mesh_provider(streams_container=streams).eval()
print(whole_mesh)

pl = DpfPlotter()
pl.add_mesh(whole_mesh)
cpos_whole_mesh = [
    (4.256160478475664, 4.73662111240005, 4.00410065817644),
    (-0.0011924505233764648, 1.8596649169921875e-05, 1.125),
    (-0.2738679385987956, -0.30771426079547065, 0.9112125360807675),
]
pl.show_figure(cpos=cpos_whole_mesh, show_axes=True, return_cpos=True)

###############################################################################
# Here we choose to work with the static pressure by default which is a scalar and
# nodal variable without multi-species/phases. With a multi-species case, we should have
# select one specific using qualifiers ellipsis pins and connecting a LabelSpace "specie"/"phase".
# ------------------------------

P_S = dpf.operators.result.static_pressure(streams_container=streams, mesh=whole_mesh).eval()
print(P_S[0])

pl = DpfPlotter()
pl.add_field(P_S[0])
cpos_mesh_variable = [
    (4.256160478475664, 4.73662111240005, 4.00410065817644),
    (-0.0011924505233764648, 1.8596649169921875e-05, 1.125),
    (-0.2738679385987956, -0.30771426079547065, 0.9112125360807675),
]
pl.show_figure(cpos=cpos_mesh_variable, show_axes=True)

###############################################################################
# We can finally use the mesh_cut operator on this specific variable for a specific iso-value
# arbitrary chosen. We have to specify also the mesh scoping. By default, we choose to take
# into account shell and skin elements.
# ------------------------------

max_pressure = 361.8170  # Pa
min_pressure = -153.5356  # Pa

number_of_iso_surface = 5
step = (max_pressure - min_pressure) / number_of_iso_surface

pl = DpfPlotter()
c_pos_iso = [
    (4.256160478475664, 4.73662111240005, 4.00410065817644),
    (-0.0011924505233764648, 1.8596649169921875e-05, 1.125),
    (-0.2738679385987956, -0.30771426079547065, 0.9112125360807675),
]
pl.add_mesh(
    meshed_region=whole_mesh,
    style="wireframe",
    show_edges=True,
    show_axes=True,
    color="black",
    opacity=0.3,
)

for i in range(number_of_iso_surface):
    iso_surface = dpf.operators.mesh.mesh_cut(
        field=P_S[0], iso_value=min_pressure, closed_surface=0, mesh=whole_mesh, slice_surfaces=True
    ).eval()
    P_S_step = dpf.Field(location=dpf.locations.overall, nature=dpf.common.natures.scalar)
    P_S_step.append([min_pressure], i)
    P_S_step.name = "static pressure"
    P_S_step.unit = "Pa"
    pl.add_field(
        field=P_S_step, meshed_region=iso_surface, style="surface", show_edges=False, show_axes=True
    )
    min_pressure += step

pl.show_figure(show_axes=True, cpos=c_pos_iso, return_cpos=True)

###############################################################################
# For elemental or face variables we should have done an averaging on node
# by using elemental_to_node operator and set as an input of the
# mesh_cut operator the node scoping