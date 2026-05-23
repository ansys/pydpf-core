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

# _order: 7
"""
.. _ref_tutorials_import_data_cyclic_expansion:

Understand cyclic expansion of results
=======================================

:bdg-mapdl:`MAPDL`

Learn how DPF handles cyclic symmetry data and the different cyclic expansion modes.

When a model possesses cyclic symmetry, only one sector (the base sector) is solved.
DPF can read these results in different ways depending on the ``read_cyclic`` option
passed to a result operator. This tutorial demonstrates the four modes available
(``0``, ``1``, ``2``, ``3``) and shows how to perform phase sweeping on the expanded
results.
"""
###############################################################################
# Import modules and load the model
# ----------------------------------
#
# Import the required modules and create a |Model| from the built-in cyclic
# symmetry example file.

# Import the ansys.dpf.core module
from ansys.dpf import core as dpf

# Import the examples module
from ansys.dpf.core import examples

# Get the path to the cyclic result file
result_url = examples.download_modal_cyclic_complex()

# Create the Model
my_model = dpf.Model(data_sources=result_url)
print(my_model)

###############################################################################
# Explore the cyclic metadata
# ----------------------------
#
# A cyclic model exposes a
# :class:`CyclicSupport<ansys.dpf.core.cyclic_support.CyclicSupport>` that
# provides the number of sectors, node counts on the base sector, and the
# mapping between low and high boundary nodes.
#
# The |TimeFreqSupport| describes how solution sets map to harmonic indices and
# mode numbers.

# Get the TimeFreqSupport. In this model we have a damped, cyclic, modal analysis.
# Therefore, mode shapes are complex. The model spans 45º, therefore there are 8
# sectors and harmonic indices range from 0 to 4. The MAPDL analysis has been run
# ensuring that we extract 4 cyclic modes per harmonic index and all harmonic
# indices, this means 5*4 = 20 solution sets, so 10 real-imaginary combinations.
# In the print of the TimeFreqSupport we can see the 20 solution sets, and by default
# only the imaginary part of the frequency is printed. Each LoadStep is a harmonic
# index and each substep represents a cyclic mode for each one of them. For both
# harmonic indices 0 and 4, modes are standalone, whereas for the intermediate
# indices modes come in pairs.
tfs = my_model.metadata.time_freq_support
print(tfs)

###############################################################################
# Get the CyclicSupport from the ResultInfo. The CyclicSupport allows to understand
# the cyclic information of the model. We can see that we have only 1 stage with 8
# sectors (45º), 3657 nodes on each sector and high/low boundaries with 217 nodes.

cyc_sup = my_model.metadata.result_info.cyclic_support
print(cyc_sup)

# Print the number of stages and sectors
print(f"Number of stages: {cyc_sup.num_stages}")
print(f"Number of sectors (stage 0): {cyc_sup.num_sectors(stage_num=0)}")

# Print the number of boundary nodes (low-high map)
low_high = cyc_sup.low_high_map(stage_num=0)
print(f"Number of boundary nodes: {len(low_high.scoping)}")

###############################################################################
# Read cyclic mode 0 - ignore cyclic symmetry
# ---------------------------------------------
#
# With ``read_cyclic=0``, cyclic symmetry is completely ignored. DPF reads the
# base and duplicate sector data together into a single |Field| per solution set.
# Each Field contains data for all nodes stored in the file (base + duplicate
# sector, hence each Field has information for 3657*2 = 7314 nodes). Results are
# extracted at all solution sets. As the solutions are complex, and the information
# in the time scoping pin represents a cumulative id, if we want to read all we
# need to pass 1, 2, ... 20/2 ids.

