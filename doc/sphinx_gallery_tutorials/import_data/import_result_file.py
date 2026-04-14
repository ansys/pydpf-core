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
.. _ref_tutorials_import_result_file:

Import a result file in DPF
============================

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

This tutorial shows how to import a result file in DPF.

There are two approaches to import a result file in DPF:

- Using the :class:`DataSources<ansys.dpf.core.data_sources.DataSources>` object
- Using the :class:`Model<ansys.dpf.core.model.Model>` object

.. note::

    The ``Model`` extracts a large amount of information by default (results, mesh, and
    analysis data). If using this helper takes a long time to process, consider using a
    ``DataSources`` object and instantiating operators directly with it.

.. seealso::

    :ref:`ref_tutorials_import_data_streams_for_multiple_operators`
        When running multiple operators directly against the same file, use a
        ``StreamsContainer`` to replicate the performance benefit that ``Model``
        provides internally.
"""
###############################################################################
# Import the PyDPF-Core modules
# -----------------------------

# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf

# Import the operators and examples module
from ansys.dpf.core import examples, operators as ops

###############################################################################
# MAPDL result files
# ------------------
#
# Define the MAPDL result file paths
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# **a) ``.rst`` result file**

result_file_path_11 = examples.find_static_rst()
print("Result file path 11:", "\n", result_file_path_11, "\n")

###############################################################################
# **b) ``.mode``, ``.rfrq`` and ``.rst`` result files (modal superposition)**
#
# In the modal superposition, modal coefficients are multiplied by mode shapes (of a
# previous modal analysis) to analyse a structure under given boundary conditions in a
# range of frequencies. Doing this expansion "on demand" in DPF instead of in the solver
# reduces the size of the result files.

result_file_path_12 = examples.download_msup_files_to_dict()
print("Result files paths 12:", "\n", result_file_path_12, "\n")

###############################################################################
# Use a ``DataSources`` for MAPDL files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# The :class:`DataSources<ansys.dpf.core.data_sources.DataSources>` object manages
# paths to result files. Use it to declare data inputs for PyDPF-Core APIs.
#
# **a) ``.rst`` result file** — pass the result file path directly.

ds_11 = dpf.DataSources(result_path=result_file_path_11)

###############################################################################
# **b) ``.mode``, ``.rfrq`` and ``.rst`` result files**
#
# The expansion is recursive in DPF: first the modal response is read, then *upstream*
# mode shapes are found in the ``DataSources``. To create a recursive workflow, add an
# upstream ``DataSources`` object containing the upstream data files to the main
# ``DataSources`` object.

ds_12 = dpf.DataSources()
ds_12.set_result_file_path(filepath=result_file_path_12["rfrq"], key="rfrq")

upstream_ds_12 = dpf.DataSources(result_path=result_file_path_12["mode"])
upstream_ds_12.add_file_path(filepath=result_file_path_12["rst"])

ds_12.add_upstream(upstream_data_sources=upstream_ds_12)

###############################################################################
# Use a ``Model`` for MAPDL files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# The :class:`Model<ansys.dpf.core.model.Model>` class creates and evaluates common
# readers for the files it is given, such as a mesh provider, a result info provider,
# and a streams provider. Provide either a result file path or a ``DataSources`` object
# to its ``data_sources`` argument.
#
# **a) ``.rst`` result file**

model_11 = dpf.Model(data_sources=result_file_path_11)
model_12 = dpf.Model(data_sources=ds_11)

###############################################################################
# **b) ``.mode``, ``.rfrq`` and ``.rst`` result files**

model_13 = dpf.Model(data_sources=ds_12)

###############################################################################
# LS-DYNA result files
# --------------------
#
# Define the LS-DYNA result file paths
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# **a) ``.d3plot`` result file**
#
# The d3plot file does not contain unit information. When the simulation was run
# through Mechanical, a ``file.actunits`` file is produced and must be supplied to
# get correct units.

result_file_path_21 = examples.download_d3plot_beam()
print("Result files paths 21:", "\n", result_file_path_21, "\n")

###############################################################################
# **b) ``.binout`` result file**

result_file_path_22 = examples.download_binout_matsum()
print("Result file path 22:", "\n", result_file_path_22, "\n")

###############################################################################
# Use a ``DataSources`` for LS-DYNA files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# **a) ``.d3plot`` result file** — use
# :func:`set_result_file_path()<ansys.dpf.core.data_sources.DataSources.set_result_file_path>`
# and
# :func:`add_file_path()<ansys.dpf.core.data_sources.DataSources.add_file_path>`
# to add the main and the units file.

ds_21 = dpf.DataSources()
ds_21.set_result_file_path(filepath=result_file_path_21[0], key="d3plot")
ds_21.add_file_path(filepath=result_file_path_21[3], key="actunits")

###############################################################################
# **b) ``.binout`` result file** — the extension key is not explicit in the file name,
# so provide the ``key`` argument explicitly.

ds_22 = dpf.DataSources()
ds_22.set_result_file_path(filepath=result_file_path_22, key="binout")

###############################################################################
# Use a ``Model`` for LS-DYNA files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

model_21 = dpf.Model(data_sources=ds_21)
model_22 = dpf.Model(data_sources=ds_22)

###############################################################################
# Fluent result files
# -------------------
#
# Define the Fluent result file paths
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# **a) ``.flprj`` result file**

result_file_path_31 = examples.download_fluent_axial_comp()["flprj"]
print("Result file path 31:", "\n", result_file_path_31, "\n")

###############################################################################
# **b) ``.cas.h5`` / ``.dat.h5`` result files**

result_file_path_32 = examples.download_fluent_axial_comp()
print("Result files paths 32:", "\n", result_file_path_32, "\n")

###############################################################################
# Use a ``DataSources`` for Fluent files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# **a) ``.flprj`` result file** — pass the result file path directly.

ds_31 = dpf.DataSources(result_path=result_file_path_31)

###############################################################################
# **b) ``.cas.h5`` / ``.dat.h5`` result files** — use
# :func:`set_result_file_path()<ansys.dpf.core.data_sources.DataSources.set_result_file_path>`
# and
# :func:`add_file_path()<ansys.dpf.core.data_sources.DataSources.add_file_path>`
# with the first extension key explicitly.

ds_32 = dpf.DataSources()
ds_32.set_result_file_path(filepath=result_file_path_32["cas"][0], key="cas")
ds_32.add_file_path(filepath=result_file_path_32["dat"][0], key="dat")

###############################################################################
# Use a ``Model`` for Fluent files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

model_31 = dpf.Model(data_sources=result_file_path_31)
model_32 = dpf.Model(data_sources=ds_31)
model_33 = dpf.Model(data_sources=ds_32)

###############################################################################
# CFX result files
# ----------------
#
# Define the CFX result file paths
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# **a) ``.res`` result file**

result_file_path_41 = examples.download_cfx_mixing_elbow()
print("Result file path 41:", "\n", result_file_path_41, "\n")

###############################################################################
# **b) ``.cas.cff`` / ``.dat.cff`` result files**

result_file_path_42 = examples.download_cfx_heating_coil()
print("Result files paths 42:", "\n", result_file_path_42, "\n")

###############################################################################
# Use a ``DataSources`` for CFX files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# **a) ``.res`` result file** — pass the result file path directly.

ds_41 = dpf.DataSources(result_path=result_file_path_41)

###############################################################################
# **b) ``.cas.cff`` / ``.dat.cff`` result files** — use
# :func:`set_result_file_path()<ansys.dpf.core.data_sources.DataSources.set_result_file_path>`
# and
# :func:`add_file_path()<ansys.dpf.core.data_sources.DataSources.add_file_path>`
# with the first extension key explicitly.

ds_42 = dpf.DataSources()
ds_42.set_result_file_path(filepath=result_file_path_42["cas"], key="cas")
ds_42.add_file_path(filepath=result_file_path_42["dat"], key="dat")

###############################################################################
# Use a ``Model`` for CFX files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

model_41 = dpf.Model(data_sources=result_file_path_41)
model_42 = dpf.Model(data_sources=ds_41)
model_43 = dpf.Model(data_sources=ds_42)
