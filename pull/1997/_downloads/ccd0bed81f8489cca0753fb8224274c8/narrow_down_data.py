# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

# _order: 5
"""
.. _ref_tutorials_narrow_down_data:

Narrow down data
=================

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

This tutorial explains how to scope your results over time and mesh domains.
"""
###############################################################################
# Understanding the scope
# -----------------------
#
# To begin the workflow setup, you need to establish the ``scoping``, that is
# a spatial and/or temporal subset of the simulation data.
#
# The data in DPF is represented by a
# :class:`Field<ansys.dpf.core.field.Field>`. Thus, narrowing down your results
# means scoping your ``Field``. To do so in DPF, you use the
# :class:`Scoping<ansys.dpf.core.scoping.Scoping>` object. You can retrieve all
# the time steps available for a result, but you can also filter them.
#
# .. note::
#
#     Scoping is important because when DPF-Core returns the ``Field`` object,
#     what Python actually has is a client-side representation of the ``Field``,
#     not the entirety of the ``Field`` itself. The most efficient way of
#     interacting with result data is to minimize the exchange of data between
#     Python and DPF, either by using operators or by accessing exclusively the
#     data that is needed. For more information on the DPF data storage structures
#     see :ref:`ref_tutorials_data_structures`.
#
# In conclusion, the essence of a scoping is to specify a set of time or mesh
# entities by defining a range of IDs:
#
# .. image:: ../../images/drawings/scoping-eg.png
#    :align: center

###############################################################################
# Import the PyDPF-Core modules
# ------------------------------

# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf

###############################################################################
# .. _ref_create_scoping_instance_object:
#
# Create a ``Scoping`` from scratch — instantiate the ``Scoping`` class
# ----------------------------------------------------------------------
#
# Create a **time** ``Scoping`` and a **mesh** ``Scoping`` by instantiating the
# :class:`Scoping<ansys.dpf.core.scoping.Scoping>` object. Use the ``ids`` and
# ``location`` arguments to give the entities ids and location of interest.
#
# **Time scoping** — use a ``'time_freq'`` location and target time sets by their ids.

time_list_1 = [14, 15, 16, 17]
time_scoping_1 = dpf.Scoping(ids=time_list_1, location=dpf.locations.time_freq)

###############################################################################
# **Mesh scoping** — use a nodal location and target nodes by their ids.

nodes_ids_1 = [103, 204, 334, 1802]
mesh_scoping_1 = dpf.Scoping(ids=nodes_ids_1, location=dpf.locations.nodal)

###############################################################################
# .. _ref_create_scoping_scoping_factory:
#
# Create a ``Scoping`` using the scoping factory modules
# -------------------------------------------------------
#
# Use the :mod:`time_freq_scoping_factory<ansys.dpf.core.time_freq_scoping_factory>`
# module for a temporal ``Scoping`` and the
# :mod:`mesh_scoping_factory<ansys.dpf.core.mesh_scoping_factory>` module for a
# spatial ``Scoping``.
#
# **Time scoping** — use the
# :func:`scoping_by_sets()<ansys.dpf.core.time_freq_scoping_factory.scoping_by_sets>`
# function to create a ``Scoping`` over multiple time sets.

time_list_2 = [14, 15, 16, 17]
time_scoping_2 = dpf.time_freq_scoping_factory.scoping_by_sets(cumulative_sets=time_list_2)

###############################################################################
# **Mesh scoping** — use the
# :func:`nodal_scoping()<ansys.dpf.core.mesh_scoping_factory.nodal_scoping>`
# function to create a nodal mesh ``Scoping``.

nodes_ids_2 = [103, 204, 334, 1802]
mesh_scoping_2 = dpf.mesh_scoping_factory.nodal_scoping(node_ids=nodes_ids_2)

###############################################################################
# Define the objects needed to extract Scopings
# ----------------------------------------------
#
# Import a result file and create a ``Model``. For this tutorial, use one available
# in the :mod:`examples<ansys.dpf.core.examples>` module. For more information about
# how to import your own result file in DPF, see the
# :ref:`ref_tutorials_import_result_file` tutorial.

# Import the operators and examples module
from ansys.dpf.core import examples, operators as ops

# Define the result file path
result_file_path_1 = examples.download_transient_result()

# Create the DataSources object
ds_1 = dpf.DataSources(result_path=result_file_path_1)

# Create the model
model_1 = dpf.Model(data_sources=ds_1)

###############################################################################
# Extract the mesh (``MeshedRegion``), a ``FieldsContainer`` with displacement
# results, and a single ``Field``.

# Get the MeshedRegion
meshed_region_1 = model_1.metadata.meshed_region

# Get a FieldsContainer with the displacement results
disp_fc = model_1.results.displacement.on_all_time_freqs.eval()

# Get a Field from the FieldsContainer
disp_field = disp_fc[0]

###############################################################################
# Extract the time ``Scoping``
# ----------------------------
#
# Extracting the time ``Scoping`` means extracting the scoping of the time
# frequencies from the ``TimeFreqSupport`` of a DPF object.
#
# **From the** ``Model``
#
# Access the ``TimeFreqSupport`` via the model metadata, then get the time
# frequencies ``Field`` and extract its scoping.

