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

# _order: 2
"""
.. _tutorials_custom_operators_and_plugins_python_plugin_for_custom_file_format:

Write a DPF Python plugin for a custom file format
====================================================

This tutorial shows how to implement a complete DPF Python plugin that reads
data from a custom binary or ASCII result file format.

The example uses a minimal ASCII format called *MyFormat* (``.myf``) that
stores harmonic analysis results for a single HEX8 element: nodal displacement
(vector, 3 components) and elemental temperature (scalar). Five operator
classes are required to make DPF aware of the format:

- **streams_provider** — opens the file and wraps it in a
  :class:`~ansys.dpf.core.streams_container.StreamsContainer`.
- **result_info_provider** — declares the available result quantities.
- **time_freq_support_provider** — describes the frequency axis.
- **mesh_provider** — builds the :class:`~ansys.dpf.core.meshed_region.MeshedRegion`.
- **result_provider** — reads one result field per frequency set.

All source files are provided under
:mod:`ansys.dpf.core.examples.python_plugins.my_format_plugin`.
"""

###############################################################################
# The custom file format
# ----------------------
#
# The ``.myf`` file is a plain-text format. Its structure is described below.
# A sample file ``cube_harmonic.myf`` ships with this tutorial.
#
# .. code-block:: text
#
#     ANALYSIS_TYPE harmonic
#     UNIT_SYSTEM   m_kg_s
#
#     FREQUENCIES
#       NUM_FREQS 2
#       1  100.0          # freq-set id  value [Hz]
#       2  200.0
#
#     NODES
#       NUM_NODES 8
#       1   0.0  0.0  0.0
#       ...                # id  x  y  z
#
#     ELEMENTS
#       NUM_ELEMENTS 1
#       1  HEX8  1 2 3 4 5 6 7 8   # id  cell_type  node_ids...
#
#     RESULT
#       name  displacement
#       location  NODAL
#       num_components  3
#       FREQ_ID 1
#         1   dx  dy  dz   # node_id  component_values
#         ...
#       FREQ_ID 2
#         ...
#
#     RESULT
#       name  temperature
#       location  ELEMENTAL
#       num_components  1
#       FREQ_ID 1
#         1   25.5         # elem_id  value
#       FREQ_ID 2
#         1   30.2
#

###############################################################################
# Step 1 — Parse the file
# -----------------------
#
# The parser lives in ``my_format_reader.py``. It exposes a ``read()`` function
# that returns a ``MyFormatModel`` dataclass: node coordinates, element
# connectivity, frequency list, and result data indexed by
# ``{freq_set_id: {entity_id: [values]}}``.
#
# .. code-block:: python
#
#     from dataclasses import dataclass, field
#     from typing import Dict, List
#
#     @dataclass
#     class MyFormatResult:
#         name: str
#         location: str          # "NODAL" or "ELEMENTAL"
#         num_components: int
#         data: Dict[int, Dict[int, List[float]]]  # freq_id -> entity_id -> values
#
#     @dataclass
#     class MyFormatModel:
#         analysis_type: str
#         unit_system: str
#         frequencies: Dict[int, float]            # freq_set_id -> Hz value
#         node_coords: Dict[int, List[float]]      # node_id -> [x, y, z]
#         elements: Dict[int, List[int]]           # elem_id -> node_ids
#         results: List[MyFormatResult]
#
#     def read(file_path: str) -> MyFormatModel:
#         """Parse a .myf file and return a MyFormatModel."""
#         ...
#

###############################################################################
# Step 2 — Implement the streams provider
# ----------------------------------------
#
# DPF looks for a ``{namespace}::stream_provider`` operator (singular) when a
# :class:`~ansys.dpf.core.data_sources.DataSources` with a matching ``key`` is
# passed to :class:`~ansys.dpf.core.model.Model`. The streams provider wraps the
# DataSources in a
# :class:`~ansys.dpf.core.streams_container.StreamsContainer` so that
# downstream operators can access the file path without re-parsing the
# DataSources.
#
# .. code-block:: python
#
#     from ansys.dpf.core.custom_operator import CustomOperatorBase
#     from ansys.dpf.core.streams_container import StreamsContainer
#     from ansys.dpf import core as dpf
#
#     class streams_provider(CustomOperatorBase):
#
#         @property
#         def name(self):
#             return "myformat::stream_provider"   # singular: stream_provider
#
#         def run(self):
#             ds: dpf.DataSources = self.get_input(4, dpf.DataSources)
#             sc = StreamsContainer(data_sources=ds)
#             self.set_output(0, sc)
#             self.set_succeeded()
#

