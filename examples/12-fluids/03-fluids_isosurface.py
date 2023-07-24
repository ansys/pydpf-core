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

path = examples.download_fluent_multi_phase()
ds = dpf.DataSources(path)
ds.set_result_file_path(path["cas"], "cas")
ds.add_file_path(path["dat"], "dat")
streams = dpf.operators.metadata.streams_provider(data_sources=ds)

###############################################################################
# Explore elemental (cell) results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# We split the work in those steps
#   -> Evaluate the mesh and store it
#   -> Extract from the mesh the node and element scoping
#   -> Evaluate on variable (for example the pressure) and store it
#   -> Average the results on nodes in order to cut iso-surfaces
#   -> Cut the mesh for a specific value

###############################################################################
# Evaluate the mesh through mesh_provider operator

mesh_whole = dpf.operators.mesh.mesh_provider(streams_container=streams).eval()
print(mesh_whole)
mesh_whole.plot()

###############################################################################
# Element and node scoping

element_scop = dpf.operators.scoping.elemental_from_mesh(mesh=mesh_whole).eval()
node_scop = dpf.operators.scoping.nodal_from_mesh(mesh=mesh_whole).eval()

print("elements in whole mesh : ", element_scop, "\n")
print("nodes in whole mesh : ", node_scop)

###############################################################################
# Here we choose to work with the static pressure by default which is a scalar and
# elemental variable without multi-species. With a multi-species case, we should have
# select one specific using qualifiers ellipsis pins and connecting a LabelSpace "phase".

P_S = dpf.operators.result.static_pressure(streams_container=streams, mesh=mesh_whole).eval()
print(P_S)

###############################################################################
# In order to extract the iso-surfaces for this specific variable, we have first to average
# the elemental values to the nodes. The mesh_cut operator only works for nodal variables.

to_nodal = dpf.operators.averaging.elemental_to_nodal(field=P_S, mesh_scoping=node_scop).eval()
print(to_nodal)

###############################################################################
# We can finally use the mesh_cut operator on this specific variable for a specific iso-value
# arbitrary chosen. We have to specify also the mesh scoping. By default, we choose to take
# into account shell and skin elements.

iso_surface = dpf.operators.mesh.mesh_cut(
    field=to_nodal, iso_value=1.0, closed_surface=0, mesh=mesh_whole, slice_surfaces=True
).eval()

c_pos = [(0.04, 0.03, 0.05), (0.0, 0.0, 0.0), (0.1, 0.2, 0.1)]

pl = DpfPlotter()
pl.add_mesh(
    mesh_whole, style="surface", show_edges=True, show_axes=True, color="w", opacity=0.3
)
pl.add_mesh(
    iso_surface, style="surface", show_edges=True, show_axes=True, color="w"
)
pl.show_figure(show_axes=True, cpos=c_pos, return_cpos=True)