tfs_1 = model_1.metadata.time_freq_support
t_freqs_1 = tfs_1.time_frequencies
time_scop_1 = t_freqs_1.scoping
print(time_scop_1)

###############################################################################
# **From the** ``FieldsContainer``

tfs_2 = disp_fc.time_freq_support
t_freqs_2 = tfs_2.time_frequencies
time_scop_2 = t_freqs_2.scoping
print(time_scop_2)

###############################################################################
# **From the** ``Field``

tfs_3 = disp_field.time_freq_support
t_freqs_3 = tfs_1.time_frequencies
time_scop_3 = t_freqs_3.scoping
print(time_scop_3)

###############################################################################
# Extract the mesh ``Scoping``
# ----------------------------
#
# **From the** ``MeshedRegion``
#
# Use the :class:`from_mesh<ansys.dpf.core.operators.scoping.from_mesh.from_mesh>`
# operator to get the ``Scoping`` for the entire mesh. It returns a nodal scoping
# by default; use the ``requested_location`` argument for an elemental scoping.

mesh_scoping_3 = ops.scoping.from_mesh(mesh=meshed_region_1).eval()
print("Scoping from mesh:", "\n", mesh_scoping_3, "\n")

###############################################################################
# Use the
# :func:`MeshedRegion.elements<ansys.dpf.core.meshed_region.MeshedRegion.elements>`
# method and then
# :func:`Elements.scoping<ansys.dpf.core.elements.Elements.scoping>` to get an
# elemental ``Scoping``.

mesh_scoping_4 = meshed_region_1.elements.scoping
print("Scoping from mesh elements:", "\n", mesh_scoping_4, "\n")

###############################################################################
# Use the
# :func:`MeshedRegion.nodes<ansys.dpf.core.meshed_region.MeshedRegion.nodes>`
# method and then
# :func:`Nodes.scoping<ansys.dpf.core.nodes.Nodes.scoping>` to get a nodal
# ``Scoping``.

mesh_scoping_5 = meshed_region_1.nodes.scoping
print("Scoping from mesh nodes:", "\n", mesh_scoping_5, "\n")

###############################################################################
# **From the** ``FieldsContainer``
#
# Use the
# :class:`extract_scoping<ansys.dpf.core.operators.utility.extract_scoping.extract_scoping>`
# operator. This operator gets the mesh ``Scoping`` for each ``Field`` in the
# ``FieldsContainer``, returning a ``ScopingsContainer``.

extract_scop_fc_op = ops.utility.extract_scoping(field_or_fields_container=disp_fc)
mesh_scoping_6 = extract_scop_fc_op.outputs.mesh_scoping_as_scopings_container()
print("Scoping from FieldsContainer:", "\n", mesh_scoping_6, "\n")

###############################################################################
# **From the** ``Field``
#
# Use the
# :class:`extract_scoping<ansys.dpf.core.operators.utility.extract_scoping.extract_scoping>`
# operator or the
# :func:`Field.scoping<ansys.dpf.core.field_base._FieldBase.scoping>` method.

mesh_scoping_7 = ops.utility.extract_scoping(field_or_fields_container=disp_field).eval()
print("Scoping from Field (operator):", "\n", mesh_scoping_7, "\n")

mesh_scoping_8 = disp_field.scoping
print("Scoping from Field (method):", "\n", mesh_scoping_8, "\n")

###############################################################################
# .. _ref_use_scoping_when_extracting:
#
# Extract and scope the results
# ------------------------------
#
# Apply a ``Scoping`` when extracting a result using the
# :func:`Model.results<ansys.dpf.core.model.Model.results>` method or the result
# operator inputs. Pass the ``Scoping`` objects to the ``time_scoping`` and
# ``mesh_scoping`` arguments.

# Extract and scope using Model.results
disp_model = model_1.results.displacement(
    time_scoping=time_scoping_1, mesh_scoping=mesh_scoping_1
).eval()

# Extract and scope using the result.displacement operator
disp_op = ops.result.displacement(
    data_sources=ds_1, time_scoping=time_scoping_1, mesh_scoping=mesh_scoping_1
).eval()

print("Displacement from Model.results:", "\n", disp_model, "\n")
print("Displacement from result.displacement operator:", "\n", disp_op, "\n")

###############################################################################
# .. _ref_use_scoping_after_extracting:
#
# Extract and rescope the results
# ---------------------------------
#
# Change the mesh ``Scoping`` after result extraction or manipulation using the
# :class:`rescope<ansys.dpf.core.operators.scoping.rescope.rescope>` operator.
# It takes a ``Field`` or ``FieldsContainer`` and rescopes it to the given
# ``Scoping``.

# Extract the results for the entire mesh
disp_all_mesh = model_1.results.displacement.eval()

# Rescope the displacement results to a specific set of nodes
disp_rescope = ops.scoping.rescope(fields=disp_all_mesh, mesh_scoping=mesh_scoping_1).eval()

print("Displacement results for the entire mesh:", "\n", disp_all_mesh, "\n")
print("Displacement results rescoped:", "\n", disp_rescope, "\n")