###############################################################################
# Step 3 — Implement the result info provider
# --------------------------------------------
#
# ``result_info_provider`` reads the result metadata from the file and returns a
# :class:`~ansys.dpf.core.result_info.ResultInfo` object that lists the
# available result quantities (name, location, tensor nature, physical
# dimension).
#
# Operator pins follow the standard DPF convention: pin 3 accepts an optional
# :class:`~ansys.dpf.core.streams_container.StreamsContainer` (preferred when
# already open); pin 4 is the fallback :class:`~ansys.dpf.core.data_sources.DataSources`.
#
# .. code-block:: python
#
#     from ansys.dpf.core.available_result import Homogeneity
#     from ansys.dpf.core.result_info import analysis_types, physics_types
#
#     class result_info_provider(CustomOperatorBase):
#
#         @property
#         def name(self):
#             return "myformat::myformat::result_info_provider"
#
#         def run(self):
#             file_path = _get_file_path(self)       # helper: pin 3 or pin 4
#             model = reader.read(file_path)
#
#             result_info = dpf.ResultInfo(
#                 analysis_type=analysis_types.harmonic,
#                 physics_type=physics_types.mechanical,
#             )
#             for res in model.results:
#                 result_info.add_result(
#                     operator_name=f"myformat::{res.name}",
#                     scripting_name=res.name,
#                     homogeneity=Homogeneity.displacement,   # per result
#                     location=dpf.locations.nodal,           # per result
#                     nature=dpf.natures.vector,              # per result
#                     dimensions=[res.num_components],        # [3] for vector, [1] for scalar
#                     description=f"MyFormat result: {res.name}",
#                 )
#
#             self.set_output(0, result_info)
#             self.set_succeeded()
#

###############################################################################
# Step 4 — Implement the time-frequency support provider
# -------------------------------------------------------
#
# ``time_freq_support_provider`` builds a
# :class:`~ansys.dpf.core.time_freq_support.TimeFreqSupport` from the
# ``FREQUENCIES`` block. All frequency values are placed in a single harmonic
# step (step id 1) using  ``append_step``.
#
# .. code-block:: python
#
#     class time_freq_support_provider(CustomOperatorBase):
#
#         @property
#         def name(self):
#             return "myformat::myformat::time_freq_support_provider"
#
#         def run(self):
#             file_path = _get_file_path(self)
#             model = reader.read(file_path)
#
#             tfs = dpf.TimeFreqSupport()
#             freq_values = list(model.frequencies.values())  # plain list of floats
#             tfs.append_step(step_id=1, step_time_frequencies=freq_values)
#
#             self.set_output(0, tfs)
#             self.set_succeeded()
#

###############################################################################
# Step 5 — Implement the mesh provider
# -------------------------------------
#
# ``mesh_provider`` builds a
# :class:`~ansys.dpf.core.meshed_region.MeshedRegion` by iterating over the
# node and element data from the parsed model.
#
# .. code-block:: python
#
#     class mesh_provider(CustomOperatorBase):
#
#         @property
#         def name(self):
#             return "myformat::myformat::mesh_provider"
#
#         def run(self):
#             file_path = _get_file_path(self)
#             model = reader.read(file_path)
#
#             mesh = dpf.MeshedRegion()
#             mesh.unit = "m"
#
#             # Add nodes (id, [x, y, z])
#             for node_id, coords in model.node_coords.items():
#                 mesh.nodes.add_node(node_id, coords)
#
#             # Add elements: map 1-based node ids to 0-based node indices
#             node_ids = list(model.node_coords.keys())
#             node_index = {nid: idx for idx, nid in enumerate(node_ids)}
#             for elem_id, connectivity in model.elements.items():
#                 indices = [node_index[nid] for nid in connectivity]
#                 mesh.elements.add_solid_element(elem_id, indices)
#
#             self.set_output(0, mesh)
#             self.set_succeeded()
#

