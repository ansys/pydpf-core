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

# _order: 8
"""
.. _ref_tutorials_import_data_data_sources_upstream:

Connect DataSources for multi-analysis results
================================================

Learn when to attach files directly and when to connect an upstream |DataSources|.

A |DataSources| object is a set of files from one analysis. An upstream
|DataSources| represents a prior analysis whose results are needed by a
downstream analysis. This distinction is important for modal superposition
(MSUP), where a harmonic response uses a modal result from an earlier analysis.

This tutorial shows the flat pattern that users often try first, the correct
upstream chain, and the special case where the downstream harmonic working
directory also contains a ``.mode`` restart file.

.. seealso::

    :ref:`ref_tutorials_import_data_data_sources_basics`
        Learn the DataSources basics before connecting analyses.
    :ref:`ref_msup`
        See the existing MSUP example using the same upstream mechanism.
"""
###############################################################################
# Download the MSUP result files
# ------------------------------
#
# The example helper returns one harmonic response file and the files from its
# upstream modal analysis.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# Download an MSUP result set that can run in CI
msup_files = examples.download_msup_files_to_dict()

###############################################################################
# The flat pattern to avoid
# -------------------------
#
# ``add_file_path()`` groups files that belong to one analysis. Adding the
# modal files directly to the harmonic DataSources loses the relationship
# between the downstream harmonic analysis and its upstream modal analysis.
# Keep this pattern as a reference only; do not use it to create the Model.

# This is the flat pattern users often try first
flat_data_sources = dpf.DataSources()
flat_data_sources.set_result_file_path(filepath=msup_files["rfrq"], key="rfrq")
flat_data_sources.add_file_path(filepath=msup_files["mode"], key="mode")
flat_data_sources.add_file_path(filepath=msup_files["rst"], key="rst")

###############################################################################
# Build the upstream relationship
# -------------------------------
#
# Use ``add_file_path()`` for files from one analysis. Use ``add_upstream()``
# when the files come from a prior analysis that the downstream result needs.

# Create the downstream harmonic DataSources
downstream_data_sources = dpf.DataSources(result_path=msup_files["rfrq"], key="rfrq")

# Create the upstream modal DataSources
upstream_data_sources = dpf.DataSources(result_path=msup_files["mode"], key="mode")
upstream_data_sources.add_file_path(filepath=msup_files["rst"], key="rst")

# Connect the modal analysis as upstream data for the harmonic analysis
downstream_data_sources.add_upstream(upstream_data_sources=upstream_data_sources)

###############################################################################
# Evaluate a harmonic result
# --------------------------
#
# After the relationship is defined, use the downstream DataSources with a
# Model. DPF reads the harmonic response and expands it with the upstream mode
# shapes using the same result request syntax as other analyses.

# Create a Model from the downstream DataSources
my_model = dpf.Model(data_sources=downstream_data_sources)

# Evaluate displacement for every harmonic frequency
displacement_fc = my_model.results.displacement.on_all_time_freqs.eval()
print("Expanded displacement:", displacement_fc)

###############################################################################
# Handle a modal restart file in the downstream analysis
# -------------------------------------------------------
#
# A modal restart in a harmonic analysis can produce two ``.mode`` files: the
# upstream modal file and another ``.mode`` file in the downstream harmonic
# working directory. The downstream file belongs to the downstream
# DataSources, while the prior-analysis files remain in the upstream object.
#
# The download helper used above contains only one ``.mode`` file, so the
# following guarded snippet shows the API call without inventing a second test
# asset. In a Mechanical workflow, replace the path with the downstream
# working-directory file before evaluating the Model.

# The downstream restart mode file belongs to the downstream DataSources
harmonic_restart_mode_path = "path/to/harmonic-working-directory/file.mode"
# downstream_data_sources.add_file_path(
#     filepath=harmonic_restart_mode_path,
#     key="mode",
# )
