# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
.. _ref_fluids_model:

Explore Fluids models
------------------------------------------------------

This example demonstrates how to explore Ansys Fluent and Ansys CFX models employing
the ``MeshInfo`` and ``ResultInfo``.

.. note::
    This example requires DPF 7.0 (ansys-dpf-server-2024-1-pre0) or above.
    For more information, see :ref:`ref_compatibility`.

"""

###############################################################################
# Exploring an Ansys Fluent model
# -------------------------------
# The first part of the example demonstrates how you can explore an Ansys Fluent
# model. Import the result file and create a model.

import ansys.dpf.core as dpf
from ansys.dpf.core import examples

path = examples.download_fluent_axial_comp()["flprj"]
ds = dpf.DataSources(path)
model = dpf.Model(data_sources=ds)


###############################################################################
# Exploring the mesh
# ~~~~~~~~~~~~~~~~~~
# Explore the mesh through the ``MeshInfo``. The ``MeshInfo`` provides metadata
# information about the mesh. For fluid models, it is useful to know the cell and
# face zones, as well as the topological relationships between them. First get all
# the available information in the ``MeshInfo`` .

minfo = model.metadata.mesh_info
print(minfo)

###############################################################################
# Then, get the bodies and their names in the model with the "body_names" ``StringField``,
# which provides a relationship between body IDs and names. In this model there are two
# bodies.

print(minfo.get_property("body_names"))

###############################################################################
# Each body is comprised of a set of cell zones. You can investigate the hierarchical
# relationship between bodies and cell zones through the "body_cell_topology"
# ``PropertyField``, which provides a relationship between the body IDs and the cell zone
# IDs. In this case, each body is only comprised of one cell zone.

print(minfo.get_property("body_cell_topology"))

###############################################################################
# Similarly, each body is limited by a set of face zones (generally representing
# boundary conditions). You can investigate the hierarchical relationship between
# bodies and face zones through the "body_face_topology" ``PropertyField``, which
# provides a relationship between the body IDs and the face zone IDs. In this case,
# each body is limited by several face zones.

print(minfo.get_property("body_face_topology"))

###############################################################################
# The cell and face zone IDs shown in the previous PropertyFields can be mapped
# to their names through the "body_zone_names" and "face_zone_names" ``PropertyField``.
# As in this model there is a 1-1 correspondence between bodies and cell zones,
# they have the same names and IDs.

print(minfo.get_property("cell_zone_names"))
print(minfo.get_property("face_zone_names"))

###############################################################################
# All zone names (regardless of them being cell or face zones) are exported to
# the "zone_names" ``StringField`` .

print(minfo.get_property("zone_names"))

###############################################################################
# Helpers are provided to quickly get a map of zone ID to zone name.
print(minfo.zones)
print(minfo.cell_zones)
print(minfo.face_zones)

###############################################################################
# As well as a map of body ID to body name.
print(minfo.bodies)

###############################################################################
# To facilitate the extraction of results, the body, cell and face zone ``Scoping``
# are extracted. They can be used to scope results.

print(minfo.get_property("body_scoping"))
print(minfo.get_property("cell_zone_scoping"))
print(minfo.get_property("face_zone_scoping"))

###############################################################################
# Exploring the results
# ~~~~~~~~~~~~~~~~~~~~~
# Explore the available results in the model through the ResultInfo. This is a Fluent model
# whose native results are exported to either the centroid of the elements (like
# Enthalpy or RMS Temperature), the centroid of the faces (like the Mass Flow Rate)
# or the centroid of both elements and faces (like Static Pressure).

rinfo = model.metadata.result_info
print(rinfo)

###############################################################################
# Each result holds more detailed information while explored individually. Enthalpy
# is a scalar magnitude exported to the centroids of the elements (cells). Thus, it is
# available for the two cell zones of the model (13 and 28). In addition, the model
# only has one phase, and therefore the result can only be extracted for "phase-1".

print(rinfo.available_results[0])

###############################################################################
# Static Pressure, however, is ElementalAndFaces, which means that it is exported
# at both the centroids of the cells and the centroids of the faces. Therefore, it is
# available for all the cell and face zones of the model.

print(rinfo.available_results[2])


###############################################################################
# Exploring an Ansys CFX model
# ----------------------------
# The second part of the example demonstrates how you can explore an Ansys CFX model.
# Import the result file and create a model.

path = examples.download_cfx_heating_coil()
ds = dpf.DataSources()
ds.set_result_file_path(path["cas"], "cas")
ds.add_file_path(path["dat"], "dat")
model = dpf.Model(data_sources=ds)

###############################################################################
# Exploring the mesh
# ~~~~~~~~~~~~~~~~~~
# If once again we explore the MeshInfo, we can see that the same information is
# readily available.

minfo = model.metadata.mesh_info
print(minfo)

###############################################################################
# In this CFX model there are also two bodies.

print(minfo.get_property("body_names"))

###############################################################################
# For this model, each body is conformed by several cell zones. In this general
# situation, the body ID corresponds to the highest cell zone ID of the one that
# comprises it.

print(minfo.get_property("body_cell_topology"))

###############################################################################
# You can also explore the face zone IDs in each body.

print(minfo.get_property("body_face_topology"))

###############################################################################
# The cell and face zone names are readily available.

print(minfo.get_property("cell_zone_names"))
print(minfo.get_property("face_zone_names"))

###############################################################################
# Exploring the results
# ~~~~~~~~~~~~~~~~~~~~~
# By exploring the ResultInfo we can see that all CFX variables are exported to
# the Nodes.

rinfo = model.metadata.result_info
print(rinfo)

###############################################################################
# However, in this model there are two distinct phases. To understand the phases
# at the model, you can explore the qualifiers of the ResultInfo. Thus, results
# could potentially be scoped on "zone" and "phase", with the ID and name of each
# phase shown below.

labels = rinfo.available_qualifier_labels
print(labels)
phase_names = rinfo.qualifier_label_support(labels[1]).string_field_support_by_property("names")
print(phase_names)

###############################################################################
# Each result holds more detailed information while explored individually. Static
# Pressure is only available for phase 1 ("<Mixture>"), and several cell and face
# zones.

print(rinfo.available_results[7])

###############################################################################
# Thermal conductivity, however, exists for phases 2 and 3 ("Copper" and "Water at 25 C",
# respectively), and several face and cell zones.

print(rinfo.available_results[4])