###############################################################################
# Step 6 — Implement the result providers
# ----------------------------------------
#
# Result operators follow a common base class ``_result_provider``. The base
# class handles reading the file and building the
# :class:`~ansys.dpf.core.fields_container.FieldsContainer`. Each concrete
# subclass only needs to declare its :attr:`name` property and a
# ``_result_name`` class attribute.
#
# The :class:`~ansys.dpf.core.fields_container.FieldsContainer` uses
# the label ``"time"`` to index fields by frequency-set id.
#
# .. code-block:: python
#
#     class _result_provider(CustomOperatorBase):
#         _result_name: str = ""          # override in subclass
#
#         def run(self):
#             file_path = _get_file_path(self)
#             try:
#                 time_scoping = self.get_input(0, int)  # optional pin 0
#             except DPFServerException:
#                 time_scoping = None
#
#             model = reader.read(file_path)
#             fc = _build_fields_container(model, self._result_name, time_scoping)
#             self.set_output(0, fc)
#             self.set_succeeded()
#
#
#     class displacement_provider(_result_provider):
#         _result_name = "displacement"
#
#         @property
#         def name(self):
#             return "myformat::myformat::displacement"
#
#
#     class temperature_provider(_result_provider):
#         _result_name = "temperature"
#
#         @property
#         def name(self):
#             return "myformat::myformat::temperature"
#

###############################################################################
# Step 7 — Declare the plugin entry-point
# ----------------------------------------
#
# DPF calls a function named ``load_operators(*args)`` when loading the plugin.
# It must call :func:`~ansys.dpf.core.custom_operator.record_operator` for
# every operator class defined in the plugin.
#
# The ``name`` argument passed to
# :func:`~ansys.dpf.core.core.load_library` (for example
# ``"py_my_format_plugin"``) tells DPF which Python file to import (here
# ``my_format_plugin.py``), so the entry-point file name and the ``name``
# argument must be consistent.
#
# .. code-block:: python
#
#     from ansys.dpf.core.custom_operator import record_operator
#     from streams_provider import streams_provider
#     from result_info_provider import result_info_provider
#     from time_freq_support_provider import time_freq_support_provider
#     from mesh_info_provider import mesh_info_provider
#     from mesh_provider import mesh_provider
#     from result_provider import displacement_provider, temperature_provider
#
#     def load_operators(*args):
#         record_operator(streams_provider, *args)
#         record_operator(result_info_provider, *args)
#         record_operator(time_freq_support_provider, *args)
#         record_operator(mesh_info_provider, *args)
#         record_operator(mesh_provider, *args)
#         record_operator(displacement_provider, *args)
#         record_operator(temperature_provider, *args)
#

###############################################################################
# Start a DPF gRPC server
# ------------------------
#
# Python plugins are only supported on gRPC servers. Start a dedicated local
# server to avoid interfering with any globally configured server.

import ansys.dpf.core as dpf

server = dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer, as_global=False)

###############################################################################
# Load the plugin
# ----------------
#
# :func:`~ansys.dpf.core.core.load_library` registers all operators declared in
# ``load_operators`` into the server registry.
#
# - The first argument is the **directory** containing the plugin source files.
# - The second argument ``"py_<module>"`` tells DPF to import the Python file
#   ``<module>.py`` from that directory (here ``my_format_plugin.py``).
# - The third argument is the entry-point function name inside that file.

from ansys.dpf.core.examples.python_plugins import my_format_plugin

dpf.load_library(
    filename=my_format_plugin.plugin_dir,
    name="py_my_format_plugin",
    symbol="load_operators",
    server=server,
    generate_operators=False,
)

available = dpf.dpf_operator.available_operator_names(server=server)
myformat_ops = sorted(op for op in available if op.startswith("myformat"))
print("Registered myformat operators:", myformat_ops)

