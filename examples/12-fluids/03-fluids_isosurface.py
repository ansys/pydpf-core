"""
.. _ref_fluids_isosurface:

Compute iso-surfaces on fluid models
------------------------------------------------------

This example shows how to compute iso-surfaces on fluid models without
polygons and polyhedrons.
"""

###############################################################################
# Import the ``dpf-core`` module and its examples files.
# ------------------------------

import ansys.dpf.core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.plotter import DpfPlotter

###############################################################################
# Specify the file path.
# We first work on a cas/dat.h5 file with only elemental variable.
# ------------------------------

path = examples.download_fluent_axial_comp()["flprj"]
ds = dpf.DataSources(path)
streams = dpf.operators.metadata.streams_provider(data_sources=ds)

###############################################################################
# Evaluate the mesh with mesh_provider operator in order to scope the mesh_cut operator
# with the mesh.

whole_mesh = dpf.operators.mesh.mesh_provider(streams_container=streams).eval()
print(whole_mesh)

pl = DpfPlotter()
pl.add_mesh(whole_mesh)
cpos_whole_mesh = [
    (-0.15891996848242032, -0.26917748231475785, -0.02581671258881637),
    (-0.012145186906044624, -0.07864627423068209, -0.022515001706779003),
    (-0.7907463709555519, 0.6100286761144966, -0.050844774939214174),
]
# pl.show_figure(cpos=cpos_whole_mesh, show_axes=True, return_cpos=True)


###############################################################################
# Element and node scoping in order to scope first the result ont the element
# and then the mesh_cut operator on the node.

node_scop = dpf.operators.scoping.nodal_from_mesh(mesh=whole_mesh).eval()

print("nodes in whole mesh : ", node_scop)

###############################################################################
# Here we choose to work with the static pressure by default which is a scalar and
# elemental variable without multi-species. With a multi-species case, we should have
# select one specific using qualifiers ellipsis pins and connecting a LabelSpace "phase".

P_S = dpf.operators.result.static_pressure(streams_container=streams, mesh=whole_mesh).eval()
print(P_S[0])

pl = DpfPlotter()
pl.add_field(P_S[0])
cpos_mesh_variable = [
    (-0.15891996848242032, -0.26917748231475785, -0.02581671258881637),
    (-0.012145186906044624, -0.07864627423068209, -0.022515001706779003),
    (-0.7907463709555519, 0.6100286761144966, -0.050844774939214174),
]
# pl.show_figure(cpos=cpos_mesh_variable, show_axes=True)

###############################################################################
# In order to extract the iso-surfaces for this specific variable, we have first to average
# the elemental values to the nodes. The mesh_cut operator only works for nodal variables.

to_nodal = dpf.operators.averaging.elemental_to_nodal(field=P_S, mesh_scoping=node_scop).eval()
print(to_nodal)

###############################################################################
# We can finally use the mesh_cut operator on this specific variable for a specific iso-value
# arbitrary chosen. We have to specify also the mesh scoping. By default, we choose to take
# into account shell and skin elements.

max_pressure = 136877.2 #Pa
min_pressure = 24554.91 #Pa
number_of_iso_surface = 5
step = (max_pressure - min_pressure)/number_of_iso_surface

pl = DpfPlotter()
c_pos_iso = [
    (-0.15891996848242032, -0.26917748231475785, -0.02581671258881637),
    (-0.012145186906044624, -0.07864627423068209, -0.022515001706779003),
    (-0.7907463709555519, 0.6100286761144966, -0.050844774939214174),
]
pl.add_mesh(meshed_region=whole_mesh, style="wireframe", show_edges=True, show_axes=True, color="w", opacity=0.3)

for i in range(number_of_iso_surface):
    iso_surface = dpf.operators.mesh.mesh_cut(
        field=to_nodal, iso_value=min_pressure, closed_surface=0, mesh=whole_mesh, slice_surfaces=True
    ).eval()
    P_S_step = dpf.Field(location=dpf.locations.overall, nature=dpf.common.natures.scalar)
    P_S_step.append([min_pressure], i)
    pl.add_field(field=P_S_step, meshed_region=iso_surface, style="surface", show_edges=False, show_axes=True)
    min_pressure += step

pl.show_figure(show_axes=True, cpos=c_pos_iso, return_cpos=True)
