"""
.. _ref_fluids_mesh:

Explore Fluids mesh
------------------------------------------------------

"""

###############################################################################
# Exploring an Ansys Fluent mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This example demonstrates how you can explore an Ansys Fluent mesh. Import
# the result file

import ansys.dpf.core as dpf
from ansys.dpf.core import examples

path = examples.download_fluent_axial_comp()["flprj"]
ds = dpf.DataSources(path)
streams = dpf.operators.metadata.streams_provider(data_sources=ds)


###############################################################################
# Using the ``mesh_provider``
# ---------------------------
# The ``mesh_provider`` operator can be used to retrieve the whole mesh of the
# model or the `MeshedRegion` restricted to a particular body or face zone. The
# behavior will differ depending on the inputs to the ``region_scoping`` pin.
# If no scoping is connected, the mesh for the whole model is obtained. This
# is the same mesh that is obtained if the ``Model.metadata.meshed_region``
# API is employed.

mesh_whole = dpf.operators.mesh.mesh_provider(streams_container=streams).eval()
print(mesh_whole)
mesh_whole.plot()

###############################################################################
# If the ``region_scoping`` pin is connected, a ``Scoping`` with 1 zone ID is
# expected, or an integer list with one item, or a single integer. The supported
# zone IDs are either face zone IDs or body IDs. The zones of this particular model
# are explored in :ref:`_ref_fluids_model`. ID 4 (rotor-shroud) corresponds to a
# face zone, and thus its mesh is only comprised of faces and nodes. ID 13 (fluid-rotor)
# is a body, and thus its mesh has elements (cells), faces and nodes.

mesh_4 = dpf.operators.mesh.mesh_provider(streams_container=streams, region_scoping=4).eval()
print(mesh_4)
mesh_4.plot()
mesh_13 = dpf.operators.mesh.mesh_provider(streams_container=streams, region_scoping=[13]).eval()
print(mesh_13)
mesh_13.plot()

###############################################################################
# Using the ``meshes_provider``
# ---------------------------
# The ``meshes_provider`` operator can be used to retrieve the mesh for several
# zones and time steps of the model. The behavior will differ depending on the
# inputs to the ``region_scoping`` pin. If no scoping is connected, the
# ``MeshedRegion`` for all body and face zones is retrieved in a ``MeshesContainer``.

meshes_all = dpf.operators.mesh.meshes_provider(streams_container=streams).eval()
print(meshes_all)

###############################################################################
# If the ``region_scoping`` pin is connected, the mesh extraction is restricted to
# the zone IDs contained in the input Scoping/list.

meshes_413 = dpf.operators.mesh.meshes_provider(
    streams_container=streams, region_scoping=[4, 13]
).eval()
print(meshes_413)
meshes_413.plot()
