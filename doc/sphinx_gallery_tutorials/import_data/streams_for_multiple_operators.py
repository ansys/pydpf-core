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

# _order: 6
"""
.. _ref_tutorials_import_data_streams_for_multiple_operators:

Speed up data requests from files using streams
================================================

Reduce I/O overhead when extracting multiple results from the same file by
opening it once and reusing cached metadata through a streams container.

Extracting data from result files is I/O intensive. Every time you open a
file, read some data, and close it again, the DPF server must re-parse the
file header, rebuild its metadata catalog, and reload the mesh from disk.
When you repeat this cycle for every result in a loop (for example iterating
over all entries in the
:class:`ResultInfo<ansys.dpf.core.result_info.ResultInfo>`), the cumulative
cost can dominate the total runtime, especially on large models.

DPF addresses this by letting you open the file once and cache its metadata
and mesh structure on the server side. A
:class:`StreamsContainer<ansys.dpf.core.streams_container.StreamsContainer>`
is the object that holds those open file handles and the cached data for the
lifetime of the container. All operators that receive the same
``StreamsContainer`` reuse those handles and skip the repeated open-parse-load
cycle.

This tutorial compares the ``DataSources``-per-operator approach against the
``StreamsContainer`` approach on the same set of result requests and explains
when each approach is appropriate.

.. note::

    For a gentler introduction to importing result files and the difference
    between ``DataSources`` and ``Model``, see
    :ref:`ref_tutorials_import_result_file`.
"""
###############################################################################
# Setup
# -----
#
# Import the required modules and locate the example result file.

import time

# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf

# Import the operators and examples module
from ansys.dpf.core import examples, operators as ops

# Locate the example MAPDL static result file
result_file = examples.find_static_rst()

###############################################################################
# Get the list of available results
# ---------------------------------
#
# Use a :class:`Model<ansys.dpf.core.model.Model>` to query which result
# operators this file exposes. The ``available_results`` property of the
# :class:`ResultInfo<ansys.dpf.core.result_info.ResultInfo>` object returns one
# entry per available result, each carrying the ``operator_name`` needed to
# instantiate the corresponding DPF operator.

# Create a Model to access file metadata
my_model = dpf.Model(data_sources=result_file)

# Retrieve the list of available result descriptors
available_results = my_model.metadata.result_info.available_results

# Print the name of each available result
print(f"Number of available results: {len(available_results)}")
for res in available_results:
    print(f"  {res.name}")

###############################################################################
# Read all results using ``DataSources``
# --------------------------------------
#
# Create a :class:`DataSources<ansys.dpf.core.data_sources.DataSources>` object
# and pass it as the ``data_sources`` argument to each result operator constructor.
# Each operator is instantiated fresh, so the DPF server opens the file, parses
# its header, loads the mesh, and extracts the result data independently for
# every call, only to repeat the entire sequence for the next operator.

# Create the DataSources object
ds = dpf.DataSources(result_path=result_file)

# Measure elapsed time for the DataSources approach
t_start = time.perf_counter()

n_evaluated_ds = 0
n_skipped_ds = 0
for res in available_results:
    # Use the operator constructor from ops.result, passing the DataSources directly
    result_op = getattr(ops.result, res.name)(data_sources=ds)
    try:
        result_op.eval()
        n_evaluated_ds += 1
    except Exception:
        # Some operators may not produce a FieldsContainer for this file type
        # (for example, element-orientation operators return a MeshedRegion)
        n_skipped_ds += 1

t_data_sources = time.perf_counter() - t_start
print(
    f"DataSources approach: {n_evaluated_ds} results in {t_data_sources:.2f} s ({n_skipped_ds} skipped)"
)

###############################################################################
# Read all results using a ``StreamsContainer``
# ---------------------------------------------
#
# Create a ``streams_provider`` operator from the same
# :class:`DataSources<ansys.dpf.core.data_sources.DataSources>` object.
# Evaluating it returns a
# :class:`StreamsContainer<ansys.dpf.core.streams_container.StreamsContainer>`
# that holds open file handles on the DPF server.
#
# Pass this ``StreamsContainer`` as the ``streams_container`` argument to each
# result operator constructor. On the first operator call the server parses the
# file header and loads the mesh; on every subsequent call that data is served
# from the cache; no further disk access is required for it.

# Create the streams_provider operator and get its StreamsContainer output
streams_op = ops.metadata.streams_provider(data_sources=ds)
sc = streams_op.outputs.streams_container()

# Measure elapsed time for the StreamsContainer approach
t_start = time.perf_counter()

