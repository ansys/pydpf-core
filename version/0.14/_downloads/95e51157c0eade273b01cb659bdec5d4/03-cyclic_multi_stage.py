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
.. _ref_multi_stage_cyclic:

Multi-stage cyclic symmetry example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to expand the mesh and results from a
multi-stage cyclic analysis.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create the model and display the state of the result.
cyc = examples.download_multi_stage_cyclic_result()
model = dpf.Model(cyc)
print(model)

###############################################################################
# Expand displacement results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This example expands displacement results, by default on all
# nodes and the first time step. Note that the displacements are expanded using
# the :func:`read_cyclic
# <ansys.dpf.core.operators.mesh.mesh_provider.InputsMeshProvider.read_cyclic>`
# property with 2 as an argument (1 would ignore the cyclic symmetry).

# Create displacement cyclic operator
u_cyc = model.results.displacement()
u_cyc.inputs.read_cyclic(2)

# expand the displacements and get a total deformation
nrm = dpf.operators.math.norm_fc()
nrm.inputs.connect(u_cyc.outputs)
fields = nrm.outputs.fields_container()

# # get the expanded mesh
mesh_provider = model.metadata.mesh_provider
mesh_provider.inputs.read_cyclic(2)
mesh = mesh_provider.outputs.mesh()

# # plot the expanded result on the expanded mesh
mesh.plot(fields)

###############################################################################
# Expand stresses at a given time step
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# define stress expansion operator and request stresses at time set = 3
s_cyc = model.results.stress()
s_cyc.inputs.read_cyclic(2)
s_cyc.inputs.time_scoping.connect([3])

# request the results averaged on the nodes
s_cyc.inputs.requested_location.connect(dpf.locations.nodal)

# request equivalent von mises operator and connect it to stress
# operator
eqv = dpf.operators.invariant.von_mises_eqv_fc(s_cyc)

# expand the results and get stress eqv
fields = eqv.outputs.fields_container()

# plot the expanded result on the expanded mesh
mesh.plot(fields)
