# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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
.. _ref_distributed_files:

Read results from distributed files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solvers usually solve analysis with distributed architecture. In this
case, one file is written by spatial or temporal domains. DPF is capable
of reading one result in distributed files. This allows it to skip the
merging of files on the solver side, which is time-consuming and
often doubles the memory used.
"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create the data sources
# ~~~~~~~~~~~~~~~~~~~~~~~
# First create a data sources with one result file by domain

distributed_file_path = examples.download_distributed_files()
data_sources = dpf.DataSources()
data_sources.set_domain_result_file_path(distributed_file_path[0], 0)
data_sources.set_domain_result_file_path(distributed_file_path[1], 1)

###############################################################################
# Compute displacements
# ~~~~~~~~~~~~~~~~~~~~~
# Once the file architecture is put in the data sources,
# computing displacements with or without domain has the exact same syntax.
# DPF reads parts of the result on each domain and merges these results in
# the outputs fields. The output is no different than when using combined
# or distributed files.

model = dpf.Model(data_sources)
disp = model.results.displacement.on_all_time_freqs.eval()

freq_scoping = disp.get_time_scoping()
for freq_set in freq_scoping:
    model.metadata.meshed_region.plot(disp.get_field_by_time_complex_ids(freq_set, 0))

###############################################################################
# Compute equivalent stress
# ~~~~~~~~~~~~~~~~~~~~~~~~~
stress_res = model.results.stress
stress_res.on_location(dpf.locations.nodal)
stress = stress_res.on_all_time_freqs.eval()

freq_scoping = stress.get_time_scoping()
for freq_set in freq_scoping:
    model.metadata.meshed_region.plot(stress.get_field_by_time_complex_ids(freq_set, 0))
