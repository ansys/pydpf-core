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

# noqa: D400
"""
.. _ref_results_over_space:

Scope results over custom space domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :class:`Result <ansys.dpf.core.results.Result>` class, which are instances
created by the :class:`Model <ansys.dpf.core.model.Model>`, give
access to helpers for requesting results on specific mesh and time scopings.
With these helpers, working on a spatial subset of the model is straightforward.
In this example, different ways to choose the spatial subset to
evaluate a result are exposed

Import necessary modules:
"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create a model object to establish a connection with an example result file:
model = dpf.Model(examples.download_all_kinds_of_complexity())
print(model)

###############################################################################
# Choose specific nodes
# ~~~~~~~~~~~~~~~~~~~~~
# If some nodes or elements are specifically of interest, a nodal ``mesh_scoping``
# can be connected.

nodes_scoping = dpf.mesh_scoping_factory.nodal_scoping(range(400, 500))
print(nodes_scoping)

###############################################################################
# or
nodes_scoping = dpf.Scoping(ids=range(400, 500), location=dpf.locations.nodal)
print(nodes_scoping)

###############################################################################

disp = model.results.displacement.on_mesh_scoping(nodes_scoping).eval()

model.metadata.meshed_region.plot(disp)

###############################################################################
# Equivalent to:
disp_op = model.results.displacement()
disp_op.inputs.mesh_scoping(nodes_scoping)
disp = disp_op.outputs.fields_container()

###############################################################################
# Equivalent to:
disp = model.results.displacement(mesh_scoping=nodes_scoping).eval()

###############################################################################
# Choose specific elements
# ~~~~~~~~~~~~~~~~~~~~~~~~
# If some elements are specifically of interest, an elemental ``mesh_scoping``
# can be connected.

elements_scoping = dpf.mesh_scoping_factory.elemental_scoping(range(500, 5000))
print(elements_scoping)

# or
elements_scoping = dpf.Scoping(ids=range(500, 5000), location=dpf.locations.elemental)
print(elements_scoping)

volume = model.results.elemental_volume.on_mesh_scoping(elements_scoping).eval()

model.metadata.meshed_region.plot(volume)

###############################################################################
# Equivalent to:
volume_op = model.results.elemental_volume()
volume_op.inputs.mesh_scoping(elements_scoping)
volume = volume_op.outputs.fields_container()

###############################################################################
# Equivalent to:
volume = model.results.elemental_volume(mesh_scoping=elements_scoping).eval()

###############################################################################
# Choose specific named selections
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Named selections (also known as components) can be selected to create
# a spatial domain for a result. A ``mesh_scoping`` can be created with a
# named selection.
# To know the available named selections in the result file, use:

print(model.metadata.available_named_selections)

###############################################################################
# Get the ``mesh_scoping`` of a named selection:

mesh_scoping = model.metadata.named_selection("_CM82")
print(mesh_scoping)

###############################################################################
# Connect this ``mesh_scoping`` to the result provider
volume = model.results.elemental_volume(mesh_scoping=mesh_scoping).eval()
model.metadata.meshed_region.plot(volume)

###############################################################################
# Equivalent to:
volume = model.results.elemental_volume.on_named_selection("_CM82")

###############################################################################
# Equivalent to:
ns_provider = dpf.operators.scoping.on_named_selection(
    requested_location=dpf.locations.elemental,
    named_selection_name="_CM82",
    data_sources=model,
)
volume = model.results.elemental_volume(mesh_scoping=ns_provider).eval()

###############################################################################
# Split results depending on spatial properties
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# For many applications, it can be useful to request results on different subsets
# of the model. The ``ScopingsContainer`` entity contains different ``Scopings``
# and can be connected to any result provider to get results split with the
# same partition as the input ``ScopingsContainer``.
# For example, some application require to get results split by body, by material,
# by element types. It might also be necessary to get results by element shape
# types, such as shell, solid, or beam, to average data properly.
# Customers might also require split by entirely custom spatial domains.


###############################################################################
# Split results by element shapes
stress = model.results.stress.split_by_shape.on_location(dpf.locations.nodal).eval()
print(stress)

shell_stresses = stress.shell_fields()
model.metadata.meshed_region.plot(shell_stresses[0])

solid_stresses = stress.solid_fields()
model.metadata.meshed_region.plot(solid_stresses[0])

###############################################################################
# Split results by bodies
stress = model.results.stress.split_by_body.on_location(dpf.locations.nodal).eval()
print(stress)

for body_id in stress.get_mat_scoping().ids:
    fields = stress.get_fields_by_mat_id(body_id)
    for field in fields:
        if field.elementary_data_count > 0:
            model.metadata.meshed_region.plot(field)

###############################################################################
# Create a custom spatial split
scopings_container = dpf.ScopingsContainer()
scopings_container.add_label("custom_split")
scopings_container.add_scoping(
    {"custom_split": 1},
    dpf.Scoping(ids=range(100, 500), location=dpf.locations.elemental),
)
scopings_container.add_scoping(
    {"custom_split": 2},
    dpf.Scoping(ids=range(500, 5000), location=dpf.locations.elemental),
)

###############################################################################
elemental_stress = model.results.stress.on_location(dpf.locations.elemental)(
    mesh_scoping=scopings_container
).eval()
print(elemental_stress)

for field in elemental_stress:
    model.metadata.meshed_region.plot(field)
