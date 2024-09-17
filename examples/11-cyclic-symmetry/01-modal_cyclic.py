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

# noqa: D400
"""
.. _ref_basic_cyclic:

Expand mesh and results for modal cyclic symmetry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows a modal cyclic symmetry model with mesh and results expansions.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create the model and display the state of the result.
model = dpf.Model(examples.find_simple_cyclic())
print(model)

###############################################################################
# Expand displacement results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This example expands displacement results, by default on all
# nodes and the first time step. Note that the displacements are expanded using
# the :func:`read_cyclic
# <ansys.dpf.core.operators.mesh.mesh_provider.InputsMeshProvider.read_cyclic>`
# property with 2 as an argument (1 does not perform expansion of the cyclic symmetry).

# Create displacement cyclic operator
u_cyc = model.results.displacement()
u_cyc.inputs.read_cyclic(2)

# expand the displacements
fields = u_cyc.outputs.fields_container()

# # get the expanded mesh
mesh_provider = model.metadata.mesh_provider
mesh_provider.inputs.read_cyclic(2)
mesh = mesh_provider.outputs.mesh()

# plot the expanded result on the expanded mesh
mesh.plot(fields[0])

###############################################################################
# Expand stresses at a given time step
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# define stress expansion operator and request stresses at time set = 8
scyc_op = model.results.stress()
scyc_op.inputs.read_cyclic(2)
scyc_op.inputs.time_scoping.connect([8])

# request the results averaged on the nodes
scyc_op.inputs.requested_location.connect(dpf.locations.nodal)

# request equivalent von mises operator and connect it to stress operator
eqv = dpf.operators.invariant.von_mises_eqv_fc(scyc_op)

# expand the results and get stress eqv
fields = eqv.outputs.fields_container()

# plot the expanded result on the expanded mesh
# mesh.plot(fields[0])


###############################################################################
# Expand stresses at given sectors
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# define stress expansion operator and request stresses at time set = 8
# request the results averaged on the nodes
# request results on sectors 1, 3 and 5
scyc_op = dpf.operators.result.cyclic_expanded_stress(
    streams_container=model.metadata.streams_provider,
    time_scoping=[8],
    requested_location=dpf.locations.nodal,
    sectors_to_expand=[1, 3, 5],
)

# extract Sx (use component selector and select the first component)
comp_sel = dpf.operators.logic.component_selector_fc(scyc_op, 0)

# expand the displacements and get the results
fields = comp_sel.outputs.fields_container()

# plot the expanded result on the expanded mesh
# mesh.plot(fields[0])


###############################################################################
# Expand stresses and average to elemental location
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# define stress expansion operator and request stresses at time set = 8
scyc_op = dpf.operators.result.cyclic_expanded_stress(
    streams_container=model.metadata.streams_provider,
    time_scoping=[8],
    sectors_to_expand=[1, 3, 5],
    bool_rotate_to_global=False,
)

# request to elemental averaging operator
to_elemental = dpf.operators.averaging.to_elemental_fc(scyc_op)

# extract Sy (use component selector and select the component 1)
comp_sel = dpf.operators.logic.component_selector_fc(to_elemental, 1)

# expand the displacements and get the results
fields = comp_sel.outputs.fields_container()

# # plot the expanded result on the expanded mesh
mesh.plot(fields)