###############################################################################
# Open the result file with :class:`~ansys.dpf.core.model.Model`
# ---------------------------------------------------------------
#
# Create a :class:`~ansys.dpf.core.data_sources.DataSources` pointing to the
# sample ``.myf`` file. The ``key`` argument identifies the result type.
# :meth:`~ansys.dpf.core.data_sources.DataSources.register_namespace` maps
# that key to the operator namespace, so DPF's generic dispatcher operators
# (``ResultInfoProvider``, ``TimeFreqSupportProvider``, ``mesh_provider``, …)
# know to look for ``myformat::myformat::result_info_provider`` etc.
#
# .. note::
#
#    The naming convention for all providers **except** ``stream_provider`` is
#    ``{namespace}::{key}::{operator_name}`` (two-level prefix). This mirrors
#    how C++ plugins register their operators — for example, the CGNS plugin
#    uses ``cgns::cgns::result_info_provider``. Only ``stream_provider`` uses a
#    single-level name (``myformat::stream_provider``) because the C++ generic
#    stream dispatcher looks it up differently.

my_ds = dpf.DataSources(server=server)
my_ds.set_result_file_path(str(my_format_plugin.sample_file), key="myformat")
my_ds.register_namespace(result_key="myformat", namespace="myformat")

my_model = dpf.Model(data_sources=my_ds, server=server)
print(my_model)

###############################################################################
# Inspect the result metadata and time-frequency support
# -------------------------------------------------------
#
# :attr:`~ansys.dpf.core.model.Model.metadata` exposes the
# :class:`~ansys.dpf.core.result_info.ResultInfo` and the
# :class:`~ansys.dpf.core.time_freq_support.TimeFreqSupport` through the
# standard DPF metadata pipeline.

result_info = my_model.metadata.result_info
print("Analysis type  :", result_info.analysis_type)
print("Number of results:", result_info.n_results)
for i in range(result_info.n_results):
    r = result_info.available_results[i]
    print(f"  [{i}] name={r.name!r:20s} location={r.native_location!r}")

tfs = my_model.metadata.time_freq_support
print("Number of frequency sets:", tfs.n_sets)
print("Frequencies [Hz]        :", tfs.time_frequencies.data)

###############################################################################
# Inspect the mesh
# -----------------
#
# :attr:`~ansys.dpf.core.model.Model.metadata` also provides the
# :class:`~ansys.dpf.core.meshed_region.MeshedRegion` through the
# ``meshed_region`` property.

mesh = my_model.metadata.meshed_region
print("Number of nodes   :", mesh.nodes.n_nodes)
print("Number of elements:", mesh.elements.n_elements)

###############################################################################
# Extract displacement results
# -----------------------------
#
# Result operators are called by their full ``{namespace}::{key}::{name}``
# scripting name. Connect the
# :class:`~ansys.dpf.core.data_sources.DataSources` on pin 4 and request the
# output :class:`~ansys.dpf.core.fields_container.FieldsContainer`.
# Use :meth:`~ansys.dpf.core.fields_container.FieldsContainer.get_label_space`
# to retrieve the frequency-set label of each field.

disp_op = dpf.Operator("myformat::myformat::displacement", server=server)
disp_op.connect(4, my_ds)
disp_fc = disp_op.get_output(0, dpf.FieldsContainer)

print(f"Displacement: {len(disp_fc)} fields")
for i in range(len(disp_fc)):
    label = disp_fc.get_label_space(i)
    field = disp_fc[i]
    print(
        f"  freq_set={label['time']:d}  "
        f"shape=({len(field.scoping)}, {field.component_count})  "
        f"first node: {field.get_entity_data(0)}"
    )

###############################################################################
# Extract temperature results
# ----------------------------
#
# The same pattern applies for the elemental scalar temperature result.

temp_op = dpf.Operator("myformat::myformat::temperature", server=server)
temp_op.connect(4, my_ds)
temp_fc = temp_op.get_output(0, dpf.FieldsContainer)

print(f"Temperature: {len(temp_fc)} fields")
for i in range(len(temp_fc)):
    label = temp_fc.get_label_space(i)
    field = temp_fc[i]
    print(f"  freq_set={label['time']:d}  element values = {field.data.flatten()}")