# Create the displacement X operator
disp_op = dpf.operators.result.displacement_X()
disp_op.inputs.streams_container.connect(my_model.metadata.streams_provider)
disp_op.inputs.read_cyclic.connect(0)
disp_op.inputs.time_scoping.connect(list(range(1, len(tfs.time_frequencies) // 2 + 1)))
disp_rc0 = disp_op.outputs.fields_container()

print("read_cyclic=0:")
print(disp_rc0)

###############################################################################
# Read cyclic mode 1 - read as cyclic without expansion (default)
# ----------------------------------------------------------------
#
# With ``read_cyclic=1`` (the default), DPF reads the data as cyclic and splits
# results into base sector (``base_sector=1``) and duplicate sector
# (``base_sector=0``) Fields, hence, each Field has 3657 nodes. Harmonic indices
# without a duplicate sector (e.g., first HI = 0) only have the base sector Field,
# we have then 10*2*2 - 2*2*2 = 32 Fields (we lack the 8 combinations between
# base_sector = 0 and time = 1,2,3,4.

# Set read_cyclic to 1
disp_op.inputs.read_cyclic.connect(1)
disp_rc1 = disp_op.outputs.fields_container()

print("read_cyclic=1:")
print(disp_rc1)

###############################################################################
# Read cyclic mode 2 - expand without merging stages
# ----------------------------------------------------
#
# With ``read_cyclic=2``, DPF performs the full cyclic expansion. The result
# Fields now contain the data for all sectors assembled into the full 360-degree
# model. Stages are kept separate (relevant for multi-stage models). In this
# case we obtain 10*2 Fields after collapsing the base_sector label. The base
# sector has 3657 nodes, and the low/high boundaries have 217 nodes, therefore
# each field     has 3657 + 6*(3657 - 217) + (3657 - 2*217) = 27520 nodes.

# Set read_cyclic to 2
disp_op.inputs.read_cyclic.connect(2)
disp_rc2 = disp_op.outputs.fields_container()

print("read_cyclic=2:")
print(disp_rc2)

###############################################################################
# Read cyclic mode 3 - expand and merge stages
# ----------------------------------------------
#
# With ``read_cyclic=3``, the cyclic expansion is done and all stages are merged
# into a single mesh/result. For single-stage models as this one, this produces
# the same output as ``read_cyclic=2``.

# Set read_cyclic to 3
disp_op.inputs.read_cyclic.connect(3)
disp_rc3 = disp_op.outputs.fields_container()

print("read_cyclic=3:")
print(disp_rc3)

###############################################################################
# Compare Field sizes across modes
# ----------------------------------
#
# The following comparison shows how the number of entities grows with each
# expansion mode.

print(f"read_cyclic=0, first field entities: {len(disp_rc0[0])}")
print(f"read_cyclic=1, first field entities: {len(disp_rc1[0])}")
print(f"read_cyclic=2, first field entities: {len(disp_rc2[0])}")
print(f"read_cyclic=3, first field entities: {len(disp_rc3[0])}")

###############################################################################
# Phase sweeping on expanded results
# ------------------------------------
#
# For complex mode shapes (modal cyclic analysis), you can perform a phase sweep
# to obtain results at any phase angle. The expression used is:
#
# .. math::
#
#    \text{field\_out} = \text{real\_field} \cdot \cos(\theta)
#    - \text{imaginary\_field} \cdot \sin(\theta)
#
# The ``sweeping_phase_fc`` operator applies this to a |FieldsContainer| that
# contains paired real and imaginary Fields (identified by the ``complex`` label).
#
# A sweep at :math:`\theta = 0º` recovers the real part, while
# :math:`\theta = -90º` recovers the imaginary part.

# Create the sweeping_phase_fc operator
sweep_op = dpf.operators.math.sweeping_phase_fc()
sweep_op.inputs.fields_container.connect(disp_rc2)
sweep_op.inputs.angle.connect(0.0)
sweep_op.inputs.unit_name.connect("deg")

# Evaluate at 0 degrees (real part)
disp_sweep_0 = sweep_op.outputs.fields_container()
print("Phase sweep at 0 degrees:")
print(disp_sweep_0)

###############################################################################
# Sweep at -90 degrees to recover the imaginary part.

sweep_op.inputs.angle.connect(-90.0)
disp_sweep_90 = sweep_op.outputs.fields_container()
print("Phase sweep at -90 degrees:")
print(disp_sweep_90)

###############################################################################
# Visualize expanded results
# ---------------------------
#
# To visualize the expanded displacement, obtain the expanded mesh by setting
# ``read_cyclic=2`` on the mesh provider. Then plot the first expanded mode
# shape on the full 360-degree mesh.

# Get the expanded mesh
mesh_provider = my_model.metadata.mesh_provider
mesh_provider.inputs.read_cyclic(2)
expanded_mesh = mesh_provider.outputs.mesh()

# Plot the first mode (real part) on the expanded mesh
expanded_mesh.plot(disp_rc2[0])

###############################################################################
# Plot a phase-swept result
# ---------------------------
#
# Plot the first mode shape after sweeping at 45 degrees.

sweep_op.inputs.angle.connect(45.0)
disp_sweep_45 = sweep_op.outputs.fields_container()

expanded_mesh.plot(disp_sweep_45[0])
