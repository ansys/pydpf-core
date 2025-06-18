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

"""
.. _plotting_scopings:

Review of available plotting commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example show how to plot scopings with a mesh location.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# Plot the bare mesh of a model
model = dpf.Model(examples.download_cfx_mixing_elbow())

mesh = model.metadata.meshed_region

node_scoping_1 = dpf.Scoping(location=dpf.locations.nodal, ids=mesh.nodes.scoping.ids[0:100])
node_scoping_2 = dpf.Scoping(location=dpf.locations.nodal, ids=mesh.nodes.scoping.ids[300:400])

node_sc = dpf.ScopingsContainer()
node_sc.add_label(label="scoping", default_value=1)
node_sc.add_scoping(label_space={"scoping": 1}, scoping=node_scoping_1)
node_sc.add_scoping(label_space={"scoping": 2}, scoping=node_scoping_2)

# node_sc.plot(mesh=mesh, show_mesh=True)
# exit()
# node_scoping.plot(mesh=mesh, color="red")

element_scoping_1 = dpf.Scoping(
    location=dpf.locations.elemental, ids=mesh.elements.scoping.ids[0:100]
)
element_scoping_2 = dpf.Scoping(
    location=dpf.locations.elemental, ids=mesh.elements.scoping.ids[300:400]
)
element_sc = dpf.ScopingsContainer()
element_sc.add_label(label="scoping", default_value=1)
element_sc.add_scoping(label_space={"scoping": 1}, scoping=element_scoping_1)
element_sc.add_scoping(label_space={"scoping": 2}, scoping=element_scoping_2)

element_sc.plot(mesh=mesh, show_mesh=True)
# element_scoping.plot(mesh=mesh, color="green")


# from ansys.dpf.core.plotter import DpfPlotter
#
# plt = DpfPlotter()
# plt.add_scoping(node_scoping, mesh, show_mesh=True, color="red")
# plt.add_scoping(element_scoping, mesh, color="green")
# plt.show_figure()
#
# faces_scoping = dpf.Scoping(
#     location=dpf.locations.faces,
#     ids=mesh.faces.scoping.ids[0:100]
# )
#
# faces_scoping.plot(mesh=mesh, color="orange")