n_evaluated_sc = 0
n_skipped_sc = 0
for res in available_results:
    # Use the operator constructor from ops.result, passing the StreamsContainer
    result_op = getattr(ops.result, res.name)(streams_container=sc)
    try:
        result_op.eval()
        n_evaluated_sc += 1
    except Exception:
        n_skipped_sc += 1

t_streams = time.perf_counter() - t_start
print(
    f"StreamsContainer approach: {n_evaluated_sc} results in {t_streams:.2f} s ({n_skipped_sc} skipped)"
)

###############################################################################
# Compare elapsed times
# ---------------------
#
# Both approaches produce identical results. The difference is purely in
# performance: the ``StreamsContainer`` eliminates the per-operator cost of
# opening the file and loading the mesh.

print(f"\nDataSources  : {t_data_sources:.2f} s")
print(f"StreamsContainer: {t_streams:.2f} s")
if t_streams > 0:
    print(f"Speed-up factor : {t_data_sources / t_streams:.1f}x")

# The speedup factor above is modest because the example file shipped with
# this repository is a small benchmark model. On large production models
# (where the mesh can be millions of nodes and the file several gigabytes),
# the gain from using a ``StreamsContainer`` can reach **20x or even 100x**,
# because every avoided file-open-and-mesh-load cycle saves proportionally
# more time. The measurement here is only intended to confirm that an
# improvement exists; the magnitude you observe in practice depends on your
# model size and the number of result requests.

###############################################################################
# Why is the ``StreamsContainer`` faster?
# ----------------------------------------
#
# When a result operator receives a ``DataSources`` object, the DPF server
# follows this sequence for every evaluation:
#
# 1. Open the result file and read its header.
# 2. Parse metadata (unit system, result catalog, time steps).
# 3. Load the mesh.
# 4. Read and return the requested result data.
# 5. Release local references to the open file.
#
# When a result operator receives a ``StreamsContainer`` instead, steps 1–3
# are performed only **once**, the first time any operator requests data from
# that container. All subsequent operators share the already-open handles and
# the cached mesh, so only step 4 is repeated.
#
# The benefit grows with the number of operators: a loop over all N results in
# the file saves N − 1 full file-open-and-mesh-load cycles.

###############################################################################
# The ``Model`` already uses streams for you
# -------------------------------------------
#
# When you create a :class:`Model<ansys.dpf.core.model.Model>`, it internally
# instantiates a ``streams_provider`` operator and stores it as
# ``model.metadata.streams_provider``. The ``StreamsContainer`` produced by
# that operator is automatically wired into every operator the ``Model`` creates:
# the mesh provider, the result info provider, and all result operators
# accessible via ``model.results``.
#
# This is why the ``Model`` helper is efficient out of the box: it uses streams
# without any additional user action. The streams provider used by the model
# in this tutorial is shown below.

# Access the streams_provider operator held by the Model
model_streams_op = my_model.metadata.streams_provider
print("Model streams provider operator:", model_streams_op)

# The StreamsContainer it holds is equivalent to the one created manually above
model_sc = model_streams_op.outputs.streams_container()
print("Model StreamsContainer:", model_sc)

###############################################################################
# When **not** to use streams
# ----------------------------
#
# The ``StreamsContainer`` caching behaviour is a default-on feature, but there
# are situations where you should connect ``DataSources`` directly instead.
#
# **Debugging custom operators or plugins**
#   When developing a custom result reader and verifying that each operator
#   call reads fresh data, caching can mask regressions. Using ``DataSources``
#   directly guarantees that every evaluation goes back to disk, so the
#   behaviour you observe matches what end users with a cold cache will see.
#
# **Files modified between evaluations**
#   If another process (such as a live solver) is updating the result file
#   while you are reading it, keeping a ``StreamsContainer`` open may either
#   prevent the writer from writing (file-lock conflict on Windows) or return
#   stale cached data that does not reflect the latest solver output. Use
#   ``DataSources`` in such scenarios so that each evaluation opens a
#   fresh connection to the file.
#
# **Memory-constrained environments**
#   The ``StreamsContainer`` keeps the mesh and file handles alive on the DPF
#   server for its entire lifetime. For very large models, this reservation may
#   exhaust server memory. Connecting ``DataSources`` directly allows the server
#   to release mesh data between evaluations.
#
# **Single one-off evaluations**
#   If you only need to extract one result once, the overhead of creating a
#   ``streams_provider`` operator is not justified. ``DataSources`` is simpler
#   and equally fast for a single request.
#
# You can also release an existing ``StreamsContainer``'s file handles
# explicitly when you no longer need them, without destroying the container
# itself:

# Release open file handles held by the StreamsContainer
sc.release_handles()
print("File handles released from the StreamsContainer.")
