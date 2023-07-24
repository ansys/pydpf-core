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

paths = examples.download_fluent_multi_phase()
ds = dpf.DataSources()
ds.set_result_file_path(paths["cas"], "cas")
ds.add_file_path(paths["dat"], "dat")
streams = dpf.operators.metadata.streams_provider(data_sources=ds)

###############################################################################
# Evaluate the mesh with mesh_provider operator in order to scope the mesh_cut operator
# with the mesh.

whole_mesh = dpf.operators.mesh.mesh_provider(streams_container=streams).eval()
print(whole_mesh)

pl = DpfPlotter()
pl.add_mesh(whole_mesh)
cpos_whole_mesh = [
    (-0.17022616684387018, -0.20190398787025482, 0.1948471407823707),
    (0.00670901800318915, 0.00674082901283412, 0.0125629516499091),
    (-0.84269816220442720, 0.39520703007216523, -0.3656107367116286),
]
pl.show_figure(cpos=cpos_whole_mesh, show_axes=True)

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
print(P_S)

pl = DpfPlotter()
pl.add_field(P_S[0])
cpos_mesh_variable = [
    (-0.17022616684387018, -0.20190398787025482, 0.1948471407823707),
    (0.00670901800318915, 0.00674082901283412, 0.0125629516499091),
    (-0.84269816220442720, 0.39520703007216523, -0.3656107367116286),
]
pl.show_figure(cpos=cpos_mesh_variable, show_axes=True)

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
    field=to_nodal, iso_value=1.0, closed_surface=0, mesh=whole_mesh, slice_surfaces=True
).eval()

print(iso_surface)

c_pos_iso = [
    (-0.17022616684387018, -0.20190398787025482, 0.1948471407823707),
    (0.00670901800318915, 0.00674082901283412, 0.0125629516499091),
    (-0.84269816220442720, 0.39520703007216523, -0.3656107367116286),
]

pl = DpfPlotter()
pl.add_mesh(
    whole_mesh, style="surface", show_edges=True, show_axes=True, color="w", opacity=0.6
)
pl.add_field(
    P_S[0], style="surface", show_edges=True, show_axes=True, color="w", opacity=0.6
)
pl.add_mesh(
    iso_surface, style="surface", show_edges=True, show_axes=True, color="r"
)
pl.show_figure(show_axes=True, cpos=c_pos_iso, return_cpos=True)
